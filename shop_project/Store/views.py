from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.db import IntegrityError
from .models import Category
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from rest_framework import generics
from .serializers import CategorySerializer

# Create your views here.

@csrf_exempt
# def category(request):
#     if request.method == 'GET':
#         categories = list(Category.objects.all().values())
#         categories0 = Category.objects.all().values()
#         json_data = serializers.serialize('json', Category.objects.all())
#         return JsonResponse({"categories":list(categories0)})
#         # return JsonResponse(categories, safe=False)
#         # return HttpResponse(categories)
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         category = Category(
#             title = title,
#         )
        
#         try:
#             category.save()
#         except IntegrityError:
#             return JsonResponse({'error':'true', 'message':'required field missing'}, status=201)
#         return JsonResponse(model_to_dict(category), status=201)

class cats(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class cat(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
