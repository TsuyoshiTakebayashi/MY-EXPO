from django.urls import path, include
from .views import SignUpView,  post_create, user_detail, user_prof_update,SignUpCompView,HomeView
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('new/', SignUpView.as_view(),name='new'),
    path('complete/', SignUpCompView.as_view(), name='complete'),
    #[develop branch]-added
    path('login/', views.SignUpView.as_view(), name='login'),#ログイン画面
    path('home/',HomeView.as_view(),name='home'),#home画面
    path('detail/', user_detail, name='detail'),#ユーザーページ
    path('profupdt/', user_prof_update, name='profupdt')#プロフ更新ページ
]