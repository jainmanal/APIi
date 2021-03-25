from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
from . models import  Schedules
from .serializers import EmployeeSerializer, ScheduleSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, DjangoModelPermissions, IsAuthenticatedOrReadOnly


# Create your views here.
# Admin User List View 
# Admin Can create Users, can assign Roles and permissions


class EmployeeViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

# Admin schedule view set 
# Admin can create schedules for employees and assign to them
# functionality is yet to be Implemented


class ScheduleView(ModelViewSet):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [DjangoModelPermissions]


class ScheduleListView(ModelViewSet):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set





# class UserSchedulesView(viewsets.ViewSet):
#     queryset = Schedules.objects.filter(user=request.user)
#     serializer_class = ScheduleSerializer
#     authentication_classes = SessionAuthentication






@api_view()
def schedule(request):
    # if request.user.is_authenticated:
    schedule = Schedules.objects.all()
    scheduleserial= ScheduleSerializer(schedule, many = True)
    user =  User.objects.all()
    userserial = EmployeeSerializer(user, many = True)
    data = JSONRenderer().render(scheduleserial.data)
    data1 = JSONRenderer().render(userserial.data)
    data = {'user':data, 'schedules':data1}
    return JsonResponse(data, safe= True)