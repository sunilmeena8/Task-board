from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TeamBoard(models.Model):
	user = models.ManyToManyField(User)
	title = models.CharField(max_length=100)

class TeamBoardList(models.Model):
	board = models.ForeignKey(TeamBoard,on_delete=models.CASCADE)
	title = models.CharField(max_length = 100)

class TeamBoardListCard(models.Model):
	list = models.ForeignKey(TeamBoardList,on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	due_date = models.DateTimeField()
	attachment = models.FileField()
	archived = models.BooleanField()
	

