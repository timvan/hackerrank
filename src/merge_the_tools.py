# assumptions
# should we consider lower/upper?
# what about k = 0, what happens if (len(s) / k) % k != 0


def split_string_into_len_string_over_k_substrings(string: str, k: int):

    sub_strings = int(len(string) / k)

    substrings = []

    for i in range(0, sub_strings):
        substrings.append(string[i * k : (i + 1) * k])

    return substrings


def get_unique_chars(string: str):

    distinct_chars = []
    for char in string:
        if char not in distinct_chars:
            distinct_chars.append(char)
    return "".join(distinct_chars)


def get_substrings_with_unique_chars(string: str, k: int):
    return [
        get_unique_chars(s)
        for s in split_string_into_len_string_over_k_substrings(string, k)
    ]


def test_split_string_into_len_string_over_k_substrings():
    assert split_string_into_len_string_over_k_substrings("AAA", 1) == ["A", "A", "A"]
    assert split_string_into_len_string_over_k_substrings("AAA", 3) == ["AAA"]
    assert split_string_into_len_string_over_k_substrings("AAABBB", 2) == [
        "AA",
        "AB",
        "BB",
    ]


def test_get_unique_chars():
    assert get_unique_chars("") == ""
    assert get_unique_chars("A") == "A"
    assert get_unique_chars("AB") == "AB"
    assert get_unique_chars("AAAAAB") == "AB"
    assert get_unique_chars("AAAAABBBBB") == "AB"
    assert get_unique_chars("BAAAAABBBBB") == "BA"
    assert get_unique_chars("BAAAACCABBBBCB") == "BAC"
    assert get_unique_chars("BAAAACABBBBCB") == "BAC"


def test_get_substrings_with_unique_chars():
    assert get_substrings_with_unique_chars("A", 1) == ["A"]
    assert get_substrings_with_unique_chars("AB", 1) == ["A", "B"]
    assert get_substrings_with_unique_chars("AB", 2) == ["AB"]
    assert get_substrings_with_unique_chars("ABCC", 2) == ["AB", "C"]
    assert get_substrings_with_unique_chars("ABCDCC", 2) == ["AB", "CD", "C"]
    assert get_substrings_with_unique_chars("ABDDCC", 3) == ["ABD", "DC"]


def test_clean_inputs():
    assert clean_inputs("Aa", 1) == ("AA", 1)
    assert clean_inputs("AaB", 1) == ("AAB", 1)
    assert clean_inputs("Aa ", 1) == ("AA", 1)
    assert clean_inputs("Aa#", 1) == ("AA", 1)
    assert clean_inputs("#Aa", 1) == ("AA", 1)


def run_tests():
    test_get_unique_chars()
    test_split_string_into_len_string_over_k_substrings()
    test_get_substrings_with_unique_chars()
    test_clean_inputs()


def clean_inputs(string, k):
    string = "".join([c for c in string if c.isalpha()])
    string = string.upper()
    # string = string.replace(" ", "")
    k = int(k)
    return string, k


def merge_the_tools(string, k):
    # your code goes here

    # string, k = clean_inputs(string, k)

    substrings = get_substrings_with_unique_chars(string, k)
    [print(s) for s in substrings]


if __name__ == "__main__":
    run_tests()
    # string, k = input(), int(input())
    # merge_the_tools(string, k)
