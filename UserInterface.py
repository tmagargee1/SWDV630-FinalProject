import re
from urllib import response


def askYesNo(question):
    question += '? (Y/N):'
    response = input(question).upper().strip()
    while(response not in ['Y', 'N']):
        response = input('Please enter only "Y" or "N":').upper().strip()
    return response == 'Y'

def enterNumber(question, items):
    optionsString = "\n"
    count = 0
    for item in items:
        count += 1
        optionsString += '{}: {}\n'.format(count, item)
        
    promptString = "Enter number between 1 to {} or (-1 to go back): ".format(count)
    question += optionsString + promptString
    testArray = ['-1'] +  list(map(str, range(1, count + 1)))
    response = input(question).upper().strip()
    while(response not in testArray):
        response = input('Invalid input... ' + promptString).upper().strip()

    return int(response)

def GetValidString(prompt, regex ='^(?!\s*$).+', invalidInputText = 'must not be blank'):
    prompt += ': '
    invalidInputText = 'Input ' + invalidInputText + ' (try again): '
    response = input(prompt)
    while(re.search(response, regex)):
        response = input(invalidInputText)
    
    return response.strip()
