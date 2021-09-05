# set up django for stand alone stuff
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
django.setup()
# import our class (must come after we've set up django)
from second_app.models import User

# import and setup faker
from faker import Faker
fakegenerator = Faker()

# functions to populate the fake data and save them.
def populate(n=20):
    for element in range(n):
        fake_first = fakegenerator.first_name()
        fake_last = fakegenerator.last_name()
        fake_email = fakegenerator.email()
        new_user = User(first=fake_first, 
                        last=fake_last,
                        email=fake_email)
        print(new_user)
        new_user.save()
        # test to see if it was working
        # print({'first': fake_first,
        #         'last': fake_last,
        #         'email': fake_email})

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete')