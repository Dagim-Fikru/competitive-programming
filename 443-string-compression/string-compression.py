class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append(" ")
        str_ = ""
        x = 0
        count = 1
        while x <len(chars)-1:
            if chars[x] == chars[x+1]:
                count +=1
            elif chars[x] != chars[x+1]:
                str_ += chars[x]
                if count == 1:
                    pass
                else:
                    str_ += str(count)
                    count = 1
            x+=1
        while chars:
            chars.pop()
        # return len(chars)
        for i in str_:
            chars.append(i)
        return len(str_)
            