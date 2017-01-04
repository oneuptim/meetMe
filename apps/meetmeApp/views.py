from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
# from . import models
from .models import User



def index(request):
	return render(request, 'meetmeApp/index.html')

def register_process(request):

	if request.method == "POST":
		result = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'], request.POST['confirm_password'])

		if result[0]==True:
			request.session['id'] = result[1].id
			# print result, "***************"
			# request.session.pop('errors')
			return redirect('/')
		else:

			# request.session['errors'] = result[1]
			messages.add_message(request, messages.WARNING, result[1][0])

			# print result[1], "***************"
			return redirect('/dashboard')
	else:

		return redirect ('/')

def login(request):
	return render(request, 'meetmeApp/login.html')

def login_process(request):
	result = User.objects.login(request.POST['email'],request.POST['password'])

	if result[0] == True:
		request.session['id'] = result[1][0].id
		return redirect('/dashboard')
	else:
		messages.add_message(request, messages.WARNING, result[1][0])
		return redirect('/login')

# def users(request, id):
# 	if not 'id' in request.session :
# 		return redirect('/')
# 	else:
# 		session = request.session['id']
# 		loggedInUser = User.objects.filter(id=session)
# 		user = User.objects.filter(id=session)
# 		userName = user[0].first_name
#
# 		allQuotes = Quote.objects.filter(user__id=id).order_by('-created_at')
# 		quoteCount = allQuotes.count()
#
# 		data = {
# 			'allQuotes': allQuotes,
# 			'userName': userName,
# 			'quoteCount': quoteCount,
# 			'loggedInUser': loggedInUser[0].first_name,
# 			'quotePosterUserName': allQuotes[0].user.first_name,
# 			'sessionID': session
# 		}
#
# 	return render(request, "myapp/users.html", data)

def dashboard(request):

	if not 'id' in request.session :
		return redirect('/')
	else:
		session = request.session['id']

		loggedInUser = User.objects.filter(id=session)

		# (favoritequote__user__id=session)

		# schedule = Trip.objects.filter(participant_id=session).order_by('-created_at')
		# joined_trips = Schedule.objects.filter(participant_id=session).order_by('-created_at')

		# just_joined_trips = []
		# for trip in joined_trips:
		# 	just_joined_trips.append(trip.trip)
		#
		# all_trips = Trip.objects.exclude(participant_id=session).order_by('-created_at')

		# for trip in all_trips: # Trip table

			# for trip in joined_trips: # Schedule table
			# 	print trip.trip.id, "^"*100
			#
			# 	if trip.id == trip.trip.id:
			# 		all_trips_minus_joined_trips = Trip.objects.filter(id = trip.trip.id).order_by('-created_at')
			#
			# print trip.id, "@"*100

		data = {

		'loggedInUser' : loggedInUser[0],
		# 'schedule' : schedule,
		# 'all_trips' : all_trips,
		# 'joined_trips': joined_trips,
		# 'just_joined': just_joined_trips
		}

		return render(request, 'meetmeApp/dashboard.html', data)

def edit(request):
	return redirect('/dashboard')

def logout(request)	:
	del request.session['id']
	return render (request, 'meetmeApp/logout.html')
