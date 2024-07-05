def shortest_way(source, target):
    min_count = 0
    idx = 0

    while idx < len(target):
        next_idx = greedy_find(source, target, idx)
        if next_idx == -1:
            return -1
        else:
            min_count += 1
            idx = next_idx

    return min_count


def greedy_find(source, target, target_idx):
    source_idx = 0
    cache = target_idx  # 缓存 target_idx

    while source_idx < len(source) and target_idx < len(target):
        if source[source_idx] == target[target_idx]:
            target_idx += 1
        source_idx += 1

    if target_idx == cache:
        # 一个字符都没匹配上
        return -1

    return target_idx


# 测试示例
print(shortest_way("abc", "abcbc"))
print(shortest_way("abc", "acdbc"))
print(shortest_way("xyz", "xzyxz"))
