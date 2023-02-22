from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from blog.models import Article, Category, Tag, Like


# Create your views here.


def home_view(request):
    obj = Article.objects.order_by('-id')
    category = Category.objects.all()[:4]
    tags = Tag.objects.all()
    tag = request.GET.get('tag')
    if tag:
        obj = obj.filter(tags__title__icontains=tag)
    try:
        user_id = request.user.profile.id
    except:
        user_id = None
    my_liked_article = Like.objects.filter(author_id=user_id).values_list('article_id')
    my_liked_article_list = [i[0] for i in my_liked_article]
    ctx = {
        'objs': obj,
        'categorys': category,
        'tags': tags,
        'my_liked_article_list': my_liked_article_list
    }
    return render(request, 'mypodcast/index.html', ctx)


def login_view(request):
    if not request.user.is_anonymous:
        return redirect('/')
    # form = AuthenticationForm(request.POST or None)
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_path = request.GET.get('next')
            if next_path:
                return redirect(next_path)
            return redirect('/')
    ctx = {
        'form': form
    }
    return render(request, 'login.html', ctx)


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')
    return render(request, 'logout.html')


def registration(request):
    if request.user.is_authenticated:
        return redirect('/login/')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login/')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
