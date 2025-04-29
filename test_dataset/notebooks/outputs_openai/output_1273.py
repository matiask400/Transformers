def remainingNodes(nodes, parent, value):
    from collections import defaultdict
    import sys
    sys.setrecursionlimit(100000)
    
    children = defaultdict(list)
    for i in range(nodes):
        if parent[i] != -1:
            children[parent[i]].append(i)
    
    def dfs(node):
        total = value[node]
        kept = 1
        for child in children[node]:
            child_sum, child_kept = dfs(child)
            total += child_sum
            kept += child_kept
        if total == 0:
            return (0, 0)
        else:
            return (total, kept)
    
    _, count = dfs(0)
    return count

# Test cases
tests = [
    {
        'nodes':7,
        'parent':[-1,0,0,1,2,2,2],
        'value':[1,-2,4,0,-2,-1,-1],
        'output':2
    },
    {
        'nodes':7,
        'parent':[-1,0,0,1,2,2,2],
        'value':[1,-2,4,0,-2,-1,-2],
        'output':6
    },
    {
        'nodes':5,
        'parent':[-1,0,1,0,0],
        'value':[-672,441,18,728,378],
        'output':5
    },
    {
        'nodes':5,
        'parent':[-1,0,0,1,1],
        'value':[-686,-842,616,-739,-746],
        'output':5
    }
]

correct = 0
total = len(tests)
for test in tests:
    res = remainingNodes(test['nodes'], test['parent'], test['value'])
    if res == test['output']:
        print(True)
        correct +=1
    else:
        print(False)
print(f"{correct} / {total}")