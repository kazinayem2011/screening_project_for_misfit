from django.shortcuts import render
from MisFit.decorators import *
from .forms import *
from users.models import User



# for pdf purpose . . .
from django.views.generic import View
from django.utils import timezone
from .render_pdf import RenderPdf


@login_required('logged_in', 'users:login')
def list_request(request):
    role_id = request.session['role_id']
    if role_id == 4:
        req = EmployeeRequest.objects.filter(user=request.session['id'])
    elif role_id == 1:
            req = EmployeeRequest.objects.filter(status=2)
    else:
        req = EmployeeRequest.objects.all()
    arg = {}
    arg['emp_request'] = "active"
    arg['emp_request_list'] = "active"
    arg['title'] = "Request List"
    arg['req_data'] = req
    arg['redirect_title'] = "Request"
    arg['rediurect_url'] = "employeeRequest:list_request"

    return render(request, 'employeeRequest/request_list.html', arg)


@login_required('logged_in', 'users:login')
def add_request(request):
    arg = {}
    arg['emp_request'] = "active"
    arg['emp_request_list'] = "active"
    arg['btn'] = "Save"
    arg['title'] = "Add Request"
    arg['redirect_title'] = "Request"
    arg['rediurect_url'] = "employeeRequest:list_request"
    arg['form'] = AddRequestForm

    if request.method == 'POST':

        form = AddRequestForm(request.POST, request.FILES)

        if form.is_valid():
            user = User.objects.get(pk=request.session['id'])
            form = form.save(commit=False)
            form.created_at = timezone.now()
            form.modified_at = timezone.now()
            form.created_by = user
            form.modified_by = user
            form.user = user
            form.save()
            messages.success(request, 'Request Added')
            return redirect('employeeRequest:list_request')

        else:
            arg['form'] = form
            return render(request, 'includes/common_form.html', arg)

    return render(request, 'includes/common_form.html', arg)



@login_required('logged_in', 'users:login')
def edit_request(request, req_id):
    try:
        emp_request = EmployeeRequest.objects.get(id=req_id)
        # Set permission for employee not to allow edit when status is in processing
        if emp_request.status != 0 and request.session['role_id'] == 4:
            messages.error(request, 'You are not allowed anymore to update your request anymore when request is in processing.')
            return redirect('employeeRequest:list_request')
    except EmployeeRequest.DoesNotExist:
        return render(request, '404.html')

    arg = {}
    arg['emp_request'] = "active"
    arg['emp_request_list'] = "active"
    arg['btn'] = "Update"
    arg['title'] = "Update Request"
    arg['redirect_title'] = "Request"
    arg['rediurect_url'] = "employeeRequest:list_request"
    arg['form'] = EditRequestForm(instance=emp_request)

    if request.method == 'POST':

        form = EditRequestForm(request.POST, instance=emp_request)

        if form.is_valid():
            user = User.objects.get(pk=request.session['id'])
            form_data = form.save(commit=False)
            form_data.modified_by = user
            form_data.save()
            messages.success(request, 'Request Updated')
            return redirect('employeeRequest:list_request')
        else:
            arg['form'] = form
            return render(request, 'includes/common_form.html', arg)

    return render(request, 'includes/common_form.html', arg)


@login_required('logged_in', 'users:login')
def edit_request_status(request, req_id):
    try:
        emp_request = EmployeeRequest.objects.get(id=req_id)
        # Set permission for employee not to allow status update
        if request.session['role_id'] == 4:
            messages.error(request, 'Only HR and Manager are allowed to update your status.')
            return redirect('employeeRequest:list_request')
        else:
            pass
    except EmployeeRequest.DoesNotExist:
        return render(request, '404.html')

    arg = {}
    arg['emp_request'] = "active"
    arg['emp_request_list'] = "active"
    arg['btn'] = "Update"
    arg['title'] = "Update Status"
    arg['redirect_title'] = "Request"
    arg['rediurect_url'] = "employeeRequest:list_request"
    if request.session['role_id'] == 1:
        arg['form'] = EditRequestStatusForManagerForm(instance=emp_request)
    else:
        arg['form'] = EditRequestStatusForm(instance=emp_request)

    if request.method == 'POST':

        form = EditRequestStatusForm(request.POST, instance=emp_request)

        if form.is_valid():
            user = User.objects.get(pk=request.session['id'])
            form_data = form.save(commit=False)
            form_data.modified_by = user
            form_data.save()
            messages.success(request, 'Request Status Updated')
            return redirect('employeeRequest:list_request')
        else:
            arg['form'] = form
            return render(request, 'includes/common_form.html', arg)

    return render(request, 'includes/common_form.html', arg)



def pdf_view(request):
    role_id = request.session['role_id']
    if role_id != 4:
        requested_data = EmployeeRequest.objects.all()
    else:
        messages.error(request, 'Sorry, Only HR and Manager are allowed to download.')
        return redirect('employeeRequest:list_request')

    today = timezone.now()
    arg = {
        'today': today,
        'requested_data': requested_data
    }
    return RenderPdf.render('employeeRequest/pdf.html', arg)