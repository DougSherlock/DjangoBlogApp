from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    print('loading home view')
    context = {
        'title': 'Polls',
        # 'posts' posts,
        # 'posts': Post.objects.all()
    }
    return render(request, 'polls/home.html', context)
