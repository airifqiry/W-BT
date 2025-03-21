from django.core.exceptions import ValidationError
import re

def custom_pass_validation(password):
    if len(password) < 8:
        raise ValidationError("Паролата трябва да съдържа поне 8 символа!")
    
    if not any(char.isdigit() for char in password):
        raise ValidationError("Паролата трябва да съдържа поне една цифра!")
    
    if not any(char.isupper() for char in password):
        raise ValidationError("Паролата трябва да съдържа поне една главна буква!")
    return password 
    

def validate_phone_number(value):
    phone_str = str(value)  # Преобразуваме в стринг, за да избегнем грешки


    if len(phone_str) > 13:
        raise ValidationError("Телефонният номер не може да бъде повече от 9 символа.")
    
    

    

