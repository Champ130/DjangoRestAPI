from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def create_category(request):
    return Response({"sucess":"Category added Sucessfully"})