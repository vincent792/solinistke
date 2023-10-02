from django.shortcuts import render,redirect
from  django.contrib import messages,  auth
from  account.models import Account
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if  request.method=='POST':
        uname=  request.POST['uname']
        pass1=  request.POST['pass1']
        user=User.objects.create_user(username=uname, password=pass1)
        user.save()
        user1=Account(user=user,username=uname, password=pass1)
        user1.save()
        print('user saved to  db')
        return redirect('login')    
        

    return render(request,  'account/register.html')

def login(request):
    if  request.method=='POST':
        uname=  request.POST['uname']
        pass1=  request.POST['pass1']
        user=auth.authenticate(username=uname, password=pass1)
        if  user is not  None:
            auth.login(request, user)
            print('user saved loged in')
            return redirect('/') 
        else:
            print('invalid')

        
    return render(request,  'account/login.html')


def logout(request):
    auth.logout(request)
    print('logged off')
    return redirect('login')    


#activation



def activate(request):
    if request.method == 'POST':
        activation_code = request.POST.get('activation_code')
        
        # Assuming you have a custom user model with an 'activation_code' field
        user = Account.objects.filter(activation_code=activation_code).first()

        if user:
            user.is_activated = True
            user.save()
            return redirect('post_detail')  # Redirect to the list of posts or any other page
        else:
            return redirect('post_list')

    return render(request, 'account/activate.html')

