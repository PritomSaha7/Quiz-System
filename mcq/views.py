from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import AllQuestionsForm, CustomUserCreationForm, loginForm, UpdateCustomUserCreationForm
from .models import AllQuestions, Result, CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import datetime

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html', {})

def CalcResult(request):
    subject = request.POST.get("subject")
    # check user already participated in this subject or not 
    UserName = request.user.username
    if Result.objects.filter(StudentName = UserName, SubjectName = subject):
        messages.info(request, 'You have already participated in ' + subject + ' test')
        return redirect('all-subjects')
    
    question_set = AllQuestions.objects.all()
    cnt_rightanswer = 0
    cnt_question = 0
    for it in question_set:
        if it.subject == subject:
            cnt_question += 1
            if it.answer == request.POST.get(it.question):
                cnt_rightanswer += 1
    cnt_wronganswer = cnt_question - cnt_rightanswer
    success_rate = int((cnt_rightanswer / cnt_question) * 100)
    grade = 'F'
    if success_rate >= 80:
        grade = 'A+'
    elif success_rate >= 70:
        grade = 'A'
    elif success_rate >= 60:
        grade = 'A-'
    elif success_rate >= 50:
        grade = 'B'
    elif success_rate >= 40:
        grade ='C'
    elif success_rate >= 33:
        grade = 'D'
    else:
        grade = 'F'
    
    print("_________________________")
    print(cnt_question)
    print(cnt_rightanswer)
    print(cnt_wronganswer)
    print(success_rate)
    print(grade)
    print("_________________________")
    
    instance = Result()
    instance.StudentName = request.user.username
    instance.SubjectName = subject
    instance.CntQuestion = cnt_question
    instance.CntCorrectAns = cnt_rightanswer
    instance.CntWrongAns = cnt_wronganswer
    instance.SuccessRate = success_rate
    instance.Grade = grade 
    instance.created_at = datetime.datetime.now()
    instance.save()
    
    result_sheet = {
        'cnt_question': cnt_question,
        'cnt_rightanswer': cnt_rightanswer,
        'cnt_wronganswer': cnt_wronganswer,
        'success_rate': success_rate,
        'grade': grade,
    }
    return render(request, 'result.html', result_sheet)

def Questions(request):
    print(request.POST)
    subject_name = request.POST.get("sub_name")
    question_set = AllQuestions.objects.filter(subject = subject_name).values()
    return render(request, 'Questions.html', {'question': question_set, 'subject': subject_name})

def AllSubjects(request):
    subjects_tuple = AllQuestions.objects.order_by().values_list('subject').distinct()
    subjects = []
    for i in subjects_tuple:
        sub = list(i)
        subjects.append(sub[0])
    return render(request, 'AllSubjects.html', {'subjects': subjects})

def base(request):
    return render(request, 'base.html', {})
    

def SetQuiz(request):
    submitted = False
    if request.method == "GET":
        form = AllQuestionsForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'set_quiz.html', {'form': form, 'submitted': submitted})
    else:
        form = AllQuestionsForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Profile details updated.")
        return HttpResponseRedirect('set-quiz?submitted=True')
    

def Signup(request):
    if request.method == "GET":
        form = CustomUserCreationForm
        return render(request, 'SignupPage.html', {'form': form})
    else:
        form = CustomUserCreationForm(request.POST, request.FILES)
        ABC = request.POST.get('user_type')
        print(ABC)
        print(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username = username, password = password)
            login(request, user)
            return redirect('home-page')
        
        f = True
        query = CustomUser.objects.filter(username = request.POST.get('username'))

        if query:
            messages.error(request, 'Username already exists')
            f = False
        if int(len(request.POST.get('password1'))) < 8:
            messages.error(request, 'Password length should be at least 8')
            f = False
        if request.POST.get('password1') != request.POST.get('password2'):
            messages.error(request, 'Both password should be same')
            f = False
        if f:
            messages.error(request, 'Password is too common')

        return redirect('sign-up')
    
def Login(request):
    if request.method == "GET":
        form = loginForm
        return render(request, 'LoginPage.html', {'form': form})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home-page')

        messages.error(request, 'Wrong username and password')
        return redirect('log-in')
    
def Logout(request):
    logout(request)
    return redirect('home-page')

def ProfilePage(request):
    return render(request, 'ProfilePage.html', {})

def ResultHistory(request):
    result = Result.objects.filter(StudentName = request.user.username)  
    return render(request, 'ResultHistory.html', {'result': result})
           
def UpdateProfile(request):
    if request.method == "GET":
        form = UpdateCustomUserCreationForm(instance = request.user)
        return render(request, 'UpdateProfile.html', {'form': form})
    else:
        form = UpdateCustomUserCreationForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            login(request, user)

            return redirect('profile-page')
        
        return redirect('update-profile')
    
    
def UpdateQuestion(request, idNum):
    if request.method == "GET":
        obj = AllQuestions.objects.get(pk = idNum)
        form = AllQuestionsForm(instance = obj)
        return render(request, 'set_quiz.html', {'form': form})
    else:
        obj = AllQuestions.objects.get(pk = idNum)
        form = AllQuestionsForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('all-subjects')
        

def DeleteQuestion(request, idNum):
    obj = AllQuestions.objects.get(pk = idNum)
    obj.delete()
    return redirect('all-subjects')
        
        