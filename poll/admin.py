from django.contrib import admin

# Register your models here
from poll.models import Question,Choice,UserVote

class ChoiceStacked(admin.StackedInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text','pub_date')
    list_filter = ('author',)
    inlines = (ChoiceStacked,)

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(UserVote)