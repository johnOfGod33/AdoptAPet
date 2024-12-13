import re

def validate_input(nom, age, espece, race, courriel, cp):
    regex = {
        'nom': r'^[^\s,]{3,20}$',
        'age': r'^(?:[1-9]|[1-2][0-9]|30)$',
        'espece': r'^[^\s,]+$',
        'race': r'^[^\s,]+$',
        'courriel': r'^[^\s@]+@[^\s@]+\.[^\s@]+$',
        'cp': r'^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$'
    }

    return all(re.match(regex[field], value) for field, value in zip(regex.keys(), [nom, age, espece, race, courriel, cp]))
