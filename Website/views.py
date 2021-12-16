from django.shortcuts import render, redirect
from .models import Player
# from .forms import PlayerForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db import connection
import pandas as pd

# Create your views here.
def home(request):
	# all_players = Player.objects.all 
	# return render(request, 'home.html', {'all': all_players})
	return render(request, 'home.html')

def playerlogin(request):
	if request.method == "POST":
		login_name = request.POST['user']
		login_password = request.POST['passwd']
		user = authenticate(username = login_name, password = login_password)

		# query = Player.objects.raw('Select * from nbaproject.player where player_id = %s', [login_password])
		# #print(query)

		cursor = connection.cursor()
		cursor.execute('Select * from nbaproject.player where player_id = %s', [login_password])
		row = cursor.fetchone()
		row1 = list(row)
		player_fields = ['player_id', 'player_name', 'age' ,'date_of_birth', 'pos', 'height', 'weight', 'status']
		row2 = dict(zip(player_fields, row1))
		if user is not None:
			# login(request, user)
			return render(request, 'playerpage.html', {'query1': row2})
		else:
			messages.error(request, "Wrong user!")
			return redirect('home.html')

	else:
		return render(request, 'playerlogin.html')

def stafflogin(request):
	#return HttpResponse('Hello!! Staff Login page here')
	return render(request, 'stafflogin.html')

def register(request):
	if request.method == "POST":
		name = request.POST['p_name']
		team_id = request.POST['team_id']
		season_year = request.POST['season_year']
		player_id = request.POST['player_id']
		date_of_birth = request.POST['date_of_birth']
		position = request.POST['position']
		height = request.POST['height']
		weight = request.POST['weight']

		myuser = User.objects.create_user(username = name, password = player_id)
		myuser.save()

		print(request, "Registered Successfully!")
		return redirect('/playerlogin')

	return render(request, 'register.html')

def playerpage(request):
	if request.method == "GET":
		cursor = connection.cursor()
		cursor.execute('select * from valid_schedule')
		obj = cursor.fetchall()
		row1 = list(obj)
		main_ls = []
		player_fields = ['schedule_id', 'practice_date', 'practice_day', 'practice_time', 'no_of_hours','session_name']
		for i in row1:
			row2 = dict(zip(player_fields, i))
			main_ls.append(row2)
		#obj1 = pd.DataFrame(obj, columns = ['player_id', 'player_name', 'fa_year', 'salary', 'aav'])
	
		return render(request, 'schedulepage.html', {'obj': main_ls})

	return render(request, 'playerpage.html')

def supportstaffpage(request):
	return render(request, 'supportstaffpage.html')

def coachpage(request):
	return render(request, 'coachpage.html')

def docpagediet(request):
	return render(request, 'docpagediet.html')

def docpagephysio(request):
	return render(request, 'docpagephysio.html')

def schedulepage(request):
	if request.method == "GET":
			
		cursor = connection.cursor()
		cursor.execute('select * from valid_schedule')
		obj = cursor.fetchall()
		row1 = list(obj)
		main_ls = []
		player_fields = ['schedule_id', 'practice_date', 'practice_day', 'practice_time', 'no_of_hours','session_name']
		for i in row1:
			row2 = dict(zip(player_fields, i))
			main_ls.append(row2)
		#obj1 = pd.DataFrame(obj, columns = ['player_id', 'player_name', 'fa_year', 'salary', 'aav'])
	
		return render(request, 'schedulepage.html', {'obj': main_ls})


	return render(request, 'schedulepage.html')

def statspage(request):
	if request.method == "GET":
		# match_id = request.POST['match_id']
		# player_id = request.POST['player_id']

		cursor = connection.cursor()
		cursor.execute('call get_player_average(60);')
		obj = cursor.fetchone()
		row1 = list(obj)
		#row1 = [0 if i is None else i for i in list(obj)]
		# main_ls = []
		player_fields = ['player_id', 'avg_points', 'avg_rebounds','avg_assists','avg_steals','avg_blocked_shots','avg_fouls']
		# for i in row1:
		row2 = dict(zip(player_fields, row1))
			# main_ls.append(row2)
		#obj1 = pd.DataFrame(obj, columns = ['player_id', 'player_name', 'fa_year', 'salary', 'aav'])
	
		return render(request, 'statspage.html', {'obj': row2})


	return render(request, 'statspage.html')

def manager(request):
	return render(request, 'manager.html')

def addaplayer(request):
	if request.method == "POST":
		player_name = request.POST['player_name']
		player_id = request.POST['player_id']
		age = request.POST['age']
		date_of_birth = request.POST['date_of_birth']
		pos = request.POST['pos']
		height = request.POST['height']
		weight = request.POST['weight']
		status = 'Active'


		cursor = connection.cursor()
		cursor.execute('insert into player values (%s,%s,%s,%s,%s,%s,%s,%s)',[player_id, player_name, age, date_of_birth, pos, height, weight, status])
		return redirect('/supportstaffpage')	
	


	return render(request, 'addaplayer.html')

def deleteaplayer(request):
	if request.method == "POST":
		player_id = request.POST['player_id']	
		cursor = connection.cursor()
		cursor.execute('delete from player where player_id = %s',[player_id])
		return redirect('/supportstaffpage')

	return render(request, 'deleteaplayer.html')

