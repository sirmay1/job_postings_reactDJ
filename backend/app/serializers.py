from rest_framework import serializers
from .models import *

class JobsSerializer(serializers.Serializer):
    class Meta:
        model = Jobs
        fields = ['job', 'location']
