from rest_framework import serializers
from .models import *

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ['job', 'location']







