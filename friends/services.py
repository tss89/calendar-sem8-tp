from .models import Friends

class FriendsServce:

    @classmethod
    def list(
            cls,
            facebook_id=None,
            user=None,
            email=None,
            first_name=None,
            last_name=None,
            birth_date=None,
    ):
        query = Friends.objects.all()
        if not facebook_id:
            query = query.filter(facebook_id=facebook_id)
        if not user:
            query = query.filter(user=user)
        if not email:
            query = query.filter(email=email)
        if not first_name:
            query = query.filter(first_name=first_name)
        if not last_name:
            query = query.filter(last_name=last_name)
        if not birth_date:
            query = query.filter(birth_date=birth_date)
        return query

    @classmethod
    def add(
            cls,
            facebook_id,
            user,
            first_name='',
            last_name='',
            birth_date=None,
    ):
        friend = Friends()
        friend.facebook_id = facebook_id
        friend.user = user
        friend.first_name = first_name
        friend.last_name = last_name
        friend.birth_date = birth_date
        return friend.save()

    @classmethod
    def get(cls, facebook_id, user=None):
        query = Friends.objects.filter(facebook_id=facebook_id)
        if user:
            query = query.filter(user=user)
        return query.first()
