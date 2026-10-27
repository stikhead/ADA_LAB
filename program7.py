import heapq
from typing import List

class ShortestPath:
    def __init__(self, vertices: int):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]
        self.edges = []

    def add_edge(self, u: int, v: int, weight: int):
        self.adj[u].append((v, weight))
        self.edges.append((u, v, weight))

    def dijkstra(self, src: int) -> List[float]:
        dist = [float('inf')] * self.V
        dist[src] = 0
        pq = [(0, src)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            if current_dist > dist[u]:
                continue
                
            for v, weight in self.adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
                    
        return dist

    def bellman_ford(self, src: int) -> List[float]:
        dist = [float('inf')] * self.V
        dist[src] = 0
        
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    
        for u, v, weight in self.edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                print("Error: Graph contains a negative-weight cycle.")
                return [] 
                
        return dist


if __name__ == "__main__":
    print("--- ShortestPath Tests ---")
    sp = ShortestPath(5)
    sp.add_edge(0, 1, 4)
    sp.add_edge(0, 2, 1)
    sp.add_edge(2, 1, 2)
    sp.add_edge(1, 3, 1)
    sp.add_edge(2, 3, 5)
    sp.add_edge(3, 4, 3)

    print("Dijkstra distances from node 0:", sp.dijkstra(0))
    print("Bellman-Ford distances from node 0:", sp.bellman_ford(0))

    print("\nTesting negative cycle detection:")
    sp_neg = ShortestPath(3)
    sp_neg.add_edge(0, 1, 1)
    sp_neg.add_edge(1, 2, -1)
    sp_neg.add_edge(2, 0, -1) 
    
    result = sp_neg.bellman_ford(0)
    print("Bellman-Ford result:", result)