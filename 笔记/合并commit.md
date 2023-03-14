# 使用reset

- git reset --soft 788df125f8641774ec4852d729672cf6173dbab9 这个commitID是你想合并的所有commit之前那个commitID

- git add -u
- git commit -m "需要重新写commit的注释"
- git push --force 已提交到远程需要强制推送

# 使用rebase

- git rebase -i HEAD~3  
  合并三个commit

- pick：使用commit。

  reword：使用commit，修改commit信息。

  squash：使用commit，将commit信息合入上一个commit。

  fixup：使用commit，丢弃commit信息。

- git push --force 已提交到远程需要强制推送
