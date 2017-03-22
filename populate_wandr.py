import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wandr_project.settings')
import django
django.setup()
from wandr.models import UserProfile, Picture, User, HaveBeenList, ToGoList
from django.core.files.base import ContentFile
import requests


def populate():
    # create users

    # users = [
    #     {"username":"Cristina", "password":"pinniped1", "email":"test1@email.com"},
    #     {"username":"Rob", "password":"pinniped2", "email":"test2@email.com"},
    #     {"username":"Cynthia", "password":"pinniped3", "email":"test3@email.com"},
    # ]


    add_user("Cristina", "pinniped1", "test1@email.com")
    add_user("Rob", "pinniped2", "test2@email.com")
    add_user("Cynthia", "pinniped3", "test3@email.com")

    update_userprofile(1, "https://www.google.co.uk/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png",
                       "https://www.google.co.uk/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png",
                       "This is the population script bio for Cristina")
    update_userprofile(2, "https://www.google.co.uk/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png",
                       "https://www.google.co.uk/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png",
                       "This is the population script bio for Rob")
    update_userprofile(3, "https://www.google.co.uk/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png",
                       "https://www.google.co.uk/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png",
                       "This is the population script bio for Cynthia")

    add_picture(1, "test_name", "test_description", "test_location",
                "https://www.google.co.uk/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png")


def add_user(username, password, email):
    u = User.objects.get_or_create(username=username, password=password, email=email)[0]
    u.save()
    return u


def update_userprofile(userid, profile_picture, cover_photo, bio):
    p = UserProfile.objects.get(pk=userid)
    p.bio = bio

    url_picture = profile_picture
    image_content = ContentFile(requests.get(url_picture).content)
    p.picture.save("profile.jpg", image_content)

    url_coverphoto = cover_photo
    image_content = ContentFile(requests.get(url_coverphoto).content)
    p.cover_photo.save("coverphoto.jpg", image_content)

    p.save()
    return p


def add_picture(userid, name, description, location, picture):
    h = HaveBeenList.objects.get(belongs_to=userid)

    url_picture = picture
    image_content = ContentFile(requests.get(url_picture).content)
    pic = Picture.objects.create(name=name, description=description, location=location, have_been_list=h)
    pic.picture.save("picture.jpg", image_content)

    pic.save()
    return pic


# Start execution here
if __name__ == '__main__':
    print("Starting population for wandr")
    populate()