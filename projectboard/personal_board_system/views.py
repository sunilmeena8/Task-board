from django.shortcuts import render,redirect
from django.db import connection
from .forms import AddBoardForm,AddBoardListForm,AddBoardListCardForm,EditBoardForm,EditListForm
from .models import PersonalBoard,PersonalBoardList,PersonalBoardListCard

# Create your views here.
def personal_board(request):
	user = request.user
	boards = PersonalBoard.objects.filter(user=user)
	
	return(render(request,'personal_board_system/personalboards.html',{'personal_boards':boards}))

def personal_board_list(request):
	user= request.user
	
	board_id = request.GET.get('id')
	board = PersonalBoard.objects.get(id=board_id)
	# print(board.id,board.title)
	lists = PersonalBoardList.objects.filter(board=board)
	
	return(render(request,"personal_board_system/personalboardlists.html",{'board':board,'personal_board_lists':lists}))


def personal_board_list_card(request):
	
	user = request.user
	temp = request.GET.get('list_id')
	if(temp is not None):
		list_id = temp
	board_id = request.GET.get('board_id')

	list = PersonalBoardList.objects.get(id=list_id)
	board = PersonalBoard.objects.get(id=board_id)
	cards = PersonalBoardListCard.objects.filter(list=list)
	for i in cards:
		print(i.attachment)
		
	return(render(request,"personal_board_system/personalboardlistcards.html",{'list':list,"board":board,'personal_board_list_cards':cards}))

def add_personal_board(request):
	user=request.user
	if(request.method=='GET'):
		form = AddBoardForm(request.GET)
		if(form.is_valid()):
			title = form.cleaned_data.get('title')
			id = user.id
			cursor = connection.cursor()
			cursor.execute('insert into personal_board_system_personalboard (user_id,title) values (%s,%s)',[id,title])
			return(redirect('personal_board'))
	# else:
	# 	form = AddBoardForm()
	return(render(request,"personal_board_system/addboard.html",{'form':form}))


def add_personal_board_list(request):
	user=request.user
	
	if(request.method=='GET'):
		form = AddBoardListForm(request.GET)
		
		if(form.is_valid()):
			title = form.cleaned_data.get('title')

			board_id = request.GET.get('board_id')
			
			cursor = connection.cursor()
			cursor.execute('insert into personal_board_system_personalboardlist (board_id,title) values (%s,%s)',[board_id,title])
			return(redirect('personal_board'))
	else:
		form = AddBoardListForm()
	board_id = request.GET.get('id')
	return(render(request,"personal_board_system/addboardlist.html",{'form':form,"board_id":board_id}))

def add_personal_board_list_card(request):
	user=request.user
	if(request.method=='POST'):
		
		title = request.POST.get('title')
		due_date = request.POST.get('due_date')
		attachment = request.FILES['attachment']
		# attachment = request.POST.get('attachment')
		list_id = request.POST.get('list_id',None)
		list = PersonalBoardList.objects.get(id= list_id)
		card = PersonalBoardListCard()
		card.list = list
		card.title = title
		card.due_date = due_date
		card.attachment = attachment
		card.archived= False
		card.save()
		return(redirect('personal_board'))
	board_id = request.GET.get('board_id')
	list_id = request.GET.get('list_id')
	print(board_id,list_id)
	board = PersonalBoard.objects.get(id=board_id)
	list = PersonalBoardList.objects.get(id = list_id)
	return(render(request,"personal_board_system/addboardlistcard.html",{"list":list,"board":board}))

def edit_title_personal_board(request):
	user=request.user
	if(request.method=='POST'):
		title = request.POST.get('title')
		board_id = request.POST.get('board_id')
		id = user.id
		cursor = connection.cursor()
		cursor.execute('update personal_board_system_personalboard set title=%s where id = %s',[title,board_id])
		return(redirect('personal_board'))
	# else:
	# 	form = AddBoardForm()
	board_id = request.GET.get('board_id')
	board = PersonalBoard.objects.get(id=board_id)
	return(render(request,"personal_board_system/editboard.html",{'board':board}))

def delete_personal_board(request):
	board_id = request.GET.get('board_id')
	cursor = connection.cursor()
	cursor.execute('delete from personal_board_system_personalboard where id = %s',[board_id])
	return(redirect('personal_board'))

def edit_title_personal_board_list(request):
	user=request.user
	if(request.method=='POST'):
		title = request.POST.get('title')
		list_id = request.POST.get('list_id')
		id = user.id
		cursor = connection.cursor()
		cursor.execute('update personal_board_system_personalboardlist set title=%s where id = %s',[title,list_id])
		return(redirect('personal_board'))
	# else:
	# 	form = AddBoardForm()
	board_id = request.GET.get('board_id')
	board = PersonalBoard.objects.get(id=board_id)
	list_id = request.GET.get('list_id')
	list = PersonalBoardList.objects.get(id = list_id)
	return(render(request,"personal_board_system/editboardlist.html",{'board':board,'list':list}))

def delete_personal_board_list(request):
	board_id = request.GET.get('board_id')
	list_id = request.GET.get('list_id')
	list = PersonalBoardList.objects.get(id= list_id)
	list.delete()
	return(redirect('personal_board'))

def edit_personal_board_list_card(request):
	user=request.user
	if(request.method=='POST'):
		title = request.POST.get('title')
		due_date = request.POST.get('due_date')
		attachment = request.POST.get('attachment')
		list_id = request.POST.get('list_id')
		board_id = request.POST.get('board_id')
		card_id = request.POST.get('card_id')
		id = user.id
		card = PersonalBoardListCard.objects.get(id = card_id)
		card.title = title
		card.due_date = due_date
		card.attachment = attachment
		card.save()
		return(redirect('personal_board'))
	# else:
	# 	form = AddBoardForm()
	board_id = request.GET.get('board_id')
	board = PersonalBoard.objects.get(id=board_id)
	list_id = request.GET.get('list_id')
	list = PersonalBoardList.objects.get(id = list_id)
	card_id = request.GET.get('card_id')
	card = PersonalBoardListCard.objects.get(id= card_id)
	return(render(request,"personal_board_system/editboardlistcard.html",{'board':board,'list':list,'card':card}))

def delete_personal_board_list_card(request):
	board_id = request.GET.get('board_id')
	list_id = request.GET.get('list_id')
	card_id = request.GET.get('card_id')
	card = PersonalBoardListCard.objects.get(id= card_id)
	card.delete()
	return(redirect('personal_board'))

def archive_personal_board_list_card(request):
	card_id = request.GET.get('card_id')
	card = PersonalBoardListCard.objects.get(id = card_id)
	card.archived=True
	card.save()
	return(redirect('personal_board'))
