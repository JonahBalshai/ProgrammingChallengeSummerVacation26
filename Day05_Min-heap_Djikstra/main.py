import pdb

class MinHeap:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)
        index = len(self.values) - 1
        while index > 0 and self.values[(index-1)//2][0] > self.values[index][0]:
            self.values[index], self.values[(index-1)//2] = self.values[(index-1)//2], self.values[index]
            index = (index - 1) // 2

    def pop(self):
        # Swap min value and last element
        self.values[0], self.values[len(self.values) - 1] = self.values[len(self.values) - 1], self.values[0]
        last_value = self.values[0][0]
        node = self.values.pop()[1]


        # Sift down
        index = 0
        while (2*index+1) < len(self.values):

            index_offset = 0
            if self.values[(2*index)+1][0] < last_value:
                index_offset += 1
            if (2*index+2) < len(self.values) and self.values[(2*index)+2][0] < last_value:
                index_offset += 2

            if index_offset == 3:
                if self.values[(2*index)+1][0] < self.values[(2*index)+2][0]:
                    index_offset = 1
                else:
                    index_offset = 2
            elif index_offset == 0:
                break

            self.values[(2*index)+index_offset], self.values[index] = self.values[index], self.values[(2*index)+index_offset]
            index = (2*index)+index_offset
                                
        return node

def main():
    graph = {
        0: {1: 4, 2: 2},
        1: {0: 4, 2: 6, 4: 8},
        2: {0: 2, 1: 6, 3: 2},
        3: {2: 2, 4: 1},
        4: {1: 8, 3: 1}
    }
 
    heap = MinHeap()
    
    # build a graph
    distances = {node : float('inf') for node in graph}
    distances[0] = 0

    heap.push((0, 0))

    while heap.values != []:
        node = heap.pop()

        for adj, dist in graph[node].items():
            alternative_dist = distances[node] + dist
        
            if alternative_dist < distances[adj]:
                distances[adj] = alternative_dist

                heap.push((alternative_dist, adj))

    print(distances)


if __name__ == "__main__":
    main()