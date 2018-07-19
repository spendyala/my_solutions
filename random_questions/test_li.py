class WordDistanceFinder:
    """
    This class will be given a list of words (such as might be tokenized
    from a paragraph of text), and will provide a method that takes two
    words and returns the shortest distance (in words) between those two
    words in the provided text.
 
    ::
      finder = WordDistanceFinder(["the", "quick", "brown", "fox", "quick", "junk", "fox"])
      assert finder.distance("fox", "the") == 3
      assert finder.distance("quick", "fox") == 1
 
    "quick" appears twice in the input. There are two possible distance values for "quick" and "fox":
        (3 - 1) = 2 and (4 - 3) = 1.
 
    Since we have to return the shortest distance between the two words we return 1.
 
    """
    def __init__(self, words):
        # Implementation here
        self.words = words
        self.words_index_dict = {}
        for idx, word in enumerate(words):                     # O(n)
            self.words_index_dict.setdefault(word, [])
            self.words_index_dict[word].append(idx)
         
    def distance(self, wordOne, wordTwo):
        # Implementation here
        word_one_list = self.words_index_dict.get(wordOne, []) # [1, 4] # k elements < n 
        word_two_list = self.words_index_dict.get(wordTwo, []) # [3, 6, 8, 10, 12, 14, 20, 100, 200] # m elements < n-1  5 7
        min_dist = None
        # 1 3 4
        for each_one in word_one_list:                 # O(k*m)
            for each_two in word_two_list:
                curr_dist = abs(each_one-each_two)
                if not min_dist or min_dist > curr_dist:
                    min_dist = curr_dist
        return min_dist

    def distance_2(self, wordOne, wordTwo):
        word_one_idx = -1
        word_two_idx = -1
        min_dist = None
        for idx, each_word in enumerate(self.words):     # O(n)
            if each_word == wordOne:
                word_one_idx = idx     # 4
            if each_word == wordTwo:
                word_two_idx = idx     # 6
            if word_one_idx > -1 and word_two_idx > -1:         
                curr_dist = abs(word_one_idx-word_two_idx)
                if not min_dist or min_dist > curr_dist:
                    min_dist = curr_dist
        return min_dist

    def distance_3(self, wordOne, wordTwo):
        try:
            min_one_idx = self.words_index_dict[wordOne][0]
            max_one_idx = self.words_index_dict[wordOne][-1]
        except Exception:
            return 'Not applicable'
        try:
            min_two_idx = self.words_index_dict[wordTwo][0]
            max_two_idx = self.words_index_dict[wordTwo][-1]
        except Exception:
            return 'Not applicable' 
        global_min = min_one_idx if min_one_idx <= min_two_idx else min_two_idx
        global_max = max_one_idx if max_one_idx >= max_two_idx else max_two_idx
        min_dist = None
        for idx, each_word in self.words[global_min, global_max]:     # O(n)
            if each_word == wordOne:
                word_one_idx = idx     # 4
            if each_word == wordTwo:
                word_two_idx = idx     # 6
            if word_one_idx > -1 and word_two_idx > -1:         
                curr_dist = abs(word_one_idx-word_two_idx)
                if not min_dist or min_dist > curr_dist:
                    min_dist = curr_dist
        return min_dist

