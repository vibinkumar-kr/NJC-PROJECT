from rest_framework import serializers
from .models import language
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = language
        fields =('id','name','paradigam')
