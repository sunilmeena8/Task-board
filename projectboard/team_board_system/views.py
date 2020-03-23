from django.shortcuts import render,redirect
from .models import TeamBoard,TeamBoardList,TeamBoardListCard
from personal_board_system.forms import AddBoardForm,AddBoardListCardForm,AddBoardListForm
from django.db import connection
from .forms import AddBoardMemberForm
from django.contrib.auth.models import User

# Create your views here.
def team_board(request):
	user = request.user
	boards = TeamBoard.objects.filter(user=user)
	return(render(request,'team_board_system/teamboards.html',{'team_boards':boards}))

def team_board_list(request):
	user= request.user
	board_id = request.GET.get('id')
	board = TeamBoard.objects.get(id=board_id)
	# print(board.id,board.title)
	lists = TeamBoardList.objects.filter(board=board)
	return(render(request,"team_board_system/teamboardlists.html",{'board':board,'team_board_lists':lists}))

def team_board_list_card(request):
	user = request.user
	list_id = request.GET.get('list_id')
	board_id = request.GET.get('board_id')
	# print(list_id,board_id)
	board = TeamBoard.objects.get(id=board_id)
	list = TeamBoardList.objects.get(id=list_id)
	cards = TeamBoardListCard.objects.filter(list=list)
	return(render(request,"team_board_system/teamboardlistcards.html",{'list':list,'board':board,'team_board_list_cards':cards}))

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
		
		title = request.POST.get('title')
		due_date = request.POST.get('due_date')
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
	board_id = request.GET.get('board_id')
	list_id = request.GET.get('list_id')
	# print(board_id,list_id)
	board = TeamBoard.objects.get(id=board_id)
	list = TeamBoardList.objects.get(id = list_id)
	return(render(request,"team_board_system/addboardlistcard.html",{"list":list,"board":board}))

def add_team_board_member(request):
	user=request.user
	if(request.method=='GET'):
		form = AddBoardMemberForm(request.GET)
		if(form.is_valid()):
			board_id = request.GET.get('board_id')
			username = form.cleaned_data.get('username')
			add_user = User.objects.get(username = username)
			add_user_id = add_user.id
			cursor = connection.cursor()
			cursor.execute('insert into team_board_system_teamboard_user (teamboard_id,user_id) values (%s,%s)',[board_id,add_user_id])
			return(redirect('team_board'))
	else:
		form = AddBoardMemberForm()
	board_id = request.GET.get('id')
	return(render(request,"team_board_system/addboardlist.html",{'form':form,"board_id":board_id}))

def team_board_member(request):
	board_id = request.GET.get('id')
	cursor = connection.cursor()
	cursor.execute('select user_id from team_board_system_teamboard_user where teamboard_id = %s',[board_id])
	member_ids = cursor.fetchall()
	members = []
	for  member_id in member_ids:
		members.append(User.objects.get(id = member_id[0]))
	board = TeamBoard.objects.get(id=board_id)
	
	return(render(request,'team_board_system/teamboardmembers.html',{'members':members,'board':board}))

def edit_title_team_board(request):
	user=request.user
	if(request.method=='POST'):
		title = request.POST.get('title')
		board_id = request.POST.get('board_id')
		id = user.id
		board = TeamBoard(id = board_id)
		board.title = title
		board.save()
		return(redirect('team_board'))

	board_id = request.GET.get('board_id')
	board = TeamBoard.objects.get(id=board_id)
	return(render(request,"personal_board_system/editboard.html",{'board':board}))

def delete_team_board(request):
	board_id = request.GET.get('board_id')
	board = TeamBoard.objects.get(id = board_id)
	board.delete()
	return(redirect('team_board'))

def edit_title_team_board_list(request):
	user=request.user
	if(request.method=='POST'):
		title = request.POST.get('title')
		list_id = request.POST.get('list_id')
		id = user.id
		list = TeamBoardList.objects.get(id=list_id)
		list.title= title
		list.save()
		return(redirect('team_board'))
	
	board_id = request.GET.get('board_id')
	list_id = request.GET.get('list_id')
	board = TeamBoard.objects.get(id=board_id)
	
	list = TeamBoardList.objects.get(id = list_id)
	return(render(request,"personal_board_system/editboardlist.html",{'board':board,'list':list}))

def delete_team_board_list(request):
	board_id = request.GET.get('board_id')
	list_id = request.GET.get('list_id')
	list = TeamBoardList.objects.get(id= list_id)
	list.delete()
	return(redirect('team_board'))


def edit_team_board_list_card(request):
	user=request.user
	if(request.method=='POST'):
		title = request.POST.get('title')
		due_date = request.POST.get('due_date')
		attachment = request.POST.get('attachment')
		list_id = request.POST.get('list_id')
		board_id = request.POST.get('board_id')
		card_id = request.POST.get('card_id')
		id = user.id
		card = TeamBoardListCard.objects.get(id = card_id)
		card.title = title
		card.due_date = due_date
		card.attachment = attachment
		card.save()
		return(redirect('team_board'))
	# else:
	# 	form = AddBoardForm()
	board_id = request.GET.get('board_id')
	board = TeamBoard.objects.get(id=board_id)
	list_id = request.GET.get('list_id')
	list = TeamBoardList.objects.get(id = list_id)
	card_id = request.GET.get('card_id')
	card = TeamBoardListCard.objects.get(id= card_id)
	return(render(request,"personal_board_system/editboardlistcard.html",{'board':board,'list':list,'card':card}))

def delete_team_board_list_card(request):
	board_id = request.GET.get('board_id')
	list_id = request.GET.get('list_id')
	card_id = request.GET.get('card_id')
	card = TeamBoardListCard.objects.get(id= card_id)
	card.delete()
	return(redirect('team_board'))

def archive_team_board_list_card(request):
	card_id = request.GET.get('card_id')
	card = TeamBoardListCard.objects.get(id = card_id)
	card.archived=True
	card.save()
	return(redirect('team_board'))
