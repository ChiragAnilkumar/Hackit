from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


#def hello_world(request):
			#data ={}
			#return render(request,"Hello.html",data)
def home(request):
	return render(request,"home.html")
def login_view(request):
			if request.method=="POST":
				username= request.POST.get("uname")
				password=request.POST.get("psw")
				user=authenticate(username=username,password=password)
				if user:
					login(request,user)
					return redirect("/welcome")
				else:
					return render(request,"login2.html",{"message":"User not Found"})

			else:
				return render(request,"login2.html")
def signup(request):
	if request.method=="POST":
				username= request.POST.get("uname")
				password=request.POST.get("psw")
				u=User.objects.create_user(username=username,password=password)
				if u:
					login(request,u)
					return redirect("/")
	else:
		return render(request,"signup.html")
def welcome(request):
	user=request.user
	print(user.username)
	data={'user':user.username}
	return render (request,"welcome.html",data)
def logout_view(request):
	logout(request)
	return redirect("/")
def todo(request):
	to=todo.object.all()
	data={'todolist':to}
	return render(request,"todolist.html",data)
			

			
