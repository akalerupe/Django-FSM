from django.db import models
from django_fsm import FSMField, transition



class Post(models.Model):
    
    title = models.CharField(max_length=100)
    body = models.TextField()

    """ 
    Post Status
    Can be : Draft -> Discarded || Published
    Published -> Unpublished 
    Unpublished -> Deleted 

    """

    status = FSMField(default="draft")


    @transition(field=status, source=["draft", "unpublished"], target="published")
    def to_published(self):
        return "Post Published!"

    @transition(field=status, source="draft", target="discarded")
    def to_discarded(self):
        return "Post Discarded from draft!"

    @transition(field=status, source="published", target="unpublished")
    def to_unpublished(self):
        return "Post Unpublished"

    @transition(field=status, source=["unpublished", "draft"], target="deleted")
    def to_deleted(self):
        return "Post Deleted fr, fr"

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return f"{self.title}"
