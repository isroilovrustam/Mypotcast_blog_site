from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Article, Category, Tag, Blog
from .forms import CommentBlogForm

# Create your views here.


def blog_view(request):
    obj = Blog.objects.order_by('-id')
    obj_article = Article.objects.order_by('-id')[:3]
    category = Category.objects.all()
    tags = Tag.objects.all()
    q = request.GET.get('q')
    if q:
        obj = obj.filter(title__icontains=q)
    cat = request.GET.get('cat')
    if cat:
        obj = obj.filter(category__title__exact=cat)
    tag = request.GET.get('tag')
    if tag:
        obj = obj.filter(tags__title__icontains=tag)
    p = Paginator(obj, 2)
    page = request.GET.get('page')
    obj_page = p.get_page(page)
    ctx = {
        'blogs': obj_page,
        'objs': obj_article,
        'categorys': category,
        'tags': tags
    }
    return render(request, 'mypodcast/blog.html', ctx)


def post_views_up(request, pk):
    obj = Article.objects.get(id=pk)
    obj.views += 1
    obj.save()
    return redirect(reverse('detail', kwargs={"pk": pk}))


def detail_blog(request, pk):
    obj = Blog.objects.order_by('-id')[:3]
    obj_detail = Blog.objects.get(id=pk)
    tags = Tag.objects.all()
    tag = request.GET.get('tag')
    form = CommentBlogForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            com = form.save(commit=False)
            com.article = obj_detail
            com.author_id = request.user.profile.id
            com.save()
            return redirect('.')
    else:
        if form.is_valid():
            com = form.save(commit=False)
            com.article = obj_detail
            com.save()
            return redirect('.')
    if tag:
        obj = obj.filter(tags__title__icontains=tag)
    ctx = {
        'objs': obj,
        "details": obj_detail,
        'tags': tags,
        'form': form,
    }

    return render(request, 'mypodcast/blog-detail.html', ctx)
