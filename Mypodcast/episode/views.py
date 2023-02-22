from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from blog.forms import CommentArticleForm
from blog.models import Article, Category, Tag, Like


# Create your views here.


def episode_view(request):
    obj = Article.objects.order_by('-id')
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
    season = request.GET.get('season')
    if season:
        obj = obj.filter(title__icontains=season)
    p = Paginator(obj, 3)
    page = request.GET.get('page')
    obj_page = p.get_page(page)
    try:
        user_id = request.user.profile.id
    except:
        user_id = None
    my_liked_article = Like.objects.filter(author_id=user_id).values_list('article_id')
    my_liked_article_list = [i[0] for i in my_liked_article]
    ctx = {
        'objs': obj_page,
        'categorys': category,
        'tags': tags,
        'my_liked_article_list': my_liked_article_list,
    }
    return render(request, 'mypodcast/episodes.html', ctx)


def get_ids_list(request):
    episode = Article.objects.all().order_by('-id')
    ids_list = [i.id for i in episode]
    return JsonResponse({"ids_list": ids_list})


@csrf_exempt
def like(request):
    print('like')
    print(request.user)
    if not request.user.is_authenticated:
        return JsonResponse({"detail": "You should authorize"}, status=401)
    if request.method == 'POST':
        print('post')
        article_id = int(request.POST.get('article_id'))
        user_id = request.user.profile.id
        likes = Like.objects.values_list('article_id', 'author_id')
        print(article_id)
        print(article_id, user_id)
        if (article_id, user_id) in likes:
            Like.objects.get(article_id=article_id, author_id=user_id).delete()
            return JsonResponse({"detail": "Un-Liked"})
        Like.objects.create(article_id=article_id, author_id=user_id)
        return JsonResponse({"detail": "Liked"})
    return JsonResponse({"detail": "Method not allowed"}, status=405)


def post_views_up(request, pk):
    obj = Article.objects.get(id=pk)
    obj.views += 1
    obj.save()
    return redirect(reverse('detail', kwargs={"pk": pk}))


def detail_view(request, pk):
    obj = Article.objects.order_by('-id')[:3]
    obj_detail = Article.objects.get(id=pk)
    category = Category.objects.all()
    tags = Tag.objects.all()
    form = CommentArticleForm(request.POST or None)
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
    cat = request.GET.get('cat')
    if cat:
        obj = obj.filter(category__title__exact=cat)
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
        "details": obj_detail,
        'categorys': category,
        'tags': tags,
        'form': form,
        'my_liked_article_list': my_liked_article_list,
    }

    return render(request, 'mypodcast/episode.html', ctx)
