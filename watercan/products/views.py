# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from models import Product, ProductDetails
from serializers import ProductSerializer, ProductDetailsSerializer
from django.db import transaction
import traceback
from .dbutils import DBHandler
from django.core.files import File
import base64

class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Product.objects.all()
        response = []
        if queryset:
            for query in queryset:
                response.append({'id':query.id, 'name':query.name})
        return Response(response, status=status.HTTP_200_OK)

    def create(self, request):

        try:
            # if not request.user.groups.filter(name__in=['Admin']).exists():
            #     return Response({'message': 'This user is not allowed to perform this action'}, status=status.HTTP_403_FORBIDDEN)
            with transaction.atomic():
                data = request.data
                product = DBHandler.process_products(data, request.user)
                serializedProduct = ProductSerializer(product)
                _response = Response(data=serializedProduct.data, status=status.HTTP_200_OK)
                return _response
        except Exception as exp:
            return Response({'message': exp.message or ', '.join(exp.messages)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

class ProductDetailsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = None
        query = None
        pk = self.request.query_params.get('pk') or None
        print 'In view : ', pk
        if pk in ['undefined',None]:
            queryset = ProductDetails.objects.all()
        else:
            query = ProductDetails.objects.get(pk=pk)
        response = []
        if queryset:
            for query in queryset:
                #TODO: Below Implementation is correct and will be uncomment later
                # f = open(query.image.path, 'rb')
                # image = File(f)
                # data = base64.b64encode(image.read())
                # f.close()
                response.append({'id':query.id, 'product':query.product.name, 'category':query.category, 'price':query.price, 'description':query.description, 'rating':query.rating, 'availability':query.availability, 'image_name':query.image.path.split('/')[-1]})
        else:
            response.append({'id':query.id, 'product':query.product.name, 'category':query.category, 'price':query.price, 'description':query.description, 'rating':query.rating, 'availability':query.availability, 'image_name':query.image.path.split('/')[-1]})

        return Response(response, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            # if not request.user.groups.filter(name__in=['Admin']).exists():
            #     return Response({'message': 'This user is not allowed to perform this action'}, status=status.HTTP_403_FORBIDDEN)
            with transaction.atomic():
                data = request.data
                product = DBHandler.process_product_details(data, request.user)
                serializedProductDetails = ProductDetailsSerializer(product)
                _response = Response(data=serializedProductDetails.data, status=status.HTTP_200_OK)
                return _response
        except Exception as exp:
            traceback.print_exc()
            return Response({'message': exp.message or ', '.join(exp.messages)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        print 'In retrieve'

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
