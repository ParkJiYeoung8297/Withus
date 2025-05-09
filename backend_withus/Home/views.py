from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import user
from .serializers import userSerializer

# Create your views here.


@api_view(['GET'])
def helloAPI(request):
    users = user.objects.all()
    if not users:
        default_data = [{'login_id': 'hello132', 'nickname': 'Hello'}]
        serializer = userSerializer(default_data, many=True)
        return Response(serializer.data)
    serializer = userSerializer(users, many=True)  #직렬화
    return Response(serializer.data)
