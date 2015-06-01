from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from blog.models import Post
# Create your views here.

def index(request):
    latest_posts = Post.objects.all().order_by('-created_at')
    template = loader.get_template('blog/index.html')
    for post in latest_posts:
        post.url = post.title.replace(' ',  '_')
    html = template.render({'latest_posts': latest_posts})
    return HttpResponse(html)

def post(request, post_url):
    single_post = get_object_or_404(Post, title=post_url.replace('_', ' '))
    template = loader.get_template('blog/post.html')
    html = template.render({'single_post': single_post})
    return HttpResponse(html)
