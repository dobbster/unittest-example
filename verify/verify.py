'''User program'''

#pylint: disable=old-style-class
class User:
    '''User-related information storage'''

    # Initialize user
    def __init__(self, name, phone, email):
        '''Initializer'''
        self.name = name
        self.phone = phone
        self.email = email

    # Getter for name
    def get_name(self):
        '''Return username'''
        return self.name

    # Getter for phone
    def get_phone(self):
        '''Return phone'''
        return self.phone

    # Getter for email
    def get_email(self):
        '''Return email'''
        return self.email

    # Object representation
    def __str__(self):
        '''Used in print statements'''
        # Print out custom user message
        return 'Hi, my name is {} and you can contact me at {} or {}' \
            .format(self.name, self.phone, self.email)

me = User('Harsh', 7506108466, 'harsh.sinha@quantiphi.com')
print(me)