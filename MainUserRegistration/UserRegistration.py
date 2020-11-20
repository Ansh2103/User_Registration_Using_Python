import re

from MainUserRegistration.UserRegistrationException import InputException

class UserRegistration:

    FIRST_NAME_PATTERN = r'^[A-Z][a-z]{3,}$'
    LAST_NAME_PATTERN = r'^[A-Z][a-z]{3,}$'
    EMAIL_PATTERN = r'^[0-9a-zA-Z]+([._+-][0-9a-zA-Z]+)*[@][0-9A-Za-z]+([.][a-zA-Z]{2,4})*$'
    PHONE_NUMBER_PATTERN = '^[0-9]{1,2}[ ][0-9]{10}$'
    PASSWORD_PATTERN = '^(?=.*[A-Z])(?=.*[a-z]).{8,}$'

    def validate_first_name(self, first_name):
        '''validate_first_name function:
            re.compile combine regex into pattern objects, which can be used for pattern matching.
             It also helps to search a pattern again without rewriting it.
             re.search return the matchobject if there is match in given string
             if it matches with the pattern it reurns true otherwise it will raise
             a exception and print the given statement
        '''

        pattern = re.compile(self.FIRST_NAME_PATTERN)
        validate = pattern.search(first_name)
        if not validate:
            raise InputException(" Enter First Name Starting With Capital letter and "
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
            raise InputException(" Enter Last Name Starting With Capital letter and "
                                 "have minimum 3 characters")
        else:
            return True


    def validate_email(self, email):
        '''

        :param email:
        :return: True , if it is valid
        User need to follow Email Id Pattern
         e.g : abcd.she@gmail.com
        '''

        pattern = re.compile(self.EMAIL_PATTERN)
        validate = pattern.search(email)
        if not validate:
            raise InputException(" Please Enter The Valid Email ID ")
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
            raise InputException(" Please Enter The Valid Phone Number ")
        else:
            return True

    def validate_password(self, password):
        '''

        :param password:
        :return: True , if it is valid
        Rule1 : User need to enter minimum 8 characters
                and have at least one upper case
        '''

        pattern = re.compile(self.PASSWORD_PATTERN)
        validate = pattern.search(password)
        if not validate:
            raise InputException(" Please Enter The Valid password ")
        else:
            return True