def reviewcontracts(request):
	if request.method == "POST":

		player_id = request.POST['player_id']
			
		cursor = connection.cursor()
		cursor.execute('call review_contracts(%s)', [player_id])
		obj = cursor.fetchone()

		row1 = list(obj)
		player_fields = ['player_id', 'player_name', 'start_year', 'end_year', 'fa_year' ,'salary', 'aav']
		row2 = dict(zip(player_fields, row1))
		
	
		return render(request, 'reviewcontracts.html', {'obj': row2})
		
	return render(request, 'reviewcontracts.html')

def expiringcontracts(request):
	if request.method == "GET":
			
		cursor = connection.cursor()
		cursor.execute('select * from contracts_expiring')
		obj = cursor.fetchall()
		row1 = list(obj)
		main_ls = []
		player_fields = ['player_id', 'player_name', 'fa_year' ,'salary', 'aav']
		for i in row1:
			row2 = dict(zip(player_fields, i))
			main_ls.append(row2)
		#obj1 = pd.DataFrame(obj, columns = ['player_id', 'player_name', 'fa_year', 'salary', 'aav'])
	
		return render(request, 'expiringcontracts.html', {'obj': main_ls})

	return render(request, 'expiringcontracts.html')

def managerlogin(request):
	return render(request, 'managerlogin.html')

def injuries(request):
	if request.method == "GET":
		value = 'Injured'
		cursor = connection.cursor()
		cursor.execute('select player_id, player_name from player where status = %s',[value])
		obj = cursor.fetchall()
		row1 = list(obj)
		main_ls = []
		player_fields = ['player_id', 'player_name']
		for i in row1:
			row2 = dict(zip(player_fields, i))
			main_ls.append(row2)
			#obj1 = pd.DataFrame(obj, columns = ['player_id', 'player_name', 'fa_year', 'salary', 'aav'])
		
		return render(request, 'injuries.html', {'obj': main_ls})

	return render(request, 'injuries.html')

def currentteam(request):
	if request.method == "GET":		
		cursor = connection.cursor()
		cursor.execute('select * from list_of_current_players')
		obj = cursor.fetchall()
		row1 = list(obj)
		main_ls = []
		player_fields = ['player_id', 'player_name', 'team_id' ,'year']
		for i in row1:
			row2 = dict(zip(player_fields, i))
			main_ls.append(row2)
		#obj1 = pd.DataFrame(obj, columns = ['player_id', 'player_name', 'fa_year', 'salary', 'aav'])
	
		return render(request, 'currentteam.html', {'obj': main_ls})
	return render(request, 'currentteam.html')

def schedulenowpage(request):
	if request.method == "GET":
			
		cursor = connection.cursor()
		cursor.execute('select * from today_schedule')
		obj = cursor.fetchall()
		row1 = list(obj)
		main_ls = []
		player_fields = ['schedule_id', 'practice_date', 'practice_day', 'practice_time', 'no_of_hours','session_name']
		for i in row1:
			row2 = dict(zip(player_fields, i))
			main_ls.append(row2)
		return render(request, 'schedulenowpage.html', {'obj': main_ls})

	return render(request, 'schedulenowpage.html')

def matchstatspage(request):
	if request.method == "POST":
		match_id = request.POST['match_id']
		player_id = request.POST['player_id']

		cursor = connection.cursor()
		cursor.execute('call stats_in_match_by_player(%s,%s); ',[match_id, player_id])
		obj = cursor.fetchone()
		
		row1 = [0 if i is None else i for i in list(obj)]
		player_fields = ['Offensive_rebound', 'Defensive_rebounds', 'rebounds', 'assists', 'steals', 'blocked_shots', 'turnovers', 'personal_fouls', 'points_scored', 'player_id', 'match_id']
		row2 = dict(zip(player_fields, row1))
		return render(request, 'matchstatspage.html', {'obj': row2})

	return render(request, 'matchstatspage.html')

def healthdata(request):
	if request.method == "POST":

		player_id = request.POST['player_id']
			
		cursor = connection.cursor()
		cursor.execute('call health_data_dietician(%s)', [player_id])
		obj = cursor.fetchone()

		row1 = list(obj)
		player_fields = ['player_name', 'check_up_date','bp', 'cholestrol', 'bpm', 'oxygen']
		row2 = dict(zip(player_fields, row1))
		
	
		return render(request, 'healthdata.html', {'obj': row2})

	return render(request, 'healthdata.html')


def commentadded(request):
	if request.method == "POST":

		comment = request.POST['comment']
			
		cursor = connection.cursor()
		cursor.execute('update check_up set d_comment= %s where player_id =%s', [comment, obj.player_id])
		return render(request, 'commentadded.html', {'obj': row2})

	return render(request, 'commentadded.html')

def fouls(request):
	if request.method == "GET":	
		cursor = connection.cursor()
		cursor.execute('select total_fouls_player(200)')
		obj = cursor.fetchone()
		return render(request, 'fouls.html', {'obj': obj})

	return render(request, 'fouls.html')

def matches(request):
	if request.method == "GET":	
		cursor = connection.cursor()
		cursor.execute('select total_matches_played(200)')
		obj = cursor.fetchone()
		return render(request, 'matches.html', {'obj': obj})

	return render(request, 'matches.html')


