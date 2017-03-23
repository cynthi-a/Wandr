import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wandr_project.settings')
import django
django.setup()
from wandr.models import UserProfile, Picture, User, HaveBeenList, ToGoList
from django.core.files.base import ContentFile
import requests


def populate():

    print "Adding users"
    add_user("Cristina", "pinniped1", "test1@email.com")
    add_user("Rob", "pinniped2", "test2@email.com")
    add_user("Cynthia", "pinniped3", "test3@email.com")

    print "Adding profiles"
    update_userprofile(1, "http://wandr.pythonanywhere.com/images/cristina-profile.jpg",
                       "http://wandr.pythonanywhere.com/images/cristina-cover.jpg",
                       "This is the population script bio for Cristina")
    update_userprofile(2, "http://wandr.pythonanywhere.com/images/rob-profile.jpg",
                       "http://wandr.pythonanywhere.com/images/rob-cover.jpg",
                       "This is the population script bio for Rob")
    update_userprofile(3, "http://wandr.pythonanywhere.com/images/cynthia-profile.jpg",
                       "http://wandr.pythonanywhere.com/images/cynthia-cover.jpg",
                       "This is the population script bio for Cynthia")

    print "Adding picture 1"
    add_picture(1, "test_name", "test_description", "test_location",
                "http://wandr.pythonanywhere.com/images/pic1.jpg", 2)
    print "Adding picture 2"
    add_picture(1, "test_name", "test_description", "test_location",
                "http://wandr.pythonanywhere.com/images/pic2.jpg", 4)
    print "Adding picture 3"
    add_picture(1, "test_name", "test_description", "test_location",
                "http://wandr.pythonanywhere.com/images/pic3.jpg", 11)
    print "Adding picture 4"
    add_picture(2, "test_name", "test_description", "test_location",
                "http://wandr.pythonanywhere.com/images/pic4.jpg", 10)
    print "Adding picture 5"
    add_picture(2, "test_name", "test_description", "test_location",
                "http://wandr.pythonanywhere.com/images/pic5.jpg", 21)
    print "Adding picture 6"
    add_picture(2, "test_name", "test_description", "test_location",
                "http://wandr.pythonanywhere.com/images/pic6.jpg", 9)
    print "Adding picture 7"
    add_picture(3, "test_name", "test_description", "test_location",
                "http://wandr.pythonanywhere.com/images/pic7.jpg", 1)
    print "Adding picture 8"
    add_picture(3, "test_name", "test_description", "test_location",
                "http://wandr.pythonanywhere.com/images/pic8.jpg", 8)
    print "Adding picture 9"
    add_picture(3, "test_name", "test_description", "test_location",
                "http://wandr.pythonanywhere.com/images/pic9.jpg", 11)


def add_user(username, password, email):
    u = User.objects.get_or_create(username=username, password=password, email=email)[0]
    u.save()
    return u


def update_userprofile(userid, profile_picture, cover_photo, bio):
    p = UserProfile.objects.get(pk=userid)
    print "Profile created"
    p.bio = bio
    print "Bio assigned"
    url_picture = profile_picture
    image_content = ContentFile(requests.get(url_picture).content)
    p.picture.save("profile.jpg", image_content)
    print "picture assigned"

    url_coverphoto = cover_photo
    image_content = ContentFile(requests.get(url_coverphoto).content)
    p.cover_photo.save("coverphoto.jpg", image_content)
    print "cover photo assigned"

    p.save()
    return p


def add_picture(userid, name, description, location, picture, likes):
    h = HaveBeenList.objects.get(belongs_to=userid)

    url_picture = picture
    image_content = ContentFile(requests.get(url_picture).content)
    pic = Picture.objects.create(name=name, description=description, location=location, have_been_list=h)
    pic.picture.save("picture.jpg", image_content)
    pic.likes = likes
    h.total_likes += likes
    h.save()
    pic.save()
    return pic


# Start execution here
if __name__ == '__main__':
    print("Starting population for wandr")
    populate()