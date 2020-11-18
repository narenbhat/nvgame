from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views import View
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse
from django import forms
from . import models
import sqlite3
import json
import psycopg2

from .models import *


# Create your views here.
no_of_questions = question.objects.count()

def index(request):
    return render(request,"newsvendor/index.html")

def index2(request):
    return render(request,"newsvendor/index2.html")

def roundOver(request):
    return render(request,"newsvendor/roundOver.html")

def roundOver2(request):
    return render(request,"newsvendor/roundOver2.html")

def downloadfile(request):
    return render(request,"newsvendor/download.html")


class checkEmail(View):
    def get(self, request):
        email_id = request.GET['email']
        game_name = request.GET['gamename']
        a = user.objects.filter(email=email_id,gamename=game_name).exists()
        return HttpResponse(a)

class userSubmit(View):
    def get(self, request):
        uemail = request.GET['email']
        uname = request.GET['name']
        ugender = request.GET['gender']
        uage = request.GET['age']
        uorganisation = request.GET['organisation']
        udesignation = request.GET['designation']
        ugameName = request.GET['gamename']
        u = user(
            name = uname,
            email = uemail,
            gender = ugender,
            age = uage,
            organisation = uorganisation,
            designation = udesignation,
            gamename = ugameName
            )
        u.save()
       # que = question.objects.filter(qid = 1)
        q = {
                'uid' : u.uid
        }
        return JsonResponse(q)


class roundSubmit(View):
    def get(self,request):
        uid = request.GET['uid']
        pf = request.GET['point_forecast']
        lb = request.GET['LB']
        ub = request.GET['UB']
        tf = request.GET['target_fill_rate']

        a = answer(
            uid = uid,
            qid=0,
            point_forecast = pf,
            LB = lb,
            UB = ub,
            target_fill_rate = tf
            )
        a.save()
        # que = question.objects.filter(qid = 1)
        q = {
            'qid': 0
        }
        return JsonResponse(q)

class submitfeedback(View):
        def get(self, request):
            uid = request.GET['uid']
            fd = request.GET['feedback']

            a = feedback(
                uid=uid,
                feedback=fd,
            )
            a.save()
            # que = question.objects.filter(qid = 1)
            q = {
                'qid': 0
            }
            return JsonResponse(q)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class fetchRecords(View):
    def get(self, request):
        # # Connecting to sqlite
        # conn = sqlite3.connect('db.sqlite3')
        # # Creating a cursor object using the cursor() method
        # cursor = conn.cursor()
        # # Retrieving data
        # rows = cursor.execute('''SELECT u.name as name from newsvendor_user u''')
        # # Fetching 1st row from the table
        # result = cursor.fetchone();
        # # Fetching 1st row from the table
        # result = cursor.fetchall();
        # print(rows)
        # # Commit your changes in the database
        # conn.commit()
        # # Closing the connection
        # conn.close()
        connection = sqlite3.connect("db.sqlite3")
        connection.row_factory = dict_factory
        cursor = connection.cursor()
        cursor.execute("select * from newsvendor_user")
        # fetch all or one we'll go for all.
        results = cursor.fetchall()
        json_string = json.dumps(results)
        connection.close()
        d2 = [results]

        return HttpResponse(d2)

class fetchfeedback(View):
        def get(self, request):
            uid = request.GET['uid']
            connection = sqlite3.connect("db.sqlite3")
            connection.row_factory = dict_factory
            cursor = connection.cursor()
            cursor.execute("select * from newsvendor_feedback where uid="+uid+"")
            # fetch all or one we'll go for all.
            results = cursor.fetchall()
            json_string = json.dumps(results)
            connection.close()
            d2 = [results]
            return HttpResponse(d2)


class fetchRounds(View):
    def get(self, request):
        uid = request.GET['uid']
        connection = sqlite3.connect("db.sqlite3")
        connection.row_factory = dict_factory
        cursor = connection.cursor()
        cursor.execute("select * from newsvendor_answer where uid=" + uid + "")
        # fetch all or one we'll go for all.
        results = cursor.fetchall()
        json_string = json.dumps(results)
        connection.close()
        d2 = [results]
        return HttpResponse(d2)
