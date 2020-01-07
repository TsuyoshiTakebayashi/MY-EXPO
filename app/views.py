# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from .forms import CustomUserCreationForm, PostForm, ProfForm
from .models import Post, User, Prof
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render


User = get_user_model()


# from django.views.generic.edit import ModelFormMixin

class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # UserCreationForm
    success_url = reverse_lazy('complete')  # 登録成功時にリダイレクトする先
    template_name = 'create.html'


class SignUpCompView(TemplateView):
    template_name = 'registration/login.html'


class IndexView(TemplateView):
    template_name = 'index.html'
    form_class = PostForm


class HomeView(TemplateView):
    template_name = 'home.html'


# [develop branch]-added
# 投稿と表示機能
@login_required
def post_create(request):
    if request.method == 'POST':
        pass
    else:
        form = PostForm()
        posts = Post.objects.all()
        login_user = User.objects.get(pk=request.user.id)
        try:
            login_user_prof = Prof.objects.get(user=login_user)
        except Prof.DoesNotExist:
            print("dosenotexist")
            login_user_prof = {}

    return render(request, 'home.html', {'posts': posts, 'login_user': login_user, 'login_user_prof':login_user_prof})


# ユーザーページ
@login_required
def user_detail(request):
    if request.method == 'POST':
        author = Post(author=User.objects.get(pk=request.user.id))
        # author = User.objects.get(pk=request.user.id)
        form = PostForm(request.POST or None, instance=author)
        if form.is_valid():
            #form.save()
            post = Post()  # 投稿内容が問題ない場合に投稿をユーザーに紐づけしつつDBに保存
            post.author = author
            post.product_img = request.FILES['product_img']
            post.category = request.POST['category']
            post.text = request.POST['text']

            post.save()

            return redirect("app:home") # フォームの内容とリストビューに出すデータを渡す
        else:
            return HttpResponse('無効な値です')

    username = request.GET.get('userid')
    user_data = User.objects.get(username=username)  # パラメーターからデータを検索しデータを受け渡す
    try:
        user_data_detail = Prof.objects.get(user=user_data)
    except Prof.DoesNotExist:
        print("dosenotexist")
        user_data_detail = {}


    return render(request, 'prof.html', {'user_data': user_data, 'user_data_detail': user_data_detail, 'form': PostForm})


def user_prof_update(request):
    if request.method == 'POST':
        form = ProfForm(request.POST, request.FILES)
        if not form.is_valid():
            raise ValueError('invalid form')

        Prof.objects.update_or_create(user=request.user,
                                      defaults={'icon': form.cleaned_data['icon']})

        return redirect('/user/detail/?userid={0}'.format(request.user.username))

    elif request.method == 'GET':
        return render(request, 'prof_update.html', {'form': ProfForm})


# 投稿の表示を別ページにする場合に渡すlistview
'''
@login_required
def listView(request):
    posts = Post.object.all()
    return render(request, index.html, {'posts': posts})
            """
         author = Post(author=User.objects.get(pk=request.user.id))
            # author = User.objects.get(pk=request.user.id)
            form = PostForm(request.POST or None, instance=author)
            form.save(commit=False)
            if form.is_valid():
                form.save()
                posts = Post.objects.all()  # 投稿内容が問題ない場合に投稿をユーザーに紐づけしつつDBに保存
                return render(request, 'home.html', {'form': form, 'posts': posts})  # フォームの内容とリストビューに出すデータを渡す
            else:
                return HttpResponse('無効な値です')

        """

'''
