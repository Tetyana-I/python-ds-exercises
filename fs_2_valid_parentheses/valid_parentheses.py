def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    stack = []
    for i in parens:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) > 0 and stack[len(stack)-1] == '(':
                stack.pop()
            else: 
                return False
    if len(stack) == 0:
        return True
    else:
        return False