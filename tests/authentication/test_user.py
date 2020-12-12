from mixtapebackend.authentication.models import User
import pytest


@pytest.mark.django_db
def test_user_must_have_email_and_password_fields():
    user = User.objects.create(email="email@email.com", password="12345678")
    assert user.email == "email@email.com"
    assert user.password == "12345678"


@pytest.mark.django_db
def test_user_cant_be_created_if_email_is_registered():
    User.objects.create(email="email@email.com", password="12345678")
    with pytest.raises(Exception) as error:
        User.objects.create(email="email@email.com", password="12345678")