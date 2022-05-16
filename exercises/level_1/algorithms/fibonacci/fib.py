from typing import List
import json
import os


def default_memo() -> List[int]:
    return [0, 1, 1]


def fib(n: int, memo: List[int] = None) -> int:
    if not memo:
        memo = default_memo()

    i = len(memo) - 1

    while i < n:
        memo.append(memo[i - 1] + memo[i])
        i += 1

    return memo[n]


class FibMemo:
    def __init__(self, memo: List[int] = None):
        self.memo = memo or default_memo()

    def __call__(self, n: int) -> int:
        return fib(n, self.memo)


class FibMemoDisc(FibMemo):
    def __init__(self, memo: List[int] = None, filename: str = 'fib_memo.json'):
        FibMemo.__init__(self, memo)

        self.filename = filename
        self.loaded = False
        self.memo_size = len(self.memo)

    def clear(self):
        self.memo = default_memo()
        with open(self.filename, 'w') as f:
            json.dump(self.memo, f)
        print(f"{self.filename}({self.memo_size - 1}) cleared")
        self.memo_size = len(self.memo)

    def load(self):
        if not self.loaded:
            if not os.path.exists(self.filename):
                with open(self.filename, 'w') as f:
                    json.dump(self.memo, f)
                print(f"created {self.filename}({len(self.memo) - 1})")
            else:
                with open('fib_memo.json', 'r') as f:
                    memo = json.load(f)
                self.memo = memo
                print(f"loaded {self.filename}({len(self.memo) - 1})")

            self.memo_size = len(self.memo)
            self.loaded = True

    def save(self):
        self.load()
        if len(self.memo) > self.memo_size:
            with open(self.filename, 'w') as f:
                json.dump(self.memo, f)
            self.memo_size = len(self.memo)
            print(f"{self.filename}({self.memo_size - 1}) updated")
        else:
            print(f"{self.filename}({self.memo_size - 1}) up to date")


if __name__ == "__main__":
    f = FibMemoDisc()
    f.load()
    print(f(1))
    print(f(11))
    print(f(112))
    print(f(33))
    print(f(5))
    f.save()
    print(f(112))
    f.clear()
