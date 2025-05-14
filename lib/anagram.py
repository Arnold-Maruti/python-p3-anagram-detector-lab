# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word=word

    def match(self,word):
        z=[]
        for x in word:
            word=[letter for letter in x]
            if (sorted(word)==sorted([char for char in self.word])):
                z.append(x)
                
            else:
                print("")
        return z

arnold=Anagram("listen")

print(arnold.match(["silent","enlist"]))
   