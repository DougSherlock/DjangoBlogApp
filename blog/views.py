from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView, 
    UpdateView,
    DeleteView,
    CreateView) # organize multiple imports using a tuple with round brackets
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
# from django.http import HttpResponse

posts = [
    {
        'author': 'Admin',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 30, 2021'
    },    
    {
        'author': 'Admin',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 1, 2021'
    },    
    {
        'author': 'Admin',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'February 1, 2021'
    },    
]


# this view is a function
def home(request):
    print('loading home view')
    context = {
        'title': 'Home',
        # 'posts' posts,
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def doug(request):
    print('loading doug view')
    context = {
        'title': 'Doug',
        'name': 'Doug Sherlock',
        'animal': 'Wombat',
    }
    return render(request, 'blog/doug.html', context)


# this view is a class - it does not use defaults so it requires some attributes
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # default:  <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # specify the name of the object for the Django Template Language (DTL) HTML template 
    ordering = ['-date_posted'] # show most recent at top
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # default:  <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # specify the name of the object for the Django Template Language (DTL) HTML template 
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# this view is a class - it uses defaults so it does not require attributes
class PostDetailView(DetailView):
    model = Post  


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post  
    success_url = '/'

    def test_func(self): # overrides UserPassesTestMixin.test_func
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


# must be logged in to create a post, so we inherit from LoginRequiredMixin
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
            

def about(request):
    print('loading about view')
    context = {
        'title': 'About',
        'about_info': {
            'creator': 'Doug Sherlock',
            'date_modified': '2021-02-21',
        }
    }
    return render(request, 'blog/about.html', context)
