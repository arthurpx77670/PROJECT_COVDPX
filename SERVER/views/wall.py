from django.shortcuts import render
from SERVER.models.db.post import Like
from SERVER.models.forms.post import CommentaryForm


def wall(request):

    if(request.user.is_authenticated):
        # form commenatry
        Commentaryform = CommentaryForm()

        # user
        friends = request.user.profile.friends.all()

        # posts
        posts = []
        for friend in friends:
            # posts friend
            for post in friend.profile.post_set.all().filter(description=False):
                posts.append(post)
            # post share by your friends
            for like in friend.profile.like_set.all():
                if(like.post.author != request.user.profile):
                    posts.append(like.post)

        # size posts
        postsCount = len(posts)

        # list of my likes on the profile user
        likesRequest = Like.objects.filter(author=request.user.profile)
        postsUserLikedRequest = []
        for likes in likesRequest:
            if posts:
                if likes.post in posts:
                    postsUserLikedRequest.append(likes.post)

        return render(request, "wall/index.html", {"posts": posts,
                                                        "postsCount" :postsCount,
                                                        "Commentaryform" : Commentaryform,
                                                        "postsUserLikedRequest":postsUserLikedRequest, })