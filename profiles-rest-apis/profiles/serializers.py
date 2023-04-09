from rest_framework import serializers

''' this file is used to convert json objects to python objects 
    so that it can be used be used when someone sends a POST or Update request
    for example.
'''
class HelloSerializer(serializers.Serializer):
    """"serialzes a name field for testing our api view, 
        it is very similar to django forms
    """
    name = serializers.CharField(max_length=20)
    