def get_fizzbuzz_for_int(n: int) -> str:
    output = ""

    if n % 3 == 0 and n != 0:
        output += "Fizz"

    if n % 5 == 0 and n != 0:
        output += "Buzz"

    if not output:
        output = str(n)

    return output


def test_get_fizzbuzz_for_int():
    assert get_fizzbuzz_for_int(0) == "0"
    assert get_fizzbuzz_for_int(1) == "1"
    assert get_fizzbuzz_for_int(3) == "Fizz"
    assert get_fizzbuzz_for_int(5) == "Buzz"
    assert get_fizzbuzz_for_int(15) == "FizzBuzz"
    assert get_fizzbuzz_for_int(16) == "16"


def get_fizzbuzz_list(n: int) -> list:
    return [get_fizzbuzz_for_int(i) for i in range(1, n + 1)]


def test_get_fizzbuzz_list():
    assert get_fizzbuzz_list(1) == ["1"]
    assert get_fizzbuzz_list(3) == ["1", "2", "Fizz"]
    assert get_fizzbuzz_list(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert get_fizzbuzz_list(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]
