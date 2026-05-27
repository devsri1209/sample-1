# ---------------- NAIVE SEARCH ----------------

def naive_search(text, pattern):

    matches = []

    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):

        if text[i:i+m] == pattern:

            matches.append(i)

    return matches


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

    matches = []

    lps = compute_lps(pattern)

    i = 0
    j = 0

    while i < len(text):

        if pattern[j] == text[i]:

            i += 1
            j += 1

        if j == len(pattern):

            matches.append(i - j)

            j = lps[j - 1]

        elif i < len(text) and pattern[j] != text[i]:

            if j != 0:

                j = lps[j - 1]

            else:

                i += 1

    return matches


# ---------------- RABIN KARP ----------------

def rabin_karp(text, pattern, prime=101):

    matches = []

    d = 256

    n = len(text)

    m = len(pattern)

    h = pow(d, m - 1) % prime

    p = 0
    t = 0

    for i in range(m):

        p = (
            d * p + ord(pattern[i])
        ) % prime

        t = (
            d * t + ord(text[i])
        ) % prime

    for i in range(n - m + 1):

        if p == t:

            if text[i:i+m] == pattern:

                matches.append(i)

        if i < n - m:

            t = (
                d * (
                    t - ord(text[i]) * h
                )
                + ord(text[i + m])
            ) % prime

    return matches


# ---------------- BOYER MOORE ----------------

def bad_char_heuristic(pattern):

    bad_char = {}

    for i in range(len(pattern)):

        bad_char[pattern[i]] = i

    return bad_char


def boyer_moore(text, pattern):

    matches = []

    m = len(pattern)

    n = len(text)

    bad_char = bad_char_heuristic(
        pattern
    )

    s = 0

    while s <= n - m:

        j = m - 1

        while (
            j >= 0
            and pattern[j]
            == text[s + j]
        ):

            j -= 1

        if j < 0:

            matches.append(s)

            s += (
                m - bad_char.get(
                    text[s + m],
                    -1
                )
                if s + m < n
                else 1
            )

        else:

            s += max(
                1,
                j - bad_char.get(
                    text[s + j],
                    -1
                )
            )

    return matches