# 暂存操作

1. 使用`git stash`将当前未提交的修改(即，工作区的修改和暂存区的修改)先暂时储藏起来，这样工作区干净了后，就可以切换切换到master分支下拉一个fix分支。
2. 在完成线上bug的修复工作后，重新切换到dev分支下通过`git stash pop`命令将之前储藏的修改取出来，继续进行新功能的开发工作.

```shell
# 储藏工作区的修改和暂存区的修改到储藏记录列表中
git stash save [stashMessage]

# 查看储藏记录列表
git stash list

# 取出指定index的储藏的修改到工作区中
git stash apply stash@{index}

# 将指定index的储藏从储藏记录列表中删除
git stash drop stash@{index}

#可取出最近一次储藏的修改到工作区中，并同时将该储藏从储藏记录列表中删除
git stash pop

#查看指定stash的diff
git stash show -p stash@{index}

#从stash创建分支
git stash branch [branchName] stash@{index}
```
