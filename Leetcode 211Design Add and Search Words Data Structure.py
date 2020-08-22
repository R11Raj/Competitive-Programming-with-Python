class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=collections.defaultdict(list)
        
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.root[len(word)].append(word)
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if '.' not in word:
            return word in self.root[len(word)]
        
        dots=set()
        for i in range(len(word)):
            if word[i]=='.':
                dots.add(i)
        for i in self.root[len(word)]:
            t=i
            for j in dots:
                t=t[:j]+'.'+t[j+1:]
            if t==word:
                return True
        return False
