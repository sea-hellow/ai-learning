# 任务 2：成绩评级器（if / elif / else）
# 要求：
#   给定一个分数 score，按下面的规则打印等级
#     90 分及以上  -> 优秀
#     75 ~ 89      -> 良好
#     60 ~ 74      -> 及格
#     60 分以下    -> 不及格
#   提示：
#     - 用 if / elif / else
#     - 判断"90 分及以上"写：if score >= 90:
#     - 注意每一层下面要缩进 4 个空格
# 验收：把 score 改成 95 / 80 / 65 / 30 各跑一次，看四个结果对不对
# 运行：python task2_grade.py

score = 30

# 从下面开始写
if score>=90:
    print("优秀")
elif score>=75:
    print("良好")
elif score>=60:
    print("及格")
else:
    print("不及格")