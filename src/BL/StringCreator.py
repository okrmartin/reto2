def CreateString(n, k):
    initialValue = 'A' * n
    initialList = list(initialValue)
    expandedNodes = Expand(initialList)


def Expand(value):
    l = list()
    for x in xrange(1, len(value)):
        iValue = list(value)
        if value[-x] == 'B':
            iValue[-x] = 'A'
            iValue[-x - 1] = 'B'
        else:
            iValue[-x] = 'B'

        l.append(iValue)

    iValue = list(value)
    if value[0] == 'B':
        iValue[0] = 'A'
    elif value[0] == 'A':
        iValue[0] = 'B'

    l.append(iValue)
    return l


def evaluate_node(string_list, target_pairs):
    """
    This is the heuristic function. Evaluate de list of chars in order to know
    how close to the solution is.
    :param string_list: list of chars
    :param target_pairs: number of couples that are requested
    :return: return the list of chars with its punctuation
    """
    current_pairs = obtain_pairs_number(string_list)
    punctuation = target_pairs - current_pairs
    evaluated_node = {'stringList': string_list, 'punctuation': punctuation}
    return evaluated_node


def obtain_pairs_number(string_list):
    """
    Otains the number of couples in the list
    :param string_list: is a character list. This chars should be 'A' or 'B'
    :return: the number of couples in the current list of chars
    """
    current_pairs = 0
    iterations = len(string_list) - 1
    for i in range(0, iterations):
        if string_list[i] == 'A':
            for letter in string_list[i + 1:]:
                if letter == 'B':
                    current_pairs += 1

    return current_pairs
