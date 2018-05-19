import random
from datetime import datetime, timedelta

from .models import Friends, FriendUser
from users.models import CalendarUser

class FriendsService:

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
            query = query.filter(frienduser__user=user)
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
    def add(cls, friend: Friends):
        return friend.save()

    @classmethod
    def get(cls, facebook_id, user=None):
        query = Friends.objects.filter(facebook_id=facebook_id)
        if user:
            query = query.filter(frienduser__user=user)
        return query.first()

    @classmethod
    def calendar_format(cls, friend):
        friend.name = "{} {}".format(friend.first_name, friend.last_name)
        if isinstance(friend.birth_date, str):
            friend.birth_date = datetime.strptime(friend.birth_date, "%Y-%m-%d")
        friend.birth_date_month = friend.birth_date.month - 1
        friend.birth_date_day = friend.birth_date.day
        return friend

    @classmethod
    def change_last_name(cls, friend, last_name):
        if not friend or not last_name:
            return friend
        friend.last_name = last_name
        return friend.save()

    @classmethod
    def change_birth_date(cls, friend, birth_date):
        if not friend or not birth_date:
            return friend
        friend.birth_date = birth_date
        return friend.save()

    @classmethod
    def remove(cls, friend):
        FriendsUserService.remove_by_friend(friend=friend)
        return friend.delete()

class FriendsUserService:

    @classmethod
    def add(cls, friend, user):
        return FriendUser(friend=friend, user=user).save()

    @classmethod
    def remove(cls, friend, user=None):
        return FriendUser.objects.filter(friend=friend, user=user).delete()

    @classmethod
    def remove_by_friend(cls, friend):
        return FriendUser.objects.filter(friend=friend).delete()

