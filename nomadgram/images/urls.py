from django.conf.urls import url
from . import views
app_name = "images"
urlpatterns = [
    url(
        regex=r'^$',
        view=views.Feed.as_view(),
        name='feed'
    ),
    url(
        regex=r'^(?P<image_id>[0-9]+)/like/',
        view=views.LikeImage.as_view(),
        name='like_image'
    ),
    url(
        regex=r'^(?P<image_id>[0-9]+)/unlike/',
        view=views.UnLikeImage.as_view(),
        name='unlike_image'
    ),
    url(
        regex=r'^(?P<image_id>[0-9]+)/comment/',
        view=views.CommentOnImage.as_view(),
        name='comment_image'
    )
]
