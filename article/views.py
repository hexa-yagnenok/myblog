from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def articles(request):
    keyword=request.GET.get("keyword")
    if keyword:
        articles=Article.objects.filter(title__contains= keyword)
    else:
        articles=Article.objects.all()
    context={
        "articles":articles
    }
    return render(request,"articles.html",context)

def index(request):
    return render(request,"index.html",)

def about(request):
    return render(request,"about.html")
    
@login_required
def dashboard(request):
    articles= Article.objects.filter(author=request.user)
    context={
        "articles":articles
    }
    return render(request,"dashboard.html",context)

@login_required
def addarticle(request):
    form=ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Successfully created article")
        return redirect("article:detail",article.id)
    context={
        "form":form
    }
    return render(request,"addarticle.html",context)

def detail(request,id):
    #article=Article.objects.filter(id = id).first()
    article=get_object_or_404(Article,id=id)
    comments=Comment.objects.filter(article=article)
    context={
        "article":article,
        "comments":comments
    }
    return render(request,"detail.html",context)

@login_required
def updateArticle(request,id):
    article=get_object_or_404(Article,id=id)
    if(article.author==request.user):
        form=ArticleForm(request.POST or None,request.FILES or None,instance=article)
        if form.is_valid():
            article=form.save(commit=False)
            article.save()
            messages.success(request,"Successfully updated article")
            return redirect("article:detail",id)
        context={
            "form":form
        }
        return render(request,"update.html",context)
    else:
        messages.info(request,"You can't change that")
        return redirect("index")

@login_required
def removeArticle(request,id):
    article=get_object_or_404(Article,id=id)
    if(article.author==request.user):
        article.delete()
        messages.success(request,"Successfully removed article")
        return redirect("article:dashboard")
    else:
        messages.info(request,"You can't remove that")
        return redirect("index")

@login_required
def addComment(request,id):
    article=get_object_or_404(Article,id=id)
    if request.method=="POST":
        comment_author=request.user
        comment_title=request.POST.get("comment_title")
        comment_content=request.POST.get("comment_content")
        newComment=Comment(article=article,comment_title=comment_title,comment_author=comment_author,comment_content=comment_content)
        newComment.save()
    return redirect("article:detail",id)