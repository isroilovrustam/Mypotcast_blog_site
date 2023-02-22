from django.urls import path
from .views import episode_view, detail_view, post_views_up, get_ids_list, like


urlpatterns =[
    path('', episode_view, name='episode'),
    path('detail/<int:pk>/', detail_view, name='detail'),
    path('ids_list/', get_ids_list, name='get_ids_list'),
    path('detail/views/<int:pk>/', post_views_up, name='post_views_up'),
    path('like/', like, name='like'),
]