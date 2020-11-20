import pytest

from MainUserRegistration.UserRegistration import UserRegistration


@pytest.fixture
def main_instance():
    user_registration =  UserRegistration()
    return user_registration