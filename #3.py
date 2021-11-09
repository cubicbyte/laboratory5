class ModifiedStr(str):
    def checkRepeat(self, s):
        for i in range(0, len(s) - 3):
            if s[i] == s[i + 1] == s[i + 2]:
                return True
        return False
    
    def isPalindrome(self, s):
        s = s.upper()
        length = len(s)

        if length < 2:
            return True
        
        for i in range(int(length / 2)):
            if s[i] != s[length - i - 1]:
                return False
        
        return True

def main():
    mod = ModifiedStr()
    print(mod.checkRepeat('1233456667890'))
    print(mod.isPalindrome('123454321'))
    print(mod.isPalindrome('D12344321d'))
    print(mod.isPalindrome('D123454322d'))
    print(mod.isPalindrome('12344322'))

if __name__ == '__main__':
    main()