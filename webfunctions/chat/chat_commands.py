#import logMaster as log
import re

def sanitize(text):
    allowedPattern = re.compile(r'[^a-zA-Z0-9!@#$%^&*()?>|<"{}.,/\\\' _+;:-=]')
    text = re.sub(allowedPattern, '', text)
    return text

print (sanitize("kk^(*&^\'%$#@!)^0^{ Gawd<>[]\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\}"))
