def perevod(n,s):
    if n < s:
        return str(n)
    return perevod(n//s,s)+str(n%s)
