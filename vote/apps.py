""" Application Configuration """

from django.apps import AppConfig


class VoteConfig(AppConfig):
    name = 'vote'

    def ready(self):
        import vote.signals

