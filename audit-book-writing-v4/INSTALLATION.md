# 安装指南 (Installation Guide)

## 📋 前置要求

### 系统要求

- **操作系统:** Linux / macOS / Windows
- **Python 版本:** Python 3.8+
- **Node.js 版本:** Node.js 16+
- **内存:** 至少 4GB RAM
- **磁盘空间:** 至少 1GB 可用空间

### 软件依赖

```bash
# 基础依赖
- Python 3.8+
- Node.js 16+
- Git

# Python 依赖
- python-docx (处理 Word 文档)
- openpyxl (处理 Excel 文档)
- PyPDF2 (处理 PDF 文档)
- requests (HTTP 请求)

# Node.js 依赖
- @types/node (TypeScript 类型定义)
```

### 模型要求

- **推荐模型:** GLM-4.7 / GLM-4.6 / Claude 3.5 Sonnet
- **最低要求:** 支持 128K 上下文的模型
- **API 密钥:** 需要配置相应的 API 密钥

---

## 🚀 安装步骤

### 方法一：手动安装

#### 1. 克隆项目

```bash
# 克隆项目到本地
git clone https://github.com/your-username/audit-book-writing-v4.git

# 进入项目目录
cd audit-book-writing-v4
```

#### 2. 安装 Python 依赖

```bash
# 创建虚拟环境（推荐）
python3 -m venv venv

# 激活虚拟环境
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 安装 Python 依赖
pip install -r requirements.txt
```

#### 3. 安装 Node.js 依赖

```bash
# 安装 Node.js 依赖
npm install
```

#### 4. 配置环境变量

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，填入你的配置
nano .env
```

**环境变量配置示例:**

```bash
# API 配置
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key

# 模型配置
DEFAULT_MODEL=glm-4.7
FALLBACK_MODEL=glm-4.6

# 文件路径配置
OUTPUT_DIR=./output
TEMP_DIR=./temp

# 案例来源网站
NCHA_URL=http://www.ncha.gov.cn
ZJWWJ_URL=http://wwj.zj.gov.cn
```

#### 5. 验证安装

```bash
# 运行测试脚本
python tests/test_installation.py

# 如果看到 "✅ 安装成功!" 说明安装完成
```

---

### 方法二：通过包管理器安装

#### 使用 pip 安装

```bash
# 安装技能包
pip install audit-book-writing-v4

# 验证安装
pip show audit-book-writing-v4
```

#### 使用 npm 安装

```bash
# 安装技能包
npm install audit-book-writing-v4

# 验证安装
npm list audit-book-writing-v4
```

---

## 🔧 配置说明

### 配置文件位置

配置文件位于项目根目录的 `config.yaml`。

### 配置项说明

```yaml
# 技能配置
skill_config:
  version: "4.0.0"
  max_file_size: 50MB
  supported_formats:
    - ".doc"
    - ".docx"
  default_min_word_count: 5000

# 标记规则配置
marking_rules:
  enable_FA1: true   # 法规条文
  enable_FA2: true   # 法规延伸
  enable_FB1: true   # 条款引用
  enable_FB2: true   # 条款延伸
  enable_FC1: true   # 发文字号
  enable_FC2: true   # 文号延伸
  enable_A1: true    # 显式地名案例
  enable_A2: true    # 隐式地名案例

# 法规验证配置
verification_rules:
  max_regulation_files: 8
  similarity_threshold: 0.7
  strict_mode: true

# 案例替换配置
case_replacement_rules:
  priority_sites:
    - "国家文物局官方网站"
    - "浙江省文物局官方网站"
    - "其他各省文物局官方网站"
  max_search_results: 5
  allow_case_deletion: true

# 内容扩充配置
content_expansion_rules:
  max_expansion_per_regulation: 3
  include_audit_application: true
  include_source_url: true
  forbid_off_topic: true
  forbid_financial_content: true

