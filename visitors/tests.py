from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from .models import Visitor, User
from .admin import VisitorAdmin


#
class MockRequest(object):
    def __init__(self, user=None):
        self.user = user


class TestModel(TestCase):

    def test_correct_visitor_created(self):
        self.visitor = Visitor.objects.create(name='Ma', surname='cin', iban='ES830081026')
        self.assertEquals(str(self.visitor), 'Ma cin')


class ModelAdminTestPermissions(TestCase):
    def setUp(self) -> None:
        self.creator = User.objects.create_superuser(username='testuseraaaa', email='z@b.a', is_staff=True)
        self.non_creator = User.objects.create_user(username='testuser', password='xxxxx', email='z@b.a', is_staff=True)
        self.visitor = Visitor.objects.create(name='Ma', surname='cin', iban='07978979')
        self.request_creator = MockRequest(self.creator)
        self.request_non_creator = MockRequest(self.non_creator)
        self.visitorAdmin = VisitorAdmin(model=self.visitor, admin_site=AdminSite())

    def test_has_add_permission(self):
        self.assertEquals(self.visitorAdmin.has_add_permission(self.request_creator), True)

    def test_has_delete_permission(self):
        self.assertEquals(self.visitorAdmin.has_delete_permission(self.request_creator), True)

    def test_has_change_permission(self):
        self.assertEquals(self.visitorAdmin.has_change_permission(self.request_creator), True)

    def test_has_no_delete_permission(self):
        self.assertEquals(self.visitorAdmin.has_delete_permission(self.request_non_creator), False)

    def test_has_no_change_permission(self):
        self.assertEquals(self.visitorAdmin.has_change_permission(self.request_non_creator), False)

