# Theory

1) what is DRF ?
-> Django REST framework is a powerful and flexible toolkit for building Web APIs.
-> DRF is a framework that help you quickly create restful APIs.


2) what is API ? (application programming interface)
->  An API is an software intermedialy that allow tow or more application talk to each other.


3) REST APIs ?
-> an API is developed using REST is known as RESTFUL API i.e. interface between user and application


4) difference between function and class based view ?
# function based view
1. we need to write no of urls in fbv
2. easy to implement, easy, understand
3. code redundency for large django project and hard to extend

# class based view
1. we need only one urls in cbv
2. hard to understand and complex to implement
3. the most significant advantage of CBV is inheritance. you can inherit another class.
4. you can extend CBV & you can add functionality using MIXIN


5) what is serializer ?
-> serializer are responsibile for converting complex data to native python datatype is called serializer.


6) what is modelserialiser ?
-> The modelserialiser class provide a shortcut that let you create serializer class with field that correspond to model field.


7) Importance of serializer ?
-> seralizer in DRF are important because they provide a way to conver data from one format to another.
   This is useful when you send data from your django application to another application


8) method of Aunthentication ?
1. Basic Aunthentication   ->  which involve sending username and password with each request.
2. Token Aunthentication   ->  which involve sending unique token with each request.
3. Session Aunthentication ->  which involve sending session id with each request.



9) Can you explain what token-based authentication is?
-> Token-based authentication is a form of authentication that uses a token – typically a string of characters – to identify a user.
   This token is then sent with each request, and the server can use it to verify the identity of the user.
   This is a popular form of authentication for APIs, as it can be easily implemented and is more secure than other methods, such as Basic Authentication.


10) What are viewsets in Django Rest Framework?
->  Viewsets are a way of grouping together related view functionality in Django Rest Framework. They provide a more concise and convenient way to write your views,
    and can help to keep your code more organized.


11) What’s the difference between a viewset and a view?
->  A viewset is a class that provides a set of actions that can be performed on a model. A view,
    on the other hand, is a single function that performs a specific action on a model.



12) Can you explain the main components of Django Rest Framework?
-> The main components of Django Rest Framework are the Request and Response objects, the View class, and the Serializer class.
-> The Request and Response objects are used to handle incoming and outgoing HTTP requests and responses, respectively.
-> The View class is used to define the logic for handling HTTP requests and responses.
-> The Serializer class is used to serialize and deserialize data.


13) What are routers in Django Rest Framework?
->  Routers are used in Django Rest Framework to automatically generate URLs for a given resource.
    This can be helpful if you have a large number of resources and don’t want to have to manually create URLs for each one.


14) What is pagination and why is it important?
->  Pagination is a way of handling large amounts of data by breaking it up into smaller, more manageable pieces


15) difference between API view and view set ?
->  API view allow us to define function that match standard http method like get, post, put, delete
->  API view allow us to define function that match to coomom api object like list, create, retrieve, update, destroy


16) ModelViewSet ?
-> the modelviewset is a special type of viewset that is automatically generated from model.
   this means that will already have all of the crud operation  (create, read, update, delete) set up.

##########################################################################################################################################################################
# virtual env

  1. pip install virtualenv
  2. virtualenv .env
  3. .env\Scripts\activate.bat

############################################################################################################################################################################
# practical

1. pip install djangorestframework
2. -> django-admin startproject tutorial .  
   -> cd tutorial
   -> django-admin startapp quickstart
3. INSTALLED APP=[
              rest_framework
              ]

#*********************************ModelViewSet********************************************
4. go to model.py
   #model.py

   from django.db import models
   class Stuent(models.Model):
      name=models.CharField(max_length=100)
      roll=models.IntegerField()
      city=models.CharField(max_length=100)
      
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py createsuperuser
      
8. create a serializer.py file in app
  # serializer.py
  from rest_framework import serializers
  from .models import Stuent
  class StudentSerializer(serializers.ModelSerializer):
     class Meta:
        model=Stuent
        fields=['id','name','roll','city']
 
9. # view.py
   from .models import stuent
   from .serializer import StudentSerializer
