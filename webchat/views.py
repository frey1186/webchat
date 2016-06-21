from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


def acc_login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(request.GET.get('next') or reverse("chat:chat_index"))
        else:
            login_err = "Wrong username or password!"
            return render(request, 'login.html', {'login_err': login_err})
    return render(request, 'login.html')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("chat:chat_index"))