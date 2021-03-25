from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Schedules


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password','is_staff','is_superuser')


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = ('user','start_time','end_time','note')
        