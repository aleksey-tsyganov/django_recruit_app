from django.contrib import admin
from .models import Planet, Master, Question, Recruit, RecruitStatus, Answer


admin.site.register(Planet)
admin.site.register(Master)
admin.site.register(Question)
admin.site.register(Recruit)
admin.site.register(RecruitStatus)
admin.site.register(Answer)