#  from rest_framework.filters import SearchFilter
#  from rest_framework.filters import OrderingFilter
   from rest_framework import viewsets
   class StudentViewSet(viewsets.ModelViewSet):
        queryset=Stuent.objects.all()
        serializer_class=StudentSerializer

         # filter_backends=[SearchFilter]
         # search_fields=['name','city']
  

        # filter_backends=[OrderingFilter]
        # ordering_fields=['name']


10. #admin.py
    from django.contrib import admin
    from .models import Stuent
    @admin.register(Stuent)
    class StudentAdmin(admin.ModelAdmin):
          list_display=['id','name','roll','city']


11. # urls.py
    from django.contrib import admin
    from django.urls import path,include
    from myapp import views
    from rest_framework.routers import DefaultRouter
    router=DefaultRouter()
    router.register('studentapi',views.StudentViewSet)
    urlpatterns = [
          path('admin/', admin.site.urls)
          path('',include(router.urls)
       ]

12. python manage.py runserver
#-------------------------------------------------------------------------------------------------------------------------------------

#********************************* Concrete View Class *****************************************
    
1. go to model.py
   #model.py

   from django.db import models
   class Stuent(models.Model):
      name=models.CharField(max_length=100)
      roll=models.IntegerField()
      city=models.CharField(max_length=100)
      
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py createsuperuser
      
5. create a serializer.py file in app
  # serializer.py
  from rest_framework import serializers
  from .models import Stuent
  class StudentSerializer(serializers.ModelSerializer):
     class Meta:
        model=Stuent
        fields=['id','name','roll','city']
 
6. # view.py
   from .models import stuent
   from .serializer import StudentSerializer
   from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
   class StudentListCreate(ListCreateAPIView):
       queryset=Stuent.objects.all()
       serializer_class=StudentSerializer

   class StudentRUD(RetrieveUpdateDestroyAPIView):
       queryset=Stuent.objects.all()
       serializer_class=StudentSerializer


7. #admin.py
    from django.contrib import admin
    from .models import Stuent
    @admin.register(Stuent)
    class StudentAdmin(admin.ModelAdmin):
          list_display=['id','name','roll','city']


8. # urls.py
    from django.contrib import admin
    from django.urls import path,include
    from myapp import views
    urlpatterns = [
          path('admin/', admin.site.urls)
          path('api', views.StudentListCreate.as_view()),
          path('api/<int:pk>', views.StudentRUD.as_view()),
       ]

9. python manage.py runserver

#--------------------------------------------------------------------------------------------------------------------------

#********************************* Generic API View Mixin *****************************************

1. go to model.py
   #model.py

   from django.db import models
   class Stuent(models.Model):
      name=models.CharField(max_length=100)
      roll=models.IntegerField()
      city=models.CharField(max_length=100)
      
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py createsuperuser
      
5. create a serializer.py file in app
  # serializer.py
  from rest_framework import serializers
  from .models import Stuent
  class StudentSerializer(serializers.ModelSerializer):
     class Meta:
        model=Stuent
        fields=['id','name','roll','city']
 
6. # view.py
   from .models import stuent
   from .serializer import StudentSerializer
   from rest_framework.generics import GenericAPIView
   from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin

   class Studentlc(GenericAPIView,ListModelMixin,CreateModelMixin):
        queryset=Stuent.objects.all()
        serializer_class=StudentSerializer

        def get(self,request,*arg,**kwarg):
             return self.list(request,*arg,**kwarg)

        def post(self,request,*arg,**kwarg):
             return self.create(request,*arg,**kwarg)

 
    class Studentrud(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
       queryset=Stuent.objects.all()
       serializer_class=StudentSerializer

       def get(self,request,*arg,**kwarg):
          return self.retrieve(request,*arg,**kwarg)

       def put(self,request,*arg,**kwarg):
          return self.update(request,*arg,**kwarg)


       def delete(self,request,*arg,**kwarg):
          return self.destroy(request,*arg,**kwarg)


7. #admin.py
    from django.contrib import admin
    from .models import Stuent
    @admin.register(Stuent)
    class StudentAdmin(admin.ModelAdmin):
          list_display=['id','name','roll','city']


8. # urls.py
    from django.contrib import admin
    from django.urls import path,include
    from myapp import views
    urlpatterns = [
          path('admin/', admin.site.urls)
          path('generic', views.Studentlc.as_view()),
          path('generic/<int:pk>', views.Studentrud.as_view()),
       ]

9. python manage.py runserver
#--------------------------------------------------------------------------------------------------------------------------------------------------------

#********************************* Aunthentication *****************************************


4. go to model.py
   #model.py

   from django.db import models
   class Stuent(models.Model):
      name=models.CharField(max_length=100)
      roll=models.IntegerField()
      city=models.CharField(max_length=100)
      
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py createsuperuser
      
8. create a serializer.py file in app
  # serializer.py
  from rest_framework import serializers
  from .models import Stuent
  class StudentSerializer(serializers.ModelSerializer):
     class Meta:
        model=Stuent
        fields=['id','name','roll','city']
 
9. # view.py
   from .models import stuent
   from .serializer import StudentSerializer
   from rest_framework import viewsets
   from rest_framework.authentication import BasicAuthentication,SessionAuthentication
   from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
   class StudentViewSet(viewsets.ModelViewSet):
        queryset=Stuent.objects.all()
        serializer_class=StudentSerializer
        # for Basic Aunthentication
        authentication_classes=[BasicAuthentication]
        permission_classes=[IsAuthenticated]
        permission_classes=[IsAdminUser]
        # for Session Aunthentication
        authentication_classes=[SessionAuthentication]
        permission_classes=[IsAuthenticated]
        permission_classes=[IsAdminUser]
        permission_classes=[IsAuthenticatedOrReadOnly]


10. #admin.py
    from django.contrib import admin
    from .models import Stuent
    @admin.register(Stuent)
    class StudentAdmin(admin.ModelAdmin):
          list_display=['id','name','roll','city']


11. # urls.py
    from django.contrib import admin
    from django.urls import path,include
    from myapp import views
    from rest_framework.routers import DefaultRouter
    router=DefaultRouter()
    router.register('studentapi',views.StudentViewSet)
    urlpatterns = [
          path('admin/', admin.site.urls)
          path('auth',include('rest_framework.urls',namespace='rest_frame_work')), # for session url
          path('',include(router.urls)
       ]

12. python manage.py runserver
#-----------------------------------------------------------------------------------------------------------------------------------------

#********************************* Token  *****************************************


INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
   ]

4. go to model.py
   #model.py

   from django.db import models
   class Stuent(models.Model):
      name=models.CharField(max_length=100)
      roll=models.IntegerField()
      city=models.CharField(max_length=100)
      
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py createsuperuser
      
8. create a serializer.py file in app
  # serializer.py
  from rest_framework import serializers
  from .models import Stuent
  class StudentSerializer(serializers.ModelSerializer):
     class Meta:
        model=Stuent
        fields=['id','name','roll','city']
 
9. # view.py
   from .models import stuent
   from .serializer import StudentSerializer
   from rest_framework import viewsets
   from rest_framework.authentication import BasicAuthentication,SessionAuthentication, TokenAunthentication
   from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
   class StudentViewSet(viewsets.ModelViewSet):
        queryset=Stuent.objects.all()
        serializer_class=StudentSerializer
        authentication_classes=[TokenAuthentication]


10. #admin.py
    from django.contrib import admin
    from .models import Stuent
    @admin.register(Stuent)
    class StudentAdmin(admin.ModelAdmin):
          list_display=['id','name','roll','city']


11. # urls.py
    from django.contrib import admin
    from django.urls import path,include
    from myapp import views
    from rest_framework.authtoken.views import obtain_auth_token

    from rest_framework.routers import DefaultRouter

    router=DefaultRouter()

    router.register('studentapi',views.StudentViewSet)

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('auth',include('rest_framework.urls',namespace='rest_frame_work')),
    #router,
        path('',include(router.urls)),
        path('gettoken/',obtain_auth_token)
        ]

12. python manage.py runserver
        # python manage.py def_create_token <username>

#-----------------------------------------------------------------------------------------------------------------------------------------

#****************************************************** Relation **********************************************************************


4. go to model.py
   #model.py
    from django.db import models

    class Singer(models.Model):
        name=models.CharField(max_length=100)
        gender=models.CharField(max_length=100)
     
        def __str__(self):
            return self.name

    class Song(models.Model):
        title=models.CharField(max_length=100)
        singer=models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='song')
        duration=models.IntegerField()
      
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py createsuperuser
      
