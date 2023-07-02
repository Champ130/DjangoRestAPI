from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
import json
from.models import Category

# Create your views here.
@api_view(['POST'])
def create_category(request):
    category_name = request.data.get('category')
    cat = Category.objects.create(name=category_name)
    cat_data = Category.objects.all().values()
    return Response({"data": cat_data})


@api_view(['DELETE'])
def delete_category(request,id):
    Category.objects.filter(id=id).delete()
    cat_data = Category.objects.all().values()
    return Response({"data": cat_data})




@api_view(['GET'])
def get_category(request):
    cat_data = Category.objects.all().values()
    return Response({"success":"category added","data2":cat_data})



# @api_view(["PATCH"])
# def update_category(request,id):
#     Category.objects.get(id=id)
#     cat_data = Category.objects.get(id=id)
#     with open ("update_category","w") as f:
#         json.dump(update_category,f)
#     return Response({"data": cat_data})



@api_view(['PUT'])
def updates_category(request,id):
    category = Category.objects.get(id=id)
    category.name =request.data.get('name')
    category.save()
    cat_data = Category.objects.all().values()
    return Response({'data':cat_data})


class CategoryView(APIView):
    def get(self,request):
        category =Category.objects.all().values()
        return Response({'category':category})
    
    def post(self,request):
        name=request.data.get('category-name')
        Category.objects.create(name=name)
        category =Category.objects.all().values()
        return Response({'category':category})