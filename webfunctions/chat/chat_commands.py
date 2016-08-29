import logMaster as log
import re

def sanitize(text):
    text = text.replace("\\\'","'").replace("'","\\\'")
    allowedPattern = re.compile(r'[^a-zA-Z0-9!@#$%^&*()?>|<"{}.,/\\\' _+;:-=]')
    text = re.sub(allowedPattern, '', text)
    return strip_tags(text)

def strip_tags(text):
    removePattern = re.compile(r'<.*?>')
    text = re.sub(removePattern, '', text)
    return text

def check_empty(text):
    if text == '' or len(text) > 255:
        return False
    else:
        return text

def check_for_commands(text):
    text = sanitize(text)
    if text[:1] == '/':
        text = text.replace(text[:1], "", 1).split()
        if text[0] == 'say':
            bark = ""
            for i in text:
                bark = bark + " " + i
            return bark[5:]
        elif len(text) == 1:
            if text[0] == 'help':
                return 'You asked for helpie help :)'
            else:
                return 'len 1'
        elif len(text) == 2:
            return 'len 2'
        elif len(text) == 3:
            return 'len 3'
        elif len(text) == 4:
            return 'len 4'
        elif len(text) == 5:
            return 'len 5'
        elif text[0] == 'say':
            for i in text:
                return text[i]
        else:
            return 'Sorry, that is not a command that is currently supported.'


    else:
        return False
