from users.services import UserService
from django.shortcuts import redirect

def logout(request):
    
    UserService.logoutHandler(request)

    return redirect("home")