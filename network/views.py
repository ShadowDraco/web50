import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import User, Post


def index(request):
    return render(request, "network/index.html")

def users(request):
    try: 
        if request.method == 'GET':
            users = list(User.objects.all().values('username', 'id'))
            return JsonResponse({'users': users[0]})
        else: 
            return JsonResponse({'error': 'There was an error with your request'})
    except: 
        return JsonResponse({'error': 'There was an error with your request'})
    
def post(request, id, action):
    try: 
        if request.method == 'PUT':
            post = Post.objects.filter(id=id)
            print(action)
            if action == 'like':
                post.update(liked_by=request.user)

            elif action == 'unlike':
                post.update(liked_by=not request.user)
            
            else: 
                return JsonResponse({'error': 'That is not a valid action'})
            
            post.save()
    except: 
        return JsonResponse({'error': 'There was an error liking or un-liking this post'})

def posts(request, id = None):

    try: 
        if request.method == 'GET' and id:
            post = Post.objects.filter({id: id})
            return JsonResponse({'post': post, "user": request.user.id})
        
        elif request.method == 'GET':
            posts = list(Post.objects.all().values())
            return JsonResponse({'posts': posts, "user": request.user.id})
        
        elif request.method == 'POST':
            # set post data
            user = request.user
            content = json.loads(request.body)["content"]
            # create new post
            newPost = Post.objects.create(posted_by=user, poster_name=user.username, content=content)
            return JsonResponse({ "status": 200, "user": request.user.id})

        elif request.method == 'PUT' and id:
            newContent = request.POST['content']
            Post.objects.update({id: id}, {content: newContent})
            return JsonResponse({ "status": 200})
        else: 
            return JsonResponse({'error': 'That type of request does not work.'})
    except: 
       return JsonResponse({'error': 'There was an error with your request'})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
   
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
