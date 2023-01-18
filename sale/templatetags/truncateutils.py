from django import template

register = template.Library()

@register.filter()
def smart_truncate(text, limit):
    char_count = 0
    words = text.split()
    result = []
    for word in words:
        length = len(word)
        if char_count + length > limit:
            result.append('...')
            break
        else:
            result.append(word)
            char_count += length
            
    return ' '.join(result)