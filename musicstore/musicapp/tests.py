from django.test import TestCase
from django.urls import reverse
from .models import Artist, Record, Review
from .forms import RecordForm, ReviewForm
from datetime import datetime

# Create your tests here.
class RecordTest(TestCase):
    def test_tablename(self):
        self.assertEqual(str(Record._meta.db_table), 'record')

class ReviewTest(TestCase):
    def test_tablename(self):
        self.assertEqual(str(Review._meta.db_table), 'review')

class ArtistTest(TestCase):
    def test_tablename(self):
        self.assertEqual(str(Artist._meta.db_table), 'name')

#testing a view
class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'musicapp/index.html')

class TestGetRecord(TestCase):


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/musicapp/records')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('records'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('records'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'musicapp/records.html')

class TestGetArtist(TestCase):


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/musicapp/artists')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('artists'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('artists'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'musicapp/artists.html')

class New_Record_Form_Test(TestCase):

    # Valid Form Data
    def test_recordForm_is_valid(self):
        form = RecordForm(data={'recordtitle': "Born This Way", 'recordrelease': "2016-05-02", 'artist': "Lady Gaga" })
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = RecordForm(data={'recordtitle': "Born This Way", 'recordrelease': "2016-05-02", 'artist': "Lady Gaga"})
        self.assertFalse(form.is_valid())

class New_Review_Form_Test(TestCase):

    # Valid Form Data
    def test_reviewForm_is_valid(self):
        form = ReviewForm(data={'record': "Purple Rain", 'dateentered': "2019-02-19", 'user': "hannah", 'review': "I loved it" })
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = ReviewForm(data={'record': "Purple Rain", 'dateentered': "2019-02-19", 'user': "hannah", 'review': "I loved it"})
        self.assertFalse(form.is_valid())