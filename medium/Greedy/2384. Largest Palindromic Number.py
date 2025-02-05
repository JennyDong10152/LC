class Solution:
    def largestPalindromic(self, num: str) -> str:

        answer = []
        collect = [str(x) for x in range(9, -1, -1)]
        record = defaultdict(int)

        for x in num:
            record[x] += 1

        for x in collect:
            n = len(answer)
            if n % 2 == 0:
                if record[x] > 0:
                    answer = answer[:n // 2] + [x] * record[x] + answer[n // 2:]
            else:
                if x == '0':
                    if len(answer) != 1:
                        answer = answer[:n // 2] + [x] * (record[x] // 2) + [answer[n // 2]] + [x] * (record[x] // 2) + answer[n // 2 + 1:]
                else:
                    if record[x] >= 2:
                        answer = answer[:n // 2] + [x] * (record[x] // 2) + [answer[n // 2]] + [x] * (record[x] // 2) + answer[n // 2 + 1:]

        answer = "".join(answer)

        while True:
            if len(answer) > 1 and answer[0] == '0':
                answer = answer[1:]
            else:
                break
        return answer