class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        visited = set()
        current_nodes = []
        step = 0
        
        if target in deadends or '0000' in deadends:
            return -1
        else:
            current_nodes.append("0000")
            visited.add("0000")
        
        while current_nodes:
            step += 1
            size = len(current_nodes)
            
            for i in range(size):
                node = current_nodes.pop(0)
                
                for j in range(4):
                    for k in [-1, 1]:
                        next_node = node[:j] + str((int(node[j]) + k) % 10) + node[j+1:]

                        if next_node == target:
                            return step
                        if next_node in deadends or next_node in visited:
                            continue
                        
                        visited.add(next_node)
                        current_nodes.append(next_node)
        
        return -1
                        
                