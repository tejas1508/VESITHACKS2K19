from django.http import HttpResponse
from django.shortcuts import render,redirect
#from django.db import connection
#from .models import EvaluationApp
from django.template import loader
#from django.template import context
#import mysql.connector
from EvaluationApp.forms import LoginForm
# from django.db.models import Q
from django.contrib import messages
from .models import User,Evaluates,HRassessment,Report
from django.shortcuts import render_to_response
import random
import datetime
import time


def index(request):
	return render(request,"EvaluationApp/landing_page.html")
# Create your views here.

def Login(request):
	return render(request,"EvaluationApp/loginpage.html")

def openadmin(request):
	return render(request,"EvaluationApp/admin-dashboard.html")

def openemp(request):
	return render(request,"EvaluationApp/employeedash.html")

def opendept(request):
	return render(request,"EvaluationApp/dept-dashboard.html")

def openrpt(request):
	return render(request,"EvaluationApp/reportform.html")


# def authlogin(request):
# 	if request.method =='POST':
# 		details = LoginForm(request.POST)
# 		if (details.is_valid()):
# 			return redirect('EvaluationApp/landing page.html')
# 		users = User.objects.get.all()
# 		for user in users:
# 			if details.user == user.email and details.password == user.password:
# 				if user.role == "admin":
# 					return HttpResponse("<h1>Hii admin</h1>",csrfContext)

		
# 		return HttpResponse("<h1>Failed</h1>",)		
		
def verifyLogin(request):
	try:
		if request.method == 'POST':
			email = request.POST['email']
			pwd = request.POST['password']
			user = User.objects.get(email = email)
			
			if pwd == user.password:
				request.session['logged_in'] = user.id
				if user.role == 'ADMIN':
					return redirect('/adminDashboard/')
				elif user.role == 'MD':
					return redirect('/mdDashboard/')
				elif user.role == 'HR':
					return redirect('/hrDashboard/')
				elif user.role == 'DH':
					return redirect('/dhDashboard/')
				elif user.role == 'DT':
					return redirect('/dtDashboard/')
				elif user.role == 'ASSOCIATE':
					return redirect('/associateDashboard/')
				elif user.role == 'EMPLOYEE':
					return redirect('/employeeDashboard/')
	except:
		return HttpResponse("Error!! Invalid Details")



def logout(request):
	try:
		del request.session['logged_in']
	except KeyError:
		pass
	return render(request,"EvaluationApp/landing_page.html")

def adminDash(request):
	# if request.user.is_authenticated:
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/admin-dashboard.html")
	else:
		return HttpResponse("Error")

def employeeDash(request):
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/employeedash.html")
	else:
		return HttpResponse("Error")
	

def mdDash(request):
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/mddashboard.html")
	else:
		return HttpResponse("Error")

def hrDash(request):
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/supervisordash.html")
	else:
		return HttpResponse("Error")

def dtDash(request):
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/dept-dashboard.html")
	else:
		return HttpResponse("Error")

def dhDash(request):
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/departmenthead.html")
	else:
		return HttpResponse("Error")

def associateDash(request):
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/associatedash.html")
	else:
		return HttpResponse("Error")

# def employeeDash(request):
# 	if(request.session['logged_in']):
# 		return render(request,"EvaluationApp/employeedash.html")
# 	else:
# 		return HttpResponse("Error")

def adduser(request):
	return render(request,"EvaluationApp/adduser.html")

def updateuser(request):
	return render(request,"EvaluationApp/updateUser.html")

def deleteuser(request):
	return render(request,"EvaluationApp/deleteuser.html")

def viewhierarchy(request):
	return render(request,"EvaluationApp/viewhierarchy.html")
	


def search(request):
	if request.method == 'POST':
		srch = request.POST['srh']

		if srch:
			match = User.objects.filter(email=srch)

			if match:
				return render(request,'EvaluationApp/admin-dashboard.html/',{'srh':match})
			else:
				messages.error(request,'No User Found')
		else:
			return redirect('landing_page/')


def adduser_database(request):
	if request.method == 'POST':
		name = request.POST['name']
		username = request.POST['username']
		id = request.POST['id']
		email = request.POST['email']
		pwd = request.POST['password']
		role = request.POST['role']
		dno = request.POST['dno']

		newuser = User()
		newuser.id = id
		newuser.email = email
		newuser.role = role
		newuser.password = pwd
		newuser.dno = dno
		newuser.save()
		return render(request,'EvaluationApp/admin-dashboard.html/')

