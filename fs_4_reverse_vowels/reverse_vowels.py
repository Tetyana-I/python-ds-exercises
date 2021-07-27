def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    s_vowels_list = [char for char in s if char in vowels]
    s_vowels_list.reverse()
    result_string = []
    i = 0
    for char in s:
        if char in vowels:
            result_string.append(s_vowels_list[i])
            i +=1
        else:
            result_string.append(char)
    return ''.join(result_string)