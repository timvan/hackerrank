def test_removeSubsequentAnagrams():
    assert removeSubsequentAnagrams([]) == []
    assert removeSubsequentAnagrams(["a"]) == ["a"]
    assert removeSubsequentAnagrams(["a", "b"]) == ["a", "b"]
    assert removeSubsequentAnagrams(["a", "b", "a"]) == ["a", "b"]
    assert removeSubsequentAnagrams(["b", "a", "b", "a"]) == ["b", "a"]
    assert removeSubsequentAnagrams(["aag", "aga", "aag", "gaa"]) == ["aag"]


def test_funWithAnagrams():
    assert funWithAnagrams(["code", "aaagmnrs", "anagrams", "doce"]) == [
        "aaagmnrs",
        "code",
    ]
    assert funWithAnagrams(["aa", "bb", "cc", "aa"]) == ["aa", "bb", "cc"]
    assert funWithAnagrams(["ca", "bb", "ac", "aa"]) == ["aa", "bb", "ca"]
    assert funWithAnagrams([]) == []
    assert funWithAnagrams(["a"]) == ["a"]
    assert funWithAnagrams(["a", "b"]) == ["a", "b"]
    assert funWithAnagrams(["aag", "aga", "aag", "gaa"]) == ["aag"]


def removeSubsequentAnagrams(text: list) -> list:
    unique_anagrams = []
    unique_anagrams_chars_sorted = []

    for word in text:
        next_word_sorted = sorted(word)
        if next_word_sorted not in unique_anagrams_chars_sorted:
            unique_anagrams.append(word)
            unique_anagrams_chars_sorted.append(next_word_sorted)

    return unique_anagrams


def funWithAnagrams(text: list) -> list:
    return sorted(removeSubsequentAnagrams(text))
