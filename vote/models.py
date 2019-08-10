from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    matric_number = models.CharField(max_length=20, unique=True)
    middle_name = models.CharField(max_length=30,null=True)


class Candidate(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    nick_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - ({self.nick_name})'


class VoteCategory(models.Model):
    name = models.CharField(max_length=225)
    candidates = models.ManyToManyField(Candidate)

    def __str__(self):
        return f'<Category: {self.name}>'

    def is_eligible(self, user):
        return Vote.objects.filter(category=self, user=user).count() == 0
    
    @classmethod
    def eligible_category(cls, user):
        return VoteCategory.objects.exclude(vote__user=user)


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='voter')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    category = models.ForeignKey(VoteCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.candidate.nick_name} - {self.category.name}'
