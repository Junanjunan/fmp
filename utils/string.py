def get_camel_text(text):
    components = text.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])