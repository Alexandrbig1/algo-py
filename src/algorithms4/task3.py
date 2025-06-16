import timeit

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""
    except IOError:
        print(f"Error reading file: {file_path}")
        return ""

def build_shift_table(pattern):
    """Builds the shift table for the Boyer-Moore algorithm."""
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    """Performs the Boyer-Moore search algorithm."""
    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1

def compute_lps(pattern):
    """Computes the longest prefix suffix (LPS) array for the KMP algorithm."""
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
    """Performs the Knuth-Morris-Pratt (KMP) search algorithm."""
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

    return -1

def polynomial_hash(s, base=256, modulus=101):
    """Computes the polynomial hash of a string."""
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1, modulus)
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    """Performs the Rabin-Karp search algorithm."""
    substring_length = len(substring)
    main_string_length = len(main_string)

    base = 256
    modulus = 101

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    h_multiplier = pow(base, substring_length - 1, modulus)

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1

# Read text files
text1 = read_file('text1.txt')
text2 = read_file('text2.txt')

# Define patterns
pattern_exist_text1 = "On the next step, you need to choose the next largest denomination coins that can be used to give the remaining change - two 10-cent coins."
pattern_non_exist_text1 = "qweasdasdeuewjgh [piotyp lertjlk kdshjf ewhjrg."

pattern_exist_text2 = "The B+ tree structure showed results close to the hash table. The access time to an individual element is constant in both cases, but the B+ tree has certain advantages: elements are stored sorted, and there is no need to expand the memory area when resizing."
pattern_non_exist_text2 = "ljakdheurwrhe ewirywhikb klxcvjlkxj qwiwbdm qioer."

# Measure search times
time_bm_exist_text1 = timeit.timeit(lambda: boyer_moore_search(text1, pattern_exist_text1), number=100)
time_knuth_exist_text1 = timeit.timeit(lambda: kmp_search(text1, pattern_exist_text1), number=100)
time_rk_exist_text1 = timeit.timeit(lambda: rabin_karp_search(text1, pattern_exist_text1), number=100)

time_bm_non_exist_text1 = timeit.timeit(lambda: boyer_moore_search(text1, pattern_non_exist_text1), number=100)
time_knuth_non_exist_text1 = timeit.timeit(lambda: kmp_search(text1, pattern_non_exist_text1), number=100)
time_rk_non_exist_text1 = timeit.timeit(lambda: rabin_karp_search(text1, pattern_non_exist_text1), number=100)

time_bm_exist_text2 = timeit.timeit(lambda: boyer_moore_search(text2, pattern_exist_text2), number=100)
time_knuth_exist_text2 = timeit.timeit(lambda: kmp_search(text2, pattern_exist_text2), number=100)
time_rk_exist_text2 = timeit.timeit(lambda: rabin_karp_search(text2, pattern_exist_text2), number=100)

time_bm_non_exist_text2 = timeit.timeit(lambda: boyer_moore_search(text2, pattern_non_exist_text2), number=100)
time_knuth_non_exist_text2 = timeit.timeit(lambda: kmp_search(text2, pattern_non_exist_text2), number=100)
time_rk_non_exist_text2 = timeit.timeit(lambda: rabin_karp_search(text2, pattern_non_exist_text2), number=100)

# Print results
print(f"For text 1 with existing substring:")
print(f"Boyer-Moore: {time_bm_exist_text1:.6f} sec")
print(f"Knuth-Morris-Pratt: {time_knuth_exist_text1:.6f} sec")
print(f"Rabin-Karp: {time_rk_exist_text1:.6f} sec")

print(f"\nFor text 1 with non-existing substring:")
print(f"Boyer-Moore: {time_bm_non_exist_text1:.6f} sec")
print(f"Knuth-Morris-Pratt: {time_knuth_non_exist_text1:.6f} sec")
print(f"Rabin-Karp: {time_rk_non_exist_text1:.6f} sec")

print(f"\nFor text 2 with existing substring:")
print(f"Boyer-Moore: {time_bm_exist_text2:.6f} sec")
print(f"Knuth-Morris-Pratt: {time_knuth_exist_text2:.6f} sec")
print(f"Rabin-Karp: {time_rk_exist_text2:.6f} sec")

print(f"\nFor text 2 with non-existing substring:")
print(f"Boyer-Moore: {time_bm_non_exist_text2:.6f} sec")
print(f"Knuth-Morris-Pratt: {time_knuth_non_exist_text2:.6f} sec")
print(f"Rabin-Karp: {time_rk_non_exist_text2:.6f} sec")