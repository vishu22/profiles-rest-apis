# Create your views here.
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import HelloSerializer
from rest_framework import status


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
        #serializers_class is a method to get the configured serialzer class in api view
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            return Response({'message':f"hello {name}"})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )
    
    def put(self,request,pk=None):
        """handeling updating an entire object"""

        return Response({'method':'PUT'})


    def patch(self,request,pk=None):
        """Handeling partial update request"""
        return Response({'message':'handeling partial update'})

    
    def delete(self,request,pk=None):
        """Deletes an object"""
        return Response({'message':'deletes an object'})


class HelloViewset(viewsets.ViewSet):
    """Test Api viewsets"""

    serializer_class = HelloSerializer

    def list(self,request):
        """return a hello message"""
        a_viewset = ["Uses actions (list, create, retrieve, update, partial_update)",
                     "automatically maps to urls using routers",
                     "provides more functionality with less code"]

        return Response({"message":a_viewset})
    
    def create(self,request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}"
            return Response({"message":message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def retrieve(self,request,pk=None):
        """Handel getting an pbject by pk or id"""
        return Response({'hello_method':'get'})

    
    def update(self,request, pk=None):
        """handle updating an object"""
        return Response({'hello_method':'put'})


    def partial_update(self,request, pk=None):
        """handle updating an object"""
        return Response({'hello_method':'patch'})

    def destroy(self,request, pk=None):
        """handle updating an object"""
        return Response({'hello_method':'delete'})