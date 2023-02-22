from django.shortcuts import render, redirect

from blog.models import Article, Category, Tag
from .forms import ContactForm, SubscribeForm


# Create your views here.


def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(".")
    forms = SubscribeForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        return redirect(".")
    obj = Article.objects.order_by('-id')[:3]
    category = Category.objects.all()
    tags = Tag.objects.all()
    ctx = {
        'form': form,
        'forms': forms,
        'objs': obj,
        'categorys': category,
        'tags': tags
    }
    return render(request, 'mypodcast/contact.html', ctx)
