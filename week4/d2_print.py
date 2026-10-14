# 补充演示：print 括号里到底能不能计算？（d2_print.py）
# 结论：能算！而且各种算式、函数都能放进去。
# 运行：python d2_print.py

print("=" * 46)
print("一、括号里直接写算式 —— 会算出结果再显示")
print("=" * 46)
print(3 + 1)
print(10 * 5)
print(100 / 4)
print(2 ** 8)

print()
print("=" * 46)
print("二、算式和文字混在一起（用逗号隔开）")
print("=" * 46)
print("3 + 1 =", 3 + 1)
print("平均分是", (80 + 90) / 2)
print("及格线是", 60, "，我考了", 85, "，高出", 85 - 60, "分")

print()
print("=" * 46)
print("三、括号里也能放别的有返回值的函数")
print("=" * 46)
print(len("hello"))            # len 有返回值 → print 拿到 5
print(max([7, 3, 9]))          # max 有返回值 → print 拿到 9
print("hello".upper())         # upper 有返回值 → print 拿到 HELLO

print()
print("=" * 46)
print("四、最关键的一组对比")
print("=" * 46)

print("--- 演示 A：print(print(3 + 1)) 会发生什么 ---")
print(print(3 + 1))
print("   ↑ 先看到 4，再看到 None")

print()
print("--- 演示 B：想让结果以后还能用，必须先赋值 ---")
total = 88 + 92 + 75
print("总分：", total)
print("平均分：", total / 3)
print("   ↑ total 存下来了，所以能二次利用")

print()
print("--- 演示 C：如果只用 print 不赋值，结果就留不住 ---")
print(88 + 92 + 75)
print("   屏幕上看到了 255，但 255 没存在任何地方")
print("   下面这行如果写 print(255 / 3) 能行，因为 255 是我手写的")
print("   但如果想写 print(total2 / 3) 就会 NameError —— 因为没那个变量")

print()
print("=" * 46)
print("五、一句话结论")
print("=" * 46)
print("括号里 '算不算' 和 print '留不留' 是两回事：")
print("  · 括号里的东西         → 一定会被计算")
print("  · print 自己给出的值   → 永远是 None（留不住）")

print()
print("=" * 46)
print("六、'print 有两条通道' —— 彻底搞懂 None 从哪来")
print("=" * 46)
print("把 print 想成有两根管子：")
print("  ① 输出通道 → 通向屏幕，负责显示内容")
print("  ② 返回通道 → 通向赋值，交出的永远是 None")
print()

scores = [88, 92, 75, 96, 61]

print("--- 写法 A：print(max(scores)) ---")
print(max(scores))
print("    ↑ 96 走了①输出通道到屏幕；②返回通道的 None 没人接，被丢掉了")
print()

print("--- 写法 B：x = max(scores) 再 print(x) ---")
best = max(scores)
print(best)
print("    ↑ max 把 96 交给 best 存着，再打印 best。完全正常")
print()

print("--- 写法 C：y = print(max(scores)) ← 出问题的写法 ---")
y = print(max(scores))
print("    ↑ 屏幕上照样显示 96（①通道正常）")
print("     但 ②通道的 None 这次被 y 接住了 → y =", y)
print()

print("★ 所以：出问题不是因为 'max 没有变量承载'，")
print("  而是因为 '把 print 塞进了赋值语句'。")
print("   max(scores) 本身完全正常 —— 写法 A 已经证明了。")

print()
print("--- 三种写法怎么选 ---")
print("  只想看一眼  → print(max(scores))")
print("  要留着以后用 → x = max(scores)  然后  print(x)")
print("  千万别写    → x = print(...)")

