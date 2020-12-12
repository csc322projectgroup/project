from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

from . import views

urlpatterns = [
    path('', views.home, name='forum-home'),
    path('about_us/', views.about_us, name='forum-about_us'),
    path('contact_us/', views.contact_us, name='forum-contact_us'),
    path('discussion_forum/', PostListView.as_view(), name='forum-discussion_forum'),
    path('discussion_forum/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('discussion_forum/post/new/', PostCreateView.as_view(), name='post-create'),
    path('discussion_forum/post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('discussion_forum/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')
]
