# commit详解

> <https://blog.csdn.net/qq_40994734/article/details/128694274>

```shell
# 将暂存区内容提交到版本库, 进入 vi 命令界面输入提交信息
git commit

# 将某些已被跟踪的文件提交到版本库（包含工作区和版本库）
git commit [file1] [file2] [...]

# 将暂存区内容提交到版本库, 无需进入 vi 命令界面输入提交信息
git commit -m [message]

# 跳过 git add, 将所有已被跟踪的文件更改提交到版本库
git commit -am [message]

# 使用一次新的commit, 替代上一次提交
# 如果代码没有任何新变化, 则用来改写上一次commit的提交信息
git commit --amend -m [message]
```
