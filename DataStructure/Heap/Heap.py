# Map Heap을 기준으로 구현함
class MaxHeap:
    def __init__(self):
        self.heap = []
        # 힙의 루트 인덱스를 (2)로 설정하기 위해 None을 삽입하여 힙을 초기화
        self.heap.append(None)
    
    # Heap 데이터 삽입
    def heapAdd(self, value):
        # 추가할 데이터를 배열의 마지막에 삽입
        self.heap.append(value)
        # 자식 노드의 값(추가한 노드의 값)과 부모 노드의 값을 비교하여 자식 노드가 부모 노드보다 큰 경우 swap
        # 부모 노드 인덱스: 자식 인덱스 // 2
        # 왼쪽 자식 노드 인덱스: 부모 인덱스 * 2
        # 오른쪽 자식 노드 인덱스: 부모 인덱스 * 2 + 1
        
        # 추가한 값의 인덱스 번호
        idx = len(self.heap) - 1

        # 힙 생성 이후 즉시 들어온 값에 대해서는 루트 노드 설정
        if idx <= 1:
            return True
        
        # 부모 노드와 자식 노드 값 비교 후 swap
        while idx > 1:
            parentIdx = idx // 2
            if self.heap[idx] > self.heap[parentIdx]:
                self.heap[idx], self.heap[parentIdx] = self.heap[parentIdx], self.heap[idx]
                idx = idx // 2
            else:
                break
            
        return True
    
    # 힙이 비어있는지 확인하는 유효성 검사
    def isEmpty(self):
        idx = len(self.heap) - 1
        if idx <= 0:
            return False
    
    def heapPop(self):
        # 유효성검사 함수 호출
        return False if self.isEmpty() else self.heap.pop()
    
    def getMaxValue(self):
        return False if self.isEmpty() else self.heap[1]
        

myHeap = MaxHeap()
myHeap.heapAdd(18)
myHeap.heapAdd(8)
myHeap.heapAdd(14)
myHeap.heapAdd(19)
myHeap.heapAdd(11)
print(myHeap.getMaxValue())
print(myHeap.heap)