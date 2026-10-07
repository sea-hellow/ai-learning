# ai-learning

AI 学习路线（阶段 0–5）的代码、笔记与实践记录。

## 学习进度

| 阶段 | 内容 | 周次 | 状态 |
|---|---|---|---|
| 0 | 工具与环境 | 周 1–2 | ✅ 已完成 |
| 1 | Python 编程基础 | 周 3–12 | ⏳ 即将开始 |
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
└── week1_test.ipynb      # 阶段 0 环境验证
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
