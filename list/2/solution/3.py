def has_alnum(strings):

    new_strings = []

    def has_alpha(string):
        for char in string:
            if char.isalpha():
                return True
        return False

    def has_numeric(string):
        for char in string:
            if char.isnumeric():
                return True
        return False

    for string in strings:
        if has_alpha(string) and has_numeric(string):
            new_strings.append(string)

    return new_strings
