from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class QuestionManager(models.Manager):

    def new(self):
        return self.order_by('-added_at')

    def popular(self):
    	return self.order_by('-rating')



class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name="question_author")
    likes = models.ManyToManyField(
        User, related_name="question_like", blank=True)

    class Meta:
        ordering = ('-added_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'pk': self.pk})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    class Meta:
        ordering = ('added_at',)

    def __str__(self):
    	return 'Answer by {}'.format(self.author)