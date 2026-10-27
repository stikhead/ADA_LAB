import heapq
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Edge:
    u: int
    v: int
    weight: int

    def __repr__(self):
        return f"Edge({self.u} - {self.v}, w:{self.weight})"

class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.edges: List[Edge] = []
        self.adj: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(vertices)}

    def add_edge(self, u: int, v: int, weight: int):
        self.edges.append(Edge(u, v, weight))
        self.adj[u].append((weight, v))
        self.adj[v].append((weight, u))

    def kruskal_mst(self) -> List[Edge]:
        mst: List[Edge] = []
        parent = list(range(self.V))
        rank = [0] * self.V

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) 
            return parent[i]

        def union(i: int, j: int) -> bool:
            root_i = find(i)
            root_j = find(j)
            
            if root_i != root_j:
                if rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                elif rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1
                return True
            return False

        sorted_edges = sorted(self.edges, key=lambda e: e.weight)
        
        for edge in sorted_edges:
            if union(edge.u, edge.v):
                mst.append(edge)
                if len(mst) == self.V - 1:
                    break
                    
        return mst

    def prim_mst(self) -> List[Edge]:
        mst: List[Edge] = []
        if self.V == 0:
            return mst
            
        visited = [False] * self.V
        min_heap: List[Tuple[int, int, int]] = [] 
        
        visited[0] = True
        for weight, v in self.adj[0]:
            heapq.heappush(min_heap, (weight, 0, v))
            
        while min_heap and len(mst) < self.V - 1:
            weight, u, v = heapq.heappop(min_heap)
            
            if visited[v]:
                continue
                
            visited[v] = True
            mst.append(Edge(u, v, weight))
            
            for next_weight, next_v in self.adj[v]:
                if not visited[next_v]:
                    heapq.heappush(min_heap, (next_weight, v, next_v))
                    
        return mst

if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    print("Kruskal's MST:", g.kruskal_mst())
    print("Prim's MST:   ", g.prim_mst())