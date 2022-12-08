from django.http import HttpResponse
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from MyAPI.serializers import PaisSerializador
from MyAPI.models import Pais


# @api_view(['GET', 'POST', 'PUT'])
# def pais(request):
#     print(request)
#
#     if request.method == 'GET':
#         paises = Pais.objects.all()
#         serializer = PaisSerializador(paises, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         print(request.data)
#         serializer = PaisSerializador(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Class needs APIView instead of View to work
# We also include format=None in the functions
class pais(APIView):
    def get(self, request, format=None):
        paises = Pais.objects.all()
        serializer = PaisSerializador(paises, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = PaisSerializador(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    if request.method == 'GET':
        return HttpResponse('Index')
