from django.test import TestCase
from django.core.urlresolvers import reverse
from wandr.models import Picture, HaveBeenList, User
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage




'''
class UserTest(TestCase):
    """
    Check if user has been created. Print out her/his username to console
    """

    def add_user(self):
        username = "Cristina"
        password = "pinniped1"
        email = "test@email.com"
        u = User.objects.get_or_create(username=username, password=password, email=email)[0]
        u.save()
        return u

   # add_user("Cristina", "pinniped1", "test1@email.com")

    def test_user_exists(self):
        u = self.add_user()
        #self.assertTrue(isinstance(u, User))
        self.assertEqual(u.__unicode__(), u.username)
        print(u.username)


class LikeTest(TestCase):
    """
    ensure_views_are_positive should results True for categories where views are zero or positive
    """

    def add_picture(self):
        userid = 1
        have_been_list = HaveBeenList.objects.get(belongs_to=userid)
        name = "test_name"
        description = "test_description"
        location = "test_location"
        picture = "http://m.chinadaily.com.cn/en/img/attachement/jpg/site1/20150823/b083fe9c5916174365cc0e.jpg"
        likes = 0
        p = Picture.objects.get_or_create(have_been_list=have_been_list, name=name, description=description, location=location, picture=picture,likes=likes)
        p.save()
        return p

        #name = 'name'
        #description = 'test'
        #location = 'test'
        #h = HaveBeenList.objects.get(belongs_to=userid)
        #Picture.objects.create(name=name, description=description, location=location, have_been_list=h)

    def test_ensure_likes_are_positive(self):
        p = self.add_picture()
        self.assertEqual((p.likes >= 0), True)

        #hbl = HaveBeenList.objects.get(pk=1)
        #pic = Picture(name='test', location='test', description='test', likes=-1, have_been_list=hbl.pk)
        #pic.save()
        #self.assertEqual((pic.likes >= 0), True)
        '''

"""
Check if app contains required static files
"""
'''
class TestStaticFiles(TestCase):

    def test_images(self):
        abs_path = finders.find('images/wandr-seal.png')
        self.assertTrue(staticfiles_storage.exists(abs_path))


"""
Check if Form to Add Pictures works
"""

class PictureFormTest(TestCase):

    def setUp(self):
        try:
            from forms import PictureForm

        except ImportError:
            print('The module forms does not exist')
        except NameError:
            print('The class PictureForm does not exist or is not correct')
        except:
            print('Something else went wrong')
#        pass

    def test_does_name_field_work(self):
        from wandr.models import Picture
        p = Picture(name='Glasgow', have_been_list_id=1)
        p.save()
        self.assertEqual(p.name,'Glasgow')