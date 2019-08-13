""" Signals and Handlers """

from django.db.models.signals import post_save
from django.db.models import F
from django.dispatch import receiver

from vote.models import VoteCount, Vote, VoteCategory


@receiver(post_save, sender=Vote)
def increment_vote_count(sender, instance,  **kwargs):
    """ Increments VoteCount when a vote has being casted """

    if kwargs['created']:
        vote_count, _ = VoteCount.objects.get_or_create(
                candidate=instance.candidate, category=instance.category)
        vote_count.number = F('number') + 1
        vote_count.save()


@receiver(post_save, sender=VoteCategory)
def increment_vote_count(sender, instance,  **kwargs):
    """ Increments VoteCount when a vote has being casted """

    # Drop old candidates
    for count in VoteCount.objects.filter(category=instance):
        if count.candidate not in instance.candidates.all():
            VoteCount.objects.get(category=instance, candidate=count.candidate).delete()
    # Add New candidates
    for candidate in instance.candidates.all():
        vote_count, _ = VoteCount.objects.get_or_create(candidate=candidate, category=instance)

