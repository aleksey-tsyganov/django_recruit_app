from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('recruit_form/', views.RecruitCreateView.as_view(), name='recruit_form'),
    path('answer_form/<int:pk>/', views.answer_create, name='answer_form'),
    path('master/', views.MasterListView.as_view(), name='master_list'),
    path('master/<int:pk>/recruit_list/', views.RecruitListView.as_view(), name='recruit_list'),
    path('master/<int:pk>/recruit_list/<int:id>/', views.RecruitDetailView.as_view(), name='recruit_detail'),
    path('update/<int:pk>/', views.RecruitStatusUpdateView.as_view(), name='update'),
    path('answer_list/<int:pk>/', views.AnswerListView.as_view(), name='answer_list'),
]

