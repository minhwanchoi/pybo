from django.contrib.auth.models import User
from django.db import models
# from django.utils import timezone
# timezone [챗gpt 를 통해 추가]
# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # voter 추가

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')  # voter 추가

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 글쓴이
    content = models.TextField()  # 댓글 내용
    create_date = models.DateTimeField()  # 댓글 작성일시
    modify_date = models.DateTimeField(null=True, blank=True)  # 댓글 수정일시
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)  # 이 댓글이 달린 질문
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)  # 이 댓글이 달린 답변