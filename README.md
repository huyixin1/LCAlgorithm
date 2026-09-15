# LeetCode 刷题仓库（LCAlgorithm）

**第一轮已归档，开启第二轮刷题**

## 目录结构

```
LCAlgorithm/
├── README.md          # 本文件（仓库说明）
├── 1round/            # 第一轮刷题（Round 1，已归档）
│   ├── README.md      # 第一轮题目总表（类型 | 题目 | 完成时间 | LeetCode 链接）
│   ├── solutions/     # 第一轮题解代码（13 个主题分类：Array/Binary Tree/Dynamic/...）
│   └── <题号>-<题名>/ # LeetSync 自动生成的题号文件夹（101-symmetric-tree 等）
├── notes-2round/      # 第二轮刷题笔记
│   ├── 刷题计划.md
│   ├── 错题集.md
│   └── 学习笔记.md
└── push.ps1           # 一键推送脚本
```

## 工作流

1. **代码**：Chrome 装 LeetSync 插件 → 授权 GitHub → LeetCode 提交通过后自动 push 到本仓库（按题号建文件夹）
2. **笔记**：每天把笔记放进 `notes-2round/` → 双击 `push.ps1` 一键提交推送

## 一次性设置

1. GitHub 新建空仓库（如 `LCAlgorithm`，不要勾选 README）
2. 本目录执行 `git init` + `git remote add origin <你的仓库地址>`（见下方命令）
3. Chrome 安装 LeetSync 扩展并登录授权
4. 首次推送后，把本仓库设为 LeetSync 的目标仓库

## 常用命令

```powershell
# 首次：关联远程仓库
git init
git remote add origin https://github.com/huyixin1/LCAlgorithm.git

# 以后：一键推送（或双击 push.ps1）
.\push.ps1
```
