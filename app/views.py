from django.shortcuts import redirect, render
from app.models import Post


def index(request):
    ctx = {}  

    posts = Post.objects.filter(status="published")

    ctx["posts"] = posts

    return render(request, "index.html", ctx)


def unpublished_posts(request):
    posts = Post.objects.filter(status="unpublished")

    return render(request, "unpublished.html", context={"posts": posts})


def deleted_posts(request):
    posts = Post.objects.filter(status="deleted")

    return render(request, "deleted.html", context={"posts": posts})
    

def drafts(request):
    posts = Post.objects.filter(status="draft")

    return render(request, "drafts.html", context={"posts": posts})
    
    

def publish_post(request, id):
    post = Post.objects.get(id=id)
    post.to_published()
    post.save()


    return redirect("posts")


def unpublish_post(request, id):
    post = Post.objects.get(id=id)
    post.to_unpublished()
    post.save()


    return redirect("posts")


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.to_deleted()
    post.save()


    return redirect("posts")