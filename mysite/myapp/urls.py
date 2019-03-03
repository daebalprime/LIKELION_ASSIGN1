from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('', views.blog, name="blog"),
    path('<int:blog_id>/', views.detail, name="detail"),
    # <type:변수이름>, 이 변수이름은 argument로 views에 전달한다. path converterㅍ
    path('create/', views.create, name='create'),
    path('newblog/', views.blogpost, name= "newblog") ,
]
