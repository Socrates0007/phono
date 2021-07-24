from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Comment, Post, Reply, Testimonies
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .forms import CommentForm,ReplyForm

# Create your views here.
class HomeView(ListView):
    model=Post
    template_name='blogapp/index.html'
    context_object_name='allposts'
    queryset=Post.objects.all()[:7]

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['testimonies']=Testimonies.objects.all()[:5]
        return context



class DetailPageView(DetailView):
    model=Post
    template_name='blogapp/post.html'
    context_object_name='post'

class CommentBlogView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name='blogapp/comment.html'
    success_url=reverse_lazy('homepage')

    def form_valid(self, form,**kwargs):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)

class SinglecommentView(DetailView):
    model=Comment
    template_name='blogapp/singlecomment.html'
    context_object_name='commen'

class ReplyCommentView(CreateView):
    model=Reply
    form_class=ReplyForm
    template_name='blogapp/reply.html'
    #success_url=reverse_lazy("singlecomments",kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form,**kwargs):
        form.instance.repl_id=self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        #return super().get_success_url()
        return reverse_lazy('reply',kwargs={'pk':self.kwargs['pk']})


class AllpostsView(ListView):
    model=Post
    template_name="blogapp/allposts.html"
    context_object_name='allposts'

def SearchView(request):
    search=request.POST.get('targs')
    results=Post.objects.filter(title__icontains=search)
    return render(request,'blogapp/search.html',{'results':results})
