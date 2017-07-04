from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class QuestionManager(models.Manager):

    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Name")
    text = models.TextField(verbose_name="Questions")
    added_at = models.DateTimeField(blank=True, auto_now_add=True, verbose_name="Date")
    rating = models.IntegerField(default=0, verbose_name="Rating")
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Autor")
    likes = models.ManyToManyField(User, related_name='question_like_user')

    objects = QuestionManager()

    def get_url(self):
        return reverse('question', args=[self.pk])

    @staticmethod
    def get_user(username=None):
        try:
            if not username:
                user = User.objects.get(pk=1)
            else:
                user = User.objects.get(username=username)
            return user
        except User.DoesNotExist, e:
            print "Handle ERROR: %s" % e
            user = User.objects.get(pk=1)
            return user

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'question'
        verbose_name_plural = 'List questions'


class Answer(models.Model):
    text = models.TextField(verbose_name="Ansvers")
    added_at = models.DateTimeField(blank=True, auto_now_add=True, verbose_name="Dates")
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Autors")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Questionse")

    def __unicode__(self):
        return self.text

    class Meta:
        db_table = 'Answer'
        verbose_name_plural = 'List ansver'