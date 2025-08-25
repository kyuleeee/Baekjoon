from  collections import deque

def solution(priorities, location):
    queue = deque(range(len(priorities)))
    result = []
    
    while queue:
        q = queue.popleft()
        if priorities[q] == max(priorities):
            result.append(q)
            priorities[q] = -1   # 출력된 문서 표시
        else:
            queue.append(q)
    
    return result.index(location) + 1