<!--
http://bbs.jooyoo.net/attachment/Mon_0905/24_65548_2835f8eaa933ff6.jpg
框架设计
个人博客搭建（一）
基于Python+Vue搭建搭建的无后端个人博客 - 原理讲解
一般的博客系统都是由前后端组成，当然也是有特殊情况，如使用WordPress工具搭建的无后端框架。对于上述几种情况来说，都需要某一个模块，能够管理所有模块的内容。普通的博客系统该部分由后端进行管理。而WordPress则在前端完成对所有内容的管理。
-->

## 个人博客搭建（一）

> 基于Python+Vue搭建搭建的无后端个人博客 - 原理讲解

一般的博客系统都是由前后端组成，当然也是有特殊情况，如使用WordPress工具搭建的无后端框架。

对于上述几种情况来说，都需要某一个模块，能够管理所有模块的内容。
普通的博客系统该部分由后端进行管理。而WordPress则在前端完成对所有内容的管理。

但是WordPress不是直接就对所用户创建内容进行管理的，他有一个`编译`的过程。
也就是将用户创建的内容，编译为前端可读的状态，然后由前端进行解读。

故知晓大致流程后，可以由Python来完成此**编译**过程。绘制大致流程如下：

![运行流程](https://ae01.alicdn.com/kf/H485cf804ba92481ba9456e9fc454563aZ.png)

**流程解读**：
* Python创建模板
* 用户编写博客：用户按markdown格式编写
* Python编译模板
* Vue异步读取json
* 前端发起异步请求