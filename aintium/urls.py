from django.urls import path

from . import views

urlpatterns = [
    path('user/list', views.UserList.as_view()),
    path('user/create', views.UserCreate.as_view()),
    path('ai/model/list', views.AiModelList.as_view()),
    path('request/list', views.RequestList.as_view()),
    path('bookmark/list', views.BookmarkList.as_view()),
    path('tag/list', views.TagList.as_view()),
]
