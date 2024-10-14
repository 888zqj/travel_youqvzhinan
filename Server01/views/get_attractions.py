# get_attractions.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Attraction  # 注意相对路径
from ..serializers import AttractionSerializer  # 注意相对路径

@api_view(['GET'])
def get_attractions(request, city_name):
    if not city_name:
        return Response({"error": "City name is required."}, status=400)
    attractions = Attraction.objects.filter(city=city_name)
    serializer = AttractionSerializer(attractions, many=True)
    return Response(serializer.data)