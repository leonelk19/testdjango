from django.shortcuts import render
from django.http import JsonResponse
from .models import market
from .serializers import marketserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
# Create your views here.
def marketls(request,format=None):
    if request.method =='GET':
        markets=market.objects.all()
        serializer=marketserializer(markets,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        serializer=marketserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET','PUT'])
# Create your views here.
def market_details(request,id,format=None):
    try:
        market.object.get(pk=id)
    except market.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer=marketserializer(market)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer=marketserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        market.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)