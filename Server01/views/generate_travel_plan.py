import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Server01.decorators import authenticate_request  # 导入自定义的装饰器

@csrf_exempt  # 允许跨域请求，开发环境下可用，生产环境需小心使用
@authenticate_request
def generate_travel_plan(request, verify_payload):
    if request.method == 'POST':
        try:
            # 从前端请求中提取数据
            data = json.loads(request.body)  # 从请求中获取 JSON 数据
            name = data.get('name')
            region = data.get('region')
            date1 = data.get('date1')
            date2 = data.get('date2')

            # 获取 Bot 在线信息
            online_info_url = 'https://www.coze.cn/s/i6xAUyWL/'
            headers = {
                'Authorization': 'Bearer pat_dIjNuMKvX4AZU2MOVRajCkpKwHVjaGLsAA003LlOkEvM8P4qrphJJKoMc4SsyNWv',# 使用提供的令牌

                "Content-Type": "application/json",
                "Accept": "*/*",
                "Host": "api.coze.cn",
                "Connection": "keep-alive"

            }
            online_info_response = requests.get(online_info_url, headers=headers)

            # 检查获取在线信息的响应
            if online_info_response.status_code != 200:
                return JsonResponse({'error': '无法获取在线信息', 'status_code': online_info_response.status_code}, status=500)



            api_url = 'https://api.coze.cn/open_api/v2/chat'  # 将 URL 替换为正确的 API 地址
            payload = {


                "conversation_id": "123",
                'bot_id': '7421729097589719079',  # 使用相关 Bot ID
                'user_id': '2102261865',  # 使用合适的 User ID
                'stream': False,
                'auto_save_history': True,
                'additional_messages': [
                    {
                        'role': 'user',
                        'content': f'我想去{name}，人数为{region}，出发日期是{date1}，返回日期是{date2}',
                        'content_type': 'text'
                    }
                ]
            }
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer pat_dIjNuMKvX4AZU2MOVRajCkpKwHVjaGLsAA003LlOkEvM8P4qrphJJKoMc4SsyNWv' , # 替换为您的实际 token
                 "Content-Type": "application/json",
            "user":'2102261865',
            "Accept": "*/*",
            "Host": "api.coze.cn",
            "Connection": "keep-alive"
            }
            response = requests.post(api_url, headers=headers, json=payload)

            # 检查外部 API 的响应
            if response.status_code == 200:
                api_result = response.json()  # 获取外部 API 返回的数据
                return JsonResponse({'info': api_result, 'online_info': online_info_response.json()}, status=200)
            else:
                return JsonResponse({'error': '外部 API 异常', 'status_code': response.status_code}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({'error': '请求体格式不正确'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': '不支持的请求方法'}, status=405)