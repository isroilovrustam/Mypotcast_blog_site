from django.urls import path
from .views import blog_view, detail_blog, post_views_up

urlpatterns = [
    path('', blog_view, name='blog'),
    path('detail/<int:pk>/', detail_blog, name='detail_blog'),
]
