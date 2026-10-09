# ai-learning

AI 学习路线（阶段 0–5）的代码、笔记与实践记录。

## 学习进度

| 阶段 | 内容 | 周次 | 状态 |
|---|---|---|---|
| 0 | 工具与环境 | 周 1–2 | ✅ 已完成 |
| 1 | Python 编程基础 | 周 3–12 | 🔄 进行中（第 3 周完成） |
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
└── week3/                # 第 3 周：Python 基础语法
    ├── hello.py          # 第一个程序
    ├── task1_me.py       # 练习 1：自我介绍卡（变量 + f-string）
    ├── task2_text.py     # 练习 2：字符串方法
    └── task3_time.py     # 练习 3：时间换算（// 与 %）
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