# 结构优化配置
structure_optimization_rules:
  merge_duplicate_content: true
  resolve_conflicts: true
  preserve_structure: true

# 输出配置
output_config:
  generate_pdf_report: true
  generate_json_reports: true
  generate_execution_log: true
```

---

## 📦 依赖安装

### Python 依赖

```bash
# 安装基础依赖
pip install python-docx openpyxl PyPDF2 requests

# 安装开发依赖（可选）
pip install pytest black flake8 mypy
```

### Node.js 依赖

```bash
# 安装基础依赖
npm install

# 安装开发依赖（可选）
npm install --save-dev @types/node typescript
```

---

## 🧪 测试安装

### 运行测试

```bash
# 运行所有测试
python -m pytest tests/

# 运行特定测试
python -m pytest tests/test_marking.py

# 查看测试覆盖率
python -m pytest tests/ --cov=src --cov-report=html
```

### 手动测试

```bash
# 创建测试脚本
python scripts/manual_test.py

# 输入测试文件路径，查看输出结果
```

---

## 🚨 常见问题

### 问题 1: Python 版本不兼容

**错误信息:**

```
Python version 3.7 is not supported. Please use Python 3.8 or higher.
```

**解决方案:**

```bash
# 升级 Python 版本
# macOS:
brew install python@3.9

# Ubuntu/Debian:
sudo apt-get update
sudo apt-get install python3.9

# Windows:
# 从官网下载安装: https://www.python.org/downloads/
```

---

### 问题 2: 依赖安装失败

**错误信息:**

```
ERROR: Could not find a version that satisfies the requirement python-docx
```

**解决方案:**

```bash
# 升级 pip
python -m pip install --upgrade pip

# 使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

### 问题 3: API 密钥未配置

**错误信息:**

```
API key not found. Please configure your API key in .env file.
```

**解决方案:**

```bash
# 编辑 .env 文件
nano .env

# 添加 API 密钥
OPENAI_API_KEY=your_api_key_here

# 保存并退出
```

---

### 问题 4: 浏览器访问失败

**错误信息:**

```
Browser access failed. Please check your browser settings.
```

**解决方案:**

```bash
# 确保 gateway 服务正在运行
moltbot gateway status

# 如果未运行，启动服务
moltbot gateway start

# 然后使用浏览器工具
browser action=start profile=clawd
```

---

## 📝 卸载

### 手动卸载

```bash
# 停止虚拟环境
deactivate

# 删除项目目录
rm -rf audit-book-writing-v4

# 删除虚拟环境
rm -rf venv
```

### 使用包管理器卸载

```bash
# 使用 pip 卸载
pip uninstall audit-book-writing-v4

# 使用 npm 卸载
npm uninstall audit-book-writing-v4
```

---

## 🔄 更新

### 更新到最新版本

```bash
# 拉取最新代码
git pull origin master

# 更新 Python 依赖
pip install -r requirements.txt --upgrade

# 更新 Node.js 依赖
npm update
```

### 更新到特定版本

```bash
# 切换到特定版本
git checkout v4.0.0

# 安装对应版本的依赖
pip install -r requirements.txt
npm install
```

---

## 📚 下一步

安装完成后，建议阅读以下文档：

1. **[README.md](README.md)** - 项目说明和快速开始
2. **[SKILL.md](SKILL.md)** - 完整技能说明
3. **[PROJECT-OVERVIEW.md](PROJECT-OVERVIEW.md)** - 项目概览
4. **[docs/user-guide/](docs/user-guide/)** - 用户指南

---

## 🤝 获取帮助

如果遇到安装问题：

1. 查看 **[常见问题](#常见问题)** 部分
2. 在项目中提交 **[Issue](https://github.com/your-username/audit-book-writing-v4/issues)**
3. 查看 **[文档](docs/)** 获取更多信息
4. 联系维护者: **OpenClaw 🦞**

---

**文档版本:** v4.0.0
**最后更新:** 2026-02-27

---

祝你安装顺利！🚀
