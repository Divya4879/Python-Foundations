# Problem 8-15: Printing Models

from printing_functions import *

def printing_model(name, field, specialization, **user_info):
    user_info['Name']= name
    user_info['Specialization']= specialization
    user_info['field']= field
    return user_info
    
printing_dict(printing_model('Divya singh',
                             'tech',
                             'backend development',
                             fav_lang='Python',
                             degree='MTECH'))