from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class HelloApiView(APIView):
    """" Test API view """

    def get(self,request,format=None):
        """Returns a list of APIView features. """

        an_apiview = [
            'uses HTTP methods as a function (get,post patch,put,delete)',
            'It is similar to a traditional Django view',
            'Gives you more control over your logic',
            'Its mapped manually to URLs',

        ]

        return Response({'message':'hello!','an_apiview':an_apiview})
