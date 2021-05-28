from django.views import generic
from .serializers import exportSerializers
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here.
from .models import classificationModel
import datetime
from django.utils import timezone
from django_q.tasks import async_task
import base64
from django.core.files.base import ContentFile


class getCount(APIView):
    def get(self, request):
        return Response({"status": "semoga bangkit"})

class listTitle(generics.ListAPIView):
    serializer_class = exportSerializers

    def get_queryset(self):
        query = classificationModel.objects.all().order_by('-id')
        return query

class dariAndroid(APIView):
    def post(self, request):
        data = request.data
        # ketika key = judul
        judul = data['judul']
        location = data['location']
        image = data['image']

        # if disini

            # classification = classificationModel(
            #     judul = judul,
            #     location = location,
            #     )
            # 
            # file_name = "'myphoto" + ".jpeg"
            # classification.image.save(file_name, imgdata, save=True)
            # classification.save()
        return Response({"status" : "Sudah Bangkit"})