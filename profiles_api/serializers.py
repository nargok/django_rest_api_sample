from rest_framework import serializers

from . import  models
from . models import UserProfile

class HelloSerializer(serializers.Serializer):
  """Serializes a name field fot testing APIView"""

  name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.Serializer):
  """A serializer for user profile objects"""

  class Meta:
    model = UserProfile
    fields = ('id', 'email', 'name', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  id = serializers.IntegerField(read_only=True)
  email = serializers.EmailField(required=True)
  name = serializers.CharField(required=True, max_length=255)
  password = serializers.CharField(required=True, max_length=255, write_only=True)

  def create(self, validated_data):
    """Create and return a new user"""

    # TODO validated_dataに値が反映されない問題を解決する
    user = models.UserProfile(
      name=validated_data['name'],
      email=validated_data['email'],
    )

    user.set_password(validated_data['password'])
    user.save()

    return user

  def update(self, user, validated_data):
    user.email = validated_data.get('email', user.email)
    user.name = validated_data.get('name', user.name)

    return user
