from django.http import HttpResponse
from django.template import loader

from blog.models import Post
# Create your views here.

def index(request):
    latest_posts = Post.objects.all().order_by('-created_at')
    template = loader.get_template('blog/index.html')
    html = template.render({'latest_posts': latest_posts})
    return HttpResponse(html)
