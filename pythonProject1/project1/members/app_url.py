from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.index,name='index'),
    path('world',views.demo1,name='demo1'),
    path('add',views.add1,name='add'),
    path('sum1',views.sum,name='sum'),
    path('bg', views.color,name='color'),
    path('index', views.index1, name='index'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('product', views.product, name='product'),
    path('register', views.register, name='register'),
    path('res', views.res, name='res'),
    path('additm',views.additm,name='additm'),
    path('logout',views.logout,name='logout'),
    path('',views.mainpg,name='mainpg'),
    path('movie/<int:id>/',views.detail,name="detail"),
    path('display/<int:id>/',views.display,name='display'),
    path('adding',views.adding,name='adding'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('session',views.session,name='session'),
    path('get_session',views.get_session, name='get_session'),
    path('cbvhome',views.movielistview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.detail_view.as_view(), name='cbvdetail'), #pk=primary key
    path('cbvupdate/<int:pk>/',views.updateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.deleteview.as_view(),name='cbvdelete'),
    path('mail',views.mail, name='mail'),
    # path('mail1', views.mail1, name='mail1'),
    path('mail2',views.mail2, name='mail2'),


]