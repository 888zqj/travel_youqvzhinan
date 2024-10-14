import jwt
from django.http import JsonResponse
from django.conf import settings

def authenticate_request(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # 从 HTTP_HEADER 中获取 Bearer Token
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header is None:
            return JsonResponse({'error': '认证令牌缺失'}, status=401)

        try:
            # 提取 JWT
            token = auth_header.split(" ")[1]  # 假设格式为 "Bearer token"
            # 验证 JWT
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            kwargs['verify_payload'] = payload  # 将 payload 传递给视图函数
        except IndexError:
            return JsonResponse({'error': '无效的认证头部'}, status=401)
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': '令牌已过期'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': '无效的令牌'}, status=401)

        return view_func(request, *args, **kwargs)

    return _wrapped_view