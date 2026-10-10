# 任务 3：成绩单统计（列表 + for 循环 + if 综合）
# 要求：
#   给定成绩列表 scores，用 for 循环遍历，统计并输出：
#     1. 平均分（总分 / 个数）
#     2. 最高分
#     3. 有几个不及格（< 60）
#   提示：
#     total = 0                      # 先准备一个累加器
#     count_fail = 0                 # 再准备一个计数器
#     for s in scores:               # 逐个取出
#         total = total + s          # 累加
#         if s < 60:                 # 判断
#             count_fail = count_fail + 1
#     print("平均分:", total / len(scores))
#   最高分提示：先设 highest = scores[0]，在循环里用 if 更新它
# 运行：python task3_stats.py

scores = [88, 92, 75, 96, 61, 45, 78]

# 从下面开始写
total = sum(scores)
number = len(scores)
pinjunfen = total/number
highest = max(scores)
fail = 0
print(f"平均分：{pinjunfen}")
print(f"最高分:{highest}")
for score in scores:
    if score<60:
        fail = fail +1
print(f"不及格人数：{fail}")



total = 0
highest = scores[0]
for s in scores:
    total = total + s
    if s > highest:
        highest = s
print("平均分:", total / len(scores))
print("最高分:", highest)
