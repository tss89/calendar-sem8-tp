from users.services import UserService

def token(request):
    token = request.GET.get('access_token')
    user_id = request.GET.get('user_id')
    
    try:
        UserService.facebookLogin(token,user_id)
    
    except:
        pass