from .models import CalendarUser
from friends.services import FriedsGeneratorService,FriendRepository,FriendsServce
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

        friends = []
        friends = FriendsServce.get(myData[1])
        print(friends)
        #if friends.count > 0:
        #    generateFriendsAndSave(user)

        


    @classmethod
    def generateFriendsAndSave(cls, user):
        friends = FriedsGeneratorService.generate_friends(20)
        FriendRepository.addfriends(friends,user)