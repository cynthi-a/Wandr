import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wandr_project.settings')
import django
django.setup()
from wandr.models import UserProfile, Picture

def populate():
    # create users

    user = [
        {"username:" "pinniped1", "password:" "pinniped"},
        {"username:" "pinniped2", "passowrd:" "cool-pinniped"}
    ]

    for user users.items()
        u = add_user(user)
        for u in user_data["username"]


#Start execution here
if __name__ == '__main__':
    print("Starting population for wandr")
    populate()