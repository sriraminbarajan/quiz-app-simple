from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import Questions,Catagory

# # Create your views here.

# view function for register
def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("login")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "quiz/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "quiz/register.html",
                  context={"form":form})

# view function for logout

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")

# view function for login
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "quiz/login.html",
                    context={"form":form})


#view function for homepage

def home(request):
    
    choices=Catagory.objects.values()
    choices = [(entry['id'],entry['Quiz_category']) for entry in choices]
    print(choices)
# below shown is how the query: Category.objects.values() looks like 
# [{'id': 1, 'Quiz_category': 'general knowledge'}, {'id': 2, 'Quiz_category': 'real'}, {'id': 3, 'Quiz_category': 'fff'}]
    
    return render(request,
        'quiz/home.html',
        {'choices':choices})

# view function for questions

def questions(request , choice):
    print(choice)
    ques = Questions.objects.filter(catagory__exact = choice)
    return render(request,
        'quiz/questions.html',
        {'ques':ques})

# view function for about page
def about(request):
    return render(request,
        'quiz/about.html')






