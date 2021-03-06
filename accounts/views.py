import csv
import io
import math
import json


import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.template import Context, Template
from amortization.schedule import amortization_schedule

from .models import loan


# Create your views here.

def home(request):
    return render(request, 'home.html')


def loaddata(request):
    csvinfo = loan.objects.filter().order_by('-id')[:0][::-1]
    return render(request, 'loaddata.html', {'data': csvinfo})
def loandata(request):
    if request.method=='GET':
        return render(request,'loandata.html')
    p=request.POST['loan_amount']
    r=request.POST['interest_rate']
    t=request.POST['loan_period']
    p=float(p)
    r=float(r)
    t=float(t)

    m=(p*(r/12)*(math.pow(1+r/12,12*t)))/(math.pow(1+r/12,12*t)-1)
    #print(str(round(m,2)))
    month=12*t
    month=int(month)
    stbalance=p
    endbalance=p
    
    data = {"sn": [], "pa": [], "m": [],"iap": [], "lob": []}
    for number, amount, interest, principal, balance in amortization_schedule(p, r, month):
        print(number,round(amount,2),round(interest,2), round(principal,2), round(balance,2))
        data["sn"].append(str(number))
        data["pa"].append(str(round(amount,2)))
        data["m"].append(str(round(principal,2)))
        data["iap"].append(str(round(interest,2)))
        data["lob"].append(str(round(balance,2)))
        
    #print(data)
    
    csv_file = pd.DataFrame(data)
    #result = json.dumps(data) 
    #context = Context(data)
    #print(context)
    #print(csv_file)
    for index, row in csv_file.iterrows():
        
        
        _,created = loan.objects.update_or_create(
            
            sn=row['sn'],
            pa=row['pa'],
            pap=row['m'],
            iap=row['iap'],
            lob=row['lob'],
        )
    csvinfo = loan.objects.filter().order_by('-id')[:month][::-1]
    return render(request, 'loaddata.html', {'data': csvinfo})


    

    

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'USER already exist')
            return redirect('/signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email taken')
            return redirect('/signup')
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            print('user created')
            return redirect('login')
        return redirect('/')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

