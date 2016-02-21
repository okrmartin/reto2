from sortedcontainers import SortedListWithKey
from strategy import Strategy


def CreateString(n, k):
    initialValue = 'A' * n
    char_list = list(initialValue)
    h = Strategy(k)
    candidates = SortedListWithKey(key=h.evaluate_node)
    candidates.add(char_list)

    candidate = candidates.pop(0)
    punctuation = h.evaluate_node(candidate)
    if punctuation == 0:
        return ''.join(candidate)
    else:
        if punctuation == 99999:
            return ''

    l = expand(candidate)
    for expanded in l:
        candidates.add(expanded)


def expand(value):
    l = list()
    for x in xrange(1, len(value)):
        result_value = list(value)
        if value[-x] == 'B':
            result_value[-x] = 'A'
            result_value[-x - 1] = 'B'
        else:
            result_value[-x] = 'B'

        l.append(result_value)

    result_value = list(value)
    if value[0] == 'B':
        result_value[0] = 'A'
    elif value[0] == 'A':
        result_value[0] = 'B'

    l.append(result_value)
    return l
