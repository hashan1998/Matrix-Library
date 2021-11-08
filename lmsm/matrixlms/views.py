from django.shortcuts import render
from django.db import connection

# Create your views here.
def my_custom_sql(self):
  with connection.cursor() as cursor:
    cursor.execute("SELECT MNIC FROM member WHERE Email = %s", [self.Email])
    row = cursor.fetchone()
  return row

def index(request):
  return render(request, 'matrixlms/index.html')

def LoginPage(request):
  return render(request, 'matrixlms/LoginPage.html')

def MemberRegisterPage(request):
  return render(request, 'matrixlms/MemberRegisterPage.html')

def MemberUser(request):
  loginas = request.POST.get('LoginAs')
  email = request.POST.get('email')
  password = request.POST.get('password')
  row = ["111A"]
  if loginas == '1':
    with connection.cursor() as cursor:
      cursor.execute("SELECT FirstName FROM admin WHERE Email = %s", [email])
      row = cursor.fetchone()
    if row == '111A':
      request.session['email'] = ["failed"]
      return render(request, 'matrixlms/MemberUser.html')
    else:
      request.session['email'] = row
      request.session['password'] = password
      request.session['loginas'] = loginas
      return render(request, 'matrixlms/MemberUser.html')
  else:
    with connection.cursor() as cursor:
      cursor.execute("SELECT FirstName FROM member WHERE Email = %s", [email])
      row = cursor.fetchone()
    if row != '111':
      request.session['email'] = row
      request.session['password'] = password
      request.session['loginas'] = loginas
      return render(request, 'matrixlms/MemberUser.html')
    else:
      request.session['email'] = "failed"
      return render(request, 'matrixlms/MemberUser.html')

def logout(request):
  try:
    del request.session['email']
  except:
    pass
  return render(request, 'matrixlms/index.html', {'alert_flag': True})


