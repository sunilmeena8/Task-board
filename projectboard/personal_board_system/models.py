from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PersonalBoard(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length = 100)


class PersonalBoardList(models.Model):
	board = models.ForeignKey(PersonalBoard,on_delete=models.CASCADE,related_name="board_lists")
	title = models.CharField(max_length = 100)

class PersonalBoardListCard(models.Model):
	list = models.ForeignKey(PersonalBoardList,on_delete=models.CASCADE,related_name="board_list_cards")
	title = models.CharField(max_length = 100)
	due_date = models.DateTimeField()
	attachment = models.FileField()
	archived = models.BooleanField()
