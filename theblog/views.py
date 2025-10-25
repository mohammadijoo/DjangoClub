from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
#Comment
from .forms import PostForm, EditForm
#CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from rest_framework import generics
from .serializers import PostSerializer

# Import Pagination
from django.core.paginator import Paginator



# def theblog(request):
#     return render(request, 'theblog.html', {})
    

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))


class theblogView(ListView):
    model = Post
    template_name = 'theblog.html'
    #ordering = ['-id']
    ordering = ['-post_date']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(theblogView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        
        # Setup Pagination
        p = Paginator(Post.objects.all(), 3)
        page = self.request.GET.get('page')
        posts = p.get_page(page)
        nums = "a" * posts.paginator.num_pages
        context["posts"] = posts
        context["nums"] = nums
        
        return context
        



def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.title().replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts': category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        
        x = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = x.total_likes()
        
        liked = False
        if x.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
        
    def get_absolute_url(self):
        return self.get_url()
    

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    
    
    
# class AddCommentView(CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = 'add_comment.html'
#     #fields = '__all__'
#     def form_valid(self, form):
#         form.instance.post_id = self.kwargs['pk']
#         return super().form_valid(form)
#     success_url = reverse_lazy('theblog')
    


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = ('name',)
   
 
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'meta_tag', 'body']
 
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('theblog')
    
    
    
    
# def Comment(request):
#     # Redirecting after comment submission
#     return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))
    
    
    
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
    
    
    
    
    