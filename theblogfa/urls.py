from django.urls import path, include
#from . import views
from .views import theblogfaView, ArticleDetailfaView, AddPostfaView, UpdatePostfaView, DeletePostfaView, AddCategoryfaView, CategoryfaView, CategoryListfaView, LikefaView, PostfaList
#AddCommentView
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    #path('', views.theblog, name="theblog"),  
    path('', theblogfaView.as_view(), name="theblogfa"),  
    path('articlefa/<int:pk>', ArticleDetailfaView.as_view(), name="article_detailfa"),  
    path('add_postfa/', AddPostfaView.as_view(), name="add_postfa"),  
    path('add_categoryfa/', AddCategoryfaView.as_view(), name="add_categoryfa"), 
    path('articlefa/edit/<int:pk>', UpdatePostfaView.as_view(), name="update_postfa"),
    path('articlefa/<int:pk>/remove', DeletePostfaView.as_view(), name="delete_postfa"),
    path('categoryfa/<str:cats>/', CategoryfaView, name="categoryfa"),
    path('category-listfa/', CategoryListfaView, name="category-listfa"),
    path('likefa/<int:pk>', LikefaView, name="like_postfa"),
    #path('article/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),  
    path('articlefa/comments/', include('django_comments_xtd.urls')),
    #path('comments/post/', Comment, name="post_comment"),
    path('api/articlesfa', PostfaList.as_view(), name="articlesfa_api"),
    
]