# 复习 · 变体练习 6／6：成绩单统计（for 循环 + if 综合）
# ------------------------------------------------------------------
# 这是第 4 周 task3 的升级版。难度提高了两点：
#   ① 统计维度从 3 个变成 5 个
#   ② ★ 不许用 sum() 和 max() ★ —— 必须用循环自己算出来
#      （这是为了强制你练熟"累加器模式"，也就是第 1 轮串讲第 7.5 节）
#
# 要求：只用 for 循环 + 累加器，算出并输出下面 5 项
#
#   总分: 598
#   平均分: 74.75
#   最高分: 95
#   及格人数: 6
#   优秀人数: 2
#
# 提示（5 个容器，全部要在循环外面准备好）：
#   total      = 0            # 累加总分
#   highest    = scores[0]    # 先假设第一个是最高分
#   pass_count = 0            # 及格（>=60）计数
#   good_count = 0            # 优秀（>=90）计数
#
#   for s in scores:
#       total = total + s              # 累加
#       if s > highest:                # 刷新最高分
#           highest = s
#       if s >= 60:                    # 及格计数
#           pass_count = pass_count + 1
#       if s >= 90:                    # 优秀计数
#           good_count = good_count + 1
#
#   平均分 = total / len(scores)
#
# ★ 重点：这 4 个容器必须写在 for 外面！
#   如果写进去，每一轮都会被清零，结果一定错。（第 1 轮串讲第 7.5 节的坑）
#
# 运行：python v6_report.py
# ------------------------------------------------------------------

scores = [72, 95, 58, 88, 91, 64, 47, 83]
total      = 0
highest    = scores[0]
pass_count = 0
good_count = 0
for s in scores:
    total=total+s
    if s>highest:
        highest=s
    if s>=60:
        pass_count=pass_count+1
    if s>=90:
        good_count=good_count+1
print(total)
print(total/len(scores))
print(highest)
print(pass_count)
print(good_count)

# 从下面开始写
