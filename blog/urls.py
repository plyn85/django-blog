from django.urls import path
from .views import PostListView, PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views

# name it blog home to be clear with naming of path
# no need to add path name to home route as path from main url page returns blog
urlpatterns = [
    path('', PostListView.as_view(),name="blog-home"),
    path('user/<str:username>/', UserPostListView.as_view(),name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(),name="post-detail"),
    path('post/new/', PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name="post-delete"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name="post-update"),
    path('about/', views.about,name="blog-about"),

]

# class based veiws look for templates In this naming convention 
# <app>/<model>_<veiwtype>.html