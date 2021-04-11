from django.http import request, response
from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from blog.views import post_content
from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestViews:
    def test_post_detail_is_authenticated(self):
        "Test if the user trying to access the view is authenticated"
        mixer.blend('blog.Post')
        path = reverse("content", kwargs={'pk':1})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        response = post_content(request, pk=1)
        assert response.status_code == 200

