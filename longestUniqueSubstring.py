def longestSubstring(string: str) -> int:
    maxLength = 0
    for i, charX in enumerate(string):
        char_occurance = set()

        for j, charY in enumerate(string[i:]):
            if charY in char_occurance:
                break
            else:
                char_occurance.add(charY)
                maxLength = max(maxLength, j - i + 1)

    return maxLength


def longestSubStringOptimized(string: str) -> int:
    start = 0  # Starting index
    mapping = dict()

    maxLength = 0
    for i, char in enumerate(string):
        if char in mapping and mapping[char] >= start:
            start = mapping[char] + 1

        end = i
        mapping[char] = i
        maxLength = max(maxLength, end - start + 1)

    return maxLength


if __name__ == "__main__":
    length = longestSubStringOptimized("abba")
    print(length)
