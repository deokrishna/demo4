from django.shortcuts import render,redirect,get_object_or_404
from .models import Tweet
from .forms import TweetForm,CustomAuthenticationForm,CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')


def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

@login_required(login_url='/login/')
def create_tweet(request):
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')

    else:
        form=TweetForm()
    return render(request,'create_list.html',{'form':form})


@login_required(login_url='/login/')
def edit_tweet(request,tweet_id):
    tweet=get_object_or_404(Tweet,id=tweet_id)
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form=TweetForm(instance=tweet)
    return render(request,'edit_tweet.html',{'form':form,'tweet':tweet})

@login_required(login_url='/login/')
def delete_tweet(request,tweet_id):
    tweet=get_object_or_404(Tweet,id=tweet_id)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'confirm_delete.html',{'tweet':tweet})

def signup_view(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form=CustomUserCreationForm()
    return render(request,'signup.html',{'form':form})


def login_view(request):
    if request.method=='POST':
        form=CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tweet_list')
    else:
            form=CustomAuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
    return redirect('login')

def custom_404_view(request, exception):
    return render(request, '404.html', {}, status=404)