from django.shortcuts import render

from post.models import Post


def home(request):
    return render(request, 'post/post_list.html', {'posts': Post.objects.order_by('-publish_date').all()})
