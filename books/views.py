# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Publisher
from .serializers import *
import json
from django.core import serializers
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def publishers_list(request):
    if request.method == 'GET':
        publishers = Publisher.objects.all()
        # serializer = PublisherSerializer(publishers,context={'request': request} ,many=True)
        json_obj = serializers.serialize('json', list(publishers))
        return Response({'data': json.loads(json_obj)})
    if request.method == 'POST':
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def publisher_detail(request, pk):
    """
    Retrieve, update or delete a product instance.
    """
    try:
        publisher = Publisher.objects.get(pk=pk)
    except Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        json_obj = serializers.serialize('json', list(publisher))
        return Response({'data': json.loads(json_obj)})

    elif request.method == 'PUT':
        serializer = PublisherSerializer(publisher, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            json_obj = serializers.serialize('json', list(publisher))
            return Response({'data': json.loads(json_obj)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)