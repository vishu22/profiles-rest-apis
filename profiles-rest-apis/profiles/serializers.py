from rest_framework import serializers
from profiles.models import UserProfile,ProfileFeedItem

''' this file is used to convert json objects to python objects 
    so that it can be used be used when someone sends a POST or Update request
    for example.
'''


class HelloSerializer(serializers.Serializer):
    """"serialzes a name field for testing our api view, 
        it is very similar to django forms
    """
    name = serializers.CharField(max_length=20)


class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile object"""
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True},
                        'style': {'input_type': 'password'}
                        }

    def create(self, validated_data):
       user = UserProfile.objects.create_user(
           email=validated_data['email'],
           name=validated_data['name'],
           password=validated_data['password']
       )
       return user
    

class ProfileFeedItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileFeedItem
        fields = ("id","user_profile","status_text","created_on")
        extra_kwargs = {'user_profile':{'read_only':True}}