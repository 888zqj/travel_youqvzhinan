from rest_framework import serializers
from Server01.models import Attraction

class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = '__all__'  # 或者明确列出字段