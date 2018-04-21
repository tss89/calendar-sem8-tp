from functools import wraps
from inspect import getmodule


from django.http import HttpResponse
from django.shortcuts import render

def template_view(template_name=''):
    def decorator(func):
        template_path = '{}/{}.html'.format(
            getmodule(func).__name__.split('.')[0],
            func.__name__,
        )

        @wraps(func)
        def wrapper(request, *args, **kwargs):
            data = func(request, *args, **kwargs)
            if isinstance(data, HttpResponse):
                return data
            elif isinstance(data, dict):
                template = getattr(
                    request, 'force_template', None
                ) or template_name or getattr(
                    request, 'template', None
                ) or template_path

                return render(
                    request,
                    template,
                    data
                )
            else:
                raise Exception("Don't know what to do with: %s" % data)

        wrapper.exposed = True
        return wrapper

    return decorator
