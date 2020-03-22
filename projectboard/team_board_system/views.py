from django.shortcuts import render,redirect
from .models import TeamBoard,TeamBoardList,TeamBoardListCard
from personal_board_system.forms import AddBoardForm,AddBoardListCardForm,AddBoardListForm
from django.db import connection

# Create your views here.
def team_board(request):
	user = request.user
	boards = TeamBoard.objects.filter(user=user)
	return(render(request,'team_board_system/teamboards.html',{'team_boards':boards}))

def team_board_list(request):
	user= request.user
	board_id = request.GET.get('id')
	print(board_id)
	board = TeamBoard.objects.get(id=board_id)
	# print(board.id,board.title)
	lists = TeamBoardList.objects.filter(board=board)
	return(render(request,"team_board_system/teamboardlists.html",{'board':board,'team_board_lists':lists}))

def team_board_list_card(request):
	user = request.user
	temp = request.GET.get('id')
	if(temp is not None):
		list_id = temp
	list = TeamBoardList.objects.get(id=list_id)
	cards = TeamBoardListCard.objects.filter(list=list)
	print(cards)
	return(render(request,"team_board_system/teamboardlistcards.html",{'list':list,'team_board_list_cards':cards}))

def add_team_board(request):
	user=request.user
	if(request.method=='GET'):
		form = AddBoardForm(request.GET)
		if(form.is_valid()):
			title = form.cleaned_data.get('title')
			user_id = user.id
			cursor = connection.cursor()
			board = TeamBoard()
			board.title = title
			board.save()
			board_id = board.id
			print(board_id)
			cursor.execute('insert into team_board_system_teamboard_user (user_id,teamboard_id) values (%s,%s)',[user_id,board_id])
			return(redirect('team_board'))
	# else:
	# 	form = AddBoardForm()
	return(render(request,"team_board_system/addboard.html",{'form':form}))


def add_team_board_list(request):
	user=request.user
	if(request.method=='GET'):
		form = AddBoardListForm(request.GET)
		if(form.is_valid()):
			title = form.cleaned_data.get('title')
			board_id = request.GET.get('board_id')
			cursor = connection.cursor()
			cursor.execute('insert into team_board_system_teamboardlist (board_id,title) values (%s,%s)',[board_id,title])
			return(redirect('team_board'))
	else:
		form = AddBoardListForm()
	board_id = request.GET.get('id')
	return(render(request,"team_board_system/addboardlist.html",{'form':form,"board_id":board_id}))

def add_team_board_list_card(request):
	user=request.user
	if(request.method=='POST'):
		form = AddBoardListCardForm(request.POST,request.FILES)
		if(form.is_valid()):
			title = form.cleaned_data.get('title')
			due_date = form.cleaned_data.get('due_date')
			attachment = request.FILES['attachment']
			list_id = request.POST.get('list_id',None)
			list = TeamBoardList.objects.get(id= list_id)
			card = TeamBoardListCard()
			card.list = list
			card.title = title
			card.due_date = due_date
			card.attachment = attachment
			card.archived= False
			card.save()
			return(redirect('team_board'))
	else:
		form = AddBoardListCardForm()
	list_id = request.GET.get('id')
	
	return(render(request,"team_board_system/addboardlistcard.html",{'form':form,"list_id":list_id}))
