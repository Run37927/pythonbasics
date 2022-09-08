# def ispalin(string):
#     start = 0
#     end = len(string) - 1
#     while start < end:
#         if string[start] != string[end]:
#             return False
#         start += 1
#         end -= 1
#     return True


def is_palindrome(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and is_palindrome(string, i+1)

