import json
import os
import fib


class FibMemo:
    def __init__(self):
        self.loaded = False
        self.memo_size = len(fib.calc)

    def clear(self):
        fib.calc = [0, 1, 1]
        with open('fib_memo.json', 'w') as f:
            json.dump(fib.calc, f)
        print(f"fib_memo({self.memo_size - 1}) cleared")
        self.memo_size = len(fib.calc)

    def load(self):
        if not self.loaded:
            if not os.path.exists('fib_memo.json'):
                with open('fib_memo.json', 'w') as f:
                    json.dump(fib.calc, f)
                print(f"created fib_memo({len(fib.calc) - 1})")
            else:
                with open('fib_memo.json', 'r') as f:
                    memo = json.load(f)
                fib.calc = memo
                print(f"loaded fib_memo({len(fib.calc) - 1})")

            self.memo_size = len(fib.calc)
            self.loaded = True

    def save(self):
        self.load()
        if len(fib.calc) > self.memo_size:
            with open('fib_memo.json', 'w') as f:
                json.dump(fib.calc, f)
            self.memo_size = len(fib.calc)
            print(f"fib_memo({self.memo_size - 1}) updated")
        else:
            print(f"fib_memo({self.memo_size - 1}) up to date")

    def __call__(self, n: int) -> int:
        res = fib.fib(n)
        self.save()
        return res


fib_memo = FibMemo()
