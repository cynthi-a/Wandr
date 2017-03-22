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
                "http://m.chinadaily.com.cn/en/img/attachement/jpg/site1/20150823/b083fe9c5916174365cc0e.jpg")
    add_picture(1, "test_name", "test_description", "test_location",
                "http://www.placestoseeinyourlifetime.com/wp-content/uploads/2016/04/a-980x642.jpg")
    add_picture(1, "test_name", "test_description", "test_location",
                "http://www.placestoseeinyourlifetime.com/wp-content/uploads/2016/04/a-980x642.jpg")
    add_picture(2, "test_name", "test_description", "test_location",
                "http://1.bp.blogspot.com/-bH8v4Tiufhs/U8UbufaBKiI/AAAAAAAAXVE/OwIxLQAhaCQ/s1600/picturesque+landscape.jpg")
    add_picture(2, "test_name", "test_description", "test_location",
                "http://media02.hongkiat.com/picturesque-villages-on-earth/wallace-idaho.jpg")
    add_picture(2, "test_name", "test_description", "test_location",
                "https://image.slidesharecdn.com/picturesquetownsinwinter-141120092550-conversion-gate01/95/picturesque-towns-in-winter-1-638.jpg?cb=1416475643")
    add_picture(3, "test_name", "test_description", "test_location",
                "http://ww3.hdnux.com/photos/57/55/00/12505134/3/920x920.jpg")
    add_picture(3, "test_name", "test_description", "test_location",
                "https://media-cdn.tripadvisor.com/media/photo-s/07/1f/a6/46/very-picturesque.jpg")
    add_picture(3, "test_name", "test_description", "test_location",
                "https://www.thepinnaclelist.com/wp-content/uploads/2014/06/2-picturesque-towns-sun-bleached-coasts-salento-peninsula-apulia-italy-the-pinnacle-list-tpl.jpg")


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