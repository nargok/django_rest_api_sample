from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from . import serializers
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import models
from . import permissions

class HelloApiView(APIView):
  """Test API View"""

  def get(self, request, format=None):
    """Returns a list of APIView freatuers"""

    serializer_class = serializers.HelloSerializer

    an_apiview = [
      'Uses HTTP methods as functions (get, post, patch, put, delte)',
      'Is simmilar to a traditional Django View',
      'Gives you the most control over your logic',
      'Is mapped manually to URLs',
    ]

    return Response({'message': 'Hello!', 'an_apiview': an_apiview})

  def post(self, request):
    """Creates a hello message with our name."""

    serializer = serializers.HelloSerializer(data=request.data)

    if serializer.is_valid():
      name = serializer.data.get('name')
      message = 'Hello {0}!'.format(name)
      return Response({'message': message})
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, rquest, pk=None):
    """Handles updateing an object."""

    return Response({"method": 'put'})

  def patch(self, rquest, pk=None):
    """Patch request, only updates fields privided in the request"""

    return Response({"method": 'patch'})

  def delete(self, rquest, pk=None):
    """Deletes adn object."""

    return Response({"method": 'delete'})

class HelloViewSet(viewsets.ViewSet):
  """Test API ViewSet"""

  def list(self, request):
    """Returns a hello message"""

    a_viewset = [
      'Uses action(list, create, retrieve, update, partial_update)',
      'Automatically maps to URLS using Routers',
      'Provides more functionality with less code',
    ]

    return Response({"message": "Hello!", "a_viewset": a_viewset})

  def create(self, request):
    """Create a new hello message"""

    serializer = serializers.HelloSerializer(date=request.data)

    if serializer.is_valid:
      name = serializer.data.get('name')
      message = "Hello {0}!".format(name)
      return Response({"message": message})
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def retrieve(self, request, pk=None):
    """Handles getting an object by its ID."""
    return Response({"http_method":"GET"})

  def update(self, request, pk=None):
    """Handles update an object."""
    return Response({"http_method": "PUT"})

  def partial_update(self, request, pk=None):
    """Handles updating part of an object."""
    return Response({"http_method": "PATCH"})

  def destroy(self, request, pk=None):
    """Handles deleting an object"""
    return Response({"http_method": "DELETE"})

class UserProfileViewSet(viewsets.ModelViewSet):
  """Handles creating and updating profiles"""

  queryset = models.UserProfile.objects.all()
  serializer_class = serializers.UserProfileSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.UpdateOwnProfile,)