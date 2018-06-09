from .models import CalendarUser
from friends.services import FriedsGeneratorService,FriendRepository,FriendsService
import facebook
from django.contrib.auth import login

class UserService:

    @classmethod
    def list(cls, facebook_id=None):
        query = CalendarUser.objects.all()
        if not facebook_id:
            query = query.filter(facebook_id=facebook_id)
        return query

    @classmethod
    def facebookLogin(cls, token, user_id, request):


        
        graph = facebook.GraphAPI(token)

        args = {'fields' : 'id,first_name,last_name,email' }
        
        myData = graph.get_object("me",**args)

        if not cls.checkIfUserExist(myData.get('id')):
            user = cls.addUserToDb(myData.get('id'),myData.get('first_name'),myData.get('last_name'),myData.get('email'))
            #dodaje do bazy
        else:
            user = cls.getUserFromDb(myData.get('id')).first()
            #pobieram usera

        login(request, user)

        

        
    @classmethod
    def checkIfUserExist(cls, facebook_id=None):
        return cls.getUserFromDb(facebook_id).exists()

    @classmethod
    def getUserFromDb(cls, facebook_id=None):
        query = CalendarUser.objects.all()
        if not facebook_id:
            query = query.filter(facebook_id=facebook_id)
            
        return query

    @classmethod
    def addUserToDb(cls, id=None, first_name=None, last_name=None, email=None):
        user = CalendarUser()
        user.facebook_id = id
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return user


    @classmethod
    def generateFriendsAndSave(cls, user):
        friends = FriedsGeneratorService.generate_friends(20)
        FriendRepository.addfriends(friends,user)


   