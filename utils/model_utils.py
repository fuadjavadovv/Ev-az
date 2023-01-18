from django.utils.text import slugify

eq = {'ü': 'u', 'ç': 'ch', 'ş': 'sh', 'ı': 'i', 'ə': 'e', 'ö': 'o', 'ğ': 'gh'}

def make_slug(text):
    text = ''.join(eq.get(i, i) for i in text.lower())
    text = slugify(text)
    return text