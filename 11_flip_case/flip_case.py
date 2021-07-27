def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase_array = [*phrase]
    new_phrase = []
    for char in phrase_array:
        if char == to_swap:
            new_phrase.append(char.lower()) if to_swap.isupper() else new_phrase.append(char.upper())
        elif char.upper() == to_swap.upper():
            new_phrase.append(char.lower()) if char.isupper() else new_phrase.append(char.upper())
        else:
            new_phrase.append(char)
    return "".join(new_phrase)
