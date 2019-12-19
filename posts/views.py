from django.shortcuts import render, HttpResponse
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,"index.template.html", {
        "posts":posts
    })
    
def create_post(request):
    if request.method == "POST":
        # recreate the form with the data from request.POST
        # request.POST contains what data the user has given
        form = PostForm(request.POST, request.FILES)
        form.save() # actually save the model
        return redirect(index)
    else:
        form = PostForm()
        return render(request, "post_form.template.html", {
            "form":form
        })
    
def about_us(request):
    return render(request, "profile.template.html", {
        "username":"Arif",
        "age":"28"
    })
    
def past_submissions(request):
    return render(request, "history.template.html")