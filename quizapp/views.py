from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.
# Controller - business logic
from quizapp.models import Question
from django.shortcuts import render

def index(request):
    questions_list = Question.objects.all()
    return render(request, "quizapp/index.html", {'questions_list':questions_list})

def detail(request, question_id):
    #Added comment
    message = ""
    is_correct = False
    if request.method == "POST":
        answer_id = int(request.POST.get("answer"))
        # print(answer_id)
        #question_id = request.POST.get("question_id")
        print(answer_id, question_id)
        question = Question.objects.get(id=question_id)

        for answer in question.answer_set.all():
            if answer.id == answer_id and answer.correct == True:
                message = "correct answer"
                is_correct = True
                break
        if not is_correct:
            message = "wrong answer"

    question = Question.objects.get(id=question_id)
    return render(request, "quizapp/detail.html", {'question':question,'message':message,'result':is_correct})

def login(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            message = "Either username or password is wrong"
        else:
            #message = "Login successful"
            return r
            
            edirect('index')
    return render(request,"quizapp/login.html",{'message': message})
