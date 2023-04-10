# Create your views here.
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import HelloSerializer, UserProfileSerializer,ProfileFeedItemSerializers
from rest_framework import status
from . models import UserProfile,ProfileFeedItem
from rest_framework.authentication import TokenAuthentication
from profiles import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class HelloAPiView(APIView):
    """test api view"""
    serializers_class = HelloSerializer

    def get(self, request, format=None):
        """returns a list of api view features"""
        an_apiview = [
            'uses get, post, put, patch, delete as functions',
            'is similar to traditional django view',
            'is mapped manually to urls',
            'gives you most control over application logic'
        ]
        return Response({'message': 'hello', 'an_apiview': an_apiview})
    # Response needs to have a dict or a list it coverts objs to JSON

    def post(self, request):
        # serializers_class is a method to get the configured serialzer class in api view
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            return Response({'message': f"hello {name}"})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """handeling updating an entire object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handeling partial update request"""
        return Response({'message': 'handeling partial update'})

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({'message': 'deletes an object'})


class HelloViewset(viewsets.ViewSet):
    """Test Api viewsets"""

    serializer_class = HelloSerializer

    def list(self, request):
        """return a hello message"""
        a_viewset = ["Uses actions (list, create, retrieve, update, partial_update)",
                     "automatically maps to urls using routers",
                     "provides more functionality with less code"]

        return Response({"message": a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handel getting an pbject by pk or id"""
        return Response({'hello_method': 'get'})

    def update(self, request, pk=None):
        """handle updating an object"""
        return Response({'hello_method': 'put'})

    def partial_update(self, request, pk=None):
        """handle updating an object"""
        return Response({'hello_method': 'patch'})

    def destroy(self, request, pk=None):
        """handle updating an object"""
        return Response({'hello_method': 'delete'})


class ProfilesViewSet(viewsets.ModelViewSet):
    """creating and updating viewset"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class =  ProfileFeedItemSerializers
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus,
                          IsAuthenticatedOrReadOnly,)

    
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
        # return super().perform_create(serializer)