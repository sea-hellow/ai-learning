# 任务 1：成绩单管理器（列表基础）
# 要求：
#   1. 建一个列表 scores，放 5 个成绩：[88, 92, 75, 96, 61]
#   2. 打印整个列表
#   3. 打印列表长度（用 len）
#   4. 打印第 1 个（下标 0）和最后 1 个成绩（用 -1）
#   5. 用 append 添加一个 85 分进去，再打印一次列表
# 运行：python task1_list.py

scores = [88, 92, 75, 96, 61]

# 从下面开始写
print(scores)
print(len(scores))
print(scores[0])
print(scores[-1])
scores.append(85)
print(scores)