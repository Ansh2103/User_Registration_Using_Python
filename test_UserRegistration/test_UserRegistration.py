import pytest

from MainUserRegistration.UserRegistrationException import InputException


def test_valid_first_name(main_instance):
    result = main_instance.validate_first_name("Shubham")
    assert result.__eq__(True)

def test_invalid_first_name(main_instance):
    with pytest.raises(InputException):
        main_instance.validate_first_name(" shubham ")



