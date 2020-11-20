import re

from MainUserRegistration.UserRegistrationException import InputException

class UserRegistration:

    FIRST_NAME_PATTERN = r'^[A-Z][A-Za-z]{2,}$'

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

