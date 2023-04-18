class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_list = []

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                fizz_list.append("FizzBuzz")
            elif i % 3 == 0:
                fizz_list.append("Fizz")
            elif i % 5 == 0:
                fizz_list.append("Buzz")
            else:
                fizz_list.append(f"{i}")

        return fizz_list