from django.shortcuts import render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from realestate_app.forms import UserAdminCreationForm
from .models import Property, Unit,Tenant, RentalDetails
from django.contrib.auth.decorators import login_required

# Create your views here.



def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(req, 'register.html', {'form': form})

@login_required(login_url='/accounts/login/')
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'profile.html', {'properties': properties})

@login_required(login_url='/accounts/login/')
def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_list.html', {'tenants': tenants})

@login_required(login_url='/accounts/login/')
def tenant_profile(request, tenant_id):
    tenant = get_object_or_404(Tenant, pk=tenant_id)
    rental_details = RentalDetails.objects.filter(tenant=tenant)
    return render(request, 'tenant_profile.html', {'tenant': tenant, 'rental_details': rental_details})

