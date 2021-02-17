from django.shortcuts import render
from rest_framework import viewsets
from .models import language
from .serializers import LanguageSerializer
from rest_framework.response import Response
from rest_framework import status


class LanguageView(viewsets.ModelViewSet):
    queryset = language.objects.all()
    serializer_class = LanguageSerializer

    def get (self, request):
        products=language.objects.all ()
        serializer = LanguageSerializer(products, many=True)
        return Response(serializer.data)

    def post (self, request):

        serializer= LanguageSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)