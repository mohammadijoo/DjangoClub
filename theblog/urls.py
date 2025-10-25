from django.urls import path, include
#from . import views
from .views import theblogView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, PostList
#AddCommentView

urlpatterns = [
    #path('', views.theblog, name="theblog"),  
    path('', theblogView.as_view(), name="theblog"),  
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_detail"),  
    #path('<slug:slug>', ArticleDetailView.as_view(), name="article_detail"), 
    path('add_post/', AddPostView.as_view(), name="add_post"),  
    path('add_category/', AddCategoryView.as_view(), name="add_category"), 
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),
    path('like/<int:pk>', LikeView, name="like_post"),
    #path('article/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),  
    path('article/comments/', include('django_comments_xtd.urls')),
    #path('comments/post/', Comment, name="post_comment"),
    path('api/articles', PostList.as_view(), name="articles_api"),
    
]