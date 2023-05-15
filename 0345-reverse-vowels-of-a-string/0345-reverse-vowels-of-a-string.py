class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
        listOfS = list(s)
        i=0
        j=len(listOfS)-1
        while i<j:
            if listOfS[i] not in vowels:
                i+=1
            elif listOfS[j] not in vowels:
                j-=1
            elif listOfS[i] in vowels and listOfS[j] in vowels:
                listOfS[i], listOfS[j] = listOfS[j], listOfS[i]
                i+=1
                j-=1
        return "".join(listOfS)
            