8. create a serializer.py file in app
  # serializer.py
    from .models import Song,Singer
    from rest_framework import serializers
    class SongSerializer(serializers.ModelSerializer):
        class Meta:
            model=Song
            fields=['id','title','singer','duration']

    class SingerSerializer(serializers.ModelSerializer):
         song=SongSerializer(many=True,read_only=True)
         class Meta:       
            model=Singer
            fields=['id','name','gender','song']
 
9. # view.py
    import imp
    from django.shortcuts import render
    from .serializer import SingerSerializer,SongSerializer
    from rest_framework import viewsets
    from .models import Singer,Song
    # Create your views here.

    class SingerViewSet(viewsets.ModelViewSet):
        queryset=Singer.objects.all()
        serializer_class=SingerSerializer

    class SongViewSet(viewsets.ModelViewSet):
        queryset=Song.objects.all()
        serializer_class=SongSerializer


10. #admin.py
    from django.contrib import admin
    from .models import Singer,Song

    @admin.register(Singer)
    class SingerAdmin(admin.ModelAdmin):
        list_display=['id','name','gender']
        
    @admin.register(Song)
    class SongAdmin(admin.ModelAdmin):
        list_display=['id','title','singer','duration']


11. # urls.py
    from django.contrib import admin
    from django.urls import path,include
    from rest_framework.routers import DefaultRouter
    from myapp import views

    router=DefaultRouter()
    router.register('song',views.SongViewSet)
    router.register('sing',views.SingerViewSet)

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',include(router.urls))
    ]

