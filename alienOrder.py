from collections import defaultdict, deque

def alienOrder(words):
    adj = defaultdict(set)
    indegree = {c:0 for w in words for c in w}
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in adj[c1]:
                    adj[c1].add(c2)
                    indegree[c2] += 1
                break

    q = deque([c for c in indegree if indegree[c]==0])
    res = ""
    while q:
        c = q.popleft()
        res += c
        for nei in adj[c]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    return res if len(res)==len(indegree) else ""
