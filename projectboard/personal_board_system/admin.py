from django.contrib import admin
from .models import PersonalBoard,PersonalBoardList,PersonalBoardListCard
# Register your models here.
admin.site.register(PersonalBoard)
admin.site.register(PersonalBoardList)
admin.site.register(PersonalBoardListCard)