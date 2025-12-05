def longest_unique_substring(s):
    start = 0
    max_len = 0
    used = {}

    for i, ch in enumerate(s):
        if ch in used and used[ch] >= start:
            start = used[ch] + 1

        used[ch] = i
        max_len = max(max_len, i - start + 1)

    return max_len

def has_four_ones_circular(binary_string):
    doubled = binary_string + binary_string
    return "1111" in doubled

s = "ABCABCFKAB"

print(longest_unique_substring(s))  # خروجی: 5

print(has_four_ones_circular("1010111"))  # True
