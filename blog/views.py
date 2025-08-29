from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import CommentForm, PublicationForm
from django.shortcuts import redirect


class PostListView(ListView):
    model = Post
    template_name = "publications-list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "detail_list.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            return redirect('blog:post_detail', pk=self.object.pk)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

class PublicationCreateView(CreateView):
    model = Post
    form_class = PublicationForm
    template_name = "publication-create.html"
    success_url = reverse_lazy("blog:post_list")
