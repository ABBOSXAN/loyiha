from django.views.generic import ListView,DetailView, CreateView, TemplateView,UpdateView, DeleteView
from .models import Matn
from django.urls import reverse_lazy
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
class PostPageView(ListView):
    model = Matn
    template_name = 'about.html'

class PostDetailView(DetailView):
    model = Matn
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Matn
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class PostUpdateView(UpdateView):
    model=Matn
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class PostDeleteView(DeleteView):
    model = Matn
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')