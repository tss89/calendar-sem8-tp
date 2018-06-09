from users.services import UserService
from django.shortcuts import redirect

def token(request):
    token = request.GET.get('access_token')
    user_id = request.GET.get('user_id')
    
    try:
        UserService.facebookLogin(token,user_id, request)
        
    except Exception as e:
        print(e)
        pass

    return redirect("home")