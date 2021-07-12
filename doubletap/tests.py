from doubletap.models import Profile,Image
from django.test import TestCase

from django.contrib.auth.models import User
# Create your tests here.

class ImageTestClass(TestCase):
    """

    test class for Image model unit tests.

    """
    def setUp(self):
        self.user = User.objects.create_user("username", "password")
        self.new_profile = Profile(profile_photo='sampletestpic.png',bio="kizuri ndio kina garamiwa",user=self.user)
        self.new_profile.save()
        self.new_image = Image(image='sampletestpic.png',image_caption="image", profile=self.new_profile)

    def test_instance_true(self):
        self.new_image.save()
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1)

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()
        