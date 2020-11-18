from django.urls import path

from .views import *

app_name="newsvendor"
urlpatterns=[
    path("",index,name="index"),
    path("2",index2,name="index2"),
    path("roundOver",roundOver,name="roundOver"),
    path("roundOver2",roundOver2,name="roundOver2"),
    path("checkEmail",checkEmail.as_view()),
    path("userSubmit",userSubmit.as_view()),
    path("roundSubmit",roundSubmit.as_view()),
    path("feedback",submitfeedback.as_view()),
    path("download",downloadfile,name="download"),
    path("fetchuser",fetchRecords.as_view()),
    path("fetchfeedback",fetchfeedback.as_view()),
    path("fetchrounds", fetchRounds.as_view()),
]