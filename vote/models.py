from django.db import models
from django.db.models import Max
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    matric_number = models.CharField(max_length=20, unique=True)
    middle_name = models.CharField(max_length=30,null=True)

    def full_name(self):
        if self.is_superuser or self.is_staff:
            return self.username
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class Candidate(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    nick_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - ({self.nick_name})'

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name} - ({self.nick_name})'


class VoteCategory(models.Model):
    name = models.CharField(max_length=225)
    candidates = models.ManyToManyField(Candidate)

    class Meta:
        verbose_name_plural = 'Vote Categories'

    def __str__(self):
        return f'<Category: {self.name}>'

    def is_eligible(self, user):
        return Vote.objects.filter(category=self, user=user).count() == 0
    
    @classmethod
    def eligible_category(cls, user):
        return VoteCategory.objects.exclude(vote__user=user)

    @property
    def votes(self):
        return self.votecount_set.all().order_by('-number')

    @property
    def highest_vote_count(self):
        return self.votecount_set.all().aggregate(Max('number'))['number__max']

    @property
    def top(self):
        return self.votecount_set.all().filter(number=self.highest_vote_count)

    @property
    def top_candidates(self):
        return [count.candidate for count in self.top ]

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='voter')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    category = models.ForeignKey(VoteCategory, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'category')

    def __str__(self):
        return f'{self.candidate.nick_name} - {self.category.name}'


class VoteCount(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    category = models.ForeignKey(VoteCategory, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)

    class Meta:
        unique_together = ('candidate', 'category')

    def __str__(self):
        return f'{self.candidate.nick_name} - {self.category.name}: {self.number}'
