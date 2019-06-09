import django
from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import *
import hashlib
from MisFit.decorators import *
from django.db.models import Q
from MisFit.pipeline import get_avatar
# from get_views_list import all_views_list


# Create your views here.


def login(request):
    if 'logged_in' in request.session:
        if request.session['logged_in'] is True:
            return redirect('users:list_user')
    else:
        if request.method == 'GET':
            form = LoginForm
            return render(request, 'users/login.html', {'form': form, 'browser_title': 'User Login'})

        elif request.method == 'POST':
            form = LoginForm(request.POST or None)
            if form.is_valid():
                pasw = form['password'].value().encode('utf-8')
                password = hashlib.sha256(pasw).hexdigest()
                email = form['email'].value()
                try:
                    user = User.objects.get(Q(email=email))
                    if user.password == password:
                        if user.is_active is True:
                            request.session['logged_in'] = True
                            request.session['email'] = user.email
                            request.session['photo'] = str(user.photo)
                            request.session['id'] = user.pk
                            role = Role.objects.get(id=user.role_id)
                            request.session['role'] = role.role_title
                            request.session['role_id'] = user.role_id
                            return redirect('users:list_user')
                        else:
                            messages.error(request, 'Your Account is not active. Please contact Admin.')

                    else:
                        messages.error(request, 'Incorrect Email or Password!')

                except User.DoesNotExist:
                    messages.error(request, 'No user found by the Email Provided!')
                return redirect('users:login')


def add_user(request):
    arg = {}
    arg['browser_title'] = "Register"
    arg['rediurect_url'] = "users:add_user"
    arg['form'] = UserAddForm

    if request.method == 'POST':

        form = UserAddForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            password = form.password.encode('utf-8')
            password = hashlib.sha256(password).hexdigest()
            form.password = password
            form.save()
            messages.success(request, 'User Added')
            return redirect('users:login')

        else:
            arg['form'] = form
            return render(request, 'users/register.html', arg)

    return render(request, 'users/register.html', arg)


@login_required('logged_in', 'users:login')
def list_user(request):
    role_id = request.session['role_id']
    if role_id == 4:
        users = User.objects.filter(pk=request.session['id'])
    else:
        users = User.objects.all()

    arg = {}
    arg['user'] = "active"
    arg['user_list'] = "active"
    arg['title'] = "Users List"
    arg['users'] = users
    arg['p_users'] = users
    arg['redirect_title'] = "User"
    arg['rediurect_url'] = "users:list_user"

    return render(request, 'users/user_list.html', arg)

def logout(request):

    if 'logged_in' in request.session:
        del request.session['logged_in']
        del request.session['id']
        del request.session['email']
        del request.session['photo']
        del request.session['role']
        return redirect('users:login')
    else:
        return redirect('users:login')


@login_required('logged_in', 'users:login')
def roles_list(request):
    role_id = request.session['role_id']
    if role_id == 4:
        return render(request, '401.html')
    else:
        roles = Role.objects.all()
    arg = {}
    arg['user'] = "active"
    arg['list_roles'] = "active"
    arg['title'] = "Roles List"
    arg['roles'] = roles
    arg['redirect_title'] = "Role"
    arg['rediurect_url'] = "users:list_roles"

    return render(request, 'users/role_list.html', arg)