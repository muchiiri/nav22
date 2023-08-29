from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        company = request.POST['company']
        address = request.POST['address']
        phone_no = request.POST['phone_no']
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email address is already in use.')
            return redirect('signup')
        
        # Create user
        user = User.objects.create_user(
            username=email, 
            email=email,
            first_name=firstname,
            last_name=lastname
        )
        user.profile.company = company
        user.profile.address = address
        user.profile.phone_no = phone_no
        user.save()
        
        messages.success(request, 'Your account has been created successfully!')
        return redirect('login')
    
    return render(request, 'signup.html')
