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
