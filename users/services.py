from .models import CalendarUser

class UserService:

    @classmethod
    def list(cls, facebook_id=None):
        query = CalendarUser.objects.all()
        if not facebook_id:
            query = query.filter(facebook_id=facebook_id)
        return query
