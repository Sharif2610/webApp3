from django.shortcuts import render,get_object_or_404
from . models import Employees
from . serializers import EmployeesSerializers,UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,\
authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework .status import HTTP_201_CREATED,\
HTTP_400_BAD_REQUEST,HTTP_200_OK ,HTTP_204_NO_CONTENT
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.permissions import IsAdminUser,\
IsAuthenticated
from rest_framework.authtoken.models import Token
# Create your views here.
@api_view(['GET','POST'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([IsAuthenticated])
def show_employees(request):
    if request.method == 'GET':
        employee = Employees.objects.all()
        serializer = EmployeesSerializers(employee,many=True)
        return Response(serializer.data)
        """paginator = PageNumberPagination()
        paginator.page_size = 2
        employees = paginator.paginate_queryset(Employees.objects.all(),request)
        return paginator.get_paginated_response(EmployeesSerializers(employees,many=True).data)"""
        """paginator = PageNumberPagination()
        paginator.page_size = 2
        employees = paginator.paginate_queryset(Employees.objects.all(),request)
        return paginator.get_paginated_response(EmployeesSerializers(employees,many=True).data)"""
    elif request.method == 'POST':
        serializer = EmployeesSerializers(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([IsAuthenticated])
def update_employee(request,id):
    employees = get_object_or_404(Employees,id=id)
    if request.method == 'GET':
        serializers = EmployeesSerializers(employees)
        return Response(serializers.data)
    elif request.method == 'PUT':
        serializers = EmployeesSerializers(employees,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=HTTP_200_OK)
        return Response(serializers.errors,status=HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializers = EmployeesSerializers(employees,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=HTTP_200_OK)
        return Response(serializers.errors,status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employees.delete()
        return Response(status=HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def registeruser(request):
    serializer_obj = UserSerializer(data=request.data)
    if serializer_obj.is_valid() == True:
        uobj = serializer_obj.save()
        uobj.set_password(serializer_obj.validated_data['password'])
        uobj.save()
        Token.objects.create(user=uobj)
        return Response(status=HTTP_201_CREATED)
    return Response(serializer_obj.errors,status=HTTP_400_BAD_REQUEST)