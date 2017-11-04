# django 入门与实践

## 1-1 课程介绍

### 课程目标
* 学习并掌握 Django 的基本用法
* 了解 Django 的部分原理以及各组件的含义
* 可以独立使用 Django 进行基本的网站开发

### 课程内容
* 了解 Django
* 搭建开发环境
* 完成一个简单的个人博客网站

### 课程知识要求
* 掌握 Python 语言
* 了解 HTML 语言
* 了解浏览器上网的基本原理

---

## 2-1 课前准备

### Django 简介
* Django 是一个基于 Python 的高级 Web 开发框架
* 它能够让开发人员进行高效且快速的开发
* 高度集成（不用自己造轮子），免费并且开源

## 4-1 创建项目目录下部分文件的作用
### 创建步骤
* 打开命令行，进入想要安置项目的目录
* 命令行输入：django-admin startproject myblog
* 若没有报错，则创建项目成功

### 项目目录结构
* manage.py
* myblog
    * __init__.py
    * settings.py
    * urls.py
    * wsgi.py

#### manage.py
* 与项目进行交互的命令行工具集的入口
* 项目管理器
* 执行 python manage.py 来查看所有命令

#### myblog目录
* 项目的一个容器
* 包含项目最基本的一些配置
* 目录名称不建议修改

#### wsgi.py
* WSGI (Python Web Server Gateway Interface)
* 中文名：Python 服务器网关借口
* Python 应用与 Web 服务器之间的接口

#### urls.py
* url 配置文件
* Django 项目中所有地址（页面）都需要我们自己去配置其URL

#### settings.py
* 项目的总配置文件
* 里面包含了数据库、Web 应用、时间等各种配置

#### __init__.py
* Python 中声明模块的文件
* 内容默认为空

---

## 4-3 创建应用
### 创建步骤
* 打开命令行，进入项目中 manage.py 同级目录
* 命令行输入：python manage.py startapp blog
* 添加应用名到 settings.py 中的 INSTALLED_APPS 里

### 目录结构
* migrations
  * __init__.py
* __init__.py
* admin.py
* apps.py
* models.py
* tests.py
* views.py

#### migrations
* 数据移植（迁移）模块
* 全部自动生成

#### admin.py
* 该应用的后台管理系统配置

#### app.py
* 该应用的一些配置

#### models.py
* 数据模块
* 使用 ORM 框架
* 类似于 MVC 结构中的 Models（模型）

#### test.py
* 自动化测试模块
* Django 提供了自动化测试功能
* 在这里编写测试脚本（语句）

#### views.py
* 执行响应的代码所在模块
* 代码逻辑处理的主要地点
* 项目中大部分代码均在这里编写

### 创建第一个页面（响应）
* 编辑 blog.views 
