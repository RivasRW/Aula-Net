from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
#forms
#from users.forms import ProfileForm, SignupForm


# Create your views here.
# funcion de inicio de sesion
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request,'users/login.html')


#funcion de cierre de sesion
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


#funcion de crear una cuenta
def signup(request):
    """ METODO DE CREAR CUENTA"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = SignupForm()

        return render(
            request=request,
            template_name='users/signup.html',
            context={'form': form}
        )

# Create your views here.
