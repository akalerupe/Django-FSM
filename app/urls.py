from django.urls import path
from app import views


urlpatterns = [
    path('', views.index, name="posts"),
    path('unpublished', views.unpublished_posts, name="unpublished-posts"),
    path('deleted', views.deleted_posts, name="deleted-posts"),
    path('drafts', views.drafts, name="drafts"),
    path('delete/<int:id>', views.delete_post, name="delete-post"),
    path('publish/<int:id>', views.publish_post, name="publish-post"),
    path('unpublish/<int:id>', views.unpublish_post, name="unpublish-post"),
]
