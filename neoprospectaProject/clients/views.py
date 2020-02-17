from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseRedirect, Http404
from django.core.serializers import serialize
from clients.serializer import ClientSerializers
from clients.models import Client
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_402_PAYMENT_REQUIRED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_301_MOVED_PERMANENTLY,
    HTTP_302_FOUND,
    HTTP_307_TEMPORARY_REDIRECT,
    HTTP_308_PERMANENT_REDIRECT,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.forms.models import model_to_dict
from django.db.models import Q
import json,sys

# Create your views here.

class ClientsView(APIView):
    '''
    '''
    def get(self, request):
        try:
            if request.GET.__contains__('id') or request.GET.__contains__('age') or request.GET.__contains__('name') or request.GET.__contains__('city'):
                query_id = request.GET.get('id',False)
                query_name = request.GET.get('name',False)
                query_age = request.GET.get('age',False)
                query_city = request.GET.get('city',False)
                client_query = None
                if query_id:
                    client_query = Client.objects.filter(id__in=query_id.split(','))
                if query_name:
                    if client_query:
                        client_query = client_query.filter(name__in=query_name.split(','))
                    else:
                        client_query = Client.objects.filter(name__in=query_name.split(','))
                if query_age:
                    if client_query:
                        client_query = client_query.filter(age__in=query_age.split(','))
                    else:
                        client_query = Client.objects.filter(age__in=query_age.split(','))
                if query_city:
                    if client_query:
                        client_query = client_query.filter(city__in=query_city.split(','))
                    else:
                        client_query = Client.objects.filter(city__in=query_city.split(','))
            else:
                client_query = Client.objects.all()
            if request.GET.__contains__('order_by'):
                client_query = client_query.order_by(request.GET['order_by'])

            paginator = PageNumberPagination()
            paginator.page_size = 10
            result_page = paginator.paginate_queryset(client_query, request)
            serialized = ClientSerializers(result_page,many=True)
            response = paginator.get_paginated_response(serialized.data)
        except Exception as e:
            data = {
            'status':'error',
            'error': str(e)
            }
            response = Response(data)
        return response

    def put(self, request):
        try:
            id = request.data.get('id', None)
            client = get_object_or_404(Client, pk=id)
            serialized = ClientSerializers(client,data = request.data)
            if serialized.is_valid():
                serialized.save()
                data = {
                'status': 'success',
                'client': serialized.data
                }
                response = Response(data, status=HTTP_200_OK)
            else:
                data = {
                'status': 'error',
                'error': serialized.errors
                }
                response = Response(data)
        except Exception as e:
            data = {
            'status':'error',
            'error': str(e)
            }
            response = Response(data)
        return response

class ClientView(APIView):
    '''
    '''
    def get(self, request, id):
        try:
            client = get_object_or_404(Client, pk=id)
            serialized = ClientSerializers(client)
            data = {
            'status':'success',
            'client': serialized.data
            }
            response = Response(data, status=HTTP_200_OK)
        except Exception as e:
            data = {
            'status':'error',
            'error': str(e)
            }
            response = Response(data)
        return response
