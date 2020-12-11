import re

NAME_EXP = r'full_name_(\d+)$'


def get_element_index(user_form):
    '''Generator: Extract index from form
    '''
    name_email = (re.search(NAME_EXP, item).groups()[0] for item in user_form if re.search(
        NAME_EXP, item) is not None)
    return name_email


def get_names_and_emails(user_form, indexes):
    '''Generator: Extract names and email
    '''
    for index in indexes:
        player_info = {
            'name': user_form['full_name_' + index],
            'email': user_form['email_' + index]
        }
        yield player_info
