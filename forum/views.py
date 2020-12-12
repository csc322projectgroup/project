from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, menu1, menu2


def home(request):
    return render(request, 'forum/index.html')

def about_us(request):
    return render(request, 'forum/about_us.html')

def contact_us(request):
    return render(request, 'forum/contact.html')

def discussion_forum(request):
        context = {
            'posts': Post.objects.all()
        }
        return render(request, 'forum/discussion_forum.html', context)

def menu_list_view(request):
	return render(request, 'forum/menu_list.html')

def menu1_view(request):
	items = menu1.objects.all()
	ctx = {'items': items}
	return render(request, 'forum/menu1.html', ctx)

def menu2_view(request):
	items = menu2.objects.all()
	ctx = {'items': items}
	return render(request, 'forum/menu2.html', ctx)

class PostListView(ListView):
    model = Post
    template_name = 'forum/discussion_forum.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'context']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'context']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
