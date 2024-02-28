# NJU Course Selector

## 简介

NJU Course Selector 是一个基于 DrissionPage 实现的自动选课 python 脚本。

主要功能包括：

- 选课网站登录
- 自动选择收藏界面中有空余名额的课程
- 无限刷新直至选课成功

## 使用

1. 安装相关依赖`DrissionPage`库，在终端中运行以下命令：
    ```
    pip install DrissionPage
    ```
2. 运行`main.py`；
3. 根据终端中的输入提示，输入所需信息；
4. 等待程序进入选课部分；
5. 看到浏览器在收藏界面无限刷新时，即代表运行成功。