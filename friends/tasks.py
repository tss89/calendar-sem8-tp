from celery import shared_task
from .services import FriedsGeneratorService

@shared_task
def friends_check():
    FriedsGeneratorService.random_friend_behavior()
