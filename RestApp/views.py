from django.shortcuts import render
from django.http import JsonResponse
from .models import market
from .serializers import marketserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
# Create your views here.
def marketls(request):
    if request.method =='GET':
        markets=market.objects.all()
        serializer=marketserializer(markets,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        serializer=marketserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)