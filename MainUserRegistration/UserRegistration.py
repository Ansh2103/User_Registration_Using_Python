import re

from MainUserRegistration.UserRegistrationException import InputException

class UserRegistration:

    FIRST_NAME_PATTERN = r'^[A-Z][A-Za-z]{2,}$'
    LAST_NAME_PATTERN = r'^[A-Z][A-Za-z]{2,}$'

    def validate_first_name(self, first_name):

        pattern = re.compile(self.FIRST_NAME_PATTERN)
        validate = pattern.search(first_name)
        if not validate:
            raise InputException(" Enter First Name Starting With Capital letter and "
                                 "have minimum 3 characters")
        else:
            return True

