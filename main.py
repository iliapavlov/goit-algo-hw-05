import timeit # type: ignore

from search_bm import build_shift_table, boyer_moore_search as search_bm
from search_kmp import compute_lps, kmp_search as search_kmp
from search_rk import polynomial_hash, rabin_karp_search as search_rk

def read_file(filename):
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=100)

if __name__ == "__main__":
    text1 = read_file("article_1.txt")
    text2 = read_file("article_2.txt")

    patterns = {
        "existing_in_1": "інтерполяції",
        "existing_in_2": "інвертований"
    }

    results = []

    for i, text in enumerate([text1, text2], 1):
        for pattern_type, pattern in patterns.items():
            bm_time = measure_time(search_bm, text, pattern)
            kmp_time = measure_time(search_kmp, text, pattern)
            rk_time = measure_time(search_rk, text, pattern)

            results.append((f"Article {i} - {pattern_type}", bm_time, kmp_time, rk_time))
    
    for result in results:
        article, bm_time, kmp_time, rk_time = result
        print(f"{article}: Boyer-Moore: {bm_time:.6f}s, KMP: {kmp_time:.6f}s, Rabin-Karp: {rk_time:.6f}s")
