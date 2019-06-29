from django.contrib.syndication.views import Feed
from .models import Post

class LatestPosts(Feed):
    title = " Blog"
    link = "/feed/"
    description = "Latest Posts of Blog"

    def items(self):
        return  Post.objects.published()[:5]