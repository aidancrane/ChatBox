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
        return 'Help needed'
    else:
        return False
