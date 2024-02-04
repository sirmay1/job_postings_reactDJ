#from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

class JobsView(APIView):
    def get(self, request):#request isn't being used? (10:25)?
        output = [{'job':output.job,
                   'location':output.location}
                  for output in Jobs.objects.all()]
        return Response(output)


    def post(self, request):
        serializer = JobsSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
        return Response(serializer.data)


# Create yur views here.
