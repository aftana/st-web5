from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class QuestionManager(models.Manager):
  def new(self):
    return super(QuestionManager, self).get_query_set().all().order_by('-added_at')

  def popular(self):
    return super(QuestionManager, self).get_query_set().all().order_by('-rating')


class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  rating = models.IntegerField(null=True, blank=True)
  author = models.ForeignKey(User, null=True, related_name='author', on_delete=models.SET_NULL)
  likes = models.ManyToManyField(User, related_name='likes')
  objects = QuestionManager()

  def get_url(self):
    return reverse('question', kwargs = { 'id': self.id})

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

  def get_url(self):
    return reverse('question', kwargs = { 'id': self.question.id })