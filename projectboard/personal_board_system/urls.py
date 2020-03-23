"""projectboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('personal_board/',views.personal_board,name="personal_board"),
    path('personal_board_lists/',views.personal_board_list,name="personal_board_list"),
    path('personal_board_list_cards/',views.personal_board_list_card,name="personal_board_list_card"),
    path('addpersonalboard/',views.add_personal_board),
    path('addpersonalboardlist/',views.add_personal_board_list),
    path('addpersonalboardlistcard/',views.add_personal_board_list_card),
    path('edittitlepersonalboard/',views.edit_title_personal_board),
    path('deletepersonalboard/',views.delete_personal_board),
    path('edittitlepersonalboardlist/',views.edit_title_personal_board_list),
    path('deletepersonalboardlist/',views.delete_personal_board_list),
    path('edittitlepersonalboardlistcard/',views.edit_personal_board_list_card),
    path('deletepersonalboardlistcard/',views.delete_personal_board_list_card),
    path('archivepersonalboardlistcard/',views.archive_personal_board_list_card),
    
    # path('edittitlepersonalboardlist/',views.edit_title_personal_board_list),
    # path('editpersonalboardlistcard/',views.edit_title_personal_board_list_card),
    
]
