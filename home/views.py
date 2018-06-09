from calendar_sem8.decorators import template_view
from friends.services import FriendsService, FriedsGeneratorService

@template_view()
def index(request):

    print(request.user)

    return {
        'friends': [
            FriendsService.calendar_format(friend)
            for friend in (FriendsService.list(user=request.user)
                           if request.user and request.user.is_authenticated else
                           FriedsGeneratorService.generate_friends(100, False))
        ],
        'test': 'test',
    }