class FriedsGeneratorService:

    FIRSTNAMES = [
        #----------------women-----------------
        'Maria', 'Krystyna', 'Anna', 'Barbara', 'Teresa', 'Elżbieta', 'Janina', 'Zofia', 'Jadwiga', 'Danuta',
        'Halina', 'Irena', 'Ewa', 'Małgorzata', 'Helena', 'Grażyna', 'Bożena', 'Stanisława', 'Jolanta', 'Marianna',
        'Urszula', 'Wanda', 'Alicja', 'Dorota', 'Agnieszka', 'Beata', 'Katarzyna', 'Joanna', 'Wiesława', 'Renata',
        'Iwona', 'Genowefa', 'Kazimiera', 'Stefania', 'Hanna', 'Lucyna', 'Józefa', 'Alina', 'Mirosława', 'Aleksandra',
        'Władysława', 'Henryka', 'Czesława', 'Lidia', 'Regina', 'Monika', 'Magdalena', 'Bogumiła', 'Marta', 'Marzena',
        #---------------men--------------------
        'Jan', 'Stanisław', 'Andrzej', 'Józef', 'Tadeusz', 'Jerzy', 'Zbigniew', 'Krzysztof', 'Henryk', 'Ryszard',
        'Kazimierz', 'Marek', 'Marian', 'Piotr', 'Janusz', 'Władysław', 'Adam', 'Wiesław', 'Zdzisław', 'Edward',
        'Mieczysław', 'Roman','Mirosław', 'Grzegorz', 'Czesław', 'Dariusz', 'Wojciech', 'Jacek', 'Eugeniusz', 'Tomasz',
        'Stefan', 'Zygmunt', 'Leszek', 'Bogdan', 'Antoni', 'Paweł', 'Franciszek', 'Sławomir', 'Waldemar', 'Jarosław',
        'Robert', 'Mariusz', 'Włodzimierz', 'Michał', 'Zenon', 'Bogusław', 'Witold', 'Aleksander', 'Bronisław', 'Wacław',

    ]

    LASTNAMES = [
        'Amsterdamski', 'Arab', 'Arabik', 'Arabowicz', 'Arabski', 'Austrijak', 'Białoruski', 'Brandenburg',
        'Brandenburger', 'Cygan', 'Chorwat', 'Czech', 'Czeski', 'Böhm', 'Duńczyk', 'Francuz', 'Gal', 'Galoch',
        'Galicki', 'Halicki', 'Góral', 'Gorol', 'Hiszpan', 'Holender', 'Holenderski', 'Holland', 'Olęder', 'Olender',
        'Kaszuba', 'Kaszub', 'Kijowski', 'Kurlandt', 'Kurlandzki', 'Kurlanda', 'Kurland', 'Kurlandczyk', 'Kuruc',
        'Kuman', 'Koman', 'Litwin', 'Litwiniuk', 'Litwinowicz', 'Łotysz', 'Macedoński', 'Madziar', 'Madziara', 'Mazur',
        'Mazurek', 'Mazurkiewicz', 'Moraw', 'Morawski', 'Moskal', 'Niemiec',
        'Niemczyk', 'Norwecki', 'Petersburski', 'Podolak', 'Podolski', 'Podolec', 'Podolan', 'Polak', 'Polok',
        'Poloczek', 'Polakowski', 'Polaczek', 'Poleszak', 'Polesiak', 'Poleski', 'Poleszczuk', 'Poleszuk', 'Pomorski',
        'Pruski', 'Prus', 'Prusak', 'Prusek', 'Prusik', 'Pruś', 'Rosjan', 'Rus', 'Rusin', 'Rusek', 'Rusak', 'Rusnak',
        'Rumun', 'Rumuński', 'Romun', 'Sakson', 'Sas', 'Sasin', 'Sass', 'Sieradzki', 'Słowak', 'Słowakiewicz',
        'Słowacki', 'Słowiak', 'Słowiakowski', 'Szwab', 'Szkot', 'Szwajcar', 'Szwajcer', 'Szwajcarski', 'Szwed',
        'Szweda', 'Szwedek', 'Szwedziak', 'Szwedowski', 'Szwedzki', 'Ślązak', 'Ślonzak', 'Szlonzak', 'Szlązak',
        'Slezak', 'Lamparska', 'Lamparski', 'Tatar', 'Tatara', 'Tatarek', 'Tatarski', 'Tatarzyn', 'Tatarczuk',
        'Tatarczak', 'Tatarczyk', 'Turek', 'Turecki', 'Ukraiński', 'Ukrainiec', 'Węgier', 'Węgierski', 'Węgrzyn',
        'Węgrzynowicz', 'Włoch', 'Wołoch', 'Wołoszek', 'Wołyniak', 'Żmuda', 'Żmudzin', 'Żmijewska', 'Żmijewski',
        'Żochowski', 'Żydek', 'Żydowicz', 'Żydowski', 'Żydziak', 'Żydzik'
    ]

    YEARS_RANGE_START = '0'
    YEARS_RANGE_STOP = '1'

    YEARS_RANGE = {
        YEARS_RANGE_START: datetime.strptime('1980-01-01', '%Y-%m-%d'),
        YEARS_RANGE_STOP: datetime.strptime('2010-12-31', '%Y-%m-%d'),
    }

    RANDOM_FRIEND_BEHAVIOR_NEW_FRIEND = 0
    RANDOM_FRIEND_BEHAVIOR_CHANGE_SURNAME = 1
    RANDOM_FRIEND_BEHAVIOR_CHANGE_BIRTH_DATE = 2
    RANDOM_FRIEND_BEHAVIOR_LEAVE_FRIEND = 3
    RANDOM_FRIEND_BEHAVIOR_REMOVE_FRIEND = 4

    @classmethod
    def random_friend_behavior(cls):
        random_value = random.randint(0, 4)
        if random_value == cls.RANDOM_FRIEND_BEHAVIOR_NEW_FRIEND:
            cls.random_friend().save()
        elif random_value == cls.RANDOM_FRIEND_BEHAVIOR_CHANGE_SURNAME:
            FriendsService.change_last_name(Friends.objects.order_by('?').first(), cls.__random_lastname())
        elif random_value == cls.RANDOM_FRIEND_BEHAVIOR_CHANGE_BIRTH_DATE:
            FriendsService.change_birth_date(Friends.objects.order_by('?').first(), cls.__random_date())
        elif random_value == cls.RANDOM_FRIEND_BEHAVIOR_LEAVE_FRIEND:
            friend_user = FriendUser.objects.order_by('?').first()
            if friend_user:
                FriendsUserService.remove(friend_user.friend, friend_user.user)
        elif random_value == cls.RANDOM_FRIEND_BEHAVIOR_REMOVE_FRIEND:
            FriendsService.remove(Friends.objects.order_by('?').first())
        return random_value

    @classmethod
    def random_friend(cls):
        friend = Friends()
        friend.first_name = cls.__random_firstname()
        friend.last_name = cls.__random_lastname()
        friend.email = "{}@facebook.com".format("{}.{}".format(friend.first_name, friend.last_name).lower())
        friend.birth_date = cls.__random_date()
        friend.facebook_id = random.randint(1000000, 10000000)
        return friend

    @classmethod
    def generate_friends(cls, count, force_random_exists = True):
        friends = []
        i = 0
        while(i < count):
            is_new = True
            if force_random_exists:
                count = Friends.objects.count()
                if count > 0:
                    is_new = bool(random.randint(0, 1))
            if is_new:
                friends.append(cls.random_friend())
            else:
                friends.append(Friends.objects.order_by('?').first())
            count -= 1
        return friends

    @classmethod
    def __random_firstname(cls):
        return cls.FIRSTNAMES[random.randint(0, len(cls.FIRSTNAMES) - 1)]

    @classmethod
    def __random_lastname(cls):
        return cls.LASTNAMES[random.randint(0, len(cls.LASTNAMES) - 1)]

    @classmethod
    def __random_date(cls):
        start = cls.YEARS_RANGE.get(cls.YEARS_RANGE_START)
        end = cls.YEARS_RANGE.get(cls.YEARS_RANGE_STOP)
        return datetime.strftime(cls.YEARS_RANGE.get(cls.YEARS_RANGE_START) + timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())),
        ), '%Y-%m-%d')

class FriendRepository:

    @classmethod
    def add_friend(cls, friend: Friends, user):
        FriendsService.add(friend)
        FriendsUserService.add(friend, user)
        return friend

    @classmethod
    def addfriends(cls, friends: list, user):
        for friend in friends:
            cls.add_friend(friend, user)
