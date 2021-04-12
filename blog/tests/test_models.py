import pytest
from blog.models import Post
@pytest.mark.django_db
class TestModels:

    def test_post_create(self):
        post = Post.objects.create(
            author="Muhammed Ali",
            title="Simple article",
            content="This is my content",
        )
        assert post.author == "Muhammed Ali"
        assert post.title == "Simple article"