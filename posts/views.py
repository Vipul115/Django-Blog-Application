from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Post


def post_list(request):

    queryset = Post.objects.all()
    if request.user.is_authenticated:

        context = { "queryset" : queryset,
                    "title": "You are "}

    else:
        context = {"title": "You are not"}

    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("<h1>Update</h1")

def post_create(request):
    return HttpResponse("<h1>Create</h1")

def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {"instance": instance,
               "title": "You are "}
    return render(request, "post_detail.html", context)


def post_delete(request):
    return HttpResponse("<h1>Delete</h1")




