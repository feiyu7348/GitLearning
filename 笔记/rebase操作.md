# rebase

> <https://www.cnblogs.com/FraserYu/p/11192840.html>
> <https://waynerv.com/posts/git-rebase-intro/>

## 一、核心概念理解

1. 变基本质：将当前分支的提交"移植"到目标分支的最新提交之上
2. 与merge区别：
   - Merge：保留历史，创建新的合并提交
   - Rebase：重写历史，形成线性提交记录
3. 黄金法则：不要对已经推送到远程仓库的提交进行rebase

## 二、基础命令详解

### 1. 基本变基操作

```SHELL
# 将当前分支变基到目标分支
git rebase <目标分支>

# 示例：将feature分支变基到main分支
git checkout feature
git rebase main
```

### 2. 交互式变基（-i参数）

```SHELL
# 修改最近3次提交
git rebase -i HEAD~3

# 修改从某个commit开始的所有提交
git rebase -i <commit-hash>
```

交互式界面操作选项：

```shell
pick：保留该提交
reword：保留提交但修改提交信息
edit：保留提交但暂停以进行修改
squash：将提交合并到前一个提交
fixup：类似squash但丢弃提交信息
drop：删除提交
```

## 三、使用场景与操作流程

### 场景1：整理本地提交

```SHELL
# 1. 查看提交日志
git log --oneline

# 2. 开始交互式变基（修改最近5次提交）
git rebase -i HEAD~5

# 3. 在编辑器中调整提交（合并、重排、修改信息等）

# 4. 解决可能的冲突
git add <冲突文件>
git rebase --continue

# 5. 完成整理
```

### 场景2：同步上游更改

```SHELL
# 1. 获取远程最新代码
git fetch origin

# 2. 变基到远程分支
git rebase origin/main

# 替代git pull的更优方式
git pull --rebase origin main
```

### 场景3：分支整合

```SHELL
# 将feature分支变基到dev分支
git checkout feature
git rebase dev

# 解决冲突后...
git add .
git rebase --continue
```

## 四、高级技巧

### 1. 部分变基

```bash
# 只将部分提交变基到目标分支
git rebase --onto <新基> <旧基> <分支>

# 示例：将feature分支中不在dev分支上的提交变基到main
git rebase --onto main dev feature
```

### 2. 提交重排序

```bash
# 在交互式界面中直接调整提交顺序
# 将pick行按需要的顺序排列
```

### 3. 分割提交

```bash
# 在交互式界面标记为edit的提交
git reset HEAD^
git add -p  # 交互式添加变更
git commit -m "第一部分"
git commit -m "第二部分"
git rebase --continue
```

## 五、问题处理指南

### 1. 冲突解决流程

1. Git会在冲突时暂停rebase
2. 手动解决冲突文件
3. 使用git add标记已解决
4. git rebase --continue继续
5. 或git rebase --skip跳过当前提交
6. 或git rebase --abort完全终止

### 2. 恢复误操作

```bash
# 查看rebase前的原始引用
git reflog

# 重置到rebase前的状态
git reset --hard ORIG_HEAD
```

## 六、最佳实践清单

1. **本地提交**：只rebase尚未推送的本地提交
2. **频繁同步**：每天开始工作前从上游rebase
3. **团队约定**：明确团队是否允许/如何使用rebase
4. **备份习惯**：复杂rebase前创建临时分支
5. **清晰历史**：用交互式rebase整理出有逻辑的提交
6. **替代pull**：配置`git config --global pull.rebase true`

## 七、可视化理解

```BASH
初始状态：
A---B---C (main)
     \
      D---E (feature)

执行git rebase main后：
A---B---C (main)
         \
          D'---E' (feature)
```

**注意**：D'和E'是内容相同但hash不同的新提交

## 八、常见误区

1. **已推送的提交**：rebase会改变commit hash，导致协作问题
2. **过度整理**：不必追求完美历史，合理平衡时间成本
3. **忽略冲突**：rebase可能需多次解决相同冲突
4. **错误目标**：确保rebase的目标分支是正确的

## 九、配置建议

```bash
# 设置pull默认使用rebase
git config --global pull.rebase true

# 设置自动stash未提交的更改
git config --global rebase.autoStash true
```

## 十、工作流示例

日常开发推荐流程：

1. `git checkout -b feature`
2. 进行多次提交
3. `git fetch origin`
4. `git rebase origin/main`
5. 解决冲突
6. `git push origin feature`
7. 创建PR/MR
