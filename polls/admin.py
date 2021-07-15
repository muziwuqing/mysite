from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice


# 自定义后台表单
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
#
#
# admin.site.register(Question, QuestionAdmin)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
