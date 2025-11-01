# Blog\_website

一个专为 Django 框架新手设计的博客网站项目，包含基础核心功能与进阶特性，适合通过实战学习 Django 开发流程。

## 🌟 功能特点



* **文章管理系统**：支持文章的创建、编辑、删除与发布，实现完整内容生命周期管理

* **用户认证体系**：包含登录、注册、个人信息修改等功能，保障用户数据安全

* **Markdown 语法支持**：集成 Markdown 渲染与 Pygments 代码高亮，优化技术文章排版

* **响应式前端设计**：基于 Bootstrap 4 构建，适配电脑、平板、手机等多设备

* **互动评论功能**：支持用户对文章发表评论，增强博客社区属性

* **文章分类管理**：可按分类归档文章，提升内容检索效率

## 🛠 技术栈



| 领域   | 技术 / 工具                           |
| ---- | --------------------------------- |
| 后端   | Python 3.x、Django 5.2             |
| 前端   | HTML5、CSS3、JavaScript、Bootstrap 4 |
| 内容渲染 | Markdown、Pygments（代码高亮）           |
| 依赖管理 | pip                               |

## 🚀 安装与配置

### 前置条件



* 已安装 Python 3.x（推荐 3.8+）

* 已安装 pip（Python 包管理工具，通常随 Python 自带）

### 安装步骤



1. **克隆仓库到本地**



```
git clone https://github.com/z2123668062/Blog\_website.git

cd Blog\_website  # 进入项目根目录
```



1. **创建并激活虚拟环境**



```
\# 创建虚拟环境（避免依赖冲突）

python -m venv venv

\# 激活虚拟环境

\# Windows 系统

venv\Scripts\activate

\# macOS/Linux 系统

source venv/bin/activate
```

> 激活成功后，终端命令行前会显示 
>
> `(venv)`
>
>  标识



1. **安装项目依赖包**



```
pip install django markdown pygments django-allauth
```



1. **执行数据库迁移**



```
cd my\_blog  # 进入项目主应用目录

python manage.py makemigrations  # 生成数据库迁移文件

python manage.py migrate         # 应用迁移，创建数据库表
```



1. **创建管理员账号（用于后台管理）**



```
python manage.py createsuperuser
```

执行命令后，按提示输入用户名、电子邮箱、密码（密码输入时不显示，输入完成按回车即可）



1. **启动开发服务器**



```
python manage.py runserver
```



1. **访问项目**

* 博客前台：打开浏览器访问 `http://127.0.0.1:8000/article/`

* 管理员后台：打开浏览器访问 `http://127.0.0.1:8000/admin/`（使用步骤 5 创建的管理员账号登录）

## 📂 项目结构



```
Blog\_website/  # 项目根目录

├── my\_blog/                 # 项目主应用目录（核心代码目录）

│   ├── article/             # 文章功能模块（文章CRUD、分类等）

│   ├── userprofile/         # 用户功能模块（登录、注册、个人信息等）

│   ├── comment/             # 评论功能模块（评论提交、展示等）

│   ├── templates/           # HTML模板目录（页面结构文件）

│   │   ├── base.html        # 基础模板（所有页面的公共布局，如导航栏、页脚）

│   │   ├── header.html      # 导航栏模板（单独拆分，便于复用）

│   │   ├── footer.html      # 页脚模板（单独拆分，便于复用）

│   │   └── ...              # 其他页面模板（如文章列表、详情页等）

│   ├── static/              # 静态文件目录（样式、脚本、图片等）

│   │   ├── bootstrap/       # Bootstrap 相关文件（CSS、JS）

│   │   ├── md\_css/          # Markdown 渲染样式文件

│   │   └── ...              # 其他静态资源（如自定义CSS、JS）

│   ├── manage.py            # Django 命令行工具（项目启动、迁移等操作）

│   └── ...                  # 其他配置文件（如settings.py、urls.py等）

├── LICENSE                  # 开源许可证文件（Apache License 2.0）

└── README.md                # 项目说明文档（当前文档）
```

## 📄 许可证

本项目基于 **Apache License 2.0** 开源协议，允许个人或企业在遵守协议的前提下自由使用、修改和分发。详情请查看项目根目录下的 [L](LICENSE)[ICENS](LICENSE)[E](LICENSE) 文件。

## 📌 新手学习建议



1. 先熟悉 `my_blog` 目录下的 `settings.py` 配置文件，了解 Django 项目的基础配置

2. 从 `article` 模块入手，学习 Django 的模型（Model）、视图（View）、URL 路由映射逻辑

3. 研究 `templates` 目录下的模板文件，理解 Django 模板继承与变量渲染机制

4. 尝试在现有功能基础上扩展（如添加文章标签、阅读量统计等），巩固学习效果
