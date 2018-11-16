from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from rest_framework import status

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
