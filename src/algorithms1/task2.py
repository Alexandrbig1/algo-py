from collections import deque

def is_pal(string):
    normalized_string = ''.join(char.lower() for char in string if char.isalnum())
    char_deque = deque(normalized_string)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

print(is_pal("checking status"))
print(is_pal("Race car"))