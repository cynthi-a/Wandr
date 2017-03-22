from django.test import TestCase
from wandr.models import Picture, HaveBeenList


class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        """
        ensure_views_are_positive should results True for categories where views are zero or positive
        """
        hbl = HaveBeenList.objects.get(belongs_to='')
        pic = Picture(name='test', location='test', description='test', likes=-1, have_been_list=HaveBeenList)
        pic.save()
        self.assertEqual((pic.likes >= 0), True)


def login_client_user(self):
    self.client.login(username='admin', password='secret666')
    return self


def logout_client_user(self):
    self.client.logout()
    return self