def comment_cleaner(comment):
    # need to clean up any , \ ' " ` characters so I can pass them into my CSV's
    comment = comment
    new_comment = ''

    for char in comment:
        if char == ',':
            new_comment = new_comment + '\\,'
        elif char == '':

    return new_comment