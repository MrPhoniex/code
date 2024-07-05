def check(strings):
    # 创建一个空列表，用于存储处理后的结果
    results = []

    # 遍历输入的每个字符串
    for s in strings:
        # 初始化一个空栈，用于跟踪左括号的位置
        stack = []
        # 创建一个与字符串长度相同的列表，用空格填充，表示注释位置
        annotations = [' ' for _ in range(len(s))]

        # 遍历字符串中的每个字符
        for i, char in enumerate(s):
            # 如果字符是左括号，将其索引压入栈中
            if char == '(':
                stack.append(i)
            elif char == ')':
                # 如果字符是右括号且栈不为空，从栈中弹出一个左括号的索引
                if stack:
                    stack.pop()
                # 如果栈为空，说明没有匹配的左括号，在当前位置标注问号
                else:
                    annotations[i] = '?'

        # 遍历完字符串后，栈中剩余的左括号位置标注为x
        while stack:
            annotations[stack.pop()] = 'x'

        result = ''.join(annotations)
        results.append(s)
        results.append(result)

    return results


# 样例输入
input_strings = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

# 输出结果
output = check(input_strings)
for line in output:
    print(line)
