import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heap)
  print(heapq.heappop(heap)[1])#맥힙팝은 인덱스 두개 반환인듯
