from django.shortcuts import render
from post.models import Post
from django.views.generic import ListView
from post.forms import PostForm
from django.shortcuts import redirect
from django.http import Http404
from django.views.generic.detail import DetailView


class PostsView(ListView):
    paginate_by = 5
    model = Post
    template_name = "all_records.html"


def new_post(request):
    context = {"form": PostForm()}
    if request.method == "POST":
        copy_post = request.POST.copy()
        copy_post["author"] = request.user
        form = PostForm(copy_post, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("all_posts")
        context.update(form=form)
    return render(request, "new_post.html", context)


# def single_post(request, url):
#     try:
#         context = {
#             "post": Post.objects.get(url=url)
#         }
#     except Post.DoesNotExist:
#         raise Http404("Post not found.")
#     except Post.MultipleObjectsReturned:
#         ...
#     if request.META.get("HTTP_REFERER"):
#         context.update(back=request.META["HTTP_REFERER"])
#     context["post"].views += 1
#     context["post"].save()

#     # print(request.META)

#     return render(request, "single_post.html", context)


class PostDetail(DetailView):
    model = Post
    template_name="single_post.html"