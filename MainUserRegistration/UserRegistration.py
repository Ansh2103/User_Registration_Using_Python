import re

from MainUserRegistration.UserRegistrationException import UserException

class UserRegistration:

    FIRST_NAME_PATTERN = r'^[A-Z][a-z]{3,}$'
    LAST_NAME_PATTERN = r'^[A-Z][a-z]{3,}$'
    EMAIL_PATTERN = r'^[0-9a-zA-Z]+([._+-][0-9a-zA-Z]+)*[@][0-9A-Za-z]+([.][a-zA-Z]{2,4})*$'
    PHONE_NUMBER_PATTERN = r'^[0-9]{1,2}[ ][0-9]{10}$'
    PASSWORD_PATTERN = r'^(?=.*[A-Z])' + '(?=.*[a-z])' + '(?=.*[!@_#$%^&*])' + '(?=.*[0-9]).{8,}$'

    def validate_first_name(self, first_name):
        '''validate_first_name function:
            re.compile combine regex into pattern objects, which can be used for pattern matching.
             It also helps to search a pattern again without rewriting it.
             re.search return the matchobject if there is match in given string
             if it matches with the pattern it reurns true otherwise it will raise
             an exception and print the given statement
        '''

        pattern = re.compile(self.FIRST_NAME_PATTERN)
        validate = pattern.search(first_name)
        if not validate:
            raise UserException(" Enter First Name Starting With Capital letter and "
                                 "have minimum 3 characters")
        else:
            return True


    def validate_last_name(self, last_name):
        '''

        :param last_name:
        :return: True ,if it is valid
        User need to enter Last name start with Cap and
         has minimum 3 characters
        '''

        pattern = re.compile(self.LAST_NAME_PATTERN)
        validate = pattern.search(last_name)
        if not validate:
            raise UserException(" Enter Last Name Starting With Capital letter and "
                                 "have minimum 3 characters")
        else:
            return True


    def validate_email(self, email):
        '''

        :param email:
        :return: True , if it is valid
        User need to follow Email Id Pattern
          and test all sample emails
         e.g : abcd.she@gmail.com
        '''

        pattern = re.compile(self.EMAIL_PATTERN)
        validate = pattern.search(email)
        if not validate:
            raise UserException(" Please Enter The Valid Email ID ")
        else:
            return True

    def validate_phone_number(self, phone_number):
        '''

        :param phone_number:
        :return: True if it is valid
        User need to enter valid phone number format
            i.e; country code follow by space and 10 digit number
        '''

        pattern = re.compile(self.PHONE_NUMBER_PATTERN)
        validate = pattern.search(phone_number)
        if not validate:
            raise UserException(" Please Enter The Valid Phone Number ")
        else:
            return True

    def validate_password(self, password):
        '''

        :param password:
        :return: True , if it is valid
        Rule3 : User need to enter minimum 8 characters,
                 have at least one upper case,
                 must have one numeric number in the password,
                 and has exactly one special character
        '''

        pattern = re.compile(self.PASSWORD_PATTERN)
        validate = pattern.search(password)
        if not validate:
            raise UserException(" Please Enter The Valid password ")
        else:
            return True

    def mood_analyzer(self, first_name, last_name, phone_number, email, true=None):
        if self.validate_first_name(first_name) == true and self.validate_last_name(last_name) == true and self.validate_phone_number(phone_number) == true and self.validate_email(email) ==  true :
            return "HAPPY"
        else:
            return "SAD"