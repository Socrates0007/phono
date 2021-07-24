from django.urls import path
from .views import HomeView,DetailPageView,CommentBlogView,SinglecommentView,ReplyCommentView,AllpostsView,SearchView





urlpatterns = [
    path('',HomeView.as_view(),name='homepage'),
    path('details/<int:pk>',DetailPageView.as_view(),name='details'),
    path('details/<int:pk>/comment',CommentBlogView.as_view(),name='comment'),
    path('singlecomment/<int:pk>',SinglecommentView.as_view(),name='singlecomment'),
    path('singlecomment/<int:pk>/reply',ReplyCommentView.as_view(),name='reply'),
    path('all',AllpostsView.as_view(),name='all'),
    path('search',SearchView,name='search'),
]
