from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 4

class QuestionAdmin(admin.ModelAdmin):
	
	fieldsets = [
		('Date', {'fields': ['pub_date']}),
		('Question', {'fields': ['question_text', 'votes_count']})
	]

	list_display = ['question_text', 'pub_date', 'votes_count', 'published_recently']

	inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)