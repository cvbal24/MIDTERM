from django.shortcuts import render, redirect
from .forms import TweetForm
from .models import Tweet

def tweet_list(request):
    tweets = Tweet.objects.order_by('-created_at')
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})

def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweets/tweet_form.html', {'form': form})
