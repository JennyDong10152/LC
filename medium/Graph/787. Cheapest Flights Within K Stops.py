class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        cheapest = [float("inf")] * n
        cheapest[src] = 0

        for start, end, weight in flights:
            graph[start].append((end, weight))
        
        queue = deque([(src, 0)])
        
        while k>=0 and queue:
            size = len(queue)
            for _ in range(size):
                current, current_price = queue.popleft()
                for neighbor, price in graph[current]:
                    new_price = current_price + price
                    if new_price < cheapest[neighbor]:
                        cheapest[neighbor] = new_price
                        queue.append((neighbor, new_price))
            k -= 1
        return cheapest[dst] if cheapest[dst] != float("inf") else -1