import pytest

from MainUserRegistration.UserRegistrationException import UserException

def test_valid_first_name(main_instance):
    '''if this function return true then the test will pass'''
    result = main_instance.validate_first_name("Shubham")
    assert result.__eq__(True)

def test_invalid_first_name(main_instance):
    with pytest.raises(UserException):
        main_instance.validate_first_name(" shubham ")


def test_valid_last_name(main_instance):
   result = main_instance.validate_last_name("Kumar")
   assert result.__eq__(True)

def test_invalid_last_name(main_instance):
   with pytest.raises(UserException):
       main_instance.validate_last_name("kumar")



def test_valid_phone_number(main_instance):
   result = main_instance.validate_phone_number("91 9334358903")
   assert result.__eq__(True)

def test_invalid_phone_number(main_instance):
   with pytest.raises(UserException):
       main_instance.validate_phone_number("9334358903")


def test_valid_password(main_instance):
   result = main_instance.validate_password("Abcd7f@ghi")
   assert result.__eq__(True)

def test_invalid_password(main_instance):
   with pytest.raises(UserException):
       main_instance.validate_password("Abcd7efghi")


@pytest.mark.parametrize("input, expected", [
    ("abc@yahoo.com", True),
    ("abc-100@yahoo.com", True),
    ("abc.100@yahoo.com", True),
    ("abc111@abc.com", True),
    ("abc-100@abc.net", True),
    ("abc.100@abc.com.au", True),
    ("abc@1.com", True),
    ("abc@gmail.com.com", True),
    ("abc+100@gmail.com", True),

])
def test_valid_email(input, expected, main_instance):
    result = main_instance.validate_email(input)
    assert result == expected


def test_moodAnalyzer_should_return_Happy(main_instance):
   result = main_instance.mood_analyzer("Shubham", "Kumar", "91 7903990740", "swayam007.sm@gmail.com")
   assert result.__eq__(True)

def test_moodAnalyzer_should_return_Sad(main_instance):
   with pytest.raises(UserException):
       main_instance.mood_analyzer("shubham", "kumar", "7903990740", "swayam007@.com")

