# valid_parentheses.py

def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping:
            if not stack or stack.pop() != mapping[ch]:
                return False
    return not stack


if __name__ == "__main__":
    s = input("Enter parentheses string: ")
    print("Valid" if is_valid(s) else "Invalid")
