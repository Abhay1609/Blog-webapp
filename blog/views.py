from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import blogform
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.urls import reverse


def index(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/index.html',context)
class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(user=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user==post.user:
            return True
        return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user==post.user:
            return True
        return False
global title
class ViewComment(ListView):
    model= Comment

    context_object_name = 'posts'



    def get_queryset(self):
        title = get_object_or_404(Post, title=self.kwargs.get('title'))
        a = Comment.objects.filter(title=title)


        if ( len(a)== 0):
            ab ={'title':title}
            return Post.objects.filter(title=title).order_by('-date_posted')




        else:
            return Comment.objects.filter(title=title).order_by('-date_posted')


class CreatComment(LoginRequiredMixin,CreateView):
    model = Comment
    fields = ['content']


    def form_valid(self, form):
        form.instance.user=self.request.user
        form.instance.title=get_object_or_404(Post, title=self.kwargs.get('title'))
        return super().form_valid(form)


def add_blog(request):
    if request.method == 'POST':

        form=blogform(request.POST)

        if form.is_valid():

            form.save( )
            #username=form.cleaned_data.get('username')
            return redirect('index')
    else:

      form=blogform
    context={'form':form}
    return render(request, 'blog/blog.html', context)

# Create your views here.
