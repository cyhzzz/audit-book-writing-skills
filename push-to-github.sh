#!/bin/bash
# GitHub仓库创建和推送脚本

# 步骤1：创建GitHub仓库
# 访问 https://github.com/new
# 仓库名称：audit-book-writing-skills
# 描述：审计专业书籍撰写、审核、优化完整工具集
# 可见性：Public（公开）或 Private（私有）
# 初始化：不添加 README、.gitignore 或 license（我们已经有了）
# 点击"Create repository"

# 步骤2：添加远程仓库
# 将下面的 <YOUR_GITHUB_USERNAME> 替换为你的GitHub用户名
echo "请将下面的命令中的 <YOUR_GITHUB_USERNAME> 替换为你的GitHub用户名，然后执行："
echo ""
echo "git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/audit-book-writing-skills.git"
echo ""

# 步骤3：推送代码到GitHub
echo "推送代码到GitHub："
echo ""
echo "git push -u origin master"
echo ""

# 步骤4：推送标签到GitHub
echo "推送标签到GitHub："
echo ""
echo "git push origin v1.0.0"
echo ""

# 例子（假设你的GitHub用户名是 wuying）：
# git remote add origin https://github.com/wuying/audit-book-writing-skills.git
# git push -u origin master
# git push origin v1.0.0
