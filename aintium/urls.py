from django.urls import path, include
from . import views


urlpatterns = [
    path('user/detail/<int:pk>', views.GetUserPk.as_view()),
    path('user/detail/', views.GetUser.as_view()),
    path('user/edit/<int:pk>', views.UserEdit.as_view()),
    path('user/create', views.UserCreate.as_view()),
    path('ai/model/list', views.AiModelList.as_view()),
    path('ai/model/detail/<int:pk>', views.GetAiModel.as_view()),
    path('request/list', views.RequestList.as_view()),
    path('bookmark/list', views.BookmarkList.as_view()),
    path('tag/list', views.TagList.as_view()),
    path('tag/detail/<int:pk>', views.GetTag.as_view()),
    path('image/list', views.ImageList.as_view()),
    path('rate/list', views.RateList.as_view())
]

