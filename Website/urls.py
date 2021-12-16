from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('playerlogin', views.playerlogin, name='playerlogin'),
	path('stafflogin', views.stafflogin, name='stafflogin'),
	path('register', views.register, name='register'),
	path('playerpage', views.playerpage, name='playerpage'),
	path('supportstaffpage', views.supportstaffpage, name='supportstaffpage'),
	path('coachpage', views.coachpage, name='coachpage'),
	path('docpagediet', views.docpagediet, name='docpagediet'),
	path('docpagephysio', views.docpagephysio, name='docpagephysio'),
	path('schedulepage', views.schedulepage, name='schedulepage'),
	path('statspage', views.statspage, name='statspage'),
	path('manager', views.manager, name='manager'),
	path('addaplayer', views.addaplayer, name='addaplayer'),
	path('deleteaplayer', views.deleteaplayer, name='deleteaplayer'),
	path('reviewcontracts', views.reviewcontracts, name='reviewcontracts'),
	path('expiringcontracts', views.expiringcontracts, name='expiringcontracts'),
	path('managerlogin', views.managerlogin, name='managerlogin'),
	path('injuries', views.injuries, name='injuries'),
	path('currentteam', views.currentteam, name='currentteam'),
	path('schedulenowpage', views.schedulenowpage, name='schedulenowpage'),
	path('matchstatspage', views.matchstatspage, name='matchstatspage'),
	path('healthdata', views.healthdata, name='healthdata'),
	path('commentadded', views.commentadded, name='commentadded'),
	path('fouls', views.fouls, name='fouls'),
	path('matches', views.matches, name='matches'),



]
