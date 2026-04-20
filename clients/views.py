from django.shortcuts import render
from . models import Clients
from . serializers import ClientSerializers,UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.status import HTTP_201_CREATED,\
HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
# Create your views here.
@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token':token.key},status = HTTP_201_CREATED)
    return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def getclients(request):
    if request.method == 'GET':
        clients = Clients.objects.all()
        serializer = ClientSerializers(clients,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClientSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)  