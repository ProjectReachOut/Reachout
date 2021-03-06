"""Reachout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import app1.views as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.listUsers),
    path('admin/', admin.site.urls),
	path('test/',views.test,name='test'),
    path('listUsers/',views.listUsers),
    path('add_user/', views.add_user, name='add_user'),

	path('login/',views.login,name='login'),
    path('update_user_details/', views.update_user_details, name='update_user_details'),
    path('get_user_details/', views.get_user_details, name='get_user_details'),
    path('update_user_profile_picture/', views.update_user_profile_picture, name='update_user_profile_picture'),
    path('update_password/', views.update_password, name='update_password'),

	path('add_article/',views.add_article,name="add_article"),
    path('delete_article/',views.delete_article,name='delete_article'),
    path('delete_event/', views.delete_event, name='delete_event'),
	path('get_articles/',views.get_articles,name='get_articles'),
    path('get_my_articles/', views.get_my_articles, name='get_my_articles'),

	path('add_event/',views.add_event,name='add_event'),
    path('get_my_events/',views.get_my_events,name='get_my_events'),
    path('get_all_events/',views.get_all_events,name='get_all_events'),
    path('get_event_details/',views.get_event_details,name='get_event_details'),
    path('add_users_to_event/',views.add_users_to_event,name='add_users_to_event'),
    path('remove_users_from_event/',views.remove_users_from_event,name='remove_users_from_event'),

	path('all_users/',views.all_users,name='all_users'),
	path('get_event_investment/',views.get_event_investment,name="get_event_investment"),
    path('add_investment/',views.add_investment,name="add_investment"),
    path('authenticateUser/',views.authenticateUser,name="authenticateUser"),

    path('get_latest_item_ids/',views.get_latest_item_ids,name="get_latest_item_ids"),
    path('retrieve_articles/',views.retrieve_articles,name="retrieve_articles"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
