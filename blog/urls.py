from django.urls import path
from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	MyPostListView,
)
from . import views


urlpatterns = [
	path('', PostListView.as_view(), name='blog-home'),
	path('myposts/', MyPostListView.as_view(), name='mypost'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('about/', views.about, name='blog-about'),
]
