from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
  """Test API View"""

  def get(self, request, format=None):
    """Returns a list of APIView freatuers"""

    an_apiview = [
      'Uses HTTP methods as functions (get, post, patch, put, delte)',
      'Is simmilar to a traditional Django View',
      'Gives you the most control over your logic',
      'Is mapped manually to URLs',
    ]

    return Response({'message': 'Hello!', 'an_apiview': an_apiview})
