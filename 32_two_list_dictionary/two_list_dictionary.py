def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    key_value_dict = {}
    for i in range(len(keys)):
        key_value_dict[keys[i]] = key_value_dict.get(keys[i],None)
    count = len(keys)  if len(keys) <= len (values) else len(values) 
    for i in range(count):
        key_value_dict[keys[i]] = values[i]
    return key_value_dict