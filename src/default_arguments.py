INPUT = [
    "100",
    "odd 2",
    "odd 7",
    "odd 5",
    "even 8",
    "odd 5",
    "odd 9",
    "even 8",
    "even 5",
    "odd 5",
    "odd 1",
    "even 5",
    "odd 9",
    "odd 8",
    "even 2",
    "even 5",
    "even 8",
    "odd 6",
    "odd 2",
    "odd 1",
    "even 7",
    "even 7",
    "odd 7",
    "odd 8",
    "even 1",
    "odd 7",
    "odd 6",
    "even 2",
    "odd 2",
    "even 1",
    "odd 9",
    "odd 5",
    "odd 6",
    "odd 7",
    "even 1",
    "odd 2",
    "even 8",
    "even 3",
    "odd 1",
    "even 9",
    "odd 5",
    "even 7",
    "even 3",
    "even 8",
    "even 8",
    "odd 9",
    "odd 2",
    "even 7",
    "odd 5",
    "even 3",
    "odd 10",
    "even 1",
    "even 4",
    "odd 4",
    "even 7",
    "even 2",
    "even 9",
    "even 4",
    "even 8",
    "even 9",
    "even 5",
    "odd 7",
    "odd 10",
    "even 3",
    "odd 4",
    "even 3",
    "even 9",
    "odd 2",
    "even 8",
    "even 10",
    "even 5",
    "odd 8",
    "even 4",
    "even 2",
    "odd 6",
    "odd 9",
    "even 6",
    "odd 1",
    "odd 1",
    "even 2",
    "even 7",
    "odd 9",
    "even 3",
    "even 7",
    "even 4",
    "odd 3",
    "odd 4",
    "even 6",
    "odd 1",
    "odd 5",
    "even 6",
    "odd 5",
    "odd 1",
    "odd 5",
    "odd 5",
    "odd 8",
    "odd 8",
    "odd 10",
    "odd 1",
    "odd 5",
    "even 9",
]


class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n, stream=EvenStream):

    for _ in range(n):
        print(stream.get_next())


queries = int(INPUT.pop(0))

for item in INPUT:
    stream_name, n = item.split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream)
