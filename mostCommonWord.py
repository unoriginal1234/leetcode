def mostCommonWord(paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = []
        current_word = ""
        boops = ["!","?","'",",",";","."," "]
        #TO DO: make everything lowercase
        paragraph = paragraph.lower()
        # Loop through and parse out the words
        n = len(paragraph)
        for i in range(n):
            if paragraph[i] not in boops:
                current_word = current_word + paragraph[i]
            else:
                words.append(current_word)
                current_word = ""
            if i == n-1 and paragraph[i] not in boops:
                words.append(current_word)
        
        for word in words:
            if word in banned:
                words.remove(word)
            if word in boops:
                words.remove(word)

        # Count the words for the most common occurance
        biggest = 0
        for word in words:
            x = words.count(word)
            if x > biggest:
                biggest = x
                ans = word

        return ans

paragraph = "Bob. hIt, baLl"
banned = ["bob", "hit"]
y = mostCommonWord(paragraph, banned)
print(y)