def updateuser_database(request):
	if request.method == 'POST':
		id = request.POST['id']
		email = request.POST['email']
		pwd = request.POST['password']
		role = request.POST['role']
		dno = request.POST['dno']

		user = User.objects.get(id = id)
		user.email = email
		user.role = role
		user.password = pwd
		user.dno = dno
		user.save()
		return render(request,'EvaluationApp/admin-dashboard.html/')

def deleteuser_database(request):
	if request.method == 'POST':
		id = request.POST['id']

		user = User.objects.get(id = id)
		user.delete()

		return render(request,'EvaluationApp/admin-dashboard.html/')

def evaluateHR(request):
	return render(request, 'EvaluationApp/evaluateHR.html')

def evaluateOperationsDept(request):
	return render(request, 'EvaluationApp/evaluateOperationsDept.html')

def evaluatePublicRelationsDept(request):
	return render(request, 'EvaluationApp/evaluatePublicRelationsDept.html')

def evaluateTreasuryDept(request):
	return render(request, 'EvaluationApp/evaluateTreasuryDept.html')

def evaluateTechnicalDept(request):
	return render(request, 'EvaluationApp/evaluateTechnicalDept.html')

def evaluateCreativityDept(request):
	return render(request, 'EvaluationApp/evaluateCreativityDept.html')	

# HR ajax rendering

def reportform(request):
	return render(request, 'EvaluationApp/reportform.html')

def assessDepthead(request):
	return render(request, 'EvaluationApp/assessOperationsDept.html')

def assessDeptteam(request):
	return render(request, 'EvaluationApp/assessPRDept.html')

def assessAssociates(request):
	return render(request, 'EvaluationApp/assessTechnicalDept.html')

def assessEmployees(request):
	return render(request, 'EvaluationApp/assessTreasuryDept.html')

def getEmpDetails(request):
    if request.method == 'POST':
        id = request.POST['userid']

        u = Report.objects.get(user_id_id=id)
        r = u.report
        return render(request,"EvaluationApp/assessOperationsDept.html",{'report':r})

def submitHrReport(request):
    if request.method == 'POST':
        id = request.POST['userid']
        marks1 = request.POST['m1']
        marks2 = request.POST['m2']
        marks3 = request.POST['m3']
        marks4 = request.POST['m4']
        marks5 = request.POST['m5']
        comments = request.POST['remarks']

        s = HRassessment()
        s.hra1 = marks1
        s.hra2 = marks2
        s.hra3 = marks3
        s.hra4 = marks4
        s.hra5 = marks5
        s.hra_assessment_report = comments
        s.assessedby_id = request.session['logged_in']
        s.assessedof_id = id
        s.save()

        return render(request,"EvaluationApp/supervisordash.html")


def evlpr(request):
	if request.method == 'POST':
		user_id = request.POST['user_id']
		comments = request.POST['Comments']
		marks1 = request.POST['marks1']
		marks2 = request.POST['marks2']
		marks3 = request.POST['marks3']
		marks4 = request.POST['marks4']
		marks5 = request.POST['marks5']
		marks6 = request.POST['marks6']
		marks7 = request.POST['marks7']
		marks8 = request.POST['marks8']
		marks9 = request.POST['marks9']
		marks10 = request.POST['marks10']
		myid = request.session['logged_in']
		table = Evaluates()
		table.evaluated_by = User.objects.get(id =myid)
		table.evaluation_of = User.objects.get(id = user_id)
		table.e1 = marks1
		table.e2 = marks2
		table.e3 = marks3
		table.e4 = marks4
		table.e5 = marks5
		table.e6 = marks6
		table.e7 = marks7
		table.e8 = marks8
		table.e9 = marks9
		table.e10 = marks10
		table.save()
	return redirect('/mdDashboard/')

def heirar(request):
	return render(request, 'EvaluationApp/vieweirarchy.html')

def viewGraph(request):
	return render(request, 'EvaluationApp/viewGraph.html')

def fetchGraphValues(request):
	if request.method == 'POST':
		id = request.POST['userid']
		s = HRassessment.objects.get(assessedof_id = id)

		xdata = ["hra1", "hra2", "hra3", "hra4", "hra5"]
		ydata = [s.hra1, s.hra2, s.hra3, s.hra4, s.hra5]

		extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
		chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
		charttype = "pieChart"

		data = {
			'charttype': charttype,
			'chartdata': chartdata,
		}
		return render_to_response('viewGraph.html', data)