from django.shortcuts import render, redirect

from blog.models import Category, Tag, Article
from contact.forms import SubscribeForm


# Create your views here.


def about_view(request):
    obj = Article.objects.order_by('-id')[:3]
    category = Category.objects.all()[:4]
    tags = Tag.objects.all()
    forms = SubscribeForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        return redirect(".")

    ctx = {
        'objs': obj,
        'forms': forms,
        'categorys': category,
        'tags': tags,
    }
    return render(request, 'mypodcast/about.html', ctx)