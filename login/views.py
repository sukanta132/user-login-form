from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from login.models import sukanta_user
from django.contrib.auth import authenticate,login



def SignupPage(request):
    if request.method=='POST':
        vname = request.POST['Username']
        vnumber = request.POST['PhoneNumber']
        vemail = request.POST['email']
        vpsw1 = request.POST['psw']
        vpsw2 = request.POST['pswrepeat']

        if vpsw1!=vpsw2:
            return HttpResponse("your password and confirm password are not same!!")
        else:

            sukanta_us = sukanta_user(Username=vname, PhoneNumber=vnumber, email=vemail, psw=vpsw1, pswrepeat=vpsw2)
            sukanta_us.save()
        # return HttpResponse('user has been created successfully!!')
            return redirect('LoginPage')
        

    return render(request, 'SignupPage.html')

def LoginPage(request):
    if request.method=='POST':
        vuname = request.POST.get('uname')
        vpsw3 = request.POST.get('pssw')
        # print(vuname,vpsw3)
        var_user=authenticate(request,Username=vuname, vpsw2=vpsw3)
        if var_user is not None:
            login(request,var_user)
            return redirect('home')
        else:
            return HttpResponse("username or password is incorrect!!!")

    return render(request, 'LoginPage.html')
  
def home(request):
    return render(request, 'Home.html')

