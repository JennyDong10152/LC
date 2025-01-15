class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = [0] * 26
        for task in tasks:
            frequency[ord(task) - ord('A')] += 1
        frequency.sort()
        chunk = frequency[25] - 1
        idle = chunk * n
        for idx in range(24, -1, -1):
            idle -= min(chunk, frequency[idx])
        return len(tasks) + idle if idle >= 0 else len(tasks)