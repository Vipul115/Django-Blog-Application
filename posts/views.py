from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.contrib import messages

# Create your views here.
from .models import Post
from .forms import PostForm

def post_list(request):

    queryset = Post.objects.all()
    if request.user.is_authenticated:

        context = { "queryset" : queryset,
                    "title": "You are "}

    else:
        context = {"title": "You are not"}

    return render(request, "index.html", context)

def post_update(request,id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Item saved")

        return HttpResponseRedirect(instance.get_absolute_url())
    context = {"title":instance.title,
                "instance": instance,
                "form":form
               }
    return render(request, "post_form.html", context)

def post_create(request):

    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {"form": form}
    return render(request, "post_form.html", context)


def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {"instance": instance,
               "title": "You are "}
    return render(request, "post_detail.html", context)


def post_delete(request):
    return HttpResponse("<h1>Delete</h1")




