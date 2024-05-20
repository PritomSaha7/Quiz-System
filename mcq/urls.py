from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'home-page'),
    path('set-quiz', views.SetQuiz, name = 'set-quiz'),
    path('all-subjects', views.AllSubjects, name = 'all-subjects'),
    path('questions', views.Questions, name = 'questions'),
    path('calc-result', views.CalcResult, name = 'calc-result'),
    path('log-in', views.Login, name = 'log-in'),
    path('log-out', views.Logout, name = 'log-out'),
    path('sign-up', views.Signup, name = 'sign-up'),
    path('profile-page', views.ProfilePage, name = 'profile-page'),
    path('result-history', views.ResultHistory, name = 'result-history'),
    path('update-profile', views.UpdateProfile, name = "update-profile"),
    path('update-question<idNum>', views.UpdateQuestion, name = 'update-question'), 
    path('delete-question<idNum>', views.DeleteQuestion, name = 'delete-question'), 
]
