def isSubsequence(pattern, text):
    if len(pattern) == 0:
        return True
    if len(text) == 0:
        return False

    if pattern[0] == text[0]:
        return isSubsequence(pattern[1:], text[1:])
    else:
        return isSubsequence(pattern, text[1:])

pattern = input()
text = input()
print(isSubsequence(pattern, text))