class merge_string_alternately1:
    def merge(self, word1: str, word2: str):

        max_length = max(len(word1),len(word2))
        res = []

        for i in range(max_length):
            if i < len(word1):
                res.append(word1[i])
            if i < len(word2):
                res.append(word2[i])

        return ''.join(res)