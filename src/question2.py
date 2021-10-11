def maximumOccurringCharacter(text: str) -> str:
    unique_letters = []
    letter_counts = []

    for char in text:

        if char not in unique_letters:
            unique_letters.append(char)
            letter_counts.append(1)

        else:
            letter_counts[unique_letters.index(char)] += 1

    return unique_letters[letter_counts.index(max(letter_counts))]


def test_maximumOccurringCharacter():
    assert maximumOccurringCharacter("helloworld") == "l"
    assert maximumOccurringCharacter("a") == "a"
    assert maximumOccurringCharacter("aab") == "a"
    assert maximumOccurringCharacter("aabb") == "a"
    assert maximumOccurringCharacter("aabbcb") == "b"
