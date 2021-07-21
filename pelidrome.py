def pelidrom_checker(s):
    rev_s=s[::-1]
    if s==rev_s:
        return True
    else:
        return False


print(pelidrom_checker("789987"))
print(pelidrom_checker("rashi"))

