import time

# ---------------- NAIVE SEARCH ----------------
def naive_search(text, pattern):
    start = time.time()

    positions = []
    comparisons = 0

    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        match = True

        for j in range(m):
            comparisons += 1

            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            positions.append(i)

    end = time.time()

    return {
        "positions": positions,
        "time": end - start,
        "comparisons": comparisons
    }


# ---------------- KMP SEARCH ----------------
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


def kmp_search(text, pattern):
    start = time.time()

    positions = []
    comparisons = 0

    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    i = 0
    j = 0

    while i < n:
        comparisons += 1

        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            positions.append(i - j)
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    end = time.time()

    return {
        "positions": positions,
        "time": end - start,
        "comparisons": comparisons
    }


# ---------------- RABIN KARP SEARCH ----------------
def rabin_karp_search(text, pattern):
    start = time.time()

    positions = []
    comparisons = 0

    d = 256
    q = 101

    n = len(text)
    m = len(pattern)

    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):

        if p == t:

            for j in range(m):
                comparisons += 1

                if text[i + j] != pattern[j]:
                    break
            else:
                positions.append(i)

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q

            if t < 0:
                t += q

    end = time.time()

    return {
        "positions": positions,
        "time": end - start,
        "comparisons": comparisons
    }