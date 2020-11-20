import pytest

from MainUserRegistration.UserRegistrationException import InputException

def test_valid_first_name(main_instance):
    '''if this function return true then the test will pass'''
    result = main_instance.validate_first_name("Shubham")
    assert result.__eq__(True)

def test_invalid_first_name(main_instance):
    with pytest.raises(InputException):
        main_instance.validate_first_name(" shubham ")

def test_valid_last_name(main_instance):
   result = main_instance.validate_first_name("Kumar")
   assert result.__eq__(True)

def test_invalid_last_name(main_instance):
   with pytest.raises(InputException):
       main_instance.validate_first_name("kumar")

def test_valid_email(main_instance):
   result = main_instance.validate_email("swyam007.sm@gmail.com")
   assert result.__eq__(True)

def test_invalid_email(main_instance):
   with pytest.raises(InputException):
       main_instance.validate_email("swayam@.com")




