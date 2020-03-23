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
    path('team_board/',views.team_board,name="team_board"),
    path('team_board_lists/',views.team_board_list,name="team_board_list"),
    path('team_board_list_cards/',views.team_board_list_card,name="team_board_list_card"),
    path('addteamboard/',views.add_team_board),
    path('addteamboardlist/',views.add_team_board_list),
    path('addteamboardlistcard/',views.add_team_board_list_card),
    path('addteamboardmember/',views.add_team_board_member),
    path('teamboardmember/',views.team_board_member),
    path('edittitleteamboard/',views.edit_title_team_board),
    path('deleteteamboard/',views.delete_team_board),
    path('edittitleteamboardlist/',views.edit_title_team_board_list),
    path('deleteteamboardlist/',views.delete_team_board_list),
    path('edittitleteamboardlistcard/',views.edit_team_board_list_card),
    path('deleteteamboardlistcard/',views.delete_team_board_list_card),
    path('archiveteamboardlistcard/',views.archive_team_board_list_card),
]
