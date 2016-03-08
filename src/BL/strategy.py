class Strategy:
    def __init__(self, target_pairs):
        self.target_pairs = target_pairs

    def evaluate_node(self, string_list):
        """
        This is the heuristic function. Evaluate de list of chars in order to know
        how close to the solution is.
        :param string_list: list of chars
        :return: return the list of chars with its punctuation
        """
        current_pairs = self.obtain_pairs_number(string_list)
        punctuation = self.target_pairs - current_pairs
        return punctuation

    @staticmethod
    def obtain_pairs_number(string_list):
        """
        Otains the number of couples in the list
        :rtype: integer
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
