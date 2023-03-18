# 如何通过本地命令行同步更新？

1. 验证远程分支可以 fetch 或 push
   `git remote -v`

2. 指明我们需要同步的仓库
   `git remote add upstream 原仓库地址`

3. 验证
   `git remote -v`

4. 拉取更新的 branches 和 commits

   `git fetch upstream`

5. Checkout 本地分支
   `git checkout master`

6. 合并

   `git merge upstream/master`

7. 提交

   `git push origin master`

## 链接地址

- [csdn](https://blog.csdn.net/wuzhongqiang/article/details/103227170)
- [知乎](https://zhuanlan.zhihu.com/p/51844239)
- [开源项目](https://github.com/firstcontributions/first-contributions)
   测试fork和pull requests
