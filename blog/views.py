from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post


def home (request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)

# This tells our list view what model to query to create the view 
# gives a list of the posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'# <app>/<model>_<veiwtype>.html
    context_object_name = 'posts'
    # reversing order of the posts newest first 
    ordering = ['-date_posted']
    paginate_by = 5

# for each user
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'# <app>/<model>_<veiwtype>.html
    context_object_name = 'posts'
    # reversing order of the posts newest first 
    ordering = ['-date_posted']
    paginate_by = 5
# over riding the qurey this list view will be making
    def get_queryset(self):
        # getting object from user model imported above and getting usertname from that model
        # if the user exits we capture then in the user var otherwise a 404 is returned
        user =get_object_or_404(User,username=self.kwargs.get('username'))
        # filtering posts by the author of the user we got above
        return Post.objects.filter(author=user).order_by('-date_posted')

# for a single post
class PostDetailView(DetailView):
    model = Post

# to create a post 
class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'content']
    success_url ="/"
# overriding the form valid method
    def form_valid(self, form):
        # this is saying the form that your trying to submit make the auhor equal to the current logged in user
       form.instance.author = self.request.user 
    #    this is just running the form cause overrided It above
       return super().form_valid(form)

# to update a post 
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url ="/"
# overriding the form valid method
    def form_valid(self, form):
        # this is saying the form that your trying to submit make the auhor equal to the current logged in user
       form.instance.author = self.request.user 
    #    this is just running the form cause overrided It above
       return super().form_valid(form)
# this is requried for the user passes test mixin stop users from updating other users posts
    def test_func(self):
        # getting the post
        post = self.get_object()
        # if the user is the author of the post
        if self.request.user == post.author:
            # if the condtionly is met return true otherwise return false
            return True
        return False

# to delete a post 
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url ="/"
# this is requried for the user passes test mixin stop users from updating other users posts
    def test_func(self):
        # getting the post
        post = self.get_object()
        # if the user is the author of the post
        if self.request.user == post.author:
            # if the condtionly is met return true otherwise return false
            return True
        return False        

def about (request):
    return render(request,'blog/about.html',{'title': "about"})