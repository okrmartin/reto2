from sortedcontainers import SortedListWithKey
from strategy import Strategy


def CreateString(n, k):
    initialValue = 'A' * n
    char_list = list(initialValue)
    h = Strategy(k)
    candidates = SortedListWithKey(key=h.evaluate_node)
    candidates.add(char_list)

    altura = 0
    while altura < k+1:
        try:
            candidate = candidates.pop(0)
            punctuation = h.evaluate_node(candidate)
            if punctuation == 0:
                return ''.join(candidate)

            l = expand(candidate)
            for expanded in l:
                punctuation = h.evaluate_node(expanded)
                if punctuation >= 0:
                    candidates.add(expanded)

            altura += 1
        except IndexError:
            return ''
    return ''


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
