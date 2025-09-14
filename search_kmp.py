def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено

def read_file(filename):
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

if __name__ == "__main__":
    text1 = read_file("article_1.txt")
    text2 = read_file("article_2.txt")
    patterns = {
        "existing_in_1": "інтерполяції",
        "existing_in_2": "інвертований"
    }

    for i, text in enumerate([text1, text2], 1):
        for pattern in patterns.values():
            print(f"Article {i}, searching for '{pattern}':")
            position = kmp_search(text, pattern)
            if position != -1:
                print(f"Substring found at index {position}")
            else:
                print("Substring not found")