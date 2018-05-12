from calendar_sem8.decorators import template_view
from friends.services import FriedsGeneratorService

@template_view()
def index(request):
    from pprint import pprint
    f = (FriedsGeneratorService.generate_friends(10, False))
    for ff in f:
        pprint(ff.__dict__)
    return {
        'test': 'test',
    }
