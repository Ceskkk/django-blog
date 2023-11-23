from django.views.generic import ListView, DetailView
from .models import Post, Category


class PostsView(ListView):
    template_name = "pages/posts.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        kword = self.request.GET.get("kword", "")
        category = self.request.GET.get("cat", "")

        response = Post.objects.search_post(kword, category)

        return response


class PostView(DetailView):
    template_name = "pages/post.html"
    model = Post
