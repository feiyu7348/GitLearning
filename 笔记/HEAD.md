
# HEAD

## HEAD 的本质

- HEAD 是一个指针，指向当前分支的最新提交（或特定的某个提交）
- 它存储在 .git/HEAD 文件中，内容通常是：

```bash
ref: refs/heads/<当前分支名>  # 例如：ref: refs/heads/main
```

## 常见表示形式

| 表达式         | 含义                                   | 示例                     |
|----------------|----------------------------------------|--------------------------|
| `HEAD`         | 当前提交（最新提交）                   | `git show HEAD`          |
| `HEAD~` 或 `HEAD~1` | 上一个提交（父提交）              | `git diff HEAD~1`        |
| `HEAD^`        | 同上，但更常用于合并提交的父提交       | `git checkout HEAD^`     |
| `HEAD@{n}`     | 引用 reflog 中的第 n 个记录            | `git reset HEAD@{1}`     |

补充：

```bash
`HEAD~n` 表示向前追溯 n 个提交（线性历史）
`HEAD^n` 用于合并提交时选择第 n 个父提交（从1开始）
`HEAD@{\"2 days ago\"}` 支持时间表达式
```

## 可视化理解

```text
          HEAD (指向分支或提交)
            |
            v
main -> Commit C (最新提交)
            |
            v
         Commit B
            |
            v
         Commit A
```

当执行 git commit 时，HEAD 和分支指针一起向前移动。
