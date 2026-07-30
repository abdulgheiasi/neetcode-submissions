class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        max_freq = max(counts.values())
        max_count = sum(1 for count in counts.values() if count == max_freq)

        intervals = (max_freq - 1) * (n + 1) + max_count

        return max(len(tasks), intervals)