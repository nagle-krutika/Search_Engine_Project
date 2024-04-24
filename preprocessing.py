# function to normalize data
def normalization(data):
    return data.lower()


# function to remove punctuation
from string import punctuation
def remove_punctuation(data):
    return ''.join([i for i in data if i not in punctuation])


# function to remove digits
def remove_digit(data):
    x=''
    for i in data:
        if i.isdigit() == False:
            x = x + i
    return x

# function to fixing contraction
import contractions
def contraction_fixing(data):
    return contractions.fix(data)

# funtion to fixing accented text
from unidecode import unidecode
def accented_fixing(data):
    return unidecode(data)

print("sucessfully runn the preprocessing")