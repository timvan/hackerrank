def transpose(matrix: list):
    # number_of_items = len(matrix)
    length_of_items = len(matrix[0])
    transposed_items = []

    for i in range(0, length_of_items):
        transposed_items.append("".join([m[i] for m in matrix]))

    return transposed_items


def remove_illegal_chars_between_alnum(string: str):
    decoded_message = ""
    cache = ""

    for c in string:

        if c.isalnum():
            if cache and not decoded_message:
                decoded_message += cache
                cache = ""
            elif cache:
                decoded_message += " "
                cache = ""
            decoded_message += c
        else:
            cache += c

    return decoded_message + cache


def test_transpose():
    assert transpose(["A", "B", "C"]) == ["ABC"]
    assert transpose(["AAA", "BBB", "CCC"]) == ["ABC", "ABC", "ABC"]


def test_remove_illegal_chars_between_alnum():
    assert remove_illegal_chars_between_alnum("") == ""
    assert remove_illegal_chars_between_alnum("AA") == "AA"
    assert remove_illegal_chars_between_alnum("A1A") == "A1A"
    assert remove_illegal_chars_between_alnum("A1A#") == "A1A#"
    assert remove_illegal_chars_between_alnum("A 1A#") == "A 1A#"
    assert remove_illegal_chars_between_alnum("A #1A#") == "A 1A#"
    assert remove_illegal_chars_between_alnum("A #1A") == "A 1A"
    assert remove_illegal_chars_between_alnum("##A #1A") == "##A 1A"


def test_decode_matrix():
    assert (
        decode_matrix(["Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "ir!"])
        == "This is Matrix#  %!"
    )
    assert (
        decode_matrix(["T%$r%r", "h%Mi$i", "iiaxsp", "sst%ct"])
        == "This is Matrix script"
    )
    assert (
        decode_matrix(["#%$r%r$n ", "O%Mi$iTi$", "yiaxsprt ", "est%ctiy#", "  t c i %"])
        == "#Oye is Mattrix sccript Triinity  $ #%"
    )


def decode_matrix(rows_of_strings: list):
    return remove_illegal_chars_between_alnum("".join(transpose(rows_of_strings)))


def run_tests():
    test_transpose()
    test_remove_illegal_chars_between_alnum()
    test_decode_matrix()


run_tests()
