from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models
# Create your views here.
class HelloApiView(APIView):
    """" Test API view """
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features. """

        an_apiview = [
            'uses HTTP methods as a function (get,post patch,put,delete)',
            'It is similar to a traditional Django view',
            'Gives you more control over your logic',
            'Its mapped manually to URLs',

        ]

        return Response({'message':'hello!','an_apiview':an_apiview})

    def post(self,request):
        """ create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handles updating an object"""
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """ patch request,only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """Deletes the objects """
        return Response({'method':'delete' })

class HelloViewSet(viewsets.ViewSet):
    """ test api view set"""

    def list(self,request):
        """return a hello message"""

        a_viewset=[
            'uses action (list,create,retrieve,update,partial_update)',
            'Automatically maps to urls using routers',
            'provide more functionality with less code',
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ handles creating , reading and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.Userprofile.objects.all()