12. python manage.py runserver
        # python manage.py def_create_token <username>
#---------------------------------------------------------------------------------------------------------------------------------------------------

#********************************** Function Based view **************************************************************

# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Stuent



@api_view(['GET','POST','PUT','DELETE'])   # api view
def student_api(request):
   if request.method=='GET':
      id=request.data.get('id')
      if id is not None:
        stu=Stuent.objects.get(id=id)           
        Serializer=StudentSerializer(stu)  # complex datatype to native datatype
        return Response(Serializer.data)   # python data to json

      stu=Stuent.objects.all()
      Serializer=StudentSerializer(stu,many=True)
      return Response(Serializer.data)

   if request.method=='POST':
      Serializer=StudentSerializer(data=request.data)
      if Serializer.is_valid():
        Serializer.save()
        return Response({'msg':'created'})


   if request.method=='PUT':
      id=request.data.get('id')
      stu=Stuent.objects.get(pk=id)
      Serializer=StudentSerializer(stu,data=request.data,partial=True)

      if Serializer.is_valid():
        Serializer.save()
        return Response({'msg':'updated'})



   if request.method=='DELETE':
      id=request.data.get('id')
      stu=Stuent.objects.get(pk=id)
      stu.delete()
 
      return Response({'msg':'deleted'})


# urls.py

    from django.contrib import admin
    from django.urls import path,include
    from myapp import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.student_api),
    ]
#---------------------------------------------------------------------------------------------------------------------------------------------------

#********************************** Class Based view **************************************************************

# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Stuent
from rest_framework.views import APIView


class StudentAPI(APIView):
   def get(self,request):
      id=request.data.get('id')
      if id is not None:
        stu=Stuent.objects.get(id=id)
        Serializer=StudentSerializer(stu)
        return Response(Serializer.data)

      stu=Stuent.objects.all()
      Serializer=StudentSerializer(stu,many=True)
      return Response(Serializer.data)


   def post(self,request):
      Serializer=StudentSerializer(data=request.data)
      if Serializer.is_valid():
        Serializer.save()
        return Response({'msg':'created'})
   

   def put(self,request):
      id=request.data.get('id')
      stu=Stuent.objects.get(pk=id)
      Serializer=StudentSerializer(stu,data=request.data,partial=True)

      if Serializer.is_valid():
        Serializer.save()
        return Response({'msg':'updated'})


   def delete(self,request):
      id=request.data.get('id')
      stu=Stuent.objects.get(pk=id)
      stu.delete()
 
      return Response({'msg':'deleted'})


# urls.py

    from django.contrib import admin
    from django.urls import path,include
    from myapp import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        ppath('cls', views.StudentAPI.as_view()),
    ]
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# HyperLinkedModelSerializers


# PAgination

     # setting.py

      REST_FRAMEWORK={
    'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE' : 2
     }










