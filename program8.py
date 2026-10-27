import heapq
from typing import Dict, Optional

class Node:
    def __init__(self, char: Optional[str], freq: int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other: 'Node') -> bool:
        return self.freq < other.freq

class HuffmanCoder:
    def __init__(self):
        self.root = None
        self.codes = {}

    def build_tree(self, frequencies: Dict[str, int]) -> Optional[Node]:
        if not frequencies:
            return None

        heap = []
        for char, freq in frequencies.items():
            heapq.heappush(heap, Node(char, freq))

        if len(heap) == 1:
            node = heapq.heappop(heap)
            root = Node(None, node.freq)
            root.left = node
            self.root = root
            return root

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            
            heapq.heappush(heap, merged)

        self.root = heapq.heappop(heap)
        return self.root

    def generate_codes(self) -> Dict[str, str]:
        self.codes = {}
        if not self.root:
            return self.codes

        def dfs(node: Node, current_code: str):
            if node is None:
                return
            
            if node.char is not None:
                self.codes[node.char] = current_code
                return
            
            dfs(node.left, current_code + "0")
            dfs(node.right, current_code + "1")

        dfs(self.root, "")
        return self.codes


if __name__ == "__main__":
    print("--- HuffmanCoder Tests ---")
    frequencies = {
        'a': 5,
        'b': 9,
        'c': 12,
        'd': 13,
        'e': 16,
        'f': 45
    }
    
    print("Input Frequencies:", frequencies)
    
    coder = HuffmanCoder()
    coder.build_tree(frequencies)
    codes = coder.generate_codes()
    
    print("\nGenerated Huffman Codes:")
    for char in sorted(codes.keys()):
        print(f"'{char}': {codes[char]}")