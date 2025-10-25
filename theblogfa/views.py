from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Postfa, Categoryfa
#Comment
from .forms import PostfaForm, EditfaForm
#CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Import Pagination
from django.core.paginator import Paginator

from rest_framework import generics
from .serializers import PostfaSerializer



# def theblog(request):
#     return render(request, 'theblogfa.html', {})
    

def LikefaView(request, pk):
    post = get_object_or_404(Postfa, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_detailfa', args=[str(pk)]))


class theblogfaView(ListView):
    model = Postfa
    template_name = 'theblogfa.html'
    #ordering = ['-id']
    ordering = ['-post_date']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Categoryfa.objects.all()
        context = super(theblogfaView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        
        # Setup Pagination
        p = Paginator(Postfa.objects.all(), 3)
        page = self.request.GET.get('page')
        posts = p.get_page(page)
        nums = "a" * posts.paginator.num_pages
        context["posts"] = posts
        context["nums"] = nums
        
        return context
        



def CategoryListfaView(request):
    cat_menu_list = Categoryfa.objects.all()
    return render(request, 'category_listfa.html', {'cat_menu_list':cat_menu_list})


def CategoryfaView(request, cats):
    category_posts = Postfa.objects.filter(category=cats.title().replace('-', ' '))
    return render(request, 'categoriesfa.html', {'cats':cats.title().replace('-', ' '), 'category_posts': category_posts})


class ArticleDetailfaView(DetailView):
    model = Postfa
    template_name = 'article_detailsfa.html'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Categoryfa.objects.all()
        context = super(ArticleDetailfaView, self).get_context_data(*args, **kwargs)
        
        x = get_object_or_404(Postfa, id=self.kwargs['pk'])
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
    

class AddPostfaView(CreateView):
    model = Postfa
    form_class = PostfaForm
    template_name = 'add_postfa.html'
    #fields = '__all__'
    
    
    
# class AddCommentView(CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = 'add_commentfa.html'
#     #fields = '__all__'
#     def form_valid(self, form):
#         form.instance.post_id = self.kwargs['pk']
#         return super().form_valid(form)
#     success_url = reverse_lazy('theblog')
    


class AddCategoryfaView(CreateView):
    model = Categoryfa
    template_name = 'add_categoryfa.html'
    fields = ('name',)
   
 
class UpdatePostfaView(UpdateView):
    model = Postfa
    form_class = EditfaForm
    template_name = 'update_postfa.html'
    #fields = ['title', 'title_tag', 'meta_tag', 'body']
 
    
class DeletePostfaView(DeleteView):
    model = Postfa
    template_name = 'delete_postfa.html'
    success_url = reverse_lazy('theblogfa')
    
    
    
    
# def Comment(request):
#     # Redirecting after comment submission
#     return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))
    
    
    
class PostfaList(generics.ListAPIView):
    queryset = Postfa.objects.all()
    serializer_class = PostfaSerializer
    
    
    
    
    
    
    