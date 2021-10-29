from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . import serializers
from .forms import PostForm
from .models import *


class PostListView(ListView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = serializers.ChatListSerializer
    context_object_name = 'posts'
    paginate_by = 10


class PostItemView(DetailView):
    queryset = Post.objects.all()
    serializer_class = serializers.ChatItemSerilizer


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            post_form = PostForm() #cleaned form data
    else:
        form = PostForm()

    template_name = 'chat/post_form.html'
    context = {'form': form}
    return render(request, template_name, context)


