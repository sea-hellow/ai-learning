# 任务 3：时间换算器
# 要求：把 10000 秒换算成「几小时几分几秒」并输出
# 正确答案：2 小时 46 分 40 秒
# 运行：python task3_time.py
# 提示：参考手册第 5 节的秒数换算写法，用 // 和 %
#   h = total // 3600
#   m = (total % 3600) // 60
#   s = total % 60

total = 10000

# 从下面开始写
hour=total//3600
minute=(total%3600)//60
second=total%60
print(f"{hour}小时{minute}分{second}秒")
