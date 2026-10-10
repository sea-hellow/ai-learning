# 第 4 周 · 列表操作演示（d1_list.py）
# 作用：把手册第 2 节「列表」的所有操作跑一遍，眼见为实
# 运行：python d1_list.py

scores = [88, 92, 75, 96, 61]
print("列表本身:", scores)
print()

print("--- 1. 下标取元素 ---")
print("scores[0]  第1个 :", scores[0])
print("scores[1]  第2个 :", scores[1])
print("scores[2]  第3个 :", scores[2])
print("scores[-1] 最后1个:", scores[-1])
print("scores[-2] 倒2个 :", scores[-2])
print()

print("--- 2. 通用工具（写在括号里） ---")
print("len 元素个数:", len(scores))
print("max 最大值 :", max(scores))
print("min 最小值 :", min(scores))
print("sum 总和   :", sum(scores))
print()

print("--- 3. append 往末尾加一个 ---")
print("加之前:", scores)
scores.append(100)
print("加之后:", scores)
print("现在个数:", len(scores))
print()

print("--- 4. 改某个元素 ---")
print("改之前:", scores)
scores[0] = 90
print("改之后:", scores)
print()

print("--- 5. 对比：字符串方法 vs 列表方法 ---")
s = "  hi  "
s.strip()                 # 没有赋值
print("没赋值，s 还是:", repr(s))
s2 = s.strip()            # 有赋值
print("有赋值，s2 变成:", repr(s2))
print()
nums = [1, 2]
nums.append(3)            # 不需要赋值
print("append 不需要赋值，nums 直接变成:", nums)
