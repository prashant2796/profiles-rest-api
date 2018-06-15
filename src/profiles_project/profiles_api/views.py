from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions
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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class LoginViewSet(viewsets.ViewSet):
    """
    Checks email and password and returns auth token
    """
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """
        Use the ObtainAuthToken APIView to validate and create a token. 
        """

        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """
    Handles Creating, reading and updating profile feed items 
    """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """
        Sets the user profile to the logged in user.
        """
        serializer.save(user_profile = self.request.user)
