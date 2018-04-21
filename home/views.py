from calendar_sem8.decorators import template_view

@template_view()
def index(request):
    return {
        'test': 'test',
    }
