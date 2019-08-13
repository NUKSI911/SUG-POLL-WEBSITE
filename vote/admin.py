from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from vote.models import User, Vote, VoteCategory, Candidate, VoteCount
from import_export import resources
from .models import User


@admin.register(Vote, Candidate, VoteCategory, User, VoteCount)

class ViewAdmin(ImportExportModelAdmin):
    pass
