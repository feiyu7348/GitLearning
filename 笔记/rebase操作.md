# rebase

> <https://www.cnblogs.com/FraserYu/p/11192840.html>
> <https://waynerv.com/posts/git-rebase-intro/>

```bash
# 将当前分支变基到目标分支
git rebase <目标分支>
# 交互式变基（修改最近3次提交）
git rebase -i HEAD~3
# 解决冲突后继续
git add <文件>
git rebase --continue
# 跳过当前提交
git rebase --skip
# 终止rebase操作
git rebase --abort
# 设置pull默认使用rebase
git config --global pull.rebase true
# 设置自动stash未提交更改
git config --global rebase.autoStash true
```
