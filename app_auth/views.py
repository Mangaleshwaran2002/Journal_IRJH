from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from author.models import Author
from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username=str(request.POST.get('username'))
        password=request.POST.get('password')
        print(f"username :{username} password :{password}")
        
        user=authenticate(username=username,password=password)
        if user:
            print("authendicated user")
            login(request,user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('homescreen')
        else:
            # messages.add_message(request, messages.ERROR, "Credentials mismatched, Please enter the correct username and password")
            print("un-authendicated user")
    return render(request,'login_page.html')



def create_author(request):
    if request.method == 'POST':
        print(request.POST)
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        orcid=request.POST.get('orcid')
        if Author.objects.filter(username=username).exists() or Author.objects.filter(email=email).exists():
            return HttpResponse("username or email is already exists")
        else:
            author=Author.objects.create(username=username,email=email,first_name=firstname,last_name=lastname,orcid=orcid)
            author.set_password(password)
            print(vars(author))
            author.save()
            return redirect('login page')
    return render(request,'signup_page.html')


def logout_page(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)