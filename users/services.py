from .models import CalendarUser
import facebook

class UserService:

    @classmethod
    def list(cls, facebook_id=None):
        query = CalendarUser.objects.all()
        if not facebook_id:
            query = query.filter(facebook_id=facebook_id)
        return query

    @classmethod
    def facebookLogin(cls, token, user_id):

        graph = facebook.GraphAPI(token)

        args = {'fields' : 'id,first_name,last_name,email' }
        
        myData = graph.get_object("me",**args)

        print(myData)