# ai-learning

AI 学习路线（阶段 0–5）的代码、笔记与实践记录。

## 学习进度

| 阶段 | 内容 | 周次 | 状态 |
|---|---|---|---|
| 0 | 工具与环境 | 周 1–2 | 进行中 |
| 1 | Python 编程基础 | 周 3–12 | 未开始 |
| 2 | 数学基础（并行轨道） | 周 9–24 | 未开始 |
| 3 | 机器学习 | 周 13–22 | 未开始 |
| 4 | 深度学习 | 周 23–32 | 未开始 |
| 5 | 方向深入（CV 线） | 周 33–44 | 未开始 |

## 环境

- Python 3.12.15（conda 环境 `ai-learn`，位于 `D:\conda\envs\ai-learn`）
- numpy / pandas / matplotlib / scikit-learn / jupyter
- 每周节奏：工作日 1–1.5 小时，周末一次 2–3 小时

## 目录说明

```
ai-learning/
├── week1_test.ipynb     # 阶段 0 环境验证
├── .gitignore
└── README.md
```

## 学习日志

### 第 1 周（2026-10-07）

- 装好 Miniconda，创建 `ai-learn` 环境（Python 3.12.15）
- 装齐 numpy / pandas / matplotlib / scikit-learn / jupyter
- VS Code 配置完成，解释器指向 ai-learn
- 跑通 `week1_test.ipynb`，五个单元格全部通过

**踩到的坑**：pip 装包时被本机安全策略拦截（清缓存动作被当成批量删除），加 `--no-cache-dir` 解决。
