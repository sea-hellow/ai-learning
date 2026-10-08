# 任务 2：文字处理小工具
# 要求：对字符串 "   Hello Python   " 做以下操作并分别打印
#   1. 去掉两端空格后原样输出
#   2. 全大写
#   3. 全小写
#   4. 统计去掉空格后的字符个数（用 len）
# 运行：python task2_text.py

s = "   Hello Python   "

# 从下面开始写
print(s.strip())
print(s.upper())
print(s.lower())
print(len(s.strip()))