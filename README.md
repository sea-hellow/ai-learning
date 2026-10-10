# ai-learning

AI 学习路线（阶段 0–5）的代码、笔记与实践记录。

## 学习进度

| 阶段 | 内容 | 周次 | 状态 |
|---|---|---|---|
| 0 | 工具与环境 | 周 1–2 | ✅ 已完成 |
| 1 | Python 编程基础 | 周 3–12 | 🔄 进行中（第 4 周完成） |
| 2 | 数学基础（并行轨道） | 周 9–24 | 未开始 |
| 3 | 机器学习 | 周 13–22 | 未开始 |
| 4 | 深度学习 | 周 23–32 | 未开始 |
| 5 | 方向深入（CV 线） | 周 33–44 | 未开始 |

## 环境

- Python 3.12.15（conda 环境 `ai-learn`，位于 `D:\conda\envs\ai-learn`）
- numpy / pandas / matplotlib / scikit-learn / jupyter / ipykernel
- 编辑器：VS Code（已装 Python + Jupyter 扩展，解释器指向 `ai-learn`）
- 每周节奏：工作日 1–1.5 小时，周末一次 2–3 小时
- 详细的环境说明与踩坑记录见 [docs/环境备忘.md](docs/环境备忘.md)

## 目录说明

```
ai-learning/
├── README.md
├── .gitignore
├── docs/
│   └── 环境备忘.md       # 环境配置、镜像源、代理等运维记录
├── week1_test.ipynb      # 阶段 0 环境验证
├── week3/                # 第 3 周：Python 基础语法
│   ├── hello.py          # 第一个程序
│   ├── task1_me.py       # 练习 1：自我介绍卡（变量 + f-string）
│   ├── task2_text.py     # 练习 2：字符串方法
│   └── task3_time.py     # 练习 3：时间换算（// 与 %）
└── week4/                # 第 4 周：列表 + 条件判断 + for 循环
    ├── d1_list.py        # 列表操作演示
    ├── task1_list.py     # 练习 1：列表基础（下标 / len / append）
    ├── task2_grade.py    # 练习 2：if-elif-else 成绩评级
    └── task3_stats.py    # 练习 3：列表 + for + if 综合统计
```

## 每周工作流程

1. 写代码、做练习（工作日每天 1–1.5 小时）
2. 周末复盘，把本周成果整理进仓库
3. 提交并推送：

```bash
git status                         # 看有哪些改动
git add -A                         # 暂存全部改动
git commit -m "第 N 周：做了什么"    # 提交
git push                           # 推送到 GitHub
```

## 学习日志

### 第 4 周（2026-10-10）

**主题**：列表（list）+ 布尔值 + 条件判断（if/elif/else）+ for 循环

**掌握的内容**：
- 列表的创建、下标取值（正向 `0` 起、反向 `-1` 末尾）、`len`/`sum`/`max`/`min`、`append`、按下标修改
- 布尔值与比较运算（`>` `<` `>=` `<=` `==` `!=`），以及 `and` / `or` / `not`
- `if` / `elif` / `else` 多分支；**elif 命中即结束**，所以条件只需从严格到宽松排列，不必写重复范围
- `for` 循环遍历列表；**累加器模式**（循环外初始化、循环内更新）
- 循环内套 `if` 做条件统计

**完成三个练习**：
- `task1_list.py` —— 列表基础操作（打印、长度、首尾元素、append）
- `task2_grade.py` —— if-elif-else 四档成绩评级（已用 95/89/75/74/60/59 等边界值验证）
- `task3_stats.py` —— 用两种写法实现统计：① `sum`/`max` 直接算 ② for 循环 + 累加器 ③ 循环内 if 统计不及格

---

#### 本周犯的错与改正（记录）

**错误 1：`print` 的返回值问题**
- 最初写成 `highest = print(max(scores))`，导致输出 `最高分:None`
- **原因**：`print()` 只负责显示，**不产生返回值**（返回 `None`）。`max(scores)` 才有返回值
- **改正**：`highest = max(scores)` 后再 `print(f"最高分:{highest}")`
- **规律**：`print` 和 `=` 赋值不要写在一起 —— 要值就只写 `变量 = xxx`，要显示就只写 `print(xxx)`

**错误 2：task1 漏了最后一步**
- `scores.append(85)` 写了，但没再打印，看不到追加结果
- **改正**：补上 `print(scores)` → 输出 `[88, 92, 75, 96, 61, 85]`

**错误 3：task2 只验证了 1 个分数**
- 只跑 `score = 30` 输出"不及格"，测不出**分支顺序**类错误
- **改正**：用 95 / 89 / 80 / 75 / 74 / 65 / 60 / 59 / 30 多档跑一遍，确认边界都对

**错误 4：变量名用了内置名**
- 写了 `file = 0` 做计数器。`file` 是 Python 内置类型名，会与后来的文件操作冲突
- **改正**：改名为 `fail`

**其他改进**：
- 删掉了多余的 `else: pass`（Python 默认就什么都不做，不需要显式写）
- 统一冒号为半角 `:`（原来 `平均分：` 用了全角，输出与其他行不一致）

---

**本周测验（第 3 周测评考卷）成绩：84 / 100**
- 错第 7 题（字符串方法不改变原串，需 `s = s.upper()` 才生效）
- 错第 9 题（`NameError` 的三种归因：拼错 / 未定义 / 大小写不符；中文标点属于 `SyntaxError` 不是 `NameError`）
- 两题已针对性复盘，概念已澄清

### 第 3 周（2026-10-08）

- 环境与目录对不上导致首次运行失败：在 `C:\Users\21618` 且处于 `(base)` 环境跑 `python hello.py`
- 学会用 `conda activate ai-learn` 切换环境、`cd /d` 切换目录
- 跑通第一个程序 `hello.py`（print / 字符串 / 数字运算）
- 掌握：变量赋值、f-string 格式化、字符串方法（`strip`/`upper`/`lower`/`len`）、整除 `//`、取余 `%`
- 完成三个练习，全部通过：
  - `task1_me.py` —— 用 4 个变量 + f-string 输出自我介绍
  - `task2_text.py` —— 对字符串做去空白、大小写转换、长度统计
  - `task3_time.py` —— 用 `//` 和 `%` 把 10000 秒换算成 2 小时 46 分 40 秒

**踩到的坑**：
- 中文标点（`“”` `（）` `，`）在代码里会导致 `SyntaxError`，输入法要保持在英文状态
- `LF will be replaced by CRLF` 是提示不是错误，Windows 下正常现象
- PowerShell 与 CMD 语法不同：切目录 PowerShell 用 `cd D:\path`，CMD 用 `cd /d D:\path`

### 第 2 周（2026-10-07）

- 配置 Git 全局身份（用户名 + GitHub 隐私邮箱）
- 初始化仓库、编写 `.gitignore`（排除数据集、模型权重与缓存）
- 完成两次提交并成功推送到 GitHub
- 打通 GitHub 网络访问（git 需单独配置代理，详见环境备忘）

**踩到的坑**：git 默认不使用 Windows 系统代理；且凭据管理器不支持 `socks5://` 方案，必须用 `http://`。

### 第 1 周（2026-10-07）

- 装好 Miniconda，创建 `ai-learn` 环境（Python 3.12.15）
- 装齐 numpy / pandas / matplotlib / scikit-learn / jupyter
- VS Code 配置完成，解释器指向 ai-learn
- 跑通 `week1_test.ipynb`，五个单元格全部通过

**踩到的坑**：pip 装包时被本机安全策略拦截（清缓存动作被当成批量删除），加 `--no-cache-dir` 解决。
