
from django.contrib import admin
from django.urls import path
from  main.views import(post_detail,post_list, category_detail,category_list,post_create,post_edit,post_delete,)
from  account.views import(register,login,logout,activate)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('categories/', category_list, name='category_list'),
    path('category/<int:pk>/', category_detail, name='category_detail'),
    path('post/create/', post_create, name='post_create'),  
    path('post/edit/<int:pk>/', post_edit, name='post_edit'),  
    path('post/delete/<int:pk>/', post_delete, name='post_delete'),
    path('activate/', activate, name='activate'),

    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),




]
