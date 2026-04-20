from django.shortcuts import render,get_object_or_404
from . models import Student
from.serializers import StudentSerilaizer
from rest_framework.response import Response
from rest_framework.decorators import api_view,\
authentication_classes,permission_classes
from rest_framework.status import HTTP_201_CREATED,\
HTTP_400_BAD_REQUEST,HTTP_200_OK,HTTP_204_NO_CONTENT
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.permissions import IsAdminUser
# Create your views here.
@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def show_students(request):
    if request.method =='GET':
        students = Student.objects.all()
        serializer = StudentSerilaizer(students,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def update_student(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == 'GET':
        serializer = StudentSerilaizer(student)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentSerilaizer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT)