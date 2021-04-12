import pytest
from blog.models import Post
@pytest.mark.django_db
class TestModels:

    def test_post_create(self):
        post = Post.objects.create(
            author="Muhammed Ali",
            title="Simple article",
            content="This is my content",
            date_posted="2021-04-12 12:12:11.343944+00:00"

        )
        assert post.author == "Muhammed Ali"
        assert post.title == "Simple article"
        assert post.content == "This is my content"
        assert post.date_posted == "2021-04-12 12:12:11.343944+00:00"