def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    phrase_lower = phrase.lower()
    vowels_in_phrase = [char for char in phrase_lower if char in vowels]
    return {char : phrase_lower.count(char) for char in vowels_in_phrase}

    