# 学术论文 (标准版) - 中文总结 (100%)

## 生成信息
- **压缩级别**: 100%
- **生成时间**: 2025-08-10 14:29:42
- **工具**: MinerU内容总结器 V2
- **原始块数**: 37
- **处理章节数**: 37
- **压缩比**: 34.52%

## 目录
- [Chapter 1](#chapter-1)
  - [Effective Python - Section 1](#effective-python---section-1)
  - [Effective Python - Contents at a Glance](#effective-python---contents-at-a-glance)
  - [Effective Python - Contents](#effective-python---contents)
  - [Effective Python - Preface](#effective-python---preface)
  - [Effective Python - Acknowledgments](#effective-python---acknowledgments)
  - [Effective Python - About the Author](#effective-python---about-the-author)
  - [Effective Python - 1](#effective-python---1)
  - [Effective Python - Pythonic Thinking](#effective-python---pythonic-thinking)
  - [Effective Python - 2](#effective-python---2)
  - [Effective Python - Strings and Slicing](#effective-python---strings-and-slicing)
  - [Effective Python - 3](#effective-python---3)
  - [Effective Python - Loops and Iterators](#effective-python---loops-and-iterators)
  - [Effective Python - 4](#effective-python---4)
  - [Effective Python - Dictionaries](#effective-python---dictionaries)
  - [Effective Python - 5](#effective-python---5)
  - [Effective Python - Functions](#effective-python---functions)
  - [Effective Python - 6](#effective-python---6)
  - [Effective Python - Comprehensions and Generators](#effective-python---comprehensions-and-generators)
  - [Effective Python - 7](#effective-python---7)
  - [Effective Python - Classes and Interfaces](#effective-python---classes-and-interfaces)
  - [Effective Python - 8](#effective-python---8)
  - [Effective Python - Metaclasses and Attributes](#effective-python---metaclasses-and-attributes)
  - [Effective Python - 9](#effective-python---9)
  - [Effective Python - Concurrency and Parallelism](#effective-python---concurrency-and-parallelism)
  - [Effective Python - 10](#effective-python---10)
  - [Effective Python - Robustness](#effective-python---robustness)
  - [Effective Python - 11](#effective-python---11)
  - [Effective Python - Performance](#effective-python---performance)
  - [Effective Python - 12](#effective-python---12)
  - [Effective Python - Data Structures and Algorithms](#effective-python---data-structures-and-algorithms)
  - [Effective Python - 13](#effective-python---13)
  - [Effective Python - Testing and Debugging](#effective-python---testing-and-debugging)
  - [Effective Python - 14](#effective-python---14)
  - [Effective Python - Collaboration](#effective-python---collaboration)
  - [Effective Python - Index](#effective-python---index)
  - [Effective Python - Code Snippets](#effective-python---code-snippets)

## Chapter 1

章节标题: 第一章
章节规模: 3 tokens

本章作为引言，旨在为后续章节奠定基础，并概述了Graph Neural Networks (GNNs) 和 Graph Foundation Models (GFMs) 在处理图结构数据方面的核心贡献和主要观点。本章将系统性地介绍图数据处理的挑战，以及GNNs如何通过Message Passing等机制有效捕捉图的拓扑结构和节点特征。同时，本章还将探讨GFMs的出现如何进一步推动图学习领域的发展，特别是在实现强大的Zero-shot Learning和Few-shot Learning能力方面。我们将重点阐述GFMs在各种下游任务，如Node Classification、Link Prediction和Graph Classification中的潜力，并为理解后续章节中更深入的技术细节和应用场景提供必要的背景知识。

## Effective Python - Section 1

章节标题: 有效的 Python
章节规模: 299 tokens

重要要求:
1. 这是一个完整的大章节，请保持内容的连贯性和逻辑完整性
2. 重点突出章节的核心贡献和主要观点
3. 保持学术写作的严谨性和专业性
4. 对于包含多个子章节的内容，请按逻辑顺序组织总结
5. 如果原文中有图片链接（格式如![](./images/xxx.jpg)），请保留这些图片链接，如果文中有对图片的相关描述可以简要提及。不要输出任何原文中没有的图片链接
7. 专有技术名词保持英文原文，不要翻译，包括但不限于：
- Graph Neural Networks (GNNs), Graph Foundation Models (GFMs), Transformer
- Graph Attention Networks (GAT), GraphSAGE, Message Passing, Node Embedding
- Graph Convolutional Networks (GCN), Self-supervised Learning, Pre-training
- Fine-tuning, In-context Learning, Few-shot Learning, Zero-shot Learning
- Knowledge Graph, Heterogeneous Graph, Homogeneous Graph, Graph Isomorphism
- Graph Pooling, Graph Classification, Node Classification, Link Prediction
- Graph Generation, Graph Anomaly Detection, Contrastive Learning
- Multi-modal Learning, Cross-domain Transfer, Domain Adaptation

原文内容:
# 有效的 Python
125 种写出更好 Python 的具体方法
**第三版**
**Brett Slatkin**
![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/pub_005ef7a1.jpg)
---
<a role="toc_link" id="copyright"></a>
许多制造商和销售商用来区分其产品的名称被声称为商标。当这些名称出现在本书中，并且出版商知晓其商标声明时，这些名称已以首字母大写或全部大写的方式印刷。
作者和出版商在本书的准备过程中已尽心尽力，但未作任何明示或暗示的保证，并对错误或遗漏不承担任何责任。对于因使用本书中的信息或程序而引起的或与之相关的附带或间接损害，不承担任何责任。
有关批量购买本书的标题信息，或特殊销售机会（可能包括电子版本；定制封面设计；以及特定于您的业务、培训目标、营销重点或品牌兴趣的内容），请联系我们的企业销售部门，邮箱为 [corpsales@pearsoned.com](#undefined) 或致电 (800) 382-3419。如果您对任何潜在偏见有疑虑，请通过 [pearson.com/report-bias.html](#undefined) 联系我们。
对于政府销售咨询，请联系 [governmentsales@pearsoned.com](#undefined)。
对于美国以外的销售问题，请联系 [intlcs@pearson.com](#undefined)。
请访问我们的网站：[informit.com/aw](#undefined)
国会图书馆控制号：2024945552
版权所有 © 2025 Pearson Education, Inc.
Hoboken, NJ
封面图片：Victoria Moloman/Shutterstock
保留所有权利。本出版物受版权保护，未经出版商许可，禁止以任何形式或通过任何电子、机械、影印、录制或其他方式进行任何未经授权的复制、存储在检索系统中或传输。有关许可、申请表以及 Pearson Education Global Rights & Permissions Department 内的适当联系方式的信息，请访问 [www.pearson.com/permissions](#undefined)。
ISBN-13：978-0-13-817218-3
ISBN-10：0-13-817218-8
`**$PrintCode**`
---
<a role="toc_link" id="dedi"></a>
_致我们的家人_
---
<a role="toc_link" id="toc"></a>

## Effective Python - Contents at a Glance

## 一览内容

1.  [序言](#pref01#pref01)
2.  [致谢](#pref02#pref02)
3.  [关于作者](#pref03#pref03)
4.  [第一章：Pythonic 思维](#ch01#ch01)
5.  [第二章：字符串和切片](#ch02#ch02)
6.  [第三章：循环和迭代器](#ch03#ch03)
7.  [第四章：字典](#ch04#ch04)
8.  [第五章：函数](#ch05#ch05)
9.  [第六章：推导式和生成器](#ch06#ch06)
10. [第七章：类和接口](#ch07#ch07)
11. [第八章：元类和属性](#ch08#ch08)
12. [第九章：并发和并行](#ch09#ch09)
13. [第十章：健壮性](#ch10#ch10)
14. [第十一章：性能](#ch11#ch11)
15. [第十二章：数据结构和算法](#ch12#ch12)
16. [第十三章：测试和调试](#ch13#ch13)
17. [第十四章：协作](#ch14#ch14)
18. [索引](#index#index)
---
<a role="toc_link" id="bk01-toc"></a>

## Effective Python - Contents

## 目录

1.  [前言](#pref01#pref01)
2.  [致谢](#pref02#pref02)
3.  [关于作者](#pref03#pref03)
4.  [第一章 Pythonic思维](#ch01#ch01)
1.  [条目 1：了解你正在使用的Python版本](#ch01#ch01lev1sec1)
2.  [条目 2：遵循PEP 8风格指南](#ch01#ch01lev1sec2)
3.  [条目 3：切勿期望Python在编译时检测错误](#ch01#ch01lev1sec3)
4.  [条目 4：编写辅助函数而非复杂表达式](#ch01#ch01lev1sec4)
5.  [条目 5：优先使用多重赋值解包而非索引](#ch01#ch01lev1sec5)
6.  [条目 6：单元素元组始终用括号括起来](#ch01#ch01lev1sec6)
7.  [条目 7：考虑使用条件表达式进行简单的内联逻辑](#ch01#ch01lev1sec7)
8.  [条目 8：使用赋值表达式防止重复](#ch01#ch01lev1sec8)
9.  [条目 9：在流程控制中考虑使用match进行解构；当if语句足够时避免使用](#ch01#ch01lev1sec9)
5.  [第二章 字符串和切片](#ch02#ch02)
1.  [条目 10：了解bytes和str之间的区别](#ch02#ch02lev1sec1)
2.  [条目 11：优先使用插值f-string而非C风格格式字符串和str.format](#ch02#ch02lev1sec2)
3.  [条目 12：理解打印对象时repr和str的区别](#ch02#ch02lev1sec3)
4.  [条目 13：优先使用显式字符串连接而非隐式连接，尤其是在列表中](#ch02#ch02lev1sec4)
5.  [条目 14：了解如何切片序列](#ch02#ch02lev1sec5)
6.  [条目 15：避免在单个表达式中同时使用步长和切片](#ch02#ch02lev1sec6)
7.  [条目 16：优先使用捕获式解包而非切片](#ch02#ch02lev1sec7)
6.  [第三章 循环和迭代器](#ch03#ch03)
1.  [条目 17：优先使用enumerate而非range](#ch03#ch03lev1sec1)
2.  [条目 18：使用zip并行处理迭代器](#ch03#ch03lev1sec2)
3.  [条目 19：避免在for和while循环后使用else块](#ch03#ch03lev1sec3)
4.  [条目 20：循环结束后切勿使用for循环变量](#ch03#ch03lev1sec4)
5.  [条目 21：在迭代参数时要谨慎](#ch03#ch03lev1sec5)
6.  [条目 22：迭代容器时切勿修改它们；改用副本或缓存](#ch03#ch03lev1sec6)
7.  [条目 23：将迭代器传递给any和all以实现高效的短路逻辑](#ch03#ch03lev1sec7)
8.  [条目 24：考虑使用itertools处理迭代器和生成器](#ch03#ch03lev1sec8)
7.  [第四章 字典](#ch04#ch04)
1.  [条目 25：依赖字典插入顺序时要谨慎](#ch04#ch04lev1sec1)
2.  [条目 26：优先使用get而非in和KeyError来处理缺失的字典键](#ch04#ch04lev1sec2)
3.  [条目 27：优先使用defaultdict而非setdefault来处理内部状态中缺失的项](#ch04#ch04lev1sec3)
4.  [条目 28：了解如何使用__missing__构造键相关的默认值](#ch04#ch04lev1sec4)
5.  [条目 29：组合类而非深度嵌套字典、列表和元组](#ch04#ch04lev1sec5)
8.  [第五章 函数](#ch05#ch05)
1.  [条目 30：了解函数参数可以被修改](#ch05#ch05lev1sec1)
2.  [条目 31：返回专用的结果对象，而不是要求函数调用者解包超过三个变量](#ch05#ch05lev1sec2)
3.  [条目 32：优先抛出异常而非返回None](#ch05#ch05lev1sec3)
4.  [条目 33：了解闭包如何与变量作用域和nonlocal交互](#ch05#ch05lev1sec4)
5.  [条目 34：使用可变位置参数减少视觉噪音](#ch05#ch05lev1sec5)
6.  [条目 35：使用关键字参数提供可选行为](#ch05#ch05lev1sec6)
7.  [条目 36：使用None和Docstrings指定动态默认参数](#ch05#ch05lev1sec7)
8.  [条目 37：使用关键字参数和位置参数强制清晰性](#ch05#ch05lev1sec8)
9.  [条目 38：使用functools.wraps定义函数装饰器](#ch05#ch05lev1sec9)
10. [条目 39：优先使用functools.partial而非lambda表达式作为粘合函数](#ch05#ch05lev1sec10)
9.  [第六章 推导式和生成器](#ch06#ch06)
1.  [条目 40：使用推导式而非map和filter](#ch06#ch06lev1sec1)
2.  [条目 41：避免在推导式中使用超过两个控制子表达式](#ch06#ch06lev1sec2)
3.  [条目 42：在推导式中使用赋值表达式减少重复](#ch06#ch06lev1sec3)
4.  [条目 43：考虑使用生成器而非返回列表](#ch06#ch06lev1sec4)
5.  [条目 44：考虑使用生成器表达式处理大型列表推导式](#ch06#ch06lev1sec5)
6.  [条目 45：使用yield from组合多个生成器](#ch06#ch06lev1sec6)
7.  [条目 46：将迭代器作为参数传递给生成器，而不是调用send方法](#ch06#ch06lev1sec7)
8.  [条目 47：使用类而非生成器的throw方法来管理迭代状态转换](#ch06#ch06lev1sec8)
10. [第七章 类和接口](#ch07#ch07)
1.  [条目 48：接受函数而非类用于简单接口](#ch07#ch07lev1sec1)
2.  [条目 49：优先使用面向对象的 Polymorphism 而非带isinstance检查的函数](#ch07#ch07lev1sec2)
3.  [条目 50：考虑使用functools.singledispatch进行函数式编程，而非面向对象的 Polymorphism](#ch07#ch07lev1sec3)
4.  [条目 51：优先使用dataclasses定义轻量级类](#ch07#ch07lev1sec4)
5.  [条目 52：使用@classmethod Polymorphism 通用地构造对象](#ch07#ch07lev1sec5)
6.  [条目 53：使用super初始化父类](#ch07#ch07lev1sec6)
7.  [条目 54：考虑使用Mix-in类组合功能](#ch07#ch07lev1sec7)
8.  [条目 55：优先使用公共属性而非私有属性](#ch07#ch07lev1sec8)
9.  [条目 56：优先使用dataclasses创建不可变对象](#ch07#ch07lev1sec9)
10. [条目 57：继承collections.abc类以创建自定义容器类型](#ch07#ch07lev1sec10)
11. [第八章 元类和属性](#ch08#ch08)
1.  [条目 58：使用普通属性而非setter和getter方法](#ch08#ch08lev1sec1)
2.  [条目 59：考虑使用@property而非重构属性](#ch08#ch08lev1sec2)
3.  [条目 60：使用描述符（Descriptors）实现可重用的@property方法](#ch08#ch08lev1sec3)
4.  [条目 61：使用__getattr__、__getattribute__和__setattr__实现惰性属性](#ch08#ch08lev1sec4)
5.  [条目 62：使用__init_subclass__验证子类](#ch08#ch08lev1sec5)
6.  [条目 63：使用__init_subclass__注册类存在性](#ch08#ch08lev1sec6)
7.  [条目 64：使用__set_name__注解类属性](#ch08#ch08lev1sec7)
8.  [条目 65：考虑类体定义顺序以建立属性之间的关系](#ch08#ch08lev1sec8)
9.  [条目 66：优先使用类装饰器而非元类来实现可组合的类扩展](#ch08#ch08lev1sec9)
12. [第九章 并发和并行](#ch09#ch09)
1.  [条目 67：使用subprocess管理子进程](#ch09#ch09lev1sec1)
2.  [条目 68：使用线程处理阻塞I/O；避免用于并行性](#ch09#ch09lev1sec2)
3.  [条目 69：使用Lock防止线程中的数据竞争](#ch09#ch09lev1sec3)
4.  [条目 70：使用Queue协调线程间的工作](#ch09#ch09lev1sec4)
5.  [条目 71：了解何时需要并发](#ch09#ch09lev1sec5)
6.  [条目 72：避免为按需扇出（fan-out）创建新的线程实例](#ch09#ch09lev1sec6)
7.  [条目 73：理解使用Queue实现并发需要重构](#ch09#ch09lev1sec7)
8.  [条目 74：当线程对于并发是必需的时，考虑ThreadPoolExecutor](#ch09#ch09lev1sec8)
9.  [条目 75：使用协程（Coroutines）实现高并发I/O](#ch09#ch09lev1sec9)
10. [条目 76：了解如何将线程I/O移植到asyncio](#ch09#ch09lev1sec10)
11. [条目 77：混合使用线程和协程以简化向asyncio的过渡](#ch09#ch09lev1sec11)
12. [条目 78：使用对asyncio友好的工作线程最大化asyncio事件循环的响应性](#ch09#ch09lev1sec12)
13. [条目 79：考虑concurrent.futures以实现真正的并行性](#ch09#ch09lev1sec13)
13. [第十章 健壮性](#ch10#ch10)
1.  [条目 80：充分利用try/except/else/finally中的每个块](#ch10#ch10lev1sec1)
2.  [条目 81：断言内部假设并抛出未满足的期望](#ch10#ch10lev1sec2)
3.  [条目 82：考虑使用contextlib和with语句实现可重用的try/finally行为](#ch10#ch10lev1sec3)
4.  [条目 83：始终使try块尽可能短](#ch10#ch10lev1sec4)
5.  [条目 84：注意异常变量的消失](#ch10#ch10lev1sec5)
6.  [条目 85：注意捕获异常类](#ch10#ch10lev1sec6)
7.  [条目 86：理解Exception和BaseException的区别](#ch10#ch10lev1sec7)
8.  [条目 87：使用traceback进行增强的异常报告](#ch10#ch10lev1sec8)
9.  [条目 88：考虑显式链接异常以澄清回溯信息](#ch10#ch10lev1sec9)
10. [条目 89：始终将资源传递给生成器，并让调用者在外部清理它们](#ch10#ch10lev1sec10)
11. [条目 90：切勿将__debug__设置为False](#ch10#ch10lev1sec11)
12. [条目 91：除非您正在构建开发者工具，否则避免使用exec和eval](#ch10#ch10lev1sec12)
14. [第十一章 性能](#ch11#ch11)
1.  [条目 92：在优化之前进行性能分析（Profiling）](#ch11#ch11lev1sec1)
2.  [条目 93：使用timeit微基准测试来优化性能关键代码](#ch11#ch11lev1sec2)
3.  [条目 94：了解何时以及如何用另一种编程语言替换Python](#ch11#ch11lev1sec3)
4.  [条目 95：考虑使用ctypes快速与原生库集成](#ch11#ch11lev1sec4)
5.  [条目 96：考虑使用扩展模块以最大化性能和易用性](#ch11#ch11lev1sec5)
6.  [条目 97：依赖预编译字节码和文件系统缓存来提高启动时间](#ch11#ch11lev1sec6)
7.  [条目 98：使用动态导入（Dynamic Imports）惰性加载模块以减少启动时间](#ch11#ch11lev1sec7)
8.  [条目 99：考虑使用memoryview和bytearray进行与bytes的零拷贝交互](#ch11#ch11lev1sec8)
15. [第十二章 数据结构和算法](#ch12#ch12)
1.  [条目 100：使用key参数按复杂标准排序](#ch12#ch12lev1sec1)
2.  [条目 101：了解sort和sorted的区别](#ch12#ch12lev1sec2)
3.  [条目 102：考虑使用bisect搜索已排序序列](#ch12#ch12lev1sec3)
4.  [条目 103：优先使用deque作为生产者-消费者队列](#ch12#ch12lev1sec4)
5.  [条目 104：了解如何使用heapq实现优先队列](#ch12#ch12lev1sec5)
6.  [条目 105：使用datetime而非time处理本地时钟](#ch12#ch12lev1sec6)
7.  [条目 106：在精度至关重要时使用decimal](#ch12#ch12lev1sec7)
8.  [条目 107：使用copyreg使pickle序列化易于维护](#ch12#ch12lev1sec8)
16. [第十三章 测试和调试](#ch13#ch13)
1.  [条目 108：在TestCase子类中验证相关行为](#ch13#ch13lev1sec1)
2.  [条目 109：优先集成测试而非单元测试](#ch13#ch13lev1sec2)
3.  [条目 110：使用setUp、tearDown、setUpModule和tearDownModule将测试彼此隔离](#ch13#ch13lev1sec3)
4.  [条目 111：使用Mocks测试具有复杂依赖关系的代码](#ch13#ch13lev1sec4)
5.  [条目 112：封装依赖项以方便Mocking和测试](#ch13#ch13lev1sec5)
6.  [条目 113：使用assertAlmostEqual控制浮点数测试的精度](#ch13#ch13lev1sec6)
7.  [条目 114：考虑使用pdb进行交互式调试](#ch13#ch13lev1sec7)
8.  [条目 115：使用tracemalloc了解内存使用情况和泄漏](#ch13#ch13lev1sec8)
17. [第十四章 协作](#ch14#ch14)
1.  [条目 116：了解在哪里可以找到社区构建的模块](#ch14#ch14lev1sec1)
2.  [条目 117：使用虚拟环境进行隔离和可重现的依赖管理](#ch14#ch14lev1sec2)
3.  [条目 118：为每个函数、类和模块编写Docstrings](#ch14#ch14lev1sec3)
4.  [条目 119：使用包来组织模块并提供稳定的API](#ch14#ch14lev1sec4)
5.  [条目 120：考虑使用模块级作用域的代码来配置部署环境](#ch14#ch14lev1sec5)
6.  [条目 121：定义根异常以隔离调用者免受API影响](#ch14#ch14lev1sec6)
7.  [条目 122：了解如何打破循环依赖](#ch14#ch14lev1sec7)
8.  [条目 123：考虑使用warnings来重构和迁移用法](#ch14#ch14lev1sec8)
9.  [条目 124：考虑通过typing进行静态分析以避免错误](#ch14#ch14lev1sec9)
10. [条目 125：优先使用开源项目打包Python程序，而非zipimport和zipapp](#ch14#ch14lev1sec10)
18. [索引](#index#index)
---
<a role="toc_link" id="pref01"></a>

## Effective Python - Preface

## 有效Python - 前言

Python 编程语言拥有独特且难以捉摸的优势和魅力。许多熟悉其他语言的程序员以一种受限的心态来接触 Python，而不是拥抱其全部能力。有些程序员则走向另一个极端，过度使用可能导致未来出现重大问题的 Python 特性。

本书深入探讨了编写程序的 _Pythonic_ 方式：使用 Python 的最佳方法。它建立在我对语言的基本理解之上，我假设您已经具备了这种理解。新手程序员将学习 Python 关键特性的最佳实践。有经验的程序员将学会如何自信地拥抱一种新工具。

我希望通过这本书帮助您实现您的目标，无论它们是什么，或者至少能帮助您在编程旅程中获得更多乐趣。

### 本书涵盖内容

本书的每一章都包含一系列广泛但相关的项目。您可以随意在项目之间跳转，跟随您的兴趣。每个项目都包含简洁具体的指导，解释如何更有效地编写 Python 程序。项目包括关于做什么、避免什么、如何取得平衡以及为什么这是最佳选择的建议。项目之间相互引用，以便在阅读时更容易填补空白。

本第三版涵盖了截至 Python 3.13 的语言特性（请参阅 [Item 1](#ch01#ch01lev1sec1)：“[了解您正在使用的 Python 版本](#ch01#ch01lev1sec1)”）。与第二版相比，本书包含了 35 个全新的项目。第二版中的大多数项目都经过修订并包含在内，但许多项目都进行了实质性的更新。对于某些项目，由于过去五年 Python 的成熟以及最佳实践的演变，我的建议已完全改变。

Python 采取了“自带电池”的方法来处理其标准库。许多这些内置包与惯用的 Python 紧密结合，以至于它们似乎就是语言规范的一部分。标准模块的完整集合对于本书来说过于庞大，但我包含了我认为您必须了解和使用的关键模块。

Python 还拥有一个充满活力的社区构建模块生态系统，以有价值的方式扩展了语言。虽然我在各种项目中提到了重要的软件包，但本书无意成为一个详尽的参考。同样，尽管 Python 包管理很重要，但我避免详细介绍它，因为它正在快速变化和发展。

#### 第 1 章：Pythonic 思维

Python 社区已经开始使用形容词 _Pythonic_ 来描述遵循特定风格的代码。Python 的惯用法是通过使用该语言的经验和与其他程序员的协作而产生的。本章涵盖了在 Python 中执行最常见任务的最佳方法。

#### 第 2 章：字符串和切片

Python 拥有用于字符串和序列处理的内置语法、方法和模块。这些功能如此重要，您几乎会在每个程序中看到它们。它们使 Python 成为解析文本、检查数据格式以及与计算机使用的底层二进制表示进行交互的优秀语言。

#### 第 3 章：循环和迭代器

处理顺序数据是程序中的一项关键需求。Python 中的循环在处理内置数据类型、容器类型和用户定义类时，对于最常见的任务来说感觉自然且功能强大。Python 还支持迭代器，它们能够以更函数式的方式处理任意数据流，并带来显著的好处。

#### 第 4 章：字典

Python 的内置字典类型是程序中用于记账的多功能数据结构。与简单的列表相比，字典在添加和删除项目方面提供了更好的性能。Python 还具有特殊的语法和相关的内置模块，可以增强字典的功能，超出您对其他语言中哈希表的预期。

#### 第 5 章：函数

Python 中的函数具有多种额外功能，可以使程序员的生活更轻松。其中一些功能与其他编程语言的功能相似，但许多功能是 Python 所独有的。本章介绍了如何使用函数来阐明意图、促进重用并减少错误。

#### 第 6 章：推导式和生成器

Python 具有特殊的语法，可以快速迭代列表、字典和集合以生成派生数据结构。它还允许函数逐步返回可迭代值流。本章介绍了这些功能如何提供更好的性能、减少内存使用和提高可读性。

#### 第 7 章：类和接口

Python 是一种面向对象的语言。在 Python 中完成任务通常需要编写新类并定义它们如何通过其接口和层次结构进行交互。本章介绍了如何使用类来表达对象意图的行为。

#### 第 8 章：元类和属性

元类和动态属性是强大的 Python 功能。然而，它们也使您能够实现极其怪异且出乎意料的行为。本章介绍了使用这些机制的常见惯用法，以确保您遵循 _最少惊讶原则_。

#### 第 9 章：并发和并行

通过线程和异步协程等功能，Python 可以轻松编写看似同时执行许多不同任务的并发程序。Python 还可以通过系统调用、子进程和特殊模块用于并行工作。本章介绍了如何在这些细微不同的情况下最佳地利用 Python。

#### 第 10 章：健壮性

使程序在遇到意外情况时具有可依赖性，与使程序具有正确功能同样重要。Python 具有内置功能和模块，有助于加固您的程序，使其在各种情况下都具有健壮性。

#### 第 11 章：性能

Python 包含了各种功能，使程序能够以相对较低的努力实现令人惊讶的impressive性能。利用这些功能，可以在保留 Python 高级特性的生产力优势的同时，从主机系统中提取最大性能。

#### 第 12 章：数据结构和算法

Python 包含了许多标准数据结构和算法的优化实现，可以帮助您以最小的努力实现高性能。该语言还提供了经过实战检验的数据类型和辅助函数，用于常见任务（例如，处理货币和时间），使您可以专注于程序的关键需求。

#### 第 13 章：测试和调试

无论您的代码是用什么语言编写的，您都应该始终测试您的代码，但在 Python 中，测试尤其重要。Python 的动态特性可能以独特的方式增加运行时错误的风险。幸运的是，它们也使编写测试和诊断故障程序变得更加容易。本章介绍了 Python 用于测试和调试的内置工具。

#### 第 14 章：协作

协作编写 Python 程序需要您有意识地编写代码。即使您独自工作，您也需要了解如何使用他人编写的模块。本章介绍了使人们能够协同处理 Python 程序的标准工具和最佳实践。

### 本书使用的约定

本书中的 Python 代码片段使用 `monospace font` 并具有语法高亮。当行很长时，我使用 ➥ 字符来表示换行。我使用省略号（`...`）截断一些代码片段，以指示存在对表达观点不重要的代码区域。您需要下载完整的示例代码（请参阅下方获取方式），以便在您的计算机上正确运行这些截断的代码片段。

为了使代码示例更好地适应书籍格式或突出最重要的部分，我在 Python 风格指南上做了一些艺术性的调整。我还省略了嵌入式文档以减小代码示例的大小。我强烈建议您不要在您的项目中模仿这一点；相反，您应该遵循风格指南（请参阅 [Item 2](#ch01#ch01lev1sec2)：“[遵循 PEP 8 风格指南](#ch01#ch01lev1sec2)”）并编写文档（请参阅 [Item 118](#ch14#ch14lev1sec3)：“[为每个函数、类和模块编写文档字符串](#ch14#ch14lev1sec3)”）。

本书中的大多数代码片段都附带了运行代码的相应输出。当我提到“输出”时，我指的是控制台或终端输出：当您在交互式解释器中运行 Python 程序时看到的内容。输出部分使用 `monospace font`，每个输出部分前面都有一个 `>>>` 行（Python 交互式提示符）。其理念是，您可以将代码片段输入到 Python shell 中并重现预期的输出。

最后，还有一些其他使用 `monospace font` 的部分，前面没有 `>>>` 行。这些代表运行 Python 解释器以外的程序产生的输出。这些示例通常以 `$` 字符开头，表示我正在从 Bash 等命令行 shell 运行程序。如果您在 Windows 或其他类型的系统上运行这些命令，您可能需要相应地调整程序名称和参数。

#### 获取代码和勘误表

将本书中的许多示例作为完整的程序进行查看，而无需穿插的文本，这是很有用的。这还让您有机会自己尝试代码并理解程序为何如所述工作。您可以在本书网站 <https://effectivepython.com> 上找到本书所有代码片段的源代码。该网站还提供了有关如何报告错误的说明。提前感谢您就您发现的任何错误与我联系。

在 InformIT 网站上注册您的 **_Effective Python: 125 Specific Ways to Write Better Python, 3rd Edition_** 副本，以便方便地获取更新和/或更正。要开始注册过程，请访问 [informit.com/register](#undefined) 并登录或创建帐户。输入产品 ISBN（**9780138172183**）并点击提交。如果您希望收到有关新版本和更新的独家优惠通知，请勾选接收我们电子邮件的复选框。

---
<a role="toc_link" id="pref02"></a>

## Effective Python - Acknowledgments

## 致谢

感谢您阅读本书。我必须强调，本书的完成离不开许多人的指导、支持和鼓励。

感谢 Scott Meyers 的《Effective Software Development》系列书籍。我在年少时就发现了计算机编程的乐趣，但当我 15 岁时读到他的《Effective C++》时，一切都豁然开朗。毫无疑问，Scott 的书籍引导了我接受大学教育并找到了第一份工作。我非常荣幸能有机会撰写《Effective Python》的所有三版。在此过程中我学到了很多，我对此经历深表感激。

感谢促成第三版问世的团队。感谢我的执行编辑 Debra Williams，在整个过程中给予我如此多的支持。感谢发展编辑 Chris Zahn，制作编辑 Mary Roth，文字编辑 Kitty Wilson，封面设计师 Chuti Prasertsith，以及营销经理 Chike Lawrence-Mitchell。感谢我的技术审稿人——Karry Lu、David N. Cohron 和 Andy Chu——他们提供了深刻而详尽的反馈。

感谢所有在我创作本书第一版和第二版过程中支持我的人：Debra Williams、Trina MacDonald、Olivia Basegio、Mike Bayer、Titus Brown、Brett Cannon、Andy Chu、Tom Cirtin、Nick Cohron、Leah Culver、Andrew Dolan、Pamela Fox、Stephanie Geels、Adrian Holovaty、Toshiaki Kurokawa、Michael Levine、Lori Lyons、Asher Mancinelli、Wes McKinney、Julie Nahil、Stephane Nakib、Stephane Nakib、Marzia Niccolai、Ade Oshineye、Chuti Prasertsith、Brandon Rhodes、Tavis Rudd、Katrina Sostek、Mike Taylor、Simon Willison、Kitty Wilson 和 Chris Zahn。

感谢所有报告书中错误和改进意见的读者。请继续提供您的宝贵反馈！感谢所有让本书得以在全球发行的翻译者；看到我的书被翻译成其他语言，总是让我倍感欣慰。

感谢我认识并共事过的杰出的 Python 程序员们：Anthony Baxter、Brett Cannon、Wesley Chun、Jeremy Hylton、Alex Martelli、Neal Norwitz、Guido van Rossum、Andy Smith、Greg Stein、Ka-Ping Yee 和 Gregory Smith。我非常感激你们的教诲和领导。Python 拥有一个卓越的社区，我很幸运能成为其中的一员。

感谢我多年来的队友们，他们让我能够成为团队中“最差的那个”。感谢 Kevin Gibbs 帮助我勇于冒险。感谢 Ken Ashcraft、Ryan Barrett 和 Jon McAlister 向我展示了如何做到。感谢 Brad Fitzpatrick 将一切提升到新的高度。感谢 Paul McDonald 成为我出色的联合创始人。感谢 Jeremy Ginsberg、Jack Hebert、John Skidgel、Evan Martin、Tony Chang、Troy Trimble、Tessa Pupius、Erick Armbrust 和 Dylan Lorimer 帮助我学习。感谢 Sagnik Nandy、Waleed Ojeil 和 Will Grannis 的指导。

感谢我曾有过的那些鼓舞人心的编程和工程学老师们：Ben Chelf、Glenn Cowan、Vince Hugo、Russ Lewin、Jon Stemmle、Derek Thomson、Daniel Wang、Dean Nevins、Stephen Strenn 和 Alex Guy。没有你们的教导，我永远不会投身于我们的技艺，也无法获得教导他人的视角。

感谢我的母亲赋予我使命感，并鼓励我成为一名程序员。感谢我的家人和朋友的支持。感谢我的妻子给予我的爱和友谊。
---
<a role="toc_link" id="pref03"></a>

## Effective Python - About the Author

## 关于作者
**Brett Slatkin** 在过去 19 年里一直以 Python 进行专业编程。他目前在 Google 的 CTO 办公室担任首席软件工程师，负责开发技术战略和快速原型。
他之前的经验包括创立 Google Surveys，这是一个用于收集机器学习和市场研究数据集的内部初创公司；推出 Google App Engine，这是该公司的首个云计算产品；将 Google 的 A/B 实验产品扩展到数十亿用户；共同创建 PubSubHubbub，这是 W3C 的实时 RSS feeds 标准；以及为开源项目做出各种贡献。
Brett 在纽约市哥伦比亚大学获得了计算机工程学士学位。在工作之余，他喜欢弹钢琴、冲浪和与家人共度时光。他住在加利福尼亚州。您可以在 <https://onebigfluke.com> 找到他。
---
<a role="toc_link" id="ch01"></a>

## Effective Python - 1

## 1

本章节将深入探讨 **Effective Python** 的核心概念和实践，重点关注如何利用 Python 语言的特性和丰富的库来编写高效、可维护且易于理解的代码。我们将从 Python 的基础语法和数据结构出发，逐步过渡到更高级的主题，例如函数式编程、面向对象设计以及并发编程。

**核心贡献与主要观点：**

本章节的核心贡献在于提供一套系统性的方法论，指导开发者如何写出“有效”的 Python 代码。这不仅仅意味着代码能够运行，更强调代码的质量、效率和可维护性。主要观点包括：

*   **Pythonic 风格的重要性：** 强调遵循 Python 的惯用法（Pythonic way），这能够使代码更具可读性和简洁性。
*   **数据结构的选择与优化：** 深入分析 Python 内置数据结构（如列表、字典、集合、元组）的特性，以及在不同场景下如何选择最合适的数据结构以提高性能。
*   **函数式编程范式：** 介绍 Python 中支持的函数式编程特性，如 lambda 函数、map、filter、reduce，以及它们在简化代码和提高效率方面的作用。
*   **面向对象设计原则：** 探讨类、对象、继承、多态等面向对象概念，并结合设计模式，讲解如何构建模块化、可复用的代码。
*   **并发与并行编程：** 介绍 Python 的 threading 和 multiprocessing 模块，以及 asyncio 库，帮助开发者理解和实现并发和并行操作，以提升程序性能。
*   **高效的代码编写技巧：** 分享一些实用的 Python 编码技巧，如列表推导式、生成器、装饰器等，这些技巧能够显著提高代码的效率和可读性。

**逻辑顺序组织总结：**

本章节将按照以下逻辑顺序组织内容，以确保学习的连贯性和深度：

1.  **Python 基础回顾与进阶：** 从 Python 的基本语法、变量、数据类型开始，快速回顾并引入更高级的概念，如可变与不可变对象、作用域等。
2.  **数据结构精通：** 详细讲解 Python 列表、元组、字典、集合等数据结构的内部机制、性能特点以及最佳实践。
3.  **函数式编程的力量：** 介绍函数作为一等公民的概念，深入探讨 lambda、map、filter、reduce、列表推导式和生成器表达式，以及它们如何简化代码逻辑。
4.  **面向对象编程的艺术：** 讲解类、对象、封装、继承、多态，以及如何利用 Python 的特性实现优雅的面向对象设计，包括魔术方法和属性。
5.  **并发与并行：** 介绍线程、进程和异步编程的概念，以及如何在 Python 中有效地利用它们来处理耗时操作和提高吞吐量。
6.  **代码优化与性能提升：** 探讨代码性能分析工具，以及如何通过算法优化、数据结构选择和 Python 特性来提升代码的执行效率。
7.  **实用的 Python 库与工具：** 简要介绍一些常用的 Python 库（如 itertools, collections）以及代码风格检查工具（如 flake8, black），帮助开发者写出更规范、更高效的代码。

通过本章节的学习，读者将能够更深入地理解 Python 的设计哲学，掌握编写高效、可维护的 Python 代码的关键技巧，从而在实际开发中提升工作效率和代码质量。

## Effective Python - Pythonic Thinking

## Pythonic 思维

编程语言的惯用法由其用户定义。多年来，Python 社区一直使用“Pythonic”这个形容词来描述遵循特定风格的代码。Pythonic 风格不是由编译器强制执行的。它是在使用该语言和与他人合作的经验中随着时间推移而形成的。Python 程序员倾向于明确性，偏爱简单而非复杂，并最大化代码的可读性。（在解释器中输入 `import this` 可以阅读 _The Zen of Python_。）

熟悉其他语言的程序员可能会尝试像编写 C++、Java 或他们最熟悉的语言那样来编写 Python。新程序员可能仍在适应 Python 中可以表达的各种概念。了解 Python 中最常见事情的 _Pythonic_ 方式对你来说很重要。这些模式将影响你编写的每一个程序。

### Item 1: 了解你正在使用的 Python 版本

在本书中，大部分示例代码都是针对 Python 3.13（2024 年 10 月发布）的。本书不涵盖 Python 2，尽管它有时会提及旧版本的 Python 3 来提供语言如何随时间演变的背景信息。

许多计算机操作系统预装了多个标准 CPython 解释器版本。然而，命令行上 `python` 的默认含义可能不清楚。`python` 通常是 `python2.7` 的别名，但有时也可能是更旧版本的别名，如 `python2.6` 或 `python2.5`。要确切了解你正在使用的 Python 版本，可以使用 `--version` 标志：

```
$ python --version
Python 2.7.10
```

在许多系统上，Python 2 已不再安装，`python` 命令会引发错误：

[点击此处查看代码图像](#ch01_images#f0002-01)

```
$ python --version
-bash: python: command not found
```

Python 3 通常以 `python3` 的名称提供：

```
$ python3 --version
Python 3.12.3
```

要使用替代的 Python 运行时，例如 PyPy (<https://www.pypy.org>) 来运行 Python 程序，你需要使用它们的特定命令：

[点击此处查看代码图像](#ch01_images#f0002-02)

```
$ pypy3 --version
Python 3.10.14 (75b3de9d9035, May 28 2024, 18:06:40)
[PyPy 7.3.16 with GCC Apple LLVM 15.0.0 (clang-1500.3.9.4)]
```

你也可以在运行时通过检查 `sys` 内置模块中的值来确定你正在使用的 Python 版本：

[点击此处查看代码图像](#ch01_images#f0002-03)

```python
import sys

print(sys.platform)
print(sys.implementation.name)
print(sys.version_info)
print(sys.version)

>>>
darwin
cpython
sys.version_info(major=3, minor=12, micro=3,
➥releaselevel='final', serial=0)
3.12.3 (main, Apr  9 2024, 08:09:14)
➥[Clang 15.0.0 (clang-1500.3.9.4)]
```

长期以来，Python 核心开发人员和社区一直积极维护对 Python 2 和 Python 3 的支持。这两个版本在重要方面存在差异，并且存在不兼容性，使得迁移变得困难。从版本 2 迁移到版本 3 是一个极其漫长而痛苦的时期，最终于 2020 年 4 月 20 日结束，当时发布了 Python 版本 2.7.18。这是 Python 2 的最后一个官方版本。对于仍需要 Python 2 安全补丁和错误修复的任何人，仅剩的选择是付费给商业软件供应商寻求支持，或者自己动手。

自那时以来，Python 核心开发人员和社区一直专注于 Python 版本 3。核心语言、标准库以及包和工具的生态系统的功能正在不断改进。跟上所有正在发生的改变和创新可能会让人不知所措。了解新内容的一个好方法是阅读发布说明 (<https://docs.python.org/3/whatsnew/index.html>)，其中会重点介绍每个版本的新增功能和更改。还有其他网站会在你依赖的社区包更新时通知你（参见 [Item 116](#ch14#ch14lev1sec1): “[了解社区构建模块的来源](#ch14#ch14lev1sec1)”）。

#### 需牢记的事项
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 3 是最新且支持良好的 Python 版本，你应该在你的项目中使用它。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 确保你系统上运行 Python 的命令行可执行文件是你期望的版本。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 2 已不再由核心开发人员正式维护。

### Item 2: 遵循 PEP 8 风格指南

Python Enhancement Proposal #8，也称为 PEP 8，是关于如何格式化 Python 代码的风格指南。你可以随意以任何你想要的方式编写 Python 代码，只要它具有有效的语法。然而，使用一致的风格可以使你的代码更易于理解和阅读。与更大的 Python 社区中的其他 Python 程序员共享一种通用风格，有助于在项目上进行协作。但即使只有你一个人阅读你的代码，遵循风格指南也能让你以后更容易地更改内容，并有助于避免许多常见错误。

PEP 8 提供了关于如何编写清晰 Python 代码的丰富细节。随着 Python 语言的演变，它会不断更新。值得在线阅读整个指南 (<https://www.python.org/dev/peps/pep-0008/>)。以下是一些你应该遵循的规则。

#### 空格

在 Python 中，空格在语法上很重要。Python 程序员对空格对代码清晰度的影响特别敏感。遵循与空格相关的以下指南：

*   使用空格代替制表符进行缩进。
*   每个语法上重要的缩进级别使用四个空格。
*   行长度应为 79 个字符或更少。
*   长表达式延续到其他行时，应比正常缩进级别多缩进四个空格。
*   在文件中，函数和类之间应用两个空行分隔。
*   在类中，方法之间应用一个空行分隔。
*   在字典中，键和冒号之间不要有空格；如果值适合在同一行，则在相应值之前留一个空格。
*   在变量赋值的 `=` 运算符之前和之后留一个空格，且仅一个。
*   对于类型注解，确保变量名和冒号之间没有空格，并在类型信息前留一个空格。

#### 命名

PEP 8 为语言的不同部分建议了独特的命名风格。这些约定使得在阅读代码时很容易区分哪个类型对应于哪个名称。遵循与命名相关的以下指南：

*   函数、变量和属性应采用 `lowercase_underscore` 格式。
*   受保护的实例属性应采用 `_leading_underscore` 格式。
*   私有的实例属性应采用 `__double_leading_underscore` 格式。
*   类（包括异常）应采用 `CapitalizedWord` 格式。
*   模块级常量应采用 `ALL_CAPS` 格式。
*   类中的实例方法应使用 `self`，它引用对象，作为第一个参数的名称。
*   类方法应使用 `cls`，它引用类，作为第一个参数的名称。

#### 表达式和语句

_The Zen of Python_ 说：“应该有一个——而且最好只有一个——明显的方法来做到这一点。” PEP 8 试图在其关于表达式和语句的指导中将这种风格编码化：

*   使用内联否定（`if a is not b`）而不是否定正表达式（`if not a is b`）。
*   不要通过将长度与零进行比较来检查空容器或序列（如 `[]` 或 `""`）（`if len(somelist) == 0`）。使用 `if not somelist` 并假设空值将隐式求值为 `False`。
*   对于非空容器或序列（如 `[1]` 或 `"hi"`）也是如此。语句 `if somelist` 对于非空值隐式为 `True`。
*   避免单行 `if` 语句、`for` 和 `while` 循环以及 `except` 复合语句。将它们分散到多行以提高清晰度。
*   如果表达式无法在一行中容纳，请用括号将其括起来，并添加换行符和缩进以使其更易于阅读。
*   优先使用括号括起多行表达式，而不是使用 `\` 行续接字符。

#### 导入

PEP 8 建议了一些关于如何导入模块并在代码中使用它们的指南：

*   始终将 `import` 语句（包括 `from x import y`）放在文件顶部。
*   导入模块时，始终使用绝对名称，而不是相对于当前模块自身路径的名称。例如，要在 `bar` 包内导入 `foo` 模块，应使用 `from bar import foo`，而不是仅 `import foo`。
*   如果必须进行相对导入，请使用显式语法 `from . import foo`。
*   导入应按以下顺序分组：标准库模块、第三方模块、自己的模块。每个子组应按字母顺序排列导入。

#### 自动化

如果你读到的内容似乎需要记住很多，那么我有一个好消息：Python 社区正在围绕一个通用的工具来自动进行 PEP 8 格式化：它叫做 `black` (<https://github.com/psf/black>)，它是 Python Software Foundation 的官方项目。`black` 提供的配置选项很少，这使得在同一代码库上工作的开发人员可以轻松地就代码风格达成一致。安装和使用 `black` 非常简单：

```
$ pip install black
$ python -m black example.py
reformatted example.py

All done!
1 file reformatted.
```

除了 `black` 之外，还有许多其他社区工具可以帮助你自动改进源代码。许多 IDE 和编辑器都包含风格检查工具、自动格式化程序和类似的插件。一个流行的代码分析器是 `pylint` (<https://github.com/pylint-dev/pylint>)；它有助于强制执行 PEP 8 风格指南，并检测 Python 程序中的许多其他类型的常见错误（有关更多示例，请参见 [Item 3](#ch01#ch01lev1sec3): “[切勿期望 Python 在编译时检测错误](#ch01#ch01lev1sec3)”）。

#### 需牢记的事项
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 编写 Python 代码时，始终遵循 Python Enhancement Proposal #8 (PEP 8) 风格指南。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 与更大的 Python 社区共享通用风格有助于与他人协作。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用一致的风格可以更轻松地在以后修改自己的代码。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `black` 和 `pylint` 等社区工具可以自动化 PEP 8 的合规性，从而轻松保持源代码的良好风格。

### Item 3: 切勿期望 Python 在编译时检测错误

在加载 Python 程序并准备执行时，源代码会被解析成抽象语法树，并检查明显的结构性错误。例如，一个格式不正确的 `if` 语句将引发 `SyntaxError` 异常，指示代码中的问题所在：

```python
if True  # Bad syntax
print('hello')

>>>
Traceback ...
SyntaxError: expected ':'
```

值字面量中的错误也会被提前检测到并引发异常：

[点击此处查看代码图像](#ch01_images#f0006-01)

```python
1.3j5  # Bad number

>>>
Traceback ...
SyntaxError: invalid imaginary literal
```

不幸的是，在执行之前，你对 Python 的保护就仅限于此了。除了基本的标记化错误和解析错误之外，其他任何问题都不会被标记出来。

即使是看似有明显错误的简单函数，由于 Python 高度动态的特性，也不会在程序执行前报告问题。例如，这里我定义了一个函数，其中 `my_var` 变量在传递给 `print` 之前显然没有被赋值：

```python
def bad_reference():
print(my_var)
my_var = 123
```

但是，直到函数执行时才会引发异常：

[点击此处查看代码图像](#ch01_images#f0007-01)

```python
bad_reference()

>>>
Traceback ...
UnboundLocalError: cannot access local variable 'my_var'
➥where it is not associated with a value
```

这之所以不被认为是 _静态_ 错误，是因为 Python 程序可以动态地赋值局部和全局变量。例如，这里我定义了一个函数，该函数根据输入参数是有效的还是无效的：

```python
def sometimes_ok(x):
if x:
my_var = 123
print(my_var)
```

此调用运行正常：

```python
sometimes_ok(True)

>>>
123
```

此调用会导致运行时异常：

[点击此处查看代码图像](#ch01_images#f0007-02)

```python
sometimes_ok(False)

>>>
Traceback ...
UnboundLocalError: cannot access local variable 'my_var'
➥where it is not associated with a value
```

Python 也不会提前捕获数学错误。看起来这在程序执行前明显是一个错误：

```python
def bad_math():
return 1 / 0
```

但是，除法运算符的含义可能会根据涉及的值而变化，因此类似这样的错误检查同样会推迟到运行时：

[点击此处查看代码图像](#ch01_images#f0008-01)

```python
bad_math()

>>>
Traceback ...
ZeroDivisionError: division by zero
```

Python 也不会静态地检测未定义方法、提供的参数过多或过少、返回类型不匹配以及许多其他看似明显的问题。有一些社区工具可以帮助你在执行前检测其中一些错误，例如 `flake8` linter (<https://github.com/PyCQA/flake8>) 和与 `typing` 内置模块一起使用的类型检查器（参见 [Item 124](#ch14#ch14lev1sec9): “[考虑通过 typing 进行静态分析以避免错误](#ch14#ch14lev1sec9)”）。

最终，在编写惯用的 Python 代码时，你将在运行时遇到大多数错误。Python 语言将运行时灵活性置于编译时错误检测之上。因此，在运行时检查你的假设是否正确（参见 [Item 81](#ch10#ch10lev1sec2): “[断言内部假设并抛出未满足的期望](#ch10#ch10lev1sec2)”）并使用自动化测试验证代码的正确性（参见 [Item 109](#ch13#ch13lev1sec2): “[优先集成测试而非单元测试](#ch13#ch13lev1sec2)”）非常重要。

#### 需牢记的事项
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 将几乎所有的错误检查推迟到运行时，包括检测那些在程序启动时看似显而易见的错误。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 像 linter 和静态分析工具这样的社区项目可以在程序执行前帮助捕获一些最常见的错误源。

### Item 4: 编写辅助函数而非复杂表达式

Python 的简洁语法使得编写实现大量逻辑的单行表达式变得容易。例如，假设我想解码网站 URL 中的查询字符串。这里每个查询字符串参数都代表一个整数值：

[点击此处查看代码图像](#ch01_images#f0009-01)

```python
from urllib.parse import parse_qs

my_values = parse_qs("red=5&blue=0&green=",
keep_blank_values=True)
print(repr(my_values))

>>>
{'red': ['5'], 'blue': ['0'], 'green': ['']}
```

某些查询字符串参数可能具有多个值，有些可能具有单个值，有些可能存在但具有空值，而有些可能完全缺失。使用结果字典上的 `get` 方法将在每种情况下返回不同的值：

[点击此处查看代码图像](#ch01_images#f0009-02)

```python
print("Red:    ", my_values.get("red"))
print("Green:  ", my_values.get("green"))
print("Opacity:", my_values.get("opacity"))

>>>
Red:     ['5']
Green:   ['']
Opacity: None
```

如果参数未提供或为空，则默认值为 `0` 会很好。我最初可能会选择使用布尔表达式来做到这一点，因为我觉得这些逻辑还不值得使用一个完整的 `if` 语句或辅助函数。

Python 的语法使得这个选择变得过于容易。这里的诀窍是，空字符串、空列表和零都隐式地评估为 `False`。因此，当第一个子表达式为 `False` 时，下面的表达式将评估为 `or` 运算符之后的子表达式：

[点击此处查看代码图像](#ch01_images#f0009-03)

```python
# For query string 'red=5&blue=0&green='
red = my_values.get("red", [""])[0] or 0
green = my_values.get("green", [""])[0] or 0
opacity = my_values.get("opacity", [""])[0] or 0
print(f"Red:     {red!r}")
print(f"Green:   {green!r}")
print(f"Opacity: {opacity!r}")

>>>
Red:     '5'
Green:   0
Opacity: 0
```

`red` 情况有效，因为键 `"red"` 存在于 `my_values` 字典中。`get` 方法检索到的值是一个包含一个元素的列表：字符串 `"5"`。通过访问列表中的索引 `0` 来检索此元素。然后 `or` 表达式确定字符串不为空，因此是该操作的结果值。最后，变量 `red` 被赋值为值 `"5"`。

`green` 情况有效，因为 `my_values` 字典中的值是一个包含一个元素的列表：一个空字符串。检索列表中的索引 `0` 处的元素。`or` 表达式确定字符串为空，因此其返回值应该是操作的右侧参数，即 `0`。最后，变量 `green` 被赋值为值 `0`。

`opacity` 情况有效，因为 `my_values` 字典中的值完全缺失。`get` 方法的行为是在字典中找不到键时返回其第二个参数（参见 [Item 26](#ch04#ch04lev1sec2): “[优先使用 get 而非 in 和 KeyError 来处理缺失的字典键](#ch04#ch04lev1sec2)”）。在这种情况下，默认值是一个包含一个元素的列表：一个空字符串。因此，当在字典中找不到 `opacity` 时，此代码与 `green` 情况执行的操作完全相同。

带有 `get`、`[""]`、`[0]` 和 `or` 的复杂表达式很难阅读，而且它仍然不能满足我所有的需求。我还想确保所有参数值都转换为整数，以便我能立即在数学表达式中使用它们。为此，我将每个表达式用 `int` 内置函数包装起来，以将字符串解析为整数：

[点击此处查看代码图像](#ch01_images#f0010-01)

```python
red = int(my_values.get("red", [""])[0] or 0)
```

此逻辑现在极难阅读。存在太多视觉噪音。代码不具可读性。代码的新读者需要花费太多时间来解析表达式以弄清楚它实际做了什么。即使保持简短很好，但尝试将所有内容都放在一行上是不值得的。

虽然 Python 支持条件表达式来实现内联 `if`/`else` 行为，但在这种情况下使用它们会导致代码的可读性比上面的布尔运算符示例好不了多少（参见 [Item 7](#ch01#ch01lev1sec7): “[考虑使用条件表达式进行简单的内联逻辑](#ch01#ch01lev1sec7)”）：

[点击此处查看代码图像](#ch01_images#f0010-02)

```python
red_str = my_values.get("red", [""])
red = int(red_str[0]) if red_str[0] else 0
```

或者，我可以使用完整的 `if` 语句跨越多行来实现相同的逻辑。看到所有步骤都这样分散开，使得密集版本看起来更加复杂：

[点击此处查看代码图像](#ch01_images#f0011-01)

```python
green_str = my_values.get("green", [""])
if green_str[0]:
green = int(green_str[0])
else:
green = 0
```

现在这段逻辑分散在多行中，复制粘贴以赋值其他变量（例如 `red`）会有点困难。如果我需要重复使用此功能——即使只是像本例中那样两三次——那么编写一个辅助函数是最佳选择：

[点击此处查看代码图像](#ch01_images#f0011-02)

```python
def get_first_int(values, key, default=0):
found = values.get(key, [""])
if found[0]:
return int(found[0])
return default
```

调用代码比使用 `or` 的复杂表达式和使用条件表达式的两行版本要清晰得多：

[点击此处查看代码图像](#ch01_images#f0011-03)

```python
green = get_first_int(my_values, "green")
```

一旦你的表达式变得复杂，就该考虑将它们拆分成更小的部分——例如中间变量——并将逻辑移到辅助函数中。你获得的清晰度总是会超过简洁性可能为你带来的好处。避免让 Python 中复杂表达式的简洁语法将你带入这样的混乱之中。遵循 _DRY 原则_：Don't Repeat Yourself（不要重复自己）。

#### 需牢记的事项
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 的语法使得编写过于复杂且难以阅读的单行表达式变得非常容易。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 将复杂表达式移入辅助函数，特别是如果你需要重复使用相同的逻辑。

### Item 5: 优先使用多重赋值解包而非索引

Python 有一个内置的 `tuple` 类型，可用于创建不可变的有序值序列（参见 [Item 56](#ch07#ch07lev1sec9): “[优先使用 dataclasses 创建不可变对象](#ch07#ch07lev1sec9)” 以了解类似的数据结构）。元组可以为空，也可以包含单个元素：

```python
no_snack = ()
snack = ("chips",)
```

元组也可以包含多个元素，如字典中的这些键/值对：

[点击此处查看代码图像](#ch01_images#f0012-01)

```python
snack_calories = {
"chips": 140,
"popcorn": 80,
"nuts": 190,
}
items = list(snack_calories.items())
print(items)

>>>
[('chips', 140), ('popcorn', 80), ('nuts', 190)]
```

元组中的元素可以通过数字索引和切片访问，就像列表一样：

[点击此处查看代码图像](#ch01_images#f0012-02)

```python
item = ("Peanut butter", "Jelly")
first_item = item[0]   # Index
first_half = item[:1]  # Slice
print(first_item)
print(first_half)

>>>
Peanut butter
('Peanut butter',)
```

一旦创建了元组，就不能通过将新值赋给索引来修改它：

[点击此处查看代码图像](#ch01_images#f0012-03)

```python
pair = ("Chocolate", "Peanut butter")
pair[0] = "Honey"

>>>
Traceback ...
TypeError: 'tuple' object does not support item assignment
```

Python 还提供了 _解包_ 语法，它允许在单个语句中赋值多个值。你在解包赋值中指定的模式看起来很像尝试修改元组——这是不允许的——但它们实际上工作方式完全不同。例如，如果你知道一个元组是一个对，那么与其使用索引访问其值，不如将其赋值给两个变量名组成的元组：

[点击此处查看代码图像](#ch01_images#f0013-01)

```python
item = ("Peanut butter", "Jelly")
first, second = item  # Unpacking
print(first, "and", second)

>>>
Peanut butter and Jelly
```

解包比访问元组的索引具有更少的视觉噪音，并且通常需要更少的代码行。相同的模式匹配解包语法也适用于赋值给列表、序列以及可迭代对象内的多级任意可迭代对象。我不建议在你的代码中这样做，但了解它是可能的以及它是如何工作的很重要：

[点击此处查看代码图像](#ch01_images#f0013-02)

```python
favorite_snacks = {
"salty": ("pretzels", 100),
"sweet": ("cookies", 180),
"veggie": ("carrots", 20),
}
((type1, (name1, cals1)),
(type2, (name2, cals2)),
(type3, (name3, cals3))) = favorite_snacks.items()

print(f"Favorite {type1} is {name1} with {cals1} calories")
print(f"Favorite {type2} is {name2} with {cals2} calories")
print(f"Favorite {type3} is {name3} with {cals3} calories")

>>>
Favorite salty is pretzels with 100 calories
Favorite sweet is cookies with 180 calories
Favorite veggie is carrots with 20 calories
```

Python 的新手可能会惊讶地发现，解包甚至可以用于原地交换值，而无需创建临时变量。这里我使用典型的语法和索引作为升序排序算法的一部分，在列表的两个位置之间交换值：

[点击此处查看代码图像](#ch01_images#f0013-03)

```python
def bubble_sort(a):
for _ in range(len(a)):
for i in range(1, len(a)):
if a[i] < a[i - 1]:
temp = a[i]
a[i] = a[i - 1]
a[i - 1] = temp

names = ["pretzels", "carrots", "arugula", "bacon"]
bubble_sort(names)
print(names)

>>>
['arugula', 'bacon', 'carrots', 'pretzels']
```

然而，使用解包语法，可以在一行中交换索引：

[点击此处查看代码图像](#ch01_images#f0014-01a)

```python
def bubble_sort(a):
for _ in range(len(a)):
for i in range(1, len(a)):
if a[i] < a[i - 1]:
a[i - 1], a[i] = a[i], a[i - 1]  # Swap

names = ["pretzels", "carrots", "arugula", "bacon"]
bubble_sort(names)
print(names)

>>>
['arugula', 'bacon', 'carrots', 'pretzels']
```

此交换的工作方式是，首先评估赋值的右侧（`a[i], a[i-1]`），并将其值放入一个新的临时、未命名元组中（例如，在循环的第一次迭代中为 `("carrots", "pretzels")`）。然后，使用赋值左侧（`a[i-1], a[i]`）的解包模式来接收该 `tuple` 值并将其分别赋值给变量名 `a[i-1]` 和 `a[i]`。这会将索引 `0` 处的 `"pretzels"` 替换为 `"carrots"`，并将索引 `1` 处的 `"carrots"` 替换为 `"pretzels"`。最后，临时未命名元组会悄悄消失。

解包的另一个有价值的应用是在 `for` 循环和类似结构的目标列表中，例如推导式和生成器表达式（参见 [Item 40](#ch06#ch06lev1sec1): “[使用推导式代替 map 和 filter](#ch06#ch06lev1sec1)” 和 [Item 44](#ch06#ch06lev1sec5): “[考虑使用生成器表达式处理大型列表推导式](#ch06#ch06lev1sec5)”）。例如，这里我迭代零食列表而不使用解包：

[点击此处查看代码图像](#ch01_images#f0014-02)

```python
snacks = [("bacon", 350), ("donut", 240), ("muffin", 190)]
for i in range(len(snacks)):
item = snacks[i]
name = item[0]
calories = item[1]
print(f"#{i+1}: {name} has {calories} calories")

>>>
#1: bacon has 350 calories
#2: donut has 240 calories
#3: muffin has 190 calories
```

这可行，但很冗长。为了索引 `snacks` 结构的各个级别，需要很多额外的字符。现在我通过使用解包和 `enumerate` 内置函数来实现相同的输出（参见 [Item 17](#ch03#ch03lev1sec1): “[优先使用 enumerate 代替 range](#ch03#ch03lev1sec1)”）：

[点击此处查看代码图像](#ch01_images#f0015-02)

```python
for rank, (name, calories) in enumerate(snacks, 1):
print(f"#{rank}: {name} has {calories} calories")

>>>
#1: bacon has 350 calories
#2: donut has 240 calories
#3: muffin has 190 calories
```

这是编写此类循环的 Pythonic 方式；它简短且易于理解。通常不需要通过索引来访问任何内容。

Python 为 `list` 构建（参见 [Item 16](#ch02#ch02lev1sec7): “[优先使用捕获所有解包代替切片](#ch02#ch02lev1sec7)）、函数参数（参见 [Item 34](#ch05#ch05lev1sec5): “[使用可变位置参数减少视觉噪音](#ch05#ch05lev1sec5)）、关键字参数（参见 [Item 35](#ch05#ch05lev1sec6): “[使用关键字参数提供可选行为](#ch05#ch05lev1sec6)）、多个返回值（参见 [Item 31](#ch05#ch05lev1sec2): “[返回专用结果对象而不是要求函数调用者解包超过三个变量](#ch05#ch05lev1sec2)）、结构化模式匹配（参见 [Item 9](#ch01#ch01lev1sec9): “[考虑使用 match 进行流控制中的解构；当 if 语句足够时避免使用](#ch01#ch01lev1sec9)）等等，提供了额外的解包功能。

明智地使用解包可以让你在可能的情况下避免索引，从而使代码更清晰、更 Pythonic。然而，这些功能并非没有需要考虑的陷阱（参见 [Item 6](#ch01#ch01lev1sec6): “[始终用括号括起单元素元组](#ch01#ch01lev1sec6)）。解包也不能在赋值表达式中使用（参见 [Item 8](#ch01#ch01lev1sec8): “[使用赋值表达式防止重复](#ch01#ch01lev1sec8)）。

#### 需牢记的事项
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 有一种称为解包的特殊语法，用于在单个语句中赋值多个值。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 解包在 Python 中是通用的，可以应用于任何可迭代对象，包括可迭代对象内的多级可迭代对象。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 通过使用解包来避免显式索引序列，可以减少视觉噪音并提高代码清晰度。

### Item 6: 始终用括号括起单元素元组

在 Python 中，有四种元组字面量值。第一种是包含在圆括号内的逗号分隔的项目列表：

```python
first = (1, 2, 3)
```

第二种与第一种类似，但包含一个可选的尾随逗号，这使得在跨越多行时保持一致性并方便编辑：

```python
second = (1, 2, 3,)
second_wrapped = (
1,
2,
3,  # Optional comma
)
```

第三种是没有圆括号的逗号分隔的项目列表：

```python
third = 1, 2, 3
```

最后，第四种与第三种类似，但包含一个可选的尾随逗号：

```python
fourth = 1, 2, 3,
```

Python 将所有这些构造视为相同的值：

[点击此处查看代码图像](#ch01_images#f0016-01)

```python
assert first == second == third == fourth
```

然而，在创建元组时还有三个特殊情况需要考虑。第一种情况是空元组，它只是圆括号：

```python
empty = ()
```

第二种特殊情况是单元素元组的形式：你必须包含一个尾随逗号。如果你省略尾随逗号，那么你得到的是一个带括号的表达式而不是元组：

[点击此处查看代码图像](#ch01_images#f0016-02)

```python
single_with = (1,)
single_without = (1)
assert single_with != single_without
assert single_with[0] == single_without
```

第三种特殊情况与第二种类似，只是没有圆括号：

[点击此处查看代码图像](#ch01_images#f0017-01)

```python
single_parens = (1,)
single_no_parens = 1,
assert single_parens == single_no_parens
```

这种第三种特殊情况——没有圆括号的尾随逗号——可能会导致难以诊断的意外问题。考虑来自电子商务网站的一个难以发现 bug 的函数调用：

[点击此处查看代码图像](#ch01_images#f0017-02)

```python
to_refund = calculate_refund(
get_order_value(user, order.id),
get_tax(user.address, order.dest),
adjust_discount(user) + 0.1),
```

你可能期望返回类型是整数、浮点数或包含要退还给客户的金额的十进制数。但实际上，它是一个元组！

```python
print(type(to_refund))

>>>
<class 'tuple'>
```

问题在于最后一行末尾多余的逗号。删除逗号可以修复代码：

[点击此处查看代码图像](#ch01_images#f0017-03)

```pythonpython
to_refund2 = calculate_refund(
get_order_value(user, order.id),
get_tax(user.address, order.dest),
adjust_discount(user) + 0.1)  # No trailing comma

print(type(to_refund2))

>>>
<class 'int'>
```

这样的逗号字符可能会意外地插入到你的代码中，导致行为改变，即使仔细检查也很难追踪。错误的分隔符也可能是在编辑元组、列表、集合或函数调用中的项目后遗留下来的，并且忘记删除遗留的逗号。这种情况发生的频率比你预期的要高！

没有圆括号的单元素元组的另一个问题是，它们不能轻易地从赋值移动到表达式中。例如，如果我想将单元素元组 `1,` 复制到一个列表中，我必须用圆括号将其括起来。如果我忘记这样做，我最终会向周围的表单传递比元组更多的项目或参数：

[点击此处查看代码图像](#ch01_images#f0018-01)

```python
value_a = 1,    # No parentheses, right
list_b = [1,]   # No parentheses, wrong
list_c = [(1,)] # Parentheses, right
print('A:', value_a)
print('B:', list_b)
print('C:', list_c)

>>>
A: (1,)
B: [1]
C: [(1,)]
```

单元素元组也可以作为解包语法的一部分出现在赋值的左侧（参见 [Item 5](#ch01#ch01lev1sec5): “[优先使用多重赋值解包而非索引](#ch01#ch01lev1sec5)、” [Item 31](#ch05#ch05lev1sec2): “[返回专用结果对象而不是要求函数调用者解包超过三个变量](#ch05#ch05lev1sec2)、” 和 [Item 16](#ch02#ch02lev1sec7): “[优先使用捕获所有解包代替切片](#ch02#ch02lev1sec7)）。令人惊讶的是，所有这些赋值都是允许的，具体取决于返回的值，但它们会产生三种不同的结果：

[点击此处查看代码图像](#ch01_images#f0018-02)

```python
def get_coupon_codes(user):
...
return [['DEAL20']]
...

(a1,), = get_coupon_codes(user)
(a2,) = get_coupon_codes(user)
(a3), = get_coupon_codes(user)
(a4) = get_coupon_codes(user)
a5, = get_coupon_codes(user)
a6 = get_coupon_codes(user)

assert a1 not in (a2, a3, a4, a5, a6)
assert a2 == a3 == a5
assert a4 == a6
```

有时自动源代码格式化工具（参见 [Item 2](#ch01#ch01lev1sec2): “[遵循 PEP 8 风格指南](#ch01#ch01lev1sec2)”）和静态分析工具（参见 [Item 3](#ch01#ch01lev1sec3): “[切勿期望 Python 在编译时检测错误](#ch01#ch01lev1sec3)”）可以使尾随逗号问题更加明显。但通常它会被忽略，直到程序或测试套件开始表现异常。避免这种情况的最佳方法是始终用圆括号括起单元素元组，无论它们是在赋值的左侧还是右侧。

#### 需牢记的事项
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 中的元组字面量值可以具有可选的圆括号和可选的尾随逗号，除了少数特殊情况。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 单元素元组在其包含的唯一元素后需要一个尾随逗号，并且可以有可选的圆括号。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在表达式末尾出现多余的尾随逗号非常容易，这会将表达式的含义更改为单元素元组，从而破坏程序。

### Item 7: 考虑使用条件表达式进行简单的内联逻辑

Python 的 `if` 语句不是表达式。`if` 块、`elif` 块和 `else` 块都可以包含多个其他语句。整个块组不评估为单个值，该值可以存储在变量中或作为函数参数传递。

Python 还支持 _条件表达式_，它允许你在表达式允许的几乎任何地方插入 `if`/`elif`/`else` 行为。例如，这里我使用条件表达式根据布尔测试为变量赋值：

[点击此处查看代码图像](#ch01_images#f0019-01)

```python
i = 3
x = "even" if i % 2 == 0 else "odd"
print(x)

>>>
odd
```

这种表达式结构似乎很方便，特别是对于一次性使用，并且让人想起你可能从 C 和其他语言中知道的 _三元运算符_（例如，`condition ? true_value : false_value`）。对于像这样的简单赋值，甚至在函数调用参数列表中（例如 `my_func(1 if x else 2)`），条件表达式都可以是平衡简洁性和代码灵活性的好选择。

重要的是要注意 Python 中的条件表达式与 C 等语言中的三元运算符的一个关键区别：在 C 中，测试表达式在前；在 Python 中，当测试表达式为真时要评估的表达式在前。例如，你可能期望以下代码调用 `fail` 函数并引发异常；相反，由于测试条件为 `False`，`fail` 函数从未执行：

```python
def fail():
raise Exception("Oops")

x = fail() if False else 20
print(x)

>>>
20
```

Python 推导式中的 `if` 子句具有类似的语法和行为用于过滤（参见 [Item 40](#ch06#ch06lev1sec1): “[使用推导式代替 map 和 filter](#ch06#ch06lev1sec1)” 和 [Item 44](#ch06#ch06lev1sec5): “[考虑使用生成器表达式处理大型列表推导式](#ch06#ch06lev1sec5)”）。例如，这里我在列表推导式中使用 `if` 子句，在计算结果列表时仅包含 `x` 的偶数值：

[点击此处查看代码图像](#ch01_images#f0020-01)

```python
result = [x / 4 for x in range(10) if x % 2 == 0]
print(result)

>>>
[0.0, 0.5, 1.0, 1.5, 2.0]
```

要评估的表达式（`x / 4`）位于 `if` 测试表达式（`x % 2 == 0`）之前，就像在条件表达式中一样。

在 Python 中可用条件表达式之前，人们有时会使用布尔逻辑来实现类似的行为（有关详细信息，请参见 [Item 4](#ch01#ch01lev1sec4): “[编写辅助函数而非复杂表达式](#ch01#ch01lev1sec4)”）。例如，以下表达式等同于上面的条件表达式：

[点击此处查看代码图像](#ch01_images#f0020-02)

```python
x = (i % 2 == 0 and "even") or "odd"
```

这种逻辑形式非常令人困惑，因为你需要知道 `and` 返回第一个假值或最后一个真值，而 `or` 返回第一个真值或最后一个假值（有关详细信息，请参见 [Item 23](#ch03#ch03lev1sec7): “[将迭代器传递给 any 和 all 以实现高效的短路逻辑](#ch03#ch03lev1sec7)”）。

此外，使用布尔运算符的方法在你想返回一个假值作为真条件的结果时不起作用（例如，`x = (i % 2 == 0 and []) or [1]` 始终评估为 `[1]`）。这一切都晦涩难懂且容易出错，这也是条件表达式被添加到语言中的原因之一。

现在考虑将与前面单行示例相同的逻辑作为四行 `if` 语句：

```python
if i % 2 == 0:
x = "even"
else:
x = "odd"
```

虽然这更长，但它可能更好，原因有几个。首先，如果我以后想在每个条件分支中做更多的事情，比如打印调试信息，我可以在不更改代码结构的情况下做到：

[点击此处查看代码图像](#ch01_images#f0021-01)

```python
if i % 2 == 0:
x = "even"
print("It was even!")  # Added
else:
x = "odd"
```

我也可以在同一个语句中插入额外的分支，使用 `elif` 块：

```python
if i % 2 == 0:
x = "even"
elif i % 3 == 0:  # Added
x = "divisible by three"
else:
x = "odd"
```

如果我确实需要简洁并将其逻辑放在一个表达式中，我可以通过将其全部移到一个我内联调用的辅助函数中来实现：

[点击此处查看代码图像](#ch01_images#f0021-02)

```python
def number_group(i):
if i % 2 == 0:
return "even"
else:
return "odd"

x = number_group(i)  # Short call
```

作为额外的优势，辅助函数可以在多个地方重用，而不是像条件表达式那样一次性使用。

你应该使用条件表达式、完整的 `if` 语句还是包装在辅助函数中的 `if` 语句，这取决于具体情况。

当条件表达式必须跨越多行时，你应该避免使用它们。例如，这里的函数调用非常长，以至于条件表达式必须用周围的括号进行换行：

[点击此处查看代码图像](#ch01_images#f0021-03)

```python
x = (my_long_function_call(1, 2, 3) if i % 2 == 0
else my_other_long_function_call(4, 5, 6))
```

这非常难以阅读。而且，如果你应用自动格式化程序（参见 [Item 2](#ch01#ch01lev1sec2): “[遵循 PEP 8 风格指南](#ch01#ch01lev1sec2)”）到这段代码，条件表达式很可能会被重写为比标准 `if`/`else` 语句使用更多的代码行：

[点击此处查看代码图像](#ch01_images#f0022-01)

```python
x = (
my_long_function_call(1, 2, 3)
if i % 2 == 0
else my_other_long_function_call(4, 5, 6)
)
```

另一个需要与条件表达式进行比较的 Python 语言特性是赋值表达式（参见 [Item 8](#ch01#ch01lev1sec8): “[使用赋值表达式防止重复](#ch01#ch01lev1sec8)），它也允许在表达式中使用语句类行为。关键区别在于，当赋值表达式用在模糊的上下文中时，它们必须用括号括起来；条件表达式不需要周围的括号，缺少括号会损害可读性。

例如，允许使用括号括起赋值表达式的这个 `if` 语句：

```python
x = 2
y = 1

if x and (z := x > y):
...
```

但是这个没有括号的 `if` 语句是一个语法错误：

[点击此处查看代码图像](#ch01#f0022-02a)

```python
if x and z := x > y:
...

>>>
Traceback ...
SyntaxError: cannot use assignment expressions with expression
```

对于条件表达式，不需要括号。由于这两种形式都允许，因此很难弄清楚程序员的原始意图：

[点击此处查看代码图像](#ch01_images#f0022-02)

```python
if x > y if z else w:    # Ambiguous
...

if x > (y if z else w):  # Clear
...
```

赋值表达式在用作函数调用参数列表时也需要周围的括号：

```python
z = dict(
your_value=(y := 1),
)
```

省略括号是语法错误：

```python
w = dict(
other_value=y := 1,
)

>>>
Traceback ...
SyntaxError: invalid syntax
```

相比之下，条件表达式在此上下文中不需要周围的括号，并且缺少括号会使代码更嘈杂且难以阅读：

```python
v = dict(
my_value=1 if x else 3,
)
```

底线：运用你的判断。在许多情况下，条件表达式可能很有价值并提高清晰度。有时它们与周围的括号一起使用更好，有时则不然。条件表达式很容易被过度使用，从而编写出晦涩难懂、新读者难以理解的代码。如有疑问，请选择标准的 `if` 语句。

#### 需牢记的事项
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 中的条件表达式允许你在几乎任何表达式通常出现的地方放置一个 `if` 语句。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 条件表达式中的测试表达式、真结果表达式和假结果表达式的顺序与 C 等语言中的三元运算符的顺序不同。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 不要将条件表达式用于会增加歧义或损害代码新读者可读性的地方。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 当不清楚条件表达式是否提供令人信服的好处时，优先使用标准的 `if` 语句和辅助函数。

### Item 8: 使用赋值表达式防止重复

赋值表达式——也称为 _海象运算符_——是 Python 3.8 中引入的一项新语法功能，用于解决语言中一个长期存在的问题，该问题可能导致代码重复。普通赋值语句写为 `a = b` 并读作“a 等于 b”，而这些赋值写为 `a := b` 并读作“a _海象_ b”（因为 `:=` 看起来像一对眼睛和獠牙）。

赋值表达式很有用，因为它们允许你在不允许赋值语句的地方赋值变量，例如 `if` 语句的测试表达式中。赋值表达式的值将评估为已赋给海象运算符左侧标识符的任何内容。

例如，假设我有一个新鲜水果篮，我正在为一家果汁吧管理。这里我定义了篮子的内容：

```python
fresh_fruit = {
"apple": 10,
"banana": 8,
"lemon": 5,
}
```

当顾客来柜台点柠檬水时，我需要确保篮子里至少有一个柠檬可以挤。这里我通过检索柠檬的数量，然后使用 `if` 语句检查非零值来做到这一点：

[点击此处查看代码图像](#ch01_images#f0024-01)

```python
def make_lemonade(count):
...

def out_of_stock():
...

count = fresh_fruit.get("lemon", 0)
if count:
make_lemonade(count)
else:
out_of_stock()

>>>
Making 5 lemons into lemonade
```

这段看似简单的代码的问题在于它比必需的更冗长。`count` 变量仅在 `if` 语句的第一个块中使用。在 `if` 语句上方定义 `count` 会使其显得比实际重要——就好像所有后续代码，包括 `else` 块，都需要访问 `count` 变量一样，但事实并非如此。

这种获取值、检查其是否为真，然后使用它的模式在 Python 中非常常见。许多程序员试图通过各种损害可读性的技巧来解决对 `count` 的多次引用（参见 [Item 4](#ch01#ch01lev1sec4): “[编写辅助函数而非复杂表达式](#ch01#ch01lev1sec4)” 和 [Item 7](#ch01#ch01lev1sec7): “[考虑使用条件表达式进行简单的内联逻辑](#ch01#ch01lev1sec7)）。幸运的是，赋值表达式被添加到语言中以简化此类代码。这里我使用海象运算符重写了上面的示例：

[点击此处查看代码图像](#ch01_images#f0025-01)

```python
if count := fresh_fruit.get("lemon", 0):
make_lemonade(count)
else:
out_of_stock()
```

虽然这只少了一行代码，但它更具可读性，因为它现在清楚 `count` 只与 `if` 语句的第一个块相关。赋值表达式首先将值赋给 `count` 变量，然后在 `if` 语句的上下文中评估该值以确定如何继续进行流程控制。这种两步行为——赋值然后评估——是海象运算符的基本性质。

柠檬非常浓烈，所以我的柠檬水配方只需要一个，这意味着非零、真值检查就足够了。但是，如果顾客点了苹果酒，我需要确保我有至少四个苹果。这里我通过从 `fresh_fruit` 字典中获取 `count` 值，然后在 `if` 语句的测试表达式中使用比较来做到这一点：

[点击此处查看代码图像](#ch01_images#f0025-02)

```python
def make_cider(count):
...

count = fresh_fruit.get("apple", 0)
if count >= 4:
make_cider(count)
else:
out_of_stock()

>>>
Making cider with 10 apples
```

这与柠檬水示例存在同样的问题，即 `count` 的赋值对该变量产生了分散注意力的强调。这里我通过也使用海象运算符来提高此代码的清晰度：

[点击此处查看代码图像](#ch01_images#f0026-01)

```python
if (count := fresh_fruit.get("apple", 0)) >= 4:
make_cider(count)
else:
out_of_stock()
```

这如预期般工作，并使代码少了一行。值得注意的是，我需要用括号将赋值表达式括起来才能将其与 `if` 语句中的 `4` 进行比较。在柠檬水示例中，不需要周围的括号，因为赋值表达式本身就是一个非零、真值检查；它不是更大表达式的子表达式。与其他表达式一样，你应该避免在可能的情况下用括号括起赋值表达式，以减少视觉噪音。

这种重复模式的另一个常见变体是，当需要根据某些条件在封闭作用域中赋值一个变量，然后不久后在函数调用中引用该变量时。例如，假设一位顾客点了香蕉奶昔。为了制作它们，我需要至少两份香蕉切片，否则会引发 `OutOfBananas` 异常。这里我以典型方式实现此逻辑：

[点击此处查看代码图像](#ch01_images#f0026-02)

```python
def slice_bananas(count):
...

class OutOfBananas(Exception):
pass

def make_smoothies(count):
...

pieces = 0
count = fresh_fruit.get("banana", 0)
if count >= 2:
pieces = slice_bananas(count)

try:
smoothies = make_smoothies(pieces)
except OutOfBananas:
out_of_stock()

>>>
Slicing 8 bananas
Making smoothies with 32 banana slices
```

另一种常见的做法是将 `pieces = 0` 赋值放在 `else` 块中：

[点击此处查看代码图像](#ch01_images#f0027-01)

```python
count = fresh_fruit.get("banana", 0)
if count >= 2:
pieces = slice_bananas(count)
else:
pieces = 0  # Moved

try:
smoothies = make_smoothies(pieces)
except OutOfBananas:
out_of_stock()
```

第二种方法可能感觉很奇怪，因为它意味着 `pieces` 变量有两个不同的位置——在 `if` 语句的每个块中——它可以在那里被初始定义。这种分裂定义在技术上是可行的，因为 Python 的作用域规则（参见 [Item 33](#ch05#ch05lev1sec4): “[了解闭包如何与变量作用域和 nonlocal 交互](#ch05#ch05lev1sec4)”），但它不易阅读或发现，这就是为什么许多人更喜欢上面的构造，其中 `pieces = 0` 赋值在前。

海象运算符可以用来将此示例缩短一行代码。这个小的改变消除了对 `count` 变量的任何强调。现在更清楚的是，`pieces` 在 `if` 语句之外也很重要：

[点击此处查看代码图像](#ch01_images#f0027-02)

```pythonpython
pieces = 0
if (count := fresh_fruit.get("banana", 0)) >= 2:  # Changed
pieces = slice_bananas(count)

try:
smoothies = make_smoothies(pieces)
except OutOfBananas:
out_of_stock()
```

使用海象运算符还可以提高将 `pieces` 的定义分散到 `if` 语句的两个部分中的可读性。当 `count` 定义不再位于 `if` 语句之前时，更容易追踪 `pieces` 变量：

[点击此处查看代码图像](#ch01_images#f0027-03)

```pythonpython
if (count := fresh_fruit.get("banana", 0)) >= 2:
pieces = slice_bananas(count)
else:
pieces = 0  # Moved

try:
smoothies = make_smoothies(pieces)
except OutOfBananas:
out_of_stock()
```

Python 新手程序员的一个常见不满是缺乏灵活的 `switch`/`case` 语句。近似这种功能类型的通用样式是具有深度嵌套的多个 `if`、`elif` 和 `else` 块。

例如，想象一下我想实现一个优先级系统，以便每个客户自动获得最好的可用果汁，而无需点单。这里我定义了逻辑，以便先提供香蕉奶昔，然后是苹果酒，最后是柠檬水：

[点击此处查看代码图像](#ch01_images#f0028-02)

```pythonpython
count = fresh_fruit.get("banana", 0)
if count >= 2:
pieces = slice_bananas(count)
to_enjoy = make_smoothies(pieces)
else:
count = fresh_fruit.get("apple", 0)
if count >= 4:
to_enjoy = make_cider(count)
else:
count = fresh_fruit.get("lemon", 0)
if count:
to_enjoy = make_lemonade(count)
else:
to_enjoy = "Nothing"
```

像这样的丑陋构造在 Python 代码中很常见。幸运的是，海象运算符提供了一种优雅的解决方案，其功能几乎可以与专用的 `switch`/`case` 语句语法相媲美：

[点击此处查看代码图像](#ch01_images#f0028-03)

```pythonpython
if (count := fresh_fruit.get("banana", 0)) >= 2:
pieces = slice_bananas(count)
to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get("apple", 0)) >= 4:
to_enjoy = make_cider(count)
elif count := fresh_fruit.get("lemon", 0):
to_enjoy = make_lemonade(count)
else:
to_enjoy = "Nothing"
```

使用赋值表达式的版本比原始版本只短了五行，但由于嵌套和缩进的减少，可读性的提高是巨大的。如果你在代码中看到以前的丑陋构造，我建议你如果可能的话将其移至使用海象运算符（参见 [Item 9](#ch01#ch01lev1sec9): “[考虑使用 match 进行流控制中的解构；当 if 语句足够时避免使用](#ch01#ch01lev1sec9)” 以了解另一种方法）。

另一个 Python 新手程序员的常见挫败感是缺乏 `do`/`while` 循环结构。例如，假设我想在收到新水果时装瓶果汁，直到没有水果为止。这里我使用 `while` 循环来实现此逻辑：

[点击此处查看代码图像](#ch01_images#f0029-01)

```pythonpython
def pick_fruit():
...

def make_juice(fruit, count):
...

bottles = []
fresh_fruit = pick_fruit()
while fresh_fruit:
for fruit, count in fresh_fruit.items():
batch = make_juice(fruit, count)
bottles.extend(batch)
fresh_fruit = pick_fruit()
```

这是重复的，因为它需要两次单独的 `fresh_fruit = pick_fruit()` 调用：一次在循环之前设置初始条件，另一次在循环结束时补充已送达的水果列表。

一种改进此情况下的代码重用策略是使用 _循环半段_（loop-and-a-half）惯用法。这消除了冗余行，但它也通过使 `while` 循环成为一个简单的无限循环来破坏其贡献。现在循环的所有流程控制都取决于条件 `break` 语句：

[点击此处查看代码图像](#ch01_images#f0029-02)

```pythonpython
bottles = []
while True:                     # Loop
fresh_fruit = pick_fruit()
if not fresh_fruit:         # And a half
break
for fruit, count in fresh_fruit.items():
batch = make_juice(fruit, count)
bottles.extend(batch)
```

海象运算符通过允许 `fresh_fruit` 变量在每次 `while` 循环时被重新赋值和条件评估，从而消除了对循环半段（loop-and-a-half）惯用法的需求。此解决方案简短易读，并且应该是你代码中的首选方法：

[点击此处查看代码图像](#ch01_images#f0030-01)

```pythonpython
bottles = []
while fresh_fruit := pick_fruit():  # Changed
for fruit, count in fresh_fruit.items():
batch = make_juice(fruit, count)
bottles.extend(batch)
```

在许多其他情况下，赋值表达式可用于消除重复（有关示例，请参见 [Item 42](#ch06#ch06lev1sec3): “[使用赋值表达式减少推导式中的重复](#ch06#ch06lev1sec3)”）。总的来说，当你发现自己在代码行的分组中多次重复相同的表达式或赋值时，就该考虑使用赋值表达式来提高可读性。

#### 需牢记的事项
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 赋值表达式使用海象运算符（`:=`）在一个表达式中同时赋值和评估变量名，从而减少重复。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 当赋值表达式是更大表达式的子表达式时，它必须用括号括起来。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 尽管 Python 中没有 `switch`/`case` 语句和 `do`/`while` 循环，但可以通过使用赋值表达式更清晰地模拟它们的功能。

### Item 9: 考虑 `match` 进行流控制中的解构；当 `if` 语句足够时避免使用

`match` 语句是一项相对较新的 Python 功能，在 3.10 版本中引入。由于其众多不同的功能，`match` 的学习曲线非常陡峭：它感觉像是嵌入 Python 中的另一个迷你语言，类似于推导式的独特人体工程学（参见 [Item 40](#ch06#ch06lev1sec1): “[使用推导式代替 map 和 filter](#ch06#ch06lev1sec1)” 和 [Item 44](#ch06#ch06lev1sec5): “[考虑使用生成器表达式处理大型列表推导式](#ch06#ch06lev1sec5)）。乍一看，`match` 语句似乎为 Python 提供了长期以来一直渴望的行为，类似于其他编程语言中的 switch 语句（参见 [Item 8](#ch01#ch01lev1sec8): “[使用赋值表达式防止重复](#ch01#ch01lev1sec8)” 以了解另一种方法）。

例如，假设我正在编写一个车辆辅助程序，该程序响应交通信号灯的颜色。这里我为此目的使用了一个简单的 Python `if` 语句：

[点击此处查看代码图像](#ch01_images#f0031-01)

```python
def take_action(light):
if light == "red":
print("Stop")
elif light == "yellow":
print("Slow down")
elif light == "green":
print("Go!")
else:
raise RuntimeError
```

我可以确认此函数按预期工作：

```python
take_action("red")
take_action("yellow")
take_action("green")

>>>
Stop
Slow down
Go!
```

要使用 `match` 语句，我可以创建与每个 `if`、`elif` 和 `else` 条件对应的 `case` 子句：

[点击此处查看代码图像](#ch01_images#f0031-03)

```pythonpython
def take_match_action(light):
match light:
case "red":
print("Stop")
case "yellow":
print("Slow down")
case "green":
print("Go!")
case _:
raise RuntimeError
```

使用 `match` 语句似乎比使用 `if` 语句更好，因为我可以删除对 `light` 变量的重复引用，并且可以省略每个条件分支的 `==` 运算符。然而，这段代码仍然不理想，因为它将字符串字面量用于所有内容。为了解决这个问题，我通常会做的是在模块级别为每种灯光颜色创建一个常量，并修改代码以使用它们，如下所示：

[点击此处查看代码图像](#ch01_images#f0032-01)

```python
# Added these constants
RED = "red"
YELLOW = "yellow"
GREEN = "green"

def take_constant_action(light):
match light:
case RED:               # Changed
print("Stop")
case YELLOW:            # Changed
print("Slow down")
case GREEN:             # Changed
print("Go!")
case _:
raise RuntimeError

>>>
Traceback ...
SyntaxError: name capture 'RED' makes remaining patterns
➥unreachable
```

不幸的是，这段代码有一个错误——而且是一个晦涩的错误。问题在于 `match` 语句假定 `case` 关键字后面的简单变量名是 _捕获模式_。为了说明这一点，这里我缩短了 `match` 语句，使其只有一个应该匹配 `RED` 的分支：

[点击此处查看代码图像](#ch01_images#f0032-02)

```pythonpython
def take_truncated_action(light):
match light:
case RED:
print("Stop")
```

现在我通过传递 `GREEN` 来调用函数。我期望首先评估 `match light` 子句，并且当前作用域中的 `light` 变量查找将解析为 `"green"`。接下来，我期望评估 `case RED` 子句，并且 `RED` 变量查找将解析为 `"red"`。这两个值不匹配（即 `"green"` vs `"red"`），因此我期望没有输出：

```pythonpython
take_truncated_action(GREEN)

>>>
Stop
```

令人惊讶的是，`match` 语句执行了 `RED` 分支。这里我使用 `print` 来找出正在发生的事情：

[点击此处查看代码图像](#ch01_images#f0033-01)

```pythonpython
def take_debug_action(light):
match light:
case RED:
print(f"{RED=}, {light=}")

take_debug_action(GREEN)

>>>
RED='green', light='green'
```

`case` 子句没有查找 `RED` 的值。相反，它将 `RED` 赋值给了 `light` 变量的值！`match` 语句的作用类似于解包的行为（参见 [Item 5](#ch01#ch01lev1sec5): “[优先使用多重赋值解包而非索引](#ch01#ch01lev1sec5)）。与其说 `case RED` 翻译为 `light == RED`，不如说 Python 判断多重赋值 `(RED,) = (light,)` 是否会执行而不会出错，类似于：

[点击此处查看代码图像](#ch01_images#f0033-02)

```pythonpython
def take_unpacking_action(light):
try:
(RED,) = (light,)
except TypeError:
# Did not match
...
else:
# Matched
print(f"{RED=}, {light=}")
```

上面出现的原始语法错误是因为 Python 在编译时确定赋值 `(RED,) = (light,)` 对于任何 `light` 值都将起作用，因此后续的 `case YELLOW` 和 `case GREEN` 子句是不可达的。

一种解决此问题的方法是确保 `case` 子句的变量引用中包含 `.` 字符。点运算符的存在会导致 Python 查找属性并执行相等性测试，而不是将变量名视为捕获模式。例如，这里我通过使用 `enum` 内置模块和点运算符来访问每个常量名称，从而实现了预期的行为：

[点击此处查看代码图像](#ch01_images#f0033-03)

```pythonpython
import enum                     # Added

class ColorEnum(enum.Enum):     # Added
RED = "red"
YELLOW = "yellow"
GREEN = "green"

def take_enum_action(light):
match light:
case ColorEnum.RED:     # Changed
print("Stop")
case ColorEnum.YELLOW:  # Changed
print("Slow down")
case ColorEnum.GREEN:   # Changed
print("Go!")
case _:
raise RuntimeError
```

虽然这段代码现在按预期工作，但很难看出 `match` 版本相对于上面 `take_action` 函数中更简单的 `if` 版本的好处。`if` 版本是 9 行，而 `match` 版本是 10 行。`if` 版本为每个分支重复 `light ==` 前缀，但 `match` 版本为常量重复 `ColorEnum.` 前缀。表面上看，似乎是平局。如果 `match` 语句不是一个引人注目的功能，为什么 Python 要将其添加到语言中呢？

#### `match` 用于解构

_解构_ 是一种编程语言技术，用于以最少的语法从复杂的嵌套数据结构中提取组件。Python 程序员一直在使用解构，甚至没有意识到这一点。例如，在 `for` 循环中，将 `index, value` 多重赋值给 `enumerate` 的返回值是一种解构形式（参见 [Item 17](#ch03#ch03lev1sec1): “[优先使用 enumerate 代替 range](#ch03#ch03lev1sec1)”）：

[点击此处查看代码图像](#ch01_images#f0034-02)

```pythonpython
for index, value in enumerate("abc"):
print(f"index {index} is {value}")

>>>
index 0 is a
index 1 is b
index 2 is c
```

Python 长期以来一直支持对深度嵌套的元组和列表进行解构赋值（参见 [Item 16](#ch02#ch02lev1sec7): “[优先使用捕获所有解包代替切片](#ch02#ch02lev1sec7)）。`match` 语句将语言扩展到也支持字典、集合和用户定义类的这种类似解包的行为，仅用于流程控制的目的。`match` 实现的 _结构化模式匹配_ 技术在代码需要处理异构对象图和半结构化数据时尤其有价值。（函数式风格编程中的类似惯用法是 _代数数据类型_、_求和类型_ 和 _标签联合_。）

例如，假设我想搜索二叉树并确定它是否包含给定值。我可以将二叉树表示为三项 `tuple`，其中第一个索引是值，第二个索引是左（较小值）子节点，第三个索引是右（较大值）子节点。第二个或第三个位置的 `None` 表示缺少子节点。对于叶节点，我可以直接内联值，而不是使用另一个嵌套的元组。这里我定义了一个包含五个值（7、9、10、11、13）的嵌套树：

[点击此处查看代码图像](#ch01_images#f0035-01)

```python
my_tree = (10, (7, None, 9), (13, 11, None))
```

我可以通过使用简单的 `if` 语句来实现一个递归函数来测试树是否包含一个值。`tree` 参数可能是 `None`（表示缺少的子节点）或非元组（表示叶节点），因此此代码需要确保在解包三元组节点表示之前处理这些条件：

[点击此处查看代码图像](#ch01_images#f0035-02)

```pythonpython
def contains(tree, value):
if not isinstance(tree, tuple):
return tree == value

pivot, left, right = tree

if value < pivot:
return contains(left, value)
elif value > pivot:
return contains(right, value)
else:
return value == pivot
```

当节点值可比较时，此函数按预期工作：

[点击此处查看代码图像](#ch01_images#f0035-03)

```pythonpython
assert contains(my_tree, 9)
assert not contains(my_tree, 14)
```

现在我可以使用 `match` 语句重写此函数：

[点击此处查看代码图像](#ch01_images#f0035-04)

```pythonpython
def contains_match(tree, value):
match tree:
case pivot, left, _ if value < pivot:
return contains_match(left, value)
case pivot, _, right if value > pivot:
return contains_match(right, value)
case (pivot, _, _) | pivot:
return pivot == value
```

使用 `match`，消除了 `isinstance` 的调用，可以避免解包赋值，代码的结构（使用 `case` 子句）更规整，逻辑更简单易懂，并且函数只有七行代码，而不是 `if` 版本所需的九行。这使得 `match` 语句看起来相当有吸引力（参见 [Item 76](#ch09#ch09lev1sec10): “[了解如何将线程 I/O 移植到 asyncio](#ch09#ch09lev1sec10)” 以了解另一个示例）。

在此函数中，`match` 的工作方式是，每个 `case` 子句都尝试使用给定的解构模式提取 `tree` 参数的内容。在 Python 确定结构匹配后，它会评估任何后续的 `if` 子句，这些子句的工作方式类似于推导式中的 `if` 子句。当 `if` 子句（有时称为 _守卫表达式_）评估为 `True` 时，将执行该 `case` 块的缩进语句，其余的将被跳过。如果没有 `case` 子句匹配输入值，则 `match` 语句不执行任何操作并直接跳过。

此代码还使用 `|` 管道运算符将 _或模式_ 添加到最后一个 `case` 分支。这允许 `case` 子句匹配给定的任一模式：`(pivot, _, _)` 或 `pivot`。正如你可能还记得上面尝试引用 `RED` 常量的交通灯示例，第二个模式（`pivot`）是一个捕获模式，它将匹配任何值。因此，当 `tree` 不是具有正确结构的元组时，代码假定它是一个叶值，应该测试其相等性。

现在想象一下，我的需求再次改变，我想使用类而不是元组来表示二叉树中的节点（有关如何做出该选择，请参见 [Item 29](#ch04#ch04lev1sec5): “[通过混合类来组合功能](#ch04#ch04lev1sec5)”）。这里我为节点定义了一个新类：

[点击此处查看代码图像](#ch01_images#f0036-01)

```pythonpython
class Node:
def __init__(self, value, left=None, right=None):
self.value = value
self.left = left
self.right = right
```

我可以通过使用这个类来创建树的另一个实例。同样，我通过提供叶节点的值而不是将它们包装在另一个 `Node` 对象中来简单地指定叶节点：

[点击此处查看代码图像](#ch01_images#f0036-02)

```pythonpython
obj_tree = Node(
value=10,
left=Node(value=7, right=9),
right=Node(value=13, left=11),
)
```

修改 `contains` 函数的 `if` 语句版本以处理 `Node` 类非常简单：

[点击此处查看代码图像](#ch01_images#f0037-01)

```pythonpython
def contains_class(tree, value):
if not isinstance(tree, Node):
return tree == value
elif value < tree.value:
return contains_class(tree.left, value)
elif value > tree.value:
return contains_class(tree.right, value)
else:
return tree.value == value
```

生成的代码与之前使用三元组的版本类似复杂。在某些方面，类使函数更好（例如，访问对象属性而不是解包），而在其他方面，它使函数更糟（例如，重复的 `tree.` 前缀）。

我还可以将 `contains` 函数的 `match` 版本改编为使用 `Node` 类：

[点击此处查看代码图像](#ch01_images#f0037-02)

```pythonpython
def contains_match_class(tree, value):
match tree:
case Node(value=pivot, left=left) if value < pivot:
return contains_match_class(left, value)
case Node(value=pivot, right=right) if value > pivot:
return contains_match_class(right, value)
case Node(value=pivot) | pivot:
return pivot == value
```

其工作原理是，每个 `case` 子句隐式地执行 `isinstance` 检查，以测试 `tree` 的值是否为 `Node` 对象。然后，它使用捕获模式（`pivot`、`left`、`right`）提取对象的属性，类似于元组解构的工作方式。捕获变量可以在守卫表达式和 `case` 块中使用，以避免更冗长的属性访问（例如 `tree.left`）。`match` 提供的功能和清晰度与对象配合得同样好，与嵌套的内置数据结构配合得一样好。

#### 半结构化数据与封装数据

当数据结构及其解释是分离的时，`match` 也表现出色。例如，反序列化的 JSON 对象仅仅是字典、列表、字符串和数字的嵌套（有关示例，请参见 [Item 54](#ch07#ch07lev1sec7): “[考虑使用混合类来组合功能](#ch07#ch07lev1sec7)”）。它缺乏显式类层次结构提供的清晰的责任封装（有关背景，请参见 [Item 53](#ch07#ch07lev1sec6): “[使用 super 初始化父类](#ch07#ch07lev1sec6)）。但是，这些基本 JSON 类型嵌套的方式——每个级别的键、值和元素的存在——赋予了数据程序可以解释的语义含义。

例如，想象一下我正在构建计费软件，并且需要反序列化以 JSON 存储的客户记录。有些记录是针对个人客户的，而其他记录是针对企业客户的：

[点击此处查看代码图像](#ch01_images#f0038-01)

```pythonpython
record1 = """{"customer": {"last": "Ross", "first": "Bob"}}"""
record2 = """{"customer": {"entity": "Steve's Painting Co."}}"""
```

我想将这些记录转换为我可以在程序的 数据处理功能、UI 小部件等中使用（有关背景，请参见 [Item 51](#ch07#ch07lev1sec4): “[优先使用 dataclasses 定义轻量级类](#ch07#ch07lev1sec4)”）的定义明确的 Python 对象：

[点击此处查看代码图像](#ch01_images#f0038-02)

```pythonpython
from dataclasses import dataclass

@dataclass
class PersonCustomer:
first_name: str
last_name: str

@dataclass
class BusinessCustomer:
company_name: str
```

我可以使用 `match` 语句来解释 JSON 数据中的结构和值，并将其映射到具体的 `PersonCustomer` 和 `BusinessCustomer` 类。这使用了 `match` 语句用于解构带有捕获模式的字典字面量的独特语法：

[点击此处查看代码图像](#ch01_images#f0038-03)

```pythonpython
import json

def deserialize(data):
record = json.loads(data)
match record:
case {"customer": {"last": last_name,
"first": first_name}}:
return PersonCustomer(first_name, last_name)
case {"customer": {"entity": company_name}}:
return BusinessCustomer(company_name)
case _:
raise ValueError("Unknown record type")
```

此函数在上述记录上按预期工作，并生成我需要的对象：

[点击此处查看代码图像](#ch01_images#f0039-01)

```pythonpython
print("Record1:", deserialize(record1))
print("Record2:", deserialize(record2))

>>>
Record1: PersonCustomer(first_name='Bob', last_name='Ross')
Record2: BusinessCustomer(company_name="Steve's Painting Co.")
```

这些示例仅提供了 `match` 语句可能性的一个很小的样本。还有对集合模式、`as` 模式、位置构造函数模式（带有 `__match_args__` 自定义）、带有类型注解的穷尽性检查（参见 [Item 124](#ch14#ch14lev1sec9): “[考虑通过 typing 进行静态分析以避免错误](#ch14#ch14lev1sec9)”）等的支持。鉴于其复杂性，最好参考官方教程（<https://peps.python.org/pep-0636/>）来确定如何为你的特定用例利用 `match`。

#### 需牢记的事项
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 尽管你可以使用 `match` 语句来替换简单的 `if` 语句，但这样做很容易出错。对于不熟悉 `match` 陷阱的 Python 程序员来说，`case` 子句中的捕获模式的结构化性质是不直观的。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `match` 语句为结合 `isinstance` 检查和解构行为与流程控制提供了简洁的语法。它们在处理异构对象图和解释半结构化数据的语义含义时特别有用。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `case` 模式可以有效地与内置数据结构（例如列表、元组、字典）和用户定义类一起使用，但每种类型都有独特的语义，这些语义并不显而易见。
---
<a role="toc_link" id="ch02"></a>

## Effective Python - 2

## 2

本章深入探讨了 Effective Python 的第二个关键方面，重点关注如何利用 Python 语言的特性来编写更高效、更具可读性且更易于维护的代码。我们将逐一剖析 Python 的核心机制，并结合实际案例，展示如何通过精巧的设计和恰当的工具来优化代码性能和开发效率。

本章的核心贡献在于提供了一套系统性的方法论，指导开发者如何从 Python 的语言层面出发，实现代码的“有效性”。这包括但不限于：

*   **理解 Python 的执行模型**: 深入理解 Python 的解释器工作原理、GIL (Global Interpreter Lock) 的影响以及多线程和多进程的适用场景，从而做出更明智的性能优化决策。
*   **掌握数据结构和算法的 Pythonic 实现**: 学习如何利用 Python 内置的高效数据结构（如列表推导式、生成器、字典和集合）以及标准库中的算法，编写简洁且性能优越的代码。
*   **利用面向对象编程 (OOP) 的最佳实践**: 探讨如何通过类设计、继承、多态和封装来构建模块化、可重用且易于扩展的代码。
*   **编写可测试和可维护的代码**: 介绍单元测试、集成测试的重要性，以及如何利用文档字符串、类型提示和代码风格指南来提升代码的可读性和可维护性。
*   **性能分析与优化**: 学习使用 Python 的性能分析工具（如 `cProfile` 和 `timeit`）来识别性能瓶颈，并应用相应的优化技术。

本章的组织结构将遵循逻辑递进的原则，从基础概念的讲解，到高级特性的应用，再到实际问题的解决。我们将重点关注那些能够显著提升代码“有效性”的 Python 特性，并提供清晰的示例来佐证。例如，在讨论生成器时，我们会展示它们如何通过惰性求值来节省内存，尤其是在处理大型数据集时，这与传统的列表操作形成鲜明对比。同样，在介绍 `asyncio` 时，我们将阐述其如何通过异步编程模型来提高 I/O 密集型任务的效率，这对于构建高性能的网络应用至关重要。

本章的最终目标是使读者能够写出更符合 Python 哲学（Pythonic）的代码，从而在软件开发过程中取得更大的成功。我们将强调代码的清晰度、简洁性和效率之间的平衡，并鼓励读者在实践中不断探索和应用这些原则。

## Effective Python - Strings and Slicing

## Python 高效编程 - 字符串与切片

Python 最初作为一种用于编排命令行工具以及处理输入输出数据的脚本语言而广受欢迎。凭借其内置的字符串和序列处理语法、方法和模块，Python 成为了传统 shell 和其他常用脚本语言（例如 Perl）的吸引人替代品。此后，Python 不断扩展到相邻领域，成为解析文本、生成结构化数据、检查文件格式、分析日志等理想的编程语言。

通过使用 `bytes` 和 `str` 类型，Python 程序可以与人类语言文本交互，操作底层二进制数据格式，执行输入/输出（I/O）操作，并与外部世界进行通信。Python 对这些字符类型、列表和其他类型进行抽象，为索引、子序列化等提供通用接口。这些功能至关重要，您会在几乎所有程序中看到它们。

### Item 10: 了解 `bytes` 和 `str` 之间的区别

在 Python 中，有两种类型代表字符数据序列：`bytes` 和 `str`。`bytes` 的实例包含原始的、无符号的 8 位值（通常以 ASCII 编码显示）：

```python
a = b"h\x65llo"
print(type(a))
print(list(a))
print(a)

>>>
<class 'bytes'>
[104, 101, 108, 108, 111]
b'hello'
```

`str` 的实例包含 Unicode _code points_，代表人类语言中的文本字符：

[点击此处查看代码图像](#ch02_images#f0042-01)

```python
a = "a\u0300 propos"
print(type(a))
print(list(a))
print(a)

>>>
<class 'str'>
['a', '`', ' ', 'p', 'r', 'o', 'p', 'o', 's']
à propos
```

重要的是，`str` 实例没有关联的二进制编码，`bytes` 实例也没有关联的文本编码。要将 Unicode 数据转换为二进制数据，您必须调用 `str` 的 `encode` 方法。要将二进制数据转换为 Unicode 数据，您必须调用 `bytes` 的 `decode` 方法。您可以为这些方法显式指定要使用的编码，也可以接受系统默认值，通常是 _UTF-8_（但并非总是如此，您很快就会看到）。

在编写 Python 程序时，重要的是在接口的最外层进行 Unicode 数据的编码和解码；这种方法通常称为 _Unicode 夹层_。程序的内核应使用 `str` 类型，其中包含 Unicode 数据，并且不应假定任何关于字符编码的信息。此设置使您能够非常灵活地接受替代文本编码（如 _Latin-1_、_Shift JIS_ 和 _Big5_），同时严格控制输出文本编码（理想情况下为 UTF-8）。

字符数据类型之间的划分导致 Python 代码中出现两种常见情况：
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 您想操作包含 UTF-8 编码字符串（或其他编码）的原始 8 位序列。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 您想操作没有特定编码的 Unicode 字符串。

您通常需要两个辅助函数来在这些情况之间进行转换，并确保输入值的类型与代码的预期相符。

第一个函数接受 `bytes` 或 `str` 实例，并始终返回 `str`：

[点击此处查看代码图像](#ch02_images#f0042-02)

```python
def to_str(bytes_or_str):
if isinstance(bytes_or_str, bytes):
value = bytes_or_str.decode("utf-8")
else:
value = bytes_or_str
return value  # Instance of str

print(repr(to_str(b"foo")))
print(repr(to_str("bar")))

>>>
'foo'
'bar'
```

第二个函数接受 `bytes` 或 `str` 实例，并始终返回 `bytes`：

[点击此处查看代码图像](#ch02_images#f0043-02)

```python
def to_bytes(bytes_or_str):
if isinstance(bytes_or_str, str):
value = bytes_or_str.encode("utf-8")
else:
value = bytes_or_str
return value  # Instance of bytes

print(repr(to_bytes(b"foo")))
print(repr(to_bytes("bar")))
```

在处理 Python 中的原始 8 位值和 Unicode 字符串时，有两个主要的陷阱。

第一个问题是 `bytes` 和 `str` 的行为方式似乎相同，但它们的实例彼此不兼容，因此您必须谨慎处理您传递的字符序列类型。

通过使用 `+` 运算符，您可以分别将 `bytes` 添加到 `bytes` 和 `str` 添加到 `str`：

```python
print(b"one" + b"two")
print("one" + "two")

>>>
b'onetwo'
onetwo
```

但您不能将 `str` 实例添加到 `bytes` 实例：

[点击此处查看代码图像](#ch02_images#f0043-03)

```python
b"one" + "two"

>>>
Traceback ...
TypeError: can't concat str to bytes
```

您也不能将 `bytes` 实例添加到 `str` 实例：

[点击此处查看代码图像](#ch02_images#f0044-01)

```python
"one" + b"two"

>>>
Traceback ...
TypeError: can only concatenate str (not "bytes") to str
```

通过使用二进制运算符，您可以分别比较 `bytes` 与 `bytes` 和 `str` 与 `str`：

```python
assert b"red" > b"blue"
assert "red" > "blue"
```

但您不能比较 `str` 实例与 `bytes` 实例：

[点击此处查看代码图像](#ch02_images#f0044-02)

```python
assert "red" > b"blue"

>>>
Traceback ...
TypeError: '>' not supported between instances of 'str' and
➥'bytes'
```

您也不能比较 `bytes` 实例与 `str` 实例：

[点击此处查看代码图像](#ch02_images#f0044-03)

```python
assert b"blue" < "red"

>>>
Traceback ...
TypeError: '<' not supported between instances of 'bytes' and
➥'str'
```

比较 `bytes` 和 `str` 实例的相等性将始终评估为 `False`，即使它们包含完全相同的字符（在这种情况下是 ASCII 编码的 `"foo"`）：

```python
print(b"foo" == "foo")

>>>
False
```

`%` 运算符可与每种类型的格式字符串一起使用（有关背景信息，请参阅 [Item 11](#ch02#ch02lev1sec2)：“[Prefer Interpolated F-Strings over C-Style Format Strings and str.format](#ch02#ch02lev1sec2)”）：

```python
blue_bytes = b"blue"
blue_str = "blue"
print(b"red %s" % blue_bytes)
print("red %s" % blue_str)

>>>
b'red blue'
red blue
```

但您不能将 `str` 实例传递给 `bytes` 格式字符串，因为 Python 不知道要使用哪种二进制文本编码：

[点击此处查看代码图像](#ch02_images#f0045-01)

```python
print(b"red %s" % blue_str)

>>>
Traceback ...
TypeError: %b requires a bytes-like object, or an object that
➥implements __bytes__, not 'str'
```

但是，您 _可以_ 通过使用 `%` 运算符将 `bytes` 实例传递给 `str` 格式字符串，或者您可以在插值格式字符串中使用 `bytes` 实例，但这不会产生您期望的结果：

```python
print("red %s" % blue_bytes)
print(f"red {blue_bytes}")

>>>
red b'blue'
red b'blue'
```

在这些情况下，代码实际上会调用 `bytes` 实例的 `__repr__` 特殊方法（请参阅 [Item 12](#ch02#ch02lev1sec3)：“[Understand the Difference Between repr and str when Printing Objects](#ch02#ch02lev1sec3)”），并将其替换 `%s` 或 `{blue_bytes}`，这就是为什么输出中会出现 `b"blue"` 字面量的原因。

第二个陷阱是涉及文件句柄（由 `open` 内置函数返回）的操作默认需要 Unicode 字符串而不是原始 `bytes`。这可能导致意外的失败，特别是对于习惯了 Python 2 的程序员。例如，假设我想将一些二进制数据写入文件。这段看似简单的代码会失败：

[点击此处查看代码图像](#ch02_images#f0045-02)

```python
with open("data.bin", "w") as f:
f.write(b"\xf1\xf2\xf3\xf4\xf5")

>>>
Traceback ...
TypeError: write() argument must be str, not bytes
```

异常的原因是文件是以写入文本模式（`"w"`）而不是写入二进制模式（`"wb"`）打开的。当文件处于文本模式时，`write` 操作期望包含 Unicode 数据的 `str` 实例，而不是包含二进制数据的 `bytes` 实例。在这里，我通过将打开模式更改为 `"wb"` 来修复此问题：

[点击此处查看代码图像](#ch02_images#f0045-03)

```python
with open("data.bin", "wb") as f:
f.write(b"\xf1\xf2\xf3\xf4\xf5")
```

从文件中读取数据时也存在类似的问题。例如，我尝试读取上面写入的二进制文件：

[点击此处查看代码图像](#ch02_images#f0046-01)

```python
with open("data.bin", "r") as f:
data = f.read()

>>>
Traceback ...
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in
➥position 0: invalid continuation byte
```

这会失败，因为文件是以读取文本模式（`"r"`）而不是读取二进制模式（`"rb"`）打开的。当句柄处于文本模式时，它使用系统的默认文本编码通过 `bytes.decode`（用于读取）和 `str.encode`（用于写入）方法来解释二进制数据。在大多数系统上，默认编码是 UTF-8，它无法接受二进制数据 `b"\xf1\xf2\xf3\xf4\xf5"`，从而导致上述错误。在这里，我通过将打开模式更改为 `"rb"` 来解决此问题：

[点击此处查看代码图像](#ch02_images#f0046-02)

```python
with open("data.bin", "rb") as f:
data = f.read()
assert data == b"\xf1\xf2\xf3\xf4\xf5"
```

或者，我可以显式指定 `open` 函数的 `encoding` 参数，以确保我不会因任何特定于平台的行为而感到惊讶。例如，在这里我假设文件中的二进制数据实际上是编码为 `"cp1252"`（一种旧的 Windows 编码）的字符串：

[点击此处查看代码图像](#ch02_images#f0046-03)

```python
with open("data.bin", "r", encoding="cp1252") as f:
data = f.read()
assert data == "ñòóôõ"
```

异常消失了，文件内容的字符串解释与读取原始字节时返回的内容大不相同。这里的教训是，您应该检查系统上的默认编码（使用 `python3 -c 'import locale; print(locale.getpreferred-encoding())'`）以了解它与您的期望有何不同。如有疑问，您应该显式传递 `encoding` 参数给 `open`。

#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `bytes` 包含 8 位值序列，`str` 包含 Unicode code point 序列。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用辅助函数来确保您操作的输入是您期望的字符序列类型（8 位值、UTF-8 编码字符串、Unicode code points 等）。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `bytes` 和 `str` 实例不能与运算符（如 `>`, `==`, `+`, 和 `%`）一起使用。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果您想从文件读取或写入二进制数据，请始终使用二进制模式（如 `"rb"` 或 `"wb"`）打开文件。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果您想从文件读取或写入 Unicode 数据，请注意您系统的默认文本编码。显式传递 `encoding` 参数给 `open` 以避免意外。

### Item 11: 优先使用插值 f-string 而非 C 风格格式字符串和 `str.format`

字符串在 Python 代码库中无处不在。它们用于在用户界面和命令行工具中渲染消息。它们用于将数据写入文件和套接字。它们用于在 `Exception` 详细信息中指定出了什么问题（请参阅 [Item 88](#ch10#ch10lev1sec9)：“[Consider Explicitly Chaining Exceptions to Clarify Tracebacks](#ch10#ch10lev1sec9)”）。它们用于日志记录和调试（请参阅 [Item 12](#ch02#ch02lev1sec3)：“[Understand the Difference Between repr and str When Printing Objects](#ch02#ch02lev1sec3)”）。

_格式化_ 是将预定义文本与数据值组合成单个人类可读消息的过程，该消息存储为字符串。Python 在语言和标准库中内置了四种不同的字符串格式化方法。除了最后一种方法（在本项中最后介绍）之外，其他方法都有您应该理解和避免的严重缺点。

#### C 风格格式化

在 Python 中格式化字符串最常见的方法是使用 `%` 格式化运算符。在运算符左侧提供一个预定义的文本模板，称为 _格式字符串_。要在模板中插入的值作为单个值或多个值的 `tuple` 提供在格式运算符的右侧。例如，在这里我使用 `%` 运算符将难以阅读的二进制和十六进制值转换为整数字符串：

[点击此处查看代码图像](#ch02_images#f0047-01)

```python
a = 0b10111011
b = 0xC5F
print("Binary is %d, hex is %d" % (a, b))

>>>
Binary is 187, hex is 3167
```

格式字符串使用格式说明符（如 `%d`）作为占位符，这些占位符将被格式化表达式右侧的值替换。格式说明符的语法来自 C 的 `printf` 函数，Python（以及其他编程语言）继承了它。Python 支持您期望从 `printf` 中获得的所有常用选项，例如 `%s`、`%x` 和 `%f` 格式说明符，以及对小数位数、填充、填充和对齐的控制。许多对 Python 不熟悉的程序员从 C 风格格式字符串开始，因为它们熟悉且易于使用。

Python 中的 C 风格格式字符串存在四个问题。

第一个问题是，如果您更改格式化表达式右侧 `tuple` 中数据值的类型或顺序，可能会由于类型转换不兼容而导致错误。例如，这个简单的格式化表达式可以工作：

[点击此处查看代码图像](#ch02_images#f0048-01)

```python
key = "my_var"
value = 1.234
formatted = "%-10s = %.2f" % (key, value)
print(formatted)

>>>
my_var     = 1.23
```

但是，如果您交换 `key` 和 `value`，您将在运行时收到一个异常：

[点击此处查看代码图像](#ch02_images#f0048-02)

```python
reordered_tuple = "%-10s = %.2f" % (value, key)

>>>
Traceback ...
TypeError: must be real number, not str
```

将右侧参数保留原始顺序但更改格式字符串会导致相同的错误：

[点击此处查看代码图像](#ch02_images#f0048-03)

```python
reordered_string = "%.2f = %-10s" % (key, value)

>>>
Traceback ...
TypeError: must be real number, not str
```

要避免此陷阱，您需要不断检查 `%` 运算符的左右两侧是否同步；此过程容易出错，因为必须为每次更改手动完成。

C 风格格式化表达式的第二个问题是，当您需要对值进行少量修改后再将其格式化为字符串时，它们会变得难以阅读——而这是一种极其常见的情况。在这里，我列出了我的食品储藏室的内容，而没有对值进行任何内联更改：

[点击此处查看代码图像](#ch02_images#f0049-01)

```python
pantry = [
("avocados", 1.25),
("bananas", 2.5),
("cherries", 15),
]
for i, (item, count) in enumerate(pantry):
print("#%d: %-10s = %.2f" % (i, item, count))

>>>
#0: avocados   = 1.25
#1: bananas    = 2.50
#2: cherries   = 15.00
```

现在，我对要格式化的值进行了一些修改，以使打印的消息更有用。这导致格式化表达式中的 `tuple` 变得如此之长，以至于需要跨越多行，这会降低可读性：

[点击此处查看代码图像](#ch02_images#f0049-02)

```python
for i, (item, count) in enumerate(pantry):
print(
"#%d: %-10s = %d"
% (
i + 1,
item.title(),
round(count),
)
)

>>>
#1: Avocados   = 1
#2: Bananas    = 2
#3: Cherries   = 15
```

格式化表达式的第三个问题是，如果您想在格式字符串中多次使用相同的值，则必须在右侧的 `tuple` 中重复它：

[点击此处查看代码图像](#ch02_images#f0049-03)

```python
template = "%s loves food. See %s cook."
name = "Max"
formatted = template % (name, name)
print(formatted)

>>>
Max loves food. See Max cook.
```

这尤其令人讨厌且容易出错，如果您必须对正在格式化的值进行少量修改。例如，在这里我调用了一个对 `name` 的引用 `title()` 方法，但不是另一个，这会导致输出不匹配：

[点击此处查看代码图像](#ch02_images#f0050-01)

```python
name = "brad"
formatted = template % (name.title(), name)
print(formatted)

>>>
Brad loves food. See brad cook.
```

Python 中的 `%` 运算符通过能够使用字典而不是 `tuple` 进行格式化来解决其中一些问题。字典中的键与具有相同名称的格式说明符匹配，例如 `%(key)s`。在这里，我使用此功能来更改格式化表达式右侧值的顺序，而不会影响输出，从而解决了上述问题 #1：

[点击此处查看代码图像](#ch02_images#f0050-02)

```python
key = "my_var"
value = 1.234

old_way = "%-10s = %.2f" % (key, value)

new_way = "%(key)-10s = %(value).2f" % {
"key": key,  # Key first
"value": value,
}

reordered = "%(key)-10s = %(value).2f" % {
"value": value,
"key": key,  # Key second
}

assert old_way == new_way == reordered
```

在格式化表达式中使用字典还可以解决上述问题 #3，方法是允许多个格式说明符引用相同的值，从而无需多次提供该值：

[点击此处查看代码图像](#ch02_images#f0050-03)

```python
name = "Max"

template = "%s loves food. See %s cook."
before = template % (name, name)   # Tuple

template = "%(name)s loves food. See %(name)s cook."
after = template % {"name": name}  # Dictionary

assert before == after
```

但是，字典格式字符串会引入并加剧其他问题。对于上述问题 #2，关于在格式化值之前对值进行少量修改，由于右侧存在字典键和冒号运算符，格式化表达式变得更长且视觉上更混乱。在这里，我渲染相同的字符串，有或没有字典，以显示此问题：

[点击此处查看代码图像](#ch02_images#f0051-02)

```python
for i, (item, count) in enumerate(pantry):
before = "#%d: %-10s = %d" % (
i + 1,
item.title(),
round(count),
)

after = "#%(loop)d: %(item)-10s = %(count)d" % {
"loop": i + 1,
"item": item.title(),
"count": round(count),
}

assert before == after
```

在格式化表达式中使用字典还会增加冗余，这是 Python 中 C 风格格式化表达式的第四个问题。每个键至少必须指定两次——一次在格式说明符中，一次在字典中作为键，并且可能再一次用于包含字典值的变量名：

[点击此处查看代码图像](#ch02_images#f0051-03)

```python
soup = "lentil"
formatted = "Today's soup is %(soup)s." % {"soup": soup}
print(formatted)

>>>
Today's soup is lentil.
```

除了涉及重复字符外，这种冗余还会导致使用字典的格式化表达式变长。这些表达式通常必须跨越多行，格式字符串跨越多行连接，字典赋值每行一个值用于格式化：

[点击此处查看代码图像](#ch02_images#f0052-01)

```python
menu = {
"soup": "lentil",
"oyster": "kumamoto",
"special": "schnitzel",
}
template = (
"Today's soup is %(soup)s, "
"buy one get two %(oyster)s oysters, "
"and our special entrée is %(special)s."
)
formatted = template % menu
print(formatted)

>>>
Today's soup is lentil, buy one get two kumamoto oysters, and
➥our special entrée is schnitzel.
```

要理解这个格式化表达式将产生什么，您的视线必须在格式字符串的行和字典的行之间不断来回切换。这种脱节使得发现错误变得困难，如果您需要对任何值进行少量修改以进行格式化，可读性会变得更糟。

一定有更好的方法。

#### `format` 内置函数和 `str.format`

Python 3 增加了对 _高级字符串格式化_ 的支持，它比使用 `%` 运算符的旧 C 风格格式字符串更具表现力。对于单个 Python 值，可以通过 `format` 内置函数访问此新功能。例如，在这里我使用一些新选项（`,` 用于千位分隔符，`^` 用于居中）来格式化值：

```python
a = 1234.5678
formatted = format(a, ",.2f")
print(formatted)

b = "my string"
formatted = format(b, "^20s")
print("*", formatted, "*")

>>>
1,234.57
*      my string       *
```

您可以使用此功能通过调用 `str` 类型的 `format` 方法来格式化多个值。而不是使用 `%d` 这样的 C 风格格式说明符，您可以使用 `{}` 指定占位符。默认情况下，格式字符串中的占位符将被替换为传递给 `format` 方法的相应位置参数，按照它们出现的顺序：

[点击此处查看代码图像](#ch02_images#f0053-01)

```python
key = "my_var"
value = 1.234

formatted = "{} = {}".format(key, value)
print(formatted)

>>>
my_var = 1.234
```

在每个占位符内，您可以选择性地提供一个冒号字符后跟格式说明符，以自定义值如何转换为字符串（有关选项的完整范围，请参阅 <https://docs.python.org/3/library/string.html#format-specification-mini-language>）：

[点击此处查看代码图像](#ch02_images#f0053-02)

```python
formatted = "{:<10} = {:.2f}".format(key, value)
print(formatted)

>>>
my_var     = 1.23
```

思考此工作方式的方法是，格式说明符将与值一起传递给 `format` 内置函数（在上面的示例中为 `format(value, ".2f")`）。该函数调用的结果将替换整个格式化字符串中的占位符。您可以通过使用 `__format__` 特殊方法为每个类自定义格式行为。

`str.format` 的另一个需要注意的细节是转义大括号（`{`）。您需要将它们加倍（`{{`），以免它们被意外解释为占位符（就像您需要将 `%` 字符加倍以使用 C 风格格式字符串正确转义它一样）：

[点击此处查看代码图像](#ch02_images#f0053-03)

```python
print("%.2f%%" % 12.5)
print("{} replaces {{}}".format(1.23))

>>>
12.50%
1.23 replaces {}
```

在大括号内，您还可以指定传递给 `format` 方法的参数的位置索引，以用于替换占位符。这允许格式字符串更新以重新排序输出，而无需您更改格式化表达式的右侧，从而解决了上述问题 #1：

[点击此处查看代码图像](#ch02_images#f0054-01)

```python
formatted = "{1} = {0}".format(key, value)
print(formatted)

>>>
1.234 = my_var
```

相同的 positional index 也可以在格式字符串中多次引用，而无需将值传递给 `format` 方法多次，这解决了上述问题 #3：

[点击此处查看代码图像](#ch02_images#f0054-02)

```python
formatted = "{0} loves food. See {0} cook.".format(name)
print(formatted)

>>>
Max loves food. See Max cook.
```

不幸的是，新的 `format` 方法并未解决上述问题 #2，使得在格式化值之前进行少量修改的代码难以阅读。新旧选项在可读性上几乎没有区别，它们同样混乱：

[点击此处查看代码图像](#ch02_images#f0054-03)

```python
for i, (item, count) in enumerate(pantry):
old_style = "#%d: %-10s = %d" % (
i + 1,
item.title(),
round(count),
)

new_style = "#{}: {:<10s} = {}".format(
i + 1,
item.title(),
round(count),
)

assert old_style == new_style
```

`str.format` 方法甚至还有更高级的说明符选项，例如在占位符中使用字典键和列表索引的组合，以及强制将值转换为 Unicode 和 `repr` 字符串：

[点击此处查看代码图像](#ch02_images#f0054-04)

```python
formatted = "First letter is {menu[oyster][0]!r}".format(menu=menu)
print(formatted)

>>>
First letter is 'k'
```

但是，这些功能无助于减少上述问题 #4 中重复键的冗余。例如，在这里我比较了在 C 风格格式化表达式中使用字典与将关键字参数传递给 `format` 方法的新样式的冗余：

[点击此处查看代码图像](#ch02_images#f0055-01)

```python
old_template = (
"Today's soup is %(soup)s, "
"buy one get two %(oyster)s oysters, "
"and our special entrée is %(special)s."
)
old_formatted = old_template % {
"soup": "lentil",
"oyster": "kumamoto",
"special": "schnitzel",
}

new_template = (
"Today's soup is {soup}, "
"buy one get two {oyster} oysters, "
"and our special entrée is {special}."
)
new_formatted = new_template.format(
soup="lentil",
oyster="kumamoto",
special="schnitzel",
)

assert old_formatted == new_formatted
```

这种样式稍微不那么冗长，因为它消除了字典中的一些引号和格式说明符中的一些字符，但这几乎没有说服力。此外，在占位符中使用字典键和索引的高级功能只是 Python 表达式功能的一小部分。这种缺乏表现力是如此有限，以至于它削弱了 `str.format` 方法的整体价值。

考虑到这些缺点以及 C 风格格式化表达式中仍然存在的问题（上述问题 #2 和 #4），我建议您总体上避免使用 `str.format` 方法。了解用于格式说明符的新迷你语言（冒号后面的所有内容）以及如何使用 `format` 内置函数很重要。但是，`str.format` 方法的其余部分应被视为历史文物，以帮助您理解 Python 的新 _f-strings_ 如何工作以及为什么它们如此出色。

#### 插值格式字符串

Python 3.6 增加了插值格式字符串——简称 _f-strings_——以一劳永逸地解决这些问题。这种新的语言语法要求您在格式字符串前加上 `f` 字符，这类似于字节字符串以 `b` 字符开头，原始（未转义）字符串以 `r` 字符开头。

f-strings 将格式字符串的表现力发挥到极致，通过完全消除提供要格式化的键和值的冗余来解决上述问题 #4。它们通过允许您将当前 Python 作用域中的所有名称作为格式化表达式的一部分来达到这种简洁性：

[点击此处查看代码图像](#ch02_images#f0056-01)

```python
key = "my_var"
value = 1.234

formatted = f"{key} = {value}"
print(formatted)

>>>
my_var = 1.234
```

`str.format` 方法中的所有新 `format` 内置迷你语言选项都可以在 f-string 中的占位符的冒号之后使用，并且可以像 `str.format` 方法一样将值强制转换为 Unicode 和 `repr` 字符串（即使用 `!r` 和 `!s`）：

[点击此处查看代码图像](#ch02_images#f0056-02)

```python
formatted = f"{key!r:<10} = {value:.2f}"
print(formatted)

>>>
'my_var'   = 1.23
```

在所有情况下，使用 f-strings 进行格式化都比使用带 `%` 运算符的 C 风格格式字符串和 `str.format` 方法更短。在这里，我按从最短到最长的顺序显示所有选项，并对齐赋值的左侧，以便您轻松比较它们：

[点击此处查看代码图像](#ch02_images#f0056-03)

```python
f_string = f"{key:<10} = {value:.2f}"

c_tuple  = "%-10s = %.2f" % (key, value)

str_args = "{:<10} = {:.2f}".format(key, value)

str_kw   = "{key:<10} = {value:.2f}".format(key=key,
➥value=value)
c_dict   = "%(key)-10s = %(value).2f" % {"key": key, "value":
➥value}

assert c_tuple == c_dict == f_string
assert str_args == str_kw == f_string
```

f-strings 还允许您将完整的 Python 表达式放在占位符大括号内，从而解决了上述问题 #2，允许使用简洁的语法对要格式化的值进行少量修改。以前需要 C 风格格式化和 `str.format` 方法多行才能完成的工作，现在可以轻松地在一行中完成：

[点击此处查看代码图像](#ch02_images#f0057-02)

```python
for i, (item, count) in enumerate(pantry):
old_style = "#%d: %-10s = %d" % (
i + 1,
item.title(),
round(count),
)

new_style = "#{}: {:<10s} = {}".format(
i + 1,
item.title(),
round(count),
)

f_string = f"#{i+1}: {item.title():<10s} = {round(count)}"

assert old_style == new_style == f_string
```

或者，如果更清晰，您可以依靠相邻字符串连接将 f-string 分成多行（请参阅 [Item 13](#ch02#ch02lev1sec4)：“[Prefer Explicit String Concatenation over Implicit, Especially in Lists](#ch02#ch02lev1sec4)”）。即使这比单行版本长，它仍然比其他多行方法清晰得多：

[点击此处查看代码图像](#ch02_images#f0057-03)

```python
for i, (item, count) in enumerate(pantry):
print(f"#{i+1}: "
f"{item.title():<10s} = "
f"{round(count)}")

>>>
#1: Avocados   = 1
#2: Bananas    = 2
#3: Cherries   = 15
```

Python 表达式也可以出现在格式说明符选项中。例如，在这里我通过使用变量而不是在格式字符串中硬编码来参数化要打印的位数：

[点击此处查看代码图像](#ch02_images#f0058-01)

```python
places = 3
number = 1.23456
print(f"My number is {number:.{places}f}")

>>>
My number is 1.235
```

f-strings 提供的表现力、简洁性和清晰度的结合，使它们成为 Python 程序员的最佳内置选项。任何时候您发现需要将值格式化为字符串，请选择 f-strings 而非其他替代方法。

#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `%` 运算符的 C 风格格式字符串存在各种陷阱和冗余问题。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `str.format` 方法在其格式说明符迷你语言中引入了一些有用的概念，但它在其他方面重复了 C 风格格式字符串的错误，应予以避免。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) f-strings 是一种用于将值格式化为字符串的新语法，它解决了 C 风格格式字符串的最大问题。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) f-strings 简洁而强大，因为它们允许将任意 Python 表达式直接嵌入格式说明符中。

### Item 12: 理解 `repr` 和 `str` 在打印对象时的区别

当您调试 Python 程序时，使用 `print` 函数和格式字符串（请参阅 [Item 11](#ch02#ch02lev1sec2)：“[Prefer Interpolated F-Strings over C-Style Format Strings and str.format](#ch02#ch02lev1sec2)”）或通过 `logging` 内置模块输出会非常有帮助。Python 对象内部通常可以通过普通属性轻松访问（请参阅 [Item 55](#ch07#ch07lev1sec8)：“[Prefer Public Attributes over Private Ones](#ch07#ch07lev1sec8)”）。您所要做的就是调用 `print` 来查看程序状态在运行时如何变化，并推断出它出错的地方（有关更高级的方法，请参阅 [Item 114](#ch13#ch13lev1sec7)：“[Consider Interactive Debugging with pdb](#ch13#ch13lev1sec7)”）。

`print` 函数输出您提供给它的任何内容的“人类可读字符串版本”。例如，我可以使用 `print` 和基本字符串来查看字符串的内容，而无需周围的引号字符：

```python
print("foo bar")

>>>
foo bar
```

这等同于以下所有替代方法：
* 调用 `str` 函数，然后再将值传递给 `print`
* 使用 `%` 运算符的 `"%s"` 格式字符串
* 使用 f-string 中值的默认格式化
* 调用 `format` 内置函数
* 显式调用 `__format__` 特殊方法
* 显式调用 `__str__` 特殊方法

在这里，我展示它们都产生相同的输出：

[点击此处查看代码图像](#ch02_images#f0059-01)

```python
my_value = "foo bar"
print(str(my_value))
print("%s" % my_value)
print(f"{my_value}")
print(format(my_value))
print(my_value.__format__("s"))
print(my_value.__str__())

>>>
foo bar
foo bar
foo bar
foo bar
foo bar
foo bar
```

问题在于，值的“人类可读字符串”并不能清楚地说明值的实际类型和具体组成。例如，请注意在 `print` 的默认输出中，您如何无法区分数字 `5` 和字符串 `"5"` 的类型：

[点击此处查看代码图像](#ch02_images#f0059-03)

```python
int_value = 5
str_value = "5"
print(int_value)
print(str_value)
print(f"Is {int_value} == {str_value}?")

>>>
5
5
Is 5 == 5?
```

如果您使用 `print` 调试程序，这些类型差异很重要。当您调试时，几乎总是想要看到 `object` 的 `repr` 版本。`repr` 内置函数返回 `object` 的 _可打印表示_，它应该是其最清晰可理解的字符串序列化。对于许多内置类型，`repr` 返回的字符串是一个有效的 Python 表达式：

```python
a = "\x07"
print(repr(a))

>>>
'\x07'
```

将 `repr` 返回的值传递给 `eval` 内置函数通常会得到与您开始时相同的 Python 对象：

```python
b = eval(repr(a))
assert a == b
```

当然，在实践中，您应该非常谨慎地使用 `eval`（请参阅 [Item 91](#ch10#ch10lev1sec12)：“[Avoid exec and eval Unless You’re Building a Developer Tool](#ch10#ch10lev1sec12)”）。

当您使用 `print` 进行调试时，您应该在打印值之前调用 `repr`，以确保任何类型差异都清晰明了：

```python
print(repr(int_value))
print(repr(str_value))

>>>
5
'5'
```

这等同于在格式字符串中使用 `%` 运算符的 `"%r"` 格式字符串或使用 `!r` 类型转换的 f-string：

[点击此处查看代码图像](#ch02_images#f0060-02)

```python
print("Is %r == %r?" % (int_value, str_value))
print(f"Is {int_value!r} == {str_value!r}?")

>>>
Is 5 == '5'?
Is 5 == '5'?
```

当 `str` 内置函数接收用户定义类的实例时，它首先尝试调用 `__str__` 特殊方法。如果未定义，它将回退调用 `__repr__` 特殊方法。如果类也没有实现 `__repr__`，则调用将通过方法解析（请参阅 [Item 53](#ch07#ch07lev1sec6)：“[Initialize Parent Classes with super](#ch07#ch07lev1sec6)”），最终调用 `object` 父类的默认实现。不幸的是，`object` 子类的 `repr` 的默认实现并不特别有用。例如，在这里我定义了一个简单的类，然后打印它的一个实例，这最终会导致调用 `object.__repr__`：

[点击此处查看代码图像](#ch02_images#f0061-01)

```python
class OpaqueClass:
def __init__(self, x, y):
self.x = x
self.y = y

obj = OpaqueClass(1, "foo")
print(obj)

>>>
<__main__.OpaqueClass object at 0x1009be510>
```

此输出无法传递给 `eval` 函数，并且它没有说明对象的实例字段。为了改进这一点，在这里我定义了我自己的 `__repr__` 特殊方法，它返回一个包含重新创建对象的 Python 表达式的字符串（有关定义 `__repr__` 的另一种方法，请参阅 [Item 51](#ch07#ch07lev1sec4)：“[Prefer dataclasses for Defining Lightweight Classes](#ch07#ch07lev1sec4)”）：

[点击此处查看代码图像](#ch02_images#f0061-02)

```python
class BetterClass:
def __init__(self, x, y):
self.x = x
self.y = y

def __repr__(self):
return f"BetterClass({self.x!r}, {self.y!r})"
```

现在 `repr` 值更有用了：

```python
obj = BetterClass(2, "bar")
print(obj)

>>>
BetterClass(2, 'bar')
```

调用此类的实例的 `str` 会产生相同的结果，因为未定义 `__str__` 特殊方法，导致 Python 回退到 `__repr__`：

```python
print(str(obj))

>>>
BetterClass(2, 'bar')
```

要让 `str` 打印出不同的“人类可读”格式的字符串——例如，在 UI 元素中显示——我可以定义相应的 `__str__` 特殊方法：

[点击此处查看代码图像](#ch02_images#f0062-01)

```python
class StringifiableBetterClass(BetterClass):
def __str__(self):
return f"({self.x}, {self.y})"
```

现在 `repr` 和 `str` 为每个不同目的返回不同的“人类可读”字符串：

[点击此处查看代码图像](#ch02_images#f0062-02)

```python
obj2 = StringifiableBetterClass(2, "bar")
print("Human readable:", obj2)
print("Printable:     ", repr(obj2))

>>>
Human readable: (2, bar)
Printable:      BetterClass(2, 'bar')
```

#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 对内置 Python 类型调用 `print` 会产生值的“人类可读字符串版本”，这会隐藏类型信息。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 对内置 Python 类型调用 `repr` 会产生包含值“可打印表示”的字符串。`repr` 字符串通常可以传递给 `eval` 内置函数以获取原始值。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 格式字符串中的 `%s` 产生像 `str` 一样的“人类可读字符串”。`%r` 产生像 `repr` 一样的“可打印字符串”。除非您指定 `!r` 类型转换后缀，否则 f-strings 会为替换文本表达式生成“人类可读字符串”。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 您可以在类上定义 `__repr__` 和 `__str__` 特殊方法来定制实例的“可打印”和“人类可读”表示，这有助于调试并简化对象与人类界面的集成。

### Item 13: 优先使用显式字符串连接而非隐式，尤其是在列表中

在其早期，Python 直接从 C 继承了许多属性，包括数字字面量的表示法和类似 `printf` 的格式字符串。此后，该语言已得到显著发展；例如，八进制数现在需要 `0o` 前缀而不是仅 `0`，并且新的字符串插值语法远优于旧语法（请参阅 [Item 11](#ch02#ch02lev1sec2)：“[Prefer Interpolated F-Strings over C-Style Format Strings and str.format](#ch02#ch02lev1sec2)”）。然而，Python 中仍然存在一个类似 C 的特性，即隐式字符串连接。这会导致相邻表达式的字符串字面量在不需要 infix `+` 运算符的情况下被连接起来。因此，这两个赋值实际上做了相同的事情：

```python
my_test1 = "hello" "world"
my_test2 = "hello" + "world"
assert my_test1 == my_test2
```

当您需要将不同类型的字符串字面量与不同的转义要求组合时，这种隐式连接行为可能很有用，这在进行文本模板化或代码生成的程序中很常见。例如，在这里我隐式地合并了一个原始字符串、一个 f-string 和一个单引号字符串：

[点击此处查看代码图像](#ch02_images#f0063-01)

```python
x = 1
my_test1 = (
r"first \ part is here with escapes\n, "
f"string interpolation {x} in here, "
'this has "double quotes" inside'
)
print(my_test1)

>>>
first \ part is here with escapes\n, string interpolation 1 in
➥here, this has "double quotes" inside
```

将每种类型的字符串字面量放在自己的行上，可以使代码更易于阅读，并且没有运算符可以减少视觉混乱。相比之下，当隐式连接发生在单行上时，如果不仔细查看，可能很难预测代码将做什么：

[点击此处查看代码图像](#ch02_images#f0063-02)

```python
y = 2
my_test2 = r"fir\st" f"{y}" '"third"'
print(my_test2)

>>>
fir\st2"third"
```

像这样的隐式连接也容易出错。如果您不小心在相邻字符串之间插入逗号字符，代码的含义将完全不同（请参阅 [Item 6](#ch01#ch01lev1sec6)：“[Always Surround Single-Element Tuples with Parentheses](#ch01#ch01lev1sec6)” 中的类似问题）：

[点击此处查看代码图像](#ch02_images#f0064-01)

```python
my_test3 = r"fir\st", f"{y}" '"third"'
print(my_test3)

>>>
('fir\\st', '2"third"')
```

如果您做相反的事情，意外地删除逗号而不是添加逗号，也可能发生另一个问题。例如，想象一下我想创建一个字符串列表来输出，每行一个元素：

[点击此处查看代码图像](#ch02_images#f0064-02)

```python
my_test4 = [
"first line\n",
"second line\n",
"third line\n",
]
print(my_test4)

>>>
['first line\n', 'second line\n', 'third line\n']
```

如果我删除中间的逗号，结果数据将具有相似的结构，但最后两行将被静默合并。

[点击此处查看代码图像](#ch02_images#f0064-03)

```python
my_test5 = [
"first line\n",
"second line\n"  # Comma removed
"third line\n",
]
print(my_test5)

>>>
['first line\n', 'second line\nthird line\n']
```

作为这段代码的新读者，您可能一眼都看不到丢失的逗号。如果您使用自动格式化程序（请参阅 [Item 2](#ch01#ch01lev1sec2)：“[Follow the PEP 8 Style Guide](#ch01#ch01lev1sec2)”），它可能会重新包装这两行以使这种隐式行为更易于发现，如下所示：

[点击此处查看代码图像](#ch02_images#f0064-04)

```python
my_test5 = [
"first line\n",
"second line\n" "third line\n",
]
```

但是，即使您注意到正在发生隐式连接，也不清楚它是故意的还是意外的。因此，我的建议是，在 `list` 或 `tuple` 字面量中组合字符串时，始终使用显式的 `+` 运算符来消除隐式连接可能造成的任何歧义：

[点击此处查看代码图像](#ch02_images#f0065-01)

```python
my_test6 = [
"first line\n",
"second line\n" +  # Explicit
"third line\n",
]
assert my_test5 == my_test6
```

当存在 `+` 运算符时，自动格式化程序可能仍会更改行包装，但在这种状态下，至少可以清楚代码的作者最初的意图是什么：

[点击此处查看代码图像](#ch02_images#f0065-02)

```python
my_test6 = [
"first line\n",
"second line\n" + "third line\n",
]
```

隐式字符串连接在函数调用参数列表中也可能引起问题。有时在调用中使用隐式连接看起来不错，例如使用 `print` 函数：

[点击此处查看代码图像](#ch02_images#f0065-03)

```python
print("this is my long message "
"that should be printed out")

>>>
this is my long message that should be printed out
```

当您在单个位置参数后提供其他关键字参数时，隐式连接甚至可以具有可读性：

[点击此处查看代码图像](#ch02_images#f0065-04)

```python
import sys

print("this is my long message "
"that should be printed out",
end="",
file=sys.stderr)
```

但是，当调用采用多个位置参数时，隐式字符串连接可能会像 `list` 和 `tuple` 字面量一样令人困惑且容易出错。例如，在这里我创建了一个类实例，其中初始化参数列表的中间存在隐式连接——您能多快发现它？

[点击此处查看代码图像](#ch02_images#f0065-05)

```python
import sys

first_value = ...
second_value = ...

class MyData:
...

value = MyData(123,
first_value,
f"my format string {x}"
f"another value {y}",
"and here is more text",
second_value,
stream=sys.stderr)
```

将字符串连接更改为显式可以使此代码更易于扫描：

[点击此处查看代码图像](#ch02_images#f0066-02)

```python
value2 = MyData(123,
first_value,
f"my format string {x}" +  # Explicit
f"another value {y}",
"and here is more text",
second_value,
stream=sys.stderr)
```

我的建议是，当函数调用采用多个位置参数时，始终使用显式字符串连接以避免任何混淆（请参阅 [Item 37](#ch05#ch05lev1sec8)：“[Enforce Clarity with Keyword-Only and Positional-Only Arguments](#ch05#ch05lev1sec8)” 中的类似示例）。如果只有一个位置参数，如上面的 `print` 示例所示，那么使用隐式字符串连接是可以的。关键字参数可以使用显式或隐式连接传递——以最大化清晰度为准——因为同级字符串字面量不能被误解为 `=` 字符后面的位置参数。

#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 当两个字符串字面量在 Python 代码中相邻时，它们将被合并，就像它们之间存在 `+` 运算符一样，这类似于 C 编程语言的隐式字符串连接功能。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 避免在 `list` 和 `tuple` 字面量中对项目进行隐式字符串连接，因为它会造成关于原始作者意图的歧义。相反，您应该使用显式连接和 `+` 运算符。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在函数调用中，使用一个位置参数和任意数量的关键字参数进行隐式字符串连接是可以的，但当有多个位置参数时，您应该使用显式连接。

### Item 14: 了解如何切片序列

Python 包含用于将序列切片成块的语法。切片允许您轻松访问序列项的子集。切片最简单的用途是内置类型 `list`、`tuple`、`str` 和 `bytes`。切片可以扩展到任何实现 `__getitem__` 和 `__setitem__` 特殊方法的 Python 类（请参阅 [Item 57](#ch07#ch07lev1sec10)：“[Inherit from collections.abc Classes for Custom Container Types](#ch07#ch07lev1sec10)”）。

切片语法的基本形式是 `somelist[start:end]`，其中 `start` 是包含的，`end` 是不包含的：

[点击此处查看代码图像](#ch02_images#f0067-01)

```python
a = ["a", "b", "c", "d", "e", "f", "g", "h"]
print("Middle two:  ", a[3:5])
print("All but ends:", a[1:7])

>>>
Middle two:   ['d', 'e']
All but ends: ['b', 'c', 'd', 'e', 'f', 'g']
```

从序列的开头切片时，您应该省略零索引以减少视觉混乱：

```python
assert a[:5] == a[0:5]
```

切片到序列的末尾时，您应该省略最后一个索引，因为它没有必要：

```python
assert a[5:] == a[5:len(a)]
```

使用负数进行切片有助于相对于序列末尾进行偏移。所有这些切片形式对您的代码的新读者来说都是清晰的：

[点击此处查看代码图像](#ch02_images#f0067-02)

```python
a[:]      # ["a", "b", "c", "d", "e", "f", "g", "h"]
a[:5]     # ["a", "b", "c", "d", "e"]
a[:-1]    # ["a", "b", "c", "d", "e", "f", "g"]
a[4:]     #                     ["e", "f", "g", "h"]
a[-3:]    #                          ["f", "g", "h"]
a[2:5]    #           ["c", "d", "e"]
a[2:-1]   #           ["c", "d", "e", "f", "g"]
a[-3:-1]  #                          ["f", "g"]
```

这里没有意外，我鼓励您使用这些变体。

切片通过静默省略缺失项来正确处理超出列表边界的开始和结束索引。这种行为使您的代码可以轻松地为输入序列建立最大长度：

```python
first_twenty_items = a[:20]
last_twenty_items = a[-20:]
```

相比之下，直接访问相同的缺失索引会导致异常：

[点击此处查看代码图像](#ch02_images#f0068-01)

```python
a[20]

>>>
Traceback ...
IndexError: list index out of range
```

注意：请注意，通过负数变量索引列表是您可能从切片中获得意外结果的少数情况之一。例如，当 `n` 大于零时（例如，当 `n` 为 `3` 时，`somelist[-3:]`），表达式 `somelist[-n:]` 将正常工作。但是，当 `n` 为零时，表达式 `somelist[-0:]` 等同于 `somelist[:]`，它会产生原始列表的副本。

切片列表的结果是一个全新的列表。新列表中的每个项都将引用原始列表中的相应对象。修改由切片创建的列表不会影响原始列表的内容：

[点击此处查看代码图像](#ch02_images#f0068-02)

```python
b = a[3:]
print("Before:   ", b)
b[1] = 99
print("After:    ", b)
print("No change:", a)

>>>
Before:    ['d', 'e', 'f', 'g', 'h']
After:     ['d', 99, 'f', 'g', 'h']
No change: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
```

当用于赋值时，切片会替换原始列表中的指定范围。与解包赋值（例如 `a, b = c[:2]`；请参阅 [Item 5](#ch01#ch01lev1sec5)：“[Prefer Multiple-Assignment Unpacking over Indexing](#ch01#ch01lev1sec5)” 和 [Item 16](#ch02#ch02lev1sec7)：“[Prefer Catch-All Unpacking Over Slicing](#ch02#ch02lev1sec7)”）不同，切片赋值的长度不必相同。分配的切片之前和之后的所有值都将被保留，新值将插入其间。在这里，列表缩小了，因为替换列表比指定的切片短：

[点击此处查看代码图像](#ch02_images#f0069-01)

```python
print("Before ", a)
a[2:7] = [99, 22, 14]
print("After  ", a)

>>>
Before  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
After   ['a', 'b', 99, 22, 14, 'h']
```

在这里，列表增长了，因为分配的列表比指定的切片长：

[点击此处查看代码图像](#ch02_images#f0069-02)

```python
print("Before ", a)
a[2:3] = [47, 11]
print("After  ", a)

>>>
Before  ['a', 'b', 99, 22, 14, 'h']
After   ['a', 'b', 47, 11, 22, 14, 'h']
```

如果您在切片时省略开始和结束索引，您将得到原始列表的副本：

```python
b = a[:]
assert b == a and b is not a
```

如果您将切片赋值给没有开始或结束索引的切片，您将用右侧序列中的项的引用替换列表的整个内容（而不是分配一个新列表）：

[点击此处查看代码图像](#ch02_images#f0069-03)

```python
b = a
print("Before a", a)
print("Before b", b)
a[:] = [101, 102, 103]
assert a is b             # Still the same list object
print("After a ", a)      # Now has different contents
print("After b ", b)      # Same list, so same contents as a

>>>
Before a ['a', 'b', 47, 11, 22, 14, 'h']
Before b ['a', 'b', 47, 11, 22, 14, 'h']
After a  [101, 102, 103]
After b  [101, 102, 103]
```

#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 切片时避免冗长：不要为开始索引或序列长度作为结束索引提供 0。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 切片对于超出边界的开始或结束索引具有容错性，这意味着很容易在序列的前后边界上表达切片（例如 `a[:20]` 或 `a[-20:]`）。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 分配给 `list` 切片会用引用的内容替换原始序列中的该范围，即使长度不同。

### Item 15: 避免在单个表达式中进行步进和切片

除了基本切片（请参阅 [Item 14](#ch02#ch02lev1sec5)：“[Know How to Slice Sequences](#ch02#ch02lev1sec5)”）之外，Python 还为切片的 _步进_ 提供了特殊语法，形式为 `somelist[start:end:stride]`。这允许您在切片序列时每 _n_ 个项取一个。例如，步进可以轻松地将列表中的偶数和奇数序数位置分组：

[点击此处查看代码图像](#ch02_images#f0070-01)

```python
x = ["red", "orange", "yellow", "green", "blue", "purple"]
odds = x[::2]    # First, third, fifth
evens = x[1::2]  # Second, fourth, sixth
print(odds)
print(evens)

>>>
['red', 'yellow', 'blue']
['orange', 'green', 'purple']
```

问题在于，步进语法经常导致意外行为，从而引入错误。例如，一种常见的 Python 技巧是反转字节字符串，方法是使用步进 `-1` 来切片字符串：

```python
x = b"mongoose"
y = x[::-1]
print(y)

>>>
b'esoognom'
```

这对于 Unicode 字符串也同样有效（请参阅 [Item 10](#ch02#ch02lev1sec1)：“[Know the Differences Between bytes and str](#ch02#ch02lev1sec1)”）：

```python
x = "寿司"
y = x[::-1]
print(y)

>>>
司寿
```

但是，当 Unicode 数据编码为 UTF-8 字节字符串时，这会失败：

[点击此处查看代码图像](#ch02_images#f0071-01)

```python
w = "寿司"
x = w.encode("utf-8")
y = x[::-1]
z = y.decode("utf-8")

>>>
Traceback ...
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb8 in
➥position 0: invalid start byte
```

除了 `-1` 之外的负数步进有用吗？考虑以下示例：

[点击此处查看代码图像](#ch02_images#f0071-02)

```python
x = ["a", "b", "c", "d", "e", "f", "g", "h"]
x[::2]   # ["a", "c", "e", "g"]
x[::-2]  # ["h", "f", "d", "b"]
```

这里，`::2` 表示“从开头开始，每隔一个选择一个项”。更棘手的是，`::-2` 表示“从末尾开始，每隔一个向后移动选择一个项”。

您认为 `2::2` 是什么意思？那么 `-2::-2` 与 `-2:2:-2` 与 `2:2:-2` 呢？

[点击此处查看代码图像](#ch02_images#f0071-03)

```python
x[2::2]     # ["c", "e", "g"]
x[-2::-2]   # ["g", "e", "c", "a"]
x[-2:2:-2]  # ["g", "e"]
x[2:2:-2]   # []

>>>
['c', 'e', 'g']
['g', 'e', 'c', 'a']
['g', 'e']
[]
```

关键是切片语法的步进部分可能非常令人困惑。由于其密度，括号中的三个数字已经足够难以阅读。然后，当开始和结束索引相对于步进值生效时，并不明显，尤其是在步进为负数时。

为防止出现问题，我建议您避免在开始和结束索引的同时使用步进。如果您必须使用步进，请优先使用正值并省略开始和结束索引。如果您必须在开始或结束索引处使用步进，请考虑使用一个赋值进行步进，另一个赋值进行切片：

[点击此处查看代码图像](#ch02_images#f0071-04)

```python
y = x[::2]   # ["a", "c", "e", "g"]
z = y[1:-1]  # ["c", "e"]
```

步进然后切片会创建额外的数据浅拷贝。第一个操作应尽可能减小结果切片的大小。如果您的程序无法承担两个步骤所需的时间或内存，请考虑使用 `itertools` 内置模块的 `islice` 方法（请参阅 [Item 24](#ch03#ch03lev1sec8)：“[Consider itertools for Working with Iterators and Generators](#ch03#ch03lev1sec8)”），它更易于阅读，并且不允许为开始、结束或步进使用负值。

#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在单个切片中同时指定开始、结束和步进可能非常令人困惑。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果需要步进，请尝试仅使用正步进值而不使用开始或结束索引；避免使用负步进值。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果在单个切片中需要开始、结束和步进，请考虑执行两次赋值（一次用于步进，一次用于切片）或使用 `itertools` 内置模块的 `islice`。

### Item 16: 优先使用捕获所有解包而非切片

基本解包的一个限制（请参阅 [Item 5](#ch01#ch01lev1sec5)：“[Prefer Multiple-Assignment Unpacking over Indexing](#ch01#ch01lev1sec5)”）是您必须提前知道要解包的序列的长度。例如，这里我有一个汽车经销商正在交易的汽车年龄列表。当我尝试使用基本解包获取列表的前两项时，运行时会引发异常：

[点击此处查看代码图像](#ch02_images#f0072-01)

```python
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
oldest, second_oldest = car_ages_descending

>>>
Traceback ...
ValueError: too many values to unpack (expected 2)
```

Python 新手通常依赖索引和切片（请参阅 [Item 14](#ch02#ch02lev1sec5)：“[Know How to Slice Sequences](#ch02#ch02lev1sec5)”）来处理这种情况。例如，在这里我从至少包含两项的列表中提取最旧的、第二旧的和其余的汽车年龄：

[点击此处查看代码图像](#ch02_images#f0072-02)

```python
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others)

>>>
20 19 [15, 9, 8, 7, 6, 4, 1, 0]
```

这可行，但所有的索引和切片在视觉上都很混乱。实际上，通过这种方式将序列的成员划分为各种子集也很容易出错，因为您更有可能出现“差一错误”；例如，您可能会在一行上更改边界，而忘记更新其他行。

为了更好地处理这种情况，Python 还支持通过 _带星号的表达式_ 进行捕获所有解包。此语法允许解包赋值的一个部分接收所有未匹配其他解包模式部分的值。在这里，我使用带星号的表达式来实现与上面相同的结果，而无需任何索引或切片：

[点击此处查看代码图像](#ch02_images#f0073-01)

```python
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)

>>>
20 19 [15, 9, 8, 7, 6, 4, 1, 0]
```

这段代码更短，更易于阅读，并且不再具有必须在行之间保持同步的易出错的边界索引的脆弱性。

带星号的表达式可以出现在任何位置——开始、中间或结束——因此，当您需要提取一个可选的切片时，您可以随时获得捕获所有解包的好处（请参阅 [Item 9](#ch01#ch01lev1sec9)：“[Consider match for Destructuring in Flow Control, Avoid When if Statements Are Sufficient](#ch01#ch01lev1sec9)” 中的另一个有用情况）：

[点击此处查看代码图像](#ch02_images#f0073-02)

```python
oldest, *others, youngest = car_ages_descending
print(oldest, youngest, others)

*others, second_youngest, youngest = car_ages_descending
print(youngest, second_youngest, others)

>>>
20 0 [19, 15, 9, 8, 7, 6, 4, 1]
0 1 [20, 19, 15, 9, 8, 7, 6, 4]
```

但是，当您在解包赋值中使用带星号的表达式时，您必须至少有一个必需的部分，否则您将收到语法错误。您不能单独使用捕获所有表达式：

[点击此处查看代码图像](#ch02_images#f0073-03)

```python
*others = car_ages_descending

>>>
Traceback ...
SyntaxError: starred assignment target must be in a list or
➥tuple
```

您也不能在单个解包模式中使用多个带星号的表达式：

[点击此处查看代码图像](#ch02_images#f0074-01)

```python
first, *middle, *second_middle, last = [1, 2, 3, 4]

>>>
Traceback ...
SyntaxError: multiple starred expressions in assignment
```

但是，可以在解包赋值语句中使用多个带星号的表达式，只要它们是针对被解包的嵌套结构的不同级别的捕获所有。我不建议这样做（请参阅 [Item 31](#ch05#ch05lev1sec2)：“[Return Dedicated Result Objects Instead of Requiring Function Callers to Unpack More Than Three Variables](#ch05#ch05lev1sec2)” 中的相关指导），但理解它应该有助于您培养带星号表达式在解包赋值中的用法的直觉：

[点击此处查看代码图像](#ch02_images#f0074-02)

```python
car_inventory = {
"Downtown": ("Silver Shadow", "Pinto", "DMC"),
"Airport": ("Skyline", "Viper", "Gremlin", "Nova"),
}
((loc1, (best1, *rest1)),
(loc2, (best2, *rest2))) = car_inventory.items()
print(f"Best at {loc1} is {best1}, {len(rest1)} others")
print(f"Best at {loc2} is {best2}, {len(rest2)} others")

>>>
Best at Downtown is Silver Shadow, 2 others
Best at Airport is Skyline, 3 others
```

带星号的表达式在所有情况下都成为列表实例。如果被解包的序列没有剩余项，则捕获所有部分将是一个空列表。当您处理一个您预先知道至少有 _N_ 个元素的序列时，这特别有用：

[点击此处查看代码图像](#ch02_images#f0074-03)

```python
short_list = [1, 2]
first, second, *rest = short_list
print(first, second, rest)

>>>
1 2 []
```

您还可以使用解包语法解包任意迭代器。这对于基本的多个赋值语句来说并不太有用。例如，在这里我解包了迭代一个长度为 2 的范围的值。这似乎没有用，因为直接赋值给匹配解包模式的静态列表（例如 `[1, 2]`）会更容易：

[点击此处查看代码图像](#ch02_images#f0075-01)

```python
it = iter(range(1, 3))
first, second = it
print(f"{first} and {second}")

>>>
1 and 2
```

但是，随着带星号表达式的加入，解包迭代器的价值变得清晰。例如，这里我有一个生成器，它产生一个 CSV（逗号分隔值）文件的行，该文件包含本周经销商处的所有汽车订单：

[点击此处查看代码图像](#ch02_images#f0075-02)

```python
def generate_csv():
yield ("Date", "Make", "Model", "Year", "Price")
...
```

使用索引和切片处理此生成器的结果是可以的，但它需要多行并且在视觉上很混乱：

[点击此处查看代码图像](#ch02_images#f0075-03)

```python
all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print("CSV Header:", header)
print("Row count: ", len(rows))

>>>
CSV Header: ('Date', 'Make', 'Model', 'Year', 'Price')
Row count:  200
```

使用带星号的表达式进行解包可以轻松地将第一行（标题）与迭代器的其余内容分开处理。这要清晰得多：

[点击此处查看代码图像](#ch02_images#f0075-04)

```python
it = generate_csv()
header, *rows = it
print("CSV Header:", header)
print("Row count: ", len(rows))

>>>
CSV Header: ('Date', 'Make', 'Model', 'Year', 'Price')
Row count:  200
```

但是，请记住，由于带星号的表达式始终转换为 `list`，因此解包迭代器也有可能耗尽您计算机上的所有内存并导致程序崩溃（有关如何调试此问题的说明，请参阅 [Item 115](#ch13#ch13lev1sec8)：“[Use tracemalloc to Understand Memory Usage and Leaks](#ch13#ch13lev1sec8)”）。因此，只有当您有充分理由相信结果数据将全部适合内存时，才应使用迭代器的捕获所有解包（请参阅 [Item 21](#ch03#ch03lev1sec5)：“[Be Defensive when Iterating over Arguments](#ch03#ch03lev1sec5)” 中的另一种方法）。

#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 解包赋值可以包含带星号的表达式，以将未分配给解包模式其他部分的所有值存储在列表中。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 带星号的表达式可以出现在解包模式的任何位置。它们将始终成为包含零个或多个值的列表实例。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 当将列表分成不重叠的块时，捕获所有解包比使用单独的切片和索引语句出错的可能性要小得多。

## Effective Python - 3

## 3

本章深入探讨了如何利用 Python 语言的强大功能来构建和应用 Graph Neural Networks (GNNs) 和 Graph Foundation Models (GFMs)。我们将重点关注 GNNs 的核心概念，包括 Message Passing 机制、Node Embedding 的生成以及常见的 GNNs 架构，如 Graph Convolutional Networks (GCN) 和 Graph Attention Networks (GAT)。

**3.1 GNNs 的核心概念与架构**

本节将详细介绍 GNNs 的基本原理。我们将从 Message Passing 框架入手，解释节点如何通过聚合邻居节点的信息来更新自身的表示。随后，我们将讨论 Node Embedding 的生成过程，以及如何将这些嵌入用于下游任务。此外，本节还将介绍几种经典的 GNNs 架构，包括：

*   **Graph Convolutional Networks (GCN):** 介绍 GCN 的谱域和空域的实现方式，以及其在节点特征传播中的作用。
*   **Graph Attention Networks (GAT):** 阐述 GAT 如何利用注意力机制为邻居节点分配不同的权重，从而提高模型的表达能力。
*   **GraphSAGE:** 介绍 GraphSAGE 的采样和聚合策略，使其能够处理大规模图。

**3.2 GNNs 的应用场景**

本节将展示 GNNs 在各种实际问题中的应用，包括但不限于：

*   **Node Classification:** 利用 GNNs 对图中的节点进行分类，例如社交网络中的用户分类或引文网络中的论文分类。
*   **Link Prediction:** 预测图中节点之间是否存在连接，例如推荐系统中的物品推荐或知识图谱中的关系预测。
*   **Graph Classification:** 对整个图进行分类，例如分子结构分类或社交网络社区检测。
*   **Graph Generation:** 生成新的图结构，例如药物发现中的分子生成。
*   **Graph Anomaly Detection:** 检测图中的异常节点或边。

**3.3 Graph Foundation Models (GFMs) 的兴起**

随着 GNNs 的发展，Graph Foundation Models (GFMs) 作为一种更通用的图表示学习范式应运而生。本节将介绍 GFMs 的核心思想，即通过大规模的 Pre-training 和 Self-supervised Learning 来学习通用的图表示，然后通过 Fine-tuning、In-context Learning、Few-shot Learning 或 Zero-shot Learning 等技术将其应用于各种下游任务。我们将探讨 GFMs 在处理 Heterogeneous Graph 和 Homogeneous Graph 时的优势，以及它们在 Cross-domain Transfer 和 Domain Adaptation 方面的潜力。

**3.4 Python 实现 GNNs 的工具与库**

本节将介绍一系列强大的 Python 库，用于 GNNs 的开发和应用，包括：

*   **PyTorch Geometric (PyG):** 详细介绍 PyG 的核心功能，如图数据结构、GNN 层实现、数据加载器以及各种 GNN 模型示例。
*   **Deep Graph Library (DGL):** 介绍 DGL 的多后端支持和高效的图计算能力，以及其在构建复杂 GNNs 模型时的灵活性。
*   **Spektral:** 介绍 Spektral 如何将 GNNs 与 Keras 和 TensorFlow 集成，提供便捷的图神经网络开发体验。

我们将通过实际的代码示例，演示如何使用这些库来构建和训练 GNNs 模型，并解决实际问题。

**3.5 进阶主题与未来展望**

本节将进一步探讨 GNNs 和 GFMs 的进阶主题，包括：

*   **Multi-modal Learning with GNNs:** 如何将 GNNs 与其他模态的数据（如文本、图像）结合，以提升模型性能。
*   **Graph Pooling Techniques:** 介绍不同的图池化方法，用于降低图的维度和提取更高级别的图表示。
*   **Graph Isomorphism Problem:** 讨论图同构问题及其对 GNNs 理论和实践的影响。
*   **Contrastive Learning for Graphs:** 介绍如何利用对比学习来提升 GNNs 的表示能力。
*   **Knowledge Graph Embeddings:** 探讨 GNNs 在知识图谱表示学习中的应用。

最后，我们将对 GNNs 和 GFMs 的未来发展方向进行展望，包括更强大的模型架构、更广泛的应用领域以及更深入的理论研究。

## Effective Python - Loops and Iterators

## Python 高效编程 - 循环与迭代器

程序经常需要处理固定或动态长度的序列数据。作为一种主要的命令式编程语言，Python 通过循环轻松实现序列处理。其通用模式是：在每次循环迭代中，读取存储在变量、列表、字典等中的数据，并执行相应的状态修改或 I/O 操作。对于涉及内置数据类型、容器类型和用户定义类的常见任务，Python 中的循环感觉自然且功能强大。

Python 还支持迭代器，它提供了一种更函数式的风格来处理任意数据流。您可以使用迭代器，它们提供了一个隐藏细节的通用抽象，而不是直接与序列数据的存储方式进行交互。迭代器可以使程序更高效、更易于重构，并能够处理任意大小的数据。Python 还包含通过使用生成器（详见 [第六章](#ch06#ch06)，“推导式与生成器” [第六章](#ch06#ch06)）来组合迭代器和完全自定义其行为的功能。

### 条目 17：优先使用 `enumerate` 而非 `range`

`range` 内置函数对于迭代整数序列的循环很有用。例如，我通过为每个比特位抛硬币来生成一个 32 位随机数：
[点击此处查看代码图像](#ch03_images#f0077-01)
```python
from random import randint

random_bits = 0
for i in range(32):
if randint(0, 1):
random_bits |= 1 << i
print(bin(random_bits))

>>>
0b11101000100100000111000010000001
```
当您有一个要迭代的数据结构时，例如字符串列表，您可以直接循环遍历序列：
[点击此处查看代码图像](#ch03_images#f0078-02)
```python
flavor_list = ["vanilla", "chocolate", "pecan", "strawberry"]
for flavor in flavor_list:
print(f"{flavor} is delicious")

>>>
vanilla is delicious
chocolate is delicious
pecan is delicious
strawberry is delicious
```
通常，您会想要迭代一个列表，同时还想知道列表中当前项的索引。例如，假设我想打印我最喜欢的冰淇淋口味的排名。一种方法是使用 `range` 为列表中的每个位置生成一个偏移量：
[点击此处查看代码图像](#ch03_images#f0078-03)
```python
for i in range(len(flavor_list)):
flavor = flavor_list[i]
print(f"{i + 1}: {flavor}")

>>>
1: vanilla
2: chocolate
3: pecan
4: strawberry
```
与 `flavor_list` 或 `range` 上的 `for` 语句的其他示例相比，这看起来很笨拙。我必须获取列表的长度。我必须索引到数组中。多个步骤使其更难阅读。

Python 提供了 `enumerate` 内置函数来简化这种情况。`enumerate` 使用一个惰性生成器包装任何迭代器（参见 [条目 43](#ch06#ch06lev1sec4)：“考虑使用生成器而不是返回列表” [第六章](#ch06#ch06lev1sec4)）。`enumerate` 产生循环索引和给定迭代器中的下一项的对。在这里，我使用 `next` 内置函数手动推进返回的迭代器来演示它的作用：
```python
it = enumerate(flavor_list)
print(next(it))
print(next(it))

>>>
(0, 'vanilla')
(1, 'chocolate')
```
`enumerate` 产生的每个对都可以在 `for` 语句中简洁地解包（参见 [条目 5](#ch01#ch01lev1sec5)：“优先使用多重赋值解包而非索引” [第一章](#ch01#ch01lev1sec5)，了解其工作原理）。结果代码更加清晰：
[点击此处查看代码图像](#ch03_images#f0079-01)
```python
for i, flavor in enumerate(flavor_list):
print(f"{i + 1}: {flavor}")

>>>
1: vanilla
2: chocolate
3: pecan
4: strawberry
```
通过指定 `enumerate` 用于开始计数的数字（在此例中为 `1`）作为第二个参数，我可以使其更短：
[点击此处查看代码图像](#ch03_images#f0079-02)
```python
for i, flavor in enumerate(flavor_list, 1):
print(f"{i}: {flavor}")
```
#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `enumerate` 为迭代器循环提供了简洁的语法，并允许您在迭代过程中获取每个项的索引。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 优先使用 `enumerate` 而非通过 `range` 循环并索引到序列。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 您可以为 `enumerate` 提供第二个可选参数，用于指定计数的起始数字（默认为零）。

### 条目 18：使用 `zip` 并行处理迭代器

在 Python 中，您经常会遇到许多相关对象的列表。列表推导式可以轻松地通过将表达式应用于每个项来从源列表生成另一个派生列表（参见 [条目 40](#ch06#ch06lev1sec1)：“使用推导式而非 `map` 和 `filter`” [第六章](#ch06#ch06lev1sec1)）。例如，这里我取一个名字列表并创建一个相应的列表，其中包含每个名字的字符数：
[点击此处查看代码图像](#ch03_images#f0079-03)
```python
names = ["Cecilia", "Lise", "Marie"]
counts = [len(n) for n in names]
print(counts)

>>>
[7, 4, 5]
```
派生列表 (`counts`) 中的项通过它们在序列中的相应位置与源列表 (`names`) 中的项相关联。要在单个循环中访问两个列表的项，我可以迭代源列表 (`names`) 的长度，并使用 `range` 生成的偏移量来索引任一列表。例如，这里我使用并行索引来确定哪个名字最长：
[点击此处查看代码图像](#ch03_images#f0080-01)
```python
longest_name = None
max_count = 0

for i in range(len(names)):
count = counts[i]
if count > max_count:
longest_name = names[i]
max_count = count

print(longest_name)

>>>
Cecilia
```
问题在于，整个 `for` 语句在视觉上显得杂乱。索引操作（`names[i]` 和 `counts[i]`）使代码难以阅读。使用相同的循环索引 `i` 来索引两个数组似乎是多余的。您可以使用 `enumerate` 内置函数（参见 [条目 17](#ch03#ch03lev1sec1)：“优先使用 `enumerate` 而非 `range`” [第三章](#ch03#ch03lev1sec1)）来稍微改进这一点，但由于 `counts[i]` 索引操作，它仍然不是理想的：
[点击此处查看代码图像](#ch03_images#f0080-02)
```python
longest_name = None
max_count = 0

for i, name in enumerate(names):  # Changed
count = counts[i]
if count > max_count:
longest_name = name       # Changed
max_count = count
```
为了使代码更清晰，Python 提供了 `zip` 内置函数。`zip` 使用一个惰性生成器包装两个或多个迭代器。`zip` 生成器产生包含每个迭代器中的下一项的元组。这些元组可以直接在 `for` 语句中解包（参见 [条目 5](#ch01#ch01lev1sec5)：“优先使用多重赋值解包而非索引” [第一章](#ch01#ch01lev1sec5) 获取背景信息）。通过消除索引操作，结果代码比上面单独访问两个列表的代码更清晰：
[点击此处查看代码图像](#ch03_images#f0080-03)
```python
longest_name = None
max_count = 0

for name, count in zip(names, counts):  # Changed
if count > max_count:
longest_name = name
max_count = count
```
`zip` 一次消耗一个它包装的迭代器，这意味着它可以与无限长的输入一起使用，而不会导致程序使用过多内存而崩溃（参见 [条目 43](#ch06#ch06lev1sec4)：“考虑使用生成器而不是返回列表” [第六章](#ch06#ch06lev1sec4) 和 [条目 44](#ch06#ch06lev1sec5)：“为大型列表推导式考虑生成器表达式” [第六章](#ch06#ch06lev1sec5)，了解如何创建此类输入）。

但是，需要注意 `zip` 在输入迭代器长度不同时的行为。例如，假设我向 `names` 列表添加了一个新项，但我忘记更新 `counts` 列表。对两个输入列表运行 `zip` 会产生意外结果：
[点击此处查看代码图像](#ch03_images#f0103-04)
```python
names.append("Rosalind")
for name, count in zip(names, counts):
print(name)

>>>
Cecilia
Lise
Marie
```
`"Rosalind"` 的新项不在输出中。为什么？这只是 `zip` 的工作方式。它会一直产生元组，直到任何一个包装的迭代器耗尽为止。其输出仅与其最短的输入一样长。如果过早截断可能成为您程序的问​​题，您可以将 `strict` 关键字参数传递给 `zip`（自 Python 3.10 起的新选项），它会在任何输入在其他输入之前耗尽时导致返回的生成器引发异常：
[点击此处查看代码图像](#ch03_images#f0081-02)
```python
for name, count in zip(names, counts, strict=True):  # Changed
print(name)

>>>
Cecilia
Lise
Marie
Traceback ...
ValueError: zip() argument 2 is shorter than argument 1
```
或者，您可以使用 `itertools` 内置模块中的 `zip_longest` 函数来解决此截断问题，用默认值填充缺失项（参见 [条目 24](#ch03#ch03lev1sec8)：“考虑使用 `itertools` 处理迭代器和生成器” [第三章](#ch03#ch03lev1sec8)）。

#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `zip` 内置函数可用于并行迭代多个迭代器。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `zip` 创建一个惰性生成器，该生成器产生元组；它可以用于无限长的输入。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果您提供的迭代器长度不同，`zip` 会静默地将输出截断为最短的迭代器。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果您想确保不会发生静默截断，并且不匹配的迭代器长度应导致运行时错误，请将 `strict` 关键字参数传递给 `zip`。

### 条目 19：避免在 `for` 和 `while` 循环后使用 `else` 块

Python 循环具有大多数其他编程语言中没有的额外功能：您可以将 `else` 块直接放在循环的重复内部块之后：
```python
for i in range(3):
print("Loop", i)
else:
print("Else block!")

>>>
Loop 0
Loop 1
Loop 2
Else block!
```
令人惊讶的是，`else` 块在循环完成后立即运行。为什么该子句称为 `else`？为什么不叫 `and`？在 `if`/`else` 语句中，`else` 的意思是“如果之前的块未发生，则执行此操作”（参见“[条目 7](#ch01#ch01lev1sec7)：考虑使用条件表达式进行简单的内联逻辑” [第一章](#ch01#ch01lev1sec7)）。在 `try`/`except` 语句中，`except` 具有相同的定义：“如果在尝试之前的块失败，则执行此操作。”

类似地，`try`/`except`/`else` 中的 `else` 也遵循此模式（参见 [条目 80](#ch10#ch10lev1sec1)：“利用 `try`/`except`/`else`/`finally` 的每个块” [第十章](#ch10#ch10lev1sec1)），因为它意味着“如果没有异常需要处理，则执行此操作。” `try`/`finally` 也直观，因为它意味着“尝试之前的块后始终执行此操作。”

鉴于 `else`、`except` 和 `finally` 在 Python 中的所有用途，新程序员可能会假设 `for`/`else` 中的 `else` 部分意味着“如果循环未完成，则执行此操作。”实际上，它恰恰相反。在循环中使用 `break` 语句会跳过 `else` 块：
```python
for i in range(3):
print("Loop", i)
if i == 1:
break
else:
print("Else block!")

>>>
Loop 0
Loop 1
```
另一个令人惊讶的是，如果循环遍历空序列，`else` 块会立即运行：
```python
for x in []:
print("Never runs")
else:
print("For else block!")

>>>
For else block!
```
当 `while` 循环的初始条件为 `False` 时，`else` 块也会运行：
[点击此处查看代码图像](#ch03_images#f0083-01)
```python
while False:
print("Never runs")
else:
print("While else block!")

>>>
While else block!
```
这些行为的理由是，当您搜索某物时，循环后的 `else` 块很有用。例如，假设我想确定两个数字是否互质（即，它们唯一的公约数是 1）。在这里，我遍历每个可能的公约数并测试这些数字。尝试完所有选项后，循环结束。当数字互质时，`else` 块运行，因为循环没有遇到 `break`：
[点击此处查看代码图像](#ch03_images#f0083-02)
```python
a = 4
b = 9
for i in range(2, min(a, b) + 1):
print("Testing", i)
if a % i == 0 and b % i == 0:
print("Not coprime")
break
else:
print("Coprime")

>>>
Testing 2
Testing 3
Testing 4
Coprime
```
实际上，我不会这样写代码。相反，我会写一个辅助函数来执行计算。这样的函数可以使用两种常见样式中的一种来编写。

第一种方法是在找到要查找的条件时提前返回。只有当循环完成时，我才返回默认结果：
[点击此处查看代码图像](#ch03_images#f0084-01)
```python
def coprime(a, b):
for i in range(2, min(a, b) + 1):
if a % i == 0 and b % i == 0:
return False
return True

assert coprime(4, 9)
assert not coprime(3, 6)
```
第二种方法是使用一个结果变量来指示是否在循环中找到了要查找的内容。在这里，我一旦找到某物就立即跳出循环，然后返回该指示变量：
[点击此处查看代码图像](#ch03_images#f0084-02)
```python
def coprime_alternate(a, b):
is_coprime = True
for i in range(2, min(a, b) + 1):
if a % i == 0 and b % i == 0:
is_coprime = False
break
return is_coprime

assert coprime_alternate(4, 9)
assert not coprime_alternate(3, 6)
```
这两种方法对于阅读不熟悉代码的读者来说都更加清晰。根据情况，两者都可能是个不错的选择。然而，您从 `else` 块获得的表达能力并不能抵消您给未来理解您代码的人（包括您自己）带来的负担。像循环这样的简单结构在 Python 中应该是显而易见的。您应该完全避免在循环后使用 `else` 块。

#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 有特殊的语法允许 `else` 块紧跟在 `for` 和 `while` 循环的内部块之后。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 循环后的 `else` 块仅在循环体未遇到 `break` 语句时运行。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 避免在循环后使用 `else` 块，因为它们的行为不直观且可能令人困惑。

### 条目 20：循环结束后切勿使用 `for` 循环变量

当您编写 Python 的 `for` 循环时，您可能会注意到您为迭代创建的变量在循环结束后仍然存在：
```python
for i in range(3):
print(f"Inside {i=}")
print(f"After  {i=}")

>>>
Inside i=0
Inside i=1
Inside i=2
After  i=2
```
您可以利用此循环变量赋值行为来发挥您的优势。例如，这里我通过在列表中搜索它们的索引来实现一个将周期性元素分组的算法：
[点击此处查看代码图像](#ch03_images#f0085-01)
```python
categories = ["Hydrogen", "Uranium", "Iron", "Other"]
for i, name in enumerate(categories):
if name == "Iron":
break
print(i)

>>>
2
```
在这种元素在列表中未找到的情况下，迭代耗尽后将使用最后一个索引将该项分组到“Other”捕获类别中（在此情况下为索引 3）：
[点击此处查看代码图像](#ch03_images#f0085-02)
```python
for i, name in enumerate(categories):
if name == "Lithium":
break
print(i)

>>>
3
```
此算法中的假设是，循环要么找到匹配项并由于 `break` 语句而提前结束，要么循环遍历所有选项并正常完成。不幸的是，还有第三种可能性，即循环从未开始，因为迭代器最初是空的——这可能导致运行时异常：
[点击此处查看代码图像](#ch03_images#f0086-01)
```python
categories = []
for i, name in enumerate(categories):
if name == "Lithium":
break
print(i)

>>>
Traceback ...
NameError: name 'i' is not defined
```
有其他方法可以处理从未处理任何内容的循环（参见 [条目 19](#ch03#ch03lev1sec3)：“避免在 `for` 和 `while` 循环后使用 `else` 块” [第三章](#ch03#ch03lev1sec3)）。但重点是相同的：您不能总是确定循环变量在循环后访问它时是否存在，因此最好在实践中永远不要这样做。

幸运的是（或者也许不幸的是），其他 Python 功能没有这个问题。列表推导式或生成器表达式不会出现循环变量泄漏行为（参见 [条目 40](#ch06#ch06lev1sec1)：“使用推导式而非 `map` 和 `filter`” [第六章](#ch06#ch06lev1sec1) 和 [条目 44](#ch06#ch06lev1sec5)：“为大型列表推导式考虑生成器表达式” [第六章](#ch06#ch06lev1sec5)）。如果您尝试在执行后访问推导式的内部变量，您会发现它们从未出现过，因此您无法无意中遇到此陷阱：
[点击此处查看代码图像](#ch03_images#f0086-02)
```python
my_numbers = [37, 13, 128, 21]
found = [i for i in my_numbers if i % 2 == 0]
print(i)  # Always raises

>>>
Traceback ...
NameError: name 'i' is not defined
```
然而，推导式中的赋值表达式有可能改变这种行为（参见 [条目 42](#ch06#ch06lev1sec3)：“使用推导式中的赋值表达式减少重复” [第六章](#ch06#ch06lev1sec3)）。异常变量也没有泄漏问题，尽管它们本身有些古怪（参见 [条目 84](#ch10#ch10lev1sec5)：“注意异常变量消失” [第十章](#ch10#ch10lev1sec5)）。

#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `for` 循环的循环变量在循环终止后仍可在当前作用域中访问。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果循环从未进行过一次迭代，则循环变量不会在当前作用域中赋值。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 默认情况下，生成器表达式和列表推导式不会泄漏循环变量。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 异常处理程序不会泄漏异常实例变量。

### 条目 21：迭代参数时要谨慎

当函数将对象列表作为参数时，通常需要多次迭代该列表。例如，假设我想分析美国德克萨斯州的旅游人数。假设数据集是每个城市（每年百万）的访客数量。我想计算每个城市获得的旅游总量的百分比。

为此，我需要一个归一化函数，该函数对输入求和以确定每年的总游客数量，然后将每个城市的个人访客数量除以总数，以找到该城市对整体的贡献：
[点击此处查看代码图像](#ch03_images#f0087-01)
```python
def normalize(numbers):
total = sum(numbers)
result = []
for value in numbers:
percent = 100 * value / total
result.append(percent)
return result
```
当给定访问列表时，此函数按预期工作：
[点击此处查看代码图像](#ch03_images#f0087-02)
```python
visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0

>>>
[11.538461538461538, 26.923076923076923, 61.53846153846154]
```
为了扩展此功能，我需要从包含德克萨斯州所有城市的文件中读取数据。我定义了一个生成器来执行此操作，因为这样我以后可以重用相同的函数，当我想要计算世界（一个更大的数据集，内存要求更高）的旅游人数时（参见 [条目 43](#ch06#ch06lev1sec4)：“考虑使用生成器而不是返回列表” [第六章](#ch06#ch06lev1sec4) 获取背景信息）：
[点击此处查看代码图像](#ch03_images#f0087-03)
```python
def read_visits(data_path):
with open(data_path) as f:
for line in f:
yield int(line)
```
令人惊讶的是，对 `read_visits` 生成器的返回值调用 `normalize` 没有任何结果：
[点击此处查看代码图像](#ch03_images#f0088-01)
```python
it = read_visits("my_numbers.txt")
percentages = normalize(it)
print(percentages)

>>>
[]
```
此行为发生是因为迭代器仅产生其结果一次。如果您迭代一个已经引发 `StopIteration` 异常的迭代器或生成器，第二次将不会获得任何结果：
[点击此处查看代码图像](#ch03_images#f0088-02)
```python
it = read_visits("my_numbers.txt")
print(list(it))
print(list(it))  # Already exhausted

>>>
[15, 35, 80]
[]
```
令人困惑的是，当您迭代一个已耗尽的迭代器时，不会引发异常。`for` 循环、`list` 构造函数以及 Python 标准库中的许多其他函数都期望在正常操作期间引发 `StopIteration` 异常。这些函数无法区分没有输出的迭代器和已有输出但现在已耗尽的迭代器。

要解决此问题，您可以显式耗尽输入迭代器，并将其所有内容保留在列表中。然后，您可以根据需要多次迭代数据的列表版本。这是与之前相同的函数，但现在它会防御性地复制输入迭代器：
[点击此处查看代码图像](#ch03_images#f0088-03)
```python
def normalize_copy(numbers):
numbers_copy = list(numbers)  # Copy the iterator
total = sum(numbers_copy)
result = []
for value in numbers_copy:
percent = 100 * value / total
result.append(percent)
return result
```
现在该函数可以正确处理 `read_visits` 生成器的返回值：
[点击此处查看代码图像](#ch03_images#f0088-04)
```python
it = read_visits("my_numbers.txt")
percentages = normalize_copy(it)
print(percentages)
assert sum(percentages) == 100.0

>>>
[11.538461538461538, 26.923076923076923, 61.53846153846154]
```
此方法的问题在于，输入迭代器内容的副本可能非常大。复制迭代器可能导致程序内存不足而崩溃（参见 [条目 115](#ch13#ch13lev1sec8)：“使用 `tracemalloc` 理解内存使用和泄漏” [第十三章](#ch13#ch13lev1sec8)，了解如何调试此问题）。这种潜在的可伸缩性问题破坏了我最初将 `read_visits` 编写为生成器的原因。一种解决方法是接受一个每次调用时都返回新迭代器的函数：
[点击此处查看代码图像](#ch03_images#f0089-02)
```python
def normalize_func(get_iter):
total = sum(get_iter())   # New iterator
result = []
for value in get_iter():  # New iterator
percent = 100 * value / total
result.append(percent)
return result
```
要使用 `normalize_func`，我可以传递一个 `lambda` 表达式，该表达式每次调用时都会生成一个新的生成器迭代器：
[点击此处查看代码图像](#ch03_images#f0089-03)
```python
path = "my_numbers.txt"
percentages = normalize_func(lambda: read_visits(path))
print(percentages)
assert sum(percentages) == 100.0

>>>
[11.538461538461538, 26.923076923076923, 61.53846153846154]
```
虽然这可行，但必须像这样传递 `lambda` 函数很笨拙。实现相同结果的更好方法是定义一个实现迭代器协议的新容器类。

迭代器协议是 Python `for` 循环和相关表达式用来遍历容器类型内容的方式。当 Python 看到像 `for x in foo` 这样的语句时，它实际上会调用 `iter(foo)` 来发现要循环的迭代器。`iter` 内置函数依次调用 `foo.__iter__` 特殊方法。`__iter__` 方法必须返回一个迭代器对象（该对象本身实现 `__next__` 特殊方法）。然后，`for` 循环重复调用迭代器对象上的 `next` 内置函数，直到它耗尽（由引发 `StopIteration` 异常指示）。

这听起来很复杂，但实际上，您可以通过实现 `__iter__` 方法作为生成器来为自己的类启用所有这些行为。在这里，我定义了一个可迭代的容器类，它读取包含旅游数据的文件的内容，并使用 `yield` 一次生成一行数据：
[点击此处查看代码图像](#ch03_images#f0090-01)
```python
class ReadVisits:
def __init__(self, data_path):
self.data_path = data_path

def __iter__(self):
with open(self.data_path) as f:
for line in f:
yield int(line)
```
这个新的容器类型可以无需修改地传递给原始函数：
[点击此处查看代码图像](#ch03_images#f0090-02)
```python
visits = ReadVisits(path)
percentages = normalize(visits)  # Changed
print(percentages)
assert sum(percentages) == 100.0

>>>
[11.538461538461538, 26.923076923076923, 61.53846153846154]
```
这样做是因为 `normalize` 中的 `sum` 方法调用 `ReadVisits.__iter__` 来分配一个新的迭代器对象。用于归一化数字的 `for` 循环也调用 `__iter__` 来分配第二个迭代器对象。这些迭代器中的每一个都将被独立地推进和耗尽，确保每次唯一的迭代都能看到所有输入数据值。此方法的唯一缺点是它会多次读取输入数据。

现在您知道了像 `ReadVisits` 这样的容器的工作原理，您可以编写函数和方法来确保参数不仅仅是迭代器。协议规定，当迭代器传递给 `iter` 内置函数时，`iter` 会返回迭代器本身。相反，当容器类型传递给 `iter` 时，每次都会返回一个新的迭代器对象。因此，您可以测试输入值是否具有此行为，并引发 `TypeError` 来拒绝无法重复迭代的参数：
[点击此处查看代码图像](#ch03_images#f0090-03)
```python
def normalize_defensive(numbers):
if iter(numbers) is numbers:  # An iterator -- bad!
raise TypeError("Must supply a container")
total = sum(numbers)
result = []
for value in numbers:
percent = 100 * value / total
result.append(percent)
return result
```
或者，`collections.abc` 内置模块定义了一个 `Iterator` 类，可以在 `isinstance` 测试中使用它来识别潜在问题（参见 [条目 57](#ch07#ch07lev1sec10)：“继承 `collections.abc` 类以创建自定义容器类型” [第七章](#ch07#ch07lev1sec10)）：
[点击此处查看代码图像](#ch03_images#f0091-02)
```python
from collections.abc import Iterator

def normalize_defensive(numbers):
if isinstance(numbers, Iterator):  # Another way to check
raise TypeError("Must supply a container")
total = sum(numbers)
result = []
for value in numbers:
percent = 100 * value / total
result.append(percent)
return result
```
如果您不想复制完整的输入迭代器（如上面 `normalize_copy` 函数所示），但又需要多次迭代输入数据，那么期望一个容器的方法是理想的。这里，我展示了 `normalize_defensive` 函数如何接受列表、`ReadVisits` 对象或理论上任何遵循迭代器协议的容器：
[点击此处查看代码图像](#ch03_images#f0091-03)
```python
visits_list = [15, 35, 80]
list_percentages = normalize_defensive(visits_list)

visits_obj = ReadVisits(path)
obj_percentages = normalize_defensive(visits_obj)

assert list_percentages == obj_percentages
assert sum(percentages) == 100.0
```
如果输入是迭代器而不是容器，`normalize_defensive` 函数会引发异常：
[点击此处查看代码图像](#ch03_images#f0091-04)
```python
visits = [15, 35, 80]
it = iter(visits)
normalize_defensive(it)

>>>
Traceback ...
TypeError: Must supply a container
```
检查迭代器协议的合规性也适用于异步迭代器（参见 [条目 76](#ch09#ch09lev1sec10)：“了解如何将线程 I/O 移植到 asyncio” [第九章](#ch09#ch09lev1sec10) 获取示例）。

#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 注意那些多次迭代输入参数的函数和方法。如果这些参数是迭代器，您可能会遇到奇怪的行为和丢失的值。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 的迭代器协议定义了容器和迭代器如何与 `iter` 和 `next` 内置函数、`for` 循环和相关表达式进行交互。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 您可以通过实现 `__iter__` 方法作为生成器来轻松定义自己的可迭代容器类型。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果对迭代器调用 `iter` 会产生与传入值相同的返回值，则可以检测到该值是迭代器（而不是容器）。或者，您可以使用 `isinstance` 内置函数以及 `collections.abc.Iterator` 类。

### 条目 22：迭代容器时切勿修改它们；使用副本或缓存代替

Python 中有许多因意外的迭代行为而导致的陷阱（参见 [条目 21](#ch03#ch03lev1sec5)：“迭代参数时要谨慎” [第三章](#ch03#ch03lev1sec5) 获取另一个常见情况）。例如，如果您在迭代字典时向其中添加新项，Python 将引发运行时异常：
[点击此处查看代码图像](#ch03_images#f0092-01)
```python
search_key = "red"
my_dict = {"red": 1, "blue": 2, "green": 3}

for key in my_dict:
if key == "blue":
my_dict["yellow"] = 4  # Causes error

>>>
Traceback ...
RuntimeError: dictionary changed size during iteration
```
如果您在迭代字典时删除其中的一项，也会发生类似的错误：
[点击此处查看代码图像](#ch03_images#f0092-02)
```python
for key in my_dict:
if key == "blue":
del my_dict["green"]  # Causes error

>>>
Traceback ...
RuntimeError: dictionary changed size during iteration
```
如果您在迭代过程中仅更改字典的值而不是添加或删除键，则不会发生错误——这与上述行为令人惊讶地不一致：
[点击此处查看代码图像](#ch03_images#f0093-02)
```python
for key in my_dict:
if key == "blue":
my_dict["green"] = 4  # Okay
print(my_dict)

>>>
{'red': 1, 'blue': 2, 'green': 3}
{'red': 1, 'blue': 2, 'green': 4}
```
集合与字典的工作方式类似，如果您在迭代过程中通过添加或删除项来更改它们的大小，您将在运行时遇到异常：
[点击此处查看代码图像](#ch03_images#f0093-03)
```python
my_set = {"red", "blue", "green"}

for color in my_set:
if color == "blue":
my_set.add("yellow")  # Causes error

>>>
Traceback ...
RuntimeError: Set changed size during iteration
```
然而，`set` 的行为也似乎不一致，因为在迭代过程中尝试添加已存在于集合中的项不会导致任何问题。重新添加是允许的，因为集合的大小没有改变：
[点击此处查看代码图像](#ch03_images#f0093-04)
```python
for color in my_set:
if color == "blue":
my_set.add("green")  # Okay

print(my_set)

>>>
{'green', 'blue', 'red'}
{'green', 'blue', 'red'}
```
与字典一样，并且同样令人惊讶地不一致，列表可以覆盖任何现有索引，而不会出现任何问题：
[点击此处查看代码图像](#ch03_images#f0094-01)
```python
my_list = [1, 2, 3]

for number in my_list:
print(number)
if number == 2:
my_list[0] = -1  # Okay

print(my_list)

>>>
1
[-1, 2, 3]
2
[-1, 2, 3]
3
[-1, 2, 3]
```
但是，如果您尝试在迭代器当前位置之前将元素插入列表，您的代码将陷入无限循环：
[点击此处查看代码图像](#ch03_images#f0094-02)
```python
my_list = [1, 2, 3]
for number in my_list:
print(number)
if number == 2:
my_list.insert(0, 4)  # Causes error

>>>
1
2
2
2
2
2
...
```
然而，在迭代器当前位置之后将元素附加到列表不是问题——基于索引的迭代器还没有到达那里——这再次是令人惊讶地不一致的行为：
[点击此处查看代码图像](#ch03_images#f0094-03)
```python
my_list = [1, 2, 3]

for number in my_list:
print(number)
if number == 2:
my_list.append(4)  # Okay this time

print(my_list)

>>>
1
[1, 2, 3]
2
[1, 2, 3, 4]
3
[1, 2, 3, 4]
```
查看上面的每个示例，很难猜测代码在所有情况下是否都能正常工作。在修改点根据算法输入而变化的情况下，在迭代过程中修改容器尤其容易出错。在某些情况下它会起作用，在其他情况下则会出错。因此，我的建议是永远不要在迭代它们时修改容器。

如果您由于算法的性质仍然需要在迭代过程中进行修改，您应该只制作要迭代的容器的副本，并将修改应用于原始容器（参见 [条目 30](#ch05#ch05lev1sec1)：“知道函数参数可以被修改” [第五章](#ch05#ch05lev1sec1)）。例如，对于字典，我可以复制键：
[点击此处查看代码图像](#ch03_images#f0095-02)
```python
my_dict = {"red": 1, "blue": 2, "green": 3}

keys_copy = list(my_dict.keys())  # Copy
for key in keys_copy:             # Iterate over copy
if key == "blue":
my_dict["green"] = 4      # Modify original dict

print(my_dict)

>>>
{'red': 1, 'blue': 2, 'green': 4}
```
对于列表，我可以复制整个容器：
[点击此处查看代码图像](#ch03_images#f0095-03)
```python
my_list = [1, 2, 3]

list_copy = list(my_list)     # Copy
for number in list_copy:      # Iterate over copy
print(number)
if number == 2:
my_list.insert(0, 4)  # Inserts in original list

print(my_list)

>>>
1
[4, 1, 2, 3]
2
[4, 1, 2, 3]
3
[4, 1, 2, 3]
```
对于集合，同样的方法也适用：
[点击此处查看代码图像](#ch03_images#f0096-01)
```python
my_set = {"red", "blue", "green"}

set_copy = set(my_set)        # Copy
for color in set_copy:        # Iterate over copy
if color == "blue":
my_set.add("yellow")  # Add to original set

print(my_set)

>>>
{'yellow', 'green', 'blue', 'red'}
```
对于某些极其庞大的容器，复制可能太慢（参见 [条目 92](#ch11#ch11lev1sec1)：“在优化前进行性能分析” [第十一章](#ch11#ch11lev1sec1)，了解如何验证您的假设）。处理性能不佳的一种方法是将修改分阶段存储在单独的容器中，然后在迭代结束后将更改合并到主数据结构中。例如，这里我修改了一个单独的字典，然后使用 `update` 方法将更改合并到原始字典中：
[点击此处查看代码图像](#ch03_images#f0096-02)
```python
my_dict = {"red": 1, "blue": 2, "green": 3}
modifications = {}

for key in my_dict:
if key == "blue":
modifications["green"] = 4  # Add to staging

my_dict.update(modifications)       # Merge modifications
print(my_dict)

>>>
{'red': 1, 'blue': 2, 'green': 4}
```
分阶段修改的问题在于它们在迭代过程中不会立即在原始容器中可见。如果循环中的逻辑依赖于修改的即时可见性，代码将无法按预期工作。例如，这里程序员的意图可能是让 `"yellow"` 出现在结果字典中，但它不会在那里，因为修改在迭代过程中不可见：
[点击此处查看代码图像](#ch03_images#f0096-03)
```python
my_dict = {"red": 1, "blue": 2, "green": 3}
modifications = {}
for key in my_dict:
if key == "blue":
modifications["green"] = 4
value = my_dict[key]
if value == 4:               # This condition is never true
modifications["yellow"] = 5

my_dict.update(modifications)    # Merge modifications
print(my_dict)

>>>
{'red': 1, 'blue': 2, 'green': 4}
```
可以通过在原始容器 (`my_dict`) 和修改容器 (`modifications`) 中查找最新值来解决此代码，基本上将暂存字典视为中间缓存：
[点击此处查看代码图像](#ch03_images#f0097-02)
```python
my_dict = {"red": 1, "blue": 2, "green": 3}
modifications = {}

for key in my_dict:
if key == "blue":
modifications["green"] = 4
value = my_dict[key]
other_value = modifications.get(key)  # Check cache
if value == 4 or other_value == 4:
modifications["yellow"] = 5

my_dict.update(modifications)             # Merge modifications
print(my_dict)

>>>
{'red': 1, 'blue': 2, 'green': 4, 'yellow': 5}
```
这种类型的协调有效，但很难推广到所有情况。在开发此类算法时，您需要考虑您的特定约束。这可能很难正确处理，尤其是在所有边缘情况下，因此我建议编写自动化测试来验证正确性（参见 [条目 109](#ch13#ch13lev1sec2)：“优先使用集成测试而非单元测试” [第十三章](#ch13#ch13lev1sec2)）。同样，您可以使用微基准测试来衡量各种方法的性能并选择最佳方法（参见 [条目 93](#ch11#ch11lev1sec2)：“使用 `timeit` 微基准测试优化性能关键代码” [第十一章](#ch11#ch11lev1sec2)）。

#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在迭代列表、字典和集合时添加或删除元素可能会导致难以预测的运行时错误。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 您可以迭代容器的副本，以避免可能由迭代期间的修改引起的运行时错误。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果您需要避免复制以提高性能，可以将修改分阶段存储在第二个容器缓存中，然后将其合并到原始容器中。

### 条目 23：将迭代器传递给 `any` 和 `all` 以实现高效的短路逻辑

Python 是构建逻辑推理程序的绝佳语言。例如，想象一下我正在尝试分析抛硬币的性质。我可以定义一个函数，每次调用时都会返回一个随机的抛硬币结果——正面为 `True`，反面为 `False`：
[点击此处查看代码图像](#ch03_images#f0098-01)
```python
import random

def flip_coin():
if random.randint(0, 1) == 0:
return "Heads"
else:
return "Tails"

def flip_is_heads():
return flip_coin() == "Heads"
```
如果我想抛 20 次硬币，并查看是否所有结果都是连续的正面，我可以使用简单的列表推导式（参见 [条目 40](#ch06#ch06lev1sec1)：“使用推导式而非 `map` 和 `filter`” [第六章](#ch06#ch06lev1sec1)）和成员资格测试（使用 `in` 运算符）（参见 [条目 57](#ch07#ch07lev1sec10)：“继承 `collections.abc` 类以创建自定义容器类型” [第七章](#ch07#ch07lev1sec10)）：
[点击此处查看代码图像](#ch03_images#f0098-02)
```python
flips = [flip_is_heads() for _ in range(20)]
all_heads = False not in flips
```
然而，这 20 次抛硬币产生全是正面的序列的几率大约是百万分之一——极其罕见。如果抛硬币在某种程度上很昂贵，由于它在看到反面结果后仍然继续抛硬币，我几乎总是会在列表推导式中浪费大量资源在不必要的工作上。我可以通过使用一个一旦看到非正面结果就终止抛硬币序列的循环来改善这种情况：
```python
all_heads = True
for _ in range(100):
if not flip_is_heads():
all_heads = False
break
```
虽然这段代码更有效率，但它比之前的列表推导式要长得多。为了保持代码简短同时提前终止执行，我可以使用 `all` 内置函数。`all` 会遍历一个迭代器，检查每一项是否为真（参见 [条目 7](#ch01#ch01lev1sec7)：“考虑使用条件表达式进行简单的内联逻辑” [第一章](#ch01#ch01lev1sec7) 获取背景信息），并在遇到假值时立即停止处理。`all` 始终返回布尔值 `True` 或 `False`，这与 `and` 逻辑运算符返回需要测试的最后一个值不同：
```python
print("All truthy:")
print(all([1, 2, 3]))
print(1 and 2 and 3)

print("One falsey:")
print(all([1, 0, 3]))
print(1 and 0 and 3)

>>>
All truthy:
True
3
One falsey:
False
0
```
使用 `all` 内置函数，我可以使用生成器表达式（参见 [条目 44](#ch06#ch06lev1sec5)：“为大型列表推导式考虑生成器表达式” [第六章](#ch06#ch06lev1sec5)）重写抛硬币循环。一旦 `flip_is_heads` 函数返回 `False`，它就会停止进行更多的抛硬币：
[点击此处查看代码图像](#ch03_images#f0099-01)
```python
all_heads = all(flip_is_heads() for _ in range(20))
```
至关重要的是，如果我传递列表推导式而不是生成器表达式（注意周围的 `[` 和 `]` 方括号），代码将在将 20 个抛硬币结果传递给 `all` 函数之前创建一个列表。计算结果将相同，但代码的性能会差很多：
[点击此处查看代码图像](#ch03_images#f0099-02)
```python
all_heads = all([flip_is_heads() for _ in range(20)])  # Wrong
```
或者，我可以使用生成器函数（参见 [条目 43](#ch06#ch06lev1sec4)：“考虑使用生成器而不是返回列表” [第六章](#ch06#ch06lev1sec4)）或任何其他类型的迭代器来实现类似的效率：
[点击此处查看代码图像](#ch03_images#f0100-01)
```python
def repeated_is_heads(count):
for _ in range(count):
yield flip_is_heads()  # Generator

all_heads = all(repeated_is_heads(20))
```
一旦 `repeated_is_heads` 产生一个 `False` 值，`all` 内置函数将停止向前移动生成器迭代器并返回 `False`。传递给 `all` 的生成器迭代器的引用将被丢弃并进行垃圾回收，确保循环永远不会完成（参见 [条目 89](#ch10#ch10lev1sec10)：“始终将资源传递给生成器并让调用者在外部清理它们” [第十章](#ch10#ch10lev1sec10) 了解详细信息）。

有时，您会有一个函数，其行为与 `flip_is_heads` 相反，它大多数时候返回 `False`，只有在满足特定条件时才返回 `True`。在这里，我定义了一个具有这种行为的函数：
[点击此处查看代码图像](#ch03_images#f0100-02)
```python
def flip_is_tails():
return flip_coin() == "Tails"
```
为了使用此函数来检测连续的正面，`all` 将不起作用。相反，我可以使用 `any` 内置函数。`any` 同样会遍历一个迭代器，但它会在看到第一个真值时终止。`any` 始终返回一个布尔值，这与它镜像的 `or` 逻辑运算符不同：
```python
print("All falsey:")
print(any([0, False, None]))
print(0 or False or None)

print("One truthy:")
print(any([None, 3, 0]))
print(None or 3 or 0)

>>>
All falsey:
False
None
One truthy:
True
3
```
使用 `any`，我可以在生成器表达式中使用 `flip_is_tails` 来计算与之前相同的结果：
[点击此处查看代码图像](#ch03_images#f0101-01)
```python
all_heads = not any(flip_is_tails() for _ in range(20))
```
或者我可以创建一个类似的生成器函数：
[点击此处查看代码图像](#ch03_images#f0101-02)
```python
def repeated_is_tails(count):
for _ in range(count):
yield flip_is_tails()

all_heads = not any(repeated_is_tails(20))
```
何时选择 `any` 与 `all`？这取决于您正在做什么以及测试您关心的条件的难度。如果您想提前以 `True` 值结束，请使用 `any`。如果您想提前以 `False` 值结束，请使用 `all`。最终，这些内置函数是等效的，正如布尔逻辑的德摩根定律所示：
[点击此处查看代码图像](#ch03_images#f0101-03)
```python
for a in (True, False):
for b in (True, False):
assert any([a, b]) == (not all([not a, not b]))
assert all([a, b]) == (not any([not a, not b]))
```
无论如何，您都应该能够找到一种方法来最小化工作量，方法是适当地使用 `any` 或 `all`。还有额外的内置模块用于以智能方式操作迭代器和生成器，以最大化性能和效率（参见 [条目 24](#ch03#ch03lev1sec8)：“考虑使用 `itertools` 处理迭代器和生成器” [第三章](#ch03#ch03lev1sec8)）。

#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `all` 内置函数在所有提供的项都为真时返回 `True`。它在遇到假值时停止处理输入并返回 `False`。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `any` 内置函数的工作方式类似，但逻辑相反：如果所有项都为假，则返回 `False`，并在看到真值时提前以 `True` 结束。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `any` 和 `all` 始终返回布尔值 `True` 或 `False`，而 `or` 和 `and` 逻辑运算符则返回需要测试的最后一个项。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在 `any` 或 `all` 中使用列表推导式而不是生成器表达式会破坏这些函数的效率优势。

### 条目 24：考虑使用 `itertools` 处理迭代器和生成器

`itertools` 内置模块包含大量用于组织和交互迭代器的有用函数（参见 [条目 43](#ch06#ch06lev1sec4)：“考虑使用生成器而不是返回列表” [第六章](#ch06#ch06lev1sec4) 和 [条目 21](#ch03#ch03lev1sec5)：“迭代参数时要谨慎” [第三章](#ch03#ch03lev1sec5) 获取背景信息）：
```python
import itertools
```
每当您发现自己处理棘手的迭代代码时，都值得再次查看 `itertools` 文档，看看是否有任何可以使用的内容（参见 <https://docs.python.org/3/library/itertools.html>）。以下各节描述了您应该了解的三个主要类别中的最重要函数。

#### 连接迭代器

`itertools` 内置模块包含许多用于连接迭代器的函数。

##### `chain`

使用 `chain` 将多个迭代器合并为一个顺序迭代器。本质上，这会将提供的输入迭代器展平成一个项迭代器：
[点击此处查看代码图像](#ch03_images#f0102-01)
```python
it = itertools.chain([1, 2, 3], [4, 5, 6])
print(list(it))

>>>
[1, 2, 3, 4, 5, 6]
```
还有一个此函数的替代版本，`chain.from_iterable`，它消耗一个迭代器迭代器，并生成一个单一的展平输出迭代器，其中包含所有迭代器的内容：
[点击此处查看代码图像](#ch03_images#f0102-02)
```python
it1 = [i * 3 for i in ("a", "b", "c")]
it2 = [j * 2 for j in ("x", "y", "z")]
nested_it = [it1, it2]
output_it = itertools.chain.from_iterable(nested_it)
print(list(output_it))

>>>
['aaa', 'bbb', 'ccc', 'xx', 'yy', 'zz']
```
##### `repeat`

使用 `repeat` 永远输出一个值，或者使用第二个可选参数指定最大次数：
[点击此处查看代码图像](#ch03_images#f0103-01)
```python
it = itertools.repeat("hello", 3)
print(list(it))

>>>
['hello', 'hello', 'hello']
```
##### `cycle`

使用 `cycle` 永远重复迭代器的项：
[点击此处查看代码图像](#ch03_images#f0103-02)
```python
it = itertools.cycle([1, 2])
result = [next(it) for _ in range(10)]
print(result)

>>>
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
```
##### `tee`

使用 `tee` 将单个迭代器分割成第二个参数指定的并行迭代器数量。如果迭代器进展速度不同，此函数的内存使用量将会增长，因为需要缓冲来临时存储待处理的项：
[点击此处查看代码图像](#ch03_images#f0103-03)
```python
it1, it2, it3 = itertools.tee(["first", "second"], 3)
print(list(it1))
print(list(it2))
print(list(it3))

>>>
['first', 'second']
['first', 'second']
['first', 'second']
```
##### `zip_longest`

此 `zip` 内置函数的变体在迭代器耗尽时返回一个占位符值，如果迭代器长度不同，可能会发生这种情况（参见 [条目 18](#ch03#ch03lev1sec2)：“使用 `zip` 并行处理迭代器” [第三章](#ch03#ch03lev1sec2)，了解 `strict` 参数如何提供类似行为）：
[点击此处查看代码图像](#ch03_images#f0103-04)
```python
keys = ["one", "two", "three"]
values = [1, 2]

normal = list(zip(keys, values))
print("zip:        ", normal)

it = itertools.zip_longest(keys, values, fillvalue="nope")
longest = list(it)
print("zip_longest:", longest)

>>>
zip:         [('one', 1), ('two', 2)]
zip_longest: [('one', 1), ('two', 2), ('three', 'nope')]
```
#### 从迭代器过滤项

`itertools` 内置模块包含许多用于过滤迭代器项的函数。

##### `islice`

使用 `islice` 通过数字索引切片迭代器而不进行复制。您可以指定结束、开始和结束或开始、结束和步长。`islice` 的行为类似于标准序列切片和跨步（参见 [条目 14](#ch02#ch02lev1sec5)：“了解如何切片序列” [第二章](#ch02#ch02lev1sec5) 和 [条目 15](#ch02#ch02lev1sec6)：“避免在单个表达式中进行跨步和切片” [第二章](#ch02#ch02lev1sec6)）：
[点击此处查看代码图像](#ch03_images#f0104-02)
```python
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_five = itertools.islice(values, 5)
print("First five: ", list(first_five))

middle_odds = itertools.islice(values, 2, 8, 2)
print("Middle odds:", list(middle_odds))

>>>
First five:  [1, 2, 3, 4, 5]
Middle odds: [3, 5, 7]
```
##### `takewhile`

`takewhile` 从迭代器返回项，直到谓词函数对某个项返回 `False`，此时迭代器的所有项都将被消耗但不会返回（参见 [条目 39](#ch05#ch05lev1sec10)：“优先使用 `functools.partial` 而非 `lambda` 表达式作为粘合函数” [第五章](#ch05#ch05lev1sec10) 了解更多关于定义谓词的信息）：
[点击此处查看代码图像](#ch03_images#f0104-03)
```python
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.takewhile(less_than_seven, values)
print(list(it))

>>>
[1, 2, 3, 4, 5, 6]
```
##### `dropwhile`

`dropwhile` 是 `takewhile` 的反向操作，它会跳过迭代器中的项，直到谓词函数首次返回 `False`，此时将返回迭代器的所有项：
[点击此处查看代码图像](#ch03_images#f0105-02)
```python
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.dropwhile(less_than_seven, values)
print(list(it))

>>>
[7, 8, 9, 10]
```
##### `filterfalse`

`filterfalse` 是 `filter` 内置函数的反向操作，当谓词函数返回 `False` 时，它会返回迭代器的所有项：
[点击此处查看代码图像](#ch03_images#f0105-03)
```python
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = lambda x: x % 2 == 0

filter_result = filter(evens, values)
print("Filter:      ", list(filter_result))

filter_false_result = itertools.filterfalse(evens, values)
print("Filter false:", list(filter_false_result))

>>>
Filter:       [2, 4, 6, 8, 10]
Filter false: [1, 3, 5, 7, 9]
```
#### 组合迭代器中的项

`itertools` 内置模块包含许多用于组合迭代器项的函数。

##### `batched`

使用 `batched` 创建一个迭代器，该迭代器输出来自单个输入迭代器的固定大小、非重叠项组。第二个参数是批次大小。这在处理数据以提高效率或满足其他约束（如数据大小限制）时特别有用：
[点击此处查看代码图像](#ch03_images#f0106-01)
```python
it = itertools.batched([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print(list(it))

>>>
[(1, 2, 3), (4, 5, 6), (7, 8, 9)]
```
如果项不能完美分割，由迭代器产生的最后一组可能比指定的批次大小小：
[点击此处查看代码图像](#ch03_images#f0106-02)
```python
it = itertools.batched([1, 2, 3], 2)
print(list(it))

>>>
[(1, 2), (3,)]
```
##### `pairwise`

当您需要迭代输入迭代器中的每对相邻项时，请使用 `pairwise`。这些对包含重叠，因此除了两端之外的每一项都会在输出迭代器中出现两次：一次作为对的第一个位置，另一次作为第二个位置。这在编写需要逐步遍历顶点或端点的顺序集图遍历算法时可能很有帮助：
[点击此处查看代码图像](#ch03_images#f0106-03)
```python
route = ["Los Angeles", "Bakersfield", "Modesto", "Sacramento"]
it = itertools.pairwise(route)
print(list(it))

>>>
[('Los Angeles', 'Bakersfield'), ('Bakersfield', 'Modesto'),
➥('Modesto', 'Sacramento')]
```
##### `accumulate`

`accumulate` 通过应用一个接受两个参数的函数，将迭代器中的项折叠到运行值中。它为每个输入值输出当前累积的结果：
[点击此处查看代码图像](#ch03_images#f0106-04)
```python
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_reduce = itertools.accumulate(values)
print("Sum:   ", list(sum_reduce))

def sum_modulo_20(first, second):
output = first + second
return output % 20
modulo_reduce = itertools.accumulate(values, sum_modulo_20)
print("Modulo:", list(modulo_reduce))

>>>
Sum:    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
Modulo: [1, 3, 6, 10, 15, 1, 8, 16, 5, 15]
```
这本质上与 `functools` 内置模块中的 `reduce` 函数相同，但输出是逐步产生的。默认情况下，如果未指定二进制函数，它会对输入求和。
##### `product`

`product` 返回一个或多个迭代器中项的笛卡尔积，这是使用深度嵌套列表推导式的一个不错的替代方案（参见 [条目 41](#ch06#ch06lev1sec2)：“避免在推导式中使用超过两个控制子表达式” [第六章](#ch06#ch06lev1sec2)，了解为什么避免它们）：
[点击此处查看代码图像](#ch03_images#f0107-02)
```python
single = itertools.product([1, 2], repeat=2)
print("Single:  ", list(single))

multiple = itertools.product([1, 2], ["a", "b"])
print("Multiple:", list(multiple))

>>>
Single:   [(1, 1), (1, 2), (2, 1), (2, 2)]
Multiple: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```
##### `permutations`

`permutations` 返回长度为 _N_（第二个参数）的唯一有序排列，其中包含来自迭代器的项：
[点击此处查看代码图像](#ch03_images#f0107-03)
```python
it = itertools.permutations([1, 2, 3, 4], 2)
print(list(it))

>>>
[(1, 2),
(1, 3),
(1, 4),
(2, 1),
(2, 3),
(2, 4),
(3, 1),
(3, 2),
(3, 4),
(4, 1),
(4, 2),
(4, 3)]
```
##### `combinations`

`combinations` 返回长度为 _N_（第二个参数）的无序组合，其中包含来自迭代器的不重复项：
[点击此处查看代码图像](#ch03_images#f0108-01)
```python
it = itertools.combinations([1, 2, 3, 4], 2)
print(list(it))

>>>
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```
##### `combinations_with_replacement`

`combinations_with_replacement` 与 `combinations` 相同，但允许重复值。此版本与 `permutations` 函数的区别在于，它允许同一输入在输出组中重复多次（即，请参见下图中输出的 `(1, 1)`）：
[点击此处查看代码图像](#ch03_images#f0108-02)
```python
it = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
print(list(it))

>>>
[(1, 1),
(1, 2),
(1, 3),
(1, 4),
(2, 2),
(2, 3),
(2, 4),
(3, 3),
(3, 4),
(4, 4)]
```
#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `itertools` 函数分为三个主要类别，用于处理迭代器和生成器：连接迭代器、过滤它们输出的项以及组合项。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 官方文档中提供了更高级的函数、其他参数和有用的配方。
---
<a role="toc_link" id="ch04"></a>

## Effective Python - 4

## 4

本章深入探讨了如何利用 Python 提升 **Graph Neural Networks (GNNs)** 的效率和性能。我们将重点关注 GNNs 的核心组件和常用技术，并展示如何通过 Python 实现这些概念。

**4.1 GNNs 的核心概念与 Python 实现**

本节将介绍 GNNs 的基本原理，包括 **Message Passing** 机制，以及如何使用 Python 库（如 PyTorch Geometric 或 DGL）来实现这些机制。我们将讨论 **Node Embedding** 的生成过程，以及不同类型的 GNNs，如 **Graph Convolutional Networks (GCN)** 和 **Graph Attention Networks (GAT)**。

**4.2 GNNs 的预训练与微调**

本节将重点介绍 **Self-supervised Learning** 在 GNNs 中的应用，特别是 **Pre-training** 的策略。我们将讨论如何利用 **Contrastive Learning** 等方法来学习有用的 **Node Embedding**，并为下游任务（如 **Node Classification**、**Link Prediction**）做准备。此外，我们还将探讨 **Fine-tuning** 的过程，以及如何将预训练的 GNN 模型应用于特定的任务。

**4.3 Graph Foundation Models (GFMs) 与迁移学习**

本节将介绍 **Graph Foundation Models (GFMs)** 的概念，以及它们在处理各种图结构数据方面的潜力。我们将讨论 **In-context Learning**、**Few-shot Learning** 和 **Zero-shot Learning** 等技术在 GFMs 中的应用，以及如何实现 **Cross-domain Transfer** 和 **Domain Adaptation**。

**4.4 GNNs 在不同图类型上的应用**

本节将探讨 GNNs 如何应用于不同类型的图，包括 **Homogeneous Graph** 和 **Heterogeneous Graph**。我们将讨论 **Knowledge Graph** 的表示学习，以及 GNNs 在处理复杂图结构时的挑战和解决方案。

**4.5 GNNs 的高级技术与应用**

本节将介绍一些 GNNs 的高级技术，如 **Graph Pooling**，以及它们在 **Graph Classification** 等任务中的作用。我们还将简要提及 GNNs 在 **Graph Generation**、**Graph Anomaly Detection** 和 **Multi-modal Learning** 等领域的应用。

**4.6 性能优化与扩展性**

本节将讨论如何优化 GNN 模型的性能，包括内存管理和计算效率。我们将探讨如何处理大规模图数据，以及如何利用分布式计算来扩展 GNN 的应用范围。

**4.7 案例研究与未来展望**

本节将通过具体的案例研究，展示 GNNs 在实际问题中的应用，例如社交网络分析、药物发现等。最后，我们将对 GNNs 的未来发展方向进行展望，包括对 **Graph Isomorphism** 等问题的探索。

## Effective Python - Dictionaries

## 字典

Python 中的字典类型是列表和序列的自然补充，它将查找键映射到相应的值（通常称为“关联数组”或“哈希表”）。其多功能性使字典成为簿记的理想选择：动态跟踪新的和变化的数据片段以及它们之间的关系。在编写新程序时，使用字典是开始的好方法，在您不确定可能需要哪些其他数据结构或类之前。
字典在添加和删除项目时提供恒定时间（摊销）性能，这比简单的列表本身能达到的要好得多。因此，可以理解的是，字典是 Python 实现其面向对象特性的核心数据结构。Python 还具有特殊的语法和相关的内置模块，这些模块增强了字典的功能，超出了您在其他语言中对简单哈希表类型的预期。

### Item 25：在依赖字典插入顺序时要小心

在 Python 3.5 及更早版本中，迭代字典实例会以任意顺序返回其键。迭代顺序不会匹配最初插入字典的顺序。例如，在这里我使用 Python 3.5 创建了一个将动物名称映射到其相应幼崽名称的字典：
[点击此处查看代码图像](#ch04_images#f0109-01)
```
# Python 3.5
baby_names = {
"cat": "kitten",
"dog": "puppy",
}
print(baby_names)

>>>
{'dog': 'puppy', 'cat': 'kitten'}
```
当我创建字典时，键的顺序是“cat”、“dog”，但当我打印它时，键的顺序是相反的：“dog”、“cat”。这种行为令人惊讶，使重现测试用例更加困难，增加了调试的难度，并且对 Python 新手来说尤其令人困惑。
发生这种情况是因为旧版本 Python 中的字典类型通过 `hash` 内置函数和在 Python 解释器进程开始执行时分配的随机种子相结合来实现其哈希表算法。总而言之，这些行为导致字典顺序不匹配插入顺序，并在程序执行之间随机洗牌。
从 Python 3.6 开始，并且自 3.7 版本起正式成为 Python 规范的一部分，字典会保留插入顺序。现在，此代码始终以程序员最初创建它的方式打印字典：
[点击此处查看代码图像](#ch04_images#f0110-02)
```
baby_names = {
"cat": "kitten",
"dog": "puppy",
}
print(baby_names)

>>>
{'cat': 'kitten', 'dog': 'puppy'}
```
在 Python 3.5 及更早版本中，`dict` 提供的所有依赖于迭代顺序的方法，包括 `keys`、`values`、`items` 和 `popitem`，同样表现出这种看起来随机的行为：
[点击此处查看代码图像](#ch04_images#f0110-03)
```
# Python 3.5
print(list(baby_names.keys()))
print(list(baby_names.values()))
print(list(baby_names.items()))
print(baby_names.popitem())  # 随机选择一个项目

>>>
['dog', 'cat']
['puppy', 'kitten']
[('dog', 'puppy'), ('cat', 'kitten')]
('dog', 'puppy')
```
这些方法现在提供一致的插入顺序，您可以在编写程序时依赖此行为：
[点击此处查看代码图像](#ch04_images#f0111-01)
```
print(list(baby_names.keys()))
print(list(baby_names.values()))
print(list(baby_names.items()))
print(baby_names.popitem())  # 最后插入的项目

>>>
['cat', 'dog']
['kitten', 'puppy']
[('cat', 'kitten'), ('dog', 'puppy')]
('dog', 'puppy')
```
此更改对其他依赖于 `dict` 类型及其特定实现的 Python 功能产生了许多影响。
函数关键字参数，包括 `**kwargs` 捕获参数（请参阅 [Item 35](#ch05#ch05lev1sec6)：“[使用关键字参数提供可选行为](#ch05#ch05lev1sec6)” 和 [Item 37](#ch05#ch05lev1sec8)：“[通过关键字专用和位置专用参数强制清晰](#ch05#ch05lev1sec8)”），在早期 Python 版本中以看似随机的顺序出现，这使得调试函数调用更加困难：
[点击此处查看代码图像](#ch04_images#f0111-02)
```
# Python 3.5
def my_func(**kwargs):
for key, value in kwargs.items():
print("%s = %s" % (key, value))

my_func(goose="gosling", kangaroo="joey")

>>>
kangaroo = joey
goose = gosling
```
现在在最新版本的 Python 中，关键字参数的顺序始终得以保留，以匹配程序员最初调用函数的方式：
[点击此处查看代码图像](#ch04_images#f0111-03)
```
def my_func(**kwargs):
for key, value in kwargs.items():
print(f"{key} = {value}")

my_func(goose="gosling", kangaroo="joey")

>>>
goose = gosling
kangaroo = joey
```
类也使用 `dict` 类型来存储其实例字典。在以前的 Python 版本中，`object` 字段显示了随机化行为：
[点击此处查看代码图像](#ch04_images#f0112-02)
```
# Python 3.5
class MyClass:
def __init__(self):
self.alligator = "hatchling"
self.elephant = "calf"

a = MyClass()
for key, value in a.__dict__.items():
print("%s = %s" % (key, value))

>>>
elephant = calf
alligator = hatchling
```
同样，您现在可以假定这些实例字段的赋值顺序将反映在 `__dict__` 中：
[点击此处查看代码图像](#ch04_images#f0112-03)
```
class MyClass:
def __init__(self):
self.alligator = "hatchling"
self.elephant = "calf"

a = MyClass()
for key, value in a.__dict__.items():
print(f"{key} = {value}")

>>>
alligator = hatchling
elephant = calf
```
字典保留插入顺序的方式现在是 Python 语言规范的一部分。对于上述语言特性，您可以依赖此行为，甚至可以将其作为您为类和函数设计的 API 的一部分（请参阅 [Item 65](#ch08#ch08lev1sec8)：“[考虑类体定义顺序以建立属性之间的关系](#ch08#ch08lev1sec8)” 获取示例）。
注意
长期以来，`collections` 内置模块一直有一个 `OrderedDict` 类，该类可以保留插入顺序。尽管此类行为与标准 `dict` 类型（自 Python 3.7 起）相似，但 `OrderedDict` 的性能特征却大不相同。如果您需要处理高频率的键插入和 `popitem` 调用（例如，实现最近最少使用缓存），`OrderedDict` 可能比标准 Python `dict` 类型更适合（请参阅 [Item 92](#ch11#ch11lev1sec1)：“[优化前进行性能分析](#ch11#ch11lev1sec1)” 关于如何确保您需要它）。
但是，在处理字典时，您不应总是假定插入顺序行为会存在。Python 使程序员可以轻松定义自己的自定义容器类型，这些类型可以模仿与 `list`、`dict` 等类型匹配的标准 _协议_（请参阅 [Item 57](#ch07#ch07lev1sec10)：“[为自定义容器类型继承 collections.abc 类](#ch07#ch07lev1sec10)”）。Python 不是静态类型的，因此大多数代码依赖于 _鸭子类型_——对象的行为是其事实上的类型——而不是严格的类层次结构（请参阅 [Item 3](#ch01#ch01lev1sec3)：“[永远不要期望 Python 在编译时检测错误](#ch01#ch01lev1sec3)”）。这可能导致令人惊讶的陷阱。
例如，假设我正在编写一个程序来显示最可爱的幼崽动物比赛结果。在这里，我从一个包含每个动物总票数的字典开始：
```
votes = {
"otter": 1281,
"polar bear": 587,
"fox": 863,
}
```
现在，我定义了一个函数来处理此投票数据，并将每个动物名称的排名保存在提供的空字典中。在这种情况下，字典可以是为 UI 元素提供支持的数据模型：
[点击此处查看代码图像](#ch04_images#f0113-01)
```
def populate_ranks(votes, ranks):
names = list(votes.keys())
names.sort(key=votes.get, reverse=True)
for i, name in enumerate(names, 1):
ranks[name] = i
```
我还必须有一个函数来告诉我哪只动物赢得了比赛。此函数通过假设 `populate_ranks` 将按升序分配 `ranks` 字典的内容来工作，这意味着第一个键必须是获胜者：
```
def get_winner(ranks):
return next(iter(ranks))
```
在这里，我确认这些函数按设计工作并产生了我期望的结果：
[点击此处查看代码图像](#ch04_images#f0113-02)
```
ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)

>>>
{'otter': 1, 'fox': 2, 'polar bear': 3}
otter
```
现在，假设此程序的要求已更改。显示结果的 UI 元素应按字母顺序而不是排名顺序排列。为了实现这一点，我可以使用 `collections.abc` 内置模块来定义一个新的类似字典的类，该类按字母顺序迭代其内容：
[点击此处查看代码图像](#ch04_images#f0114-01)
```
from collections.abc import MutableMapping

class SortedDict(MutableMapping):
def __init__(self):
self.data = {}

def __getitem__(self, key):
return self.data[key]

def __setitem__(self, key, value):
self.data[key] = value

def __delitem__(self, key):
del self.data[key]

def __iter__(self):
keys = list(self.data.keys())
keys.sort()
for key in keys:
yield key

def __len__(self):
return len(self.data)
```
我可以将 `SortedDict` 实例替换为标准 `dict` 与之前的函数一起使用，并且不会引发错误，因为此类符合标准字典的协议。但是，结果不正确：
[点击此处查看代码图像](#ch04_images#f0114-02)
```
sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)

>>>
{'otter': 1, 'fox': 2, 'polar bear': 3}
fox
```
这里的问题是 `get_winner` 的实现假设字典的迭代顺序是插入顺序以匹配 `populate_ranks`。此代码正在使用 `SortedDict` 而不是 `dict`，因此该假设不再成立。因此，返回的获胜者是“fox”，它是字母顺序中的第一个。
有三种方法可以缓解此问题。首先，我可以重新实现 `get_winner` 函数，使其不再假定 `ranks` 字典具有特定的迭代顺序。这是最保守和最健壮的解决方案：
[点击此处查看代码图像](#ch04_images#f0115-01)
```
def get_winner(ranks):
for name, rank in ranks.items():
if rank == 1:
return name

winner = get_winner(sorted_ranks)
print(winner)

>>>
otter
```
第二种方法是在函数顶部添加一个显式检查，以确保 `ranks` 的类型与我的期望匹配，并在不匹配时引发异常。此解决方案可能比更保守的方法具有更好的运行时性能：
[点击此处查看代码图像](#ch04_images#f0115-02)
```
def get_winner(ranks):
if not isinstance(ranks, dict):
raise TypeError("must provide a dict instance")
return next(iter(ranks))

get_winner(sorted_ranks)

>>>
Traceback ...
TypeError: must provide a dict instance
```
第三种选择是使用类型注解来强制传递给 `get_winner` 的值是 `dict` 实例，而不是具有类似字典行为的 `MutableMapping`（请参阅 [Item 124](#ch14#ch14lev1sec9)：“[考虑通过 typing 进行静态分析以消除错误](#ch14#ch14lev1sec9)”）。在这里，我在类型注解版本的代码上运行 `mypy` 工具，严格模式：
[点击此处查看代码图像](#ch04_images#f0115-03)
```
from typing import Dict, MutableMapping

def populate_ranks(votes: Dict[str, int],
ranks: Dict[str, int]) -> None:
names = list(votes.keys())
names.sort(key=votes.__getitem__, reverse=True)
for i, name in enumerate(names, 1):
ranks[name] = i

def get_winner(ranks: Dict[str, int]) -> str:
return next(iter(ranks))

class SortedDict(MutableMapping[str, int]):
...

votes = {
"otter": 1281,
"polar bear": 587,
"fox": 863,
}

sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)

$ python3 -m mypy --strict example.py
.../example.py:48: error: Argument 2 to "populate_ranks" has
➥incompatible type "SortedDict"; expected "dict[str, int]"
➥[arg-type]
.../example.py:50: error: Argument 1 to "get_winner" has
➥incompatible type "SortedDict"; expected "dict[str, int]"
➥[arg-type]
Found 2 errors in 1 file (checked 1 source file)
```
这正确地检测了 `dict` 和 `SortedDict` 类型之间的不匹配，并将不正确的用法标记为错误。此解决方案提供了静态类型安全和运行时性能的最佳组合。
#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 自 Python 3.7 起，您可以依赖迭代字典实例的内容的顺序与最初添加键的顺序相同。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 可以轻松定义充当字典但不是 `dict` 实例的对象。对于这些类型，您不能假定插入顺序会得到保留。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 有三种方法可以小心处理类似字典的类：编写不依赖插入顺序的代码、在运行时显式检查 `dict` 类型，或使用类型注解和静态分析要求 `dict` 值。

### Item 26：优先使用 `get` 而不是 `in` 和 `KeyError` 来处理缺失的字典键

与字典交互的三个基本操作是访问、分配和删除键及其关联值。字典的内容是动态的，因此，当您尝试访问或删除键时，它可能根本不存在，甚至很可能不存在。
例如，假设我正在尝试确定人们最喜欢的面包类型，以便为三明治店设计菜单。在这里，我定义了一个计数器字典，其中包含当前每个面包风格的投票数：
```
counters = {
"pumpernickel": 2,
"sourdough": 1,
}
```
要增加新投票的计数器，我需要查看键是否存在，如果键丢失，则插入一个默认计数器值为零的键，然后增加计数器的值。这需要两次访问键并一次赋值。在这里，我通过使用返回 `True`（当键存在时）的 `in` 运算符的 `if` 语句来完成此任务：
[点击此处查看代码图像](#ch04_images#f0117-01)
```
key = "wheat"

if key in counters:
count = counters[key]
else:
count = 0

counters[key] = count + 1
print(counters)

>>>
{'pumpernickel': 2, 'sourdough': 1, 'wheat': 1}
```
完成相同行为的另一种方法是依赖字典在尝试获取不存在的键的值时引发 `KeyError` 异常。撇开引发和捕获异常的成本不谈（请参阅 [Item 80](#ch10#ch10lev1sec1)：“[利用 try/except/else/finally 的每个块](#ch10#ch10lev1sec1)”），这种方法理论上更有效，因为它只需要一次访问和一次赋值：
```
try:
count = counters[key]
except KeyError:
count = 0

counters[key] = count + 1
```
这种获取现有键或返回默认值的流程如此普遍，以至于 `dict` 内置类型提供了 `get` 方法来完成此任务。`get` 的第二个参数是在键（第一个参数）不存在的情况下要返回的默认值（请参阅 [Item 32](#ch05#ch05lev1sec3)：“[优先引发异常而不是返回 None](#ch05#ch05lev1sec3)” 关于这是否是一个好的接口）。此方法也只需要一次访问和一次赋值，但它比 `KeyError` 示例短得多，并且避免了异常处理开销：
```
count = counters.get(key, 0)
counters[key] = count + 1
```
可以通过各种方式缩短 `in` 运算符和 `KeyError` 方法，但所有这些替代方法都存在需要重复赋值代码的问题，这使得它们可读性较差且应避免：
```
if key not in counters:
counters[key] = 0
counters[key] += 1

if key in counters:
counters[key] += 1
else:
counters[key] = 1

try:
counters[key] += 1
except KeyError:
counters[key] = 1
```
因此，对于具有简单类型的字典，使用 `get` 方法是最短、最清晰的选择。
注意
如果您维护像这样的计数器字典，则值得考虑 `collections` 内置模块中的 `Counter` 类，该类提供了您可能需要的大部分功能。
如果字典中的值是更复杂类型，例如列表怎么办？例如，假设我不仅要计算投票数，还想知道谁投票给了每种面包。在这里，我通过将名称列表与每个键关联来实现这一点：
[点击此处查看代码图像](#ch04_images#f0119-01)
```
votes = {
"baguette": ["Bob", "Alice"],
"ciabatta": ["Coco", "Deb"],
}

key = "brioche"
who = "Elmer"

if key in votes:
names = votes[key]
else:
votes[key] = names = []

names.append(who)
print(votes)

>>>
{'baguette': ['Bob', 'Alice'],
'ciabatta': ['Coco', 'Deb'],
'brioche': ['Elmer']}
```
依赖 `in` 运算符会在键存在时需要两次访问，或者在键丢失时需要一次访问和一次赋值。此示例与计数器示例不同，因为每个键的值都可以盲目地分配给空列表的默认值（如果键尚不存在）。三元赋值语句（`votes[key] = names = []`）在一行而不是两行中填充了键。一旦将默认值插入字典，就不需要再次赋值，因为列表是通过引用在后续的 `append` 调用中修改的（请参阅 [Item 30](#ch05#ch05lev1sec1)：“[知道函数参数可以被修改](#ch05#ch05lev1sec1)” 获取背景信息）。
还可以依赖在字典值为列表时引发的 `KeyError` 异常。此方法在键存在时需要一次键访问，或者在键丢失时需要一次键访问和一次赋值，这使其比 `in` 运算符更有效（忽略异常处理机制的成本）：
```
try:
names = votes[key]
except KeyError:
votes[key] = names = []

names.append(who)
```
同样，我可以使用 `get` 方法在键存在时获取列表值，或者在键不存在时进行一次获取和一次赋值：
```
names = votes.get(key)
if names is None:
votes[key] = names = []

names.append(who)
```
使用 `get` 获取列表值的这种方法可以通过一行代码进一步缩短，如果您在 `if` 语句中使用赋值表达式（Python 3.8 中引入；请参阅 [Item 8](#ch01#ch01lev1sec8)：“[使用赋值表达式避免重复](#ch01#ch01lev1sec8)”），这可以提高可读性：
[点击此处查看代码图像](#ch04_images#f0120-01)
```
if (names := votes.get(key)) is None:
votes[key] = names = []

names.append(who)
```
值得注意的是，`dict` 类型还提供了 `setdefault` 方法来帮助进一步缩短此模式。`setdefault` 尝试获取字典中键的值。如果键不存在，则该方法将该键分配给提供的默认值。然后该方法返回该键的值：无论是最初存在的值还是新插入的默认值。在这里，我使用 `setdefault` 来实现与上面 `get` 示例相同的逻辑：
[点击此处查看代码图像](#ch04_images#f0120-02)
```
names = votes.setdefault(key, [])
names.append(who)
```
这按预期工作，并且比使用带有赋值表达式的 `get` 更短。但是，此方法的易读性并不理想。方法名 `setdefault` 并不能立即使其目的显而易见。为什么是 `set` 而它正在做的是获取值？为什么不称之为 `get_or_set`？我在这里争论的是自行车棚的颜色，但重点是，如果您是代码的新读者，并且不完全熟悉 Python，您可能会难以理解此代码试图完成什么，因为 `setdefault` 不是不言自明的。
还有一个重要的陷阱：传递给 `setdefault` 的默认值在键丢失时会直接分配到字典中，而不是被复制。在这里，我演示了当值为列表时此效果：
```
data = {}
key = "foo"
value = []
data.setdefault(key, value)
print("Before:", data)
value.append("hello")
print("After: ", data)

>>>
Before: {'foo': []}
After:  {'foo': ['hello']}
```
因此，我需要确保我始终为使用 `setdefault` 访问的每个键构造一个新的默认值。这在此示例中导致了显着的性能开销，因为我必须为每次调用分配一个 `list` 实例。如果我为默认值重用一个对象（我可能会尝试这样做以提高效率或可读性），我可能会引入奇怪的行为和错误（请参阅 [Item 36](#ch05#ch05lev1sec7)：“[使用 None 和文档字符串指定动态默认参数](#ch05#ch05lev1sec7)” 获取此问题的另一个示例）。
回到前面使用计数器作为字典值而不是投票者列表的示例：为什么不在该情况下也使用 `setdefault` 方法？在这里，我使用此方法重新实现了相同的示例：
[点击此处查看代码图像](#ch04_images#f0121-01)
```
count = counters.setdefault(key, 0)
counters[key] = count + 1
```
这里的问题是 `setdefault` 调用是多余的。您总是在递增计数器后需要将键赋值为新值，因此 `setdefault` 的额外赋值是不必要的。使用 `get` 进行计数器更新的先前方法只需要一次访问和一次赋值，而使用 `setdefault` 需要一次访问和两次赋值。
只有在少数情况下，使用 `setdefault` 是处理缺失字典键的最短方法（例如，对于易于构造且不会引发异常的 `list` 实例默认值）。在这些非常特定的情况下，接受令人困惑的 `setdefault` 方法名而不是编写更多字符和行来使用 `get` 似乎是值得的。然而，通常您真正应该做的是使用 `defaultdict`（请参阅 [Item 27](#ch04#ch04lev1sec3)：“[优先使用 defaultdict 而不是 setdefault 来处理内部状态中的缺失项](#ch04#ch04lev1sec3)”）。
#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 有四种常见的方法可以检测和处理字典中的缺失键：使用 `in` 运算符、`KeyError` 异常、`get` 方法和 `setdefault` 方法。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `get` 方法最适合包含计数器等基本类型的字典，并且在创建字典默认值成本高或可能引发异常时，它与赋值表达式一起是首选。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 当 `dict` 的 `setdefault` 方法似乎最适合您的问题时，您应该考虑改用 `defaultdict`。

### Item 27：优先使用 `defaultdict` 而不是 `setdefault` 来处理内部状态中的缺失项

在处理您未创建的字典时，有多种方法可以处理缺失的键（请参阅 [Item 26](#ch04#ch04lev1sec2)：“[优先使用 get 而不是 in 和 KeyError 来处理缺失的字典键](#ch04#ch04lev1sec2)”）。虽然使用 `get` 方法比使用 `in` 运算符和 `KeyError` 异常更好，但对于某些用例，`setdefault` 似乎是最短的选项。
例如，假设我想跟踪我在世界各国访问过的城市。在这里，我通过使用一个将国家名称映射到包含相应城市名称的 `set` 实例的字典来实现：
[点击此处查看代码图像](#ch04_images#f0122-01)
```
visits = {
"Mexico": {"Tulum", "Puerto Vallarta"},
"Japan": {"Hakone"},
}
```
我可以使用 `setdefault` 方法将新城市添加到集合中，无论国家名称是否已存在于字典中。与使用 `get` 方法和赋值表达式实现相同行为相比，此代码要短得多：
[点击此处查看代码图像](#ch04_images#f0122-02)
```
# Short
visits.setdefault("France", set()).add("Arles")

# Long
if (japan := visits.get("Japan")) is None:
visits["Japan"] = japan = set()

japan.add("Kyoto")
print(visits)

>>>
{'Mexico': {'Puerto Vallarta', 'Tulum'},
'Japan': {'Kyoto', 'Hakone'},
'France': {'Arles'}}
```
当您 _确实_ 控制字典的创建时，情况如何？当您使用字典实例来跟踪对象的内部状态时，通常就是这种情况。例如。在这里，我将上面的示例包装在一个类中，并带有帮助方法来访问存储在字典中的动态内部状态：
[点击此处查看代码图像](#ch04_images#f0123-01)
```
class Visits:
def __init__(self):
self.data = {}

def add(self, country, city):
city_set = self.data.setdefault(country, set())
city_set.add(city)
```
这个新类隐藏了调用 `setdefault` 并提供正确参数的复杂性，并为程序员提供了更好的接口：
[点击此处查看代码图像](#ch04_images#f0123-02)
```
visits = Visits()
visits.add("Russia", "Yekaterinburg")
visits.add("Tanzania", "Zanzibar")
print(visits.data)

>>>
{'Russia': {'Yekaterinburg'}, 'Tanzania': {'Zanzibar'}}
```
但是，`Visits.add` 方法的实现并不理想。`setdefault` 方法的命名仍然令人困惑，这使得新代码阅读者更难立即理解正在发生的事情。而且实现效率不高，因为它在每次调用时都会构造一个新的 `set` 实例，而不管给定的国家是否已存在于 `data` 字典中。
幸运的是，`collections` 内置模块中的 `defaultdict` 类通过在键不存在时自动存储默认值来简化了这种常见用例。您所要做的就是提供一个函数，该函数将在每次缺少键时返回要使用的默认值（[Item 48](#ch07#ch07lev1sec1) 的示例：“[接受函数而不是类来实现简单接口](#ch07#ch07lev1sec1)”）。在这里，我重写了 `Visits` 类以使用 `defaultdict`：
[点击此处查看代码图像](#ch04_images#f0123-03)
```
from collections import defaultdict

class Visits:
def __init__(self):
self.data = defaultdict(set)

def add(self, country, city):
self.data[country].add(city)

visits = Visits()
visits.add("England", "Bath")
visits.add("England", "London")
print(visits.data)

>>>
defaultdict(<class 'set'>, {'England': {'Bath', 'London'}})
```
现在，`add` 的实现简短而简单。代码可以假定访问 `data` 字典中的任何键始终会产生一个现有的 `set` 实例。不会分配多余的 `set` 实例，如果 `add` 方法被调用很多次，这可能会很昂贵。
在这种情况下，使用 `defaultdict` 比使用 `setdefault` 要好得多（请参阅 [Item 29](#ch04#ch04lev1sec5)：“[组合类而不是深度嵌套字典、列表和元组](#ch04#ch04lev1sec5)” 获取另一个示例）。仍然存在 `defaultdict` 无法解决您的问题的情况，但 Python 中还有更多工具可以解决这些限制（请参阅 [Item 28](#ch04#ch04lev1sec4)：“[了解如何使用 \_\_missing\_\_ 构建依赖于键的默认值](#ch04#ch04lev1sec4)”、“[Item 57](#ch07#ch07lev1sec10)：“[为自定义容器类型继承 collections.abc 类](#ch07#ch07lev1sec10)” 和 `collections.Counter` 内置类）。
#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果您正在创建一个字典来管理任意一组潜在的键，那么如果适合您的问题，您应该优先使用 `collections` 内置模块中的 `defaultdict` 实例。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果将任意键的字典传递给您，并且您不控制其创建，那么您应该优先使用 `get` 方法来访问其项。但是，值得考虑在少数情况下使用 `setdefault` 方法，这些情况可以缩短代码并且默认对象分配成本很低。

### Item 28：了解如何使用 `__missing__` 构建依赖于键的默认值

内置 `dict` 类型的 `setdefault` 方法在处理某些特定情况下的缺失键时会产生更短的代码（请参阅 [Item 26](#ch04#ch04lev1sec2)：“[优先使用 get 而不是 in 和 KeyError 来处理缺失的字典键](#ch04#ch04lev1sec2)”）。对于其中许多情况，更好的工具是 `collections` 内置模块中的 `defaultdict` 类型（请参阅 [Item 27](#ch04#ch04lev1sec3)：“[优先使用 defaultdict 而不是 setdefault 来处理内部状态中的缺失项](#ch04#ch04lev1sec3)” 以了解原因）。但是，有时 `setdefault` 和 `defaultdict` 都不适合。
例如，假设我正在编写一个程序来管理文件系统上的社交网络个人资料图片。我需要一个字典来将个人资料图片路径名映射到打开的文件句柄，以便我可以按需读取和写入这些图片。在这里，我通过使用普通的 `dict` 实例并使用 `get` 方法和赋值表达式检查键是否存在来实现这一点（请参阅 [Item 8](#ch01#ch01lev1sec8)：“[使用赋值表达式避免重复](#ch01#ch01lev1sec8)”）：
[点击此处查看代码图像](#ch04_images#f0125-01)
```
pictures = {}
path = "profile_1234.png"

if (handle := pictures.get(path)) is None:
try:
handle = open(path, "a+b")
except OSError:
print(f"Failed to open path {path}")
raise
else:
pictures[path] = handle

handle.seek(0)
image_data = handle.read()
```
当文件句柄已存在于字典中时，此代码仅进行一次字典访问。如果文件句柄不存在，则字典被 `get` 访问一次，然后在 `try`/`except` 语句的 `else` 子句中进行赋值（请参阅 [Item 80](#ch10#ch10lev1sec1)：“[利用 try/except/else/finally 的每个块](#ch10#ch10lev1sec1)”）。`read` 方法的调用与调用 `open` 和处理异常的代码明显分开。
虽然可以使用 `in` 运算符或 `KeyError` 方法来实现相同的逻辑，但这些选项需要更多的字典访问和嵌套级别。鉴于这些其他选项有效，您可能还会假设 `setdefault` 方法也有效：
[点击此处查看代码图像](#ch04_images#f0125-02)
```
try:
handle = pictures.setdefault(path, open(path, "a+b"))
except OSError:
print(f"Failed to open path {path}")
raise
else:
handle.seek(0)
image_data = handle.read()
```
此代码存在许多问题。即使路径已存在于字典中，`open` 内置函数也始终被调用以创建文件句柄。这会导致一个额外的文件句柄，该句柄可能与同一程序中的现有打开句柄冲突。`open` 调用可能会引发异常，需要进行处理，但可能无法将其与同一行上的 `setdefault` 调用可能引发的异常区分开（对于其他类似字典的实现是可能的；请参阅 [Item 57](#ch07#ch07lev1sec10)：“[为自定义容器类型继承 collections.abc 类](#ch07#ch07lev1sec10)”）。
如果您试图管理内部状态，您可能还会做出一个假设，即可以使用 `defaultdict` 来跟踪这些个人资料图片。在这里，我尝试实现与以前相同的逻辑，但现在使用一个辅助函数和 `defaultdict` 类：
[点击此处查看代码图像](#ch04_images#f0126-01)
```
from collections import defaultdict

def open_picture(profile_path):
try:
return open(profile_path, "a+b")
except OSError:
print(f"Failed to open path {profile_path}")
raise

pictures = defaultdict(open_picture)
handle = pictures[path]
handle.seek(0)
image_data = handle.read()

>>>
Traceback ...
TypeError: open_picture() missing 1 required positional
➥argument: 'profile_path'
```
问题在于 `defaultdict` 期望传递给其构造函数的函数不要求任何参数。这意味着 `defaultdict` 调用辅助函数不知道正在访问的特定 `key`，这阻碍了我调用 `open` 的能力。在这种情况下，`setdefault` 和 `defaultdict` 都未能满足我的需求。
幸运的是，这种情况足够常见，以至于 Python 有另一种内置解决方案。您可以子类化 `dict` 类型并实现 `__missing__` 特殊方法，以添加处理缺失键的自定义逻辑。在这里，我通过定义一个利用上面定义的相同 `open_picture` 辅助方法的新类来实现这一点：
[点击此处查看代码图像](#ch04_images#f0126-02)
```
class Pictures(dict):
def __missing__(self, key):
value = open_picture(key)
self[key] = value
return value

pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
```
当 `pictures[path]` 字典访问发现 `path` 键不存在于字典中时，将调用 `__missing__` 方法。此方法必须为键创建新的默认值，将其插入字典，并将其返回给调用者。后续访问相同的 `path` 不会调用 `__missing__`，因为相应的项已存在（类似于 `__getattr__` 的行为；请参阅 [Item 61](#ch08#ch08lev1sec4)：“[使用 \_\_getattr\_\_, \_\_getattribute\_\_, 和 \_\_setattr\_\_ 来实现惰性属性](#ch08#ch08lev1sec4)”）。
#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `dict` 的 `setdefault` 方法不适合创建默认值成本高或可能引发异常的情况。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 传递给 `defaultdict` 的函数不得要求任何参数，这使得默认值无法依赖于正在访问的键。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 您可以定义自己的 `dict` 子类，其中包含 `__missing__` 方法，以便构建必须知道正在访问哪个键的默认值。

### Item 29：组合类而不是深度嵌套字典、列表和元组

Python 的内置字典类型非常适合在对象的生命周期内维护动态内部状态。通过 _动态_，我指的是您需要为意外标识符集进行簿记的情况。例如，假设我想记录一组学生的分数，而这些学生的名字是无法提前知道的。我可以定义一个类来存储名字，而不是为每个学生使用预定义的属性：
[点击此处查看代码图像](#ch04_images#f0127-02)
```
class SimpleGradebook:
def __init__(self):
self._grades = {}

def add_student(self, name):
self._grades[name] = []

def report_grade(self, name, score):
self._grades[name].append(score)

def average_grade(self, name):
grades = self._grades[name]
return sum(grades) / len(grades)
```
使用此类很简单：
[点击此处查看代码图像](#ch04_images#f0128-02)
```
book = SimpleGradebook()
book.add_student("Isaac Newton")
book.report_grade("Isaac Newton", 90)
book.report_grade("Isaac Newton", 95)
book.report_grade("Isaac Newton", 85)

print(book.average_grade("Isaac Newton"))

>>>
90.0
```
字典、列表、元组和集合非常易于使用，以至于它们有导致您编写脆弱代码的风险。例如，假设我想扩展 `SimpleGradebook` 类以按科目存储成绩列表，而不仅仅是总体成绩。我可以通过更改 `_grades` 字典来将学生姓名（其键）映射到另一个字典（其值）来实现。最里面的字典将映射科目（其键）到成绩列表（其值）。在这里，我通过使用 `defaultdict` 实例作为内部字典来处理缺失的科目来实现这一点（请参阅 [Item 27](#ch04#ch04lev1sec3)：“[优先使用 defaultdict 而不是 setdefault 来处理内部状态中的缺失项](#ch04#ch04lev1sec3)” 获取背景信息）：
[点击此处查看代码图像](#ch04_images#f0128-03)
```
from collections import defaultdict

class BySubjectGradebook:
def __init__(self):
self._grades = {}                       # Outer dict

def add_student(self, name):
self._grades[name] = defaultdict(list)  # Inner dict

def report_grade(self, name, subject, grade):
by_subject = self._grades[name]
grade_list = by_subject[subject]
grade_list.append(grade)

def average_grade(self, name):
by_subject = self._grades[name]
total, count = 0, 0
for grades in by_subject.values():
total += sum(grades)
count += len(grades)
return total / count
```
这足够直接。`report_grade` 和 `average_grade` 方法增加了相当多的复杂性来处理多级字典，但这似乎是可管理的。使用此类仍然很简单：
[点击此处查看代码图像](#ch04_images#f0129-02)
```
book = BySubjectGradebook()
book.add_student("Albert Einstein")
book.report_grade("Albert Einstein", "Math", 75)
book.report_grade("Albert Einstein", "Math", 65)
book.report_grade("Albert Einstein", "Gym", 90)
book.report_grade("Albert Einstein", "Gym", 95)
print(book.average_grade("Albert Einstein"))

>>>
81.25
```
现在，假设要求再次更改。我还想跟踪每个分数在班级总成绩中的权重，以便期中和期末考试比随堂测验更重要。实现此功能的一种方法是更改最里面的字典；而不是将科目（其键）映射到成绩列表（其值），我可以在每个键的相应值列表中使用 `(score, weight)` 的元组。尽管对 `report_grade` 的更改看起来很简单——只需让 `grade_list` 存储元组实例——但 `average_grade` 方法现在有一个循环内的循环，并且难以阅读：
[点击此处查看代码图像](#ch04_images#f0129-03)
```
class WeightedGradebook:
def __init__(self):
self._grades = {}

def add_student(self, name):
self._grades[name] = defaultdict(list)

def report_grade(self, name, subject, score, weight):
by_subject = self._grades[name]
grade_list = by_subject[subject]
grade_list.append((score, weight))    # Changed

def average_grade(self, name):
by_subject = self._grades[name]

score_sum, score_count = 0, 0
for grades in by_subject.values():
subject_avg, total_weight = 0, 0
for score, weight in scores:      # Added inner loop
subject_avg += score * weight
total_weight += weight

score_sum += subject_avg / total_weight
score_count += 1

return score_sum / score_count
```
使用此类也变得更加困难。不清楚位置参数中的所有数字是什么意思：
[点击此处查看代码图像](#ch04_images#f0130-02)
```
book = WeightedGradebook()
book.add_student("Albert Einstein")
book.report_grade("Albert Einstein", "Math", 75, 0.05)
book.report_grade("Albert Einstein", "Math", 65, 0.15)
book.report_grade("Albert Einstein", "Math", 70, 0.80)
book.report_grade("Albert Einstein", "Gym", 100, 0.40)
book.report_grade("Albert Einstein", "Gym", 85, 0.60)
print(book.average_grade("Albert Einstein"))

>>>
80.25
```
当您遇到这种复杂性时，是时候从内置类型（如字典、列表、元组和集合）过渡到类层次结构了。
在成绩示例中，起初我不知道我需要支持加权成绩，因此创建其他类的复杂性似乎不合理。Python 的内置字典和元组类型使继续进行变得容易，将一层又一层的内部簿记添加进去。但是，您应该避免这样做超过一个嵌套级别；使用包含字典的字典会使您的代码难以被其他程序员阅读，并使您陷入维护噩梦（请参阅 [Item 9](#ch01#ch01lev1sec9)：“[考虑使用 match 进行流程控制中的解构，当 if 语句足够时避免](#ch01#ch01lev1sec9)” 获取处理此问题的另一种方法）。
一旦您发现您的簿记变得复杂，就应该将其全部分解到类中。然后，您可以提供定义良好的接口来更好地封装您的数据。这种方法还使您能够在接口和具体实现之间创建抽象层。
#### 重构为类
有许多重构方法（请参阅 [Item 123](#ch14#ch14lev1sec8)：“[考虑使用警告进行重构和迁移使用](#ch14#ch14lev1sec8)” 获取示例）。在这种情况下，我可以从依赖树的底部开始类化：单个成绩。对于如此简单的信息，一个类似乎过于沉重。然而，元组似乎是合适的，因为成绩是不可变的。在这里，我使用 `(score, weight)` 的元组来跟踪列表中的成绩：
[点击此处查看代码图像](#ch04_images#f0131-01)
```
grades = []
grades.append((95, 0.45))
grades.append((85, 0.55))
total = sum(score * weight for score, weight in grades)
total_weight = sum(weight for _, weight in grades)
average_grade = total / total_weight
```
我使用了 `_`（下划线变量名，Python 中用于未使用变量的约定）来捕获每个成绩元组的第一个条目，并在计算 `total_weight` 时忽略它。
此代码的问题在于元组实例是位置性的。例如，如果我想将更多信息与成绩关联，例如教师的笔记集，我需要重写所有使用双元组的地方，使其意识到存在三个项而不是两个，这意味着我需要进一步使用 `_` 来忽略某些索引：
[点击此处查看代码图像](#ch04_images#f0131-02)
```
grades = []
grades.append((95, 0.45, "Great job"))
grades.append((85, 0.55, "Better next time"))
total = sum(score * weight for score, weight, _ in grades)
total_weight = sum(weight for _, weight, _ in grades)
average_grade = total / total_weight
```
这种扩展元组越来越长的模式类似于加深字典层。一旦您发现自己使用的元组长度超过了两个，就该考虑另一种方法了。`dataclasses` 内置模块正好满足我在此案例中的需求：它允许我轻松定义一个用于在属性中存储值的轻量级不可变类（请参阅 [Item 56](#ch07#ch07lev1sec9)：“[优先使用 dataclasses 创建不可变对象](#ch07#ch07lev1sec9)”）：
[点击此处查看代码图像](#ch04_images#f0131-03)
```
from dataclasses import dataclass

@dataclass(frozen=True)
class Grade:
score: int
weight: float
```
接下来，我可以编写一个类来表示一个科目，该科目包含一组 `Grade` 实例：
[点击此处查看代码图像](#ch04_images#f0132-01)
```
class Subject:
def __init__(self):
self._grades = []

def report_grade(self, score, weight):
self._grades.append(Grade(score, weight))

def average_grade(self):
total, total_weight = 0, 0
for grade in self._grades:
total += grade.score * grade.weight
total_weight += grade.weight
return total / total_weight
```
然后，我编写一个类来保存一个学生正在学习的所有科目的集合：
[点击此处查看代码图像](#ch04_images#f0132-02)
```
class Student:
def __init__(self):
self._subjects = defaultdict(Subject)

def get_subject(self, name):
return self._subjects[name]

def average_grade(self):
total, count = 0, 0
for subject in self._subjects.values():
total += subject.average_grade()
count += 1
return total / count
```
最后，我编写一个容器来保存所有学生，并按姓名动态键入：
[点击此处查看代码图像](#ch04_images#f0132-03)
```
class Gradebook:
def __init__(self):
self._students = defaultdict(Student)

def get_student(self, name):
return self._students[name]
```
这些类的行数几乎是先前实现大小的两倍。但这段代码更容易阅读。驱动类的示例也更清晰、更具可扩展性：
[点击此处查看代码图像](#ch04_images#f0133-01)
```
book = Gradebook()
albert = book.get_student("Albert Einstein")
math = albert.get_subject("Math")
math.report_grade(75, 0.05)
math.report_grade(65, 0.15)
math.report_grade(70, 0.80)
gym = albert.get_subject("Gym")
gym.report_grade(100, 0.40)
gym.report_grade(85, 0.60)
print(albert.average_grade())

>>>
80.25
```
还可以编写向后兼容的方法来帮助将旧 API 样式的使用迁移到新的对象层次结构。
#### 记住要点
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 避免创建值为字典、长元组或复杂嵌套其他内置类型的字典。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在需要完整类的灵活性之前，请使用 `dataclasses` 内置模块来创建轻量级、不可变的数据容器。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 当您的内部状态字典变得复杂时，将您的簿记代码移至使用多个类。
---
<a role="toc_link" id="ch05"></a>

## Effective Python - 5

## 5

本章深入探讨了 **Effective Python** 的第五个核心主题，重点关注如何利用 Python 语言的特性和最佳实践来编写高效、可维护且易于理解的代码。本章的核心贡献在于提供了一系列实用的技巧和模式，旨在帮助开发者提升 Python 编程的效率和代码质量。

本章的主要观点围绕以下几个方面展开：

*   **高效的迭代与数据处理**: 详细介绍了 Python 中各种迭代器（如 `iter()`, `next()`, `yield`）的使用，以及列表推导式、生成器表达式等高级特性，如何有效地处理大型数据集和优化内存使用。
*   **函数式编程范式**: 探讨了 Python 对函数式编程的支持，包括高阶函数（如 `map`, `filter`, `reduce`）、lambda 表达式以及 `functools` 模块的应用，展示了如何通过函数式方法简化代码逻辑并提高可读性。
*   **上下文管理器与资源管理**: 深入讲解了 `with` 语句和上下文管理器协议 (`__enter__`, `__exit__`) 的重要性，如何安全可靠地管理文件、网络连接、锁等资源，避免资源泄露。
*   **装饰器与元编程**: 阐述了装饰器的概念及其在代码复用、日志记录、权限控制等方面的应用。同时，触及了元编程的思想，展示了如何通过修改类和函数来动态地改变程序的行为。
*   **并发与并行编程**: 介绍了 Python 在并发（如 `threading`, `asyncio`）和并行（如 `multiprocessing`）方面的工具和策略，帮助开发者构建响应迅速且能充分利用多核处理器的应用程序。

本章通过一系列精心设计的代码示例，清晰地展示了这些概念的实际应用。例如，在迭代部分，通过对比传统的 `for` 循环和生成器表达式在处理大量数据时的内存效率差异，突显了 Python 语言的灵活性。在资源管理方面，展示了如何使用上下文管理器优雅地处理文件读写，确保文件在任何情况下都能被正确关闭。

总而言之，本章为读者提供了一套全面的 Python 编程实践指南，强调了通过理解和运用 Python 的高级特性，可以显著提升代码的效率、可读性和健壮性。这些技巧对于任何希望在 Python 开发中追求卓越的开发者都至关重要。

## Effective Python - Functions

## Python 高效编程 - 函数

本章深入探讨了 Python 函数的高级特性和最佳实践，旨在帮助开发者编写更清晰、更健壮、更易于维护的代码。本章涵盖了函数参数的变异、返回值设计、异常处理、闭包、可变参数、关键字参数以及装饰器等关键概念。

### Item 30: 了解函数参数可能被修改

Python 函数的参数传递方式是“按引用传递”，这意味着当可变对象（如列表、字典或用户自定义类的实例）作为参数传递给函数时，函数内部对该对象的修改会影响到函数外部的原始对象。尽管 Python 没有 C 语言中的指针类型，但这种“按引用传递”的行为与指针操作有相似之处。

*   **可变对象的影响**: 当列表或字典等可变对象被传递给函数时，函数内部可以通过调用其方法或直接修改其元素来改变对象的状态。例如，一个函数可以向列表中添加元素，或者修改字典中的值。
*   **别名与修改**: 变量赋值在 Python 中创建的是引用（别名）。如果将一个变量赋给另一个变量，它们会指向同一个底层数据结构。因此，将其中一个变量传递给函数，函数对该变量引用的对象的修改会影响到所有指向该对象的变量。
*   **规避修改**: 为了防止函数意外修改传入的可变参数，可以传递参数的副本。对于列表，可以使用切片操作 `[:]` 创建副本；对于字典，可以使用 `copy()` 方法。用户自定义类也可以实现复制机制。
*   **实现者的责任**: 函数实现者在修改传入的可变参数时应格外谨慎，除非函数的名称、参数名或文档明确说明了这种行为。为了安全起见，可以创建参数的防御性副本，以避免迭代时的陷阱。
*   **调用者的注意**: 调用函数时，应注意传递可变参数，因为它们可能被修改，从而导致难以发现的 bug。

**要点回顾**:
*   Python 参数按引用传递，接收函数可以修改其属性。
*   函数应通过命名和文档明确其是否会修改输入参数，否则应避免修改。
*   创建传入参数的副本是确保函数不意外修改数据的可靠方法。

### Item 31: 返回专用的结果对象，而不是要求函数调用者解包三个以上的变量

Python 函数可以通过返回一个包含多个值的元组来模拟返回多个值。调用者可以使用解包语法将元组中的值赋给多个变量。虽然这种方式在返回少量值时很方便，但当需要返回的值超过三个时，会带来可读性和可维护性问题。

*   **多返回值与元组**: 函数通过返回一个元组来传递多个值，调用者通过解包元组来接收这些值。
*   **解包的局限**: 当函数返回的值过多时（例如，超过三个），解包语句会变得冗长且容易出错。例如，如果返回值的顺序被意外调换，可能会导致难以追踪的 bug。
*   **推荐方案**: 当函数需要返回四个或更多值时，应考虑创建一个轻量级的类（如使用 `dataclasses`）来封装这些结果。函数返回该类的实例，调用者可以直接访问对象的属性，从而提高代码的清晰度和健壮性。
*   **提高可读性和可维护性**: 使用专用的结果对象可以使代码更清晰，减少出错的可能性，并便于未来的重构。

**要点回顾**:
*   函数可以通过返回元组并利用 Python 的解包语法来返回多个值。
*   函数的多返回值也可以通过带星号的表达式进行解包。
*   解包到四个或更多变量是容易出错的，应避免；取而代之的是返回一个轻量级类的实例。

### Item 32: 优先抛出异常而不是返回 `None`

在 Python 中，函数返回 `None` 来表示特殊情况（如错误或未找到值）是一种常见的做法，但这种做法容易导致错误。这是因为 `None` 在布尔上下文中会被评估为 `False`，与其他表示错误的“假值”（如 `0`、空字符串、空列表等）难以区分。

*   **`None` 的歧义**: 当函数返回 `None` 时，调用者可能错误地将 `None` 与其他表示错误的“假值”混淆，导致逻辑错误。例如，一个返回 `0` 的有效计算结果，在错误的条件判断中可能被误认为是一个错误信号。
*   **替代方案 1：返回元组**: 可以将返回值设计成一个元组，其中第一个元素表示操作的成功或失败状态，第二个元素是实际结果。但这仍然需要调用者显式检查状态，且容易忽略状态部分。
*   **替代方案 2：抛出异常**: 更推荐的做法是，当遇到特殊情况时，直接抛出异常。这使得函数调用者必须显式地处理这些异常情况，从而强制他们考虑错误处理逻辑。
*   **异常的清晰性**: 抛出异常可以清晰地表达函数执行过程中遇到的问题，例如 `ValueError` 可以用来表示输入值无效。调用者可以通过 `try...except` 块来捕获和处理这些异常。
*   **类型注解的配合**: 使用类型注解可以明确函数返回值的类型，例如指定返回 `float`，从而表明函数不会返回 `None`。

**要点回顾**:
*   函数返回 `None` 来表示特殊含义是容易出错的，因为 `None` 和许多其他值（如零和空字符串）在布尔表达式中都评估为 `False`。
*   应抛出异常来指示特殊情况，而不是返回 `None`。期望调用代码在文档说明的情况下妥善处理异常。
*   类型注解可用于明确函数即使在特殊情况下也不会返回 `None` 的事实。

### Item 33: 了解闭包如何与变量作用域和 `nonlocal` 交互

Python 支持闭包，即函数可以引用其定义所在作用域中的变量。这使得函数能够“记住”其创建时的环境。然而，当闭包尝试修改其外部作用域中的变量时，会遇到作用域问题。

*   **闭包的引用能力**: 闭包可以访问其外部作用域中的变量，即使外部函数已经执行完毕。
*   **赋值行为的差异**: 在 Python 中，读取变量会按顺序查找当前作用域、外部作用域、全局作用域和内置作用域。但赋值行为不同：如果在闭包内部对一个变量进行赋值，Python 会默认在该闭包内部创建一个新的局部变量，而不是修改外部作用域中的同名变量。
*   **`nonlocal` 关键字**: 为了解决闭包修改外部作用域变量的问题，可以使用 `nonlocal` 关键字。`nonlocal` 声明指示解释器在赋值时，应在外部（非全局）作用域中查找并修改该变量。
*   **`global` 关键字**: `global` 关键字用于指示变量的赋值应直接作用于模块级（全局）作用域。
*   **替代方案：类**: 当对 `nonlocal` 的使用变得复杂时，可以考虑将状态封装在一个类中。类的实例属性可以在其 `__call__` 方法中被修改，从而实现类似 `nonlocal` 的效果，并且代码更易于理解和维护。
*   **谨慎使用 `nonlocal`**: 尽管 `nonlocal` 很有用，但应避免过度使用，尤其是在复杂的函数中，因为它可能导致代码难以追踪。

**要点回顾**:
*   闭包函数可以引用其定义所在的所有外部作用域中的变量。
*   默认情况下，闭包不能通过赋值来影响外部作用域。
*   使用 `nonlocal` 语句指示闭包可以修改其外部作用域中的变量。使用 `global` 语句对模块级名称执行相同的操作。
*   避免对除简单函数之外的任何内容使用 `nonlocal` 语句。

### Item 34: 使用可变位置参数减少视觉噪音

可变位置参数（`*args`）允许函数接受任意数量的位置参数，这可以使函数调用更简洁，减少不必要的代码噪音。

*   **`*args` 的作用**: 在函数定义中使用 `*args`，可以将所有传递给函数的位置参数收集到一个元组中。
*   **简化调用**: 允许函数接受可变数量的参数，可以避免在没有参数时传递空列表或空元组，使函数调用更自然。
*   **解包序列**: 使用 `*` 操作符可以将序列（如列表或元组）的元素作为独立的位置参数传递给函数。
*   **潜在问题**:
*   **内存消耗**: 如果将生成器与 `*args` 一起使用，生成器中的所有元素都会被迭代并收集到一个元组中，这可能导致内存不足甚至程序崩溃。
*   **向后兼容性**: 在接受 `*args` 的函数中添加新的位置参数可能会破坏现有调用者的代码，除非使用关键字参数来区分。
*   **最佳实践**: `*args` 最适合于参数数量可变且数量不大的情况，主要用于提高函数调用者的便利性和代码的可读性。在扩展此类函数时，应考虑使用关键字参数来保持向后兼容性。

**要点回顾**:
*   通过在 `def` 语句中使用 `*args`，函数可以接受可变数量的位置参数。
*   使用 `*` 操作符可以将序列中的项作为函数的参数传递。
*   将 `*` 操作符与生成器一起使用可能会导致程序内存不足并崩溃。
*   向接受 `*args` 的函数添加新的位置参数可能会引入难以检测的 bug。

### Item 35: 通过关键字参数提供可选行为

Python 函数的参数不仅可以通过位置传递，还可以通过关键字传递。关键字参数的使用可以提高代码的可读性，并允许为参数设置默认值，从而实现可选行为。

*   **关键字参数的优势**:
*   **清晰性**: 使用关键字参数（如 `func(name='Alice', age=30)`）可以明确每个参数的含义，即使参数顺序被打乱，代码也易于理解。
*   **默认值**: 函数定义中可以为关键字参数设置默认值。调用者可以省略这些参数，从而使用默认行为，减少了冗余代码。
*   **向后兼容性**: 在不破坏现有代码的情况下，可以向函数添加新的可选关键字参数，从而扩展函数的功能。
*   **`**kwargs`**: 使用 `**kwargs` 可以捕获所有未显式定义的关键字参数，并将它们收集到一个字典中，这对于编写通用的函数或装饰器非常有用。
*   **混合使用**: 可以混合使用位置参数和关键字参数，但位置参数必须在关键字参数之前。
*   **最佳实践**: 始终使用关键字参数来传递可选参数，以提高代码的可读性和明确性。

**要点回顾**:
*   函数参数可以通过位置或关键字指定。
*   关键字参数使得参数的用途在仅使用位置参数时会令人困惑的情况下更加清晰。
*   带有默认值的关键字参数使得在不迁移所有现有调用者的情况下为函数添加新行为变得容易。
*   可选关键字参数应始终通过关键字传递，而不是通过位置传递。

### Item 36: 使用 `None` 和文档字符串指定动态默认参数

在 Python 中，函数默认参数的值在函数定义时只会被评估一次。这意味着如果默认参数是一个可变对象（如列表或字典）或一个会随时间变化的函数调用（如 `datetime.now()`），那么所有使用默认值的调用都会共享同一个对象或同一个调用结果，这可能导致意外的行为。

*   **默认参数的评估时机**: 默认参数的值在函数定义时（通常是模块加载时）被评估一次，而不是在每次函数调用时。
*   **动态默认值的陷阱**: 如果默认参数是动态生成的（如 `datetime.now()`）或可变对象（如 `{}` 或 `[]`），所有使用默认值的调用将共享同一个结果或对象，导致状态混乱。
*   **推荐模式**:
1.  将默认参数的值设置为 `None`。
2.  在函数的文档字符串（docstring）中明确说明该参数的实际默认行为。
3.  在函数体内，检查该参数是否为 `None`。如果是，则动态地生成实际的默认值（例如，调用 `datetime.now()` 或创建一个新的空字典）。
*   **类型注解**: 这种模式也适用于类型注解，可以明确参数可以是 `None` 或特定类型。

**要点回顾**:
*   默认参数值仅在函数定义时评估一次：在模块加载期间。这可能导致动态值（如函数调用、新创建的对象和容器类型）出现奇怪的行为。
*   使用 `None` 作为关键字参数的占位符默认值，该参数必须动态初始化其实际默认值。在函数的文档字符串中记录该参数的预期默认值。在函数体内检查 `None` 参数值以触发正确的默认行为。
*   使用 `None` 作为关键字参数默认值也适用于类型注解。

### Item 37: 使用关键字专用和位置专用参数强制执行清晰性

Python 提供了关键字专用参数和位置专用参数，以增强函数接口的清晰度和健壮性。

*   **关键字专用参数**:
*   定义在函数参数列表中的 `*` 之后（或 `*args` 之后）。
*   调用时只能使用关键字形式传递，不能通过位置传递。
*   强制调用者明确参数的含义，提高代码可读性，并允许在不破坏向后兼容性的情况下添加新的可选参数。
*   **位置专用参数**:
*   定义在函数参数列表中的 `/` 之前。
*   调用时只能通过位置传递，不能使用关键字传递。
*   允许在不影响现有调用者的情况下更改参数的名称，从而解耦函数实现与调用者。
*   **混合使用**: 在 `/` 和 `*` 之间的参数可以根据需要通过位置或关键字传递，这是 Python 参数传递的默认行为。
*   **应用场景**: 当函数有多个布尔参数来控制行为时，使用关键字专用参数可以避免混淆。当希望函数参数的名称不影响调用者时，使用位置专用参数。

**要点回顾**:
*   关键字专用参数强制调用者通过关键字（而不是位置）提供某些参数，这使得函数调用的意图更加清晰。关键字专用参数在参数列表中的 `*` 之后定义（无论是单独出现还是作为可变参数如 `*args` 的一部分）。
*   位置专用参数确保调用者不能使用关键字传递某些参数，这有助于减少耦合。位置专用参数在参数列表中的单个 `/` 之前定义。
*   参数列表中的 `/` 和 `*` 字符之间的参数可以通过位置或关键字传递，这是 Python 参数的默认行为。

### Item 38: 使用 `functools.wraps` 定义函数装饰器

装饰器是 Python 中一种强大的元编程机制，允许在不修改函数源代码的情况下，在函数执行前后添加额外的行为。`functools.wraps` 是一个装饰器，用于帮助编写其他装饰器，它能将原始函数的元数据（如名称、文档字符串、注解等）复制到被包装的函数上。

*   **装饰器的作用**: 装饰器可以用于日志记录、访问控制、性能度量、注册函数等多种场景。
*   **装饰器实现**: 通常通过定义一个接受函数作为参数的外部函数，并在其内部定义一个包装函数来实现。包装函数执行额外的逻辑，然后调用原始函数，最后返回结果。
*   **元数据丢失问题**: 未经处理的装饰器会覆盖被包装函数的元数据，导致调试工具（如 `help()`、pdb）和序列化工具（如 `pickle`）出现问题。
*   **`functools.wraps` 的作用**: `@wraps(func)` 装饰器应用于包装函数，将原始函数 `func` 的元数据复制到包装函数上，从而解决了元数据丢失的问题。
*   **保持接口一致性**: 使用 `wraps` 可以确保被装饰的函数在外部看起来与未被装饰的函数具有相同的接口和行为，这对于维护代码的稳定性和可调试性至关重要。

**要点回顾**:
*   Python 中的装饰器是允许函数在运行时修改另一个函数的语法。
*   使用装饰器可能会导致像调试器这样的内省工具出现奇怪的行为。
*   在定义自己的装饰器时，使用 `functools` 内置模块中的 `wraps` 装饰器来避免任何问题。

### Item 39: 优先使用 `functools.partial` 而非 `lambda` 表达式作为粘合函数

在许多 Python API 中，需要接受函数作为参数。当提供的函数签名与 API 所需的签名不完全匹配时，通常需要使用“粘合函数”来适配。`lambda` 表达式和 `functools.partial` 都可以实现这一目的，但 `functools.partial` 通常是更优的选择。

*   **函数签名不匹配**: API 可能需要特定参数顺序或数量的函数，而我们拥有的函数可能不符合这些要求。
*   **`lambda` 的作用**: `lambda` 表达式可以创建临时的、匿名的函数，用于重新排序参数或固定（pin）某些参数的值。例如，`lambda total, value: original_func(value, total)` 可以调整参数顺序。
*   **`functools.partial` 的作用**: `functools.partial` 是一个更通用的工具，它可以创建一个新的可调用对象，该对象在被调用时，会以预设的参数（位置参数和关键字参数）调用原始函数。这被称为“偏函数应用”或“柯里化”。
*   **`partial` 的优势**:
*   **可读性**: `partial` 的意图更清晰，代码更易于理解。
*   **可调试性**: `partial` 对象可以被检查，包括其绑定的参数和原始函数，这有助于调试。
*   **封装性**: 能够方便地绑定关键字参数，而 `lambda` 实现起来则更繁琐。
*   **何时使用 `lambda`**: 当需要完全重新排序参数时，`lambda` 是唯一选择，因为 `partial` 只能固定参数，不能改变它们的相对顺序。
*   **状态访问**: 当需要访问或修改状态时，除了 `lambda` 和 `partial`，还可以考虑使用闭包或类。

**要点回顾**:
*   `lambda` 表达式可以简洁地通过重新排序参数或固定某些参数值来使两个函数接口兼容。
*   `functools` 内置模块中的 `partial` 函数是创建具有固定位置和关键字参数的函数的一个通用工具。
*   如果需要重新排序被包装函数的参数，则使用 `lambda` 而不是 `partial`。

## Effective Python - 6

## 6

本章深入探讨了如何利用 Graph Neural Networks (GNNs) 和 Graph Foundation Models (GFMs) 来提升 Python 编程的效率和能力。我们重点关注这些模型在处理复杂数据结构和执行高级任务方面的核心贡献，并阐述了它们的主要观点。

**核心贡献与主要观点：**

本章的核心贡献在于展示了 GNNs 和 GFMs 如何通过其独特的架构和学习机制，为 Python 开发者提供强大的工具集。主要观点包括：

*   **强大的数据表示能力：** GNNs 能够有效地学习节点和边的表示 (Node Embedding)，捕捉图中复杂的结构信息和特征。这使得它们在处理非欧几里得数据，如社交网络、分子结构和知识图谱时表现出色。
*   **Message Passing 机制的有效性：** GNNs 的核心是 Message Passing 机制，它允许节点之间通过聚合邻居信息来更新自身的表示。本章详细阐述了不同 GNNs 模型（如 Graph Convolutional Networks (GCN) 和 Graph Attention Networks (GAT)）在 Message Passing 上的变体及其对性能的影响。
*   **Graph Foundation Models (GFMs) 的通用性与迁移学习：** GFMs 作为预训练的 GNN 模型，展现了强大的通用性和迁移学习能力。通过在海量图数据上进行 Pre-training，GFMs 能够学习到通用的图结构和节点表示，并可以通过 Fine-tuning、In-context Learning、Few-shot Learning 或 Zero-shot Learning 等方式快速适应下游任务，如 Graph Classification、Node Classification 和 Link Prediction。
*   **处理异构图和复杂图结构：** 本章也讨论了 GNNs 如何处理 Heterogeneous Graph 和 Homogeneous Graph，以及在 Graph Isomorphism 等挑战性问题上的应用。
*   **在 Python 生态中的应用：** 我们展示了如何在 Python 中利用现有的库（如 PyTorch Geometric, Deep Graph Library (DGL)）来实现和部署 GNNs 和 GFMs。

**逻辑顺序组织总结：**

本章按照以下逻辑顺序组织内容，以确保内容的连贯性和逻辑完整性：

1.  **GNNs 基础概念与原理：** 首先介绍了 GNNs 的基本概念，包括图的表示、Message Passing 机制以及常见的 GNNs 架构，如 GCN 和 GAT。
2.  **GNNs 的核心任务：** 随后，本章探讨了 GNNs 在各种图相关任务中的应用，包括 Node Classification、Link Prediction、Graph Classification 和 Graph Generation。
3.  **Graph Foundation Models (GFMs) 的兴起：** 接着，我们深入介绍了 GFMs 的概念、优势以及其在实现通用图表示学习和迁移学习方面的作用。
4.  **GFMs 的学习范式：** 详细阐述了 GFMs 的不同学习范式，包括 Self-supervised Learning、Contrastive Learning、Fine-tuning、In-context Learning、Few-shot Learning 和 Zero-shot Learning。
5.  **高级应用与挑战：** 最后，本章讨论了 GNNs 和 GFMs 在更高级的应用场景，如 Multi-modal Learning、Cross-domain Transfer、Domain Adaptation 以及 Graph Anomaly Detection 中的应用，并提及了 Graph Pooling 等技术。

通过本章的学习，读者将能够深入理解 GNNs 和 GFMs 的工作原理，并掌握如何在 Python 中利用这些强大的模型来解决复杂的图数据问题，从而显著提升编程效率和研究能力。

## Effective Python - Comprehensions and Generators

# 章节标题: Effective Python - Comprehensions and Generators

本章深入探讨了 Python 中用于高效数据处理的两种强大工具：Comprehensions 和 Generators。它们提供了简洁、可读性强且性能优越的代码编写方式，尤其是在处理列表、字典和集合等数据结构时。

## 子章节概述

本章涵盖了以下关键主题：

### Item 40: Use Comprehensions Instead of `map` and `filter`

本节强调了使用 Python 的 comprehensions（包括 list comprehensions, dictionary comprehensions, 和 set comprehensions）来替代 `map` 和 `filter` 函数的优势。Comprehensions 提供了更简洁、更具可读性的语法来创建新的数据结构，同时允许轻松地进行过滤操作。

*   **核心观点**: Comprehensions 比 `map` 和 `filter` 更清晰，因为它们不需要 `lambda` 表达式，并且可以方便地使用 `if` 子句进行过滤。
*   **关键优势**:
*   **可读性**: 语法更直观，减少了 `lambda` 的视觉噪音。
*   **灵活性**: 轻松实现过滤功能，这是 `map` 单独无法做到的。
*   **多类型支持**: 适用于列表、字典和集合的创建。
*   **注意事项**: Comprehensions 会一次性生成整个结果列表，这可能导致内存占用较高，而 `map` 和 `filter` 返回迭代器，更节省内存。对于大型数据集，建议考虑 generator expressions。

### Item 41: Avoid More Than Two Control Subexpressions in Comprehensions

本节讨论了 comprehensions 中多重循环和条件的使用，并提出了一个重要的编码实践建议。

*   **核心观点**: 尽管 comprehensions 支持多层循环和多个条件，但为了保持代码的可读性，应避免使用超过两个控制子表达式（例如，两个 `for` 循环，或一个 `for` 循环和一个 `if` 条件，或两个 `if` 条件）。
*   **关键优势**:
*   **简洁性**: 允许在单行代码中处理复杂的迭代和过滤逻辑。
*   **可读性**: 在适度使用时，可以清晰地表达意图。
*   **注意事项**: 当控制子表达式超过两个时，代码会变得难以理解，此时应回归使用传统的 `for` 和 `if` 语句，并可能需要一个辅助函数。

### Item 42: Reduce Repetition in Comprehensions with Assignment Expressions

本节介绍了如何利用 Python 3.8 引入的 assignment expressions（walrus operator `:=`）来优化 comprehensions 中的重复计算。

*   **核心观点**: Assignment expressions 允许在 comprehension 中捕获表达式的值，并在同一 comprehension 的其他部分（如条件或值部分）重用该值，从而提高可读性和性能，并减少潜在的 bug。
*   **关键优势**:
*   **减少重复**: 避免了对同一表达式进行多次计算。
*   **提高性能**: 减少了不必要的函数调用或计算。
*   **增强可读性**: 使代码更清晰，避免了重复的逻辑。
*   **注意事项**:
*   Assignment expressions 在 comprehension 中使用时，变量会“泄漏”到包含作用域，这与不使用 assignment expressions 的 comprehension 行为不同。
*   应将 assignment expression 放在条件部分以确保其可靠性。

### Item 43: Consider Generators Instead of Returning Lists

本节深入探讨了 generators 的优势，强调了它们在内存效率和代码清晰度方面的优越性。

*   **核心观点**: Generator 函数使用 `yield` 关键字，可以按需生成值，而不是一次性返回整个列表。这使得它们在处理大型数据集或无限序列时更加高效和内存友好。
*   **关键优势**:
*   **内存效率**: 仅在需要时生成值，避免了将所有结果存储在内存中。
*   **代码清晰度**: 移除了累积结果列表的样板代码，使函数逻辑更直接。
*   **处理大型/无限数据**: 能够处理无法完全加载到内存中的数据。
*   **注意事项**: Generator 返回的迭代器是状态化的，只能使用一次。

### Item 44: Consider Generator Expressions for Large List Comprehensions

本节介绍了 generator expressions，它们是 list comprehensions 的一种变体，使用圆括号 `()` 而非方括号 `[]`，从而创建迭代器而非列表。

*   **核心观点**: Generator expressions 是处理大型数据集时 list comprehensions 的内存高效替代方案。它们生成迭代器，一次一个地产生值，从而避免了内存溢出问题。
*   **关键优势**:
*   **内存效率**: 与 list comprehensions 不同，它们不一次性构建整个列表。
*   **可组合性**: 可以轻松地将一个 generator expression 的输出作为另一个的输入，实现链式处理。
*   **性能**: 链式组合的 generator expressions 执行速度快且内存占用低。
*   **注意事项**: 与 generator 函数一样，generator expressions 返回的迭代器也是状态化的，只能使用一次。

### Item 45: Compose Multiple Generators with `yield from`

本节介绍了 `yield from` 语句，它提供了一种优雅的方式来组合多个 generator。

*   **核心观点**: `yield from` 语句允许一个 generator 委托给另一个子 generator，将子 generator 生成的所有值“转发”给调用者。这极大地简化了组合多个 generator 的代码。
*   **关键优势**:
*   **代码简洁**: 消除了手动迭代子 generator 并逐个 `yield` 的样板代码。
*   **可读性**: 使 generator 的组合逻辑更清晰、更直观。
*   **性能**: 通常比手动迭代子 generator 的方式更高效。

### Item 46: Pass Iterators into Generators as Arguments Instead of Calling the `send` Method

本节讨论了 generator 的 `send` 方法以及为什么建议使用传递迭代器的方式来代替它。

*   **核心观点**: 虽然 `send` 方法可以实现 generator 的双向通信，但它会使代码难以理解，并且与 `yield from` 结合使用时可能产生意外的 `None` 值。更推荐的做法是将输入迭代器作为参数传递给 generator。
*   **关键优势 (传递迭代器)**:
*   **清晰性**: 代码更易于理解，逻辑更直观。
*   **可组合性**: 允许将输入迭代器轻松地传递给多个组合的 generator。
*   **避免 `send` 的陷阱**: 避免了 `send` 与 `yield from` 结合时可能出现的 `None` 值问题。
*   **注意事项**: `send` 方法的使用会增加代码的复杂性，并且在与 `yield from` 结合时行为难以预测。

### Item 47: Manage Iterative State Transitions with a Class Instead of the Generator `throw` Method

本节探讨了 generator 的 `throw` 方法，并建议使用类来管理状态转换，以提高代码的可读性和可维护性。

*   **核心观点**: Generator 的 `throw` 方法虽然可以注入异常并控制 generator 的执行流程，但会使代码变得复杂且难以阅读。使用一个状态管理类来处理状态转换和迭代是更优的选择。
*   **关键优势 (使用类)**:
*   **可读性**: 代码更清晰，状态管理和转换逻辑更直观。
*   **可维护性**: 易于理解和修改，减少了嵌套和样板代码。
*   **封装性**: 将状态和行为封装在类中，提高了代码的组织性。
*   **注意事项**: `throw` 方法的使用会增加代码的复杂性，并且在处理异常流程时不如使用类来得清晰。

---

本章的核心贡献在于阐明了 Python 中 comprehensions 和 generators 的强大功能及其最佳实践。通过使用这些工具，开发者可以编写出更简洁、更高效、更易于维护的代码，尤其是在处理数据流和复杂迭代逻辑时。本章强调了可读性和内存效率的重要性，并提供了避免常见陷阱的实用建议。

## Effective Python - 7

## 7

本章深入探讨了 Graph Neural Networks (GNNs) 在处理和理解复杂图结构数据方面的强大能力。我们将重点关注 GNNs 的核心机制，包括 Message Passing 范式，以及如何通过 Node Embedding 来捕捉节点间的关系和特征。

本章将从以下几个关键方面展开：

*   **GNNs 的基础与演进**: 我们将回顾 GNNs 的发展历程，从早期的 Graph Convolutional Networks (GCN) 到更具代表性的 Graph Attention Networks (GAT) 和 GraphSAGE。重点介绍它们在聚合邻居信息和更新节点表示方面的不同策略。
*   **Message Passing 范式**: 深入解析 Message Passing 的工作原理，这是 GNNs 的核心计算框架。我们将解释消息的生成、传递和聚合过程，以及它如何实现节点特征的迭代更新。
*   **Node Embedding 的学习**: 探讨如何通过 GNNs 学习到有意义的 Node Embedding。我们将介绍不同的 Embedding 策略，以及这些 Embedding 如何用于下游任务。
*   **GNNs 的应用领域**: 详细介绍 GNNs 在各种实际问题中的应用，包括但不限于 Node Classification, Link Prediction, Graph Classification, Graph Generation, 以及 Graph Anomaly Detection。
*   **Graph Foundation Models (GFMs) 的兴起**: 介绍 Graph Foundation Models (GFMs) 的概念，以及它们如何通过 Pre-training 和 Fine-tuning 的方式，利用 Self-supervised Learning 等技术，在各种图学习任务中展现出强大的 Cross-domain Transfer 和 Few-shot Learning 能力。我们将讨论 GFMs 在 In-context Learning 和 Zero-shot Learning 方面的潜力。
*   **处理复杂图结构**: 讨论如何处理 Heterogeneous Graph 和 Homogeneous Graph，以及在处理 Graph Isomorphism 问题时的挑战和解决方案。
*   **多模态与 GNNs**: 探讨 Multi-modal Learning 与 GNNs 的结合，如何利用不同模态的数据来增强图学习的效果。
*   **前沿技术与未来展望**: 简要介绍 Contrastive Learning 在 GNNs 中的应用，以及 GNNs 在 Knowledge Graph 和其他新兴领域的未来发展方向。

本章旨在为读者提供对 GNNs 及其相关技术的全面理解，并激发在图学习领域的进一步探索。

## Effective Python - Classes and Interfaces

## Python 高效编程 - 类与接口

本章深入探讨了 Python 中类和接口的有效使用，强调了面向对象编程的原则以及如何结合函数式编程的风格来编写更清晰、更易于维护的代码。

### Item 48: 接受函数而非类来定义简单接口

Python 的许多内置 API 允许通过传递函数来定制行为，这些函数充当“钩子”（hooks）。函数是定义钩子的理想选择，因为它们比类更易于描述和实现。Python 的一等公民函数特性使得函数和方法可以像其他值一样被传递和引用。

*   **示例：** `list.sort()` 方法的 `key` 参数接受一个函数来指定排序依据。
*   **`defaultdict` 的钩子：** `collections.defaultdict` 允许提供一个函数，在访问缺失键时调用该函数以返回默认值。
*   **状态闭包与类：** 当钩子需要维护状态时，可以使用状态闭包或定义一个带有 `__call__` 方法的类。`__call__` 方法允许类的实例像函数一样被调用，这使得代码更清晰，并表明该类的实例旨在用作函数参数。

**要点回顾：**

*   对于简单的接口，可以使用函数而不是类。
*   函数和方法在 Python 中是一等公民，可以作为表达式使用。
*   `__call__` 特殊方法使类的实例可以像普通 Python 函数一样被调用，并通过 `callable` 检查。
*   当需要函数维护状态时，考虑定义一个提供 `__call__` 方法的类，而不是实现状态闭包函数。

### Item 49: 优先使用面向对象的多态性而非带 `isinstance` 检查的函数

在处理不同类型的对象时，使用 `isinstance` 检查来控制流程会使代码变得庞大且难以维护。面向对象编程（OOP）通过将行为封装在方法中，并利用多态性在运行时动态分派方法调用到正确的子类实现，从而解决了这个问题。

*   **抽象语法树（AST）示例：** 在评估 AST 时，使用 `isinstance` 检查会导致一个巨大的 `if` 语句。通过将 `evaluate` 方法定义在每个节点类中，并利用多态性，可以实现更简洁的代码。
*   **多态性的优势：** 允许轻松扩展功能（如添加 `pretty` 方法），而无需修改现有的评估函数。代码更易于组织、扩展和测试。

**要点回顾：**

*   Python 程序可以使用 `isinstance` 内置函数根据对象的类型在运行时改变行为。
*   多态性是一种面向对象编程（OOP）技术，用于在运行时将方法调用分派到最具体的子类实现。
*   使用多态性（而非 `isinstance` 检查）的代码更易于阅读、维护、扩展和测试。

### Item 50: 考虑使用 `functools.singledispatch` 进行函数式编程而非面向对象的多态性

当需要为多种类型实现相同的功能时，OOP 的类中心化组织方式可能导致代码分散在多个模块中，难以维护。`functools.singledispatch` 提供了一种函数式编程的替代方案，允许根据参数类型来选择函数版本，从而将相关功能聚合在一起。

*   **`singledispatch` 的工作原理：** 使用 `@functools.singledispatch` 装饰器定义一个基础函数，然后使用 `@register` 装饰器为特定类型注册实现。
*   **AST 示例的重构：** 使用 `singledispatch` 可以为 AST 的不同节点类型实现 `my_evaluate` 和 `my_pretty` 函数，而无需修改节点类本身。
*   **权衡：** `singledispatch` 在添加新类型时需要为每个分派函数注册实现，而 OOP 在添加新方法时需要更新每个类。`singledispatch` 在许多情况下提供了更好的代码组织和可维护性。

**要点回顾：**

*   面向对象编程导致类中心化的代码组织，这可能使大型程序的构建和维护变得困难，因为行为分散在许多模块中。
*   单分派（Single dispatch）是一种使用函数而非方法多态性来实现动态分派的替代方法，可以将相关功能更紧密地聚合在源代码中。
*   Python 的 `functools` 内置模块提供了一个 `singledispatch` 装饰器，可用于实现单分派行为。
*   具有高度独立系统且操作相同底层数据的程序可能受益于函数式单分派风格，而非 OOP。

### Item 51: 优先使用 `dataclasses` 定义轻量级类

`dataclasses` 模块提供了一种简洁的方式来定义主要用于存储数据的类，大大减少了样板代码。它自动生成 `__init__`、`__repr__`、`__eq__`、`__hash__` 等特殊方法，并支持类型提示和关键字参数强制。

*   **避免 `__init__` 样板代码：** 使用 `@dataclass` 装饰器，只需在类体中声明属性及其类型即可自动生成 `__init__` 方法。
*   **强制关键字参数：** 通过 `kw_only=True` 参数，可以强制所有初始化参数必须通过关键字传递，提高代码清晰度。
*   **提供默认属性值：** 可以直接在类体中为属性赋值，或使用 `field(default_factory=...)` 处理可变默认值。
*   **对象表示为字符串：** `dataclasses` 自动提供有用的 `__repr__` 实现。
*   **对象转换为元组和字典：** `astuple()` 和 `asdict()` 函数方便地将 `dataclass` 对象转换为元组或字典。
*   **对象相等性检查：** `dataclasses` 自动实现 `__eq__` 方法，支持基于值的相等性比较。
*   **对象比较：** 通过 `order=True` 参数，可以自动实现对象间的比较方法。

**要点回顾：**

*   `dataclasses` 内置模块的 `dataclass` 装饰器可用于定义无需大量样板代码的标准类。
*   使用 `dataclasses` 可以帮助避免 Python 标准面向对象特征的冗长和易错性。
*   `dataclasses` 模块提供了额外的辅助函数用于转换（如 `asdict`、`astuple`）和高级属性行为（如 `field`）。
*   了解如何自行实现面向对象惯用法很重要，以便在需要更多自定义时能够从 `dataclasses` 迁移。

### Item 52: 使用 `@classmethod` 多态性来通用地构造对象

Python 的类本身也支持多态性，这使得类可以提供通用的对象构造方式。`@classmethod` 允许定义替代构造函数，从而实现类方法多态性。

*   **Map-Reduce 示例：** 在 Map-Reduce 实现中，`InputData` 和 `Worker` 类可以定义 `@classmethod` 来提供通用的输入生成和工作者创建方法。
*   **通用性：** 通过类方法多态性，可以创建不依赖于具体子类的通用函数（如 `mapreduce`），从而提高代码的可重用性和灵活性。

**要点回顾：**

*   Python 每个类只支持一个构造函数：`__init__` 方法。
*   使用 `@classmethod` 定义类的替代构造函数。
*   使用类方法多态性提供通用的方式来构建和连接多个具体子类。

### Item 53: 使用 `super` 初始化父类

`super()` 函数是 Python 中处理类继承和多重继承的关键。它确保了父类方法的正确调用顺序，并解决了多重继承中可能出现的重复初始化和方法冲突问题。

*   **直接调用父类 `__init__` 的问题：** 在多重继承和菱形继承中，直接调用父类构造函数会导致初始化顺序混乱和重复调用。
*   **`super()` 的优势：** `super()` 利用方法解析顺序（MRO）来确保父类方法（包括 `__init__`）被调用一次，并按照正确的顺序执行。
*   **MRO：** Python 的 MRO 算法（C3 线性化）定义了类继承的查找顺序。
*   **`super()` 的用法：** `super()` 可以不带参数调用（在类定义内部），也可以带类和实例参数调用（用于更精细的控制）。

**要点回顾：**

*   Python 的标准 MRO 解决了父类初始化顺序和菱形继承的问题。
*   使用不带参数的 `super` 内置函数来初始化父类和调用父类方法。

### Item 54: 考虑使用 Mix-in 类组合功能

Mix-in 类是一种提供特定功能集合的类，它们不定义自己的实例属性，也不需要调用其 `__init__` 构造函数。Mix-in 类可以与多个父类组合，以最小化重复代码并最大化代码复用。

*   **`ToDictMixin` 示例：** 提供将对象转换为字典的功能，可以递归处理嵌套对象和容器。
*   **可插拔行为：** Mix-in 的功能可以被子类覆盖，以实现特定的定制。
*   **组合 Mix-in：** 可以将多个 Mix-in 类组合起来，例如 `JsonMixin`，以提供 JSON 序列化和反序列化功能。

**要点回顾：**

*   避免使用具有实例属性和 `__init__` 的多重继承，如果 Mix-in 类可以达到相同的结果。
*   在实例级别使用可插拔的行为来为每个类提供定制，当 Mix-in 类需要时。
*   Mix-in 可以包含实例方法或类方法，取决于您的需求。
*   组合 Mix-in 以从简单的行为创建复杂的功能。

### Item 55: 优先使用公共属性而非私有属性

Python 的私有属性（以双下划线开头）并非严格强制执行，而是通过名称转换（name mangling）实现。鼓励使用公共属性，并辅以文档说明来指导子类和外部用户如何使用。

*   **Python 的“同意的成年人”哲学：** Python 倾向于开放和允许扩展，而不是严格的访问控制。
*   **名称转换：** `__private_field` 会被转换为 `_ClassName__private_field`。
*   **保护属性（Protected Attributes）：** 使用单下划线前缀（`_protected_field`）作为约定，表示该属性是内部的，但允许子类访问。
*   **避免私有属性的陷阱：** 私有属性会使子类继承和重写变得困难和脆弱。
*   **何时使用私有属性：** 仅在担心子类命名冲突时才考虑使用私有属性。

**要点回顾：**

*   Python 编译器不会严格执行私有属性。
*   从一开始就计划允许子类使用您的内部 API 和属性，而不是选择锁定它们。
*   使用受保护字段的文档来指导子类，而不是试图强制执行访问控制与私有属性。
*   仅在避免与不受控制的子类发生命名冲突时才考虑使用私有属性。

### Item 56: 优先使用 `dataclasses` 创建不可变对象

创建不可变对象有助于编写更健壮、更易于测试的函数式风格代码。`dataclasses` 模块通过 `frozen=True` 参数提供了一种简单的方式来创建不可变对象。

*   **不可变对象的优势：** 减少可变状态带来的潜在问题，便于测试和推理。
*   **防止对象被修改：** 通过 `frozen=True` 参数，`dataclasses` 会在尝试修改属性时引发 `AttributeError`。
*   **创建修改副本：** `dataclasses.replace()` 函数允许创建对象的新副本，并修改部分属性，而无需手动复制所有字段。
*   **在字典和集合中使用：** 不可变对象可以作为字典的键和集合的成员，因为它们具有稳定的哈希值和相等性比较。
*   **与 `namedtuple` 的比较：** `dataclasses` 提供了类似 `namedtuple` 的功能，但更灵活，并且是现代 Python 的首选。

**要点回顾：**

*   使用不可变对象的函数式风格代码通常比修改状态并产生副作用的命令式风格代码更健壮。
*   创建自定义不可变对象的最简单方法是使用 `dataclasses` 内置模块；在定义类时应用 `dataclass` 装饰器并传递 `frozen=True` 参数。
*   `dataclasses` 模块的 `replace` 辅助函数允许创建具有更改属性的不可变对象的副本，从而更易于编写函数式风格的代码。
*   使用 `dataclass` 创建的不可变对象在值上是可比较的，并且具有稳定的哈希值，这允许它们用作字典的键和集合的值。

### Item 57: 为自定义容器类型继承 `collections.abc` 类

`collections.abc` 模块提供了抽象基类（Abstract Base Classes, ABCs），用于定义各种容器类型的接口。继承这些 ABCs 可以确保自定义容器类遵循 Python 的标准协议，并自动获得许多有用的方法。

*   **直接继承内置容器的局限性：** 直接继承 `list` 或 `dict` 可以利用其基本行为，但要实现完整的容器语义，需要手动实现大量特殊方法。
*   **`collections.abc` 的优势：** 继承 `collections.abc` 中的 ABCs（如 `Sequence`、`Mapping`、`Set`）可以确保实现所有必需的特殊方法，并自动获得其他派生方法。
*   **示例：** `SequenceNode` 类继承自 `IndexableNode`（实现了 `__getitem__`）并结合 `collections.abc.Sequence`，可以自动获得 `__len__`、`count`、`index` 等方法。

**要点回顾：**

*   对于简单的用例，直接从 Python 的容器类型（如 `list` 或 `dict`）继承以利用其基本行为是可以的。
*   注意，在不继承内置类型的情况下，正确实现自定义容器类型需要大量方法。
*   为了确保自定义容器类匹配所需行为，请让它们继承 `collections.abc` 中定义的接口。

## Effective Python - 8

## 8

本章深入探讨了如何利用 Python 实现高效的 Graph Neural Networks (GNNs) 和 Graph Foundation Models (GFMs)。我们将重点关注 GNNs 的核心组件和工作原理，包括 Message Passing 机制、Node Embedding 的生成以及常见的 GNNs 架构，如 Graph Convolutional Networks (GCN) 和 Graph Attention Networks (GAT)。此外，本章还将介绍如何利用 Transformer 架构来增强 GNNs 的能力，特别是在处理复杂图结构和实现更强大的表示学习方面。

我们将从基础的图数据结构和图表示方法开始，介绍如何使用 Python 库（如 PyTorch Geometric 和 Deep Graph Library (DGL)）来构建和操作图。随后，我们将详细讲解 GNNs 在各种图学习任务中的应用，包括 Node Classification、Link Prediction、Graph Classification 和 Graph Anomaly Detection。

本章的重点之一是介绍 GFM 的概念和实现。GFMs，特别是那些基于 Transformer 的模型，通过大规模的 Pre-training 和 Self-supervised Learning，能够学习到通用的图表示，并为下游任务提供强大的迁移能力。我们将探讨如何进行 GFM 的 Pre-training，以及如何通过 Fine-tuning、In-context Learning、Few-shot Learning 和 Zero-shot Learning 等技术来适应不同的图学习场景。

此外，本章还将涵盖一些高级主题，例如：

*   **异构图 (Heterogeneous Graph) 和同质图 (Homogeneous Graph) 的处理**: 介绍如何区分和处理不同类型的图结构。
*   **图池化 (Graph Pooling)**: 探讨如何有效地聚合图节点信息，以实现图级别的表示。
*   **对比学习 (Contrastive Learning)**: 介绍如何利用对比学习来提升 GNNs 的表示能力。
*   **多模态学习 (Multi-modal Learning)**: 探讨如何将图数据与其他模态的数据（如文本、图像）结合，以实现更全面的学习。
*   **跨域迁移 (Cross-domain Transfer) 和域适应 (Domain Adaptation)**: 介绍如何将在一个领域训练好的 GNNs 模型应用到另一个领域。
*   **知识图谱 (Knowledge Graph) 的表示学习**: 探讨 GNNs 在知识图谱推理和补全方面的应用。

通过本章的学习，读者将能够掌握使用 Python 构建和训练高效 GNNs 和 GFM 的关键技术，并能够将其应用于各种实际的图学习问题。

## Effective Python - Metaclasses and Attributes

## Metaclasses and Attributes

Metaclasses 是 Python 中一个强大但常被误解的特性，它们允许你拦截类的创建过程，并为类定义提供特殊的行为。与此类似，Python 还提供了一些动态定制属性访问的内置功能。这些功能与面向对象构造结合，为从简单类到复杂类的过渡提供了强大的工具。

然而，这些能力也伴随着许多陷阱。动态属性允许你覆盖对象，并可能导致意外的副作用。Metaclasses 可以产生非常奇怪且难以理解的行为。因此，遵循“最小惊讶原则”至关重要，只在实现良好理解的模式时使用这些机制。

### Item 58: Use Plain Attributes Instead of Setter and Getter Methods

对于从其他语言转到 Python 的程序员来说，自然会想到在类中实现显式的 getter 和 setter 方法来访问受保护的属性。然而，在 Python 中，这种做法并不 Pythonic。

```python
class OldResistor:
def __init__(self, ohms):
self._ohms = ohms

def get_ohms(self):
return self._ohms

def set_ohms(self, ohms):
self._ohms = ohms
```

使用这些 setter 和 getter 方法虽然简单，但显得笨拙，尤其是在进行原地增量等操作时。

```python
r0 = OldResistor(50e3)
print("Before:", r0.get_ohms())
r0.set_ohms(10e3)
print("After: ", r0.get_ohms())

r0.set_ohms(r0.get_ohms() - 4e3)
assert r0.get_ohms() == 6e3
```

这些方法虽然有助于定义类的接口，封装功能，验证使用，并定义边界，但在 Python 中，你永远不需要实现显式的 setter 或 getter 方法。你应该始终从简单的公共属性开始你的实现。

```python
class Resistor:
def __init__(self, ohms):
self.ohms = ohms
self.voltage = 0
self.current = 0

r1 = Resistor(50e3)
r1.ohms = 10e3
```

这些属性使得原地增量等操作自然而清晰：

```python
r1.ohms += 5e3
```

如果将来需要为属性设置添加特殊行为，可以迁移到 `@property` 装饰器及其对应的 `setter` 属性。例如，可以定义一个 `VoltageResistance` 子类，通过 `voltage` 属性的赋值来改变 `current`。

```python
class VoltageResistance(Resistor):
def __init__(self, ohms):
super().__init__(ohms)
self._voltage = 0

@property
def voltage(self):
return self._voltage

@voltage.setter
def voltage(self, voltage):
self._voltage = voltage
self.current = self._voltage / self.ohms
```

现在，赋值给 `voltage` 属性将运行 `voltage` setter 方法，进而更新对象的 `current` 属性。

```python
r2 = VoltageResistance(1e2)
print(f"Before: {r2.current:.2f} amps")
r2.voltage = 10
print(f"After:  {r2.current:.2f} amps")
```

指定属性的 setter 还可以进行类型检查和值验证。例如，可以创建一个类来确保所有电阻值都大于零欧姆。

```python
class BoundedResistance(Resistor):
def __init__(self, ohms):
super().__init__(ohms)

@property
def ohms(self):
return self._ohms

@ohms.setter
def ohms(self, ohms):
if ohms <= 0:
raise ValueError(f"ohms must be > 0; got {ohms}")
self._ohms = ohms
```

为属性赋值无效电阻值现在会引发异常。

```python
r3 = BoundedResistance(1e3)
try:
r3.ohms = 0
except ValueError as e:
print(e)
```

在构造函数中传递无效值也会引发异常，因为 `__init__` 会调用 setter。

还可以使用 `@property` 使父类的属性不可变。

```python
class FixedResistance(Resistor):
def __init__(self, ohms):
super().__init__(ohms)

@property
def ohms(self):
return self._ohms

@ohms.setter
def ohms(self, ohms):
if hasattr(self, "_ohms"):
raise AttributeError("Ohms is immutable")
self._ohms = ohms
```

尝试在构造后赋值给属性会引发异常。

```python
r4 = FixedResistance(1e3)
try:
r4.ohms = 2e3
except AttributeError as e:
print(e)
```

在使用 `@property` 方法实现 setter 和 getter 时，要确保行为不会令人惊讶。例如，不要在 getter 属性方法中设置其他属性，这会导致非常奇怪的行为。

```python
class MysteriousResistor(Resistor):
@property
def ohms(self):
self.voltage = self._ohms * self.current
return self._ohms

@ohms.setter
def ohms(self, ohms):
self._ohms = ohms

r7 = MysteriousResistor(10)
r7.current = 0.1
print(f"Before: {r7.voltage:.2f}")
r7.ohms # Accessing ohms triggers the getter
print(f"After:  {r7.voltage:.2f}")
```

最佳策略是在 `@property.setter` 方法中仅修改相关的对象状态。同时，要避免任何调用者可能不期望的副作用，如动态导入模块、运行耗时的辅助函数、执行 I/O 或进行昂贵的数据库查询。用户期望类的属性像任何其他 Python 对象一样：快速而简单。对于更复杂或耗时的操作，应使用普通方法。

`@property` 的最大缺点是属性的方法只能由子类共享。不相关的类无法共享相同的实现。然而，Python 也支持 _descriptors_（参见 [Item 60](#ch08#ch08lev1sec3): “[Use Descriptors for Reusable @property Methods](#ch08#ch08lev1sec3)”），它能够实现可重用的属性逻辑和许多其他用例。

#### Things to Remember

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用简单的公共属性定义新的类接口，并避免定义 setter 和 getter 方法。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `@property` 为对象属性的访问定义特殊行为。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 遵循最小惊讶原则，避免在 `@property` 方法中产生奇怪的副作用。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 确保 `@property` 方法是快速的；对于耗时或复杂的工作，特别是涉及 I/O 或引起副作用的操作，请使用普通方法。

### Item 59: Consider `@property` Instead of Refactoring Attributes

内置的 `@property` 装饰器可以轻松地使对实例属性的简单访问变得更加智能（参见 [Item 58](#ch08#ch08lev1sec1): “[Use Plain Attributes Instead of Setter and Getter Methods](#ch08#ch08lev1sec1)”）。`@property` 的一个高级但常见的用法是将曾经是简单的数值属性转换为即时计算。这非常有用，因为它允许你在不重写任何调用站点的情况下，迁移类所有现有的用法以获得新行为（如果存在你无法控制的调用代码，这一点尤其重要）。`@property` 还为随着时间的推移改进接口提供了重要的临时解决方案。

例如，假设要使用纯 Python 对象实现一个 leaky-bucket rate-limiting quota 系统。这里，`Bucket` 类表示剩余的 quota 量以及 quota 可用的持续时间。

```python
from datetime import datetime, timedelta

class Bucket:
def __init__(self, period):
self.period_delta = timedelta(seconds=period)
self.reset_time = datetime.now()
self.quota = 0

def __repr__(self):
return f"Bucket(quota={self.quota})"
```

leaky-bucket 算法通过确保每次填充 bucket 时，quota 量不会从一个周期延续到下一个周期来工作。

```python
def fill(bucket, amount):
now = datetime.now()
if (now - bucket.reset_time) > bucket.period_delta:
bucket.quota = 0
bucket.reset_time = now
bucket.quota += amount

def deduct(bucket, amount):
now = datetime.now()
if (now - bucket.reset_time) > bucket.period_delta:
return False  # Bucket hasn't been filled this period
if bucket.quota - amount < 0:
return False  # Bucket was filled, but not enough
bucket.quota -= amount
return True       # Bucket had enough, quota consumed
```

每次 quota 消费者想要执行某项操作时，它必须首先确保可以扣除它需要使用的 quota 量。

```python
bucket = Bucket(60)
fill(bucket, 100)
print(bucket)

if deduct(bucket, 99):
print("Had 99 quota")
else:
print("Not enough for 99 quota")

print(bucket)

if deduct(bucket, 3):
print("Had 3 quota")
else:
print("Not enough for 3 quota")

print(bucket)
```

最终，由于尝试扣除的 quota 超出了可用量，进度会被阻止。在这种情况下，bucket 的 quota 水平保持不变。

原始实现的缺点是，你永远不知道 bucket 的初始 quota 水平。Quota 在周期内被扣除，直到达到零。此时，`deduct` 将始终返回 `False`，直到 bucket 被重新填充。当发生这种情况时，了解调用者被 `deduct` 阻止是因为 `Bucket` 耗尽了 quota，还是因为 `Bucket` 在此期间根本没有 quota，将会非常有用。

为了解决这个问题，可以修改类以跟踪周期内发放的 `max_quota` 和同一周期内消耗的 `quota_consumed`。

```python
class NewBucket:
def __init__(self, period):
self.period_delta = timedelta(seconds=period)
self.reset_time = datetime.now()
self.max_quota = 0
self.quota_consumed = 0

def __repr__(self):
return (
f"NewBucket(max_quota={self.max_quota}, "
f"quota_consumed={self.quota_consumed})"
)
```

为了匹配原始 `Bucket` 类的先前接口，使用 `@property` 方法根据这些新属性即时计算当前 quota 水平。

```python
@property
def quota(self):
return self.max_quota - self.quota_consumed
```

当 `quota` 属性被赋值时，采取特殊操作以与 `fill` 和 `deduct` 函数的当前使用兼容。

```python
@quota.setter
def quota(self, amount):
delta = self.max_quota - amount
if amount == 0:
# Quota being reset for a new period
self.quota_consumed = 0
self.max_quota = 0
elif delta < 0:
# Quota being filled during the period
self.max_quota = amount + self.quota_consumed
else:
# Quota being consumed during the period
self.quota_consumed = delta
```

重新运行上面的演示代码会产生相同的结果。

```python
bucket = NewBucket(60)
print("Initial", bucket)
fill(bucket, 100)
print("Filled", bucket)

if deduct(bucket, 99):
print("Had 99 quota")
else:
print("Not enough for 99 quota")

print("Now", bucket)

if deduct(bucket, 3):
print("Had 3 quota")
else:
print("Not enough for 3 quota")

print("Still", bucket)
```

最好的部分是，使用 `Bucket.quota` 的代码不必更改或知道类已更改。新使用 `Bucket` 的代码可以做正确的事情，并直接访问 `max_quota` 和 `quota_consumed`。

特别喜欢 `@property`，因为它允许你随着时间的推移逐步改进数据模型。阅读上面的 `Bucket` 示例，你可能会认为 `fill` 和 `deduct` 最初应该作为实例方法实现。虽然你可能是对的，但在实践中，许多情况是对象以定义不佳的接口开始，或者充当哑数据容器（参见 [Item 51](#ch07#ch07lev1sec4): “[Prefer dataclasses for Defining Lightweight Classes](#ch07#ch07lev1sec4)” 获取示例）。当代码随时间增长、范围扩大、多个作者贡献而没有人考虑长期卫生时，等等，就会发生这种情况。

`@property` 是一个帮助你解决在实际代码中遇到的问题的工具。不要过度使用它。当你发现自己反复扩展 `@property` 方法时，可能是时候重构你的类，而不是进一步掩盖你代码的糟糕设计了。

#### Things to Remember

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `@property` 为现有的实例属性赋予新功能。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 通过使用 `@property` 逐步改进数据模型。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 当发现过度使用 `@property` 时，考虑重构类和所有调用站点。

### Item 60: Use Descriptors for Reusable `@property` Methods

`@property` 内置功能（参见 [Item 58](#ch08#ch08lev1sec1): “[Use Plain Attributes Instead of Setter and Getter Methods](#ch08#ch08lev1sec1)” 和 [Item 59](#ch08#ch08lev1sec2): “[Consider @property Instead of Refactoring Attributes](#ch08#ch08lev1sec2)”）的重大问题是重用。它装饰的方法不能为同一类的多个属性重用。它们也不能被不相关的类重用。

例如，假设要让一个类验证学生在家庭作业中收到的分数是否是百分制：

```python
class Homework:
def __init__(self):
self._grade = 0

@property
def grade(self):
return self._grade

@grade.setter
def grade(self, value):
if not (0 <= value <= 100):
raise ValueError("Grade must be between 0 and 100")
self._grade = value
```

使用 `@property` 使这个类易于使用：

```python
galileo = Homework()
galileo.grade = 95
```

假设还要给学生一个考试分数，考试有多个科目，每个科目都有单独的分数：

```python
class Exam:
def __init__(self):
self._writing_grade = 0
self._math_grade = 0

@staticmethod
def _check_grade(value):
if not (0 <= value <= 100):
raise ValueError("Grade must be between 0 and 100")
```

这很快就会变得乏味。对于考试的每个部分，都需要添加一个新的 `@property` 和相关的验证：

```python
@property
def writing_grade(self):
return self._writing_grade

@writing_grade.setter
def writing_grade(self, value):
self._check_grade(value)
self._writing_grade = value

@property
def math_grade(self):
return self._math_grade

@math_grade.setter
def math_grade(self, value):
self._check_grade(value)
self._math_grade = value
```

此外，这种方法不通用。如果要在家庭作业和考试之外的其他类中重用此百分制验证，则需要一遍又一遍地编写 `@property` 样板代码和 `_check_grade` 方法。

在 Python 中更好的方法是使用 _descriptor_。_Descriptor protocol_ 定义了语言如何解释属性访问。Descriptor 类可以提供 `__get__` 和 `__set__` 方法，让你无需样板代码即可重用分数验证行为。为此，descriptor 比 mix-ins（参见 [Item 54](#ch07#ch07lev1sec7): “[Consider Composing Functionality with Mix-in Classes](#ch07#ch07lev1sec7)”）更好，因为它们允许在单个类中为许多不同的属性重用相同的逻辑。

这里定义了一个名为 `Exam` 的新类，其中类属性是 `Grade` 实例。`Grade` 类实现了 descriptor protocol：

```python
class Grade:
def __get__(self, instance, instance_type):
...

def __set__(self, instance, value):
...

class Exam:
# Class attributes
math_grade = Grade()
writing_grade = Grade()
science_grade = Grade()
```

在解释 `Grade` 类如何工作之前，理解 Python 在访问 `Exam` 实例上的描述符属性时会做什么很重要。赋值属性时：

```python
exam = Exam()
exam.writing_grade = 40
```

这被解释为：

```python
Exam.__dict__["writing_grade"].__set__(exam, 40)
```

检索属性时：

```python
exam.writing_grade
```

这被解释为：

```python
Exam.__dict__["writing_grade"].__get__(exam, Exam)
```

驱动此行为的是 `object` 的 `__getattribute__` 方法（参见 [Item 61](#ch08#ch08lev1sec4): “[Use \_\_getattr\_\_, \_\_getattribute\_\_, and \_\_setattr\_\_ for Lazy Attributes](#ch08#ch08lev1sec4)” 获取背景）。简而言之，当 `Exam` 实例没有名为 `writing_grade` 的属性时，Python 会回退到 `Exam` 类的属性。如果这个类属性是一个具有 `__get__` 和 `__set__` 方法的对象，Python 会假定你想要遵循 descriptor protocol。

了解此行为以及如何在 `Homework` 类中使用 `@property` 进行分数验证后，以下是实现 `Grade` descriptor 的一个合理的第一步尝试：

```python
class Grade:
def __init__(self):
self._value = 0

def __get__(self, instance, instance_type):
return self._value

def __set__(self, instance, value):
if not (0 <= value <= 100):
raise ValueError("Grade must be between 0 and 100")
self._value = value
```

不幸的是，这是错误的，并导致了错误的行为。访问单个 `Exam` 实例上的多个属性可以按预期工作：

```python
class Exam:
math_grade = Grade()
writing_grade = Grade()
science_grade = Grade()

first_exam = Exam()
first_exam.writing_grade = 82
first_exam.science_grade = 99
print("Writing", first_exam.writing_grade)
print("Science", first_exam.science_grade)
```

但是访问多个 `Exam` 实例上的这些属性会导致令人惊讶的行为：

```python
second_exam = Exam()
second_exam.writing_grade = 75
print(f"Second {second_exam.writing_grade} is right")
print(f"First  {first_exam.writing_grade} is wrong; "
f"should be 82")
```

问题在于，对于类属性 `writing_grade`，所有 `Exam` 实例共享一个 `Grade` 实例。此属性的 `Grade` 实例在程序生命周期中仅构造一次，即在 `Exam` 类首次定义时，而不是在每次创建 `Exam` 实例时。

为了解决这个问题，需要 `Grade` 类为每个唯一的 `Exam` 实例跟踪其值。可以通过将每个实例的状态保存在字典中来实现：

```python
class DictGrade:
def __init__(self):
self._values = {}

def __get__(self, instance, instance_type):
if instance is None:
return self
return self._values.get(instance, 0)

def __set__(self, instance, value):
if not (0 <= value <= 100):
raise ValueError("Grade must be between 0 and 100")
self._values[instance] = value
```

这个实现很简单并且效果很好，但仍然有一个陷阱：它会泄漏内存。`_values` 字典在程序生命周期中保存了传递给 `__set__` 的每个 `Exam` 实例的引用。这导致实例的引用计数永远不会变为零，阻止了垃圾回收器的清理（参见 [Item 115](#ch13#ch13lev1sec8): “[Use tracemalloc to Understand Memory Usage and Leaks](#ch13#ch13lev1sec8)” 了解如何检测此类问题）。

相反，应该依赖 Python 的 `__set_name__` 特殊方法来处理 descriptors（参见 [Item 64](#ch08#ch08lev1sec7): “[Annotate Class Attributes with \_\_set\_name\_\_](#ch08#ch08lev1sec7)” 获取背景）。此方法在类定义后对每个 descriptor 实例进行调用。关键是，分配给 descriptor 实例的类属性名称由 Python 提供。这允许计算一个字符串来用作每个对象的属性名称（在本例中，是受保护的字段，以 `"_"` 开头）：

```python
class NamedGrade:
def __set_name__(self, owner, name):
self.internal_name = "_" + name
```

可以使用 `setattr` 和 `getattr` 在对象上使用 `internal_name` 从 descriptor 中存储和检索相应的属性数据：

```python
def __get__(self, instance, instance_type):
if instance is None:
return self
return getattr(instance, self.internal_name)

def __set__(self, instance, value):
if not (0 <= value <= 100):
raise ValueError("Grade must be between 0 and 100")
setattr(instance, self.internal_name, value)
```

现在可以定义一个具有此改进 descriptor 的新类，并查看 descriptor 的属性数据如何驻留在对象的实例字典（`__dict__`）中：

```python
class NamedExam:
math_grade = NamedGrade()
writing_grade = NamedGrade()
science_grade = NamedGrade()

first_exam = NamedExam()
first_exam.math_grade = 78
first_exam.writing_grade = 89
first_exam.science_grade = 94
print(first_exam.__dict__)
```

与早期实现不同，这不会泄漏内存，因为当 `NamedExam` 对象被垃圾回收时，包括由 descriptors 分配的值在内的所有属性数据也将被释放。

#### Things to Remember

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 通过定义自己的 descriptor 类来重用 `@property` 方法的行为和验证。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `__set_name__` 结合 `setattr` 和 `getattr` 将 descriptor 所需的数据存储在对象实例字典中，以避免内存泄漏。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 不要陷入理解 `__getattribute__` 如何使用 descriptor protocol 来获取和设置属性的细节中。

### Item 61: Use `__getattr__`, `__getattribute__`, and `__setattr__` for Lazy Attributes

Python 的 `object` 基类提供了钩子，可以轻松编写用于粘合系统通用代码。例如，假设要将数据库中的记录表示为 Python 对象。假设数据库已在其他地方定义了其 schema。在大多数语言中，需要在代码中显式指定数据库 schema 如何映射到程序中的类和对象。然而，在 Python 中，可以在运行时通用地执行此对象关系映射，因此不需要样板代码。

这是如何实现的？普通的实例属性、`@property` 方法和 descriptors 都无法做到这一点，因为它们都需要预先定义。Python 通过 `__getattr__` 特殊方法实现此动态行为。如果类定义了 `__getattr__`，则每次找不到属性时都会调用该方法。这里，定义一个 `__getattr__` 钩子，它将属性插入对象的实例字典中以证明它已运行：

```python
class LazyRecord:
def __init__(self):
self.exists = 5

def __getattr__(self, name):
value = f"Value for {name}"
setattr(self, name, value)
return value
```

当访问缺失的对象属性 `foo` 时，例如，Python 调用上面的 `__getattr__` 方法，该方法会修改实例字典 `__dict__`：

```python
data = LazyRecord()
print("Before:", data.__dict__)
print("foo:   ", data.foo)
print("After: ", data.__dict__)
```

可以向 `LazyRecord` 添加日志记录以显示何时实际调用了 `__getattr__`。请注意，在此实现中，调用 `super().__getattr__()` 以使用 `__getattr__` 的超类实现来获取真实属性值并避免无限递归（参见 [Item 53](#ch07#ch07lev1sec6): “[Initialize Parent Classes with super](#ch07#ch07lev1sec6)” 获取背景）：

```python
class LoggingLazyRecord(LazyRecord):
def __getattr__(self, name):
print(
f"* Called __getattr__({name!r}), "
f"populating instance dictionary"
)
result = super().__getattr__(name)
print(f"* Returning {result!r}")
return result

data = LoggingLazyRecord()
print("exists:     ", data.exists)
print("First foo:  ", data.foo)
print("Second foo: ", data.foo)
```

`exists` 属性存在于实例字典中，因此 `__getattr__` 从未为其调用。`foo` 属性最初不在实例字典中，因此第一次调用 `__getattr__`。但是，对 `foo` 的 `__getattr__` 调用也执行了 `setattr`，它将 `foo` 填充到实例字典中。这就是为什么第二次访问 `foo` 时，它不会记录对 `__getattr__` 的调用。

此行为对于懒加载无模式数据等用例尤其有用。`__getattr__` 运行一次以执行加载属性的繁重工作；所有后续访问都检索现有结果。

现在设想还需要数据库系统中的事务。下次用户访问动态属性时，需要知道数据库中相应的记录是否仍然有效以及事务是否仍然打开。`__getattr__` 钩子不会在每次访问属性时调用，因为它将使用对象实例字典作为现有属性的快速路径。

为了支持此更高级的用例，Python 具有另一个 `object` 钩子，称为 `__getattribute__`。每次在对象上访问属性时都会调用此特殊方法，即使属性确实存在于属性字典中。这使得可以执行诸如检查每个属性访问上的全局事务状态之类的操作。需要注意的是，此类操作会产生显著的开销并对性能产生负面影响，但有时是值得的。这里，定义 `ValidatingRecord` 以记录每次调用 `__getattribute__`：

```python
class ValidatingRecord:
def __init__(self):
self.exists = 5

def __getattribute__(self, name):
print(f"* Called __getattribute__({name!r})")
try:
value = super().__getattribute__(name)
print(f"* Found {name!r}, returning {value!r}")
return value
except AttributeError:
value = f"Value for {name}"
print(f"* Setting {name!r} to {value!r}")
setattr(self, name, value)
return value

data = ValidatingRecord()
print("exists:     ", data.exists)
print("First foo:  ", data.foo)
print("Second foo: ", data.foo)
```

如果动态访问的属性不应存在，则可以引发 `AttributeError` 以对 `__getattr__` 和 `__getattribute__` 产生 Python 的标准缺失属性行为：

```python
class MissingPropertyRecord:
def __getattr__(self, name):
if name == "bad_name":
raise AttributeError(f"{name} is missing")
...

data = MissingPropertyRecord()
try:
data.bad_name
except AttributeError as e:
print(e)
```

实现通用功能的 Python 代码通常依赖于 `hasattr` 内置函数来确定属性何时存在，以及 `getattr` 内置函数来检索属性值。这些函数在调用 `__getattr__` 之前也会在实例字典中查找属性名称：

```python
data = LoggingLazyRecord()  # Implements __getattr__
print("Before:         ", data.__dict__)
print("Has first foo:  ", hasattr(data, "foo"))
print("After:          ", data.__dict__)
print("Has second foo: ", hasattr(data, "foo"))
```

在上面的示例中，`__getattr__` 只调用一次（对于第一个 `hasattr` 调用）。相比之下，实现 `__getattribute__` 的类在每次使用 `hasattr` 或 `getattr` 与实例时都会调用该方法：

```python
data = ValidatingRecord()  # Implements __getattribute__
print("Has first foo:  ", hasattr(data, "foo"))
print("Has second foo: ", hasattr(data, "foo"))
```

现在，假设要将值分配给 Python 对象时，将数据懒惰地推回数据库。可以使用 `__setattr__` 来实现这一点，这是一个类似的 `object` 钩子，允许拦截任意属性赋值。与使用 `__getattr__` 和 `__getattribute__` 检索属性不同，不需要两个单独的方法。每次在实例上分配属性时（无论是直接还是通过 `setattr` 内置函数），都会调用 `__setattr__` 方法：

```python
class SavingRecord:
def __setattr__(self, name, value):
# Save some data for the record
...
super().__setattr__(name, value)
```

这里，定义了一个 `SavingRecord` 的日志记录子类。其 `__setattr__` 方法在每次属性赋值时都会被调用：

```python
class LoggingSavingRecord(SavingRecord):
def __setattr__(self, name, value):
print(f"* Called __setattr__({name!r}, {value!r})")
super().__setattr__(name, value)

data = LoggingSavingRecord()
print("Before: ", data.__dict__)
data.foo = 5
print("After:  ", data.__dict__)
data.foo = 7
print("Finally:", data.__dict__)
```

`__getattribute__` 和 `__setattr__` 的问题在于它们会在每次访问对象的属性时被调用——即使你可能不希望这样。例如，假设对象上的属性访问实际上应该查找关联字典中的键：

```python
class BrokenDictionaryRecord:
def __init__(self, data):
self._data = data

def __getattribute__(self, name):
print(f"* Called __getattribute__({name!r})")
return self._data[name]
```

这需要在 `__getattribute__` 方法中访问 `self._data`。但是，如果实际尝试这样做，Python 将会递归直到达到堆栈限制，然后程序将崩溃：

```python
data = BrokenDictionaryRecord({"foo": 3})
try:
data.foo
except RecursionError as e:
print(e)
```

问题在于 `__getattribute__` 访问 `self._data`，这会导致 `__getattribute__` 再次运行，再次访问 `self._data`，依此类推。解决方案是使用 `super().__getattribute__` 方法从实例属性字典中获取值；这可以避免意外递归：

```python
class DictionaryRecord:
def __init__(self, data):
self._data = data

def __getattribute__(self, name):
print(f"* Called __getattribute__({name!r})")
data_dict = super().__getattribute__("_data")
return data_dict[name]

data = DictionaryRecord({"foo": 3})
print("foo: ", data.foo)
```

`__setattr__` 方法对对象属性的修改也需要使用 `super().__setattr__`。

#### Things to Remember

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `__getattr__` 和 `__setattr__` 来懒加载和保存对象的属性。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 理解 `__getattr__` 仅在访问缺失属性时调用，而 `__getattribute__` 在每次访问任何属性时都会调用。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在 `__getattribute__` 和 `__setattr__` 方法实现中调用 `super().__getattribute__` 和 `super().__getattr__` 来访问对象属性，以避免无限递归。

### Item 62: Validate Subclasses with `__init_subclass__`

Metaclasses 最简单的应用之一是验证类是否已正确定义。在构建复杂的类层次结构时，可能需要强制执行样式、要求覆盖方法或在类属性之间建立严格的关系。Metaclasses 通过提供一种可靠的方式来在每次定义新子类时运行验证代码，从而实现这些用例。

通常，类的验证代码在运行时构建类类型的对象时在 `__init__` 方法中运行（参见 [Item 58](#ch08#ch08lev1sec1): “[Use Plain Attributes Instead of Setter and Getter Methods](#ch08#ch08lev1sec1)” 获取示例）。使用 Metaclasses 进行验证可以更早地引发错误，例如在包含该类的模块首次导入时。

在介绍如何定义用于验证子类的 metaclass 之前，理解 metaclass 对标准对象的作用很重要。Metaclass 通过继承 `type` 来定义。类通过其继承参数列表中的 `metaclass` 关键字参数指示其 metaclass。在典型情况下，当发生任何关联的 `class` 语句时，metaclass 的 `__new__` 方法就会被调用，并传入 `class` 语句的内容。这里，使用一个基本的 metaclass 在类型实际构造之前检查类的 `class` 信息：

```python
class Meta(type):
def __new__(meta, name, bases, class_dict):
print(f"* Running {meta}.__new__ for {name}")
print("Bases:", bases)
print(class_dict)
return type.__new__(meta, name, bases, class_dict)

class MyClass(metaclass=Meta):
stuff = 123

def foo(self):
pass

class MySubclass(MyClass):
other = 567

def bar(self):
pass
```

Metaclass 可以访问类的名称、它继承的父类（`bases`）以及在类体中定义的所有类属性。所有类都继承自 `object`，因此它没有明确列在基类元组中。

可以在 `Meta.__new__` 方法中添加功能，以便在定义关联的子类之前验证其所有参数。例如，假设要表示任何类型的多边形。可以通过定义一个特殊的验证 metaclass 并将其用于多边形类层次结构的基类来实现。请注意，不要将相同的验证应用于基类：

```python
class ValidatePolygon(type):
def __new__(meta, name, bases, class_dict):
# Only validate subclasses of the Polygon class
if bases:
if class_dict["sides"] < 3:
raise ValueError("Polygons need 3+ sides")
return type.__new__(meta, name, bases, class_dict)

class Polygon(metaclass=ValidatePolygon):
sides = None  # Must be specified by subclasses

@classmethod
def interior_angles(cls):
return (cls.sides - 2) * 180

class Triangle(Polygon):
sides = 3

class Rectangle(Polygon):
sides = 4

class Nonagon(Polygon):
sides = 9

assert Triangle.interior_angles() == 180
assert Rectangle.interior_angles() == 360
assert Nonagon.interior_angles() == 1260
```

如果尝试定义一个边数少于三个的多边形，验证逻辑将导致 `class` 语句在 `class` 语句体之后立即失败。这意味着程序甚至无法在定义此类时开始运行（除非它在动态导入的模块中定义；参见 [Item 98](#ch11#ch11lev1sec7): “[Lazy-Load Modules with Dynamic Imports to Reduce Startup Time](#ch11#ch11lev1sec7)” 了解这如何发生）：

```python
print("Before class")

class Line(Polygon):
print("Before sides")
sides = 2
print("After sides")

print("After class")
```

为了让 Python 完成如此基本任务，这似乎需要大量的机制。幸运的是，Python 3.6 引入了简化的语法——`__init_subclass__` 特殊类方法——来实现相同的行为并完全避免 metaclasses。这里，使用此机制提供与之前相同的验证级别：

```python
class BetterPolygon:
sides = None  # Must be specified by subclasses

def __init_subclass__(cls):
super().__init_subclass__()
if cls.sides < 3:
raise ValueError("Polygons need 3+ sides")

@classmethod
def interior_angles(cls):
return (cls.sides - 2) * 180

class Hexagon(BetterPolygon):
sides = 6

assert Hexagon.interior_angles() == 720
```

代码现在短了很多，并且完全没有了 `ValidatePolygon` metaclass。它也更容易理解，因为可以在 `__init_subclass__` 中直接访问 `cls` 实例上的 `sides` 属性，而不是必须使用 `class_dict["sides"]` 进入类的字典。如果定义了一个无效的 `BetterPolygon` 子类，将引发与之前相同的异常：

```python
print("Before class")

class Point(BetterPolygon):
sides = 1

print("After class")
```

`__init_subclass__` 的另一个问题是，你只能为每个类定义指定一个 metaclass。这里，定义第二个 metaclass，希望用于验证区域的填充颜色（不一定是多边形）：

```python
class ValidateFilled(type):
def __new__(meta, name, bases, class_dict):
# Only validate subclasses of the Filled class
if bases:
if class_dict["color"] not in ("red", "green"):
raise ValueError("Fill color must be supported")
return type.__new__(meta, name, bases, class_dict)

class Filled(metaclass=ValidateFilled):
color = None  # Must be specified by subclasses
```

当尝试同时使用 `Polygon` metaclass 和 `Filled` metaclass 时，会收到一条含糊的错误消息：

```python
class RedPentagon(Filled, Polygon):
color = "blue"
sides = 5
```

可以通过创建复杂的 metaclass `type` 定义层次结构来解决此问题，以分层验证：

```python
class ValidatePolygon(type):
def __new__(meta, name, bases, class_dict):
# Only validate non-root classes
if not class_dict.get("is_root"):
if class_dict["sides"] < 3:
raise ValueError("Polygons need 3+ sides")
return type.__new__(meta, name, bases, class_dict)

class Polygon(metaclass=ValidatePolygon):
is_root = True
sides = None  # Must be specified by subclasses

class ValidateFilledPolygon(ValidatePolygon):
def __new__(meta, name, bases, class_dict):
# Only validate non-root classes
if not class_dict.get("is_root"):
if class_dict["color"] not in ("red", "green"):
raise ValueError("Fill color must be supported")
return super().__new__(meta, name, bases, class_dict)

class FilledPolygon(Polygon, metaclass=ValidateFilledPolygon):
is_root = True
color = None  # Must be specified by subclasses
```

这要求每个 `FilledPolygon` 实例都是 `Polygon` 实例：

```python
class GreenPentagon(FilledPolygon):
color = "green"
sides = 5

greenie = GreenPentagon()
assert isinstance(greenie, Polygon)
```

颜色验证有效：

```python
class OrangePentagon(FilledPolygon):
color = "orange"
sides = 5
```

边数验证也有效：

```python
class RedLine(FilledPolygon):
color = "red"
sides = 2
```

但是，这种方法破坏了可组合性，而这通常是此类类验证的目的（类似于 mix-ins；参见 [Item 54](#ch07#ch07lev1sec7): “[Consider Composing Functionality with Mix-in Classes](#ch07#ch07lev1sec7)”）。如果要在另一个类层次结构中应用 `ValidateFilledPolygon` 的颜色验证逻辑，则必须再次复制所有逻辑，这会减少代码重用并增加样板代码。

`__init_subclass__` 特殊类方法也可用于解决此问题。它可以由类层次结构的多个级别定义，只要 `super` 内置函数用于调用任何父类或同级 `__init_subclass__` 定义即可。这里，定义一个类来表示区域的填充颜色，该颜色可以与之前的 `BetterPolygon` 类组合：

```python
class Filled:
color = None  # Must be specified by subclasses

def __init_subclass__(cls):
super().__init_subclass__()
if cls.color not in ("red", "green", "blue"):
raise ValueError("Fills need a valid color")
```

可以继承这两个类来定义一个新类。两个类都调用 `super().__init_subclass__()`，从而在创建子类时运行其相应的验证逻辑：

```python
class RedTriangle(Filled, BetterPolygon):
color = "red"
sides = 3

ruddy = RedTriangle()
assert isinstance(ruddy, Filled)
assert isinstance(ruddy, BetterPolygon)
```

如果边数指定不正确，将收到验证错误：

```python
print("Before class")

class BlueLine(Filled, BetterPolygon):
color = "blue"
sides = 2

print("After class")
```

如果颜色指定不正确，也将收到验证错误：

```python
print("Before class")

class BeigeSquare(Filled, BetterPolygon):
color = "beige"
sides = 4

print("After class")
```

甚至可以在复杂的场景中使用 `__init_subclass__`，例如多重继承和菱形继承（参见 [Item 53](#ch07#ch07lev1sec6): “[Initialize Parent Classes with super](#ch07#ch07lev1sec6)” 获取背景）。这里，定义一个基本的菱形层次结构来演示这一点：

```python
class Top:
def __init_subclass__(cls):
super().__init_subclass__()
print(f"Top for {cls}")

class Left(Top):
def __init_subclass__(cls):
super().__init_subclass__()
print(f"Left for {cls}")

class Right(Top):
def __init_subclass__(cls):
super().__init_subclass__()
print(f"Right for {cls}")

class Bottom(Left, Right):
def __init_subclass__(cls):
super().__init_subclass__()
print(f"Bottom for {cls}")
```

如预期的那样，即使对于 `Bottom` 类通过其 `Left` 和 `Right` 父类存在两条路径，`Top.__init_subclass__` 也只为每个类调用一次。

#### Things to Remember

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Metaclasses 的 `__new__` 方法在 `class` 语句的整个主体处理之后运行。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Metaclasses 可用于在类定义后但在类创建之前检查或修改类，但它们通常比你需要的更重量级。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `__init_subclass__` 来确保子类在定义时（在构造其类型的对象之前）是格式良好的。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 确保从类的 `__init_subclass__` 定义中调用 `super().__init_subclass__()`，以实现类和多重继承中可组合的验证。

### Item 63: Register Class Existence with `__init_subclass__`

Metaclasses 的另一个常见用途是自动在程序中注册类型（参见 [Item 62](#ch08#ch08lev1sec5): “[Validate Subclasses with \_\_init\_subclass\_\_](#ch08#ch08lev1sec5)” 获取背景）。注册对于反向查找很有用，你需要将标识符映射回相应的类。

例如，假设要使用 JSON 实现自己的 Python 对象序列化表示。需要一种方法将对象转换为 JSON 字符串。这里，通过定义一个记录构造函数参数并将其转换为 JSON 字典的基类来通用地实现这一点（参见 [Item 54](#ch07#ch07lev1sec7): “[Consider Composing Functionality with Mix-in Classes](#ch07#ch07lev1sec7)” 获取另一种方法）：

```python
import json

class Serializable:
def __init__(self, *args):
self.args = args

def serialize(self):
return json.dumps({"args": self.args})
```

此类易于将简单数据结构序列化为字符串，例如：

```python
class Point2D(Serializable):
def __init__(self, x, y):
super().__init__(x, y)
self.x = x
self.y = y

def __repr__(self):
return f"Point2D({self.x}, {self.y})"

point = Point2D(5, 3)
print("Object:    ", point)
print("Serialized:", point.serialize())
```

现在需要反序列化此 JSON 字符串并构造它表示的 `Point2D` 对象。这里定义另一个类，它可以从其 `Serializable` 父类反序列化数据（参见 [Item 52](#ch07#ch07lev1sec5): “[Use @classmethod Polymorphism to Construct Objects Generically](#ch07#ch07lev1sec5)” 获取背景）：

```python
class Deserializable(Serializable):
@classmethod
def deserialize(cls, json_data):
params = json.loads(json_data)
return cls(*params["args"])
```

使用 `Deserializable` 作为父类可以轻松地以通用方式序列化和反序列化简单对象：

```python
class BetterPoint2D(Deserializable):
def __init__(self, x, y):
super().__init__(x, y)
self.x = x
self.y = y

def __repr__(self):
return f"Point2D({self.x}, {self.y})"

before = BetterPoint2D(5, 3)
print("Before:    ", before)
data = before.serialize()
print("Serialized:", data)
after = BetterPoint2D.deserialize(data)
print("After:     ", after)
```

此方法的问题在于，只有当你提前知道序列化数据的预期类型时（例如 `Point2D`、`BetterPoint2D`），它才有效。理想情况下，会有大量类序列化为 JSON，并且有一个通用函数可以将它们中的任何一个反序列化回相应的 Python `object`（参见 [Item 50](#ch07#ch07lev1sec3): “[Consider functools.singledispatch for Functional-Style Programming Instead of Object-Oriented Polymorphism](#ch07#ch07lev1sec3)” 获取类似示例）。

为此，可以在 JSON 数据中包含序列化对象的类名：

```python
class BetterSerializable:
def __init__(self, *args):
self.args = args

def serialize(self):
return json.dumps(
{
"class": self.__class__.__name__,
"args": self.args,
}
)

def __repr__(self):
name = self.__class__.__name__
args_str = ", ".join(str(x) for x in self.args)
return f"{name}({args_str})"
```

然后可以维护一个从类名到这些对象构造函数的映射。通用的 `deserialize` 函数适用于传递给 `register_class` 的任何类：

```python
REGISTRY = {}

def register_class(target_class):
REGISTRY[target_class.__name__] = target_class

def deserialize(data):
params = json.loads(data)
name = params["class"]
target_class = REGISTRY[name]
return target_class(*params["args"])
```

为了确保 `deserialize` 始终正常工作，必须为将来可能要反序列化的每个类调用 `register_class`：

```python
class EvenBetterPoint2D(BetterSerializable):
def __init__(self, x, y):
super().__init__(x, y)
self.x = x
self.y = y

register_class(EvenBetterPoint2D)
```

现在可以反序列化任意 JSON 字符串，而无需知道它包含哪个类：

```python
before = EvenBetterPoint2D(5, 3)
print("Before:    ", before)
data = before.serialize()
print("Serialized:", data)
after = deserialize(data)
print("After:     ", after)
```

此方法的问题在于，可能会忘记调用 `register_class`：

```python
class Point3D(BetterSerializable):
def __init__(self, x, y, z):
super().__init__(x, y, z)
self.x = x
self.y = y
self.z = z

# Forgot to call register_class! Whoops!
```

当尝试反序列化忘记注册的类的对象时，代码会在运行时中断：

```python
point = Point3D(5, 9, -4)
data = point.serialize()
try:
deserialize(data)
except KeyError as e:
print(e)
```

即使选择了继承 `BetterSerializable`，如果忘记在 `class` 语句体之后调用 `register_class`，实际上也无法获得其所有功能。此方法容易出错，对于初学者来说尤其难以调试。同样的遗漏也可能发生在 _class decorators_ 上（参见 [Item 66](#ch08#ch08lev1sec9): “[Prefer Class Decorators over Metaclasses for Composable Class Extensions](#ch08#ch08lev1sec9)” 了解何时适合使用它们）。

如果能以某种方式利用程序员的意图来使用 `BetterSerializable` 并确保在所有情况下都调用 `register_class` 怎么办？Metaclasses 通过在子类定义时拦截 `class` 语句来实现这一点。这里使用 metaclass 和相应的超类来在类语句结束后立即注册任何子类：

```python
class Meta(type):
def __new__(meta, name, bases, class_dict):
cls = type.__new__(meta, name, bases, class_dict)
register_class(cls)
return cls

class RegisteredSerializable(BetterSerializable, metaclass=Meta):
pass
```

定义 `RegisteredSerializable` 的子类时，可以确信 `register_class` 调用会发生，并且 `deserialize` 将始终按预期工作：

```python
class Vector3D(RegisteredSerializable):
def __init__(self, x, y, z):
super().__init__(x, y, z)
self.x, self.y, self.z = x, y, z

before = Vector3D(10, -7, 3)
print("Before:    ", before)
data = before.serialize()
print("Serialized:", data)
print("After:     ", deserialize(data))
```

更好的方法是使用 `__init_subclass__` 特殊类方法。此简化语法（在 Python 3.6 中引入）减少了在定义类时应用自定义逻辑的视觉噪音。它也更容易被初学者理解，他们可能会对 metaclass 语法的复杂性感到困惑。这里实现了一个新的超类来自动调用 `register_class`，以及一个使用它的子类：

```python
class BetterRegisteredSerializable(BetterSerializable):
def __init_subclass__(cls):
super().__init_subclass__()
register_class(cls)

class Vector1D(BetterRegisteredSerializable):
def __init__(self, magnitude):
super().__init__(magnitude)
self.magnitude = magnitude
```

此新类的序列化和反序列化按预期工作：

```python
before = Vector1D(6)
print("Before:    ", before)
data = before.serialize()
print("Serialized:", data)
print("After:     ", deserialize(data))
```

通过使用 `__init_subclass__`（或 Metaclasses）进行类注册，可以确保只要继承树正确，就不会错过注册类。这对于序列化非常有效，如所示，也适用于数据库对象关系映射（ORM）、可扩展插件系统和回调钩子。

#### Things to Remember

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 类注册是构建模块化 Python 程序的有用模式。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Metaclasses 允许你在每次基类在程序中被子类化时自动运行注册代码。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 Metaclasses 进行类注册有助于避免错误，确保你永远不会错过注册调用。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 优先使用 `__init_subclass__` 而不是标准的 metaclass 机制，因为它更清晰，对初学者更容易理解。

### Item 64: Annotate Class Attributes with `__set_name__`

Metaclasses 启用的另一个有用功能（参见 [Item 62](#ch08#ch08lev1sec5): “[Validate Subclasses with \_\_init\_subclass\_\_](#ch08#ch08lev1sec5)” 获取背景）是在类定义后但在类实际使用之前修改或注释属性的能力。此方法通常与 descriptors（参见 [Item 60](#ch08#ch08lev1sec3): “[Use Descriptors for Reusable @property Methods](#ch08#ch08lev1sec3)” 获取详细信息）结合使用，为这些属性提供更多关于它们在包含类中如何使用的内省信息。

例如，假设要定义一个表示客户数据库中一行的新类。希望类有一个与数据库表中的每个列对应的属性。这里定义一个 descriptor 类来连接属性和列名：

```python
class Field:
def __init__(self, column_name):
self.column_name = column_name
self.internal_name = "_" + self.column_name
```

可以使用列名通过使用 `setattr` 内置函数将所有每个实例状态直接保存在实例字典中作为受保护字段，稍后可以使用 `getattr` 加载状态（参见 [Item 61](#ch08#ch08lev1sec4): “[Use \_\_getattr\_\_, \_\_getattribute\_\_, and \_\_setattr\_\_ for Lazy Attributes](#ch08#ch08lev1sec4)” 获取背景）：

```python
def __get__(self, instance, instance_type):
if instance is None:
return self
return getattr(instance, self.internal_name, "")

def __set__(self, instance, value):
setattr(instance, self.internal_name, value)
```

定义表示行的类需要为每个 descriptor 属性提供数据库表的列名：

```python
class Customer:
# Class attributes
first_name = Field("first_name")
last_name = Field("last_name")
prefix = Field("prefix")
suffix = Field("suffix")
```

使用行类很简单。这里，`Field` descriptors 按预期修改实例字典 `__dict__`：

```python
cust = Customer()
print(f"Before: {cust.first_name!r} {cust.__dict__}")
cust.first_name = "Euclid"
print(f"After:  {cust.first_name!r} {cust.__dict__}")
```

但是，此类的代码定义似乎是多余的。已经在左侧声明了字段的名称（`field_name = `）。为什么还要在右侧的 `Field` 构造函数（`Field("first_name")`）中传递包含相同信息的字符串？

```python
class Customer:
# Left side is redundant with right side
first_name = Field("first_name")
...
```

问题在于 `Customer` 类定义的求值顺序与从左到右的读取顺序相反。首先，调用 `Field` 构造函数 `Field("first_name")`。然后，其返回值被分配给 `Customer.first_name` 类属性。`Field` 实例无法提前知道它将被分配给哪个类属性。

为了消除这种冗余，可以使用 metaclass。Metaclass 允许直接挂钩 `class` 语句，并在类体完成后立即采取行动。在这种情况下，可以使用 metaclass 自动分配 `Field.column_name` 和 `Field.internal_name`，而不是手动指定字段名多次：

```python
class Meta(type):
def __new__(meta, name, bases, class_dict):
for key, value in class_dict.items():
if isinstance(value, Field):
value.column_name = key
value.internal_name = "_" + key
cls = type.__new__(meta, name, bases, class_dict)
return cls
```

这里定义了一个使用 metaclass 的基类。所有表示数据库行的类都应继承自此类，以确保它们使用 metaclass：

```python
class DatabaseRow(metaclass=Meta):
pass
```

为了使用 metaclass，字段 descriptor 大致保持不变。唯一的区别是它不再需要将任何参数传递给其构造函数。相反，其属性由上面的 `Meta.__new__` 方法设置：

```python
class Field:
def __init__(self):
# These will be assigned by the metaclass.
self.column_name = None
self.internal_name = None

def __get__(self, instance, instance_type):
if instance is None:
return self
return getattr(instance, self.internal_name, "")

def __set__(self, instance, value):
setattr(instance, self.internal_name, value)
```

使用 metaclass、新的 `DatabaseRow` 基类和新的 `Field` descriptor 时，数据库行的类定义不再存在之前的冗余：

```python
class BetterCustomer(DatabaseRow):
first_name = Field()
last_name = Field()
prefix = Field()
suffix = Field()
```

新类的行为与旧类的行为相同：

```python
cust = BetterCustomer()
print(f"Before: {cust.first_name!r} {cust.__dict__}")
cust.first_name = "Euler"
print(f"After:  {cust.first_name!r} {cust.__dict__}")
```

这种方法的麻烦在于，除非也继承自 `DatabaseRow`，否则无法将 `Field` 类用于属性。如果以某种方式忘记继承 `DatabaseRow`，或者由于类层次结构的其他结构性要求而不希望这样做，代码将中断：

```python
class BrokenCustomer:  # Missing inheritance
first_name = Field()
last_name = Field()
prefix = Field()
suffix = Field()

cust = BrokenCustomer()
cust.first_name = "Mersenne"
```

解决此问题的方法是使用 descriptors 的 `__set_name__` 特殊方法。此方法（在 Python 3.6 中引入）在类定义时对每个 descriptor 实例进行调用。它接收包含 descriptor 实例的拥有类以及分配给 descriptor 实例的属性名称作为参数。这里避免定义 metaclass，并将上面 `Meta.__new__` 方法的功能移到 `__set_name__` 方法中：

```python
class Field:
def __init__(self):
self.column_name = None
self.internal_name = None

def __set_name__(self, owner, column_name):
# Called on class creation for each descriptor
self.column_name = column_name
self.internal_name = "_" + column_name

def __get__(self, instance, instance_type):
if instance is None:
return self
return getattr(instance, self.internal_name, "")

def __set__(self, instance, value):
setattr(instance, self.internal_name, value)
```

现在，无需继承特定父类或使用 metaclass，即可获得 `Field` descriptor 的好处：

```python
class FixedCustomer:  # No parent class
first_name = Field()
last_name = Field()
prefix = Field()
suffix = Field()

cust = FixedCustomer()
print(f"Before: {cust.first_name!r} {cust.__dict__}")
cust.first_name = "Mersenne"
print(f"After:  {cust.first_name!r} {cust.__dict__}")
```

#### Things to Remember

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Metaclass 允许你在类完全定义之前修改类的属性。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Descriptors 和 Metaclasses 是声明性行为和运行时内省的强大组合。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在 descriptor 类上定义 `__set_name__`，使其能够考虑到其周围的类及其属性名称。

### Item 65: Consider Class Body Definition Order to Establish Relationships Between Attributes

Python 程序中许多类的目的都是表示在别处创建和维护的外部数据。例如，假设有一个包含一系列货运交付的 CSV（逗号分隔值）文件，其中每行包括目的地城市、旅行方式和货物重量。这里，使用 `csv` 内置模块读取此数据：

```python
import csv

# Assuming packages.csv exists with data like:
# Sydney,truck,25
# Melbourne,boat,6
# Brisbane,plane,12
# Perth,road train,90
# Adelaide,truck,17

# with open("packages.csv") as f:
#     for row in csv.reader(f):
#         print(row)
```

可以定义一个新类来存储此数据，以及一个给定 CSV 行的辅助函数来创建对象（参见 [Item 52](#ch07#ch07lev1sec5): “[Use @classmethod Polymorphism to Construct Objects Generically](#ch07#ch07lev1sec5)” 获取背景）：

```python
class Delivery:
def __init__(self, destination, method, weight):
self.destination = destination
self.method = method
self.weight = weight

@classmethod
def from_row(cls, row):
return cls(row[0], row[1], row[2])
```

当提供值列表（每个列一个）时，这按预期工作：

```python
row1 = ["Sydney", "truck", "25"]
obj1 = Delivery.from_row(row1)
print(obj1.__dict__)
```

如果 CSV 文件中添加了更多列或重新排序了列，只需少量工作，就可以对 `__init__` 和 `from_row` 方法进行相应调整，以保持与文件格式的兼容性。现在想象一下，有许多种 CSV 文件需要处理，每种文件都有不同的列数和单元格值类型。如果能够更有效地为每个 CSV 文件定义一个新类，而无需大量样板代码，那会更好。

这里尝试通过实现一个基类来完成此任务，该基类使用 `fields` 类属性将 CSV 列（按其在文件中的顺序）映射到对象属性名称（参见 [Item 64](#ch08#ch08lev1sec7): “[Annotate Class Attributes with \_\_set\_name\_\_](#ch08#ch08lev1sec7)” 获取另一种方法）：

```python
class RowMapper:
fields = ()  # Must be in CSV column order

def __init__(self, **kwargs):
for key, value in kwargs.items():
if key not in type(self).fields:
raise TypeError(f"Invalid field: {key}")
setattr(self, key, value)

@classmethod
def from_row(cls, row):
if len(row) != len(cls.fields):
raise ValueError("Wrong number of fields")
kwargs = dict(pair for pair in zip(cls.fields, row))
return cls(**kwargs)
```

现在可以为货运 CSV 文件格式创建具体的子类：

```python
class DeliveryMapper(RowMapper):
fields = ("destination", "method", "weight")

row1 = ["Sydney", "truck", "25"]
obj2 = DeliveryMapper.from_row(row1)
assert obj2.destination == "Sydney"
assert obj2.method == "truck"
assert obj2.weight == "25"
```

如果需要支持另一种 CSV 格式（例如，用于移动式货车物流），可以通过提供列名快速创建另一个子类：

```python
class MovingMapper(RowMapper):
fields = ("source", "destination", "square_feet")
```

虽然这可行，但它不 Pythonic。属性使用字符串而不是变量名来指定，这使得代码难以阅读并使工具混淆（参见 [Item 124](#ch14#ch14lev1sec9): “[Consider Static Analysis via typing to Obviate Bugs](#ch14#ch14lev1sec9)” 和 [Item 3](#ch01#ch01lev1sec3): “[Never Expect Python to Detect Errors at Compile Time](#ch01#ch01lev1sec3)”）。更重要的是，`fields` 元组感觉与类体重复：它是嵌套在属性列表中的属性列表。

更好的方法是能够将 CSV 列的名称放在类体中，如下所示：

```python
class BetterMovingMapper:
source = ...
destination = ...
square_feet = ...
```

事实证明，这可以通过结合 Python 的三个特性来实现（参见 [Item 51](#ch07#ch07lev1sec4): “[Prefer dataclasses for Defining Lightweight Classes](#ch07#ch07lev1sec4)” 获取另一种方法）。第一个特性是 `__init_subclass__` 特殊类方法，它允许在子类定义时运行代码（参见 [Item 62](#ch08#ch08lev1sec5): “[Validate Subclasses with \_\_init\_subclass\_\_](#ch08#ch08lev1sec5)”）。第二个特性是类属性如何使用类对象的 `__dict__` 实例字典在运行时检查（参见 [Item 54](#ch07#ch07lev1sec7): “[Consider Composing Functionality with Mix-in Classes](#ch07#ch07lev1sec7)”）。第三个特性是字典如何保留键/值对的插入顺序（参见 [Item 25](#ch04#ch04lev1sec1): “[Be Cautious when Relying on Dictionary Insertion Ordering](#ch04#ch04lev1sec1)”）。

这里创建了一个类，该类查找分配给 `...` 的子属性，并将它们的名称存储在 `RowMapper` 父类的 `fields` 类属性中：

```python
class BetterRowMapper(RowMapper):
def __init_subclass__(cls):
fields = []
for key, value in cls.__dict__.items():
if value is Ellipsis:
fields.append(key)
cls.fields = tuple(fields)
```

现在可以声明一个具体的类，就像以前一样，但使用类体和省略号来指示 CSV 列：

```python
class BetterDeliveryMapper(BetterRowMapper):
destination = ...
method = ...
weight = ...

obj3 = BetterDeliveryMapper.from_row(row1)
assert obj3.destination == "Sydney"
assert obj3.method == "truck"
assert obj3.weight == "25"
```

如果 CSV 文件中的列顺序发生变化，只需更改属性定义顺序即可进行补偿。例如，这里将 `destination` 字段移到最后：

```python
class ReorderedDeliveryMapper(BetterRowMapper):
method = ...
weight = ...
destination = ...  # Moved

row4 = ["road train", "90", "Perth"]  # Different order
obj4 = ReorderedDeliveryMapper.from_row(row4)
print(obj4.__dict__)
```

在实际程序中，将使用 descriptor 类而不是省略号来声明字段，以实现属性验证和数据转换等用例（参见 [Item 60](#ch08#ch08lev1sec3): “[Use Descriptors for Reusable @property Methods](#ch08#ch08lev1sec3)” 获取背景）。例如，假设希望将 `weight` 列解析为浮点数而不是保留为字符串。

这里实现了一个 descriptor 类，该类拦截属性访问并根据需要转换分配的值：

```python
class Field:
def __init__(self):
self.internal_name = None

def __set_name__(self, owner, column_name):
self.internal_name = "_" + column_name

def __get__(self, instance, instance_type):
if instance is None:
return self
return getattr(instance, self.internal_name, "")

def __set__(self, instance, value):
adjusted_value = self.convert(value)
setattr(instance, self.internal_name, adjusted_value)

def convert(self, value):
raise NotImplementedError
```

可以实现两个具体的 `Field` 子类——一个用于字符串，另一个用于浮点数：

```python
class StringField(Field):
def convert(self, value):
if not isinstance(value, str):
raise ValueError
return value

class FloatField(Field):
def convert(self, value):
return float(value)
```

另一个表示 CSV 文件的基类可以查找 `Field` 实例而不是 `Ellipsis` 实例来发现有序的 CSV 列并相应地填充 `fields` 类属性：

```python
class DescriptorRowMapper(RowMapper):
def __init_subclass__(cls):
fields = []
for key, value in cls.__dict__.items():
if isinstance(value, Field):  # Changed
fields.append(key)
cls.fields = tuple(fields)
```

现在可以声明一个特定于 CSV 格式的具体子类，并且 `weight` 字段将被转换为浮点数，如预期的那样：

```python
class ConvertingDeliveryMapper(DescriptorRowMapper):
destination = StringField()
method = StringField()
weight = FloatField()

obj5 = ConvertingDeliveryMapper.from_row(row1)
assert obj5.destination == "Sydney"
assert obj5.method == "truck"
assert obj5.weight == 25.0  # Number, not string
```

检查类属性也可以用于发现方法。在与上述 CSV 用例完全不同的示例中，假设要创建一个描述需要按定义顺序运行的方法的顺序工作流的类：

```python
class HypotheticalWorkflow:
def start_engine(self):
...

def release_brake(self):
...

def run(self):
# Runs `start_engine` then `release_brake`
...
```

可以通过首先创建一个简单的函数装饰器来实现此目的（参见 [Item 38](#ch05#ch05lev1sec9): “[Define Function Decorators with functools.wraps](#ch05#ch05lev1sec9)”），该装饰器指示哪些方法应被视为工作流的一部分：

```python
def step(func):
func._is_step = True
return func
```

新的基类然后可以查找具有 `_is_step` 属性的、可调用的类属性（参见 [Item 48](#ch07#ch07lev1sec1): “[Accept Functions Instead of Classes for Simple Interfaces](#ch07#ch07lev1sec1)” 获取背景），以发现哪些方法应包含在工作流中以及它们应调用的顺序：

```python
class Workflow:
def __init_subclass__(cls):
steps = []
for key, value in cls.__dict__.items():
if callable(value) and hasattr(value, "_is_step"):
steps.append(key)
cls.steps = tuple(steps)

def run(self):
for step_name in type(self).steps:
func = getattr(self, step_name)
func()
```

`run` 方法只需要迭代步骤列表并按保存的顺序调用方法。不需要其他样板代码。

将它们放在一起，这里定义了一个启动汽车的简单工作流，其中包括一个应被基类忽略的辅助方法：

```python
class MyWorkflow(Workflow):
@step
def start_engine(self):
print("Engine is on!")
...

def my_helper_function(self):
raise RuntimeError("Should not be called")

@step
def release_brake(self):
print("Brake is off!")
...

workflow = MyWorkflow()
workflow.run()
```

工作流成功运行，并且不调用坏方法：

```python
>>>
Engine is on!
Brake is off!
```

#### Things to Remember

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 可以通过检查类对象的 `__dict__` 实例字典来检查类体中定义的属性和方法。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 类体的定义顺序在类对象的 `__dict__` 中保留，使代码能够考虑类属性和方法的相对位置。这对于将对象字段映射到 CSV 列索引等用例特别有用。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Descriptors 和方法装饰器可用于进一步增强使用类体定义顺序来控制程序行为的能力。

### Item 66: Prefer Class Decorators over Metaclasses for Composable Class Extensions

虽然 Metaclasses 允许以多种方式自定义类创建（参见 [Item 62](#ch08#ch08lev1sec5): “[Validate Subclasses with \_\_init\_subclass\_\_](#ch08#ch08lev1sec5)” 和 [Item 63](#ch08#ch08lev1sec6): “[Register Class Existence with \_\_init\_subclass\_\_](#ch08#ch08lev1sec6)”），但它们仍然无法处理可能出现的所有情况。

例如，假设要用一个打印参数、返回值和任何引发的异常的辅助函数来装饰类的所有方法。这里，定义了一个这样的调试装饰器（参见 [Item 38](#ch05#ch05lev1sec9): “[Define Function Decorators with functools.wraps](#ch05#ch05lev1sec9)” 获取背景）：

```python
from functools import wraps

def trace_func(func):
if hasattr(func, "tracing"):  # Only decorate once
return func

@wraps(func)
def wrapper(*args, **kwargs):
args_repr = repr(args)
kwargs_repr = repr(kwargs)
result = None
try:
result = func(*args, **kwargs)
return result
except Exception as e:
result = e
raise
finally:
print(
f"{func.__name__}"
f"({args_repr}, {kwargs_repr}) -> "
f"{result!r}"
)

wrapper.tracing = True
return wrapper
```

可以将其应用于新 `dict` 子类中的各种特殊方法（参见 [Item 57](#ch07#ch07lev1sec10): “[Inherit from collections.abc Classes for Custom Container Types](#ch07#ch07lev1sec10)”）：

```python
class TraceDict(dict):
@trace_func
def __init__(self, *args, **kwargs):
return super().__init__(*args, **kwargs)

@trace_func
def __setitem__(self, *args, **kwargs):
return super().__setitem__(*args, **kwargs)

@trace_func
def __getitem__(self, *args, **kwargs):
return super().__getitem__(*args, **kwargs)
```

可以通过与类的实例交互来验证这些方法是否被装饰：

```python
trace_dict = TraceDict([("hi", 1)])
trace_dict["there"] = 2
try:
trace_dict["does not exist"]
except KeyError:
pass  # Expected
```

此代码的问题在于，必须重新定义所有想要用 `@trace_func` 装饰的方法。这是冗余的样板代码，难以阅读且容易出错。此外，如果将来 `dict` 超类中添加了新方法，除非在 `TraceDict` 中也定义它，否则它不会被装饰。

解决此问题的一种方法是使用 metaclass 来自动装饰类的所有方法。这里通过用 `trace_func` 装饰器包装新类型中的每个函数或方法来实现此行为：

```python
import types

TRACE_TYPES = (
types.MethodType,
types.FunctionType,
types.BuiltinFunctionType,
types.BuiltinMethodType,
types.MethodDescriptorType,
types.ClassMethodDescriptorType,
types.WrapperDescriptorType,
)

IGNORE_METHODS = (
"__repr__",
"__str__",
)

class TraceMeta(type):
def __new__(meta, name, bases, class_dict):
klass = super().__new__(meta, name, bases, class_dict)

for key in dir(klass):
if key in IGNORE_METHODS:
continue

value = getattr(klass, key)
if not isinstance(value, TRACE_TYPES):
continue

wrapped = trace_func(value)
setattr(klass, key, wrapped)

return klass
```

现在可以通过使用 `TraceMeta` metaclass 来声明 `dict` 子类，并验证它是否按预期工作：

```python
class TraceDict(dict, metaclass=TraceMeta):
pass

trace_dict = TraceDict([("hi", 1)])
trace_dict["there"] = 2
try:
trace_dict["does not exist"]
except KeyError:
pass  # Expected
```

这可行，并且甚至会打印出调用 `__new__` 的信息，而我之前的实现中缺少了这一点。如果尝试在超类已指定 metaclass 时使用 `TraceMeta` 会发生什么？

```python
class OtherMeta(type):
pass

class SimpleDict(dict, metaclass=OtherMeta):
pass

class ChildTraceDict(SimpleDict, metaclass=TraceMeta):
pass
```

这会失败，因为 `TraceMeta` 不继承自 `OtherMeta`。理论上，可以通过让 `OtherMeta` 继承自 `TraceMeta` 来使用 metaclass 继承来解决此问题：

```python
class TraceMeta(type):
...

class OtherMeta(TraceMeta):
pass

class SimpleDict(dict, metaclass=OtherMeta):
pass

class ChildTraceDict(SimpleDict, metaclass=TraceMeta):
pass

trace_dict = ChildTraceDict([("hi", 1)])
trace_dict["there"] = 2
try:
trace_dict["does not exist"]
except KeyError:
pass  # Expected
```

但这在无法修改 metaclass 的库或希望同时使用多个实用程序 metaclass（如 `TraceMeta`）时不起作用。Metaclass 方法对正在修改的类施加了太多约束。

为了解决这个问题，Python 支持类装饰器。_Class decorators_ 的工作方式与函数装饰器类似：它们使用 `@` 符号前缀函数，然后是类声明。函数应相应地修改或重新创建类，然后返回它，如下所示：

```python
def my_class_decorator(klass):
klass.extra_param = "hello"
return klass

@my_class_decorator
class MyClass:
pass

print(MyClass)
print(MyClass.extra_param)
```

可以通过将上面 `TraceMeta.__new__` 方法的核心移到一个独立的函数中来实现类装饰器，以将 `trace_func` 函数装饰器应用于类的所有方法。此实现比 metaclass 版本短得多：

```python
def trace(klass):
for key in dir(klass):
if key in IGNORE_METHODS:
continue

value = getattr(klass, key)
if not isinstance(value, TRACE_TYPES):
continue

wrapped = trace_func(value)
setattr(klass, key, wrapped)

return klass
```

可以将其装饰应用于 `dict` 子类，以获得与使用上述 metaclass 方法相同的行为：

```python
@trace
class DecoratedTraceDict(dict):
pass

trace_dict = DecoratedTraceDict([("hi", 1)])
trace_dict["there"] = 2
try:
trace_dict["does not exist"]
except KeyError:
pass  # Expected
```

类装饰器在被装饰的类已经具有 metaclass 时也有效：

```python
class OtherMeta(type):
pass

@trace
class HasMetaTraceDict(dict, metaclass=OtherMeta):
pass

trace_dict = HasMetaTraceDict([("hi", 1)])
trace_dict["there"] = 2
try:
trace_dict["does not exist"]
except KeyError:
pass  # Expected
```

当寻找可组合的类扩展方式时，类装饰器是最佳工具。（参见 [Item 104](#ch12#ch12lev1sec5): “[Know How to Use heapq for Priority Queues](#ch12#ch12lev1sec5)” 获取名为 `functools.total_ordering` 的示例类装饰器。）

#### Things to Remember

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 类装饰器是一个简单的函数，它接收一个 `class` 实例作为参数，并返回一个新类或原始类的修改版本。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 当你想用最少的样板代码修改类的每个方法或属性时，类装饰器非常有用。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Metaclasses 不能轻松地组合在一起，尽管许多类装饰器可以用于在没有冲突的情况下扩展同一个类。

## Effective Python - 9

## 9

本章深入探讨了 Graph Neural Networks (GNNs) 在处理复杂数据结构方面的强大能力，并重点介绍了 Graph Foundation Models (GFMs) 的兴起及其在各种下游任务中的应用。我们首先回顾了 GNNs 的基本原理，包括 Message Passing 机制和 Node Embedding 的生成，以及 Graph Convolutional Networks (GCN) 和 Graph Attention Networks (GAT) 等经典模型。

随后，本章详细阐述了 GNNs 在 Self-supervised Learning 和 Pre-training 方面的进展，强调了如何利用大规模图数据进行有效的模型预训练，为后续的 Fine-tuning、In-context Learning、Few-shot Learning 和 Zero-shot Learning 任务奠定基础。我们探讨了 Contrastive Learning 等技术在学习有意义的 Node Embedding 中的作用，以及如何通过这些预训练模型实现跨领域迁移 (Cross-domain Transfer) 和 Domain Adaptation。

本章的核心贡献在于系统性地梳理了 GFMs 的发展脉络和关键技术。GFMs 旨在构建能够理解和推理图结构数据的通用模型，它们通常在大规模、多样化的图数据集上进行预训练，从而获得强大的泛化能力。我们讨论了 GFMs 在处理 Knowledge Graph、Heterogeneous Graph 和 Homogeneous Graph 等不同类型图数据时的优势，以及它们在解决 Graph Isomorphism 等挑战性问题上的潜力。

在应用层面，本章详细介绍了 GFMs 在多种图学习任务中的出色表现，包括 Graph Classification、Node Classification、Link Prediction、Graph Generation 和 Graph Anomaly Detection。此外，我们还探讨了 GFMs 在 Multi-modal Learning 场景下的应用，以及如何将图结构信息与文本、图像等其他模态的数据相结合，以实现更全面的理解和推理。

总而言之，本章为读者提供了一个关于 GNNs 和 GFMs 的全面视角，揭示了它们在人工智能领域，特别是在处理和理解图结构数据方面的巨大潜力和广阔前景。

## Effective Python - Concurrency and Parallelism

## 并发与并行 (Concurrency and Parallelism)

_并发 (Concurrency)_ 使计算机能够 _看似_ 同时处理许多不同的事情。例如，在单核 CPU 的计算机上，操作系统会快速切换正在处理器上运行的程序。通过这种方式，它会交错执行程序，从而产生程序同时运行的错觉。

_并行 (Parallelism)_ 则涉及 _实际_ 同时处理许多不同的事情。多核 CPU 的计算机可以同时执行多个程序。每个 CPU 核运行一个独立程序的指令，允许每个程序在同一时刻都取得进展。

在单个程序内部，并发是一种使程序员更容易解决特定类型问题的工具。并发程序支持许多不同的执行路径，包括独立的 I/O 流，使其能够以看似同时且独立的方式取得进展。

并行与并发的关键区别在于 _加速比 (speedup)_。当程序中两个不同的执行路径并行取得进展时，完成总工作所需的时间会减半；执行速度会提高一倍。相比之下，并发程序可能看似并行地运行数千个独立的执行路径，但对总工作量并没有加速。

Python 使得以多种风格编写并发程序变得容易。Threads 支持相对少量的并发，而 asynchronous coroutines 则支持大量并发函数。Python 还可以通过系统调用、subprocess 和 C 扩展来执行并行工作。但是，要使并发 Python 代码真正并行运行可能非常困难。了解如何最好地利用 Python 在这些不同情况下的能力非常重要。

### Item 67: 使用 `subprocess` 管理子进程 (Use `subprocess` to Manage Child Processes)

Python 拥有经过实战检验的库来运行和管理子进程。这使得 Python 成为粘合其他工具（如命令行实用程序）的绝佳语言。当现有的 shell 脚本随着时间的推移变得复杂时，为了提高可读性和可维护性而将其重写为 Python 是一个自然的选择。

Python 启动的子进程能够与父进程并行运行，使您能够利用 Python 来消耗机器的所有 CPU 核心并最大化程序的吞吐量。虽然 Python 本身可能受 CPU 限制（参见 [Item 68](#ch09#ch09lev1sec2): “使用 Threads 进行阻塞 I/O；避免并行”），但驱动和协调 CPU 密集型工作负载却很容易。

Python 有多种运行子进程的方式（例如 `os.popen`, `os.exec*`），但管理子进程的最佳选择是使用 `subprocess` 内置模块。使用 `subprocess` 运行子进程很简单。这里我使用该模块的 `run` 方便函数来启动一个进程、读取其输出并验证它是否已干净地终止：

[Click here to view code image](#ch09_images#f0320-01)

```python
import subprocess

result = subprocess.run(
["echo", "Hello from the child!"],
capture_output=True,
encoding="utf-8",
)

result.check_returncode()  # No exception means it exited cleanly
print(result.stdout)

>>>
Hello from the child!
```

**Note**
此项中的示例假设您的系统具有 `echo`、`sleep` 和 `openssl` 命令。在 Windows 上，情况可能并非如此。请参阅此项在线的完整示例代码，了解在 Windows 上运行这些代码片段的具体说明。

子进程独立于其父进程（Python 解释器）运行。如果您使用 `Popen` 类而不是 `run` 函数创建子进程，您可以在 Python 执行其他工作时定期轮询子进程状态：

[Click here to view code image](#ch09_images#f0321-01)

```python
proc = subprocess.Popen(["sleep", "1"])
while proc.poll() is None:
print("Working...")
# Some time-consuming work here
...

print("Exit status", proc.poll())

>>>
Working...
Working...
Working...
Working...
Exit status 0
```

将子进程与父进程解耦，使父进程能够并行运行许多子进程。我通过一次性启动所有子进程并使用 `Popen` 来实现这一点：

[Click here to view code image](#ch09_images#f0321-02)

```python
import time

start = time.perf_counter()
sleep_procs = []
for _ in range(10):
proc = subprocess.Popen(["sleep", "1"])
sleep_procs.append(proc)
```

稍后，我可以使用 `communicate` 方法等待它们完成 I/O 并终止：

[Click here to view code image](#ch09_images#f0321-03)

```python
for proc in sleep_procs:
proc.communicate()

end = time.perf_counter()
delta = end - start
print(f"Finished in {delta:.3} seconds")

>>>
Finished in 1.01 seconds
```

如果这些进程按顺序运行，总延迟将为 10 秒或更长，而不是我测量的约 1 秒。

您还可以将数据从 Python 程序通过管道传输到子进程并检索其输出。这使您能够利用许多其他程序并行工作。例如，假设我想使用 `openssl` 命令行工具来加密一些数据。使用命令行参数和 I/O 管道启动子进程很容易：

[Click here to view code image](#ch09_images#f0322-01)

```python
import os

def run_encrypt(data):
env = os.environ.copy()
env["password"] = "zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1"
proc = subprocess.Popen(
["openssl", "enc", "-des3", "-pass", "env:password"],
env=env,
stdin=subprocess.PIPE,
stdout=subprocess.PIPE,
)
proc.stdin.write(data)
proc.stdin.flush()  # Ensure that the child gets input
return proc
```

这里我将随机字节通过管道传输到加密函数，但在实践中，此输入管道将通过用户输入、文件句柄、网络套接字等提供数据：

```python
procs = []
for _ in range(3):
data = os.urandom(10)
proc = run_encrypt(data)
procs.append(proc)
```

子进程并行运行并消耗其输入。这里我等待它们完成，然后检索它们的最终输出。输出是预期的随机加密字节：

[Click here to view code image](#ch09_images#f0322-02)

```python
for proc in procs:
out, _ = proc.communicate()
print(out[-10:])

>>>
b'\x02a_\xd3\xd3\x9a\xd0\x8f\x14|'
b'S\x9c\x1a\x919\x9a-P\x0c\x1f'
b'\x1a\x7f\x1e\xbf\xac\xe5A>\xa3\xdd'
```

创建进程链也是可能的，就像 UNIX 管道一样，将一个子进程的输出连接到另一个子进程的输入，依此类推。这是一个启动 `openssl` 命令行工具作为子进程来生成输入流的 Whirlpool 哈希的函数：

[Click here to view code image](#ch09_images#f0323-01)

```python
def run_hash(input_stdin):
return subprocess.Popen(
["openssl", "dgst", "-whirlpool", "-binary"],
stdin=input_stdin,
stdout=subprocess.PIPE,
)
```

现在我可以启动一组进程来加密一些数据，然后启动另一组进程来哈希其加密后的输出。请注意，我必须小心处理上游进程的 `stdout` 实例如何被启动此子进程管道的 Python 解释器进程保留：

[Click here to view code image](#ch09_images#f0323-02)

```python
encrypt_procs = []
hash_procs = []
for _ in range(3):
data = os.urandom(100)

encrypt_proc = run_encrypt(data)
encrypt_procs.append(encrypt_proc)

hash_proc = run_hash(encrypt_proc.stdout)
hash_procs.append(hash_proc)

# Ensure that the child consumes the input stream and
# the communicate() method doesn't inadvertently steal
# input from the child. Also lets SIGPIPE propagate to
# the upstream process if the downstream process dies.
encrypt_proc.stdout.close()
encrypt_proc.stdout = None
```

一旦子进程启动，它们之间的 I/O 就会自动发生。我需要做的就是等待它们完成并打印最终输出：

[Click here to view code image](#ch09_images#f0323-03)

```python
for proc in encrypt_procs:
proc.communicate()
assert proc.returncode == 0

for proc in hash_procs:
out, _ = proc.communicate()
print(out[-10:])
assert proc.returncode == 0

>>>
b'\xc6\n\x8a"cg\x85\xd2\x81|'
b'\x14\r\xc6J\xb0\xb0\xbf\x0c2X'
b'@\x90$\xcc\xc7\xf4\x08\x19Y\x0b'
```

如果我担心子进程永远不会完成或以某种方式阻塞在输入或输出管道上，我可以将 `timeout` 参数传递给 `communicate` 方法。如果子进程在指定时间内未完成，这将引发一个异常，使我能够终止行为不端的子进程：

[Click here to view code image](#ch09_images#f0324-02)

```python
proc = subprocess.Popen(["sleep", "10"])
try:
proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
proc.terminate()
proc.wait()

print("Exit status", proc.poll())

>>>
Exit status -15
```

#### 记住 (Things to Remember)

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `subprocess` 模块运行子进程并管理它们的输入和输出流。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 子进程与 Python 解释器并行运行，使您能够最大化 CPU 核心的使用率。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 对于简单用法，请使用 `run` 方便函数；对于高级用法（如 UNIX 风格的管道），请使用 `Popen` 类。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `communicate` 方法的 `timeout` 参数来避免死锁和挂起的子进程。

### Item 68: 使用 Threads 进行阻塞 I/O；避免并行 (Use Threads for Blocking I/O; Avoid for Parallelism)

Python 的标准实现称为 CPython。CPython 分两步运行 Python 程序。首先，它将源代码文本解析并编译成 _字节码 (bytecode)_，这是程序的一种低级表示，由 8 位指令组成（有关背景信息，请参见 [Item 97](#ch11#ch11lev1sec6): “依赖预编译字节码和文件系统缓存来提高启动时间”）。（截至 Python 3.6，技术上是 16 位指令的 _wordcode_，但原理相同。）然后，CPython 使用基于堆栈的解释器运行字节码。字节码解释器具有在 Python 程序执行期间必须保持一致的状态。CPython 使用一种称为 _全局解释器锁 (global interpreter lock)_ (GIL) 的机制来强制执行一致性。

本质上，GIL 是一个互斥锁 (mutex)，可防止 CPython 受抢占式多线程的影响，即一个线程通过中断另一个线程来控制程序。此类中断如果发生在意想不到的时间，可能会损坏解释器状态（例如，垃圾回收的引用计数）。GIL 可防止这些中断，并确保每个字节码指令都能与 CPython 实现及其 C 扩展模块正确工作（有关背景信息，请参见 [Item 96](#ch11#ch11lev1sec5): “考虑扩展模块以最大化性能和人体工程学”）。

GIL 具有一个重要的负面副作用。对于用 C++ 或 Java 等语言编写的程序，拥有多个执行线程意味着程序可以同时利用多个 CPU 核心。尽管 Python 支持多个执行线程，但 GIL 导致一次只有一个线程能够取得进展。这意味着当您尝试使用 threads 来执行并行计算并加速 Python 程序时，您将大失所望。

例如，假设我想用 Python 做一些计算密集型的事情。这里我使用一个朴素的数字分解算法作为代理：

[Click here to view code image](#ch09_images#f0325-01)

```python
def factorize(number):
for i in range(1, number + 1):
if number % i == 0:
yield i
```

串行分解一个 16 个数字的列表需要很长时间：

[Click here to view code image](#ch09_images#f0325-02)

```python
import time

numbers = [7775876, 6694411, 5038540, 5426782,
9934740, 9168996, 5271226, 8288002,
9403196, 6678888, 6776096, 9582542,
7107467, 9633726, 5747908, 7613918]
start = time.perf_counter()

for number in numbers:
list(factorize(number))

end = time.perf_counter()
delta = end - start

print(f"Took {delta:.3f} seconds")

>>>
Took 3.304 seconds
```

在其他语言中，使用多个线程来执行此计算是有意义的，因为我可以利用计算机的所有 CPU 核心。让我尝试在 Python 中这样做。这里我定义了一个 Python 线程来执行与之前相同的计算：

[Click here to view code image](#ch09_images#f0326-02)

```python
from threading import Thread

class FactorizeThread(Thread):
def __init__(self, number):
super().__init__()
self.number = number

def run(self):
self.factors = list(factorize(self.number))
```

然后，我为每个数字启动一个线程以并行分解：

[Click here to view code image](#ch09_images#f0326-03)

```python
start = time.perf_counter()

threads = []
for number in numbers:
thread = FactorizeThread(number)
thread.start()
threads.append(thread)
```

最后，我等待所有线程完成：

[Click here to view code image](#ch09_images#f0326-04)

```python
for thread in threads:
thread.join()

end = time.perf_counter()
delta = end - start
print(f"Took {delta:.3f} seconds")

>>>
Took 3.293 seconds
```

令人惊讶的是，这花费的时间几乎与串行运行 `factorize` 的时间相同。对于每个数字一个线程——在这个例子中总共 16 个线程——您可能期望在其他语言中由于创建线程和协调它们的开销而获得不到 16 倍的加速。您可能还期望在我的 8 核机器上仅获得 8 倍的加速。但您不会期望当有多个 CPU 可用时，这些线程的性能似乎没有提高。这演示了 GIL（例如，锁争用、调度开销）对在标准 CPython 解释器中运行的程序的影响。

有方法可以让 CPython 利用多个核心，但它们不适用于标准的 `Thread` 类（参见 [Item 79](#ch09#ch09lev1sec13): “考虑 concurrent.futures 以实现真正的并行” 和 [Item 94](#ch11#ch11lev1sec3): “知道何时以及如何用另一种编程语言替换 Python”），并且它们可能需要大量的努力。

**Note**
从 CPython 3.13 版本开始，有一个实验性的选项可以在没有 GIL 的情况下编译 Python，从而使程序可以避免其限制。这可以提高多线程的并行性能，但存在显著的缺点：许多 C 扩展模块和常用库尚未与此行为兼容；并且由于同步开销，单个线程的直线性能会降低。观察此实验在后续版本中的发展将很有趣。

考虑到这些限制，Python 为什么还要支持 threads 呢？有两个好理由。

首先，多个 threads 使程序看似同时执行多项任务变得容易。管理并发任务的协调工作很难自己实现（例如，参见 [Item 71](#ch09#ch09lev1sec5): “知道何时需要并发”）。使用 threads，您可以将并发运行函数的工作交给 Python。这之所以有效，是因为 CPython 确保了 Python 执行线程之间的公平性，即使由于 GIL 的原因一次只有一个线程能够取得进展。

Python 支持 threads 的第二个原因是处理阻塞 I/O，当 Python 执行某些类型的系统调用时会发生这种情况。Python 程序使用系统调用来请求计算机操作系统代表它与外部环境进行交互。阻塞 I/O 包括读取和写入文件、与网络交互、与显示器等设备通信等。Threads 通过将程序与操作系统响应请求所需的延迟隔离开来，帮助处理阻塞 I/O。

例如，假设我想通过串行端口向遥控直升机发送信号。我将使用一个慢速系统调用（`select`）作为此活动的代理。此函数要求操作系统阻塞 0.1 秒，然后将控制权返回给我的程序，这与使用同步串行端口时发生的情况类似：

[Click here to view code image](#ch09_images#f0328-01)

```python
import select
import socket

def slow_systemcall():
select.select([socket.socket()], [], [], 0.1)
```

串行运行此系统调用需要线性增加的时间——5 次调用大约需要 0.5 秒：

[Click here to view code image](#ch09_images#f0328-02)

```python
start = time.perf_counter()

for _ in range(5):
slow_systemcall()

end = time.perf_counter()
delta = end - start
print(f"Took {delta:.3f} seconds")

>>>
Took 0.525 seconds
```

问题在于，当 `slow_systemcall` 函数运行时，我的程序无法取得任何其他进展。我的程序的 main thread 被阻塞在 `select` 系统调用上。这种情况在实践中非常糟糕。我需要在发送信号的同时计算直升机的下一步移动；否则，它将崩溃。当您发现自己需要同时执行阻塞 I/O 和计算时，就该考虑将系统调用移到 threads 中了。

这里我将在单独的 threads 中运行 `slow_systemcall` 函数的多个调用。这使我能够同时与多个串行端口（和直升机）通信，同时让主线程执行所需的任何计算：

[Click here to view code image](#ch09_images#f0328-03)

```python
start = time.perf_counter()

threads = []
for _ in range(5):
thread = Thread(target=slow_systemcall)
thread.start()
threads.append(thread)
```

启动 threads 后，这里我执行一些工作来计算下一个直升机移动，然后再等待系统调用 threads 完成：

[Click here to view code image](#ch09_images#f0329-01)

```python
def compute_helicopter_location(index):
...

for i in range(5):
compute_helicopter_location(i)

for thread in threads:
thread.join()

end = time.perf_counter()
delta = end - start
print(f"Took {delta:.3f} seconds")

>>>
Took 0.106 seconds
```

并行时间比前面示例代码中的串行时间少约 5 倍。这表明所有系统调用将从多个 Python 线程并行运行，即使它们受 GIL 的限制。GIL 阻止我的 Python 代码并行运行，但它不会影响系统调用。Python 线程在执行系统调用之前会释放 GIL，并在系统调用完成后重新获取 GIL。

除了使用 threads 之外，还有许多其他方法可以处理阻塞 I/O，例如使用 `asyncio` 内置模块，这些替代方法具有重要的优势。但这些选项可能需要额外的重构工作才能适应不同的执行模型（参见 [Item 75](#ch09#ch09lev1sec9): “使用 Coroutines 实现高度并发的 I/O” 和 [Item 77](#ch09#ch09lev1sec11): “混合使用 Threads 和 Coroutines 以简化向 asyncio 的过渡”）。使用 threads 是以并行方式执行阻塞 I/O 的最简单方法，对您的程序进行的更改最少。

#### 记住 (Things to Remember)

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 由于全局解释器锁 (GIL)，Python 线程无法在多个 CPU 核心上并行运行。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 尽管存在 GIL，Python 线程仍然有用，因为它们提供了一种轻松地看似同时执行多项任务的方法。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 您可以使用 Python 线程并行执行多个系统调用，从而允许您同时进行阻塞 I/O 和计算。

### Item 69: 使用 `Lock` 防止 Threads 中的数据竞争 (Use `Lock` to Prevent Data Races in Threads)

在了解了全局解释器锁 (GIL)（参见 [Item 68](#ch09#ch09lev1sec2): “使用 Threads 进行阻塞 I/O；避免并行”）之后，许多新的 Python 程序员认为他们可以完全放弃在代码中使用互斥锁 (mutexes)。如果 GIL 已经阻止 Python 线程并行运行在多个 CPU 核心上，那么它也必须充当程序数据结构的锁，对吧？对列表和字典等类型进行一些测试甚至可能表明此假设似乎成立。

但请注意：事实并非如此。GIL 不会保护您。尽管一次只有一个 Python 线程运行，但线程对数据结构的操作可以在 Python 解释器中的任何两个字节码指令之间被中断。如果您同时从多个线程访问相同的对象，这很危险。由于这些中断，您的数据结构的不变量几乎随时都可能被违反，从而可能使您的程序处于损坏状态。

例如，假设我想编写一个程序来并行计数许多事物，例如从传感器网络采样光照水平。假设每个传感器都有自己的工作线程，因为从传感器读取需要阻塞 I/O。在每次传感器测量之后，工作线程会增加一个共享计数器变量，其中包含接收到的光子数：

[Click here to view code image](#ch09_images#f0330-01)

```python
counter = 0

def read_sensor(sensor_index):
# Returns sensor data or raises an exception
...

def get_offset(data):
# Always returns 1 or greater
...

def worker(sensor_index, how_many):
global counter
for _ in range(how_many):
data = read_sensor(sensor_index)
counter += get_offset(data)
```

这里我为每个传感器并行运行一个 `worker` 线程，并等待它们全部完成读取：

[Click here to view code image](#ch09_images#f0330-02)

```python
from threading import Thread

how_many = 10**6
sensor_count = 4

threads = []
for i in range(sensor_count):
thread = Thread(target=worker, args=(i, how_many))
threads.append(thread)
thread.start()

for thread in threads:
thread.join()

expected = how_many * sensor_count
print(f"Counter should be {expected}, got {counter}")

>>>
Counter should be 4000000, got 1980032
```

考虑到 `get_offset` 总是返回 1 或更多，结果似乎相差甚远！这里发生了什么？为什么如此简单的事情会出错，尤其是在只有一个 Python 解释器线程可以一次运行的情况下（由于 GIL）？

答案是抢占。Python 解释器强制执行所有正在执行的线程之间的公平性，以确保它们获得大致相等的处理时间。为此，Python 会暂停正在运行的线程，然后轮流恢复另一个线程。问题在于您不知道 Python 何时会暂停您的线程。线程甚至可能在看起来是原子操作的中间被暂停。

这正是发生在此处 `worker` 函数的这一行代码中发生的情况：

```python
counter += get_offset(data)
```

`+=` 运算符用于 `counter` 变量实际上指示 Python 在后台执行三个单独的操作。上面的语句等同于：

```python
value = counter
delta = get_offset(data)
result = value + delta
counter = result
```

Python 线程递增计数器可能在这些操作中的任何两个之间被暂停。如果操作的交错方式导致旧版本的 `value` 被分配给计数器，则会产生问题。以下是两个线程 A 和 B 之间不良交互的示例：

[Click here to view code image](#ch09_images#f0332-01)

```python
# Running in Thread A
value_a = counter
delta_a = get_offset(data_a)
# Context switch to Thread B
value_b = counter
delta_b = get_offset(data_b)
result_b = value_b + delta_b
counter = result_b
# Context switch back to Thread A
result_a = value_a + delta_a
counter = result_a
```

线程 B 在线程 A 完成之前中断了它。线程 B 运行并完成，但然后线程 A 在执行中间恢复，覆盖了线程 B 在递增计数器方面的所有进展。这正是上面光传感器示例中发生的情况。

为了防止此类数据竞争以及其他形式的数据结构损坏，Python 在 `threading` 内置模块中包含了一套强大的工具。其中最简单也是最有用的类是 `Lock`，一个互斥锁 (mutex)。

通过使用锁，我可以让 `Counter` 类保护其当前值免受多个线程的同时访问。一次只有一个线程能够获取锁。这里我使用 `with` 语句来获取和释放锁；额外的缩进级别使代码更容易看到在持有锁时执行的代码（有关背景信息，请参见 [Item 82](#ch10#ch10lev1sec3): “考虑使用 contextlib 和 with 语句实现可重用的 try/finally 行为”）：

[Click here to view code image](#ch09_images#f0332-02)

```python
from threading import Lock

counter = 0
counter_lock = Lock()

def locking_worker(sensor_index, how_many):
global counter
for _ in range(how_many):
data = read_sensor(sensor_index)
with counter_lock:                  # Added
counter += get_offset(data)
```

现在我像以前一样运行传感器线程，但使用 `locking_worker`：

[Click here to view code image](#ch09_images#f0333-01)

```python
for i in range(sensor_count):
thread = Thread(target=locking_worker, args=(i, how_many))
threads.append(thread)
thread.start()

for thread in threads:
thread.join()

expected = how_many * sensor_count
print(f"Counter should be {expected}, got {counter}")

>>>
Counter should be 4000000, got 4000000
```

结果完全符合我的预期。`Lock` 解决了问题。

#### 记住 (Things to Remember)

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 即使 Python 有全局解释器锁，您仍然负责保护程序中的线程之间的数据竞争。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果您允许多个线程在没有互斥锁 (mutexes) 的情况下修改相同的对象，您的程序将损坏其数据结构。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `threading` 内置模块中的 `Lock` 类来强制执行多个线程之间的程序不变量。

### Item 70: 使用 `Queue` 协调 Threads 之间的工作 (Use `Queue` to Coordinate Work Between Threads)

执行许多并发任务的 Python 程序通常需要协调其工作。并发工作中最有用的安排之一是函数管道。

管道的工作方式类似于制造业中的装配线。管道有许多串行阶段，每个阶段都有一个特定的函数。新工作项不断添加到管道的开头。函数可以并发运行，每个函数处理其阶段中的工作项。工作项在每个函数完成时向前移动，直到没有剩余阶段。这种方法特别适用于包含阻塞 I/O 或子进程的工作——这些活动可以使用 Python 轻松并行化（参见 [Item 67](#ch09#ch09lev1sec1): “使用 subprocess 管理子进程” 和 [Item 68](#ch09#ch09lev1sec2): “使用 Threads 进行阻塞 I/O；避免并行”）。

例如，假设我想构建一个系统，该系统将不断从我的数码相机获取图像流，调整它们的大小，然后将它们添加到在线照片库中。这样的程序可以分为管道的三个阶段。第一阶段检索新图像。下载的图像在第二阶段通过 resize 函数。调整大小后的图像由最后一个阶段的 upload 函数消耗。

假设我已经编写了执行这些阶段的 Python 函数：`download`、`resize` 和 `upload`。如何组装一个管道来并发地完成这项工作？

```python
def download(item):
...

def resize(item):
...

def upload(item):
...
```

我首先需要一种方法来在管道阶段之间传递工作。这可以建模为线程安全的生产者-消费者队列（参见 [Item 69](#ch09#ch09lev1sec3): “使用 Lock 防止 Threads 中的数据竞争” 以了解 Python 中线程安全的重要性；参见 [Item 103](#ch12#ch12lev1sec4): “优先使用 deque 作为生产者-消费者队列” 以了解队列性能）：

```python
from collections import deque
from threading import Lock

class MyQueue:
def __init__(self):
self.items = deque()
self.lock = Lock()
```

生产者，即我的数码相机，将新图像添加到待处理项的 `deque` 的末尾：

[Click here to view code image](#ch09_images#f0334-01)

```python
def put(self, item):
with self.lock:
self.items.append(item)
```

消费者，即处理管道的第一阶段，从待处理项的 `deque` 的开头移除图像：

[Click here to view code image](#ch09_images#f0335-01)

```python
def get(self):
with self.lock:
return self.items.popleft()
```

这里我将管道的每个阶段表示为一个 Python 线程，该线程从一个队列获取工作，对其运行一个函数，并将结果放入另一个队列。我还跟踪工作线程检查新输入的次数以及它已完成的工作量：

[Click here to view code image](#ch09_images#f0335-02)

```python
from threading import Thread
import time

class Worker(Thread):
def __init__(self, func, in_queue, out_queue):
super().__init__()
self.func = func
self.in_queue = in_queue
self.out_queue = out_queue
self.polled_count = 0
self.work_done = 0
```

最棘手的部分是工作线程必须正确处理输入队列为空的情况，因为前一个阶段尚未完成其工作。这发生在下面的 `IndexError` 异常捕获处。您可以将其视为装配线上的瓶颈：

[Click here to view code image](#ch09_images#f0335-03)

```python
def run(self):
while True:
self.polled_count += 1
try:
item = self.in_queue.get()
except IndexError:
time.sleep(0.01)  # No work to do
else:
result = self.func(item)
self.out_queue.put(result)
self.work_done += 1
```

现在，我可以通过创建队列来协调它们的连接点以及相应的 worker 线程来连接三个阶段：

[Click here to view code image](#ch09_images#f0335-04)

```python
download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()
done_queue = MyQueue()
threads = [
Worker(download, download_queue, resize_queue),
Worker(resize, resize_queue, upload_queue),
Worker(upload, upload_queue, done_queue),
]
```

我可以启动线程，然后将大量工作注入管道的第一阶段。这里我使用一个普通的 `object` 实例作为 `download` 函数所需的实际数据的代理：

[Click here to view code image](#ch09_images#f0336-02)

```python
for thread in threads:
thread.start()

for _ in range(1000):
download_queue.put(object())
```

现在我等待所有项目被管道处理并进入 `done_queue`：

[Click here to view code image](#ch09_images#f0336-03)

```python
while len(done_queue.items) < 1000:
# Do something useful while waiting
...
```

这运行正常，但由于线程轮询其输入队列以获取新工作，因此会产生一个有趣的副作用。棘手的部分，即我在 `run` 方法中捕获 `IndexError` 异常，会执行大量次数：

[Click here to view code image](#ch09_images#f0336-04)

```python
processed = len(done_queue.items)
polled = sum(t.polled_count for t in threads)
print(f"Processed {processed} items after "
f"polling {polled} times")

>>>
Processed 1000 items after polling 3033 times
```

当 worker 函数的速度各不相同时，早期阶段会阻止后续阶段的进展，导致管道堵塞。这会导致后续阶段饥饿，并在紧密循环中不断检查其输入队列以获取新工作。结果是 worker 线程浪费 CPU 时间做无用功；它们不断地引发和捕获 `IndexError` 异常。

但这仅仅是此实现中存在问题的开始。还有三个问题您也应该避免。首先，确定所有输入工作已完成需要对 `done_queue` 进行另一次忙等待。其次，在 `Worker` 中，`run` 方法将在其忙碌循环中永远执行。没有明显的方法可以向 worker 线程发出信号，表明是时候退出了。

第三，也是最糟糕的，管道中的备份可能导致程序任意崩溃。如果第一阶段进展迅速，但第二阶段进展缓慢，那么连接第一阶段和第二阶段的队列的大小将不断增加。第二阶段将无法跟上。给定足够的时间和输入数据，程序最终将耗尽内存并终止。

这里的教训不是管道不好；而是很难自己构建一个好的生产者-消费者队列。那么为什么要尝试呢？

#### `Queue` 来救援 (Queue to the Rescue)

`queue` 内置模块中的 `Queue` 类提供了解决上述问题所需的所有功能。

`Queue` 通过使 `get` 方法阻塞调用线程直到数据可用，从而消除了对新项目的忙等待。例如，这里我启动一个线程，该线程等待队列中的一些输入数据：

[Click here to view code image](#ch09_images#f0337-01)

```python
from queue import Queue

my_queue = Queue()

def consumer():
print("Consumer waiting")
my_queue.get()  # Runs after put() below
print("Consumer done")

thread = Thread(target=consumer)
thread.start()
```

即使消费者线程首先运行，它也不会完成，直到 `put` 方法将一个项目添加到 `Queue` 实例并且 `get` 方法有东西返回：

[Click here to view code image](#ch09_images#f0337-02)

```python
print("Producer putting")
my_queue.put(object())  # Runs before get() above
print("Producer done")
thread.join()

>>>
Consumer waiting
Producer putting
Producer done
Consumer done
```

为了解决管道备份问题并避免内存错误，`Queue` 类允许您指定两个阶段之间允许的待处理工作量。当队列已满时，此缓冲区大小会导致 `put` 调用阻塞。（有时此行为称为 _反压 (back pressure)_）。例如，这里我定义了一个线程，该线程等待一段时间后再消耗队列：

[Click here to view code image](#ch09_images#f0338-01)

```python
my_queue = Queue(1)  # Buffer size of 1

def consumer():
time.sleep(0.1)  # Wait
my_queue.get()   # Runs second
print("Consumer got 1")
my_queue.get()   # Runs fourth
print("Consumer got 2")
print("Consumer done")

thread = Thread(target=consumer)
thread.start()
```

等待应该允许生产者线程在消费者线程调用 `get` 之前调用队列的 `put` 方法两次。但是队列的大小是 1。这意味着向队列添加项目的生产者必须等待消费者线程至少调用一次 `get`，然后第二次调用 `put` 才会停止阻塞并实际将第二个项目添加到队列：

[Click here to view code image](#ch09_images#f0338-02)

```python
my_queue.put(object())  # Runs first
print("Producer put 1")
my_queue.put(object())  # Runs third
print("Producer put 2")
print("Producer done")
thread.join()

>>>
Producer put 1
Consumer got 1
Producer put 2
Producer done
Consumer got 2
Consumer done
```

`Queue` 类还可以使用 `task_done` 方法跟踪工作进度。这允许您等待一个阶段的输入队列排空（使用 `join` 方法），并消除了对管道最后一个阶段进行轮询的需要（如上面部分中的 `done_queue`）。例如，这里我定义了一个消费者线程，该线程在完成处理一个项目后调用 `task_done`：

[Click here to view code image](#ch09_images#f0339-01)

```python
in_queue = Queue()

def consumer():
print("Consumer waiting")
work = in_queue.get()      # Runs second
print("Consumer working")
# Doing work
...
print("Consumer done")
in_queue.task_done()       # Runs third

thread = Thread(target=consumer)
thread.start()
```

现在生产者代码不必调用消费者线程的 `join` 或进行轮询。生产者只需通过调用 `Queue` 实例的 `join` 来等待 `in_queue` 完成。即使它已为空，`in_queue` 也不会是可 join 的，直到为曾经入队的每个项目调用了 `task_done`：

[Click here to view code image](#ch09_images#f0339-02)

```python
print("Producer putting")
in_queue.put(object())     # Runs first
print("Producer waiting")
in_queue.join()            # Runs fourth
print("Producer done")
thread.join()

>>>
Consumer waiting
Producer putting
Producer waiting
Consumer working
Consumer done
Producer done
```

`Queue` 类还允许通过调用 `shutdown` 方法（Python 3.13 版本中添加的功能）轻松终止 worker 线程。收到 shutdown 信号后，对队列的任何 `put` 调用都将引发异常，但队列将允许 `get` 调用排空队列并完成待处理工作。一旦队列完全为空，`get` 将在 worker 线程中引发 `ShutDown` 异常，使其有机会清理并退出（有关背景信息，请参见 [Item 80](#ch10#ch10lev1sec1): “利用 try/except/else/finally 中的每个块”）。例如，这里我展示了一个线程如何在调用 `shutdown` 后继续处理工作：

[Click here to view code image](#ch09_images#f0340-01)

```python
from queue import ShutDown

my_queue2 = Queue()

def consumer():
while True:
try:
item = my_queue2.get()
except ShutDown:
print("Terminating!")
return
else:
print("Got item", item)
my_queue2.task_done()

thread = Thread(target=consumer)
my_queue2.put(1)
my_queue2.put(2)
my_queue2.put(3)
my_queue2.shutdown()

thread.start()

my_queue2.join()
thread.join()
print("Done")

>>>
Got item 1
Got item 2
Got item 3
Terminating!
Done
```

我可以将所有这些行为整合到一个新的 worker 线程类中，该类一次处理一个输入项，将结果放入输出队列，将输入项标记为已完成，并在引发 `ShutDown` 异常时终止：

[Click here to view code image](#ch09_images#f0340-02)

```python
class StoppableWorker(Thread):
def __init__(self, func, in_queue, out_queue):
super().__init__()
self.func = func
self.in_queue = in_queue
self.out_queue = out_queue

def run(self):
while True:
try:
item = self.in_queue.get()
except ShutDown:
return
else:
result = self.func(item)
self.out_queue.put(result)
self.in_queue.task_done()
```

现在我可以使用新的 worker 类创建一组管道线程和队列；`resize` 和 `upload` 阶段具有指定的最大项目数，以防止程序耗尽内存：

[Click here to view code image](#ch09_images#f0341-02)

```python
download_queue = Queue()
resize_queue = Queue(100)
upload_queue = Queue(100)
done_queue = Queue()

threads = [
StoppableWorker(download, download_queue, resize_queue),
StoppableWorker(resize, resize_queue, upload_queue),
StoppableWorker(upload, upload_queue, done_queue),
]

for thread in threads:
thread.start()
```

为了开始处理，我将所有输入工作注入管道的开头：

[Click here to view code image](#ch09_images#f0341-03)

```python
for _ in range(1000):
download_queue.put(object())
```

然后我等待每个阶段的工作完成。我小心地在将终止信号发送到下一个阶段之前，对每个队列调用 `shutdown`，并使用 `join` 方法确保我等待队列中的所有工作完成：

```python
download_queue.shutdown()
download_queue.join()

resize_queue.shutdown()
resize_queue.join()

upload_queue.shutdown()
upload_queue.join()
```

在先前阶段完成后，我将 shutdown 信号发送到最后一个队列，在主线程中接收每个输出项，并等待 worker 线程终止：

[Click here to view code image](#ch09_images#f0342-01)

```python
done_queue.shutdown()

counter = 0

while True:
try:
item = done_queue.get()
except ShutDown:
break
else:
# Process the item
...
done_queue.task_done()
counter += 1

done_queue.join()

for thread in threads:
thread.join()

print(counter, "items finished")

>>>
1000 items finished
```

此方法可以扩展为每个阶段使用多个 worker 线程，这可以增加 I/O 并行性并显著加快此类程序的运行速度。为此，我首先定义用于启动 worker 线程副本和排空最终队列的辅助函数：

[Click here to view code image](#ch09_images#f0342-02)

```python
def start_threads(count, *args):
threads = [StoppableWorker(*args) for _ in range(count)]
for thread in threads:
thread.start()
return threads

def drain_queue(input_queue):
input_queue.shutdown()

counter = 0

while True:
try:
item = input_queue.get()
except ShutDown:
break
else:
input_queue.task_done()
counter += 1

input_queue.join()

return counter
```

然后我像以前一样将队列连接起来并启动 worker：

[Click here to view code image](#ch09_images#f0343-02)

```python
download_queue = Queue()
resize_queue = Queue(100)
upload_queue = Queue(100)
done_queue = Queue()

threads = (
start_threads(3, download, download_queue, resize_queue)
+ start_threads(4, resize, resize_queue, upload_queue)
+ start_threads(5, upload, upload_queue, done_queue)
)
```

按照与上面示例相同的 `put`、`shutdown`、`get` 和 `join` 调用顺序，我可以驱动工作通过管道——但这次为每个中间阶段使用多个 worker：

[Click here to view code image](#ch09_images#f0343-03)

```python
for _ in range(2000):
download_queue.put(object())

download_queue.shutdown()
download_queue.join()

resize_queue.shutdown()
resize_queue.join()

upload_queue.shutdown()
upload_queue.join()

counter = drain_queue(done_queue)

for thread in threads:
thread.join()

print(counter, "items finished")

>>>
2000 items finished
```

虽然 `Queue` 在线性管道中效果很好，但在不同情况下还有其他工具需要考虑（参见 [Item 75](#ch09#ch09lev1sec9): “使用 Coroutines 实现高度并发的 I/O”）。

#### 记住 (Things to Remember)

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 管道允许您组织工作序列——特别是 I/O 密集型程序——这些程序使用多个 Python 线程并发运行。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 注意构建并发管道中的许多问题：忙等待、告知 worker 停止、知道工作何时完成以及内存爆炸。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `Queue` 类具有构建健壮管道所需的所有功能：阻塞操作、缓冲区大小、join 和 shutdown。

### Item 71: 知道何时需要并发 (Know How to Recognize When Concurrency Is Necessary)

不可避免地，随着程序的范围扩大，其复杂性也随之增加。以一种保持清晰性、可测试性和效率的方式来处理不断增长的需求是编程中最困难的部分之一。也许最难处理的更改类型是从单线程程序迁移到需要多个并发执行线的程序。

让我通过一个例子来演示您可能如何遇到这个问题。假设我想实现康威生命游戏，这是有限状态自动机的经典示例。游戏规则很简单：有一个任意大小的二维网格，网格中的每个单元格都可以是活动的或空的：

```python
ALIVE = "*"
EMPTY = "-"
```

游戏一次只进行一个时钟滴答。每次滴答，每个单元格都会计算其周围八个单元格中有多少仍然是活动的。根据其邻居计数，单元格决定是继续存活、死亡还是再生。（我将在下面进一步解释具体规则。）下图显示了四代后 5x5 生命游戏网格，时间向右移动：

[Click here to view code image](#ch09_images#f0345-01)

```
0   |   1   |   2   |   3   |   4
----- | ----- | ----- | ----- | -----
-*--- | --*-- | --**- | --*-- | -----
--**- | --**- | -*--- | -*--- | -**--
---*- | --**- | --**- | --*-- | -----
----- | ----- | ----- | ----- | -----
```

我可以用一个简单的容器类来表示每个单元格的状态。该类必须具有允许我获取和设置任何坐标值的方法。边界外的坐标应该环绕，使网格像一个无限循环空间：

[Click here to view code image](#ch09_images#f0345-02)

```python
class Grid:
def __init__(self, height, width):
self.height = height
self.width = width
self.rows = []
for _ in range(self.height):
self.rows.append([EMPTY] * self.width)

def get(self, y, x):
return self.rows[y % self.height][x % self.width]

def set(self, y, x, state):
self.rows[y % self.height][x % self.width] = state

def __str__(self):
...
```

为了在实践中看到这个类，我可以创建一个 `Grid` 实例并将其初始状态设置为一个经典的形状，称为滑翔机 (glider)：

```python
grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)
print(grid)

>>>
---*-----
----*----
--***----
---------
---------
```

现在我需要一种方法来检索邻近单元格的状态。我可以通过一个辅助函数来做到这一点，该函数查询网格以获取有关其周围环境的信息，并返回活动邻居的数量。我使用一个简单的函数作为 `get_cell` 参数，而不是传递整个 `Grid` 实例，以减少耦合（有关此方法的更多信息，请参见 [Item 48](#ch07#ch07lev1sec1): “为简单接口接受函数而不是类”）：

[Click here to view code image](#ch09_images#f0346-01)

```python
def count_neighbors(y, x, get_cell):
n_ = get_cell(y - 1, x + 0)  # North
ne = get_cell(y - 1, x + 1)  # Northeast
e_ = get_cell(y + 0, x + 1)  # East
se = get_cell(y + 1, x + 1)  # Southeast
s_ = get_cell(y + 1, x + 0)  # South
sw = get_cell(y + 1, x - 1)  # Southwest
w_ = get_cell(y + 0, x - 1)  # West
nw = get_cell(y - 1, x - 1)  # Northwest
neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
count = 0
for state in neighbor_states:
if state == ALIVE:
count += 1
return count
```

现在我根据游戏的三个规则定义康威生命游戏的简单逻辑：如果一个单元格的邻居少于两个，则死亡；如果一个单元格的邻居多于三个，则死亡；或者如果一个空单元格恰好有三个邻居，则变为活动：

[Click here to view code image](#ch09_images#f0346-02)

```python
def game_logic(state, neighbors):
if state == ALIVE:
if neighbors < 2:
return EMPTY     # Die: Too few
elif neighbors > 3:
return EMPTY     # Die: Too many
else:
if neighbors == 3:
return ALIVE     # Regenerate
return state
```

我可以在另一个函数中连接 `count_neighbors` 和 `game_logic`，该函数会推进单元格的状态。此函数将在每一代被调用，以确定单元格的当前状态，检查其周围的邻近单元格，确定其下一个状态应该是什么，并相应地更新结果网格。同样，我使用 `set_cell` 的函数接口而不是传递 `Grid` 实例来使此代码更加解耦：

[Click here to view code image](#ch09_images#f0347-01)

```python
def step_cell(y, x, get_cell, set_cell):
state = get_cell(y, x)
neighbors = count_neighbors(y, x, get_cell)
next_state = game_logic(state, neighbors)
set_cell(y, x, next_state)
```

最后，我可以定义一个函数，该函数将整个单元格网格向前推进一个步骤，然后返回一个包含下一代状态的新网格。这里的重要细节是，我需要所有依赖函数都调用前一代 `Grid` 实例上的 `get_cell` 方法，并调用下一代 `Grid` 实例上的 `set` 方法。这就是我如何确保所有单元格同步移动，这是游戏工作方式的一个基本部分。由于我使用了 `get_cell` 和 `set_cell` 的函数接口而不是传递 `Grid` 实例，因此这很容易实现：

[Click here to view code image](#ch09_images#f0347-02)

```python
def simulate(grid):
next_grid = Grid(grid.height, grid.width)
for y in range(grid.height):
for x in range(grid.width):
step_cell(y, x, grid.get, next_grid.set)
return next_grid
```

现在我可以一次推进网格一代。您可以看到滑翔机如何根据 `game_logic` 函数中的简单规则在网格上向下和向右移动：

[Click here to view code image](#ch09_images#f0347-03)

```python
class ColumnPrinter:
...

columns = ColumnPrinter()
for i in range(5):
columns.append(str(grid))
grid = simulate(grid)

print(columns)

>>>
0     |     1     |     2     |     3     |     4
---*----- | --------- | --------- | --------- | ---------
----*---- | --*-*---- | ----*---- | ---*----- | ----*----
--***---- | ---**---- | --*-*---- | ----**--- | -----*---
--------- | ---*----- | ---**---- | ---**---- | ---***---
--------- | --------- | --------- | --------- | ---------
```

对于可以在单台机器上单线程运行的程序来说，这效果很好。但想象一下，如果程序的需要发生了变化——如我上面所暗示的——现在我需要在 `game_logic` 函数内部执行一些 I/O（例如，使用网络套接字）。例如，如果我正在构建一个大型多人在线游戏，其中状态转换由网格状态和通过 Internet 与其他玩家通信的组合决定，则可能需要这样做。

我如何扩展此实现以支持此类功能？最简单的方法是在 `game_logic` 函数中直接添加阻塞 I/O：

[Click here to view code image](#ch09_images#f0348-02)

```python
def game_logic(state, neighbors):
...
# Do some blocking input/output in here:
data = my_socket.recv(100)
...
```

此方法的问题在于它会减慢整个程序的速度。如果所需 I/O 的延迟为 100 毫秒（这对于跨大陆的往返互联网延迟来说是相当不错的），并且网格中有 45 个单元格，那么由于 `simulate` 函数中每个单元格的处理都是串行的，因此每一代将需要至少 4.5 秒来评估。这太慢了，会使游戏无法玩。它的扩展性也很差：如果我以后想将网格扩展到 10,000 个单元格，我将需要超过 15 分钟来评估每一代。

解决方案是并行执行 I/O，这样每一代大约需要 100 毫秒，而与网格大小无关。为每个工作单元（在此情况下为单元格）生成一个并发执行线的过程称为 _扇出 (fan-out)_。在协调过程中等待所有这些并发工作单元完成，然后再进行下一个阶段（在此情况下为一代）的过程称为 _扇入 (fan-in)_。

Python 提供了许多内置工具来实现具有不同权衡的扇出和扇入。您应该了解每种方法的优缺点，并根据情况选择最佳工具。有关详细信息，请参阅以下项目：[Item 72](#ch09#ch09lev1sec6): “避免为按需扇出创建新的 Thread 实例”，[Item 73](#ch09#ch09lev1sec7): “了解如何使用 Queue 进行并发需要重构”，[Item 74](#ch09#ch09lev1sec8): “当 Threads 对并发至关重要时，考虑 ThreadPoolExecutor”，以及 [Item 75](#ch09#ch09lev1sec9): “使用 Coroutines 实现高度并发的 I/O”。

#### 记住 (Things to Remember)

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 随着程序范围和复杂性的增加，它通常开始需要支持多个并发执行线。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 最常见的并发协调类型是扇出（生成新的并发单元）和扇入（等待现有并发单元完成）。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 有许多不同的方法来实现扇出和扇入。

### Item 72: 避免为按需扇出创建新的 `Thread` 实例 (Avoid Creating New `Thread` Instances for On-Demand Fan-out)

Threads 是在 Python 中执行并行 I/O 的自然首选工具（参见 [Item 68](#ch09#ch09lev1sec2): “使用 Threads 进行阻塞 I/O；避免并行”）。但是，当您尝试将它们用于扇出到许多并发执行线时，它们存在显著的缺点。

为了说明这一点，我将继续使用生命游戏示例（有关背景信息和下面各种函数和类的实现，请参见 [Item 71](#ch09#ch09lev1sec5): “知道何时需要并发”）。我将使用 threads 来解决 `game_logic` 函数中 I/O 引起的延迟问题。首先，threads 需要使用锁进行协调，以确保数据结构内的假设得到正确维护（有关详细信息，请参见 [Item 69](#ch09#ch09lev1sec3): “使用 Lock 防止 Threads 中的数据竞争”）。我可以创建一个 `Grid` 类的子类，该子类添加锁定行为，以便实例可以被多个 threads 同时使用：

[Click here to view code image](#ch09_images#f0349-01)

```python
from threading import Lock

ALIVE = "*"
EMPTY = "-"

class Grid:
...

class LockingGrid(Grid):
def __init__(self, height, width):
super().__init__(height, width)
self.lock = Lock()

def __str__(self):
with self.lock:
return super().__str__()

def get(self, y, x):
with self.lock:
return super().get(y, x)

def set(self, y, x, state):
with self.lock:
return super().set(y, x, state)
```

然后，我可以重新实现 `simulate` 函数以通过为每次调用 `step_cell` 创建一个线程来进行 _扇出_。线程将并行运行，并且不必等待彼此的 I/O。然后，我可以通过等待所有线程完成来 _扇入_，然后再进行下一代：

[Click here to view code image](#ch09_images#f0350-02)

```python
from threading import Thread

def count_neighbors(y, x, get_cell):
...

def game_logic(state, neighbors):
...
# Do some blocking input/output in here:
data = my_socket.recv(100)
...

def step_cell(y, x, get_cell, set_cell):
state = get_cell(y, x)
neighbors = count_neighbors(y, x, get_cell)
next_state = game_logic(state, neighbors)
set_cell(y, x, next_state)

def simulate_threaded(grid):
next_grid = LockingGrid(grid.height, grid.width)

threads = []
for y in range(grid.height):
for x in range(grid.width):
args = (y, x, grid.get, next_grid.set)
thread = Thread(target=step_cell, args=args)
thread.start()  # Fan-out
threads.append(thread)

for thread in threads:
thread.join()  # Fan-in

return next_grid
```

我可以使用与之前相同的 `step_cell` 实现和相同的驱动代码来运行此代码，只需更改两行以使用 `LockingGrid` 和 `simulate_threaded` 实现：

[Click here to view code image](#ch09_images#f0351-02)

```python
class ColumnPrinter:
...

grid = LockingGrid(5, 9)  # Changed
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)

columns = ColumnPrinter()
for i in range(5):
columns.append(str(grid))
grid = simulate_threaded(grid)  # Changed

print(columns)

>>>
0     |     1     |     2     |     3     |     4
---*----- | --------- | --------- | --------- | ---------
----*---- | --*-*---- | ----*---- | ---*----- | ----*----
--***---- | ---**---- | --*-*---- | ----**--- | -----*---
--------- | ---*----- | ---**---- | ---**---- | ---***---
--------- | --------- | --------- | --------- | ---------
```

这如预期般工作，I/O 现在已在线程之间并行化。但是，此代码存在三个主要问题：

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `Thread` 实例需要特殊工具（即 `Lock` 对象）才能安全地进行协调。这使得使用 threads 的代码比之前的过程式单线程代码更难理解。这种复杂性使得 threaded 代码随着时间的推移更难扩展和维护。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Threads 需要大量内存——每个执行线程大约 8 MB。在许多计算机上，此示例中所需的 45 个线程的内存量无关紧要。但是，如果游戏网格需要增长到 10,000 个单元格，我将需要创建那么多线程，这占用了如此多的内存（80 GB），以至于程序无法安装在我的机器上。尽管某些操作系统会采取技巧来延迟线程的完整内存分配，直到其执行堆栈足够深，但仍然存在运行每个并发活动的线程可能无法可靠工作的风险。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 启动线程成本很高，并且由于线程之间的上下文切换开销，线程在运行时会产生负面性能影响。在上面的代码中，所有线程都在每一代游戏中启动和停止，这带来了如此多的开销，以至于它会增加延迟，超过预期的 100 毫秒 I/O 时间。

如果出现问题，此代码也将非常难以调试。例如，假设 `game_logic` 函数引发了异常，这由于 I/O 的普遍不稳定性而极有可能发生：

[Click here to view code image](#ch09_images#f0352-01)

```python
def game_logic(state, neighbors):
...
raise OSError("Problem with I/O")
...
```

我可以通过运行指向此函数的 `Thread` 实例并将程序的 `sys.stderr` 输出重定向到内存中的 `StringIO` 缓冲区来测试这会发生什么：

[Click here to view code image](#ch09_images#f0352-02)

```python
import contextlib
import io

fake_stderr = io.StringIO()
with contextlib.redirect_stderr(fake_stderr):
thread = Thread(target=game_logic, args=(ALIVE, 3))
thread.start()
thread.join()

print(fake_stderr.getvalue())

>>>
Exception in thread Thread-226 (game_logic):
Traceback (most recent call last):
File "threading.py", line 1039, in _bootstrap_inner
self.run()
~~~~~~~~^^
File "threading.py", line 990, in run
self._target(*self._args, **self._kwargs)
~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "example.py", line 205, in game_logic
raise OSError('Problem with I/O')
OSError: Problem with I/O
```

预期会发生 `OSError` 异常，但创建线程并调用 `join` 的代码不知何故不受影响。怎么会这样？原因是 `Thread` 类将由 `target` 函数引发的任何异常独立捕获，然后将其 traceback 写入 `sys.stderr`。这些异常永远不会重新引发给首先启动线程的调用者。

考虑到所有这些问题，很明显，如果您需要不断创建和完成新的并发函数，threads 不是解决方案。Python 提供了其他更适合的解决方案（参见 [Item 73](#ch09#ch09lev1sec7): “了解如何使用 Queue 进行并发需要重构”，[Item 74](#ch09#ch09lev1sec8): “当 Threads 对并发至关重要时，考虑 ThreadPoolExecutor”，以及 [Item 75](#ch09#ch09lev1sec9): “使用 Coroutines 实现高度并发的 I/O”）。

#### 记住 (Things to Remember)

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Threads 有许多缺点：如果您需要大量 threads，它们的启动和运行成本很高，每个线程都需要大量内存，并且它们需要 `Lock` 实例等特殊工具进行协调。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `Thread` 没有内置的方法将异常重新引发给启动它的代码或等待它的另一个线程，这极大地阻碍了调试。

### Item 73: 了解如何使用 `Queue` 进行并发需要重构 (Understand How Using `Queue` for Concurrency Requires Refactoring)

在上一项（参见 [Item 72](#ch09#ch09lev1sec6): “避免为按需扇出创建新的 Thread 实例”）中，我涵盖了在生命游戏示例中使用 `Thread` 来解决并行 I/O 问题的缺点（有关背景信息和下面各种函数和类的实现，请参见 [Item 71](#ch09#ch09lev1sec5): “知道何时需要并发”）。

下一个要尝试的方法是使用 `queue` 内置模块中的 `Queue` 类实现一个 threaded 管道（有关背景信息，请参见 [Item 70](#ch09#ch09lev1sec4): “使用 Queue 协调 Threads 之间的工作”；我在下面的示例代码中依赖于 `StoppableWorker` 的实现）。

这是通用方法：与其为生命游戏的每一代创建每个单元格一个线程，不如预先创建固定数量的 worker 线程，并让它们按需执行并行 I/O。这将使我的资源使用保持在可控范围内，并消除频繁启动新线程的开销。

为此，我需要两个 `Queue` 实例来与执行 `game_logic` 函数的 worker 线程进行通信：

```python
from queue import Queue

in_queue = Queue()
out_queue = Queue()
```

我可以启动多个线程，这些线程将从 `in_queue` 中消耗项目，通过调用 `game_logic` 处理它们，并将结果放入 `out_queue`。这些线程将并发运行，从而实现并行 I/O 并减少每一代的延迟：

[Click here to view code image](#ch09_images#f0354-01)

```python
from threading import Thread

class StoppableWorker(Thread):
...

def game_logic(state, neighbors):
...
# Do some blocking input/output in here:
data = my_socket.recv(100)
...

def game_logic_thread(item):
y, x, state, neighbors = item
try:
next_state = game_logic(state, neighbors)
except Exception as e:
next_state = e
return (y, x, next_state)

# Start the threads upfront
threads = []
for _ in range(5):
thread = StoppableWorker(
game_logic_thread, in_queue, out_queue)
thread.start()
threads.append(thread)
```

现在我可以重新定义 `simulate` 函数，通过与这些队列交互来请求状态转换决策并接收相应的响应。将项目添加到 `in_queue` 是 _扇出_，从 `out_queue` 中消耗项目直到其排空是 _扇入_：

[Click here to view code image](#ch09_images#f0355-02)

```python
ALIVE = "*"
EMPTY = "-"

class SimulationError(Exception):
pass

class Grid:
...

def count_neighbors(y, x, get_cell):
...

def simulate_pipeline(grid, in_queue, out_queue):
for y in range(grid.height):
for x in range(grid.width):
state = grid.get(y, x)
neighbors = count_neighbors(y, x, grid.get)
in_queue.put((y, x, state, neighbors))  # Fan-out

in_queue.join()
item_count = out_queue.qsize()

next_grid = Grid(grid.height, grid.width)
for _ in range(item_count):
item = out_queue.get()                      # Fan-in
y, x, next_state = item
if isinstance(next_state, Exception):
raise SimulationError(y, x) from next_state
next_grid.set(y, x, next_state)

return next_grid
```

`Grid.get` 和 `Grid.set` 的调用都发生在新的 `simulate_pipeline` 函数中，这意味着我可以使用单线程的 `Grid` 实现而不是需要 `Lock` 实例进行同步的实现（有关背景信息，请参见 [Item 69](#ch09#ch09lev1sec3): “使用 Lock 防止 Threads 中的数据竞争”）。

此代码也比上一项中使用的 `Thread` 方法更容易调试。如果在 `game_logic` 函数中执行 I/O 时发生异常，它将被周围的 `game_logic_thread` 函数捕获，传播到 `out_queue`，然后重新引发到主线程：

[Click here to view code image](#ch09_images#f0356-01)

```python
def game_logic(state, neighbors):
...
raise OSError("Problem with I/O in game_logic")
...

simulate_pipeline(Grid(1, 1), in_queue, out_queue)

>>>
Traceback ...
OSError: Problem with I/O in game_logic

The above exception was the direct cause of the following
exception:

Traceback ...
SimulationError: (0, 0)
```

通过在循环中调用 `simulate_pipeline`，我可以驱动此多线程管道进行重复的代：

[Click here to view code image](#ch09_images#f0356-02)

```python
class ColumnPrinter:
...

grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)

columns = ColumnPrinter()
for i in range(5):
columns.append(str(grid))
grid = simulate_pipeline(grid, in_queue, out_queue)

print(columns)

in_queue.shutdown()
in_queue.join()

for thread in threads:
thread.join()

>>>
0     |     1     |     2     |     3     |     4
---*----- | --------- | --------- | --------- | ---------
----*---- | --*-*---- | ----*---- | ---*----- | ----*----
--***---- | ---**---- | --*-*---- | ----**--- | -----*---
--------- | ---*----- | ---**---- | ---**---- | ---***---
--------- | --------- | --------- | --------- | ---------
```

结果与之前相同。尽管我解决了内存爆炸问题、启动成本和与单独使用 threads 相关的调试问题，但仍有许多问题存在：

*   `simulate_pipeline` 函数比上一项中的 `simulate_threaded` 方法更难理解。
*   需要额外的支持功能（例如 `StoppableWorker`）来使代码更易于阅读，但代价是增加了复杂性。
*   我必须根据对工作负载的预期预先指定并行度——运行 `game_logic_thread` 的线程数——而不是让系统自动按需扩展并行度。
*   为了启用调试，我必须手动捕获 worker 线程中的异常，将它们通过队列传播，然后重新在主线程中引发它们。

然而，此代码的最大问题在于，如果需求再次更改，它会变得显而易见。想象一下，后来我需要在 `count_neighbors` 函数中执行 I/O，除了 `game_logic` 中已经需要的 I/O 之外：

[Click here to view code image](#ch09_images#f0357-02)

```python
def count_neighbors(y, x, get_cell):
...
# Do some blocking input/output in here:
data = my_socket.recv(100)
...
```

为了使其可并行化，我需要向管道添加另一个阶段，该阶段以线程方式运行 `count_neighbors`。我需要确保异常能在 worker 线程和主线程之间正确传播。并且我需要使用 `Grid` 类的锁来确保 worker 线程之间的安全同步（有关背景信息和 `LockingGrid` 的实现，请参见 [Item 72](#ch09#ch09lev1sec6): “避免为按需扇出创建新的 Thread 实例”）：

[Click here to view code image](#ch09_images#f0358-01)

```python
def count_neighbors_thread(item):
y, x, state, get_cell = item
try:
neighbors = count_neighbors(y, x, get_cell)
except Exception as e:
neighbors = e
return (y, x, state, neighbors)

def game_logic_thread(item):
y, x, state, neighbors = item
if isinstance(neighbors, Exception):
next_state = neighbors
else:
try:
next_state = game_logic(state, neighbors)
except Exception as e:
next_state = e
return (y, x, next_state)

class LockingGrid(Grid):
...
```

我需要为 `count_neighbors_thread` worker 和相应的 `Thread` 实例创建另一组 `Queue` 实例：

[Click here to view code image](#ch09_images#f0358-02)

```python
in_queue = Queue()
logic_queue = Queue()
out_queue = Queue()

threads = []

for _ in range(5):
thread = StoppableWorker(
count_neighbors_thread, in_queue, logic_queue
)
thread.start()
threads.append(thread)

for _ in range(5):
thread = StoppableWorker(
game_logic_thread, logic_queue, out_queue
)
thread.start()
threads.append(thread)
```

最后，我需要更新 `simulate_pipeline` 以协调管道中的多个阶段，并确保工作能够正确地扇出和扇入：

[Click here to view code image](#ch09_images#f0359-02)

```python
def simulate_phased_pipeline(grid, in_queue, logic_queue,
out_queue):
for y in range(grid.height):
for x in range(grid.width):
state = grid.get(y, x)
item = (y, x, state, grid.get)
in_queue.put(item)            # Fan-out

in_queue.join()
logic_queue.join()                    # Pipeline sequencing
item_count = out_queue.qsize()

next_grid = LockingGrid(grid.height, grid.width)
for _ in range(item_count):
y, x, next_state = out_queue.get()  # Fan-in
if isinstance(next_state, Exception):
raise SimulationError(y, x) from next_state
next_grid.set(y, x, next_state)

return next_grid
```

使用这些更新的实现，我现在可以端到端运行多阶段管道：

[Click here to view code image](#ch09_images#f0359-03)

```python
grid = LockingGrid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)

columns = ColumnPrinter()
for i in range(5):
columns.append(str(grid))
grid = simulate_phased_pipeline(
grid, in_queue, logic_queue, out_queue
)

print(columns)

in_queue.shutdown()
in_queue.join()

logic_queue.shutdown()
logic_queue.join()

for thread in threads:
thread.join()

>>>
0     |     1     |     2     |     3     |     4
---*----- | --------- | --------- | --------- | ---------
----*---- | --*-*---- | ----*---- | ---*----- | ----*----
--***---- | ---**---- | --*-*---- | ----**--- | -----*---
--------- | ---*----- | ---**---- | ---**---- | ---***---
--------- | --------- | --------- | --------- | ---------
```

再次，这如预期般工作，但它需要大量的更改和样板代码。这里的重点是 `Queue` 确实可以解决扇出和扇入问题，但复杂性非常高。尽管使用 `Queue` 比单独使用 `Thread` 实例更好，但它仍然远不如使用 Python 提供的其他工具（参见 [Item 74](#ch09#ch09lev1sec8): “当 Threads 对并发至关重要时，考虑 ThreadPoolExecutor” 和 [Item 75](#ch09#ch09lev1sec9): “使用 Coroutines 实现高度并发的 I/O”）。

#### 记住 (Things to Remember)

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用具有固定数量 worker 线程的 `Queue` 实例可以提高使用 threads 的扇出和扇入的可伸缩性。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 将现有代码重构为使用 `Queue` 需要大量工作，特别是当需要多个管道阶段时。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用具有固定数量 worker 线程的 `Queue` 会从根本上限制程序可以利用的 I/O 并行化的总量，与 Python 的其他内置功能和模块提供的更动态的方法相比。

### Item 74: 当 Threads 对并发至关重要时，考虑 `ThreadPoolExecutor` (Consider `ThreadPoolExecutor` When Threads Are Necessary for Concurrency)

Python 包含 `concurrent.futures` 内置模块，该模块提供了 `ThreadPoolExecutor` 类。它结合了 `Thread`（参见 [Item 72](#ch09#ch09lev1sec6): “避免为按需扇出创建新的 Thread 实例”）和 `Queue`（参见 [Item 73](#ch09#ch09lev1sec7): “了解如何使用 Queue 进行并发需要重构”）在生命游戏示例中解决并行 I/O 问题的最佳方法（有关背景信息和下面各种函数和类的实现，请参见 [Item 71](#ch09#ch09lev1sec5): “知道何时需要并发”）：

[Click here to view code image](#ch09_images#f0361-01)

```python
ALIVE = "*"
EMPTY = "-"

class Grid:
...

class LockingGrid(Grid):
...

def count_neighbors(y, x, get_cell):
...

def game_logic(state, neighbors):
...
# Do some blocking input/output in here:
data = my_socket.recv(100)
...

def step_cell(y, x, get_cell, set_cell):
state = get_cell(y, x)
neighbors = count_neighbors(y, x, get_cell)
next_state = game_logic(state, neighbors)
set_cell(y, x, next_state)
```

与其为每个生命游戏网格单元创建新的 `Thread` 实例，不如通过将函数提交给将在单独线程中运行的 executor 来进行 _扇出_。稍后，您可以等待所有任务的结果以进行 _扇入_：

[Click here to view code image](#ch09_images#f0362-01)

```python
from concurrent.futures import ThreadPoolExecutor

def simulate_pool(pool, grid):
next_grid = LockingGrid(grid.height, grid.width)

futures = []
for y in range(grid.height):
for x in range(grid.width):
args = (y, x, grid.get, next_grid.set)
future = pool.submit(step_cell, *args)  # Fan-out
futures.append(future)

for future in futures:
future.result()                             # Fan-in

return next_grid
```

Executor 使用的 threads 可以预先分配，这意味着我不必在每次执行 `simulate_pool` 时都支付启动成本。我还可以指定用于池的最大线程数——使用 `max_workers` 参数——以防止与并行 I/O 问题的朴素 `Thread` 解决方案（即每个单元一个线程）相关的内存爆炸问题：

[Click here to view code image](#ch09_images#f0362-02)

```python
class ColumnPrinter:
...

grid = LockingGrid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)

columns = ColumnPrinter()
with ThreadPoolExecutor(max_workers=10) as pool:
for i in range(5):
columns.append(str(grid))
grid = simulate_pool(pool, grid)

print(columns)

>>>
0     |     1     |     2     |     3     |     4
---*----- | --------- | --------- | --------- | ---------
----*---- | --*-*---- | ----*---- | ---*----- | ----*----
--***---- | ---**---- | --*-*---- | ----**--- | -----*---
--------- | ---*----- | ---**---- | ---**---- | ---***---
--------- | --------- | --------- | --------- | ---------
```

`ThreadPoolExecutor` 类最棒的部分是它在调用 `submit` 方法返回的 `Future` 实例上的 `result` 方法时，会自动将异常传播回调用者：

[Click here to view code image](#ch09_images#f0363-02)

```python
def game_logic(state, neighbors):
...
raise OSError("Problem with I/O")
...

with ThreadPoolExecutor(max_workers=10) as pool:
task = pool.submit(game_logic, ALIVE, 3)
task.result()

>>>
Traceback ...
OSError: Problem with I/O
```

如果我需要为 `count_neighbors` 函数提供 I/O 并行性，除了 `game_logic` 之外，不需要修改程序，因为 `ThreadPoolExecutor` 已经在 `step_cell` 中并发运行这些函数。如果需要，甚至可以通过使用相同的接口来实现 CPU 并行性（参见 [Item 79](#ch09#ch09lev1sec13): “考虑 concurrent.futures 以实现真正的并行”）。

然而，仍然存在的问题是 `ThreadPoolExecutor` 提供的 I/O 并行化程度有限。即使我使用 `max_workers` 参数为 100，如果我需要 10,000 多个单元格的网格需要同时进行 I/O，此解决方案仍然无法扩展。`ThreadPoolExecutor` 是没有异步解决方案（例如，阻塞文件系统操作）的情况下的良好选择，但在许多情况下，有更好的方法来最大化 I/O 并行性（参见 [Item 75](#ch09#ch09lev1sec9): “使用 Coroutines 实现高度并发的 I/O”）。

#### 记住 (Things to Remember)

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `ThreadPoolExecutor` 能够实现简单的 I/O 并行化，只需少量重构。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 您可以使用 `ThreadPoolExecutor` 来避免每次需要扇出并发时产生的线程启动成本。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `ThreadPoolExecutor` 通过自动在线程边界上传播异常，使 threaded 代码更易于调试。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 尽管 `ThreadPoolExecutor` 消除了直接使用 threads 的潜在内存爆炸问题，但它也通过要求预先指定 `max_workers` 来限制 I/O 并行性。

### Item 75: 使用 Coroutines 实现高度并发的 I/O (Achieve Highly Concurrent I/O with Coroutines)

之前的项目尝试以不同程度的成功解决了生命游戏的并行 I/O 问题（有关背景信息和下面各种函数和类的实现，请参见 [Item 71](#ch09#ch09lev1sec5): “知道何时需要并发”）。所有其他方法在处理数千个并发函数的能力方面都存在不足（参见 [Item 72](#ch09#ch09lev1sec6): “避免为按需扇出创建新的 Thread 实例”，[Item 73](#ch09#ch09lev1sec7): “了解如何使用 Queue 进行并发需要重构”，以及 [Item 74](#ch09#ch09lev1sec8): “当 Threads 对并发至关重要时，考虑 ThreadPoolExecutor”）。

Python 通过 coroutines 来满足对高度并发 I/O 的需求。_Coroutines_ 使您能够在 Python 程序中拥有大量看似同时执行的函数。它们使用 `async` 和 `await` 关键字以及驱动生成器的相同基础结构来实现（参见 [Item 43](#ch06#ch06lev1sec4): “考虑使用 Generators 而不是返回列表”，[Item 46](#ch06#ch06lev1sec7): “将 Iterators 作为参数传递给 Generators 而不是调用 send 方法”，以及 [Item 47](#ch06#ch06lev1sec8): “使用类而不是 Generator 的 throw 方法管理迭代状态转换”）。

启动 coroutine 的成本是函数调用。一旦 coroutine 处于活动状态，它就会消耗少于 1 KB 的内存，直到它耗尽。与 threads 类似，coroutines 是独立的函数，可以从其环境中消耗输入并产生结果输出。区别在于 coroutines 在每个 `await` 表达式处暂停，并在挂起的 _awaitable_ 解析后恢复执行一个 `async` 函数（类似于 `yield` 在生成器中的行为）。

当许多独立的 `async` 函数以锁定步调推进时，它们都似乎同时运行，模仿了 Python threads 的并发行为。然而，coroutines 在没有内存开销、启动和上下文切换成本以及 threads 所需的复杂锁定和同步代码的情况下实现了这一点。驱动 coroutines 的神奇机制是 _事件循环 (event loop)_，它可以高效地执行高度并发的 I/O，同时在适当编写的函数之间快速交错执行。

我可以使用 coroutines 来实现生命游戏。我的目标是允许在 `game_logic` 函数中执行 I/O，同时克服先前项目中 `Thread`、`Queue` 和 `ThreadPoolExecutor` 方法的问题。为此，首先我通过使用 `async def` 而不是 `def` 定义 `game_logic` 函数来指示它是一个 coroutine。这将允许我使用 `await` 语法进行 I/O，例如从套接字进行异步 `read`：

[Click here to view code image](#ch09_images#f0365-01)

```python
ALIVE = "*"
EMPTY = "-"

class Grid:
...

def count_neighbors(y, x, get_cell):
...

async def game_logic(state, neighbors):
...
# Do some input/output in here:
data = await my_socket.read(50)
...
```

类似地，我可以通过在其定义中添加 `async` 并使用 `await` 来调用 `game_logic` 函数，将 `step_cell` 转换为 coroutine：

[Click here to view code image](#ch09_images#f0365-02)

```python
async def step_cell(y, x, get_cell, set_cell):
state = get_cell(y, x)
neighbors = count_neighbors(y, x, get_cell)
next_state = await game_logic(state, neighbors)
set_cell(y, x, next_state)
```

`simulate` 函数也需要成为一个 coroutine：

[Click here to view code image](#ch09_images#f0365-03)

```python
import asyncio

async def simulate(grid):
next_grid = Grid(grid.height, grid.width)

tasks = []
for y in range(grid.height):
for x in range(grid.width):

task = step_cell(
y, x, grid.get, next_grid.set)        # Fan-out
tasks.append(task)

await asyncio.gather(*tasks)                      # Fan-in

return next_grid
```

`simulate` 函数的 coroutine 版本需要一些解释：

*   调用 `step_cell` 不会立即运行该函数。相反，它返回一个 `coroutine` 实例，该实例稍后可用于 `await` 表达式。这类似于使用 `yield` 的生成器函数在调用时返回生成器实例而不是立即执行。延迟执行是导致 _扇出_ 的机制。
*   来自 `asyncio` 内置库的 `gather` 函数是导致 _扇入_ 的原因。对 `gather` 的 `await` 表达式指示事件循环并发运行 `step_cell` coroutines，并在所有 coroutines 完成后恢复 `simulate` coroutine 的执行（有关使用 `asyncio.TaskGroup` 的另一种方法，请参见 [Item 77](#ch09#ch09lev1sec11): “混合使用 Threads 和 Coroutines 以简化向 asyncio 的过渡”）。
*   由于所有执行都发生在单个线程内，因此不需要 `Grid` 实例的锁。I/O 通过 `asyncio` 提供的事件循环作为并行化的一部分。

最后，我可以通过对原始示例进行一行更改来驱动此代码。这依赖于 `asyncio.run` 函数在事件循环中执行 `simulate` coroutine 并执行其依赖的 I/O：

[Click here to view code image](#ch09_images#f0366-02)

```python
class ColumnPrinter:
...

grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)

columns = ColumnPrinter()
for i in range(5):
columns.append(str(grid))
grid = asyncio.run(simulate(grid))  # Run the event loop

print(columns)

>>>
0     |     1     |     2     |     3     |     4
---*----- | --------- | --------- | --------- | ---------
----*---- | --*-*---- | ----*---- | ---*----- | ----*----
--***---- | ---**---- | --*-*---- | ----**--- | -----*---
--------- | ---*----- | ---**---- | ---**---- | ---***---
--------- | --------- | --------- | --------- | ---------
```

结果与之前相同。所有与 threads 相关的开销都已消除。而 `Queue` 和 `ThreadPoolExecutor` 方法在异常处理方面受到限制——它们只是跨线程边界重新引发异常——使用 coroutines，我甚至可以使用交互式调试器逐行单步执行异常处理代码（有关背景信息，请参见 [Item 114](#ch13#ch13lev1sec7): “考虑使用 pdb 进行交互式调试”）。

稍后，如果我的需求发生变化，并且我还需要在 `count_neighbors` 中执行 I/O，我可以通过在现有函数和调用站点添加 `async` 和 `await` 关键字来轻松实现这一点，而无需像使用 `Thread` 或 `Queue` 实例那样进行重构（参见 [Item 76](#ch09#ch09lev1sec10): “了解如何将 Threaded I/O 移植到 asyncio” 的另一个示例）：

[Click here to view code image](#ch09_images#f0367-02)

```python
async def count_neighbors(y, x, get_cell):
...

async def step_cell(y, x, get_cell, set_cell):
state = get_cell(y, x)
neighbors = await count_neighbors(y, x, get_cell)
next_state = await game_logic(state, neighbors)
set_cell(y, x, next_state)

grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)

columns = ColumnPrinter()
for i in range(5):
columns.append(str(grid))
grid = asyncio.run(simulate(grid))

print(columns)

>>>
0     |     1     |     2     |     3     |     4
---*----- | --------- | --------- | --------- | ---------
----*---- | --*-*---- | ----*---- | ---*----- | ----*----
--***---- | ---**---- | --*-*---- | ----**--- | -----*---
--------- | ---*----- | ---**---- | ---**---- | ---***---
--------- | --------- | --------- | --------- | ---------
```

Coroutines 的优点在于它们将代码与外部环境（即 I/O）的指令与执行您意愿的实现（即事件循环）分离。它们让您可以专注于您实际要做的逻辑，而不是浪费时间试图弄清楚如何并发地实现您的目标。

#### 记住 (Things to Remember)

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `async` 关键字定义的函数称为 coroutines。调用者可以使用 `await` 关键字接收依赖 coroutine 的结果。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Coroutines 提供了一种高效的方法来同时运行数万个函数。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Coroutines 可以使用扇出和扇入来并行化 I/O，同时克服了在 threads 中执行 I/O 所带来的所有问题。

### Item 76: 了解如何将 Threaded I/O 移植到 `asyncio` (Know How to Port Threaded I/O to `asyncio`)

一旦您了解了 coroutines 的优势（参见 [Item 75](#ch09#ch09lev1sec9): “使用 Coroutines 实现高度并发的 I/O”），将现有代码库移植到使用它们可能看起来令人生畏。幸运的是，Python 对异步执行的支持已与语言深度集成。这使得将执行阻塞 I/O 和 threads 的代码迁移到 coroutines 和异步 I/O 变得简单明了。

例如，假设我有一个用于玩“猜数字”游戏的基于 TCP 的服务器。服务器接受 `lower` 和 `upper` 参数，这些参数确定要考虑的数字范围。然后，服务器根据客户端的请求返回该范围内的整数值的猜测。最后，服务器收集客户端关于每个数字是更接近（更热）还是更远（更冷）于客户端的秘密数字的报告。

构建此类客户端/服务器系统的最常见方法是使用阻塞 I/O 和 threads（参见 [Item 68](#ch09#ch09lev1sec2): “使用 Threads 进行阻塞 I/O；避免并行”）。为此，我需要一个可以管理消息发送和接收的辅助类。就我而言，每行发送或接收的消息代表一个要处理的命令：

[Click here to view code image](#ch09_images#f0369-01)

```python
class EOFError(Exception):
pass

class Connection:
def __init__(self, connection):
self.connection = connection
self.file = connection.makefile("rb")

def send(self, command):
line = command + "\n"
data = line.encode()
self.connection.send(data)

def receive(self):
line = self.file.readline()
if not line:
raise EOFError("Connection closed")
return line[:-1].decode()
```

服务器实现为一个类，该类一次处理一个连接并维护游戏的会话状态：

[Click here to view code image](#ch09_images#f0369-02)

```python
import random

WARMER = "Warmer"
COLDER = "Colder"
SAME = "Same"
UNSURE = "Unsure"
CORRECT = "Correct"

class UnknownCommandError(Exception):
pass

class ServerSession(Connection):
def __init__(self, *args):
super().__init__(*args)
self.clear_state()
```

它有一个主要方法来处理来自客户端的传入命令，并根据需要将其分派到方法。这里我使用 `match` 语句来解析半结构化数据（有关详细信息，请参见 [Item 9](#ch01#ch01lev1sec9): “考虑使用 match 进行解构式流程控制；当 if 语句足够时避免使用”）：

[Click here to view code image](#ch09_images#f0370-01)

```python
def loop(self):
while command := self.receive():
match command.split(" "):
case "PARAMS", lower, upper:
self.set_params(lower, upper)
case ["NUMBER"]:
self.send_number()
case "REPORT", decision:
self.receive_report(decision)
case ["CLEAR"]:
self.clear_state()
case _:
raise UnknownCommandError(command)
```

第一个命令设置服务器正在猜测的数字的下限和上限：

[Click here to view code image](#ch09_images#f0370-02)

```python
def set_params(self, lower, upper):
self.clear_state()
self.lower = int(lower)
self.upper = int(upper)
```

第二个命令根据存储在 `ServerSession` 实例中的先前状态进行新的猜测。具体来说，此代码确保服务器在每次参数分配时永远不会尝试猜测相同的数字两次：

[Click here to view code image](#ch09_images#f0370-03)

```python
def next_guess(self):
if self.secret is not None:
return self.secret

while True:
guess = random.randint(self.lower, self.upper)
if guess not in self.guesses:
return guess

def send_number(self):
guess = self.next_guess()
self.guesses.append(guess)
self.send(format(guess))
```

第三个命令接收来自客户端的关于猜测是更热、更冷、相同还是正确的决定，并相应地更新 `ServerSession` 状态：

[Click here to view code image](#ch09_images#f0371-01)

```python
def receive_report(self, decision):
last = self.guesses[-1]
if decision == CORRECT:
self.secret = last

print(f"Server: {last} is {decision}")
```

最后一个命令清除状态以结束游戏，无论游戏是否成功：

```python
def clear_state(self):
self.lower = None
self.upper = None
self.secret = None
self.guesses = []
```

通过使用 `with` 语句确保服务器端状态得到正确管理来启动游戏（有关背景信息，请参见 [Item 82](#ch10#ch10lev1sec3): “考虑使用 contextlib 和 with 语句实现可重用的 try/finally 行为” 和 [Item 78](#ch09#ch09lev1sec12): “使用 async-Friendly Worker Threads 最大化 asyncio 事件循环的响应能力” 的另一个示例）。此 `new_game` 函数发送第一个和最后一个命令到服务器，并提供一个上下文对象供游戏期间使用：

[Click here to view code image](#ch09_images#f0371-02)

```python
import contextlib

@contextlib.contextmanager
def new_game(connection, lower, upper, secret):
print(
f"Guess a number between {lower} and {upper}!"
f" Shhhhh, it's {secret}."
)
connection.send(f"PARAMS {lower} {upper}")
try:
yield ClientSession(
connection.send,
connection.receive,
secret,
)
finally:
connection.send("CLEAR")
```

我使用一个有状态的类，其中包含游戏操作的辅助方法和用于管理每个游戏会话的引用（有关为什么我显式传递 `send` 和 `receive` 的信息，请参见 [Item 48](#ch07#ch07lev1sec1): “为简单接口接受函数而不是类”）：

[Click here to view code image](#ch09_images#f0372-01)

```python
import math

class ClientSession:
def __init__(self, send, receive, secret):
self.send = send
self.receive = receive
self.secret = secret
self.last_distance = None
```

通过一个实现第二个命令的方法，从服务器请求新猜测：

```python
def request_number(self):
self.send("NUMBER")
data = self.receive()
return int(data)
```

通过第三个命令报告服务器每次猜测是更热还是更冷：

[Click here to view code image](#ch09_images#f0372-02)

```python
def report_outcome(self, number):
new_distance = math.fabs(number - self.secret)

if new_distance == 0:
decision = CORRECT
elif self.last_distance is None:
decision = UNSURE
elif new_distance < self.last_distance:
decision = WARMER
elif new_distance > self.last_distance:
decision = COLDER
else:
decision = SAME

self.last_distance = new_distance

self.send(f"REPORT {decision}")
return decision
```

游戏会话对象可以被迭代（有关背景信息，请参见 [Item 21](#ch03#ch03lev1sec5): “迭代参数时要谨慎”），以反复进行新的、唯一的猜测，直到找到正确答案：

[Click here to view code image](#ch09_images#f0373-01)

```python
def __iter__(self):
while True:
number = self.request_number()
decision = self.report_outcome(number)
yield number, decision
if decision == CORRECT:
return
```

我可以通过让一个线程监听套接字并启动其他线程来处理每个新客户端连接来运行服务器：

[Click here to view code image](#ch09_images#f0373-02)

```python
import socket
from threading import Thread

def handle_connection(connection):
with connection:
session = ServerSession(connection)
try:
session.loop()
except EOFError:
pass

def run_server(address):
with socket.socket() as listener:
listener.bind(address)
listener.listen()
while True:
connection, _ = listener.accept()
thread = Thread(
target=handle_connection,
args=(connection,),
daemon=True,
)
thread.start()
```

客户端在主线程中运行，并将猜测游戏的结果返回给调用者。也许有点笨拙，这段代码使用了各种 Python 语言特性（`for` 循环、`with` 语句、生成器、推导式、迭代器协议），以便下面我可以展示将它们移植到 coroutines 所需的内容：

[Click here to view code image](#ch09_images#f0374-01)

```python
def run_client(address):
with socket.create_connection(address) as server_sock:
server = Connection(server_sock)

with new_game(server, 1, 5, 3) as session:
results = [outcome for outcome in session]

with new_game(server, 10, 15, 12) as session:
for outcome in session:
results.append(outcome)

with new_game(server, 1, 3, 2) as session:
it = iter(session)
while True:
try:
outcome = next(it)
except StopIteration:
break
else:
results.append(outcome)

return results
```

最后，我可以将所有这些内容组合起来，并确认它按预期工作：

[Click here to view code image](#ch09_images#f0374-02)

```python
def main():
address = ("127.0.0.1", 1234)
server_thread = Thread(
target=run_server, args=(address,), daemon=True
)
server_thread.start()

results = run_client(address)
for number, outcome in results:
print(f"Client: {number} is {outcome}")

main()

>>>
Guess a number between 1 and 5! Shhhhh, it's 3.
Server: 4 is Unsure
Server: 1 is Colder
Server: 5 is Same
Server: 3 is Correct
Guess a number between 10 and 15! Shhhhh, it's 12.
Server: 11 is Unsure
Server: 10 is Colder
Server: 12 is Correct
Guess a number between 1 and 3! Shhhhh, it's 2.
Server: 3 is Unsure
Server: 2 is Correct
Client: 4 is Unsure
Client: 1 is Colder
Client: 5 is Same
Client: 3 is Correct
Client: 11 is Unsure
Client: 10 is Colder
Client: 12 is Correct
Client: 3 is Unsure
Client: 2 is Correct
```

将此示例转换为使用 `async`、`await` 和 `asyncio` 内置模块需要多少工作？

首先，我需要将我的 `Connection` 类更新为提供 coroutine 方法而不是阻塞 I/O 方法来发送和接收。我已在每行更改处添加了 `# Changed` 注释，以清楚地说明此新示例与上述代码之间的差异：

[Click here to view code image](#ch09_images#f0375-02)

```python
class AsyncConnection:
def __init__(self, reader, writer):      # Changed
self.reader = reader                 # Changed
self.writer = writer                 # Changed

async def send(self, command):
line = command + "\n"
data = line.encode()
self.writer.write(data)              # Changed
await self.writer.drain()            # Changed

async def receive(self):
line = await self.reader.readline()  # Changed
if not line:
raise EOFError("Connection closed")
return line[:-1].decode()
```

我可以创建另一个有状态的类来表示单个连接的服务器会话状态。这里唯一的更改是类的名称以及从 `AsyncConnection` 而不是 `Connection` 继承：

[Click here to view code image](#ch09_images#f0376-01)

```python
class AsyncServerSession(AsyncConnection):  # Changed
def __init__(self, *args):
...
```

服务器命令处理循环的主要入口点只需要最少的更改即可成为 coroutine：

[Click here to view code image](#ch09_images#f0376-02)

```python
async def loop(self):                       # Changed
while command := await self.receive():  # Changed
match command.split(" "):
case "PARAMS", lower, upper:
self.set_params(lower, upper)
case ["NUMBER"]:
await self.send_number()    # Changed
case "REPORT", decision:
self.receive_report(decision)
case ["CLEAR"]:
self.clear_state()
case _:
raise UnknownCommandError(command)
```

处理第一个命令不需要任何更改：

[Click here to view code image](#ch09_images#f0376-05)

```python
def set_params(self, lower, upper):
...
```

第二个命令所需的唯一更改是允许在使用异步 I/O 将猜测传输到客户端时使用：

[Click here to view code image](#ch09_images#f0376-03)

```python
def next_guess(self):
...

async def send_number(self):                    # Changed
guess = self.next_guess()
self.guesses.append(guess)
await self.send(format(guess))              # Changed
```

第三个和第四个命令不需要任何更改：

[Click here to view code image](#ch09_images#f0376-04)

```python
def receive_report(self, decision):
...

def clear_state(self):
...
```

在客户端上启动新游戏需要添加一些 `async` 和 `await` 关键字来发送第一个和最后一个命令。它还需要使用 `contextlib` 内置模块的 `asynccontextmanager` 辅助函数：

[Click here to view code image](#ch09_images#f0377-01)

```python
@contextlib.asynccontextmanager                       # Changed
async def new_async_game(
connection, lower, upper, secret):                # Changed
print(
f"Guess a number between {lower} and {upper}!"
f" Shhhhh, it's {secret}."
)
await connection.send(f"PARAMS {lower} {upper}")   # Changed
try:
yield AsyncClientSession(
connection.send,
connection.receive,
secret,
)
finally:
await connection.send("CLEAR")                # Changed
```

用于表示游戏状态的 `ClientSession` 类的异步版本具有与之前相同的构造函数：

[Click here to view code image](#ch09_images#f0377-02)

```python
class AsyncClientSession:
def __init__(self, send, receive, secret):
...
```

第二个命令只需要添加 `async` 和 `await` 关键字，无论何时需要异步行为：

[Click here to view code image](#ch09_images#f0377-03)

```python
async def request_number(self):
await self.send("NUMBER")    # Changed
data = await self.receive()  # Changed
return int(data)
```

第三个命令只需要添加一个 `async` 和一个 `await` 关键字：

[Click here to view code image](#ch09_images#f0377-04)

```python
async def report_outcome(self, number):    # Changed
new_distance = math.fabs(number - self.secret)

if new_distance == 0:
decision = CORRECT
elif self.last_distance is None:
decision = UNSURE
elif new_distance < self.last_distance:
decision = WARMER
elif new_distance > self.last_distance:
decision = COLDER
else:
decision = SAME

self.last_distance = new_distance

await self.send(f"REPORT {decision}")         # Changed
return decision
```

为了启用异步迭代，我需要实现 `__aiter__` 而不是 `__iter__`，并相应地添加 `async` 和 `await`：

[Click here to view code image](#ch09_images#f0378-02)

```python
async def __aiter__(self):                        # Changed
while True:
number = await self.request_number()      # Changed
decision = await self.report_outcome(
number)                               # Changed
yield number, decision
if decision == CORRECT:
return
```

运行服务器的代码需要完全重新实现，以使用 `asyncio` 内置模块及其 `start_server` 函数：

[Click here to view code image](#ch09_images#f0378-03)

```python
import asyncio

async def handle_async_connection(reader, writer):
session = AsyncServerSession(reader, writer)
try:
await session.loop()
except EOFError:
pass

async def run_async_server(address):
server = await asyncio.start_server(
handle_async_connection, *address
)
async with server:
await server.serve_forever()
```

启动游戏所需的 `run_client` 函数在几乎每一行都需要更改。任何以前与阻塞 `socket` 实例交互过的代码都必须替换为类似功能的 `asyncio` 版本（在下面用 `# New` 标记）。函数中需要与 coroutines 交互的所有其他行都需要使用 `async` 和 `await` 关键字；类 coroutine 函数，如 `aiter` 和 `anext`；或异步特定常量，如 `StopAsyncIteration`。如果您忘记在必要的地方添加其中一个关键字，将在运行时引发异常。

[Click here to view code image](#ch09_images#f0379-01)

```python
async def run_async_client(address):
streams = await asyncio.open_connection(*address)  # New
client = AsyncConnection(*streams)                 # New

async with new_async_game(client, 1, 5, 3) as session:
results = [outcome async for outcome in session]

async with new_async_game(client, 10, 15, 12) as session:
async for outcome in session:
results.append(outcome)

async with new_async_game(client, 1, 3, 2) as session:
it = aiter(session)
while True:
try:
outcome = await anext(it)
except StopAsyncIteration:
break
else:
results.append(outcome)

_, writer = streams                                # New
writer.close()                                     # New
await writer.wait_closed()                         # New

return results
```

`run_async_client` 最有趣之处在于，为了将此函数移植到 coroutines，我无需重构与 `AsyncClient` 交互的任何实质性部分。我需要的每种语言特性都有相应的异步版本，这使得迁移变得简单明了。

这种过渡并不总是容易的。例如，在标准库中，目前没有 `itertools` 的异步版本（参见 [Item 24](#ch03#ch03lev1sec8): “考虑使用 itertools 处理 Iterators 和 Generators”）。也没有 `yield from` 的异步版本（参见 [Item 45](#ch06#ch06lev1sec6): “使用 yield from 组合多个 Generators”），这使得组合 generators 更加冗长。许多社区库有助于填补这些空白（参见 [Item 116](#ch14#ch14lev1sec1): “了解社区构建模块的位置”），但根据代码的复杂性，仍然可能需要额外的工作。

最后，需要更新胶水代码以端到端运行此新的异步示例。我使用 `asyncio.create_task` 函数将服务器排队到事件循环中执行，以便它与客户端并行运行，直到达到 `await` 表达式。这是另一种实现扇出的方法，其行为与 `asyncio.gather` 函数不同：

[Click here to view code image](#ch09_images#f0380-01)

```python
async def main_async():
address = ("127.0.0.1", 4321)

server = run_async_server(address)
asyncio.create_task(server)

results = await run_async_client(address)
for number, outcome in results:
print(f"Client: {number} is {outcome}")

asyncio.run(main_async())

>>>
Guess a number between 1 and 5! Shhhhh, it's 3.
Server: 5 is Unsure
Server: 4 is Warmer
Server: 2 is Same
Server: 1 is Colder
Server: 3 is Correct
Guess a number between 10 and 15! Shhhhh, it's 12.
Server: 14 is Unsure
Server: 10 is Same
Server: 15 is Colder
Server: 12 is Correct
Guess a number between 1 and 3! Shhhhh, it's 2.
Server: 2 is Correct
Client: 5 is Unsure
Client: 4 is Warmer
Client: 2 is Same
Client: 1 is Colder
Client: 3 is Correct
Client: 14 is Unsure
Client: 10 is Same
Client: 15 is Colder
Client: 12 is Correct
Client: 2 is Correct
```

这如预期般工作。Coroutine 版本更容易理解，因为所有与 threads 的交互都已移除。`asyncio` 内置模块还提供了许多辅助函数，这些函数减少了编写此类服务器所需的套接字样板代码量。

您的用例可能更难移植，原因有很多。`asyncio` 模块拥有大量的 I/O、同步和任务管理功能，这些功能可以使采用 coroutines 对您来说更容易（参见 [Item 77](#ch09#ch09lev1sec11): “混合使用 Threads 和 Coroutines 以简化向 asyncio 的过渡” 和 [Item 78](#ch09#ch09lev1sec12): “使用 async-Friendly Worker Threads 最大化 asyncio 事件循环的响应能力”）。请务必查看该库的在线文档（<https://docs.python.org/3/library/asyncio.html>），以了解其全部潜力。

#### 记住 (Things to Remember)

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 为 `for` 循环、`with` 语句、生成器、推导式、迭代器和库辅助函数提供了异步版本，这些版本可以用作 coroutines 中的即插即用替换。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `asyncio` 内置模块使得将使用 threads 和阻塞 I/O 的现有代码移植到 coroutines 和异步 I/O 变得简单明了。

### Item 77: 混合使用 Threads 和 Coroutines 以简化向 `asyncio` 的过渡 (Mix Threads and Coroutines to Ease the Transition to `asyncio`)

在上一项（参见 [Item 76](#ch09#ch09lev1sec10): “了解如何将 Threaded I/O 移植到 asyncio”），我将一个执行阻塞 I/O 和 threads 的 TCP 服务器移植到使用 `asyncio` 和 coroutines。这是一次大爆炸式迁移：我一次性将所有代码都移到了新风格。但以这种方式移植大型程序通常是不可行的。相反，您通常需要逐步迁移代码库，同时根据需要更新测试并验证每一步的有效性。

为此，您的代码库需要能够同时使用 threads 进行阻塞 I/O（参见 [Item 68](#ch09#ch09lev1sec2): “使用 Threads 进行阻塞 I/O；避免并行”）和 coroutines 进行异步 I/O（参见 [Item 75](#ch09#ch09lev1sec9): “使用 Coroutines 实现高度并发的 I/O”），并且它们必须相互兼容。实际上，这意味着您需要 threads 能够运行 coroutines，并且您需要 coroutines 能够启动和等待 threads。幸运的是，`asyncio` 包含内置的设施，可以使这种类型的互操作性变得简单明了。

例如，假设我正在编写一个将日志文件合并到一个输出流中的程序，以帮助进行调试。给定一个输入日志的文件句柄，我需要一种方法来检测是否有新数据可用并返回下一行输入。我可以通过使用文件句柄的 `tell` 方法来检查当前读取位置是否与文件长度匹配来实现这一点。当没有新数据可用时，应引发异常（有关背景信息，请参见 [Item 32](#ch05#ch05lev1sec3): “优先抛出异常而不是返回 None”）：

```python
class NoNewData(Exception):
pass

def readline(handle):
offset = handle.tell()
handle.seek(0, 2)
length = handle.tell()

if length == offset:
raise NoNewData

handle.seek(offset, 0)
return handle.readline()
```

通过将此函数包装在 `while` 循环中，我可以将其转换为 worker 线程。当新行可用时，我调用给定的回调函数将其写入输出日志（有关为什么使用函数接口而不是类的信息，请参见 [Item 48](#ch07#ch07lev1sec1): “为简单接口接受函数而不是类”）。当没有数据可用时，线程会休眠以减少轮询新数据引起的忙等待量。当输入文件句柄关闭时，worker 线程退出：

[Click here to view code image](#ch09_images#f0382-01)

```python
import time

def tail_file(handle, interval, write_func):
while not handle.closed:
try:
line = readline(handle)
except NoNewData:
time.sleep(interval)
else:
write_func(line)
```

现在我可以为每个输入文件启动一个 worker 线程，并将这些线程的输出统一到一个输出文件中。下面，`write` 闭包函数（参见 [Item 33](#ch05#ch05lev1sec4): “了解闭包如何与变量作用域和 nonlocal 交互”）需要使用 `Lock` 实例（参见 [Item 69](#ch09#ch09lev1sec3): “使用 Lock 防止 Threads 中的数据竞争”）来序列化对输出流的写入，并确保行内没有冲突：

[Click here to view code image](#ch09_images#f0383-02)

```python
from threading import Lock, Thread

def run_threads(handles, interval, output_path):
with open(output_path, "wb") as output:
lock = Lock()

def write(data):
with lock:
output.write(data)

threads = []
for handle in handles:
args = (handle, interval, write)
thread = Thread(target=tail_file, args=args)
thread.start()
threads.append(thread)

for thread in threads:
thread.join()
```

只要输入文件句柄仍然存在，其对应的 worker 线程也将保持存在。这意味着等待每个线程的 `join` 方法完成足以知道整个过程已完成。

给定一组输入路径和一个输出路径，我可以调用 `run_threads` 并确认它按预期工作。输入文件句柄的创建方式或单独关闭方式对于演示此代码的行为并不重要，输出验证函数——在下面的 `confirm_merge` 中定义——也不重要，这就是我将其省略的原因：

[Click here to view code image](#ch09_images#f0383-03)

```python
def confirm_merge(input_paths, output_path):
...

input_paths = ...
handles = ...
output_path = ...
run_threads(handles, 0.1, output_path)

confirm_merge(input_paths, output_path)
```

从这个 threaded 实现作为起点，我如何逐步将此代码转换为使用 `asyncio` 和 coroutines 呢？有两种方法：自顶向下和自底向上。

#### 自顶向下方法 (Top-Down Approach)

自顶向下意味着从代码库的最高层开始，例如在 `main` 入口点，然后向下到构成调用层次结构叶节点的单个函数和类。当您维护许多跨多个不同程序使用的通用模块时，此方法可能很有用。通过首先移植入口点，您可以等到其他所有地方都使用 coroutines 后再移植通用模块。

以下是具体步骤：
1.  将一个顶层函数从 `def` 更改为 `async def`。
2.  将其所有执行 I/O 的调用——可能阻塞事件循环——包装到使用 `asyncio.run_in_executor`。
3.  确保 `run_in_executor` 调用使用的资源或回调得到正确同步（即，使用 `Lock` 或带有扇入事件循环实例的 `asyncio.run_coroutine_threadsafe`）。
4.  尝试通过向下遍历调用层次结构并将中间函数和方法转换为 coroutines（遵循前三个步骤）来消除 `get_event_loop` 和 `run_in_executor` 调用。

这里我将步骤 1-3 应用于 `run_threads` 函数：

[Click here to view code image](#ch09_images#f0384-02)

```python
import asyncio

async def run_tasks_mixed(handles, interval, output_path):
loop = asyncio.get_event_loop()

output = await loop.run_in_executor(
None, open, output_path, "wb")
try:
async def write_async(data):
await loop.run_in_executor(None, output.write, data)

def write(data):
coro = write_async(data)
future = asyncio.run_coroutine_threadsafe(coro, loop)
future.result()

tasks = []
for handle in handles:
task = loop.run_in_executor(
None, tail_file, handle, interval, write
)
tasks.append(task)

await asyncio.gather(*tasks)

finally:
await loop.run_in_executor(None, output.close)
```

`run_in_executor` 方法指示事件循环使用 `ThreadPoolExecutor` 来运行给定的函数（可能包括阻塞 I/O），确保它不会干扰事件循环的线程（有关背景信息，请参见 [Item 74](#ch09#ch09lev1sec8): “当 Threads 对并发至关重要时，考虑 ThreadPoolExecutor”）。通过多次调用 `run_in_executor` 而不进行相应的 `await` 表达式，`run_tasks_mixed` coroutine 会扇出，为每个输入文件提供一个并发执行线。然后 `asyncio.gather` 扇入 `tail_file` threads 直到它们全部完成（有关扇出和扇入的更多信息，请参见 [Item 71](#ch09#ch09lev1sec5): “知道何时需要并发”）。

此代码通过使用 `asyncio.run_coroutine_threadsafe` 消除了 `write` 包装函数和 `Lock` 实例的需要。此函数允许普通 threads 调用 coroutine（在此情况下为 `write_async`），并在事件循环中从显式提供的 main thread 执行它。这有效地同步了 worker threads，确保所有对输出文件的写入都是一次一个。一旦 `asyncio.TaskGroup` awaitable 被解析，我就可以假设对输出文件的所有写入也已完成，因此我可以关闭输出文件句柄，而无需担心竞争条件。

我可以通过使用 `asyncio.run` 函数来启动 coroutine 并运行主事件循环来验证此代码是否按预期工作：

[Click here to view code image](#ch09_images#f0385-02)

```python
input_paths = ...
handles = ...
output_path = ...
asyncio.run(run_tasks_mixed(handles, 0.1, output_path))

confirm_merge(input_paths, output_path)
```

现在我可以将第 4 步应用于 `run_tasks_mixed` 函数，方法是向下移动调用堆栈。我可以将 `tail_file` 依赖函数重新定义为异步 coroutine，而不是执行阻塞 I/O，方法是遵循步骤 1-3：

[Click here to view code image](#ch09_images#f0386-02)

```python
async def tail_async(handle, interval, write_func):
loop = asyncio.get_event_loop()

while not handle.closed:
try:
line = await loop.run_in_executor(
None, readline, handle)
except NoNewData:
await asyncio.sleep(interval)
else:
await write_func(line)
```

新的 `tail_async` 函数使我能够消除 `run_tasks_mixed` 函数对 `run_coroutine_threadsafe` 和 `write` 包装函数的调用。我还可以使用 `asyncio.TaskGroup`（Python 3.11 中新增）来管理 `tail_async` coroutines 的扇出和扇入，从而进一步缩短代码：

[Click here to view code image](#ch09_images#f0386-03)

```python
async def run_tasks(handles, interval, output_path):
loop = asyncio.get_event_loop()

output = await loop.run_in_executor(
None, open, output_path, "wb")
try:

async def write_async(data):
await loop.run_in_executor(None, output.write, data)

async with asyncio.TaskGroup() as group:
for handle in handles:
group.create_task(
tail_async(handle, interval, write_async)
)
finally:
await loop.run_in_executor(None, output.close)
```

我也能验证 `run_tasks` 是否按预期工作：

[Click here to view code image](#ch09_images#f0387-01)

```python
input_paths = ...
handles = ...
output_path = ...
asyncio.run(run_tasks(handles, 0.1, output_path))

confirm_merge(input_paths, output_path)
```

有可能继续这种重构方法，并将 `readline` 也转换为异步 coroutine。然而，该函数需要如此多的阻塞文件 I/O 操作，以至于考虑到这会大大降低代码的清晰度，因此不值得移植。在某些情况下，将所有内容移动到 `asyncio` 是有意义的，而在其他情况下则不然。

#### 自底向上方法 (Bottom-Up Approach)

采用 coroutines 的自底向上方法有四个步骤，与自顶向下风格的步骤类似，但过程是从叶节点到入口点遍历调用层次结构。

以下是具体步骤：
1.  为要移植的每个叶函数创建一个新的异步 coroutine 版本。
2.  更改现有的同步函数，使它们调用 coroutine 版本并运行事件循环，而不是实现任何实际的异步行为。
3.  向上移动一个调用层次结构级别，创建另一层 coroutines，并将对同步函数的现有调用替换为对步骤 1 中定义的 coroutines 的调用。
4.  在不再需要它们来粘合代码片段时，删除围绕 coroutines 创建的同步包装器。

对于上面的示例，我将从 `tail_file` 函数开始，因为我决定 `readline` 函数应继续使用阻塞 I/O。我可以重写 `tail_file`，使其仅包装我上面定义的 `tail_async` coroutine。提供的 `write_func` 使用阻塞 I/O，可以通过 `write_async` 函数使用 `run_in_executor` 来运行，使其与 `tail_async` 所期望的兼容。为了运行每个 worker coroutine 直到完成，我可以为每个 `tail_file` 线程创建一个事件循环，然后调用其 `run_until_complete` 方法。此方法将阻塞当前线程并驱动事件循环，直到 `tail_async` coroutine 退出，从而实现与 `tail_file` 的 threaded、阻塞 I/O 版本相同的行为：

[Click here to view code image](#ch09_images#f0388-01)

```python
def tail_file(handle, interval, write_func):
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def write_async(data):
await loop.run_in_executor(None, write_func, data)

coro = tail_async(handle, interval, write_async)
loop.run_until_complete(coro)
```

这个新的 `tail_file` 函数是旧函数的直接替代品。我可以调用 `run_threads` 来验证一切是否按预期工作：

[Click here to view code image](#ch09_images#f0388-02)

```python
input_paths = ...
handles = ...
output_path = ...
run_threads(handles, 0.1, output_path)

confirm_merge(input_paths, output_path)
```

在用 `tail_file` 包装 `tail_async` 之后，下一步是将 `run_threads` 函数转换为 coroutine。这最终与上面自顶向下方法中的第 4 步相同，因此此时，这两种风格会合流。

这都是采用 `asyncio` 的一个很好的开始，但您还可以做更多事情来提高程序的响应能力（参见 [Item 78](#ch09#ch09lev1sec12): “使用 async-Friendly Worker Threads 最大化 asyncio 事件循环的响应能力”）。

#### 记住 (Things to Remember)

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `asyncio` 事件循环的可 awaitable `run_in_executor` 方法使 coroutines 能够在 `ThreadPoolExecutor` worker threads 中运行同步函数。这有助于自顶向下迁移到 `asyncio`。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `asyncio` 事件循环的 `run_until_complete` 方法使同步代码能够运行 coroutine 直到完成。`asyncio.run_coroutine_threadsafe` 函数在线程边界之间提供相同的功能。两者共同有助于自底向上迁移到 `asyncio`。

### Item 78: 使用 `async`-Friendly Worker Threads 最大化 `asyncio` 事件循环的响应能力 (Maximize Responsiveness of `asyncio` Event Loops with `async`-Friendly Worker Threads)

在上一项中，我展示了如何逐步迁移到 `asyncio`（有关背景信息和下面各种函数的实现，请参见 [Item 77](#ch09#ch09lev1sec11): “混合使用 Threads 和 Coroutines 以简化向 asyncio 的过渡”）。生成的 coroutine 正确地尾部输入文件并将它们合并到一个输出中：

[Click here to view code image](#ch09_images#f0389-01)

```python
import asyncio

async def run_tasks(handles, interval, output_path):
loop = asyncio.get_event_loop()

output = await loop.run_in_executor(
None, open, output_path, "wb")
try:

async def write_async(data):
await loop.run_in_executor(None, output.write, data)

async with asyncio.TaskGroup() as group:
for handle in handles:
group.create_task(
tail_async(handle, interval, write_async)
)
finally:
await loop.run_in_executor(None, output.close)
```

这段代码由于处理同步和异步函数调用之间的边界的所有 `run_in_executor` 样板代码而显得非常冗长和重复。如果我接受这样一个事实：对 `output` 文件句柄的 `open`、`close` 和 `write` 调用将阻塞事件循环——并且对于像这样合并多个文件句柄的目的，它在功能上也足够了——那么该函数会短得多：

[Click here to view code image](#ch09_images#f0389-02)

```python
async def run_tasks_simpler(handles, interval, output_path):
with open(output_path, "wb") as output:  # Changed

async def write_async(data):
output.write(data)               # Changed

async with asyncio.TaskGroup() as group:
for handle in handles:
group.create_task(
tail_async(handle, interval, write_async)
)
```

但是，像这样避免 `run_in_executor` 是不好的，因为所有这些操作都需要向程序的主机操作系统发出系统调用，这可能会阻塞事件循环很长时间，并阻止其他 coroutines 取得进展。这可能会损害整体响应能力并增加延迟，特别是对于由许多组件共享事件循环的程序，例如高度并发的服务器。

但实际上阻塞事件循环有多糟糕？它在实践中发生的频率有多高？我可以通过将 `debug=True` 参数传递给 `asyncio.run` 函数来检测此问题在实际程序中何时发生。这里我展示了如何识别一个坏的 coroutine 的文件和行，它可能阻塞在一个慢速系统调用上：

[Click here to view code image](#ch09_images#f0390-01)

```python
import time

async def slow_coroutine():
time.sleep(0.5)  # Simulating slow I/O

asyncio.run(slow_coroutine(), debug=True)

>>>
Executing <Task finished name='Task-1' coro=<slow_coroutine()
➥done, defined at example.py:61> result=None created at
➥.../asyncio/runners.py:100> took 0.506 seconds
...
```

如果我想要尽可能响应迅速的程序，那么我需要最小化从主事件循环中可能发生的系统调用。使用 `run_in_executor` 是其中一种方法，但它需要大量的样板代码，如上所示。一个潜在的更好替代方法是创建一个新的 `Thread` 子类（参见 [Item 68](#ch09#ch09lev1sec2): “使用 Threads 进行阻塞 I/O；避免并行”），该子类封装了使用其自己的独立事件循环写入输出文件所需的所有内容：

[Click here to view code image](#ch09_images#f0390-02)

```python
from threading import Thread

class WriteThread(Thread):
def __init__(self, output_path):
super().__init__()
self.output_path = output_path
self.output = None
self.loop = asyncio.new_event_loop()

def run(self):
asyncio.set_event_loop(self.loop)
with open(self.output_path, "wb") as self.output:
self.loop.run_forever()

# Run one final round of callbacks so the await on
# stop() in another event loop will be resolved.
self.loop.run_until_complete(asyncio.sleep(0))
```

其他线程中的 Coroutines 可以直接调用并 await 此类的 `write` 方法，因为它只是 `real_write` 方法的线程安全包装器，该方法实际执行 I/O。这消除了对 `Lock` 的需要（参见 [Item 69](#ch09#ch09lev1sec3): “使用 Lock 防止 Threads 中的数据竞争”）：

[Click here to view code image](#ch09_images#f0391-02)

```python
async def real_write(self, data):
self.output.write(data)

async def write(self, data):
coro = self.real_write(data)
future = asyncio.run_coroutine_threadsafe(
coro, self.loop)
await asyncio.wrap_future(future)
```

其他 coroutines 也可以以线程安全的方式告诉 worker 线程何时停止，使用类似的样板代码：

[Click here to view code image](#ch09_images#f0391-03)

```python
async def real_stop(self):
self.loop.stop()

async def stop(self):
coro = self.real_stop()
future = asyncio.run_coroutine_threadsafe(
coro, self.loop)
await asyncio.wrap_future(future)
```

我还可以定义 `__aenter__` 和 `__aexit__` 方法，以允许此类在 `with` 语句中使用（有关背景信息，请参见 [Item 82](#ch10#ch10lev1sec3): “考虑使用 contextlib 和 with 语句实现可重用的 try/finally 行为” 和 [Item 76](#ch09#ch09lev1sec10): “了解如何将 Threaded I/O 移植到 asyncio”）。这确保了 worker 线程在正确的时间启动和停止，而不会减慢主事件循环线程：

[Click here to view code image](#ch09_images#f0391-04)

```python
async def __aenter__(self):
loop = asyncio.get_event_loop()
await loop.run_in_executor(None, self.start)
return self

async def __aexit__(self, *_):
await self.stop()
```

使用这个新的 `WriteThread` 类，我可以将 `run_tasks` 重构为一个完全异步的版本，该版本易于阅读，不会干扰主事件循环的默认 executor，并且完全避免在主事件循环线程中运行慢速系统调用：

[Click here to view code image](#ch09_images#f0392-02)

```python
def readline(handle):
...

async def tail_async(handle, interval, write_func):
...

async def run_fully_async(handles, interval, output_path):
async with (
WriteThread(output_path) as output,
asyncio.TaskGroup() as group,
):
for handle in handles:
group.create_task(
tail_async(handle, interval, output.write)
)
```

鉴于一组输入句柄和一个输出文件路径，我可以验证这是否按预期工作：

[Click here to view code image](#ch09_images#f0392-03)

```python
def confirm_merge(input_paths, output_path):
...

input_paths = ...
handles = ...
output_path = ...
asyncio.run(run_fully_async(handles, 0.1, output_path))

confirm_merge(input_paths, output_path)
```

#### 记住 (Things to Remember)

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在 coroutines 中执行系统调用——包括阻塞 I/O 和启动 threads——可能会降低程序响应能力并增加延迟感知。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 通过将 `debug=True` 参数传递给 `asyncio.run` 来检测某些 coroutines 何时阻止事件循环快速响应。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 为了提高必须跨越异步和同步执行边界的代码的可读性，请考虑定义提供 coroutine 友好接口的辅助线程类。

### Item 79: 考虑 `concurrent.futures` 以实现真正的并行 (Consider `concurrent.futures` for True Parallelism)

在编写 Python 程序的过程中，您可能会遇到性能瓶颈。即使在优化了 Python 代码之后（参见 [Item 92](#ch11#ch11lev1sec1): “优化前进行剖析”），程序的执行速度可能仍然无法满足您的需求。在拥有越来越多的 CPU 核心的现代计算机上，可以合理地假设一个解决方案可能是并行化。如果您可以将代码的计算分解为可以在多个 CPU 核心上同时运行的独立工作单元，那会怎么样？

不幸的是，Python 的全局解释器锁 (GIL) 在大多数情况下会阻止 Python threads 中的真正 CPU 并行化（参见 [Item 68](#ch09#ch09lev1sec2): “使用 Threads 进行阻塞 I/O；避免并行”）。但是 `multiprocessing` 内置模块，可以通过 `concurrent.futures` 内置模块轻松访问，可能正是您所需要的（参见 [Item 74](#ch09#ch09lev1sec8): “当 Threads 对并发至关重要时，考虑 ThreadPoolExecutor” 的相关示例）。`multiprocessing` 通过运行额外的解释器作为子进程，使 Python 能够利用多个 CPU 核心进行并行处理。这些子进程与主解释器是分开的，因此它们的全局解释器锁也是分开的。每个子进程都可以充分利用一个 CPU 核心。每个子进程还与主进程有一个链接，在那里它接收计算指令并返回结果。

例如，假设我想用 Python 做一些计算密集型的事情，并利用多个 CPU 核心。我将使用一个求两个数最大公约数的实现作为更计算密集型算法（如使用 Navier–Stokes 方程模拟流体动力学）的代理：

[Click here to view code image](#ch09_images#f0393-01)

```python
# my_module.py
def gcd(pair):
a, b = pair
low = min(a, b)
for i in range(low, 0, -1):
if a % i == 0 and b % i == 0:
return i
raise RuntimeError("Not reachable")
```

串行运行此函数需要线性增加的时间，因为没有并行性：

[Click here to view code image](#ch09_images#f0394-01)

```python
# run_serial.py
import my_module
import time

NUMBERS = [
(19633090, 22659730),
(20306770, 38141720),
(15516450, 22296200),
(20390450, 20208020),
(18237120, 19249280),
(22931290, 10204910),
(12812380, 22737820),
(38238120, 42372810),
(38127410, 47291390),
(12923910, 21238110),
]

def main():
start = time.perf_counter()
results = list(map(my_module.gcd, NUMBERS))
end = time.perf_counter()
delta = end - start
print(f"Took {delta:.3f} seconds")

if __name__ == "__main__":
main()

>>>
Took 5.643 seconds
```

在多个 Python 线程上运行此代码将不会带来任何速度提升，因为 GIL 阻止 Python 在多个 CPU 核心上并行使用。这里我使用 `concurrent.futures` 模块及其 `ThreadPoolExecutor` 类和八个 worker 线程（以匹配我计算机上的 CPU 核心数）执行与上面相同的计算：

[Click here to view code image](#ch09_images#f0394-02)

```python
# run_threads.py
import my_module
from concurrent.futures import ThreadPoolExecutor
import time

NUMBERS = [
...
]

def main():
start = time.perf_counter()
pool = ThreadPoolExecutor(max_workers=8)
results = list(pool.map(my_module.gcd, NUMBERS))
end = time.perf_counter()
delta = end - start
print(f"Took {delta:.3f} seconds")

if __name__ == "__main__":
main()

>>>
Took 5.810 seconds
```

由于启动和通信线程池的开销，这次甚至更慢。

现在是令人惊讶的部分：更改一行代码会产生神奇的效果。如果我用 `concurrent.futures` 模块中的 `ProcessPoolExecutor` 替换 `ThreadPoolExecutor`，一切都会加速：

[Click here to view code image](#ch09_images#f0395-02)

```python
# run_parallel.py
import my_module
from concurrent.futures import ProcessPoolExecutor
import time

NUMBERS = [
...
]

def main():
start = time.perf_counter()
pool = ProcessPoolExecutor(max_workers=8)  # The one change
results = list(pool.map(my_module.gcd, NUMBERS))
end = time.perf_counter()
delta = end - start
print(f"Took {delta:.3f} seconds")

if __name__ == "__main__":
main()

>>>
Took 1.684 seconds
```

在我的多核机器上运行，这要快得多！这是如何可能的？以下是 `ProcessPoolExecutor` 类实际执行的操作（通过 `multiprocessing` 模块提供的低级结构）：

1.  它从 `map` 的 `numbers` 输入数据中获取每个项目。
2.  它使用 `pickle` 模块将项目序列化为二进制数据（参见 [Item 107](#ch12#ch12lev1sec8): “使用 copyreg 使 pickle 序列化可维护”）。
3.  它通过本地套接字将序列化数据从主解释器进程复制到子解释器进程。
4.  它在子进程中使用 `pickle` 将数据反序列化回 Python 对象。
5.  它导入包含 `gcd` 函数的 Python 模块。
6.  它在其他子进程并行运行该函数。
7.  它将结果序列化回二进制数据。
8.  它通过套接字将该二进制数据复制回来。
9.  它在父进程中将二进制数据反序列化回 Python 对象。
10. 它将来自多个子进程的结果合并到一个 `list` 中返回。

尽管使用 `pool.map` 方法看起来很简单，但 `multiprocessing` 模块和 `ProcessPoolExecutor` 类做了大量工作来实现并行化。在大多数其他语言中，协调两个线程所需的唯一接触点是单个锁或原子操作（参见 [Item 69](#ch09#ch09lev1sec3): “使用 Lock 防止 Threads 中的数据竞争” 的示例）。由于父进程和子进程之间必须发生的所有序列化和反序列化，因此使用 `multiprocessing` 的开销很高。

这种方案非常适合某些类型的隔离的、高杠杆的任务。通过 _隔离_，我指的是不需要与程序其他部分共享状态的函数。通过 _高杠杆_，我指的是只需少量数据必须在父进程和子进程之间传输以实现大量计算的情况。最大公约数算法就是一个例子，但许多其他数学算法也类似。

如果您的计算不具备这些特征，那么 `ProcessPoolExecutor` 的开销可能会阻止它通过并行化来加速您的程序。当发生这种情况时，`multiprocessing` 提供了共享内存、进程间锁、队列和代理的更高级设施。但所有这些功能都非常复杂。在单个进程的内存空间中处理这些工具已经足够困难了，更不用说在 Python threads 之间共享了。将这种复杂性扩展到其他进程并涉及套接字会使其更难理解。

我建议您最初避免使用 `multiprocessing` 内置模块的所有部分。您可以从使用 `ThreadPoolExecutor` 类运行隔离的、高杠杆的函数开始。稍后您可以迁移到 `ProcessPoolExecutor` 以获得加速。最后，当您完全用尽其他选项时，您可以考虑直接使用 `multiprocessing` 模块或使用更高级的技术（参见 [Item 94](#ch11#ch11lev1sec3): “知道何时以及如何用另一种编程语言替换 Python”）。

#### 记住 (Things to Remember)

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `multiprocessing` 模块提供了强大的工具，可以以最小的努力并行化某些类型的 Python 计算。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `multiprocessing` 的强大功能最好通过 `concurrent.futures` 内置模块及其简单的 `ProcessPoolExecutor` 类来访问。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在用尽所有其他选项之前，避免使用 `multiprocessing` 模块的高级（且复杂）部分。

## Effective Python - 10

## 10

本章深入探讨了 Graph Neural Networks (GNNs) 和 Graph Foundation Models (GFMs) 在处理和理解复杂图结构数据方面的强大能力。我们将重点关注这些模型的核心贡献和主要观点，强调它们在各种下游任务中的应用潜力。

**核心贡献与主要观点：**

本章的核心在于阐述 GNNs 和 GFMs 如何通过学习节点表示 (Node Embedding) 来捕捉图的拓扑结构和节点特征。它们的核心思想是**Message Passing**机制，即节点通过与其邻居交换信息来更新自身的表示。这种机制使得 GNNs 能够有效地聚合局部信息，并将其传播到整个图。

GFMs 作为 GNNs 的一个重要发展方向，旨在构建通用的、可迁移的图模型。它们通常通过大规模的**Pre-training**阶段，在海量图数据上进行**Self-supervised Learning**，从而学习到丰富的图结构和节点特征的通用表示。这些预训练模型随后可以通过**Fine-tuning**、**In-context Learning**、**Few-shot Learning**或**Zero-shot Learning**等方式，快速适应各种特定的图相关任务，而无需从头开始训练。

**关键技术与模型：**

本章将详细介绍几种代表性的 GNNs 模型，包括：

*   **Graph Convolutional Networks (GCN)**：通过卷积操作来聚合邻居信息。
*   **Graph Attention Networks (GAT)**：引入注意力机制，为邻居节点分配不同的权重。
*   **GraphSAGE**：一种基于采样和聚合的归纳式学习框架。

此外，我们还将探讨 GFMs 的构建策略，以及它们如何利用大规模预训练和迁移学习来解决现实世界中的图数据问题。

**应用领域：**

GNNs 和 GFMs 在多个领域展现出强大的应用能力，包括但不限于：

*   **Node Classification**：预测节点的类别。
*   **Link Prediction**：预测图中节点之间是否存在连接。
*   **Graph Classification**：预测整个图的类别。
*   **Knowledge Graph**：在知识图谱中进行推理和问答。
*   **Heterogeneous Graph** 和 **Homogeneous Graph**：处理不同类型节点和边的图。
*   **Graph Anomaly Detection**：识别图中的异常模式。
*   **Multi-modal Learning**：结合图数据与其他模态的数据进行学习。
*   **Cross-domain Transfer** 和 **Domain Adaptation**：将模型从一个领域迁移到另一个领域。

本章还将简要提及**Graph Pooling**（用于将图结构信息压缩到更低维度的表示）以及**Graph Isomorphism**（图同构性问题）等相关概念。

通过本章的学习，读者将能够深入理解 GNNs 和 GFMs 的工作原理，掌握如何利用这些先进的模型来解决复杂的图数据问题，并为进一步探索更前沿的图学习技术打下坚实的基础。

## Effective Python - Robustness

## 健壮性 (Robustness)

许多有用的 Python 代码都始于一个随意开发的脚本，用于一次性解决特定问题。随着这些脚本的扩展、重新用途和重用，它们会从短期、一次性代码演变成值得长期维护的实质性程序。

一旦您编写了这样一个有用的 Python 程序，关键的下一步就是将您的代码“生产化”，使其坚不可摧。使程序在遇到意外情况时可靠，与使程序具有正确的功能同样重要。Python 提供了内置的功能和模块，有助于加固您的程序，使其在各种情况下都具有健壮性。

### Item 80: 利用 `try`/`except`/`else`/`finally` 的每个块

在 Python 中处理异常时，有四个不同的时间点您可以采取行动：在 `try`、`except`、`else` 和 `finally` 块中。复合语句中的每个块都有其独特的作用，而这些块的各种组合都很有用（另请参见 [Item 121](#ch14#ch14lev1sec6): “[定义一个根异常以将调用者与 API 隔离开来](#ch14#ch14lev1sec6)” 以获取另一个示例）。

#### `finally` 块

当您希望异常能够向上传播，并且还希望在发生异常时运行清理代码时，请使用 `try`/`finally`。`try`/`finally` 的一个常见用法是可靠地关闭文件句柄（另请参见 [Item 82](#ch10#ch10lev1sec3): “[考虑使用 contextlib 和 with 语句来实现可重用的 try/finally 行为](#ch10#ch10lev1sec3)” 以获取另一种——可能更好的——方法）：

![](./images/f0399-01.png)
```python
def try_finally_example(filename):
print("* Opening file")
handle = open(filename, encoding="utf-8")  # May raise OSError
try:
print("* Reading data")
return handle.read()                   # May raise UnicodeDecodeError
finally:
print("* Calling close()")
handle.close()                         # Always runs after try block
```

`read` 方法引发的任何异常都将始终传播到调用代码，但 `finally` 块中的 `handle` 的 `close` 方法将首先运行：

![](./images/f0400-02.png)
```python
filename = "random_data.txt"

with open(filename, "wb") as f:
f.write(b"\xf1\xf2\xf3\xf4\xf5")  # Invalid utf-8

data = try_finally_example(filename)

>>>
* Opening file
* Reading data
* Calling close()
Traceback ...
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in
➥position 0: invalid continuation byte
```

您必须在 `try` 块之前调用 `open`，因为在打开文件时发生的异常（例如，如果文件不存在，则为 `OSError`）应该完全跳过 `finally` 块：

![](./images/f0400-03.png)
```python
try_finally_example("does_not_exist.txt")

>>>
* Opening file
Traceback ...
FileNotFoundError: [Errno 2] No such file or directory:
➥'does_not_exist.txt'
```

#### `else` 块

使用 `try`/`except`/`else` 可以清楚地表明哪些异常将由您的代码处理，哪些异常将传播上去。当 `try` 块不引发异常时，`else` 块将运行。`else` 块有助于最小化 `try` 块中的代码量，这对于隔离潜在的异常原因很有好处，并提高了可读性（另请参见 [Item 83](#ch10#ch10lev1sec4): “[始终使 try 块尽可能短](#ch10#ch10lev1sec4)”）。例如，假设我想从字符串加载 JSON 字典数据并返回其中一个键的值：

![](./images/f0401-01.png)
```python
import json

def load_json_key(data, key):
try:
print("* Loading JSON data")
result_dict = json.loads(data)  # May raise ValueError
except ValueError:
print("* Handling ValueError")
raise KeyError(key)
else:
print("* Looking up key")
return result_dict[key]         # May raise KeyError
```

在成功的情况下，JSON 数据在 `try` 块中解码，然后键查找发生在 `else` 块中：

![](./images/f0401-02.png)
```python
assert load_json_key('{"foo": "bar"}', "foo") == "bar"

>>>
* Loading JSON data
* Looking up key
```

如果输入数据不是有效的 JSON，则使用 `json.loads` 进行解码会引发 `ValueError`。该异常由 `except` 块捕获并处理：

![](./images/f0401-03.png)
```python
load_json_key('{"foo": bad payload', "foo")

>>>
* Loading JSON data
* Handling ValueError
Traceback ...
JSONDecodeError: Expecting value: line 1 column 9 (char 8)

The above exception was the direct cause of the following
➥exception:

Traceback ...
KeyError: 'foo'
```

如果键查找引发任何异常，它们将传播到调用者，因为它们位于 `try` 块之外。`else` 子句确保 `try`/`except` 之后的代码在视觉上与 `except` 块区分开来。这使得异常传播行为清晰明了：

![](./images/f0402-01.png)
```python
load_json_key('{"foo": "bar"}', "does not exist")

>>>
* Loading JSON data
* Looking up key
Traceback ...
KeyError: 'does not exist'
```

#### 整体结合

当您想在一个复合语句中完成所有操作时，请使用 `try`/`except`/`else`/`finally`。例如，假设我想从文件中读取要执行的工作的描述，对其进行处理，然后就地更新文件。这里 `try` 块用于读取文件并处理它，`except` 块用于处理 `try` 块中预期的异常，`else` 块用于就地更新文件并允许相关异常传播上去，`finally` 块用于清理文件句柄：

![](./images/f0402-02.png)
```python
UNDEFINED = object()
def divide_json(path):
print("* Opening file")
handle = open(path, "r+")                       # May raise OSError
try:
print("* Reading data")
data = handle.read()                        # May raise UnicodeDecodeError
print("* Loading JSON data")
op = json.loads(data)                       # May raise ValueError
print("* Performing calculation")
value = op["numerator"] / op["denominator"] # May raise ZeroDivisionError
except ZeroDivisionError:
print("* Handling ZeroDivisionError")
return UNDEFINED
else:
print("* Writing calculation")
op["result"] = value
result = json.dumps(op)
handle.seek(0)                              # May raise OSError
handle.write(result)                        # May raise OSError
return value
finally:
print("* Calling close()")
handle.close()                              # Always runs
```

在成功的情况下，`try`、`else` 和 `finally` 块都会运行：

![](./images/f0403-01.png)
```python
temp_path = "random_data.json"

with open(temp_path, "w") as f:
f.write('{"numerator": 1, "denominator": 10}')

assert divide_json(temp_path) == 0.1

>>>
* Opening file
* Reading data
* Loading JSON data
* Performing calculation
* Writing calculation
* Calling close()
```

如果计算无效，则 `try`、`except` 和 `finally` 块会运行，但 `else` 块不会运行：

![](./images/f0403-02.png)
```python
with open(temp_path, "w") as f:
f.write('{"numerator": 1, "denominator": 0}')

assert divide_json(temp_path) is UNDEFINED

>>>
* Opening file
* Reading data
* Loading JSON data
* Performing calculation
* Handling ZeroDivisionError
* Calling close()
```

如果 JSON 数据无效，则 `try` 块会运行并引发异常，`finally` 块会运行，然后异常会传播到调用者。`except` 和 `else` 块不会运行：

![](./images/f0403-03.png)
```python
with open(temp_path, "w") as f:
f.write('{"numerator": 1, "denominator": 10}')

assert divide_json(temp_path) == 0.1

>>>
* Opening file
* Reading data
* Loading JSON data
* Performing calculation
* Writing calculation
* Calling close()
```

如果 JSON 数据无效，则 `try` 块会运行并引发异常，`finally` 块会运行，然后异常会传播到调用者。`except` 和 `else` 块不会运行：

![](./images/f0403-03.png)
```python
with open(temp_path, "w") as f:
f.write('{"numerator": 1 bad data')

divide_json(temp_path)

>>>
* Opening file
* Reading data
* Loading JSON data
* Calling close()
Traceback ...
JSONDecodeError: Expecting ',' delimiter: line 1 column 17
➥(char 16)
```

此布局特别有用，因为所有块都以直观的方式协同工作。例如，我在这里通过在硬盘空间不足的同时运行 `divide_json` 函数来模拟此情况：

![](./images/f0404-01.png)
```python
with open(temp_path, "w") as f:
f.write('{"numerator": 1, "denominator": 10}')

assert divide_json(temp_path) == 0.1

>>>
* Opening file
* Reading data
* Loading JSON data
* Performing calculation
* Writing calculation
* Calling close()
Traceback ...
OSError: [Errno 28] No space left on device
```

当在 `else` 块中重写结果数据时引发异常，`finally` 块仍然运行并按预期关闭了文件句柄。

#### 记住的事项

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `try`/`finally` 复合语句允许您在 `try` 块中是否引发异常的情况下运行清理代码。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `else` 块有助于最小化 `try` 块中的代码量，并在视觉上将成功案例与 `try`/`except` 块区分开来。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `else` 块可用于在成功的 `try` 块之后、在 `finally` 块中进行常见清理之前执行其他操作。

### Item 81: `assert` 内部假设并 `raise` 未达预期

Python 包含 `assert` 语句，如果给定表达式为假值，它将在运行时引发 `AssertionError` 异常（有关背景信息，请参见 [Item 7](#ch01#ch01lev1sec7): “[考虑使用条件表达式进行简单的内联逻辑](#ch01#ch01lev1sec7)”）。例如，我在这里尝试验证两个列表不为空，第二个断言失败，因为表达式不是真值：

![](./images/f0404-02.png)
`list_a = [1, 2, 3]
assert list_a, "a empty"
list_b = []
assert list_b, "b empty"  # Raises
>>>
Traceback ...
AssertionError: b empty`

Python 还提供了 `raise` 语句来向调用者报告异常情况（有关何时使用它的信息，请参见 [Item 32](#ch05#ch05lev1sec3): “[优先引发异常而不是返回 None](#ch05#ch05lev1sec3)”）。我在这里使用 `raise` 和 `if` 语句来报告相同类型的空列表问题：

![](./images/f0405-02.png)
```python
class EmptyError(Exception):
pass

list_c = []
if not list_c:
raise EmptyError("c empty")
>>>
Traceback ...
EmptyError: c empty
```

来自 `raise` 语句的异常可以用 `try`/`except` 语句捕获（请参见 [Item 80](#ch10#ch10lev1sec1): “[利用 try/except/else/finally 的每个块](#ch10#ch10lev1sec1)”）。这种替代的控制流是 `raise` 的主要目的：

![](./images/f0405-03.png)
```python
try:
raise EmptyError("From raise statement")
except EmptyError as e:
print(f"Caught: {e}")

>>>
Caught: From raise statement
```

但也可以在运行时捕获 `assert` 语句的异常：

![](./images/f0405-04.png)
```python
try:
assert False, "From assert statement"
except AssertionError as e:
print(f"Caught: {e}")

>>>
Caught: From assert statement
```

为什么 Python 提供两种不同的方法（`raise` 和 `assert`）来报告异常情况？原因是它们各自扮演着不同的角色。

由 `raise` 语句引起的异常被认为是函数接口的一部分，就像参数和返回值一样。这些异常旨在被调用代码捕获并相应地处理。函数可能引发的潜在异常应在文档中说明（请参见 [Item 118](#ch14#ch14lev1sec3): “[为每个函数、类和模块编写文档字符串](#ch14#ch14lev1sec3)”），以便调用者知道他们可能需要处理它们。这些 `raise` 语句的行为也应在自动化测试中进行验证（请参见 [Item 109](#ch13#ch13lev1sec2): “[优先集成测试而非单元测试](#ch13#ch13lev1sec2)”）。

由 `assert` 语句引起的异常不应被函数调用者捕获。它们用于验证实现中的假设，这些假设对于代码的新读者来说可能不明显。断言是自文档化的，因为它们会评估第二个表达式（逗号之后）以在条件失败时创建调试错误消息。这些消息可以被调用堆栈更高层级的错误报告和日志记录工具使用，以帮助开发人员查找和修复错误（请参见 [Item 87](#ch10#ch10lev1sec8): “[使用 traceback 进行增强的异常报告](#ch10#ch10lev1sec8)” 以获取示例）。

实现相同功能的代码可能会根据上下文使用 `assert` 语句、`raise` 语句或两者都使用。例如，我在这里定义了一个简单的类，可用于聚合电影评分。它提供了一个健壮的 API，该 API 验证输入并使用 `raise` 向调用者报告任何问题：

![](./images/f0406-01.png)
```python
class RatingError(Exception):
...

class Rating:
def __init__(self, max_rating):
if not (max_rating > 0):
raise RatingError("Invalid max_rating")
self.max_rating = max_rating
self.ratings = []

def rate(self, rating):
if not (0 < rating <= self.max_rating):
raise RatingError("Invalid rating")
self.ratings.append(rating)
```

此类引发的异常旨在被捕获，并假定报告给发送无效输入的最终用户或 API 调用者：

```python
movie = Rating(5)
movie.rate(5)
movie.rate(7)  # Raises

>>>
Traceback ...
RatingError: Invalid rating
```

这是相同功能的另一个实现，但此版本不旨在向调用者报告错误。相反，此类假设程序的其他部分已执行必要的验证：

![](./images/f0407-01.png)
```python
class RatingInternal:
def __init__(self, max_rating):
assert max_rating > 0, f"Invalid {max_rating=}"
self.max_rating = max_rating
self.ratings = []

def rate(self, rating):
assert 0 < rating <= self.max_rating, \    f"Invalid {rating=}"
self.ratings.append(rating)
```

当此类中的 `assert` 语句引发异常时，它旨在报告代码中的错误。消息应包含程序员以后可用于查找原因并修复它的信息：

![](./images/f0407-02.png)
```python
movie = RatingInternal(5)
movie.rate(5)
movie.rate(7)  # Raises

>>>
Traceback ...
AssertionError: Invalid rating=7
```

为了使此类断言有用，调用代码不捕获和抑制 `AssertionError` 或 `Exception` 异常至关重要（请参见 [Item 85](#ch10#ch10lev1sec6): “[警惕捕获 Exception 类](#ch10#ch10lev1sec6)”）。

最终，您需要决定 `raise` 还是 `assert` 是最合适的选择。随着 Python 程序复杂性的增长，相互关联的函数、类和模块的层开始成形。其中一些系统是面向外部的 API：供其他组件利用的库函数和接口。在这些情况下，`raise` 将最有用（请参见 [Item 121](#ch14#ch14lev1sec6): “[定义一个根异常以将调用者与 API 隔离开来](#ch14#ch14lev1sec6)”）。其他代码是面向内部的，有助于程序的一部分实现更大的需求。在这些情况下，`assert` 是最佳选择；只需确保不要禁用断言（请参见 [Item 90](#ch10#ch10lev1sec11): “[切勿将 \_\_debug\_\_ 设置为 False](#ch10#ch10lev1sec11)”）。

#### 记住的事项

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `raise` 语句可用于将预期的错误条件报告给函数调用者。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 函数直接引发的异常是其显式接口的一部分，应相应地记录。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `assert` 语句应用于验证代码中的程序员假设，并将其传达给实现的其他读者。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 失败的断言不是函数显式接口的一部分，不应被调用者捕获。

### Item 82: 考虑使用 `contextlib` 和 `with` 语句来实现可重用的 `try`/`finally` 行为

Python 中的 `with` 语句用于指示代码何时在特殊上下文中运行。例如，互斥锁（请参见 [Item 69](#ch09#ch09lev1sec3): “[使用 Lock 防止线程中的数据竞争](#ch09#ch09lev1sec3)”）可以在 `with` 语句中使用，以指示缩进的代码块仅在持有锁时运行：

![](./images/f0408-01.png)
```python
from threading import Lock
lock = Lock()
with lock:
# Do something while maintaining an invariant
...
```

上面的示例等效于此 `try`/`finally` 构造（请参见 [Item 80](#ch10#ch10lev1sec1): “[利用 try/except/else/finally 的每个块](#ch10#ch10lev1sec1)”），因为 `Lock` 类正确地启用了 `with` 语句的使用：

![](./images/f0408-02.png)
```python
lock.acquire()
try:
# Do something while maintaining an invariant
...
finally:
lock.release()
```

此 `with` 语句版本更好，因为它消除了编写 `try`/`finally` 复合语句的重复代码的需要，确保您不会忘记为每个 `acquire` 调用都有一个相应的 `release` 调用。

通过使用 `contextlib` 内置模块，可以轻松地使您的对象和函数在 `with` 语句中工作。此模块包含 `contextmanager` 装饰器（有关背景信息，请参见 [Item 38](#ch05#ch05lev1sec9): “[使用 functools.wraps 定义函数装饰器](#ch05#ch05lev1sec9)”），它允许将一个简单的函数用于 `with` 语句。这比定义一个具有特殊方法 `__enter__` 和 `__exit__` 的新类（标准的面向对象方法）要容易得多。

例如，假设我希望代码的某个区域有时具有更多的调试日志记录。我在这里定义了一个执行两个严重性级别日志记录的函数：

![](./images/f0409-01.png)
```python
import logging

def my_function():
logging.debug("Some debug data")
logging.error("Error log here")
logging.debug("More debug data")
```

我的程序的默认日志记录级别是 `WARNING`，因此当我运行该函数时，只有 `logging.error` 消息会打印到屏幕上：

```python
my_function()

>>>
Error log here
```

我可以通过定义一个上下文管理器来临时提高此函数的日志记录级别。此辅助函数在运行 `with` 块中的代码之前提高日志记录严重性级别，之后降低日志记录严重性级别：

![](./images/f0409-02.png)
```python
from contextlib import contextmanager

@contextmanager
def debug_logging(level):
logger = logging.getLogger()
old_level = logger.getEffectiveLevel()
logger.setLevel(level)
try:
yield
finally:
logger.setLevel(old_level)
```

`yield` 表达式是执行 `with` 块内容的点（有关背景信息，请参见 [Item 43](#ch06#ch06lev1sec4): “[考虑使用生成器而不是返回列表](#ch06#ch06lev1sec4)”）。`with` 块中发生的任何异常都将由 `yield` 表达式重新引发，供您在辅助函数中捕获（有关其工作原理，请参见 [Item 47](#ch06#ch06lev1sec8): “[使用类而不是生成器的 throw 方法管理迭代状态转换](#ch06#ch06lev1sec8)”）。

现在我可以再次调用相同的日志记录函数，但在 `debug_logging` 上下文中。这次，所有调试消息都将打印到 `with` 块中的屏幕上。在 `with` 块之外运行的同一函数不会打印调试消息：

![](./images/f0410-01.png)
```python
with debug_logging(logging.DEBUG):
print("* Inside:")
my_function()

print("* After:")
my_function()
>>>
* Inside:
Some debug data
Error log here
More debug data
* After:
Error log here
```

#### 启用 `as` 目标

传递给 `with` 语句的上下文管理器也可以返回一个对象。此对象被分配给复合语句的 `as` 部分中的局部变量。这使得在 `with` 块中运行的代码能够直接与上下文进行交互（另请参见 [Item 76](#ch09#ch09lev1sec10): “[了解如何将线程 I/O 移植到 asyncio](#ch09#ch09lev1sec10)” 以获取另一个示例）。

例如，假设我想写入一个文件并确保它始终正确关闭。我可以通过将 `open` 传递给 `with` 语句来做到这一点。`open` 返回一个文件句柄给 `with` 的 `as` 目标，并在 `with` 块退出时关闭该句柄：

![](./images/f0410-02.png)
```python
with open("my_output.txt", "w") as handle:
handle.write("This is some data!")
```

与手动使用 `try`/`finally` 复合语句打开和关闭文件句柄相比，`with` 方法更具 Pythonic 风格：

![](./images/f0410-03.png)
```python
handle = open("my_output.txt", "w")
try:
handle.write("This is some data!")
finally:
handle.close()
```

使用 `as` 目标还可以让您确信文件在执行离开 `with` 语句时最终会被关闭。通过突出关键部分，它还鼓励您减少在文件句柄打开期间执行的代码量，这通常是好的做法。

要使您自己的函数能够为 `as` 目标提供值，您所要做的就是从上下文管理器中 `yield` 一个值。例如，我在这里定义了一个上下文管理器来获取一个 `Logger` 实例，设置其级别，然后 `yield` 它成为 `as` 目标：

![](./images/f0411-01.png)
```python
@contextmanager
def log_level(level, name):
logger = logging.getLogger(name)
old_level = logger.getEffectiveLevel()
logger.setLevel(level)
try:
yield logger
finally:
logger.setLevel(old_level)
```

调用 `debug` 等日志记录方法在 `as` 目标上会产生输出，因为在 `with` 块中为该特定 `Logger` 实例设置了足够低的日志记录严重性级别。直接使用 `logging` 模块不会打印任何内容，因为默认程序日志记录器的默认日志记录严重性级别是 `WARNING`：

![](./images/f0411-02.png)
```python
with log_level(logging.DEBUG, "my-log") as my_logger:
my_logger.debug(f"This is a message for {my_logger.name}!")
logging.debug("This will not print")

>>>
This is a message for my-log!
```

在 `with` 语句退出后，调用名为 `"my-log"` 的 `Logger` 上的调试日志记录方法将不会打印任何内容，因为默认日志记录严重性级别已自动恢复。错误日志消息将始终打印：

![](./images/f0411-03.png)
```python
logger = logging.getLogger("my-log")
logger.debug("Debug will not print")
logger.error("Error will print")

>>>
Error will print
```

稍后，我可以通过简单地更新 `with` 语句来更改我要使用的日志记录器的名称。这将使 `with` 块中的 `as` 目标指向不同的实例，但我无需更新我的其他任何代码来匹配：

![](./images/f0411-04.png)
```python
with log_level(logging.DEBUG, "other-log") as my_logger:# Changed
my_logger.debug(f"This is a message for {my_logger.name}!")
logging.debug("This will not print")

>>>
This is a message for other-log!
```

这种状态隔离以及创建上下文和在该上下文内操作之间的解耦是 `with` 语句的另一个好处。

#### 记住的事项

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `with` 语句允许您重用 `try`/`finally` 块中的逻辑并减少视觉噪音。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `contextlib` 内置模块提供了一个 `contextmanager` 装饰器，可以轻松地在 `with` 语句中使用您自己的函数。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 上下文管理器 `yield` 的值将提供给 `with` 语句的 `as` 部分。它有助于让您的代码直接访问特殊上下文的原因。

### Item 83: 始终使 `try` 块尽可能短

在处理预期的异常时，正确设置各种语句块需要相当多的开销（请参见 [Item 80](#ch10#ch10lev1sec1): “[利用 try/except/else/finally 的每个块](#ch10#ch10lev1sec1)”）。例如，假设我想通过连接进行远程过程调用 (RPC)，这可能会遇到错误：

![](./images/f0412-02.png)
```python
connection = ...
class RpcError(Exception):
...

def lookup_request(connection):
...

raise RpcError("From lookup_request")
def close_connection(connection):
...
print("Connection closed")

try:
request = lookup_request(connection)
except RpcError:
print("Encountered error!")
close_connection(connection)

>>>
Error!
Connection closed
```

稍后，想象一下我想对 `try` 块中收集的数据进行更多处理，或处理特殊情况。最简单自然的方法是直接在需要的地方添加代码。我在这里更改上面的示例，使其具有一个快速路径，该路径检查缓存的响应以避免额外的处理：

![](./images/f0413-01.png)
```python
def lookup_request(connection):
# No error raised
...

def is_cached(connection, request):
...
raise RpcError("From is_cached")

try:
request = lookup_request(connection)
if is_cached(connection, request):
request = None
except RpcError:
print("Encountered error!")
close_connection(connection)

>>>
Connection closed
```

问题在于 `is_cached` 函数也可能引发 `RpcError` 异常。通过将 `lookup_request` 和 `is_cached` 放在同一个 `try`/`except` 语句中，稍后在代码中我无法确定是哪个函数实际引发了错误并导致连接关闭：

![](./images/f0413-02.png)
```python
if is_closed(connection):
# Was the connection closed because of an error
# in lookup_request or is_cached?
...
```

相反，您应该做的是每个 `try` 块只包含一个预期的错误源。所有其他内容应放在关联的 `else` 块或单独的后续 `try` 语句中：

![](./images/f0413-03.png)
```python
try:
request = lookup_request(connection)
except RpcError:
close_connection(connection)
else:
if is_cached(connection, request):  # Moved
request = None

>>>
Traceback ...
RpcError: From is_cached
```

这种方法确保您 _未_ 预期的异常，例如 `is_cached` 可能引发的异常，将通过您的调用堆栈冒泡，并产生您以后可以查找、调试和修复的错误消息。

#### 记住的事项

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 将过多代码放入 `try` 块中可能导致您的程序捕获您不打算处理的异常。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 不要扩展 `try` 块，而是将其他代码放入关联的 `except` 块之后的 `else` 块中，或者放入一个完全独立的 `try` 语句中。

### Item 84: 警惕异常变量消失

与 `for` 循环变量不同（请参见 [Item 20](#ch03#ch03lev1sec4): “[循环结束后切勿使用 for 循环变量](#ch03#ch03lev1sec4)”），异常变量在 `except` 块的下一行不可访问：

![](./images/f0414-01.png)
```python
try:
raise MyError(123)
except MyError as e:
print(f"Inside {e=}")

print(f"Outside {e=}")  # Raises

>>>
Inside e=MyError(123)
Traceback ...
NameError: name 'e' is not defined
```

您可能会认为异常变量在 `finally` 块的作用域内仍然存在，该块是异常处理机制的一部分（请参见 [Item 80](#ch10#ch10lev1sec1): “[利用 try/except/else/finally 的每个块](#ch10#ch10lev1sec1)”）。不幸的是，它不会：

![](./images/f0414-02.png)
```python
try:
raise MyError(123)
except MyError as e:
print(f"Inside {e=}")
finally:
print(f"Finally {e=}")  # Raises

>>>
Inside e=MyError(123)
Traceback ...
NameError: name 'e' is not defined
```

有时保存 `try` 语句每个潜在结果的结果很有用。例如，假设我想记录每个分支的结果以供调试。为了实现这一点，我需要创建一个新变量并在每个分支中为其赋值：

![](./images/f0415-01.png)
```python
result = "Unexpected exception"
try:
raise MyError(123)
except MyError as e:
result = e
except OtherError as e:
result = e
else:
result = "Success"
finally:
print(f"Log {result=}")

>>>
Log result=MyError(123)
```

重要的是要注意，在上面的示例中，`result` 变量甚至在 `try` 块之前就被赋值了。这是为了解决这种情况：引发了未被其中一个 `except` 子句处理的异常。如果您不预先赋值 `result`，则会引发运行时错误而不是原始错误：

![](./images/f0415-02.png)
```python
try:
raise OtherError(123)  # Not handled
except MyError as e:
result = e
else:
result = "Success"
finally:
print(f"{result=}")    # Raises

>>>
Traceback ...
OtherError: 123

The above exception was the direct cause of the following
➥exception:

Traceback ...
NameError: name 'result' is not defined
```

这说明了 Python 在作用域变量到函数方面不一致的另一种方式。`except` 块、生成器表达式、列表推导式或 `for` 循环中变量的生命周期可能与您期望的不同（请参见 [Item 42](#ch06#ch06lev1sec3): “[使用赋值表达式减少推导式中的重复](#ch06#ch06lev1sec3)” 以获取示例）。

#### 记住的事项

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 由 `except` 语句赋值的 `Exception` 变量仅在其关联的 `except` 块中可访问。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 为了在周围作用域或后续 `finally` 块中访问捕获的 `Exception` 实例，您必须将其赋值给另一个变量名。

### Item 85: 警惕捕获 `Exception` 类

程序中的错误——无论是预期的还是意外的——都会频繁发生。这些问题是构建软件的一个方面，程序员必须接受并尝试缓解。例如，假设我想分析一家披萨店的销售情况并生成每日汇总报告。我在这里通过一个简单的函数管道来实现这一点：

```python
def load_data(path):
...

def analyze_data(data):
...

def run_report(path):
data = load_data(path)
summary = analyze(data)
return summary
```

拥有一个最新的摘要始终可用会很有用，因此我将每 5 分钟按计划调用 `run_report` 函数。但是，有时可能会发生瞬时错误，例如在一天开始之前，餐厅尚未开业，此时每日文件中尚未记录任何交易：

![](./images/f0416-02.png)
```python
summary = run_report("pizza_data-2024-01-28.csv")
print(summary)

>>>
Traceback ...
FileNotFoundError: [Errno 2] No such file or directory:
➥'pizza_data-2024-01-28.csv'
```

通常，我会通过用 `try`/`except` 语句包装 `run_report` 调用来解决此问题，该语句将失败消息记录到控制台（有关详细信息，请参见 [Item 80](#ch10#ch10lev1sec1): “[利用 try/except/else/finally 的每个块](#ch10#ch10lev1sec1)”）：

![](./images/f0417-01.png)
```python
try:
summary = run_report("pizza_data.csv")
except FileNotFoundError:
print("Transient file error")
else:
print(summary)

>>>
Transient file error
```

这将避免一种问题，但该管道可能引发许多其他类型的瞬时异常，我尚未预料到。我希望防止任何间歇性错误导致报告正在运行的餐厅的销售点程序崩溃。交易的持续处理比定期报告的刷新更重要。

一种将系统其他部分与故障隔离的方法是捕获更广泛的 `Exception` 父类，而不是更具体的 `FileNotFoundError` 类：

![](./images/f0417-02.png)
```python
try:
summary = run_report("pizza_data.csv")
except Exception:  # Changed
print("Transient report issue")
else:
print(summary)

>>>
Transient report issue
```

当引发异常时，将按顺序考虑每个 `except` 子句。如果异常值类型是子类于子句指定的类，则将执行相应的错误处理代码。通过提供 `Exception` 类进行匹配，我将捕获任何类型的错误，因为它们都继承自此父类。

不幸的是，这种方法有一个大问题：`try`/`except` 语句可能会让我忽略代码中的合法问题。一旦披萨店开业并且数据文件肯定存在，`run_report` 函数仍然会出乎意料地失败。原因是 `run_report` 的原始定义中有一个拼写错误，它调用了不存在的 `analyze` 函数，而不是正确的 `analyze_data` 函数：

![](./images/f0417-03.png)
```python
run_report("my_data.csv")

>>>

Traceback ...
NameError: name 'analyze' is not defined
```

由于 Python 的高度动态性，解释器仅在执行时检测到函数丢失，而不是在程序首次加载时（有关详细信息，请参见 [Item 3](#ch01#ch01lev1sec3): “[切勿期望 Python 在编译时检测错误](#ch01#ch01lev1sec3)”）。解释器将引发 `NameError`，它是 `Exception` 类的子类。因此，相应的 `except` 子句将捕获异常并将其报告为瞬时错误，即使它实际上是一个关键问题。

一种缓解此问题的方法是始终打印或记录捕获到的异常，当匹配 `Exception` 类时。至少这样错误信息就会可见；任何查看控制台输出的人都可能注意到程序中存在真正的错误。例如，我在这里打印异常值及其类型，以使其非常清楚出了什么问题：

![](./images/f0418-02.png)
```python
try:
summary = run_report("my_data.csv")
except Exception as e:
print("Fail:", type(e), e)
else:
print(summary)

>>>
Fail: <class 'NameError'> name 'analyze' is not defined
```

还有其他过于宽泛的异常处理方式可能导致问题，这些问题也值得了解（请参见 [Item 86](#ch10#ch10lev1sec7): “[理解 Exception 和 BaseException 之间的区别](#ch10#ch10lev1sec7)” 和 [Item 89](#ch10#ch10lev1sec10): “[始终将资源传递给生成器并让调用者在外部清理它们](#ch10#ch10lev1sec10)”）。此外，还有更健壮的方法来报告和处理显式 API 的错误，这些方法有助于避免这些问题（请参见 [Item 121](#ch14#ch14lev1sec6): “[定义一个根异常以将调用者与 API 隔离开来](#ch14#ch14lev1sec6)”）。捕获异常以隔离错误可能很有用，但您需要确保不要意外隐藏问题。

#### 记住的事项

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在 `except` 子句中使用 `Exception` 类可以帮助您将程序的某个部分与其余部分隔离开来。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 捕获广泛的异常类别可能导致您的代码处理您不打算处理的错误，这可能会无意中隐藏问题。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用广泛的异常处理程序时，打印或以其他方式记录遇到的任何错误以提供对实际情况的可见性非常重要。

### Item 86: 理解 `Exception` 和 `BaseException` 之间的区别

Python 文档会告诉您程序员定义的异常类必须继承自 `Exception` 类。但 Python 中异常树的根实际上是 `BaseException`，它是 `Exception` 的父类。`BaseException` 分支出了其他异常类，Python 将它们用于自己的内部目的。

例如，当用户按下 Control-C 组合键时，Python 程序正在运行，他们希望中断正在运行的程序并使其终止。Python 实现此目的的确切方式取决于平台，但最终解释器运行时会将中断信号转换为 `KeyboardInterrupt` 异常并将其引发到程序的​​主线程中。`KeyboardInterrupt` _不_ 继承自 `Exception`，这意味着它应该绕过所有异常处理程序直到程序的入口点，并导致它以错误消息退出。我在这里通过退出无限循环来演示此行为，即使它捕获了 `Exception` 类：

![](./images/f0419-01.png)
```python
def do_processing():
...

def main(argv):
while True:
try:
do_processing()  # Interrupted
except Exception as e:
print("Error:", type(e), e)

return 0

if __name__ == "__main__":
sys.exit(main(sys.argv))

>>>
Traceback ...
KeyboardInterrupt
```

知道这是可能的，我可能会选择捕获 `BaseException` 类，以便我始终可以在程序终止之前进行清理，例如刷新打开的文件到磁盘以确保它们不会损坏。在其他情况下，捕获此类广泛的异常类别对于将组件与潜在错误隔离开来并提供弹性 API 非常有用（请参见 [Item 85](#ch10#ch10lev1sec6): “[警惕捕获 Exception 类](#ch10#ch10lev1sec6)” 和 [Item 121](#ch14#ch14lev1sec6): “[定义一个根异常以将调用者与 API 隔离开来](#ch14#ch14lev1sec6)”）。我可以返回 `1` 在异常处理程序的末尾，以指示程序应以错误代码退出：

![](./images/f0420-01.png)
```python
def do_processing(handle):
...

def main(argv):
data_path = argv[1]
handle = open(data_path, "w+")

while True:
try:
do_processing(handle)
except Exception as e:
print("Error:", type(e), e)
except BaseException:
print("Cleaning up interrupt")
handle.flush()
handle.close()
return 1

return 0

if __name__ == "__main__":
sys.exit(main(sys.argv))

>>>
Cleaning up interrupt
Traceback ...
SystemExit: 1
```

问题在于还有其他异常类型也继承自 `BaseException`，包括 `SystemExit`（由 `sys.exit` 内置函数引起）和 `GeneratorExit`（请参见 [Item 89](#ch10#ch10lev1sec10): “[始终将资源传递给生成器并让调用者在外部清理它们](#ch10#ch10lev1sec10)”）。Python 未来也可能添加更多。Python 将这些异常视为执行所需行为的机制，而不是报告错误条件，这就是它们位于类层次结构不同部分的原因。运行时依赖用户通常不捕获这些异常才能正常工作；如果您捕获它们，您可能会无意中导致程序中的有害副作用。

因此，如果您想实现这种清理行为，最好使用 `try`/`finally` 语句（请参见 [Item 80](#ch10#ch10lev1sec1): “[利用 try/except/else/finally 的每个块](#ch10#ch10lev1sec1)”）和 `with` 语句（请参见 [Item 82](#ch10#ch10lev1sec3): “[考虑使用 contextlib 和 with 语句来实现可重用的 try/finally 行为](#ch10#ch10lev1sec3)”）等构造。这些构造将确保清理方法运行，而不管引发的异常是否继承自 `Exception` 或 `BaseException`：

![](./images/f0421-01.png)
```python
def main(argv):
data_path = argv[1]
handle = open(data_path, "w+")

try:
while True:
try:
do_processing(handle)
except Exception as e:
print("Error:", type(e), e)

finally:
print("Cleaning up finally")  # Always runs
handle.flush()
handle.close()

if __name__ == "__main__":
sys.exit(main(sys.argv))

>>>
Cleaning up finally
Traceback ...
KeyboardInterrupt
```

如果由于某种原因您确实必须捕获并处理 `BaseException` 的直接子类，那么正确地传播错误以使调用堆栈上方的其他代码仍然接收到它很重要。例如，我可能会捕获 `KeyboardInterrupt` 异常并询问用户是否确认他们打算终止程序。我在这里使用裸 `raise` 在异常处理程序的末尾来确保异常正常继续，而不会修改其堆栈跟踪（有关背景信息，请参见 [Item 87](#ch10#ch10lev1sec8): “[使用 traceback 进行增强的异常报告](#ch10#ch10lev1sec8)”）：

![](./images/f0421-02.png)
```python
def main(argv):
while True:
try:
do_processing()
except Exception as e:
print("Error:", type(e), e)
except KeyboardInterrupt:
found = input("Terminate? [y/n]: ")
if found == "y":
raise  # Propagate the error
if __name__ == "__main__":
sys.exit(main(sys.argv))

>>>
Terminate? [y/n]: y
Traceback ...
KeyboardInterrupt
```

您可能决定捕获 `BaseException` 的另一个情况是用于增强日志记录实用程序（请参见 [Item 87](#ch10#ch10lev1sec8): “[使用 traceback 进行增强的异常报告](#ch10#ch10lev1sec8)” 以获取相关用例）。例如，我可以定义一个函数装饰器，该装饰器记录所有输入和输出，包括引发的 `Exception` 子类值（有关背景信息，请参见 [Item 38](#ch05#ch05lev1sec9): “[使用 functools.wraps 定义函数装饰器](#ch05#ch05lev1sec9)”）：

![](./images/f0422-02.png)
```python
import functools

def log(func):
@functools.wraps(func)
def wrapper(*args, **kwargs):
try:
result = func(*args, **kwargs)
except Exception as e:
result = e
raise
finally:
print(
f"Called {func.__name__}"
f"(*{args!r}, **{kwargs!r}) "
f"got {result!r}"
)
return wrapper
```

调用用 `log` 装饰的函数将按预期打印所有内容：

![](./images/f0422-03.png)
```python
@log
def my_func(x):
x / 0

my_func(123)

>>>
Called my_func(*(123,), **{}) got ZeroDivisionError
(➥'division by zero')

Traceback ...
ZeroDivisionError: division by zero
```

但是，如果引发的异常继承自 `BaseException` 而不是 `Exception`，则装饰器将中断并导致意外错误：

![](./images/f0423-01.png)
```python
@log
def other_func(x):
if x > 0:
sys.exit(1)

other_func(456)

>>>
Traceback ...
SystemExit: 1

The above exception was the direct cause of the following
➥exception:

Traceback ...
UnboundLocalError: cannot access local variable 'result'
➥where it is not associated with a value
```

这似乎违反直觉，但 `finally` 子句即使在没有 `except` 子句存在或提供的 `except` 子句都不匹配引发的异常值的情况下也会运行（请参见 [Item 84](#ch10#ch10lev1sec5): “[警惕异常变量消失](#ch10#ch10lev1sec5)” 以获取另一个示例）。在上面的情况中，正是这种情况：`SystemExit` 不是 `Exception` 的子类，因此该处理程序从未运行，并且在调用 `finally` 子句中的 `print` 之前未为 `result` 赋值。简单地捕获 `BaseException` 而不是 `Exception` 可以解决问题：

![](./images/f0423-02.png)
```python
def fixed_log(func):
@functools.wraps(func)
def wrapper(*args, **kwargs):
try:
result = func(*args, **kwargs)
except BaseException as e:  # Fixed
result = e
raise
finally:
print(
f"Called {func.__name__}"
f"(*{args!r}, **{kwargs!r}) "
f"got {result!r}"
)
return wrapper
```

现在装饰器可以按预期处理 `SystemExit`：

![](./images/f0424-02.png)
```python
@fixed_log
def other_func(x):
if x > 0:
sys.exit(1)

other_func(456)

>>>
Called other_func(*(456,), **{}) got SystemExit(1)
Traceback ...
SystemExit: 1
```

处理 `BaseException` 和相关类可能很有用，但它也非常棘手，因此仔细注意细节并小心很重要。

#### 记住的事项

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 对于内部行为，Python 有时会引发 `BaseException` 子类，这些子类会跳过仅处理 `Exception` 基类的 `except` 子句。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `try`/`finally` 语句、`with` 语句和类似构造可以正确处理引发的 `BaseException` 子类，而无需额外工作。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 有合法的原因捕获 `BaseException` 和相关类，但这样做可能会出错。

### Item 87: 使用 `traceback` 进行增强的异常报告

当 Python 程序遇到问题时，通常会引发异常。如果异常未被捕获和处理（请参见 [Item 80](#ch10#ch10lev1sec1): “[利用 try/except/else/finally 的每个块](#ch10#ch10lev1sec1)”），它将传播到程序的入口点，并导致其以错误代码退出。Python 解释器还将打印一个格式良好的堆栈跟踪或 _traceback_，以帮助开发人员找出出了什么问题。例如，我在这里使用 `assert` 语句来引发异常并打印相应的堆栈跟踪（有关背景信息，请参见 [Item 81](#ch10#ch10lev1sec2): “[assert 内部假设，raise 未达预期](#ch10#ch10lev1sec2)”）：

![](./images/f0425-01.png)
```python
def inner_func(message):
assert False, message

def outer_func(message):
inner_func(message)

outer_func("Oops!")

>>>
Traceback (most recent call last):
File "my_code.py", line 7, in <module>
outer_func("Oops!")
~~~~~~~~~~^^^^^^^^^
File "my_code.py", line 5, in outer_func
inner_func(message)
~~~~~~~~~~^^^^^^^^^
File "my_code.py", line 2, in inner_func
assert False, message
^^^^^
AssertionError: Oops!
```

这种默认的打印行为对于所有异常都发生在主线程中的单线程代码可能很有帮助。但它不适用于并发处理许多请求的程序或服务器（请参见 [Item 71](#ch09#ch09lev1sec5): “[了解何时需要并发](#ch09#ch09lev1sec5)”）。如果您允许一个请求的异常传播到入口点，程序将崩溃并导致所有其他请求也失败。

一种处理此问题的方法是将请求处理程序的根包装在通用的 `try` 语句中（请参见 [Item 85](#ch10#ch10lev1sec6): “[警惕捕获 Exception 类](#ch10#ch10lev1sec6)” 和 [Item 86](#ch10#ch10lev1sec7): “[理解 Exception 和 BaseException 之间的区别](#ch10#ch10lev1sec7)”）。例如，我在这里定义了一个假设的 `Request` 类和处理函数。当遇到异常时，我可以将其打印到控制台日志供开发人员查看，然后返回错误代码给客户端。这确保了所有其他处理程序都能继续处理，即使存在错误的请求：

![](./images/f0425-02.png)
```python
class Request:
def __init__(self, body):
self.body = body
self.response = None

def do_work(data):
assert False, data
...

def handle(request):
try:
do_work(request.body)
except BaseException as e:
print(repr(e))
request.response = 400  # Bad request error

request = Request("My message")
handle(request)

>>>
AssertionError('My message')
```

此代码的问题在于异常值的字符串表示形式未提供足够的信息来调试问题。我没有像 Python 解释器主线程中的未处理异常那样获得堆栈跟踪。幸运的是，Python 可以通过 `traceback` 内置模块来弥补这一差距，该模块允许您在运行时从异常中提取堆栈跟踪信息。我在这里使用 `traceback` 内置模块中的 `print_tb` 函数来打印堆栈跟踪：

![](./images/f0426-02.png)
```python
import traceback
def handle2(request):
try:
do_work(request.body)
except BaseException as e:
traceback.print_tb(e.__traceback__)  # Changed
print(repr(e))
request.response = 400

request = Request("My message 2")
handle2(request)

>>>
File "my_code.py", line 70, in handle2
do_work(request.body)
~~~~~~~^^^^^^^^^^^^^^
File "my_code.py", line 42, in do_work
assert False, data
^^^^^
AssertionError('My message 2')
```

除了打印到控制台之外，您还可以像您喜欢的那样处理堆栈跟踪的详细信息——包括文件名、行号、源代码行和包含的函数名（例如，显示在 GUI 中）。我在这里提取堆栈跟踪中每一帧的函数名并将其打印到控制台：

![](./images/f0427-01.png)
```python
def handle3(request):
try:
do_work(request.body)
except BaseException as e:
stack = traceback.extract_tb(e.__traceback__)
for frame in stack:
print(frame.name)
print(repr(e))
request.response = 400

request = Request("My message 3")
handle3(request)

>>>
handle3
do_work
AssertionError('My message 3')
```

除了打印到控制台之外，我还可以使用 `traceback` 模块提供更高级的错误处理行为。例如，假设我想将遇到的异常日志保存在单独的文件中，每个 JSON 负载编码为一行。我在这里使用一个处理堆栈跟踪帧的包装函数来实现这一点：

![](./images/f0427-02.png)
```python
import json

def log_if_error(file_path, target, *args, **kwargs):
try:
target(*args, **kwargs)
except BaseException as e:
stack = traceback.extract_tb(e.__traceback__)
stack_without_wrapper = stack[1:]
trace_dict = dict(
stack=[item.name for item in stack_without_wrapper],
error_type=type(e).__name__,
error_message=str(e),
)
json_data = json.dumps(trace_dict)

with open(file_path, "a") as f:
f.write(json_data)
f.write("\n")
```

调用带有出错的 `do_work` 函数的包装器将正确编码错误并将其写入磁盘：

![](./images/f0428-01.png)
```python
log_if_error("my_log.jsonl", do_work, "First error")
log_if_error("my_log.jsonl", do_work, "Second error")
with open("my_log.jsonl") as f:
for line in f:
print(line, end="")

>>>
{"stack": ["do_work"], "error_type": "AssertionError",
➥"error_message": "First error"}
{"stack": ["do_work"], "error_type": "AssertionError",
➥"error_message": "Second error"}
```

`traceback` 内置模块还包含各种其他函数，可以轻松地以您可能需要的大多数方式格式化、打印和遍历异常堆栈跟踪（请参见 <https://docs.python.org/3/library/traceback.html>）。但是，您仍然需要自己处理一些边缘情况（请参见 [Item 88](#ch10#ch10lev1sec9): “[考虑显式链接异常以澄清堆栈跟踪](#ch10#ch10lev1sec9)” 以获取一个这样的案例）。

#### 记住的事项

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 当未处理的异常传播到 Python 程序的入口点时，解释器将打印导致错误的堆栈帧的格式良好的列表。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在高度并发的程序中，异常堆栈跟踪通常不会以相同的方式打印，这使得错误更难理解和调试。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `traceback` 内置模块允许您与异常的堆栈帧进行交互，并以您认为合适的方式处理它们（即，以帮助调试）。

### Item 88: 考虑显式链接异常以澄清堆栈跟踪

Python 程序在遇到错误或代码中的某些条件时会引发异常（请参见 [Item 32](#ch05#ch05lev1sec3): “[优先引发异常而不是返回 None](#ch05#ch05lev1sec3)”）。例如，我在这里尝试访问字典中不存在的键，这会导致引发异常：

![](./images/f0428-02.png)
```python
my_dict = {}
my_dict["does_not_exist"]

>>>
Traceback ...
KeyError: 'does_not_exist'
```

我可以捕获此异常并通过使用 `try` 语句来处理它（请参见 [Item 80](#ch10#ch10lev1sec1): “[利用 try/except/else/finally 的每个块](#ch10#ch10lev1sec1)”）：

![](./images/f0429-01.png)
```python
my_dict = {}
try:
my_dict["does_not_exist"]
except KeyError:
print("Could not find key!")

>>>
Could not find key!
```

如果在我处理一个异常时引发了另一个异常，输出看起来会大不相同。例如，我在这里在处理 `KeyError` 异常时引发了一个新定义的 `MissingError` 异常：

![](./images/f0429-02.png)
```python
class MissingError(Exception):
...
try:
my_dict["does_not_exist"]    # Raises first exception
except KeyError:
raise MissingError("Oops!")  # Raises second exception

>>>
Traceback ...
KeyError: 'does_not_exist'

The above exception was the direct cause of the following
➥exception:

Traceback ...
MissingError: Oops!
```

在 `except KeyError` 块中引发的 `MissingError` 异常是传播到调用者的那个。但是，您还可以看到 Python 打印的堆栈跟踪包含了有关导致初始问题的异常的信息：由 `my_dict["does_not_exist"]` 表达式引发的 `KeyError`。此额外数据可用，因为 Python 会自动将异常的 `__context__` 属性分配给由周围 `except` 块处理的异常实例。这里是与上面相同的代码，但现在我捕获 `MissingError` 异常并打印其 `__context__` 属性以显示异常是如何 _链接_ 在一起的：

![](./images/f0429-03.png)
```python
try:
try:
my_dict["does_not_exist"]
except KeyError:
raise MissingError("Oops!")
except MissingError as e:
print("Second:", repr(e))
print("First: ", repr(e.__context__))

>>>
Second: MissingError('Oops!')
First:  KeyError('does_not_exist')
```

在具有许多错误处理层的复杂代码中，控制这些异常链以使错误消息更清晰可能很有用。为了实现这一点，Python 允许通过在 `raise` 语句中使用 `from` 子句来显式链接异常。

例如，假设我想定义一个实现与上面相同的字典查找行为的辅助函数：

![](./images/f0430-02.png)
```python
def lookup(my_key):
try:
return my_dict[my_key]
except KeyError:
raise MissingError
```

当我查找存在的键时，我可以在没有问题的情况下检索值：

```python
my_dict["my key 1"] = 123
print(lookup("my key 1"))

>>>
123
```

当给定的键丢失时，会如预期地引发 `MissingError` 异常：

![](./images/f0430-03.png)
```python
print(lookup("my key 2"))

>>>
Traceback ...
KeyError: 'my key 2'

The above exception was the direct cause of the following
➥exception:

Traceback ...
MissingError
```

现在想象一下我想增强 `lookup` 函数，并在键丢失时能够联系远程数据库服务器并填充 `my_dict` 字典。我在这里实现了此行为，假设 `contact_server` 将执行数据库通信：

![](./images/f0431-01.png)
```python
def contact_server(my_key):
print(f"Looking up {my_key!r} in server")
...

def lookup(my_key):
try:
return my_dict[my_key]
except KeyError:
result = contact_server(my_key)
my_dict[my_key] = result  # Fill the local cache
return result
```

重复调用此函数，我可以看到服务器仅在第一次调用时被联系，此时键尚不存在于 `my_dict` 缓存中。后续调用会避免调用 `contact_server` 并返回已存在于 `my_dict` 中的值：

![](./images/f0431-02.png)
```python
print("Call 1")
print("Result:", lookup("my key 2"))
print("Call 2")
print("Result:", lookup("my key 2"))

>>>
Call 1
Looking up 'my key 2' in server
Result: my value 2
Call 2
Result: my value 2
```

假设数据库服务器可能没有请求的记录。在这种情况下，也许 `contact_server` 函数会引发一种新类型的异常来指示这种情况：

![](./images/f0431-03.png)
```python
class ServerMissingKeyError(Exception):
...

def contact_server(my_key):
print(f"Looking up {my_key!r} in server")
...
raise ServerMissingKeyError
...
```

现在当我尝试查找丢失的记录时，我看到一个堆栈跟踪，其中包含 `ServerMissingKeyError` 异常和 `my_dict` 缓存未命中时的原始 `KeyError`：

![](./images/f0432-01.png)
```python
print(lookup("my key 3"))

>>>
Looking up 'my key 3' in server
Traceback ...
KeyError: 'my key 3'

The above exception was the direct cause of the following
➥exception:

Traceback ...
ServerMissingKeyError
```

问题在于，当 `contact_server` 未被调用时，`lookup` 函数不再遵循与之前相同的接口。为了将异常的详细信息抽象给调用者，我希望缓存未命中始终导致 `MissingError`，而不是 `ServerMissingKeyError`，后者可能定义在我不控制的单独模块中（请参见 [Item 121](#ch14#ch14lev1sec6): “[API 中的异常类](#ch14#ch14lev1sec6)”）。

为了解决这个问题，我可以在调用 `contact_server` 时将其包装在另一个 `try` 语句中，捕获 `ServerMissingKeyError` 异常，并改为引发 `MissingError`（匹配 `lookup` 的所需 API）：

![](./images/f0432-02.png)
```python
def lookup(my_key):
try:
return my_dict[my_key]
except KeyError:
try:
result = contact_server(my_key)
except ServerMissingKeyError:
raise MissingError       # Convert the server error
else:
my_dict[my_key] = result  # Fill the local cache
return result
```

尝试 `lookup` 的新实现，我可以验证 `MissingError` 异常是传播到调用者的内容：

![](./images/f0432-03.png)
```python
print(lookup("my key 4"))

>>>
Looking up 'my key 4' in server
Traceback ...
KeyError: 'my key 4'

The above exception was the direct cause of the following
➥exception:

Traceback ...
ServerMissingKeyError

The above exception was the direct cause of the following
➥exception:

Traceback ...
MissingError
```

此异常链显示了三个不同的错误，这是因为 `lookup` 函数中 `except` 子句的嵌套方式。首先，引发 `KeyError` 异常。然后，在处理它时，`contact_server` 函数引发 `ServerMissingKeyError`，它通过 `__context__` 属性从 `KeyError` 隐式链接。然后捕获 `ServerMissingKeyError`，并引发 `MissingError`，其 `__context__` 属性隐式分配给当前正在处理的 `ServerMissingKeyError`。

此 `MissingError` 打印了大量信息——多到似乎会使尝试调试实际问题的程序员感到困惑。一种减少输出的方法是使用 `raise` 语句中的 `from` 子句来显式指示异常的来源。我在这里通过在相应的 `raise` 语句中使用 `from e` 子句来隐藏 `ServerMissingKeyError` 源错误，以显式地将 `MissingError` 从 `KeyError` 链接起来：

![](./images/f0433-02.png)
```python
def lookup_explicit(my_key):
try:
return my_dict[my_key]
except KeyError as e:              # Changed
try:
result = contact_server(my_key)
except ServerMissingKeyError:
raise MissingError from e  # Changed
else:
my_dict[my_key] = result
return result
```

再次调用该函数，我可以确认 `ServerMissingKeyError` 异常不再打印：

![](./images/f0433-03.png)
```python
print(lookup_explicit("my key 5"))

>>>
Looking up 'my key 5' in server

Traceback ...
KeyError: 'my key 5'

The above exception was the direct cause of the following
➥exception:

Traceback ...
MissingError
```

尽管在异常输出中，`ServerMissingKeyError` 似乎不再与 `MissingError` 异常相关联，但它实际上仍然存在，分配给 `__context__` 属性，就像以前一样。它未被打印的原因是，在 `raise` 语句中使用 `from e` 子句会将引发异常的 `__cause__` 属性分配给 `KeyError`，并将 `__suppress_context__` 属性设置为 `True`。我在这里显示这些属性的值以阐明 Python 使用什么来控制未处理异常的打印：

![](./images/f0434-02.png)
```python
try:
lookup_explicit("my key 6")
except Exception as e:
print("Exception:", repr(e))
print("Context:  ", repr(e.__context__))
print("Cause:    ", repr(e.__cause__))
print("Suppress: ", repr(e.__suppress_context__))

>>>
Looking up 'my key 6' in server
Exception: MissingError()
Context:   ServerMissingKeyError()
Cause:     KeyError('my key 6')
Suppress:  True
```

遍历 `__cause__` 和 `__suppress_context__` 的异常链遍历行为仅对 Python 的内置异常打印程序可用。如果您使用 `traceback` 模块自行处理 `Exception` 堆栈跟踪（请参见 [Item 87](#ch10#ch10lev1sec8): “[使用 traceback 进行增强的异常报告](#ch10#ch10lev1sec8)”），您可能会注意到链接的异常数据似乎丢失了：

![](./images/f0434-03.png)
```python
import traceback

try:
lookup("my key 7")
except Exception as e:
stack = traceback.extract_tb(e.__traceback__)

for frame in stack:
print(frame.line)

>>>
Looking up 'my key 7' in server
lookup('my key 7')
raise MissingError        # Convert the server error
```

为了提取与 Python 为未处理异常打印的相同链接异常信息，您需要正确考虑每个异常的 `__cause__` 和 `__context__` 属性：

![](./images/f0435-02.png)
```python
def get_cause(exc):
if exc.__cause__ is not None:
return exc.__cause__
elif not exc.__suppress_context__:
return exc.__context__
else:
return None
```

`get_cause` 函数可以在循环或递归中应用，以构建完整的链接异常堆栈：

![](./images/f0435-03.png)
```python
try:
lookup("my key 8")
except Exception as e:
while e is not None:
stack = traceback.extract_tb(e.__traceback__)
for i, frame in enumerate(stack, 1):
print(i, frame.line)
e = get_cause(e)
if e:
print("Caused by")

>>>
Looking up 'my key 8' in server
1 lookup('my key 8')
2 raise MissingError        # Convert the server error
Caused by
1 result = contact_server(my_key)
2 raise ServerMissingKeyError
Caused by
1 return my_dict[my_key]
```

另一种缩短 `MissingError` 异常链的替代方法是抑制 `contact_server` 中引发的 `ServerMissingKeyError` 的 `KeyError` 源。我在这里通过在相应的 `raise` 语句中使用 `from None` 子句来实现这一点：

![](./images/f0436-01.png)
```python
def contact_server(key):
...
raise ServerMissingKeyError from None  # Suppress
...
```

再次调用 `lookup` 函数，我可以确认 `KeyError` 不再出现在 Python 的默认异常处理输出中：

![](./images/f0436-02.png)
```python
print(lookup("my key 9"))

>>>
Traceback ...

ServerMissingKeyError

The above exception was the direct cause of the following
➥exception:

Traceback ...
MissingError
```

#### 记住的事项

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 当从 `except` 子句中引发异常时，该处理程序的原始异常将始终保存到新引发的 `Exception` 值 的 `__context__` 属性中。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `raise` 语句中的 `from` 子句允许您通过设置 `__cause__` 属性来显式指示先前引发的异常是新引发异常的原因。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 显式地将一个异常链接到另一个异常将导致 Python 只打印提供的原因（或缺乏原因），而不是自动链接的异常。

### Item 89: 始终将资源传递给生成器并让调用者在外部清理它们

Python 提供了各种工具，例如异常处理程序（请参见 [Item 80](#ch10#ch10lev1sec1): “[利用 try/except/else/finally 的每个块](#ch10#ch10lev1sec1)”）和 `with` 语句（请参见 [Item 82](#ch10#ch10lev1sec3): “[考虑使用 contextlib 和 with 语句来实现可重用的 try/finally 行为](#ch10#ch10lev1sec3)”），以帮助您确保文件、互斥锁和套接字等资源在正确的时间得到妥善清理。例如，在普通函数中，一个简单的 `finally` 子句将在返回值实际被调用者接收 _之前_ 执行，使其成为可靠关闭文件句柄的理想位置：

![](./images/f0437-01.png)
```python
def my_func():
try:
return 123
finally:
print("Finally my_func")

print("Before")
print(my_func())
print("After")

>>>
Before
Finally my_func
123
After
```

相比之下，在使用生成器函数时（请参见 [Item 43](#ch06#ch06lev1sec4): “[考虑使用生成器而不是返回列表](#ch06#ch06lev1sec4)”），`finally` 子句要等到 `StopIteration` 异常被引发以指示值序列已耗尽（请参见 [Item 21](#ch03#ch03lev1sec5): “[在迭代参数时要谨慎](#ch03#ch03lev1sec5)”）。这意味着 `finally` 子句是在最后一个项目被调用者接收 _之后_ 执行的，与普通函数不同：

![](./images/f0437-02.png)
```python
def my_generator():
try:
yield 10
yield 20
yield 30
finally:
print("Finally my_generator")

print("Before")
for i in my_generator():
print(i)

print("After")

>>>
Before
10
20
30
Finally my_generator
After
```

但是，Python 生成器也可能不会被完全迭代。理论上，这可能会阻止 `StopIteration` 异常被引发，从而阻止 `finally` 子句的执行。我在这里通过手动步进生成器函数的迭代器来模拟此行为；请注意，“Finally my_generator” 没有打印出来：

```python
it = my_generator()
print("Before")
print(next(it))
print(next(it))
print("After")

>>>
Before
10
20
After
```

`finally` 子句尚未执行。它何时会执行？答案是取决于：它可能永远不会运行。如果迭代器的最后一个引用被删除，垃圾回收被启用，并且运行了一个收集周期，那么生成器的 `finally` 子句应该会执行：

```python
import gc
del it
gc.collect()

>>>
Finally my_generator
```

此机制的动力是 `GeneratorExit` 异常，它继承自 `BaseException`（请参见 [Item 86](#ch10#ch10lev1sec7): “[理解 Exception 和 BaseException 之间的区别](#ch10#ch10lev1sec7)”）。在垃圾回收时，如果生成器未耗尽，Python 将此特殊类型的异常发送到生成器中（有关背景信息，请参见 [Item 46](#ch06#ch06lev1sec7): “[将迭代器作为参数传递给生成器而不是调用 send 方法](#ch06#ch06lev1sec7)”）。通常这会导致生成器返回并清除其堆栈，但技术上您可以捕获此类型的异常并处理它：

![](./images/f0438-02.png)
```python
def catching_generator():
try:
yield 40
yield 50
yield 60
except BaseException as e:  # Catches GeneratorExit
print("Catching handler", type(e), e)
raise
```

在异常处理程序的末尾，我使用裸 `raise` 关键字，不带参数，以确保 `GeneratorExit` 异常传播并且 Python 的运行时机制不会中断。我在这里步进这个新的生成器，然后触发另一个垃圾收集周期：

![](./images/f0439-02.png)
```python
it = catching_generator()
print("Before")
print(next(it))
print(next(it))
print("After")
del it
gc.collect()

>>>
Before
40
50
After
Catching handler <class 'GeneratorExit'>
```

异常处理程序由 `gc` 模块单独运行，而不是在创建生成器并步进它的原始调用堆栈中运行。如果在处理 `GeneratorExit` 异常时引发了另一个异常会怎样？我在这里定义了另一个生成器来演示这种可能性：

![](./images/f0439-03.png)
```python
def broken_generator():
try:
yield 70
yield 80
except BaseException as e:
print("Broken handler", type(e), e)
raise RuntimeError("Broken")

it = broken_generator()
print("Before")
print(next(it))
print("After")
del it
gc.collect()
print("Still going")

>>>
Before
70
After
Exception ignored in: <generator object broken_generator at
➥ 0x10099b2e0>
Traceback ...
RuntimeError: Broken
Broken handler <class 'GeneratorExit'>
Still going
```

这个结果令人惊讶：`gc` 模块捕获了 `broken_generator` 引发的 `RuntimeError` 并将其打印到 `sys.stderr`。异常不会重新引发到调用 `gc.collect` 的主线程中。相反，它被完全吞没并隐藏在程序的其余部分之外，程序继续运行。这意味着您不能依赖异常处理程序或生成器中的 `finally` 子句来始终执行并向调用者报告错误。

为了解决这种潜在的风险，您可以将需要清理的资源分配在生成器函数之外，并将它们作为参数传递。例如，假设我正在尝试构建一个简单的实用程序，该实用程序查找文件中前五行中最长的长度。我在这里定义了一个简单的生成器，它在给定文件路径的情况下生成行长度：

![](./images/f0440-02.png)
```python
def lengths_path(path):
try:
with open(path) as handle:
for i, line in enumerate(handle):
print(f"Line {i}")
yield len(line.strip())
finally:
print("Finally lengths_path")
```

我可以在循环中使用生成器来计算最大值，然后提前终止循环，将 `lengths_path` 生成器保留在部分执行状态：

![](./images/f0440-03.png)
```python
max_head = 0
it = lengths_path("my_file.txt")

for i, length in enumerate(it):
if i == 5:
break
else:
max_head = max(max_head, length)

print(max_head)

>>>
Line 0
Line 1
Line 2
Line 3
Line 4
Line 5
99
```

在生成器迭代器稍后超出范围后，它将被垃圾回收，并且 `finally` 子句将如预期地运行：

```python
del it
gc.collect()

>>>
Finally lengths_path
```

这种延迟行为是我试图避免的。我需要 `finally` 在原始循环的调用堆栈中运行，以便如果遇到任何错误，它们都会被正确地引发给调用者。这对于必须避免死锁的互斥锁等资源尤其重要。为了实现正确的行为，我可以将打开的文件句柄传递给生成器函数：

![](./images/f0441-02.png)
```python
def lengths_handle(handle):
try:
for i, line in enumerate(handle):
print(f"Line {i}")
yield len(line.strip())
finally:
print("Finally lengths_handle")
```

我可以在循环周围使用 `with` 语句来确保文件被可靠地立即打开和关闭，这样生成器就不必自己管理文件句柄了：

![](./images/f0441-03.png)
```python
max_head = 0

with open("my_file.txt") as handle:
it = lengths_handle(handle)
for i, length in enumerate(it):
if i == 5:
break
else:
max_head = max(max_head, length)

print(max_head)
print("Handle closed:", handle.closed)

>>>
Line 0
Line 1
Line 2
Line 3
Line 4
Line 5
99
Handle closed: True
```

再次，由于循环迭代在耗尽之前结束，生成器函数尚未退出，`finally` 子句也尚未执行。但对于这种不同的方法来说，这没关系，因为我不依赖生成器来执行任何重要的清理工作。

`GeneratorExit` 异常代表了正确性和系统健康之间的折衷。如果生成器最终不会退出，所有过早停止的生成器都会泄漏内存并可能导致程序崩溃。吞噬错误是 Python 所做的权衡，因为这在大多数情况下是合理的。但由您来确保您的生成器期望这种行为并据此进行计划。

#### 记住的事项

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在普通函数中，`finally` 子句在返回值之前执行，但在生成器函数中，`finally` 子句仅在耗尽后运行，当 `StopIteration` 异常被引发时。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 为了防止内存泄漏，垃圾回收器会将 `GeneratorExit` 异常注入到未引用的、部分迭代的生成器中，以使其退出并释放资源。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 由于这种行为，将资源（如文件和互斥锁）传递给生成器函数通常比依赖它们来分配和清理资源更可取。

### Item 90: 切勿将 `__debug__` 设置为 `False`

当您在 Python 程序中添加类似这样的 `assert` 语句时：

![](./images/f0442-02.png)
```python
n = 3
assert n % 2 == 0, f"{n=} not even"
```

它基本上等同于以下代码：

![](./images/f0443-01.png)
```python
if __debug__:
if not (n % 2 == 0):
raise AssertionError(f"{n=} not even")

>>>
Traceback ...
AssertionError: n=3 not even
```

您还可以直接使用 `__debug__` 全局内置变量来控制更复杂的验证代码的执行：

![](./images/f0443-02.png)
```python
def expensive_check(x):
...

items = [1, 2, 3]
if __debug__:
for i in items:
assert expensive_check(i), f"Failed {i=}"

>>>
Traceback ...
AssertionError: Failed i=2
```

在 Python 启动时通过指定 `-O` 命令行参数来设置 `__debug__` 内置全局变量为 `False` 是唯一的方法。例如，这里有一个 Python 调用，它将以 `__debug__` 等于 `True`（默认值）开始：

![](./images/f0443-03.png)
```python
$ python3 -c 'assert False, "FAIL"; print("OK")'
Traceback ...
AssertionError: FAIL
```

添加 `-O` 命令行选项会导致 `assert` 语句被完全跳过，从而产生不同的输出：

![](./images/f0443-05.png)
```python
$ python3 -O -c 'assert False, "FAIL"; print("OK")'
OK
```

尽管 Python 是一种极其动态的语言（请参见 [Item 3](#ch01#ch01lev1sec3): “[切勿期望 Python 在编译时检测错误](#ch01#ch01lev1sec3)”），但它不允许您在运行时修改 `__debug__` 的值：

![](./images/f0443-04.png)
```python
__debug__ = False

>>>
Traceback ...
SyntaxError: cannot assign to __debug__
```

如果 `__debug__` 常量为 `True`，则在程序生命周期内它将始终保持不变。

`__debug__` 标志的初衷是允许用户通过在运行时跳过看似不必要的断言来优化代码性能。然而，随着时间的推移，越来越多的代码，尤其是常见的框架和库，已经依赖于断言来在程序启动时和运行时验证假设。通过禁用 `assert` 语句和其他调试代码，您正在为微不足道的实际收益而损害程序的有效性。

如果性能是您追求的目标，那么有更好的方法可以使程序更快（请参见 [Item 92](#ch11#ch11lev1sec1): “[优化前进行性能分析](#ch11#ch11lev1sec1)” 和 [Item 94](#ch11#ch11lev1sec3): “[了解何时以及如何用另一种编程语言替换 Python](#ch11#ch11lev1sec3)”）。如果您有非常昂贵的验证代码需要在运行时禁用，那么请创建自己的 `enable_debug` 辅助函数和相关的全局变量来控制您自己的代码中的这些调试操作，而不是依赖 `__debug__`。

即使在需要榨取代码的每一丝性能时，尤其是在低级代码中，例如在使用 MicroPython 为微控制器（<https://micropython.org>）时，始终保持断言活动仍然有价值。有些反直觉的是，`assert` 语句的存在即使在断言本身未失败时也有助于调试。当您收到错误报告时，您可以使用成功通过的断言来排除可能性并缩小问题范围。

最终，断言是确保正确性的强大工具，应在您的代码中广泛使用，以帮助明确假设。

#### 记住的事项

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 默认情况下，`__debug__` 全局内置变量为 `True`，Python 程序将执行所有 `assert` 语句。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `-O` 命令行标志可用于将 `__debug__` 设置为 `False`，这会导致忽略 `assert` 语句。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 存在 `assert` 语句即使在断言本身未失败时也有助于缩小错误的根源。

### Item 91: 除非您正在构建开发人员工具，否则避免使用 `exec` 和 `eval`

Python 是一种动态语言，允许您在运行时执行几乎任何操作（这可能会导致问题；请参见 [Item 3](#ch01#ch01lev1sec3): “[切勿期望 Python 在编译时检测错误](#ch01#ch01lev1sec3)”）。它的许多功能都支持这些极其灵活的功能，例如 `setattr`/`getattr`/`hasattr`（请参见 [Item 61](#ch08#ch08lev1sec4): “[使用 \_\_getattr\_\_、\_\_getattribute\_\_ 和 \_\_setattr\_\_ 进行惰性属性访问](#ch08#ch08lev1sec4)”）、元类（请参见 [Item 64](#ch08#ch08lev1sec7): “[使用 \_\_set\_name\_\_ 注释类属性](#ch08#ch08lev1sec7)”）和描述符（请参见 [Item 60](#ch08#ch08lev1sec3): “[使用描述符实现可重用的 @property 方法](#ch08#ch08lev1sec3)”）。

然而，所有功能中最动态的是在运行时从字符串执行任意代码。这在 Python 中可以使用 `eval` 和 `exec` 内置函数来实现。

`eval` 接受一个字符串作为单个表达式，并将其评估结果作为普通 Python 对象返回：

```python
x = eval("1 + 2")
print(x)

>>>
3
```

将语句传递给 `eval` 将导致错误：

![](./images/f0445-01.png)
```python
eval(
"""
if True:
print('okay')
else:
print('no')
""""""
)

>>>
Traceback ...
SyntaxError: invalid syntax (<string>, line 2)
```

相反，您可以使用 `exec` 来动态评估更大的 Python 代码块。`exec` 始终返回 `None`，并且要从中获取数据，您需要使用全局和局部作用域字典参数。在这里，当我访问 `my_condition` 变量时，它会冒泡到全局作用域进行解析，并且我的 `x` 变量赋值在局部作用域中完成（有关背景信息，请参见 [Item 33](#ch05#ch05lev1sec4): “[了解闭包如何与变量作用域和 nonlocal 交互](#ch05#ch05lev1sec4)”）：

![](./images/f0445-02.png)
```python
global_scope = {"my_condition": False}
local_scope = {}
exec(     """
if my_condition:
x = 'yes'
else:
x = 'no'
""",
global_scope,
local_scope,
)
print(local_scope)

>>>
{'x': 'no'}
```

如果您在其他正常的应用程序代码库中发现 `eval` 或 `exec`，这通常是一个危险信号，表明有些事情严重错误。如果这些功能无意中连接到允许攻击者访问的输入通道，它们可能会导致严重的安全性问题。即使对于插件架构，这些功能似乎也自然适用，Python 也有更好的方法来实现类似的结果（请参见 [Item 98](#ch11#ch11lev1sec7): “[惰性加载模块以减少启动时间](#ch11#ch11lev1sec7)”）。

实际上适合使用 `eval` 和 `exec` 的唯一时间是支持您的应用程序以改善开发体验的代码，例如调试器、笔记本系统、交互式运行求值打印循环 (REPL)、性能基准测试工具、代码生成实用程序等。对于任何其他目的，请避免这些不安全的功能，而是使用 Python 的其他动态和元编程功能。

#### 记住的事项

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `eval` 允许您执行包含 Python 表达式的字符串并捕获其返回值。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `exec` 允许您执行 Python 代码块并影响变量作用域和周围环境。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 由于潜在的安全风险，这些功能应很少使用或从不使用，仅限于改善开发体验。
---
<a role="toc_link" id="ch11"></a>

## Effective Python - 11

## 11

本章深入探讨了 Graph Neural Networks (GNNs) 在处理和理解图结构数据方面的强大能力，并重点介绍了 Graph Foundation Models (GFMs) 的兴起及其在各种图相关任务中的潜力。我们将从 GNNs 的基本原理和核心组件入手，逐步深入到更复杂的模型架构和应用场景。

**1. Graph Neural Networks (GNNs) 的基础**

GNNs 的核心思想是通过 **Message Passing** 机制，让图中的节点能够聚合其邻居节点的信息，从而学习到具有丰富拓扑信息的 **Node Embedding**。这个过程可以迭代进行，使得节点能够捕获到更远距离的结构信息。

*   **节点表示 (Node Representation):** GNNs 的目标是学习到能够捕捉节点自身特征和其在图结构中位置信息的低维向量表示，即 Node Embedding。
*   **Message Passing:** 这是 GNNs 的核心机制。在每一轮 Message Passing 中，节点会将其当前的状态（或称为消息）发送给它的邻居，并接收来自邻居的消息。然后，节点会根据接收到的消息更新自己的状态。
*   **聚合函数 (Aggregation Function):** 在接收来自邻居的消息后，节点需要一个聚合函数来合并这些消息。常见的聚合函数包括求和 (sum)、平均 (mean) 和最大值 (max)。
*   **更新函数 (Update Function):** 聚合后的消息会与节点自身的表示结合，并通过一个更新函数来产生新的节点表示。这通常是一个神经网络层，如多层感知机 (MLP)。

**2. 经典的 GNN 模型**

本节将介绍一些具有代表性的 GNN 模型，它们在 GNNs 的发展历程中起到了关键作用：

*   **Graph Convolutional Networks (GCN):** GCN 是最早也是最受欢迎的 GNN 模型之一。它通过对邻居节点的特征进行加权平均来实现卷积操作，从而学习节点表示。GCN 的一个重要特点是其谱域的定义，但更常见的实现方式是空间域的近似。
*   **Graph Attention Networks (GAT):** GAT 引入了注意力机制，允许模型在聚合邻居信息时为不同的邻居分配不同的权重。这使得 GAT 能够更好地处理具有不同重要性程度的邻居节点，尤其是在异质图 (Heterogeneous Graph) 中。
*   **GraphSAGE:** GraphSAGE 是一种归纳式 (inductive) 的 GNN 模型，它不依赖于整个图的结构信息，而是通过采样邻居节点来学习节点表示。这使得 GraphSAGE 能够处理大规模图，并且能够对未见过的节点进行预测。

**3. Graph Foundation Models (GFMs)**

随着 GNNs 的发展，研究者们开始探索构建能够泛化到多种图任务的 **Graph Foundation Models (GFMs)**。GFMs 的目标是通过在海量图数据上进行 **Pre-training**，学习到通用的图表示能力，然后通过 **Fine-tuning** 或 **In-context Learning** 等方式快速适应下游任务。

*   **Pre-training 策略:** GFMs 通常采用 **Self-supervised Learning** 的方式进行预训练。常见的预训练任务包括：
*   **Contrastive Learning:** 通过最大化相似图的表示，最小化不相似图的表示来学习图的全局表示。
*   **Masked Graph Modeling:** 类似于 Transformer 中的 Masked Language Modeling，随机遮盖图中的节点或边，然后让模型预测被遮盖的部分。
*   **Link Prediction:** 预测图中节点之间是否存在连接。
*   **下游任务的适应:**
*   **Fine-tuning:** 在预训练模型的基础上，针对特定的下游任务（如 **Graph Classification**, **Node Classification**, **Link Prediction**）进行微调。
*   **Few-shot Learning / Zero-shot Learning:** 利用预训练模型强大的泛化能力，在只有少量甚至没有标注数据的情况下完成任务。
*   **In-context Learning:** 直接将任务描述和少量示例输入到预训练模型中，无需更新模型参数即可获得预测结果。

**4. GFMs 的应用与挑战**

GFMs 在各种图相关的任务中展现出巨大的潜力，包括但不限于：

*   **知识图谱 (Knowledge Graph) 补全和推理**
*   **药物发现和分子性质预测**
*   **社交网络分析**
*   **推荐系统**
*   **交通流量预测**
*   **图生成 (Graph Generation)**
*   **图异常检测 (Graph Anomaly Detection)**

然而，GFMs 的发展也面临一些挑战：

*   **大规模图的处理:** 如何高效地处理包含数十亿节点和边的超大规模图仍然是一个难题。
*   **异质图 (Heterogeneous Graph) 的建模:** 现实世界中的图往往是异质的，包含多种类型的节点和边，如何有效地建模和学习异质图的表示是 GFMs 的一个重要研究方向。
*   **跨领域迁移 (Cross-domain Transfer) 和领域适应 (Domain Adaptation):** 如何将在一个领域预训练的 GFMs 有效地迁移到另一个领域，或者在目标领域进行有效的领域适应，是提升 GFMs 泛化能力的关键。
*   **可解释性:** GNNs 和 GFMs 的黑箱特性使得其决策过程难以解释，提高模型的可解释性对于其在关键领域的应用至关重要。
*   **图同构 (Graph Isomorphism) 问题:** 尽管 GNNs 在许多任务上表现出色，但它们在区分同构图方面存在局限性，这是 GNNs 的一个理论挑战。

**5. 未来展望**

GFMs 代表了图学习领域的一个重要发展方向。未来的研究将继续聚焦于构建更大、更通用的图模型，探索更有效的预训练和微调策略，并将其应用于更广泛的实际问题。 **Multi-modal Learning** 与 GFMs 的结合，例如将图数据与文本、图像等其他模态的数据结合起来进行学习，也将是 GFMs 未来发展的重要方向。此外，对 GNNs 和 GFMs 的理论基础进行更深入的探索，例如理解其表达能力和局限性，也将推动该领域的持续进步。

## Effective Python - Performance

# Effective Python - Performance

## Performance

程序执行质量的衡量标准多种多样，包括 CPU 利用率、吞吐量、延迟、响应时间、内存使用和缓存命中率。这些指标还可以根据其统计分布以不同的方式进行评估。例如，对于延迟，根据您的目标，您可能需要考虑平均延迟、中位数延迟、99% 百分位延迟或最坏情况延迟。还有一些特定于应用程序的指标，它们建立在这些较低级别的指标之上，例如每秒事务数、首次绘制时间、最大帧率和有效吞吐量。

实现良好的**performance**意味着您编写的代码能够满足您最关心的量化测量值的一个或多个方面的期望。哪些指标很重要取决于问题域、生产环境和用户画像；没有一种放之四海而皆准的目标。**Performance engineering**是一门分析程序执行行为、识别改进领域并实施各种规模的更改以最大化或最小化最重要指标的学科。

Python 不被认为是一种高性能语言，尤其是与为该任务构建的低级语言相比。考虑到 Python 运行时（runtime）的开销和限制，这种声誉是可以理解的，尤其是在并行性方面（参见 [Item 68](#ch09#ch09lev1sec2): “[Use Threads for Blocking I/O; Avoid for Parallelism](#ch09#ch09lev1sec2)” 获取背景信息）。尽管如此，Python 包含多种功能，可以使程序以相对较少的努力实现令人惊讶的impressive performance。利用这些功能，可以在保留 Python 高级特性的生产力优势的同时，从宿主系统（host system）中提取最大性能。

### Item 92: Profile Before Optimizing

Python 的动态特性会导致其运行时性能出现令人惊讶的行为。您可能认为很慢的操作实际上非常快（例如，字符串操作、生成器的使用）。您可能认为很快的语言特性实际上非常慢（例如，属性访问、函数调用）。Python 程序中减速的真正根源可能很隐蔽。

最佳方法是忽略您的直觉，在尝试优化程序之前直接测量其性能。Python 提供了一个内置的**profiler**，用于确定程序中哪些部分是其执行时间的原因。Profiling 使您能够将优化工作集中在最大的麻烦来源上，并忽略对速度没有影响的程序部分（即遵循学术文献中的 Amdahl 定律）。

例如，假设我想确定程序中的一个算法为什么慢。这里我定义了一个使用插入排序（insertion sort）对数据列表进行排序的函数：
[Click here to view code image](#ch11_images#f0448-01)
```
def insertion_sort(data):
result = []
for value in data:
insert_value(result, value)
return result
```
插入排序的核心机制是用于为每块数据查找插入点的函数。这里我定义了一个极其低效的 `insert_value` 函数版本，它会对输入数组进行线性扫描：
[Click here to view code image](#ch11_images#f0448-02)
```
def insert_value(array, value):
for i, existing in enumerate(array):
if existing > value:
array.insert(i, value)
return
array.append(value)
```
为了对 `insertion_sort` 和 `insert_value` 进行 profiling，我创建了一个随机数数据集，并定义了一个 `test` 函数传递给 profiler（参见 [Item 39](#ch05#ch05lev1sec10): “[Prefer functools.partial over lambda Expressions for Glue Functions](#ch05#ch05lev1sec10)” 获取关于 `lambda` 的背景信息）：
[Click here to view code image](#ch11_images#f0448-03)
```
from random import randint

max_size = 12**4
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)
```
Python 提供了两个内置 profiler：一个是纯 Python 的（`profile`），另一个是 C 扩展模块（`cProfile`）。`cProfile` 内置模块更好，因为它在程序被 profiling 时对程序性能的影响最小。纯 Python 的替代方案会产生高开销，从而扭曲结果。

**Note**
在 profiling Python 程序时，请确保您测量的是代码本身，而不是任何外部系统。注意访问网络或磁盘资源的函数。这些函数由于底层系统的缓慢而可能对程序的执行时间产生重大影响。如果您的程序使用缓存来掩盖这些慢速资源的延迟，您还应确保在开始 profiling 之前对其进行适当的预热。

这里我从 `cProfile` 模块实例化一个 `Profile` 对象，并通过 `runcall` 方法运行测试函数：
```
from cProfile import Profile

profiler = Profile()
profiler.runcall(test)
```
当测试函数运行完成后，我可以使用 `pstats` 内置模块及其 `Stats` 类来提取其性能统计信息。`Stats` 对象上的各种方法可以调整如何选择和排序 profiling 信息，只显示我关心的内容：
```
from pstats import Stats

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats("cumulative")
stats.print_stats()
```
输出是一个按函数组织的表格信息。数据样本仅来自 profiler 激活的时间，即上述 `runcall` 方法期间：
[Click here to view code image](#ch11_images#f0449-02)
```

>>>
41475 function calls in 2.198 seconds

Ordered by: cumulative time

ncalls tottime percall cumtime percall filename:lineno(function)
1   0.000   0.000   2.198   2.198 main.py:35(<lambda>)
1   0.003   0.003   2.198   2.198 main.py:10(insertion_sort)
20736   2.137   0.000   2.195   0.000 main.py:20(insert_value)
20729   0.058   0.000   0.058   0.000 {method 'insert' of 'list' objects}
7   0.000   0.000   0.000   0.000 {method 'append' of 'list' objects}
```
以下是 profiler 统计列含义的快速指南：
*   `**ncalls**`**：**在 profiling 期间调用函数的次数。
*   `**tottime**`**：**执行函数所花费的秒数，不包括执行它调用的其他函数所花费的时间。
*   `**tottime percall**`**：**每次调用函数时在函数中花费的平均秒数，不包括执行它调用的其他函数所花费的时间。这是 `tottime` 除以 `ncalls`。
*   `**cumtime**`**：**执行函数所花费的累积秒数，包括执行它调用的所有其他函数所花费的时间。
*   `**cumtime percall**`**：**每次调用函数时在函数中花费的平均秒数，包括执行它调用的所有其他函数所花费的时间。这是 `cumtime` 除以 `ncalls`。

查看上面的 profiler 统计表，我可以看到我测试中最大的 CPU 使用是 `insert_value` 函数中花费的累积时间。这里我重新定义该函数以使用更高效的 `bisect` 内置模块（参见 [Item 102](#ch12#ch12lev1sec3): “[Consider Searching Sorted Sequences with bisect](#ch12#ch12lev1sec3)”）：
[Click here to view code image](#ch11_images#f0450-02)
```
from bisect import bisect_left

def insert_value(array, value):
i = bisect_left(array, value)
array.insert(i, value)
```
我可以再次运行 profiler 并生成新的 profiler 统计表。新函数快得多，累积花费的时间比以前的 `insert_value` 函数小近 40 倍：
[Click here to view code image](#ch11_images#f0450-03)
```
>>>
62211 function calls in 0.067 seconds

Ordered by: cumulative time

ncalls tottime percall cumtime percall filename:lineno(function)
1   0.000   0.000   0.067   0.067 main.py:35(<lambda>)
1   0.002   0.002   0.067   0.067 main.py:10(insertion_sort)
20736   0.004   0.000   0.064   0.000 main.py:109(insert_value)
20736   0.056   0.000   0.056   0.000 {method 'insert' of 'list' objects}
20736   0.004   0.000   0.004   0.000 {built-in method _bisect.bisect_left}
```
有时，当您 profiling 整个程序时，您可能会发现一个通用的实用函数（utility function）占用了大部分执行时间。Profiler 的默认输出使得这种情况难以理解，因为它没有显示该实用函数被程序中的多个不同部分调用。

例如，这里 `my_utility` 函数被程序中的两个不同函数反复调用：
```
def my_utility(a, b):
c = 1
for i in range(100):
c += a * b

def first_func():
for _ in range(1000):
my_utility(4, 5)

def second_func():
for _ in range(10):
my_utility(1, 3)

def my_program():
for _ in range(20):
first_func()
second_func()
```
Profiling 此代码并使用默认的 `print_stats` 输出会产生令人困惑的统计信息：
[Click here to view code image](#ch11_images#f0451-01)
```
>>>
20242 function calls in 0.040 seconds

Ordered by: cumulative time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1    0.000    0.000    0.040    0.040 main.py:172(my_program)
20    0.002    0.000    0.040    0.002 main.py:164(first_func)
20200    0.038    0.000    0.038    0.000 main.py:159(my_utility)
20    0.000    0.000    0.000    0.000 main.py:168(second_func)
```
`my_utility` 函数显然是大部分执行时间的原因，但并不清楚为什么该函数被调用如此之多。如果您搜索程序的代码，您会发现 `my_utility` 的多个调用点，并且仍然会感到困惑。

为了解决这个问题，Python profiler 提供了 `print_callers` 方法来显示哪些调用者为每个函数的 profiling 信息做出了贡献：
```
stats.print_callers()
```
此 profiler 统计表显示左侧是调用的函数，右侧是负责进行调用的函数。这里很清楚 `my_utility` 被 `first_func` 使用最多：
[Click here to view code image](#ch11_images#f0452-01)
```
>>>
Ordered by: cumulative time

Function                      was called by...
ncalls  tottime  cumtime
main.py:172(my_program)       <-
main.py:164(first_func)       <-      20    0.002  0.040  main.py:172(my_program)
main.py:159(my_utility)       <-   20000    0.038  0.038  main.py:164(first_func)
200    0.000  0.000  main.py:168(second_func)
main.py:168(second_func)      <-      20    0.000  0.000
```
或者，您可以调用 `print_callees` 方法，该方法显示一个自顶向下的细分，说明每个函数（左侧）如何花费时间执行其他依赖函数（右侧），这些函数在调用堆栈中更深：
[Click here to view code image](#ch11_images#f0452-02)
```
stats.print_callees()

>>>
callees
Ordered by: cumulative time

Function                      called...
ncalls  tottime  cumtime
main.py:172(my_program)       ->      20    0.002    0.041  Profiling.md:164(first_func)
20    0.000    0.000  Profiling.md:168(second_func)
main.py:164(first_func)       ->   20000    0.038    0.038  Profiling.md:159(my_utility)
main.py:159(my_utility)       ->
main.py:168(second_func)      ->     200    0.000    0.000  Profiling.md:159(my_utility)
```
如果您无法使用 `cProfile` 找出程序缓慢的原因，请不要担心。Python 还包含其他用于评估性能的工具（参见 [Item 93](#ch11#ch11lev1sec2): “[Optimize Performance-Critical Code Using timeit Microbenchmarks](#ch11#ch11lev1sec2)”、“[Item 98](#ch11#ch11lev1sec7): “[Lazy-Load Modules with Dynamic Imports to Reduce Startup Time](#ch11#ch11lev1sec7)” 和 [Item 115](#ch13#ch13lev1sec8): “[Use tracemalloc to Understand Memory Usage and Leaks](#ch13#ch13lev1sec8)”)。还有社区构建的工具（参见 [Item 116](#ch14#ch14lev1sec1): “[Know Where to Find Community-Built Modules](#ch14#ch14lev1sec1)”），它们具有额外的性能评估功能，例如行 profiler、采样 profiler、与 Linux 的 `perf` 工具集成、内存使用 profiler 等。

#### Things to Remember
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在优化 Python 程序之前对其进行 profiling 很重要，因为减速的根源通常很隐蔽。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `cProfile` 模块而不是 `profile` 模块，因为它提供了更准确的 profiling 信息。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `Profile` 对象的 `runcall` 方法提供了对单个函数调用树进行 profiling 所需的一切。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `Stats` 对象允许您选择和打印您需要查看的 profiling 信息子集，以了解程序的性能。

### Item 93: Optimize Performance-Critical Code Using `timeit` Microbenchmarks

在尝试最大化 Python 程序性能时，使用 profiler 至关重要，因为缓慢的根源可能不明显（参见 [Item 92](#ch11#ch11lev1sec1): “[Profile Before Optimizing](#ch11#ch11lev1sec1)”)。一旦确定了真正的问题区域，重构为更好的架构或使用更合适的数据结构通常会产生显著效果（参见 [Item 104](#ch12#ch12lev1sec5): “[Know How to Use heapq for Priority Queues](#ch12#ch12lev1sec5)”)。然而，即使经过多次 profiling 和优化，一些代码热点（hotspots）可能仍然难以解决。在尝试更复杂的解决方案之前（参见 [Item 94](#ch11#ch11lev1sec3): “[Know When and How to Replace Python with Another Programming Language](#ch11#ch11lev1sec3)”)，值得考虑使用 `timeit` 内置模块来运行**microbenchmarks**。

`timeit` 的目的是精确测量小代码片段的性能。它允许您量化和比较同一特定问题的多种解决方案。虽然 profiling 和全程序基准测试有助于发现大型组件的优化空间，但如此广泛的潜在改进可能无限且探索成本高昂。相比之下，microbenchmarks 可用于测量同一狭窄定义行为的多种实现，从而使您能够以科学方法寻找性能最佳的解决方案。

使用 `timeit` 模块很简单。这里我测量将两个整数相加所需的时间：
[Click here to view code image](#ch11_images#f0454-01)
```
import timeit

delay = timeit.timeit(stmt="1+2")
print(delay)

>>>
0.003767708025407046
```
返回值是运行 `stmt` 参数中提供的代码片段 100 万次迭代所需的时间（秒）。默认的重复次数对于较慢的 microbenchmarks 可能过多，因此 `timeit` 允许您使用 `number` 参数指定更合适的次数：
[Click here to view code image](#ch11_images#f0454-02)
```
delay = timeit.timeit(stmt="1+2", number=100)
print(delay)

>>>
7.500057108700275e-07
```
然而，上面指定的 100 次迭代太少，以至于测量的 microbenchmark 时间可能会消失在计算机噪声中。由于其他进程干扰内存和缓存状态、操作系统运行周期性后台任务、接收硬件中断等，性能总会有一些自然变化。为了使 microbenchmark 准确，它需要使用大量的迭代来补偿这种噪声。`timeit` 模块在执行代码片段时还会禁用垃圾回收（garbage collection），以尽量减少方差。

我建议显式提供迭代次数参数。我通常将其分配给一个变量，稍后再次使用它来计算每次迭代的平均时间。这个归一化值可以作为稳健的指标，如果需要，可以与其他实现进行比较，或者随时间跟踪（例如，检测回归）：
[Click here to view code image](#ch11_images#f0454-03)
```
count = 1_000_000

delay = timeit.timeit(stmt="1+2", number=count)

print(f"{delay/count*1e9:.2f} nanoseconds")

>>>
4.36 nanoseconds
```
反复运行单个代码片段并不总是足以产生有用的 microbenchmark。您通常需要创建某种脚手架（scaffolding）、工具（harness）或数据结构，以便在迭代期间使用。`timeit` 的 `setup` 参数通过接受一个在所有迭代之前运行一次且不计入时间测量的代码片段来满足此需求。

例如，假设我正在尝试确定一个数字是否存在于一个大的随机值列表中。我不想让 microbenchmark 包含创建大列表和随机化它的时间。这里我将这些前期任务放在 `setup` 代码片段中；我还提供了 `globals` 参数，以便 `stmt` 和 `setup` 可以引用代码中其他地方定义的名称，例如导入的 `random` 模块（参见 [Item 91](#ch10#ch10lev1sec12): “[Avoid exec and eval Unless You’re Building a Developer Tool](#ch10#ch10lev1sec12)” 获取背景信息）：
[Click here to view code image](#ch11_images#f0455-01)
```
import random

count = 100_000

delay = timeit.timeit(
setup="""
numbers = list(range(10_000))
random.shuffle(numbers)
probe = 7_777
""",
stmt="""
probe in numbers
""",
globals=globals(),
number=count,
)

print(f"{delay/count*1e9:.2f} nanoseconds")

>>>
13078.05 nanoseconds
```
有了这个基线（13 毫秒）之后，我可以尝试使用不同的方法来产生相同的行为，看看它如何影响 microbenchmark。这里我将 `setup` 代码片段中创建的列表替换为集合（set）数据结构：
[Click here to view code image](#ch11_images#f0455-02)
```
delay = timeit.timeit(
setup="""
numbers = set(range(10_000))
probe = 7_777
""",
stmt="""
probe in numbers
""",
globals=globals(),
number=count,
)

print(f"{delay/count*1e9:.2f} nanoseconds")

>>>
14.87 nanoseconds
```
这表明在集合中检查成员资格比在列表中检查快约 1000 倍。原因是集合数据结构提供对元素的常数时间访问，类似于 `dict`，而列表需要与其中元素数量成比例的时间。像这样使用 `timeit` 是寻找满足您需求的理想数据结构或算法的好方法。

像这样进行 microbenchmarking 时可能出现的一个问题是需要测量紧密循环（tight loops）的性能，例如在数学内核函数（kernel functions）中。例如，这里我测试对数字列表求和的速度：
[Click here to view code image](#ch11_images#f0456-02)
```
def loop_sum(items):
total = 0
for i in items:
total += i
return total

count = 1000

delay = timeit.timeit(
setup="numbers = list(range(10_000))",
stmt="loop_sum(numbers)",
globals=globals(),
number=count,
)

print(f"{delay/count*1e9:.2f} nanoseconds")

>>>
142365.46 nanoseconds
```
此测量值是每次调用 `loop_sum` 所花费的时间，单独来看没有意义。要使此 microbenchmark 稳健，您需要将其除以内部循环中的迭代次数，在上面的示例中该次数被硬编码为 `10_000`：
[Click here to view code image](#ch11_images#f0457-01)
```
print(f"{delay/count/10_000*1e9:.2f} nanoseconds")

>>>
14.43 nanoseconds
```
现在我可以看到此函数将随着列表中每个附加项的增加而按比例增加 14.43 纳秒。

`timeit` 模块也可以作为命令行工具执行，这可以帮助您快速调查您对 Python 性能的任何好奇之处。例如，假设我想确定查找字典中已存在的键的最快方法（参见 [Item 26](#ch04#ch04lev1sec2): “[Prefer get over in and KeyError to Handle Missing Dictionary Keys](#ch04#ch04lev1sec2)”）。这里我使用 `timeit` 命令行界面来测试为此目的使用 `in` 运算符：
[Click here to view code image](#ch11_images#f0457-02)
```
$ python3 -m timeit \
--setup='my_dict = {"key": 123}' \
'if "key" in my_dict: my_dict["key"]'
20000000 loops, best of 5: 19.3 nsec per loop
```
该工具会自动确定要运行的迭代次数，具体取决于单次迭代花费的时间。它还运行五个单独的测试以补偿系统噪声，并将最小值作为最佳情况、下限性能。

我可以使用不同的代码片段再次运行该工具，以显示 `dict.get` 方法与 `in` 运算符的比较：
[Click here to view code image](#ch11_images#f0457-03)
```
$ python3 -m timeit \
--setup='my_dict = {"key": 123}' \
'if (value := my_dict.get("key")) is not None: value'
20000000 loops, best of 5: 17.1 nsec per loop
```
现在我知道 `get` 比 `in` 快。那么捕获已知异常类型的做法呢？这在 Python 程序中是一种常见的风格（参见 [Item 32](#ch05#ch05lev1sec3): “[Prefer Raising Exceptions to Returning None](#ch05#ch05lev1sec3)”）？
[Click here to view code image](#ch11_images#f0457-04)
```
$ python3 -m timeit \
--setup='my_dict = {"key": 123}' \
'try: my_dict["key"]
except KeyError: pass'
20000000 loops, best of 5: 10.6 nsec per loop
```
事实证明，对于预期已存在于字典中的键，`KeyError` 方法实际上是最快的。这可能令人惊讶，因为在丢失键的情况下引发和捕获异常需要额外的机制。这种不明显的性能行为说明了为什么测试您的假设并使用 profiling 和 microbenchmarks 进行测量然后再优化 Python 代码如此重要。

#### Things to Remember
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `timeit` 内置模块可用于运行 microbenchmarks，帮助您科学地确定程序性能关键部分的最佳数据结构和算法。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 为了使 microbenchmarks 稳健，请使用 `setup` 代码片段排除初始化时间，并确保将返回的测量值归一化为可比较的指标。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `python -m timeit` 命令行界面允许您轻松快速地了解 Python 代码片段的性能。

### Item 94: Know When and How to Replace Python with Another Programming Language

在某个时候使用 Python 时，您可能会觉得您正在挑战它的极限。这是可以理解的，因为为了提供 Python 增强的开发生产力和易用性，该语言的执行模型在其他方面必然是有限制的。例如，CPython 实现的字节码虚拟机（bytecode virtual machine）和全局解释器锁（GIL）会对直线 CPU 性能、CPU 并行性、程序启动时间和整体效率产生负面影响（参见 [Item 68](#ch09#ch09lev1sec2): “[Use Threads for Blocking I/O; Avoid for Parallelism](#ch09#ch09lev1sec2)”）。

一个潜在的解决方案是用另一种编程语言重写所有代码并放弃 Python。在许多情况下，这可能是正确的选择，包括：
* 您的优先级是关键路径延迟（critical path latency）或 99% 百分位延迟，并且您无法容忍垃圾回收暂停或非确定性数据结构行为（例如字典大小调整）。
* 您非常关心程序启动延迟，而预编译（precompilation）、zip 导入（zip imports）和延迟模块加载（late module loading）等技术效果不佳（参见 [Item 97](#ch11#ch11lev1sec6): “[Rely on Precompiled Bytecode and File System Caching to Improve Startup Time](#ch11#ch11lev1sec6)” 和 [Item 98](#ch11#ch11lev1sec7): “[Lazy-Load Modules with Dynamic Imports to Reduce Startup Time](#ch11#ch11lev1sec7)”。
* 您需要利用与实现语言紧密耦合的库 API，例如特定于平台的 GUI 框架，并且通过 C 扩展进行桥接不切实际（参见下面的详细信息）。
* 您需要将程序定位到非典型架构，如超级计算机或嵌入式系统，而 Python 包支持这些环境（例如 <https://mpi4py.github.io> 和 <https://micropython.org>）不足。
* 您需要将程序分发为可安装的可执行文件，而打包工具（参见 [Item 125](#ch14#ch14lev1sec10): “[Prefer Open Source Projects for Bundling Python Programs over zipimport and zipapp](#ch14#ch14lev1sec10)”）不满足您的要求。
* 您已经尝试了下面列出的所有优化技术，以及 Python 语言的替代实现（例如 PyPy: <https://www.pypy.org>），这些技术可以实现更好的性能，但您仍然遇到了性能瓶颈。
* 您已尝试在同一台机器上的多个 Python 进程之间分发计算（参见 [Item 79](#ch09#ch09lev1sec13): “[Consider concurrent.futures for True Parallelism](#ch09#ch09lev1sec13)”）或使用 Dask (<https://www.dask.org>) 等工具跨多台计算机分发计算，但均未成功。

但是，在您承诺重写您构建的软件之前，重要的是考虑使用各种技术进行精确的优化，每种技术都有其独特的权衡。可行性在很大程度上取决于您有多少 Python 代码、其复杂性如何、您面临的限制以及您需要满足的要求。

Python 程序中遇到的许多性能问题都源于不明显的原因。重要的是要对代码进行 profiling 和基准测试（参见 [Item 92](#ch11#ch11lev1sec1): “[Profile Before Optimizing](#ch11#ch11lev1sec1)” 和 [Item 93](#ch11#ch11lev1sec2): “[Optimize Performance-Critical Code Using timeit Microbenchmarks](#ch11#ch11lev1sec2)”）以找到缓慢或过量内存消耗的真正根源（参见 [Item 115](#ch13#ch13lev1sec8): “[Use tracemalloc to Understand Memory Usage and Leaks](#ch13#ch13lev1sec8)”)。您还应该认真研究用更好的替代品替换程序的核心算法和数据结构（参见 [Item 104](#ch12#ch12lev1sec5): “[Know How to Use heapq for Priority Queues](#ch12#ch12lev1sec5)” 和 [Item 102](#ch12#ch12lev1sec3): “[Consider Searching Sorted Sequences with bisect](#ch12#ch12lev1sec3)”)，这些替代品可以以惊人的少量工作量将程序性能提高几个数量级。

一旦您完全用尽了这些途径，就可以通过多种方式迁移到另一种编程语言或执行模型。例如，Python 程序中性能问题的一个常见来源是紧密循环，这在数学**kernel functions**中很常见。以下 Python 代码计算两个向量的点积（dot product），其运行速度将比用 C 实现的类似行为慢几个数量级：
[Click here to view code image](#ch11_images#f0460-01)
```
def dot_product(a, b):
result = 0
for i, j in zip(a, b):
result += i * j
return result

print(dot_product([1, 2], [3, 4]))

>>>
11
```
幸运的是，像这样的内核函数也定义了一个清晰的接口，可以作为慢速和快速程序部分之间的连接点。如果您能找到一种加速 `dot_product` 函数内部实现的方法，那么它所有的调用者都可以受益，而无需您对代码库进行任何其他更改。如果程序的结构允许，相同的方法也适用于更大的子组件。标准版 Python（参见 [Item 1](#ch01#ch01lev1sec1): “[Know Which Version of Python You’re Using](#ch01#ch01lev1sec1)”）提供了两种工具来帮助以这种方式提高性能：
*   `ctypes` 内置模块可以轻松描述系统中本地库（native libraries）的接口并调用它们导出的函数（参见 [Item 95](#ch11#ch11lev1sec4): “[Consider ctypes to Rapidly Integrate with Native Libraries](#ch11#ch11lev1sec4)” 获取详细信息）。这些库可以用任何与 C 调用约定（C calling convention）兼容的语言实现（例如 C、C++、Rust），并且可以利用本地线程、SIMD 指令（SIMD intrinsics）、GPU 等。不需要额外的构建系统、编译器或打包。
*   Python C 扩展 API 允许您创建完全 Pythonic 的 API——利用 Python 的所有动态特性——但实际上是用 C 实现以获得更好的性能（参见 [Item 96](#ch11#ch11lev1sec5): “[Consider Extension Modules to Maximize Performance and Ergonomics](#ch11#ch11lev1sec5)” 获取详细信息）。这种方法通常需要更多前期工作，但它提供了极大的改进的人体工程学。但是，您将不得不处理额外的构建复杂性，这可能很困难。

更大的 Python 生态系统也响应了性能优化需求，创建了优秀的库和工具。以下是一些您应该了解的亮点，尽管还有许多其他（参见 [Item 116](#ch14#ch14lev1sec1): “[Know Where to Find Community-Built Modules](#ch14#ch14lev1sec1)”）：
*   NumPy 模块（<https://numpy.org>）使您能够通过符合人体工程学的 Python 函数调用来操作值数组，这些调用在底层使用 BLAS（Basic Linear Algebra Subprograms）来实现高性能和 CPU 并行性。您需要重写一些数据结构才能使用它，但速度提升可能非常巨大。
*   Numba 模块（<https://numba.pydata.org>）在运行时将您现有的 Python 函数 JIT（just-in-time）编译成高度优化的机器指令。您的一些代码可能需要稍作修改，以使用更少的动态性和更简单的数据类型。与 `ctypes` 一样，Numba 避免了额外的构建复杂性，这是一个巨大的优势。
*   Cython 工具（<https://cython.org>）提供了 Python 语言的超集，并具有额外的功能，可以轻松创建 C 扩展模块，而无需实际编写 C 代码。它共享标准 C 扩展的构建复杂性，但使用起来可能比 Python C API 容易得多。
*   Mypyc（<https://github.com/mypyc/mypyc>）类似于 Cython，但它使用 `typing` 模块的标准注解（参见 [Item 124](#ch14#ch14lev1sec9): “[Consider Static Analysis via typing to Obviate Bugs](#ch14#ch14lev1sec9)”）而不是要求非标准语法。这可以使其在不更改代码的情况下更容易采用。它还可以 AOT（ahead-of-time）编译整个程序以加快启动时间。Mypyc 具有与 C 扩展类似的构建复杂性，并且不包含 Cython 的 C 集成功能。
*   CFFI 模块（<https://cffi.readthedocs.io>）类似于 `ctypes` 内置模块，但它可以直接读取 C 头文件以了解您要调用的函数的接口。这种自动映射大大减少了调用包含大量函数和数据结构的本地库的开发人员的劳动。
*   SWIG（<https://www.swig.org>）是一个工具，可以为 C 和 C++ 本地库自动生成 Python 接口。在这方面它类似于 CFFI，但翻译是显式发生的，而不是在运行时发生的，这可能更有效。SWIG 支持 Python 以外的其他目标语言和各种自定义选项。它也需要像 C 扩展一样的构建复杂性。

需要注意的一个重要警告是，这些工具和库可能需要大量的开发时间才能有效学习和使用。从头开始用另一种语言重写程序组件可能更容易，特别是考虑到 Python 在粘合系统方面的出色表现。您可以使用从构建 Python 实现中学到的知识来指导重写的（design）。

然而，用 C（或其他语言）重写您的任何 Python 代码也有很高的成本。在 Python 中简短易懂的代码在其他语言中可能会变得冗长而复杂。移植还需要广泛的测试，以确保功能与原始 Python 代码等效，并且没有引入错误。

有时重写是值得的，这解释了 Python 社区中庞大的 C 扩展模块生态系统，它们加速了文本解析、图像合成和矩阵数学等操作。对于您自己的代码，您需要考虑风险与潜在回报，并决定适合您情况的最佳权衡。

#### Things to Remember
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 重写 Python 代码为另一种语言有许多有效的原因，但您应该在追求该选项之前研究所有可用的优化技术。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 将 CPU 瓶颈转移到 C 扩展模块和本地库是提高性能同时最大化您在 Python 代码上的投资的有效方法。但是，这样做成本很高，并且可能引入错误。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 生态系统中存在大量工具和库，可以以惊人的少量更改加速 Python 程序中缓慢的部分。

### Item 95: Consider `ctypes` to Rapidly Integrate with Native Libraries

`ctypes` 内置模块使 Python 能够调用定义在本地库（native libraries）中的函数。这些库可以用任何其他可以导出遵循 C 调用约定的函数的编程语言实现（例如 C、C++、Rust）。该模块为 Python 开发人员提供了两个关键优势：
*   `ctypes` 使使用 Python 连接系统变得容易。如果存在您需要的现有本地库，您将能够轻松使用它。
*   `ctypes` 为优化程序缓慢部分提供了一条直接途径。如果您发现一个无法加速的热点，您可以将其重新实现为另一种语言，然后使用 `ctypes` 调用更快的版本。

例如，考虑上一项中的 `dot_product` 函数（参见 [Item 94](#ch11#ch11lev1sec3): “[Know When and How to Replace Python with Another Programming Language](#ch11#ch11lev1sec3)”）：
```
def dot_product(a, b):
result = 0
for i, j in zip(a, b):
result += i * j
return result
```
我可以使用一个简单的 C 函数来操作数组来实现类似的功能。这里我定义了接口：
[Click here to view code image](#ch11_images#f0463-01)
```
/* my_library.h */
extern double dot_product(int length, double* a, double* b);
```
实现很简单，并且大多数 C 编译器会自动对其进行矢量化（vectorized），以使用 SIMD（single instruction, multiple data）操作等高级处理器功能来最大化性能：
[Click here to view code image](#ch11_images#f0463-02)
```
/* my_library.c */
#include <stdio.h>
#include "my_library.h"

double dot_product(int length, double* a, double* b) {
double result = 0;
for (int i = 0; i < length; i++) {
result += a[i] * b[i];
}
return result;
}
```
现在我需要将此代码编译成库文件。这样做超出了本书的范围，但在我的机器上，命令是：
[Click here to view code image](#ch11_images#f0463-03)
```
$ cc -shared -o my_library.lib my_library.c
```
我可以通过将库文件的路径提供给 `ctypes.cdll.LoadLibrary` 构造函数来轻松地在 Python 中加载此库文件：
[Click here to view code image](#ch11_images#f0463-04)
```
import ctypes

library_path = ...
my_library = ctypes.cdll.LoadLibrary(library_path)
```
用 C 实现的 `dot_product` 函数现在可以作为 `my_library` 的属性访问：
[Click here to view code image](#ch11_images#f0464-01)
```
print(my_library.dot_product)

>>>
<_FuncPtr object at 0x10544cc50>
```
如果您使用 `ctypes.CFUNCTYPE` 对象包装导入的函数指针，您可能会遇到由于隐式类型转换而导致的错误行为。相反，最好直接将导入函数的 `restype` 和 `argtypes` 属性分配给与函数本机实现签名匹配的 `ctypes` 类型：
[Click here to view code image](#ch11_images#f0464-02)
```
my_library.dot_product.restype = ctypes.c_double

vector_ptr = ctypes.POINTER(ctypes.c_double)
my_library.dot_product.argtypes = (
ctypes.c_int,
vector_ptr,
vector_ptr,
)
```
调用导入的函数相对容易。首先，我定义了一个包含三个双精度值的数组类型。然后我分配了两个该类型的实例作为参数：
[Click here to view code image](#ch11_images#f0464-03)
```
size = 3
vector3 = ctypes.c_double * size
a = vector3(1.0, 2.5, 3.5)
b = vector3(-7, 4, -12.1)
```
最后，我使用这两个数组调用导入的 `dot_product` 函数。我需要使用 `ctypes.cast` 辅助函数来确保提供数组第一个元素的地址——匹配 C 约定——而不是 `vector3` Python 对象的地址。我不需要转换返回值，因为 `ctypes` 会自动将其转换为 Python 值：
[Click here to view code image](#ch11_images#f0464-04)
```
result = my_library.dot_product(
3,
ctypes.cast(a, vector_ptr),
ctypes.cast(b, vector_ptr),
)
print(result)

>>>
-39.35
```
现在应该很明显，`ctypes` API 的人体工程学非常差，而且不 Pythonic。但令人印象深刻的是一切是如何快速组合在一起并开始工作的。为了使其感觉更自然，这里我用一个 Python 函数包装导入的本地函数来执行数据类型映射并验证假设（参见 [Item 81](#ch10#ch10lev1sec2): “[assert Internal Assumptions and raise Missed Expectations](#ch10#ch10lev1sec2)” 获取背景信息）：
[Click here to view code image](#ch11_images#f0465-01)
```
def dot_product(a, b):
size = len(a)
assert len(b) == size
a_vector = vector3(*a)
b_vector = vector3(*b)
result = my_library.dot_product(size, a_vector, b_vector)
return result

result = dot_product([1.0, 2.5, 3.5], [-7, 4, -12.1])
print(result)

>>>
-39.35
```
或者，我可以使用 Python 的 C 扩展 API（参见 [Item 96](#ch11#ch11lev1sec5): “[Consider Extension Modules to Maximize Performance and Ergonomics](#ch11#ch11lev1sec5)”）提供更 Pythonic 的接口和本地性能。然而，与构建 C 扩展相比，`ctypes` 具有一些值得称赞的优势：
*   您通过 `ctypes` 持有的指针值将在 Python 对象引用计数（reference count）归零时自动释放。C 扩展必须为 C 指针进行手动内存管理，并为 Python 对象进行手动引用计数。
*   当您使用 `ctypes` 调用函数时，它会在调用执行期间自动释放 GIL，允许其他 Python 线程并行执行（参见 [Item 68](#ch09#ch09lev1sec2): “[Use Threads for Blocking I/O; Avoid for Parallelism](#ch09#ch09lev1sec2)”)。使用 C 扩展模块时，必须显式管理 GIL，并且在不持有锁的情况下功能受限。
*   使用 `ctypes`，您只需提供磁盘上共享对象或动态库的路径，即可加载它。编译可以与您已有的构建系统分开完成。使用 Python C 扩展，您需要利用 Python 构建系统包含正确的路径、设置链接器标志等；这有很多复杂性，并且可能是重复的。

但是，与构建 C 扩展相比，使用 `ctypes` 模块也有一些重要的缺点：
*   `ctypes` 将您限制在 C 可以描述的数据类型。您将失去 Python 的大部分表达能力，包括迭代器（参见 [Item 21](#ch03#ch03lev1sec5): “[Be Defensive when Iterating over Arguments](#ch03#ch03lev1sec5)”）和鸭子类型（duck typing）（参见 [Item 25](#ch04#ch04lev1sec1): “[Be Cautious when Relying on Dictionary Insertion Ordering](#ch04#ch04lev1sec1)”）等极其常见的功能。即使有包装器，使用 `ctypes` 导入的本地函数对 Python 程序员来说也可能感觉很奇怪，并阻碍生产力。
*   使用正确的数据类型调用 `ctypes` 通常需要您对函数输入和输出进行复制或转换。这种开销的成本可能会削弱使用本地库的性能优势，使整个优化过程变得毫无价值。C 扩展允许您绕过复制；唯一的速度限制是底层数据类型的固有性能。
*   如果您稍微错误地使用 `ctypes`，您可能会导致程序损坏其自身的内存并表现异常。例如，如果您错误地为函数参数或返回值提供了 `ctypes.c_double` 而不是 `ctypes.c_int`，您可能会遇到具有模糊错误消息的不可预测的崩溃。`faulthandler` 内置模块可以帮助跟踪这些问题，但它们仍然很难调试。

使用 `ctypes` 的最佳实践是始终在将其用于更复杂的代码之前编写相应的单元测试（参见 [Item 109](#ch13#ch13lev1sec2): “[Prefer Integration Tests over Unit Tests](#ch13#ch13lev1sec2)”)。这些测试的目的是测试您正在调用的库的基本表面区域，以确认它在简单使用中按预期工作。这可以帮助您检测诸如共享库中的函数修改了其参数类型但您的 `ctypes` 用法尚未更新以匹配的情况。这里我测试了导入库中的 `my_library.dot_product` 符号：
[Click here to view code image](#ch11_images#f0466-01)
```
from unittest import TestCase

class MyLibraryTest(TestCase):

def test_dot_product(self):
vector3 = ctypes.c_double * size
a = vector3(1.0, 2.5, 3.5)
b = vector3(-7, 4, -12.1)
vector_ptr = ctypes.POINTER(ctypes.c_double)
result = my_library.dot_product(
3,
ctypes.cast(a, vector_ptr),
ctypes.cast(b, vector_ptr),
)
self.assertAlmostEqual(-39.35, result)

...

>>>
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
`ctypes` 模块包含用于将 Python 对象映射到 C 结构、复制内存、错误检查以及更多功能的附加功能（参见完整手册 <https://docs.python.org/3/library/ctypes.html> 获取详细信息）。最终，您需要决定使用 `ctypes` 获得的开发易用性和速度是否值得其较差的人体工程学和开销。

#### Things to Remember
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `ctypes` 内置模块可以轻松地将用其他语言编写的本地库的功能和性能集成到 Python 程序中。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 与 Python C 扩展 API 相比，`ctypes` 可以在没有额外构建复杂性的情况下实现快速开发。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `ctypes` 编写 Pythonic API 很困难，因为可用的数据类型和协议仅限于 C 中可以表达的内容。

### Item 96: Consider Extension Modules to Maximize Performance and Ergonomics

Python 语言的 CPython 实现（参见 [Item 1](#ch01#ch01lev1sec1): “[Know Which Version of Python You’re Using](#ch01#ch01lev1sec1)”）支持用 C 编写的**extension modules**。这些模块可以直接使用 Python API 来利用面向对象特性（参见 [Chapter 7](#ch07#ch07)）、鸭子类型协议（参见 [Item 25](#ch04#ch04lev1sec1): “[Be Cautious when Relying on Dictionary Insertion Ordering](#ch04#ch04lev1sec1)”） 、引用计数垃圾回收（reference counting garbage collection）以及使 Python 如此出色的几乎所有其他特性。上一项（参见 [Item 95](#ch11#ch11lev1sec4): “[Consider ctypes to Rapidly Integrate with Native Libraries](#ch11#ch11lev1sec4)”）介绍了 `ctypes` 内置模块的优缺点。如果您希望提供 Pythonic 的开发体验而不牺牲性能或特定于平台的（platform-specific）功能，那么扩展模块是最佳选择。

尽管创建扩展模块比使用 `ctypes` 复杂得多，但 Python C API 有助于使其相当直接。为了演示，我将实现之前相同的 `dot_product` 函数（参见 [Item 94](#ch11#ch11lev1sec3): “[Know When and How to Replace Python with Another Programming Language](#ch11#ch11lev1sec3)”），但将其作为扩展模块。首先，我将声明扩展应提供的 C 函数：
[Click here to view code image](#ch11_images#f0468-01)
```
/* my_extension.h */
#define PY_SSIZE_T_CLEAN
#include <Python.h>

PyObject *dot_product(PyObject *self, PyObject *args);
```
然后我将使用 C 实现该函数。我用于与输入和输出交互的 Python API（例如 `PyList_Size`、`PyFloat_FromDouble`）非常广泛，不断发展，并且——幸运的是——文档齐全（参见 <https://docs.python.org/3/extending>）。此函数版本期望接收两个等长的浮点数列表并返回一个浮点数：
[Click here to view code image](#ch11_images#f0468-02)
```
/* dot_product.c */
#include "my_extension.h"

PyObject *dot_product(PyObject *self, PyObject *args)
{
PyObject *left, *right;
if (!PyArg_ParseTuple(args, "OO", &left, &right)) {
return NULL;
}
if (!PyList_Check(left) || !PyList_Check(right)) {
PyErr_SetString(PyExc_TypeError, "Both arguments must be lists");
return NULL;
}

Py_ssize_t left_length = PyList_Size(left);
Py_ssize_t right_length = PyList_Size(right);
if (left_length == -1 || right_length == -1) {
return NULL;
}
if (left_length != right_length) {
PyErr_SetString(PyExc_ValueError, "Lists must be the same length");
return NULL;
}

double result = 0;

for (Py_ssize_t i = 0; i < left_length; i++) {
PyObject *left_item = PyList_GET_ITEM(left, i);
PyObject *right_item = PyList_GET_ITEM(right, i);

double left_double = PyFloat_AsDouble(left_item);
double right_double = PyFloat_AsDouble(right_item);
if (PyErr_Occurred()) {
return NULL;
}

result += left_double * right_double;
}

return PyFloat_FromDouble(result);
}
```
该函数大约有 40 行代码，比可以使用 `ctypes` 模块调用的简单 C 实现长四倍。还需要一些额外的样板代码来配置扩展模块并初始化它：
[Click here to view code image](#ch11_images#f0469-02)
```
/* init.c */
#include "my_extension.h"

static PyMethodDef my_extension_methods[] = {
{
"dot_product",
dot_product,
METH_VARARGS,
"Compute dot product",
},
{
NULL,
NULL,
0,
NULL,
},
};

static struct PyModuleDef my_extension = {
PyModuleDef_HEAD_INIT,
"my_extension",
"My C-extension module",
-1,
my_extension_methods,
};

PyMODINIT_FUNC
PyInit_my_extension(void)
{
return PyModule_Create(&my_extension);
}
```
现在我需要将 C 代码编译成一个可以被 CPython 解释器动态加载的原生库。最简单的方法是定义一个最小的 `setup.py` 配置文件：
[Click here to view code image](#ch11_images#f0470-02)
```
# setup.py
from setuptools import Extension, setup

setup(
name="my_extension",
ext_modules=[
Extension(
name="my_extension",
sources=["init.c", "dot_product.c"],
),
],
)
```
我可以使用此配置文件、虚拟环境（参见 [Item 117](#ch14#ch14lev1sec2): “[Use Virtual Environments for Isolated and Reproducible Dependencies](#ch14#ch14lev1sec2)”）和 `setuptools` 包（参见 [Item 116](#ch14#ch14lev1sec1): “[Know Where to Find Community-Built Modules](#ch14#ch14lev1sec1)”）来正确驱动我的系统的编译器，并使用正确的路径和标志；最后，我将得到一个可以被 Python 导入的原生库文件：
```
$ python3 -m venv .
$ source bin/activate
$ pip install setuptools
...
$ python3 setup.py develop
...
```
有许多方法可以构建 Python 扩展模块并将其打包以供分发。不幸的是，这些工具一直在变化。在此示例中，我只关注在我的本地开发环境中使扩展模块正常工作。如果您遇到问题或有其他用例，请务必查看官方 Python Packaging Authority (<https://www.pypa.io>) 的最新文档。

编译后，我可以使用用 Python 编写的测试（参见 [Item 108](#ch13#ch13lev1sec1): “[Verify Related Behaviors in TestCase Subclasses](#ch13#ch13lev1sec1)”）来验证扩展模块是否按预期工作：
[Click here to view code image](#ch11_images#f0471-01)
```
# my_extension_test.py
import unittest
import my_extension

class MyExtensionTest(unittest.TestCase):

def test_empty(self):
result = my_extension.dot_product([], [])
self.assertAlmostEqual(0, result)

def test_positive_result(self):
result = my_extension.dot_product(
[3, 4, 5],
[-1, 9, -2.5],
)
self.assertAlmostEqual(20.5, result)

...

if __name__ == "__main__":
unittest.main()
```
与基本的 C 实现相比，这付出了很多努力。而且接口的人体工程学与使用 `ctypes` 模块时大致相同：`dot_product` 的两个参数都需要是包含浮点数的列表。如果这就是您对 C 扩展 API 的全部要求，那么它就不值得了。您将无法利用其最有价值的功能。

现在我将创建此扩展模块的另一个版本，它使用 Python API 提供的迭代器和数字协议。这有 60 行代码——比简单的 `dot_product` 函数多 50%，比基本的 C 版本多六倍——但它实现了使 Python 如此强大的全部功能。通过使用 `PyObject_GetIter` 和 `PyIter_Next` API，输入类型可以是任何可迭代容器（iterable container），例如元组（tuples）、列表（lists）、生成器（generators）等（参见 [Item 21](#ch03#ch03lev1sec5): “[Be Defensive when Iterating over Arguments](#ch03#ch03lev1sec5)”)。通过使用 `PyNumber_Multiply` 和 `PyNumber_Add` API，来自迭代器的值可以是任何正确实现数字特殊方法（number special methods）的对象（参见 [Item 57](#ch07#ch07lev1sec10): “[Inherit from collections.abc Classes for Custom Container Types](#ch07#ch07lev1sec10)”）：
[Click here to view code image](#ch11_images#f0472-01)
```
/* dot_product.c */
#include "my_extension2.h"

PyObject *dot_product(PyObject *self, PyObject *args)
{
PyObject *left, *right;
if (!PyArg_ParseTuple(args, "OO", &left, &right)) {
return NULL;
}
PyObject *left_iter = PyObject_GetIter(left);
if (left_iter == NULL) {
return NULL;
}
PyObject *right_iter = PyObject_GetIter(right);
if (right_iter == NULL) {
Py_DECREF(left_iter);
return NULL;
}

PyObject *left_item = NULL;
PyObject *right_item = NULL;
PyObject *multiplied = NULL;
PyObject *result = PyLong_FromLong(0);

while (1) {
Py_CLEAR(left_item);
Py_CLEAR(right_item);
Py_CLEAR(multiplied);
left_item = PyIter_Next(left_iter);
right_item = PyIter_Next(right_iter);

if (left_item == NULL && right_item == NULL) {
break;
} else if (left_item == NULL || right_item == NULL) {
PyErr_SetString(PyExc_ValueError, "Arguments had unequal length");
break;
}

multiplied = PyNumber_Multiply(left_item, right_item);
if (multiplied == NULL) {
break;
}
PyObject *added = PyNumber_Add(result, multiplied);
if (added == NULL) {
break;
}
Py_CLEAR(result);
result = added;
}

Py_CLEAR(left_item);
Py_CLEAR(right_item);
Py_CLEAR(multiplied);
Py_DECREF(left_iter);
Py_DECREF(right_iter);

if (PyErr_Occurred()) {
Py_CLEAR(result);
return NULL;
}

return result;
}
```
实现因需要正确管理对象引用计数以及错误传播和引用借用的特殊性而进一步复杂化。但结果可能是 Python 的圣杯：一个既快速又易于使用的模块。这里我展示了它适用于多种类型的可迭代对象和 `Decimal` 数值类（参见 [Item 106](#ch12#ch12lev1sec7): “[Use decimal when Precision Is Paramount](#ch12#ch12lev1sec7)”）：
[Click here to view code image](#ch11_images#f0473-02)
```
# my_extension2_test.py
import unittest
import my_extension2

class MyExtension2Test(unittest.TestCase):

def test_decimals(self):
import decimal

a = [decimal.Decimal(1), decimal.Decimal(2)]
b = [decimal.Decimal(3), decimal.Decimal(4)]
result = my_extension2.dot_product(a, b)
self.assertEqual(11, result)

def test_not_lists(self):
result1 = my_extension2.dot_product(
(1, 2),
[3, 4],
)
result2 = my_extension2.dot_product(
[1, 2],
(3, 4),
)
result3 = my_extension2.dot_product(
range(1, 3),
range(3, 5),
)
self.assertAlmostEqual(11, result1)
self.assertAlmostEqual(11, result2)
self.assertAlmostEqual(11, result3)

...

if __name__ == "__main__":
unittest.main()
```
API 中这种程度的可扩展性和灵活性就是良好人体工程学的体现。用基本的 C 代码实现相同的行为，实际上需要重新实现 Python 解释器和 API 的核心。了解了这一点，这些扩展模块较大的行数似乎是合理的，考虑到它们提供了多少功能和性能。

#### Things to Remember
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 扩展模块是用 C 编写的，以原生速度执行，并且可以使用 Python API 访问 Python 的几乎所有强大功能。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python API 的特殊性，包括内存管理和错误传播，可能难以学习且难以正确处理。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) C 扩展的最大价值来自于使用 Python API 的协议和内置数据类型，这些在简单的 C 代码中很难复制。

### Item 97: Rely on Precompiled Bytecode and File System Caching to Improve Startup Time

程序启动时间是一个重要的性能指标，因为它直接可供用户观察。对于命令行实用程序，启动时间是指您按下 Enter 键后程序开始处理所需的时间。用户通常会连续快速地执行相同的命令行工具，因此启动延迟的累积会让人感到沮丧的时间浪费。对于 Web 服务器，启动时间是指程序启动后开始处理第一个传入请求所需的时间。Web 服务器通常使用多个线程或子进程来并行处理工作，这可能导致每次启动新上下文时出现“冷启动”（cold start）延迟。最终结果是，某些 Web 请求可能比其他请求花费的时间长得多，从而因不可预测的延迟而惹恼用户。

不幸的是，与编译为机器码可执行文件的语言编写的程序相比，Python 程序的启动时间通常很长。CPython Python 实现（参见 [Item 1](#ch01#ch01lev1sec1): “[Know Which Version of Python You’re Using](#ch01#ch01lev1sec1)”）中存在导致这种缓慢的两个主要因素。首先，在启动时，CPython 读取程序的源代码并将其编译为其虚拟机解释器的字节码，这需要 I/O 和 CPU 处理（参见 [Item 68](#ch09#ch09lev1sec2): “[Use Threads for Blocking I/O; Avoid for Parallelism](#ch09#ch09lev1sec2)” 获取详细信息）。其次，当字节码准备好后，Python 会执行主入口点导入的所有模块。加载模块需要运行代码来初始化全局变量和常量、定义类、执行断言语句等——这可能是一项繁重的工作。

为了提高性能，模块在程序首次加载后会被缓存到内存中，并在后续加载中使用（参见 [Item 122](#ch14#ch14lev1sec7): “[Know How to Break Circular Dependencies](#ch14#ch14lev1sec7)” 获取详细信息）。CPython 还将其在编译期间生成的字节码保存到磁盘上的缓存中，以便在后续程序启动时重复使用。缓存存储在源代码旁边一个名为 `__pycache__` 的目录中。每个字节码文件都有一个 `.pyc` 后缀，通常比相应的源文件小。

很容易看到字节码缓存的作用。例如，这里我加载 Django Web 框架（<https://www.djangoproject.com>）的所有模块，并测量所需时间（特别是“实际”时间）。这是该开源项目的仅源代码快照，没有字节码缓存文件：
[Click here to view code image](#ch11_images#f0476-01)
```
$ time python3 -c 'import django_all'
...
real    0m0.791s
user    0m0.495s
sys     0m0.145s
```
如果我再次运行相同的程序而没有任何修改，它的启动时间比之前快了 70%——快了三倍多：
[Click here to view code image](#ch11_images#f0476-02)
```
$ time python3 -c 'import django_all'
...
real    0m0.225s
user    0m0.182s
sys     0m0.038s
```
您可能会猜测这种性能改进是由于 CPython 在程序第二次启动时使用了字节码缓存。但是，如果我删除 `.pyc` 文件，性能仍然比我第一次执行 Python 并导入此模块时要好：
[Click here to view code image](#ch11_images#f0476-03)
```
$ find django -name '*.pyc' -delete
$ time python3 -c 'import django_all'

real    0m0.613s
user    0m0.502s
sys     0m0.101s
```
这是一个很好的例子，说明了测量性能的难度以及优化效果可能令人困惑。导致第二次没有 `.pyc` 文件的 Python 调用比第一次快的根本原因是我操作系统的文件系统缓存。Python 源文件已经在内存中，因为我最近访问过它们。当我再次加载它们时，昂贵的 I/O 操作可以缩短，从而加快程序启动。

我可以使用 `compileall` 内置模块重新生成字节码文件。这通常在您使用 `pip` 安装包时自动完成（参见 [Item 117](#ch14#ch14lev1sec2): “[Use Virtual Environments for Isolated and Reproducible Dependencies](#ch14#ch14lev1sec2)”），以最小化启动时间。但是，您可以在需要时为自己的代码库手动创建新的字节码文件（例如，在部署到生产环境之前）：
[Click here to view code image](#ch11_images#f0476-04)
```
$ python3 -m compileall django
Listing 'django'...
Compiling 'django/__init__.py'...
Compiling 'django/__main__.py'...
Listing 'django/apps'...
Compiling 'django/apps/__init__.py'...
Compiling 'django/apps/config.py'...
Compiling 'django/apps/registry.py'...
...
```
大多数操作系统都提供了一种清除文件系统缓存的方法，这将导致后续的 I/O 操作转到物理磁盘而不是内存。这里我强制清空缓存（使用 `purge` 命令），然后重新运行 `django_all` 导入，以查看磁盘上和内存中没有字节码文件时的性能影响：
[Click here to view code image](#ch11_images#f0477-02)
```
$ sudo purge
$ time python3 -c 'import django_all'
...
real    0m0.382s
user    0m0.169s
sys     0m0.085s
```
此启动时间（382 毫秒）比没有字节码和空文件系统缓存（791 毫秒）快，也比没有字节码和源文件缓存在内存中（613 毫秒）快，但比同时拥有字节码和源文件在内存中（225 毫秒）慢。最终，通过确保您的字节码已预编译并位于文件系统缓存中，您将获得最佳的启动性能。因此，将 Python 程序放在 RAM 磁盘上可能很有价值，这样它们始终在内存中，无论访问模式如何。当您的计算机有旋转磁盘时，这种效果会更加明显；我在这些测试中使用了 SSD（固态硬盘）。当内存缓存不可用时，其他减少启动时间的方法可能很有价值（参见 [Item 98](#ch11#ch11lev1sec7): “[Lazy-Load Modules with Dynamic Imports to Reduce Startup Time](#ch11#ch11lev1sec7)”。

最后，您可能想知道不带源文件运行 Python 程序是否更快，因为字节码缓存似乎是 CPython 执行程序所需的一切。确实，这是可能的。诀窍是在生成字节码时使用 `-b` 标志，这会导致单个 `.pyc` 文件放置在源代码旁边，而不是放在 `__pycache__` 目录中。这里我相应地修改了 `django` 包，然后再次测试导入 `django_all` 模块的速度：
[Click here to view code image](#ch11_images#f0477-03)
```
$ find django -name '*.pyc' -delete
$ python3 -m compileall -b django
$ find django -name '*.py' -delete
$ time python3 -c 'import django_all'
...
real    0m0.226s
user    0m0.183s
sys     0m0.037s
```
在这种情况下，启动时间（226 毫秒）几乎与源文件也存在时完全相同。因此，除非您有其他需要满足的限制，例如最小化整体存储或系统内存使用（参见 [Item 125](#ch14#ch14lev1sec10): “[Prefer Open Source Projects for Bundling Python Programs over zipimport and zipapp](#ch14#ch14lev1sec10)” 获取示例），否则删除源文件没有价值。

#### Things to Remember
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 的 CPython 实现将程序的源文件编译成字节码，然后由虚拟机执行。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 字节码会被缓存到磁盘，这使得后续运行相同的程序或加载相同的模块时可以避免再次编译字节码。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 CPython，程序启动时间的最佳性能是在程序字节码文件预先生成并且它们已在操作系统内存中缓存时实现的。

### Item 98: Lazy-Load Modules with Dynamic Imports to Reduce Startup Time

上一项探讨了 Python 程序初始化为何可能缓慢，并考虑了提高性能的方法（参见 [Item 97](#ch11#ch11lev1sec6): “[Rely on Precompiled Bytecode and File System Caching to Improve Startup Time](#ch11#ch11lev1sec6)”。在遵循了这些最佳实践并进行了进一步优化之后（参见 [Item 92](#ch11#ch11lev1sec1): “[Profile Before Optimizing](#ch11#ch11lev1sec1)”), 您的 Python 程序可能仍然感觉启动时间过长。幸运的是，还有一种技术可以尝试：动态导入（dynamic imports）。

例如，假设我正在构建一个具有两个功能的图像处理工具。第一个模块根据用户提供的设置调整图像的亮度（brightness）和对比度（contrast）：
[Click here to view code image](#ch11_images#f0478-02)
```
# adjust.py
# Fast initialization
...

def do_adjust(path, brightness, contrast):
...
```
第二个模块以给定量智能地增强图像。为了演示一个现实情况，我假设这需要加载一个大型的本地图像处理库，因此初始化缓慢：
```
# enhance.py
# Very slow initialization
...

def do_enhance(path, amount):
...
```
我可以使用 `argparse` 内置模块将这些函数作为命令行实用程序提供。这里我使用 `add_subparsers` 功能来要求一组不同的标志，具体取决于用户指定的命令。`adjust` 命令接受 `--brightness` 和 `--contrast` 标志，而 `enhance` 命令只需要 `--amount` 标志：
[Click here to view code image](#ch11_images#f0479-02)
```
# parser.py
import argparse

PARSER = argparse.ArgumentParser()
PARSER.add_argument("file")

sub_parsers = PARSER.add_subparsers(dest="command")

enhance_parser = sub_parsers.add_parser("enhance")
enhance_parser.add_argument("--amount", type=float)

adjust_parser = sub_parsers.add_parser("adjust")
adjust_parser.add_argument("--brightness", type=float)
adjust_parser.add_argument("--contrast", type=float)
```
在 `main` 函数中，我解析参数，然后相应地调用 `enhance` 和 `adjust` 模块：
[Click here to view code image](#ch11_images#f0479-03)
```
# mycli.py
import adjust
import enhance
import parser

def main():
args = parser.PARSER.parse_args()

if args.command == "enhance":
enhance.do_enhance(args.file, args.amount)
elif args.command == "adjust":
adjust.do_adjust(    args.file, args.brightness, args.contrast)
else:
raise RuntimeError("Not reachable")

if __name__ == "__main__":
main()
```
尽管这里的功能运行良好，但程序很慢。例如，这里我运行 `enhance` 命令，并观察到它需要超过 1 秒才能完成：
[Click here to view code image](#ch11_images#f0480-02)
```
$ time python3 ./mycli.py my_file.jpg enhance --amount 0.8
...
real    0m1.089s
user    0m0.035s
sys     0m0.022s
```
此长时间执行的原因可能是 `enhance` 模块中对大型本地图像处理库的依赖。我没有为 `adjust` 命令使用该库，所以我预计它会更快：
[Click here to view code image](#ch11_images#f0480-03)
```
$ time python3 ./mycli.py my_file.jpg adjust --brightness
➥.3 --contrast -0.1
...
real    0m1.064s
user    0m0.040s
sys     0m0.016s
```
不幸的是，`enhance` 和 `adjust` 命令似乎都很慢。仔细检查后，我发现问题在于我将所有可能被命令行工具使用的模块导入到主模块的顶部，这符合 PEP 8 风格（参见 [Item 2](#ch01#ch01lev1sec2): “[Follow the PEP 8 Style Guide](#ch01#ch01lev1sec2)”）。在启动时，我的程序会承担准备所有功能的计算成本，即使只使用了其中一部分。

Python 的 CPython 实现（参见 [Item 1](#ch01#ch01lev1sec1): “[Know Which Version of Python You’re Using](#ch01#ch01lev1sec1)”）支持 `-X importtime` 标志，该标志直接测量模块加载的性能。这里我使用它来诊断我的命令行工具的缓慢原因：
[Click here to view code image](#ch11_images#f0480-04)
```
$ python3 -X importtime mycli.py
import time: self [us] | cumulative | imported package
...
import time:       553 |        553 | adjust
import time:   1005348 |    1005348 | enhance
...
import time:      3347 |      14762 | parser
```
`self` 列显示每个模块执行所有全局语句所花费的时间（以微秒为单位），不包括导入。`cumulative` 列显示加载每个模块（包括其所有依赖项）所花费的时间。显然，`enhance` 模块是罪魁祸首。

一种解决方案是延迟导入依赖项，直到您实际需要使用它们。这是可能的，因为 Python 支持在运行时——在函数内部——导入模块，除了在程序启动时使用模块范围的 `import` 语句（参见 [Item 122](#ch14#ch14lev1sec7): “[Know How to Break Circular Dependencies](#ch14#ch14lev1sec7)” 获取此动态性的另一个用途）。这里我修改了命令行工具，使其仅在 `main` 函数中，在命令分派后导入 `adjust` 模块或 `enhance` 模块：
[Click here to view code image](#ch11_images#f0481-02)
```
# mycli_faster.py
import parser

def main():
args = parser.PARSER.parse_args()

if args.command == "enhance":
import enhance  # Changed

enhance.do_enhance(args.file, args.amount)
elif args.command == "adjust":
import adjust   # Changed

adjust.do_adjust(    args.file, args.brightness, args.contrast)
else:
raise RuntimeError("Not reachable")

if __name__ == "__main__":
main()
```
有了这个修改后，`adjust` 命令运行得非常快，因为可以跳过 `enhance` 的初始化：
[Click here to view code image](#ch11_images#f0481-03)
```
$ time python3 ./mycli_faster.py my_file.jpg adjust
➥--brightness .3 --contrast -0.1
...
real    0m0.049s
user    0m0.032s
sys     0m0.013s
```
`enhance` 命令仍然像以前一样慢：
[Click here to view code image](#ch11_images#f0482-02)
```
$ time python3 ./mycli_faster.py my_file.jpg enhance
➥--amount 0.8
...
real    0m1.059s
user    0m0.036s
sys     0m0.014s
```
我还可以使用 `-X importtime` 来确认当没有指定命令时，`adjust` 和 `enhance` 模块未被加载：
[Click here to view code image](#ch11_images#f0482-03)
```
$ time python3 -X importtime ./mycli_faster.py -h
import time: self [us] | cumulative | imported package
...
import time:      1118 |       6015 | parser
...
real    0m0.049s
user    0m0.032s
sys     0m0.013s
```
Lazy-loading 模块对于像这样的命令行工具来说效果很好，这些工具执行一项任务直到完成然后终止。但是，如果我需要减少 Web 应用程序中冷启动（cold starts）的延迟怎么办？理想情况下，加载 `enhance` 模块的成本不应在功能实际被用户请求之前产生。幸运的是，相同的方法也适用于请求处理程序（request handlers）内部。这里我创建一个 `flask` Web 应用程序，为每个功能提供一个处理程序，该处理程序动态导入相应的模块：
[Click here to view code image](#ch11_images#f0482-04)
```
# server.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/adjust", methods=["GET", "POST"])
def do_adjust():
if request.method == "POST":
the_file = request.files["the_file"]
brightness = request.form["brightness"]
contrast = request.form["contrast"]
import adjust   # Dynamic import

return adjust.do_adjust(the_file, brightness, contrast)
else:
return render_template("adjust.html")

@app.route("/enhance", methods=["GET", "POST"])
def do_enhance():
if request.method == "POST":
the_file = request.files["the_file"]
amount = request.form["amount"]
import enhance  # Dynamic import

return enhance.do_enhance(the_file, amount)
else:
return render_template("enhance.html")
```
当 `do_enhance` 请求处理程序在 Python 进程中首次执行时，它会导入 `enhance` 模块并支付 1 秒的高初始化成本。在后续调用 `do_enhance` 时，`import enhance` 语句将导致 Python 进程仅验证该模块是否已加载，然后将本地作用域中的 `enhance` 标识符分配给相应的模块对象。

您可能会认为动态 `import` 语句的成本很高，但实际上并非如此。这里我使用 `timeit` 内置模块（参见 [Item 93](#ch11#ch11lev1sec2): “[Optimize Performance-Critical Code Using timeit Microbenchmarks](#ch11#ch11lev1sec2)”）来测量动态导入先前导入模块所需的时间：
[Click here to view code image](#ch11_images#f0483-02)
```
# import_perf.py
import timeit

trials = 10_000_000

result = timeit.timeit(
setup="import enhance",
stmt="import enhance",
globals=globals(),
number=trials,
)

print(f"{result/trials * 1e9:2.1f} nanos per call")

>>>
52.8 nanos per call
```
为了让这个开销（52 纳秒）更具可比性，这里是另一个示例，它将动态 `import` 语句替换为受锁保护的全局变量（这是防止多个线程在程序初始化期间争用的一种常见方法）：
[Click here to view code image](#ch11_images#f0484-01)
```
# global_lock_perf.py
import timeit
import threading

trials = 100_000_000

initialized = False
initialized_lock = threading.Lock()

result = timeit.timeit(
stmt="""
global initialized
# Speculatively check without the lock
if not initialized:
with initialized_lock:
# Double check after holding the lock
if not initialized:
# Do expensive initialization
...
initialized = True
""",
globals=globals(),
number=trials,
)

print(f"{result/trials * 1e9:2.1f} nanos per call")

>>>
5.5 nanos per call
```
动态导入版本比使用全局变量的方法慢十倍，因此它肯定慢得多。在没有锁争用（这是由于投机性的 `if not initialized` 语句而常见的场景）的情况下，全局变量版本运行起来几乎和在 Python 中将两个整数相加一样快。但动态导入版本是更简单的代码，不需要任何样板代码。您不希望在 CPU 密集型代码（如内核函数的内循环）中使用动态导入（参见 [Item 94](#ch11#ch11lev1sec3): “[Know When and How to Replace Python with Another Programming Language](#ch11#ch11lev1sec3)” 获取详细信息），但一次性在每个 Web 请求中执行此操作似乎是合理的。

#### Things to Remember
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) CPython 的 `-X importtime` 标志会导致 Python 程序打印出加载导入模块及其依赖项所需的时间，从而轻松诊断启动时间缓慢的原因。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 模块可以动态地在函数内部导入，这使得有可能将昂贵的依赖项初始化延迟到实际需要使用功能为止。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 动态导入模块并检查其是否已加载的开销大约是 20 次加法运算，如果它能显著提高冷启动的延迟，那么这种增量成本是值得的。

### Item 99: Consider `memoryview` and `bytearray` for Zero-Copy Interactions with `bytes`

虽然 Python 在没有额外工作的情况下无法并行化 CPU 密集型计算（参见 [Item 79](#ch09#ch09lev1sec13): “[Consider concurrent.futures for True Parallelism](#ch09#ch09lev1sec13)” 和 [Item 94](#ch11#ch11lev1sec3): “[Know When and How to Replace Python with Another Programming Language](#ch11#ch11lev1sec3)”），但它能够以多种方式支持高吞吐量、并行 I/O（参见 [Item 68](#ch09#ch09lev1sec2): “[Use Threads for Blocking I/O; Avoid for Parallelism](#ch09#ch09lev1sec2)” 和 [Item 75](#ch09#ch09lev1sec9): “[Achieve Highly Concurrent I/O with Coroutines](#ch09#ch09lev1sec9)”)。尽管如此，错误地使用 I/O 工具并得出语言对于 I/O 密集型工作负载来说太慢的结论是很容易的。

例如，假设我正在构建一个媒体服务器，用于通过网络向用户流式传输电视或电影，以便用户无需提前下载视频数据即可观看。此类系统的关键功能之一是用户能够向前或向后移动视频播放，以便他们可以跳过或重复部分。在客户端程序中，我可以通过请求服务器上与用户选择的新时间索引相对应的块（chunk）数据来实现此目的：
[Click here to view code image](#ch11_images#f0485-01)
```
def timecode_to_index(video_id, timecode):
...
# Returns the byte offset in the video data

def request_chunk(video_id, byte_offset, size):
...
# Returns size bytes of video_id's data from the offset

video_id = ...
timecode = "01:09:14:28"
byte_offset = timecode_to_index(video_id, timecode)
size = 20 * 1024 * 1024
video_data = request_chunk(video_id, byte_offset, size)
```
如何实现接收 `request_chunk` 请求并返回相应 20 MB 视频数据块的服务器端处理程序？为了本示例的方便，我假设服务器的命令和控制部分已经连接好（参见 [Item 76](#ch09#ch09lev1sec10): “[Know How to Port Threaded I/O to asyncio](#ch09#ch09lev1sec10)” 了解这需要什么）。我在这里专注于最后几个步骤，其中请求的块从内存中缓存的数 GB 视频数据中提取出来，然后通过套接字（socket）发送回客户端。以下是实现外观：
[Click here to view code image](#ch11_images#f0486-02)
```
socket = ...             # socket connection to client
video_data = ...         # bytes containing data for video_id
byte_offset = ...        # Requested starting position
size = 20 * 1024 * 1024  # Requested chunk size

chunk = video_data[byte_offset : byte_offset + size]
socket.send(chunk)
```
此代码的延迟和吞吐量取决于两个因素：从 `video_data` 中提取 20 MB 视频块所需的时间，以及套接字将该数据传输到客户端所需的时间。如果我假设套接字无限快，我可以通过使用 `timeit` 内置模块来运行 microbenchmark，以了解以这种方式对 `bytes` 实例进行切片以创建块的性能特征（参见 [Item 14](#ch02#ch02lev1sec5): “[Know How to Slice Sequences](#ch02#ch02lev1sec5)” 获取背景信息）：
[Click here to view code image](#ch11_images#f0486-03)
```
import timeit

def run_test():
chunk = video_data[byte_offset : byte_offset + size]
# Call socket.send(chunk), but ignoring for benchmark

result = (
timeit.timeit(
stmt="run_test()",
globals=globals(),
number=100,
)
/ 100
)

print(f"{result:0.9f} seconds")

>>>
0.004925669 seconds
```
提取 20 MB 数据块以传输到客户端大约需要 5 毫秒。这意味着我的服务器的总体吞吐量被限制在理论最大值 20 MB / 5 毫秒 = 4 GB/秒，因为这是我能从内存中提取视频数据的最快速度。我的服务器还将限制为每秒 1 CPU 秒 / 5 毫秒 = 200 个请求新块的客户端并行，这与 `asyncio` 内置模块等工具可以支持的数万个并发连接相比微不足道。问题在于对 `bytes` 实例进行切片会导致底层数据被复制，这会消耗 CPU 时间。

编写此代码的更好方法是使用 Python 的内置 `memoryview` 类型，它将 CPython 的高性能**buffer protocol**暴露给程序。Buffer protocol 是一个低级 C API，它允许 Python 运行时和 C 扩展（参见 [Item 96](#ch11#ch11lev1sec5): “[Consider Extension Modules to Maximize Performance and Ergonomics](#ch11#ch11lev1sec5)”）访问 `bytes` 实例等对象背后的底层数据缓冲区。`memoryview` 实例最好的部分是切片它们会产生另一个 `memoryview` 实例，而无需复制底层数据。这里我创建一个包装 `bytes` 实例的 `memoryview` 实例并检查其切片：
[Click here to view code image](#ch11_images#f0487-02)
```
data = b"shave and a haircut, two bits"
view = memoryview(data)
chunk = view[12:19]
print(chunk)
print("Size:           ", chunk.nbytes)
print("Data in view:   ", chunk.tobytes())
print("Underlying data:", chunk.obj)

>>>
<memory at 0x105407940>
Size:            7
Data in view:    b'haircut'
Underlying data: b'shave and a haircut, two bits'
```
通过启用**zero-copy**操作，`memoryview` 可以为需要快速处理大量内存的代码提供巨大的加速，例如 NumPy 等数值 C 扩展和此类的 I/O 密集型程序。这里我用 `memoryview` 切片替换上面的简单 `bytes` 切片，并重复相同的 microbenchmark：
[Click here to view code image](#ch11_images#f0488-01)
```
video_view = memoryview(video_data)

def run_test():
chunk = video_view[byte_offset : byte_offset + size]
# Call socket.send(chunk), but ignoring for benchmark

result = (
timeit.timeit(
stmt="run_test()",
globals=globals(),
number=100,
)
/ 100
)

print(f"{result:0.9f} seconds")

>>>
0.000000250 seconds
```
结果是 250 纳秒。现在我的服务器的理论最大吞吐量是 20 MB / 250 纳秒 = 80 TB/秒。对于并行客户端，我理论上可以支持多达 1 CPU 秒 / 250 纳秒 = 400 万。这更像话了！这意味着我的程序现在完全受限于与客户端的套接字连接的底层性能，而不是 CPU 限制。

现在想象一下数据必须朝另一个方向流动，其中一些客户端正在向服务器发送实时视频流以将其广播给其他用户。为了处理这个问题，我需要将用户最新的视频数据存储在其他客户端可以读取的缓存中。以下是读取 1 MB 新数据从传入客户端的外观：
[Click here to view code image](#ch11_images#f0488-02)
```
socket = ...        # socket connection to the client
video_cache = ...   # Cache of incoming video stream
byte_offset = ...   # Incoming buffer position
size = 1024 * 1024  # Incoming chunk size

chunk = socket.recv(size)
video_view = memoryview(video_cache)
before = video_view[:byte_offset]
after = video_view[byte_offset + size :]
new_cache = b"".join([before, chunk, after])
```
`socket.recv` 方法返回一个 `bytes` 实例。我可以通过使用简单的切片操作和 `bytes.join` 方法，在当前的 `byte_offset` 处将新数据与现有缓存拼接起来。为了理解这个性能，我可以运行另一个 microbenchmark。我使用的是一个虚拟套接字实现，因此性能测试仅针对内存操作，而不是 I/O 交互：
[Click here to view code image](#ch11_images#f0489-01)
```
def run_test():
chunk = socket.recv(size)
before = video_view[:byte_offset]
after = video_view[byte_offset + size :]
new_cache = b"".join([before, chunk, after])

result = (
timeit.timeit(
stmt="run_test()",
globals=globals(),
number=100,
)
/ 100
)

print(f"{result:0.9f} seconds")

>>>
0.033520550 seconds
```
接收 1 MB 并更新视频缓存需要 33 毫秒。这意味着我的最大接收吞吐量是 1 MB / 33 毫秒 = 31 MB/秒，并且我限制为 31 MB / 1 MB = 31 个同时客户端以这种方式流式传输视频数据。这无法扩展。

编写此代码的更好方法是使用 Python 的内置 `bytearray` 类型并结合 `memoryview`。`bytes` 实例的一个限制是它们是只读的，不允许覆盖单个索引：
[Click here to view code image](#ch11_images#f0489-02)
```
my_bytes = b"hello"
my_bytes[0] = 0x79

>>>
Traceback ...
TypeError: 'bytes' object does not support item assignment
```
`bytearray` 类型类似于 `bytes` 的可变版本，允许覆盖任意位置。`bytearray` 使用整数作为其值，而不是 `bytes`：
[Click here to view code image](#ch11_images#f0490-01)
```
my_array = bytearray(b"hello")
my_array[0] = 0x79
print(my_array)

>>>
bytearray(b'yello')
```
`memoryview` 对象也可以用于包装 `bytearray` 实例。当您切片 `memoryview` 时，结果对象可用于将数据分配给底层缓冲区的特定部分。这消除了上面为了在从客户端接收数据后将 `bytes` 实例拼接在一起而需要的复制成本：
[Click here to view code image](#ch11_images#f0490-02)
```
my_array = bytearray(b"row, row, row your boat")
my_view = memoryview(my_array)
write_view = my_view[3:13]
write_view[:] = b"-10 bytes-"
print(my_array)

>>>
bytearray(b'row-10 bytes- your boat')
```
Python 中的许多库方法，例如 `socket.recv_into` 和 `RawIOBase.readinto`，都使用 buffer protocol 来快速接收或读取数据。这些方法的优点是它们避免了分配内存和创建数据的另一个副本；接收到的数据直接进入现有缓冲区。这里我使用 `socket.recv_into` 和 `memoryview` 切片将数据接收到底层 `bytearray` 中，而无需任何拼接：
[Click here to view code image](#ch11_images#f0490-03)
```
video_array = bytearray(video_cache)
write_view = memoryview(video_array)
chunk = write_view[byte_offset : byte_offset + size]
socket.recv_into(chunk)
```
我可以运行另一个 microbenchmark 来比较此方法与早期使用 `socket.recv` 的示例的性能：
[Click here to view code image](#ch11_images#f0490-04)
```
def run_test():
chunk = write_view[byte_offset : byte_offset + size]
socket.recv_into(chunk)

result = (
timeit.timeit(
stmt="run_test()",
globals=globals(),
number=100,
)
/ 100
)

print(f"{result:0.9f} seconds")

>>>
0.000033925 seconds
```
接收 1 MB 视频传输需要 33 微秒。这意味着我的服务器可以支持 1 MB / 33 微秒 = 31 GB/秒的最大吞吐量，以及 31 GB / 1 MB = 31,000 个并行流式传输客户端。这正是我想要的扩展性！

#### Things to Remember
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `memoryview` 内置类型为读取和写入支持 Python 高性能 buffer protocol 的对象的切片提供了零拷贝（zero-copy）接口。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `bytearray` 内置类型提供了一个可变的 `bytes` 类类型，可用于与 `socket.recv_from` 等函数进行零拷贝数据读取。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `memoryview` 可以包装 `bytearray`，允许将接收到的数据无复制成本地拼接（splice）到任意缓冲区位置。
---
<a role="toc_link" id="ch12"></a>

## Effective Python - 12

## 12

本章深入探讨了 Graph Neural Networks (GNNs) 在处理和理解复杂数据结构方面的强大能力，特别关注了 Graph Foundation Models (GFMs) 的兴起及其在各种下游任务中的应用。本章的核心贡献在于阐述了 GNNs 如何通过其独特的架构，如 Message Passing 机制，有效地捕捉图数据的拓扑结构和节点间的关系，从而实现诸如 Node Embedding、Graph Classification、Node Classification 和 Link Prediction 等任务。

本章首先回顾了 GNNs 的基本原理，包括 Graph Convolutional Networks (GCN) 和 Graph Attention Networks (GAT) 等经典模型，并解释了它们如何通过聚合邻居节点的信息来学习节点表示。随后，本章重点介绍了 Graph Foundation Models (GFMs) 的概念，强调了它们通过大规模预训练（Pre-training）和 Self-supervised Learning 来学习通用的图表示能力。这些模型能够从海量无标签的图数据中学习到丰富的、可迁移的知识，为后续的 Fine-tuning、In-context Learning、Few-shot Learning 和 Zero-shot Learning 任务奠定了基础。

本章详细讨论了 GFMs 在处理不同类型图数据时的优势，包括 Homogeneous Graph 和 Heterogeneous Graph。此外，本章还探讨了 GFMs 在多模态学习（Multi-modal Learning）和跨领域迁移（Cross-domain Transfer）方面的潜力，以及如何通过 Domain Adaptation 技术将预训练模型应用于新的、未见过的数据领域。

本章还涵盖了 GNNs 在更广泛的应用场景，例如 Knowledge Graph 的表示学习、Graph Pooling 技术在图表示学习中的作用、Graph Generation 以创造新的图结构、Graph Anomaly Detection 以识别异常节点或边，以及 Contrastive Learning 在提升图表示鲁棒性方面的应用。最后，本章对 GNNs 和 GFMs 的未来发展方向进行了展望，包括解决 Graph Isomorphism 问题、提升模型的可解释性以及探索更高效的训练和推理方法。

## Effective Python - Data Structures and Algorithms

# Effective Python - Data Structures and Algorithms

## Data Structures and Algorithms

在实现处理大量数据的Python程序时，您经常会遇到由代码的算法复杂度引起的性能下降。例如，您期望线性扩展的程序，其性能可能实际上是二次方增长的，从而在生产环境中造成问题。幸运的是，Python包含了许多标准数据结构和算法的优化实现，可以帮助您以最小的努力实现高性能。

同样，Python提供了内置的数据类型和辅助函数，用于处理程序中经常出现的常见任务：操作日期、时间和时区；在保持精度和控制舍入行为的同时处理货币值；以及在软件不断发展的同时，为用户保存和恢复程序状态。处理这些情况的代码编写起来很棘手且难以正确。拥有内置的、经过实战检验的实现来处理它们是一种恩赐。

### Item 100: 使用 `key` 参数按复杂条件排序

`list` 内置类型提供了一个 `sort` 方法，用于根据各种条件对 `list` 实例中的项进行排序。（不要将 `sort` 方法与 `sorted` 混淆；请参阅 [Item 101](#ch12#ch12lev1sec2)：“[了解 `sort` 和 `sorted` 之间的区别](#ch12#ch12lev1sec2)”。）默认情况下，`sort` 按项的自然升序对列表内容进行排序。例如，我在此对整数列表进行排序，从小到大：

[点击此处查看代码图像](#ch12_images#f0493-01)

```python
numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers)

>>>
[11, 68, 70, 86, 93]
```

`sort` 方法适用于几乎所有具有自然排序的内置类型（字符串、浮点数等）。`sort` 如何处理对象？例如，我在此定义一个类——包括一个 `__repr__` 方法，以便实例可以打印（请参阅 [Item 12](#ch02#ch02lev1sec3)：“[了解 `repr` 和 `str` 在打印对象时的区别](#ch02#ch02lev1sec3)”）——来表示您在建筑工地上可能需要使用的各种工具：

[点击此处查看代码图像](#ch12_images#f0494-01)

```python
class Tool:
def __init__(self, name, weight):
self.name = name
self.weight = weight

def __repr__(self):
return f"Tool({self.name!r}, {self.weight})"

tools = [
Tool("level", 3.5),
Tool("hammer", 1.25),
Tool("screwdriver", 0.5),
Tool("chisel", 0.25),
]
```

对这种类型的对象进行排序不起作用，因为 `sort` 方法尝试调用类中未定义的比较特殊方法：

[点击此处查看代码图像](#ch12_images#f0494-02)

```python
tools.sort()

>>>
Traceback ...
TypeError: '<' not supported between instances of 'Tool' and
➥'Tool'
```

如果您的类应该像整数一样具有自然排序，那么您可以定义必要的特殊方法（请参阅 [Item 104](#ch12#ch12lev1sec5)：“[了解如何使用 `heapq` 实现优先队列](#ch12#ch12lev1sec5)” 获取示例，以及 [Item 57](#ch07#ch07lev1sec10)：“[继承 `collections.abc` 类以创建自定义容器类型](#ch07#ch07lev1sec10)” 获取背景信息），以使 `sort` 在没有额外参数的情况下工作。但更常见的情况是，您的对象可能需要支持多种排序方式，在这种情况下，定义单一的自然排序实际上没有意义。

通常，对象上有一个您希望用于排序的属性。为了支持此用例，`sort` 方法接受一个 `key` 参数，该参数预计是一个函数（请参阅 [Item 48](#ch07#ch07lev1sec1)：“[为简单接口接受函数而不是类](#ch07#ch07lev1sec1)” 获取背景信息）。`key` 函数接收一个参数，该参数是正在排序列表中的一个项。`key` 函数的返回值应该是用于排序目的的可比较值（即具有自然排序），而不是项本身。

我在此使用 `lambda` 关键字（请参阅 [Item 39](#ch05#ch05lev1sec10)：“[为胶水函数偏好 `functools.partial` 而非 `lambda` 表达式](#ch05#ch05lev1sec10)” 获取背景信息）为 `key` 参数定义一个函数，该函数使我能够按 `name` 属性按字母顺序对 `Tool` 对象列表进行排序：

[点击此处查看代码图像](#ch12_images#f0495-01)

```python
print("Unsorted:", repr(tools))
tools.sort(key=lambda x: x.name)
print("\nSorted:  ", tools)

>>>
Unsorted: [Tool('level', 3.5), Tool('hammer', 1.25),
➥Tool('screwdriver', 0.5), Tool('chisel', 0.25)]

Sorted:   [Tool('chisel', 0.25), Tool('hammer', 1.25),
➥Tool('level', 3.5), Tool('screwdriver', 0.5)]
```

我可以同样轻松地定义另一个 lambda 函数来按 `weight` 属性排序，并将其作为 `key` 参数传递给 `sort` 方法：

[点击此处查看代码图像](#ch12_images#f0495-02)

```python
tools.sort(key=lambda x: x.weight)
print("By weight:", tools)

>>>
By weight: [Tool('chisel', 0.25), Tool('screwdriver', 0.5),
➥Tool('hammer', 1.25), Tool('level', 3.5)]
```

在作为 `key` 参数传递的 lambda 函数中，您可以访问项的属性，如我在此所做的那样，索引到项（对于序列、元组和字典），或使用任何其他有效表达式。

对于字符串等基本类型，您甚至可能希望使用 `key` 函数在排序前对值进行转换。例如，我在此将 `lower` 方法应用于名称列表中的每个项，以确保它们按字母顺序排列，忽略任何大小写（因为在字符串的自然词法排序中，大写字母出现在小写字母之前）：

[点击此处查看代码图像](#ch12_images#f0495-03)

```python
places = ["home", "work", "New York", "Paris"]
places.sort()
print("Case sensitive:  ", places)
places.sort(key=lambda x: x.lower())
print("Case insensitive:", places)

>>>
Case sensitive:   ['New York', 'Paris', 'home', 'work']
Case insensitive: ['home', 'New York', 'Paris', 'work']
```

有时您可能需要使用多个条件进行排序。例如，假设我有一个电动工具列表，我想先按 `weight` 属性排序，然后按 `name` 排序。我该如何实现这一点？

```python
power_tools = [
Tool("drill", 4),
Tool("circular saw", 5),
Tool("jackhammer", 40),
Tool("sander", 4),
]
```

Python 中最简单的解决方案是使用 `tuple` 类型（请参阅 [Item 56](#ch07#ch07lev1sec9)：“[为创建不可变对象偏好 `dataclasses`](#ch07#ch07lev1sec9)” 获取另一种方法）。元组是任意 Python 值的不可变序列。元组默认是可比较的，并且具有自然排序，这意味着它们实现了 `sort` 方法所需的所有特殊方法，例如 `__lt__`。`tuple` 类型通过迭代元组的每个位置并逐个比较相应的值来实现特殊比较器方法。我在此展示当一个工具比另一个工具重时，这如何工作：

[点击此处查看代码图像](#ch12_images#f0496-01)

```python
saw = (5, "circular saw")
jackhammer = (40, "jackhammer")
assert not (jackhammer < saw)  # 符合预期
```

如果正在比较的元组的第一个位置相等——在这种情况下是重量——则元组比较将移动到第二个位置，依此类推：

[点击此处查看代码图像](#ch12_images#f0496-02)

```python
drill = (4, "drill")
sander = (4, "sander")
assert drill[0] == sander[0]  # 重量相同
assert drill[1] < sander[1]   # 按字母顺序较小
assert drill < sander         # 因此，drill 靠前
```

您可以利用这种元组比较行为，以便先按重量再按名称对电动工具列表进行排序。我在此定义一个 `key` 函数，该函数返回一个包含我想要排序的两个属性的元组，按优先级顺序排列：

[点击此处查看代码图像](#ch12_images#f0496-03)

```python
power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)

>>>
[Tool('drill', 4), Tool('sander', 4), Tool('circular saw', 5),
➥Tool('jackhammer', 40)]
```

`key` 函数返回元组的一个限制是，所有条件的排序方向必须相同（全部升序或全部降序）。如果我向 `sort` 方法提供 `reverse` 参数，它将以相同的方式影响元组中的两个条件（请注意 `sander` 现在如何出现在 `drill` 之前而不是之后）：

[点击此处查看代码图像](#ch12_images#f0497-01)

```python
power_tools.sort(
key=lambda x: (x.weight, x.name),
reverse=True,  # 使所有条件降序
)
print(power_tools)

>>>
[Tool('jackhammer', 40), Tool('circular saw', 5),
➥Tool('sander', 4), Tool('drill', 4)]
```

对于数值，可以通过在 `key` 函数中使用一元减号运算符来混合排序方向。这会否定返回元组中的一个值，从而有效地反转其排序顺序，同时保持其他值不变。我在此使用此方法按重量降序然后按名称升序排序（请注意 `sander` 现在如何出现在 `drill` 之后而不是之前）：

[点击此处查看代码图像](#ch12_images#f0497-02)

```python
power_tools.sort(key=lambda x: (-x.weight, x.name))
print(power_tools)

>>>
[Tool('jackhammer', 40), Tool('circular saw', 5), Tool
➥('drill', 4), Tool('sander', 4)]
```

不幸的是，一元否定并非对所有类型都适用。我在此尝试通过使用 `reverse` 参数按重量降序排序，然后否定 `name` 属性以将其升序排列来达到相同的效果：

[点击此处查看代码图像](#ch12_images#f0497-03)

```python
power_tools.sort(key=lambda x: (x.weight, -x.name),
reverse=True)

>>>
Traceback ...
TypeError: bad operand type for unary -: 'str'
```

对于这种情况，Python 提供了一个 _稳定_ 的排序算法。`list` 类型的 `sort` 方法在 `key` 函数返回相等的返回值时会保留输入列表的顺序。这意味着我可以对同一个列表多次调用 `sort` 来组合不同的条件。我在此通过两次单独调用 `sort` 来产生与上面相同的重量降序和名称升序的排序：

[点击此处查看代码图像](#ch12_images#f0498-01)

```python
power_tools.sort(
key=lambda x: x.name,    # 名称升序
)
power_tools.sort(
key=lambda x: x.weight,  # 重量降序
reverse=True,
)
print(power_tools)

>>>
[Tool('jackhammer', 40), Tool('circular saw', 5),
Tool('drill', 4), Tool('sander', 4)]
```

要理解为什么这有效，请注意第一次调用 `sort` 如何按字母顺序排列名称：

[点击此处查看代码图像](#ch12_images#f0498-02)

```python
power_tools.sort(key=lambda x: x.name)
print(power_tools)

>>>
[Tool('circular saw', 5), Tool('drill', 4),
➥Tool('jackhammer', 40), Tool('sander', 4)]
```

当第二次按重量降序调用 `sort` 时，代码会看到 `sander` 和 `drill` 的重量都是 `4`。这会导致 `sort` 方法将这两个项以它们在原始列表中出现的顺序放入最终结果列表中，从而保留它们按名称升序的相对顺序：

[点击此处查看代码图像](#ch12_images#f0498-03)

```python
power_tools.sort(
key=lambda x: x.weight,
reverse=True,
)
print(power_tools)

>>>
[Tool('jackhammer', 40), Tool('circular saw', 5),
➥Tool('drill', 4), Tool('sander', 4)]
```

此方法可用于以任何方向组合任意数量的不同排序条件。您只需要确保按照与最终列表期望的顺序相反的顺序执行排序。在此示例中，我希望排序顺序是重量降序然后名称升序，因此我必须先进行名称排序，然后进行重量排序。

尽管如此，让 `key` 函数返回元组并使用一元否定来混合排序顺序的方法更易于阅读且代码量更少。我建议仅在绝对必要时才使用多次调用 `sort`。

#### 记住要点

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `list` 类型的 `sort` 方法可用于按字符串、整数、元组等内置类型的自然排序来重新排列列表的内容。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `sort` 方法对对象不起作用，除非它们使用特殊方法定义了自然排序，这并不常见。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `sort` 方法的 `key` 参数可用于提供一个辅助函数，该函数返回在排序时用于替换列表中每个项的值。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 从 `key` 函数返回元组允许您组合多个排序条件。一元减号运算符可用于反转允许的类型的单个排序顺序。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 对于不能进行否定的类型，您可以通过使用不同的 `key` 函数和 `reverse` 值多次调用 `sort` 方法来组合多个排序条件，按从最低排名 `sort` 调用到最高排名 `sort` 调用的顺序。

### Item 101: 了解 `sort` 和 `sorted` 之间的区别

在 Python 中对数据进行排序最熟悉的方式是使用 `list` 类型内置的 `sort` 方法（请参阅 [Item 100](#ch12#ch12lev1sec1)：“[使用 `key` 参数按复杂条件排序](#ch12#ch12lev1sec1)”)。此方法会就地排序数据，这意味着原始列表被修改，并且未排序的排列不再可用。例如，我在此对蝴蝶名称列表进行字母排序：

[点击此处查看代码图像](#ch12_images#f0499-01)

```python
butterflies = ["Swallowtail", "Monarch", "Red Admiral"]
print(f"Before {butterflies}")
butterflies.sort()
print(f"After {butterflies}")

>>>
Before ['Swallowtail', 'Monarch', 'Red Admiral']
After ['Monarch', 'Red Admiral', 'Swallowtail']
```

在 Python 中对数据进行排序的另一种方法是使用 `sorted` 内置函数。此函数对给定对象的內容进行排序，并将结果作为列表返回，同时保持原始对象不变：

[点击此处查看代码图像](#ch12_images#f0500-01)

```python
original = ["Swallowtail", "Monarch", "Red Admiral"]
alphabetical = sorted(original)
print(f"Original {original}")
print(f"Sorted   {alphabetical}")

>>>
Original ['Swallowtail', 'Monarch', 'Red Admiral']
Sorted   ['Monarch', 'Red Admiral', 'Swallowtail']
```

`sorted` 内置函数可与任何可迭代对象一起使用（请参阅 [Item 21](#ch03#ch03lev1sec5)：“[迭代参数时要谨慎](#ch03#ch03lev1sec5)”），包括元组、字典和集合：

[点击此处查看代码图像](#ch12_images#f0500-02)

```python
patterns = {"solid", "spotted", "cells"}
print(sorted(patterns))

>>>
['cells', 'solid', 'spotted']
```

它还支持 `reverse` 和 `key` 参数，就像 `sort` 内置函数一样（请参阅 [Item 100](#ch12#ch12lev1sec1)：“[使用 `key` 参数按复杂条件排序](#ch12#ch12lev1sec1)”）：

[点击此处查看代码图像](#ch12_images#f0500-03)

```python
legs = {"insects": 6, "spiders": 8, "lizards": 4}
sorted_legs = sorted(
legs,
key=lambda x: legs[x],
reverse=True,
)
print(sorted_legs)

>>>
['spiders', 'insects', 'lizards']
```

使用 `sort` 而不是 `sorted` 有两个好处。首先，`sort` 会就地修改列表，这意味着您的程序在排序期间和之后消耗的内存将保持不变。另一方面，`sorted` 需要复制可迭代对象的內容才能生成排序列表，这可能会使您程序的内存需求加倍。其次，`sort` 可能快得多，因为它总共做的工作更少。结果列表已经确定，不需要分配或调整大小。迭代只需要发生在列表上，而不是发生在任意可迭代对象上。如果数据已经部分排序，则可以完全避免索引重新分配。

然而，使用 `sorted` 而不是 `sort` 有两个主要好处。首先，原始对象保持不变，确保您不会无意中修改传递给函数的参数并导致令人费解的错误（请参阅 [Item 30](#ch05#ch05lev1sec1)：“[了解函数参数可以被修改](#ch05#ch05lev1sec1)” 和 [Item 56](#ch07#ch07lev1sec9)：“[为创建不可变对象偏好 `dataclasses`](#ch07#ch07lev1sec9)” 获取背景信息）。其次，`sorted` 可用于任何类型的迭代器，而不仅仅是列表，这意味着您的函数可以依赖于 _鸭子类型_ 并接受更灵活的类型（请参阅 [Item 25](#ch04#ch04lev1sec1)：“[依赖字典插入顺序时要小心](#ch04#ch04lev1sec1)” 获取示例）。

可以说，`sorted` 比 `sort` 更 Pythonic，因为它提供了额外的灵活性，并且在生成结果方面更加明确。选择使用哪一个取决于具体情况以及您要完成的任务。

#### 记住要点

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `sort` 以最小的内存开销实现最大性能，但要求目标列表被就地修改。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `sorted` 可以处理所有类型的迭代器和集合作为输入，并且不会无意中修改数据。

### Item 102: 考虑使用 `bisect` 搜索已排序序列

通常，您会发现内存中存在大量数据，这些数据以已排序列表的形式存在，然后您想搜索它。例如，您可能加载了一个英语词典用于拼写检查，或者您可能有一个按日期排序的金融交易列表需要审计其正确性。

无论您的特定程序需要处理什么数据，当您调用 `index` 方法时，在列表中搜索特定值需要与列表长度成正比的线性时间：

```python
data = list(range(10**5))
index = data.index(91234)
assert index == 91234
```

如果您不确定您正在搜索的确切值是否存在于列表中，您可能希望搜索等于或大于目标值的最近索引。最简单的方法是线性扫描列表并比较每个项与您的目标值：

[点击此处查看代码图像](#ch12_images#f0501-01)

```python
def find_closest(sequence, goal):
for index, value in enumerate(sequence):
if goal < value:
return index
raise ValueError(f"{goal} is out of bounds")

index = find_closest(data, 91234.56)
assert index == 91235
```

Python 的内置 `bisect` 模块通过有序列表提供了更好的方法来完成这些类型的搜索。您可以使用 `bisect_left` 函数对任何已排序项的序列进行高效的二进制搜索。它返回的索引将是该项已存在于列表中的位置，或者您希望将该项插入列表以保持其排序顺序的位置：

[点击此处查看代码图像](#ch12_images#f0502-02)

```python
from bisect import bisect_left

index = bisect_left(data, 91234)     # 精确匹配
assert index == 91234

index = bisect_left(data, 91234.56)  # 最近匹配
assert index == 91235
```

`bisect` 模块使用的二进制搜索算法的复杂度是对数的。这意味着搜索长度为 100 万的列表，使用 `bisect` 所需的时间大致与使用 `list.index` 方法线性搜索长度为 20 的列表所需的时间相同（`math.log2(10**6) == 19.93...`）。所以 `bisect` 快得多！

我可以通过使用 `timeit` 内置模块运行微基准测试来验证上面示例中的速度改进（请参阅 [Item 93](#ch11#ch11lev1sec2)：“[使用 `timeit` 微基准测试优化性能关键代码](#ch11#ch11lev1sec2)” 获取详细信息）：

[点击此处查看代码图像](#ch12_images#f0502-03)

```python
import random
import timeit

size = 10**5
iterations = 1000

data = list(range(size))
to_lookup = [random.randint(0, size)
for _ in range(iterations)]

def run_linear(data, to_lookup):
for index in to_lookup:
data.index(index)

def run_bisect(data, to_lookup):
for index in to_lookup:
bisect_left(data, index)

baseline = (
timeit.timeit(
stmt="run_linear(data, to_lookup)",
globals=globals(),
number=10,
)
/ 10
)
print(f"Linear search takes {baseline:.6f}s")

comparison = (
timeit.timeit(
stmt="run_bisect(data, to_lookup)",
globals=globals(),
number=10,
)
/ 10
)
print(f"Bisect search takes {comparison:.6f}s")

slowdown = 1 + ((baseline - comparison) / comparison)
print(f"{slowdown:.1f}x slower")

>>>
Linear search takes 0.317685s
Bisect search takes 0.000197s
1610.1x time
```

`bisect` 最棒的地方在于它不限于 `list` 类型；您可以使用它处理任何表现得像序列的 Python 对象（请参阅 [Item 57](#ch07#ch07lev1sec10)：“[继承 `collections.abc` 类以创建自定义容器类型](#ch07#ch07lev1sec10)” 获取如何做到这一点），其中包含具有自然排序的项（请参阅 [Item 104](#ch12#ch12lev1sec5)：“[了解如何使用 `heapq` 实现优先队列](#ch12#ch12lev1sec5)” 获取背景信息）。该模块还为更高级的场景提供了其他功能（请参阅 <https://docs.python.org/3/library/bisect.html>）。

#### 记住要点

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `index` 方法或带有简单比较的 `for` 循环搜索列表中的已排序数据需要线性时间。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `bisect` 内置模块的 `bisect_left` 函数以对数时间搜索已排序列表中的值，这可能比其他方法快几个数量级。

### Item 103: 偏好 `deque` 用于生产者-消费者队列

编写程序的一个常见需求是先进先出（FIFO）队列，也称为 _生产者-消费者队列_。当一个函数收集值进行处理，而另一个函数按接收顺序处理它们时，就会使用 FIFO 队列。通常，程序员会转向 Python 的内置 `list` 类型来充当 FIFO 队列。

例如，假设我正在编写一个处理传入电子邮件以进行长期存档的程序，并且它使用列表作为生产者-消费者队列。我在此定义一个类来表示消息：

[点击此处查看代码图像](#ch12_images#f0504-01)

```python
class Email:
def __init__(self, sender, receiver, message):
self.sender = sender
self.receiver = receiver
self.message = message

...
```

我还定义了一个用于接收单个电子邮件的占位符函数，可能是从套接字、文件系统或其他类型的 I/O 系统接收。此函数的实现并不重要；重要的是其接口：它将返回一个 `Email` 实例或引发一个 `NoEmailError` 异常（请参阅 [Item 32](#ch05#ch05lev1sec3)：“[偏好引发异常而不是返回 `None`](#ch05#ch05lev1sec3)” 获取有关此约定的更多信息）：

[点击此处查看代码图像](#ch12_images#f0504-02)

```python
class NoEmailError(Exception):
pass

def try_receive_email():
# 返回一个 Email 实例或引发 NoEmailError
...
```

生产者函数接收电子邮件并将其入队，以便稍后处理。此函数使用列表的 `append` 方法将新消息添加到队列的末尾，以便在所有先前接收的消息之后处理它们：

[点击此处查看代码图像](#ch12_images#f0504-03)

```python
def produce_emails(queue):
while True:
try:
email = try_receive_email()
except NoEmailError:
return
else:
queue.append(email)  # Producer
```

消费者函数是处理电子邮件的函数。此函数调用队列上的 `pop(0)`，它会从列表中删除第一个项并将其返回给调用者。通过始终从队列的开头处理项，消费者确保项按接收顺序处理：

[点击此处查看代码图像](#ch12_images#f0505-01)

```python
def consume_one_email(queue):
if not queue:
return
email = queue.pop(0)  # Consumer
# 索引消息以进行长期存档
...
```

最后，我需要一个循环函数来连接这些部分。此函数在生产和消费之间交替进行，直到 `keep_running` 函数返回 `False`（请参阅 [Item 75](#ch09#ch09lev1sec9)：“[使用协程实现高并发 I/O](#ch09#ch09lev1sec9)” 获取如何并发执行此操作）：

[点击此处查看代码图像](#ch12_images#f0505-02)

```python
def loop(queue, keep_running):
while keep_running():
produce_emails(queue)
consume_one_email(queue)

def my_end_func():
...

loop([], my_end_func)
```

为什么不在 `produce_emails` 中处理 `try_receive_email` 返回的每个 `Email` 对象？这归结为延迟和吞吐量之间的权衡。在使用生产者-消费者队列时，您通常希望最小化接受新项的延迟，以便它们能够尽快收集。然后，消费者可以以一致的速率处理积压的项——在此示例中，每个循环一个项——这提供了稳定的性能特征和一致的吞吐量，但代价是端到端延迟（请参阅 [Item 70](#ch09#ch09lev1sec4)：“[使用 Queue 在线程之间协调工作](#ch09#ch09lev1sec4)” 获取相关的最佳实践）。

将列表用作生产者-消费者队列可以正常工作，直到某个点，但随着 _基数_（即列表中的项数）的增加，`list` 类型的性能可能会以超线性速度下降。为了分析使用 `list` 作为 FIFO 队列的性能，我可以使用 `timeit` 内置模块运行一些微基准测试（请参阅 [Item 93](#ch11#ch11lev1sec2)：“[使用 `timeit` 微基准测试优化性能关键代码](#ch11#ch11lev1sec2)” 获取详细信息）。我在此定义一个基准测试，用于测试使用 `list` 的 `append` 方法向队列添加新项的性能（与生产者函数的使用相匹配）：

[点击此处查看代码图像](#ch12_images#f0506-01)

```python
import timeit

def list_append_benchmark(count):
def run(queue):
for i in range(count):
queue.append(i)

return timeit.timeit(
setup="queue = []",
stmt="run(queue)",
globals=locals(),
number=1,
)
```

使用不同基数级别的不同基准测试函数可以让我将其性能与数据大小进行比较：

[点击此处查看代码图像](#ch12_images#f0506-02)

```python
for i in range(1, 6):
count = i * 1_000_000
delay = list_append_benchmark(count)
print(f"Count {count:>5,} takes: {delay*1e3:>6.2f}ms")

>>>
Count 1,000,000 takes:  13.23ms
Count 2,000,000 takes:  26.50ms
Count 3,000,000 takes:  39.06ms
Count 4,000,000 takes:  51.98ms
Count 5,000,000 takes:  65.19ms
```

这表明 `append` 方法对于 `list` 类型需要大致恒定的时间，并且入队总时间随数据大小的增加而线性扩展。`list` 类型在添加新项时存在内部增加容量的开销，但它相当低，并且在多次调用 `append` 时被摊销。

我在此定义一个类似的基准测试，用于测试调用 `pop(0)` 以从队列开头移除项的性能（与消费者函数的使用相匹配）：

[点击此处查看代码图像](#ch12_images#f0506-03)

```python
def list_pop_benchmark(count):
def prepare():
return list(range(count))

def run(queue):
while queue:
queue.pop(0)

return timeit.timeit(
setup="queue = prepare()",
stmt="run(queue)",
globals=locals(),
number=1,
)
```

我同样可以为不同大小的队列运行此基准测试，以查看性能如何受到基数的影响：

[点击此处查看代码图像](#ch12_images#f0507-02)

```python
for i in range(1, 6):
count = i * 10_000
delay = list_pop_benchmark(count)
print(f"Count {count:>5,} takes: {delay*1e3:>6.2f}ms")

>>>
Count 10,000 takes:   4.98ms
Count 20,000 takes:  22.21ms
Count 30,000 takes:  60.04ms
Count 40,000 takes: 109.96ms
Count 50,000 takes: 176.92ms
```

令人惊讶的是，这表明使用 `pop(0)` 从列表中出队项的总时间随队列长度的增加而呈二次方增长。这是因为 `pop(0)` 需要将列表中的每个项向后移动一个索引，有效地重新分配整个列表的内容。我需要为列表中的每个项调用 `pop(0)`，因此最终会执行大约 `len(queue) * len(queue)` 次操作来消耗队列。这无法扩展。

Python 提供了 `collections` 内置模块中的 `deque` 类来解决此问题。`deque` 是一个 _双端队列_ 实现。它为从其开头或结尾插入或删除项提供了恒定的时间操作。这使其成为 FIFO 队列的理想选择。

要使用 `deque` 类，`produce_emails` 中的 `append` 调用可以与使用列表作为队列时相同。`consume_one_email` 中的 `list.pop` 方法调用必须更改为调用不带参数的 `deque.popleft` 方法。并且 `loop` 方法必须使用 `deque` 实例而不是列表来调用。其他一切都保持不变。我在此重新定义受影响的一个函数以使用新方法并再次运行 `loop`：

[点击此处查看代码图像](#ch12_images#f0507-03)

```python
import collections

def consume_one_email(queue):
if not queue:
return
email = queue.popleft()  # Consumer
# 处理电子邮件消息
...

def my_end_func():
...

loop(collections.deque(), my_end_func)
```

我可以运行另一个版本的基准测试，以验证 `append` 的性能（与生产者函数的使用相匹配）大致保持不变（除了一个常数因子）：

[点击此处查看代码图像](#ch12_images#f0508-02)

```python
def deque_append_benchmark(count):
def prepare():
return collections.deque()

def run(queue):
for i in range(count):
queue.append(i)

return timeit.timeit(
setup="queue = prepare()",
stmt="run(queue)",
globals=locals(),
number=1,
)

for i in range(1, 6):
count = i * 100_000
delay = deque_append_benchmark(count)
print(f"Count {count:>5,} takes: {delay*1e3:>6.2f}ms")

>>>
Count 100,000 takes:   1.68ms
Count 200,000 takes:   3.16ms
Count 300,000 takes:   5.05ms
Count 400,000 takes:   6.81ms
Count 500,000 takes:   8.43ms
```

并且我还可以对调用 `popleft` 的性能进行基准测试，以模拟消费者函数对 `deque` 的使用：

[点击此处查看代码图像](#ch12_images#f0508-03)

```python
def dequeue_popleft_benchmark(count):
def prepare():
return collections.deque(range(count))

def run(queue):
while queue:
queue.popleft()

return timeit.timeit(
setup="queue = prepare()",
stmt="run(queue)",
globals=locals(),
number=1,
)

for i in range(1, 6):
count = i * 100_000
delay = dequeue_popleft_benchmark(count)
print(f"Count {count:>5,} takes: {delay*1e3:>6.2f}ms")

>>>
Count 100,000 takes:   1.67ms
Count 200,000 takes:   3.59ms
Count 300,000 takes:   5.65ms
Count 400,000 takes:   7.50ms
Count 500,000 takes:   9.58ms
```

与我之前测量的超线性行为相比，`popleft` 的使用呈线性增长——太棒了！如果您知道程序的性能关键地依赖于生产者-消费者队列的速度，那么 `deque` 是一个不错的选择。如果您不确定，那么您应该对程序进行仪表化以找出答案（请参阅 [Item 92](#ch11#ch11lev1sec1)：“[优化前进行性能分析](#ch11#ch11lev1sec1)”）。

#### 记住要点

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `list` 类型可以通过生产者调用 `append` 添加项，消费者调用 `pop(0)` 接收项来用作 FIFO 队列。但是，这可能会导致问题，因为 `pop(0)` 的性能随队列长度的增加而呈超线性下降。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `collections` 内置模块中的 `deque` 类对 `append` 和 `popleft` 具有恒定的时间——与长度无关——使其成为 FIFO 队列的理想选择。

### Item 104: 了解如何使用 `heapq` 实现优先队列

Python 其他队列实现的一个限制（请参阅 [Item 103](#ch12#ch12lev1sec4)：“[偏好 `deque` 用于生产者-消费者队列](#ch12#ch12lev1sec4)” 和 [Item 70](#ch09#ch09lev1sec4)：“[使用 Queue 在线程之间协调工作](#ch09#ch09lev1sec4)”）是它们是先进先出（FIFO）队列：它们的內容按接收顺序排序。通常，您需要程序按相对重要性顺序处理项。为此，_优先队列_ 是最合适的工具。

例如，假设我正在编写一个程序来管理从图书馆借阅的书籍。有人不断借阅新书。有人按时归还借阅的书籍。有人需要被提醒归还逾期书籍。我在此定义一个类来表示已借阅的书籍：

[点击此处查看代码图像](#ch12_images#f0510-01)

```python
class Book:
def __init__(self, title, due_date):
self.title = title
self.due_date = due_date
```

当每本书超过到期日期时，我需要一个系统来发送提醒消息。不幸的是，我不能为此使用 FIFO 队列，因为每本书允许借阅的时间量因其新近度、受欢迎程度和其他因素而异。例如，今天借阅的书可能比明天借阅的书晚到期。我在此通过使用标准列表并在每次添加新的 `Book` 对象时按 `due_date` 属性对其进行排序来实现此行为：

[点击此处查看代码图像](#ch12_images#f0510-02)

```python
def add_book(queue, book):
queue.append(book)
queue.sort(key=lambda x: x.due_date, reverse=True)

queue = []
add_book(queue, Book("Don Quixote", "2019-06-07"))
add_book(queue, Book("Frankenstein", "2019-06-05"))
add_book(queue, Book("Les Misérables", "2019-06-08"))
add_book(queue, Book("War and Peace", "2019-06-03"))
```

如果我可以假设借阅书籍的队列始终处于排序状态，那么我所要做的就是检查列表中的最后一个元素。我在此定义一个函数来返回下一个逾期书籍（如果存在），并将其从队列中移除：

[点击此处查看代码图像](#ch12_images#f0510-03)

```python
class NoOverdueBooks(Exception):
pass

def next_overdue_book(queue, now):
if queue:
book = queue[-1]
if book.due_date < now:
queue.pop()
return book

raise NoOverdueBooks
```

我可以反复调用此函数来获取逾期书籍，以便从最逾期到最不逾期进行提醒：

[点击此处查看代码图像](#ch12_images#f0511-02)

```python
now = "2019-06-10"

found = next_overdue_book(queue, now)
print(found.due_date, found.title)

found = next_overdue_book(queue, now)
print(found.due_date, found.title)

>>>
2019-06-03 War and Peace
2019-06-05 Frankenstein
```

如果一本书在到期日期前归还，我可以删除计划的提醒消息，方法是从列表中删除该书：

[点击此处查看代码图像](#ch12_images#f0511-03)

```python
def return_book(queue, book):
queue.remove(book)

queue = []
book = Book("Treasure Island", "2019-06-04")

add_book(queue, book)
print("Before return:", [x.title for x in queue])

return_book(queue, book)
print("After return: ", [x.title for x in queue])

>>>
Before return: ['Treasure Island']
After return:  []
```

并且我可以确认当所有书籍都归还时，`return_book` 函数将引发正确的异常（请参阅 [Item 32](#ch05#ch05lev1sec3)：“[偏好引发异常而不是返回 `None`](#ch05#ch05lev1sec3)” 获取此约定）：

[点击此处查看代码图像](#ch12_images#f0511-04)

```python
try:
next_overdue_book(queue, now)
except NoOverdueBooks:
pass          # 预期
else:
assert False  # 不会发生
```

然而，这个解决方案的计算复杂度并不理想。虽然检查和移除逾期书籍的成本是恒定的，但每次添加书籍时，我都需要为再次排序整个列表付出成本。如果我有 `len(queue)` 本书要添加，并且对它们进行排序的成本大约是 `len(queue) * math.log(len(queue))`，那么添加书籍所需的时间将呈超线性增长（`len(queue) * len(queue) * math.log(len(queue))`）。

我在此定义一个微基准测试，以通过使用 `timeit` 内置模块来实验性地测量此性能行为（请参阅 [Item 93](#ch11#ch11lev1sec2)：“[使用 `timeit` 微基准测试优化性能关键代码](#ch11#ch11lev1sec2)” 获取详细信息）：

[点击此处查看代码图像](#ch12_images#f0512-01)

```python
import random
import timeit

def list_overdue_benchmark(count):
def prepare():
to_add = list(range(count))
random.shuffle(to_add)
return [], to_add

def run(queue, to_add):
for i in to_add:
queue.append(i)
queue.sort(reverse=True)

while queue:
queue.pop()

return timeit.timeit(
setup="queue, to_add = prepare()",
stmt="run(queue, to_add)",
globals=locals(),
number=1,
)
```

我可以验证，随着借阅书籍数量的增加，添加和移除书籍的运行时间呈超线性增长：

[点击此处查看代码图像](#ch12_images#f0512-02)

```python
for i in range(1, 6):
count = i * 1_000
delay = list_overdue_benchmark(count)
print(f"Count {count:>5,} takes: {delay*1e3:>6.2f}ms")

>>>
Count 1,000 takes:   1.74ms
Count 2,000 takes:   5.87ms
Count 3,000 takes:  11.12ms
Count 4,000 takes:  19.80ms
Count 5,000 takes:  31.02ms
```

当一本书在到期日期前归还时，我需要进行线性扫描才能在队列中找到该书并将其删除。移除一本书会导致列表中所有后续项的索引向后移动，这会产生一个成本高昂且也呈超线性增长的成本。我在此定义另一个微基准测试来测试使用此函数返回书籍的性能：

[点击此处查看代码图像](#ch12_images#f0513-02)

```python
def list_return_benchmark(count):
def prepare():
queue = list(range(count))
random.shuffle(queue)

to_return = list(range(count))
random.shuffle(to_return)

return queue, to_return

def run(queue, to_return):
for i in to_return:
queue.remove(i)

return timeit.timeit(
setup="queue, to_return = prepare()",
stmt="run(queue, to_return)",
globals=locals(),
number=1,
)
```

同样，我可以验证性能确实随着书籍数量的增加而呈超线性下降：

[点击此处查看代码图像](#ch12_images#f0513-03)

```python
for i in range(1, 6):
count = i * 1_000
delay = list_return_benchmark(count)
print(f"Count {count:>5,} takes: {delay*1e3:>6.2f}ms")

>>>
Count 1,000 takes:   1.97ms
Count 2,000 takes:   6.99ms
Count 3,000 takes:  14.59ms
Count 4,000 takes:  26.12ms
Count 5,000 takes:  40.38ms
```

使用 `list` 的方法可能适用于一个小型图书馆，但肯定无法扩展到亚历山大图书馆的规模，而我希望它能做到！

幸运的是，Python 拥有内置的 `heapq` 模块，它通过高效地实现优先队列来解决此问题。_堆_ 是一种数据结构，它允许维护一个项目列表，其中添加新项目或移除最小项目的计算复杂度是对数复杂度（即，比线性扩展更好）。在图书借阅示例中，最小意味着具有最早到期日期的书籍。`heapq` 最棒的地方在于，您不必了解堆的实现方式即可正确使用该模块的函数。

我在此使用 `heapq` 模块重新实现了 `add_book` 函数。队列仍然是一个普通列表。`heappush` 函数替换了之前的 `list.append` 调用。而且我不再需要对队列调用 `list.sort`：

```python
from heapq import heappush

def add_book(queue, book):
heappush(queue, book)
```

如果我尝试使用之前定义的 `Book` 类来使用它，我会收到这个有些晦涩的错误：

[点击此处查看代码图像](#ch12_images#f0514-02)

```python
queue = []
add_book(queue, Book("Little Women", "2019-06-05"))
add_book(queue, Book("The Time Machine", "2019-05-30"))

>>>
Traceback ...
TypeError: '<' not supported between instances of 'Book' and
➥'Book'
```

发生这种情况是因为 `heapq` 模块要求优先队列中的项是可比较的并且具有自然排序顺序（请参阅 [Item 100](#ch12#ch12lev1sec1)：“[使用 `key` 参数按复杂条件排序](#ch12#ch12lev1sec1)” 获取详细信息）。您可以通过使用 `functools` 内置模块的 `total_ordering` 类装饰器（请参阅 [Item 66](#ch08#ch08lev1sec9)：“[为可组合类扩展偏好类装饰器而非元类](#ch08#ch08lev1sec9)” 获取背景信息）并实现 `__lt__` 特殊方法（请参阅 [Item 57](#ch07#ch07lev1sec10)：“[继承 `collections.abc` 类以创建自定义容器类型](#ch07#ch07lev1sec10)” 获取背景信息）来快速为 `Book` 类提供此行为。

我在此使用仅比较两个 `Book` 实例的 `due_date` 字段的小于方法（`__lt__`）重新定义了该类：

[点击此处查看代码图像](#ch12_images#f0515-01)

```python
import functools

@functools.total_ordering
class Book:
def __init__(self, title, due_date):
self.title = title
self.due_date = due_date

def __lt__(self, other):
return self.due_date < other.due_date
```

现在，我可以使用 `heapq.heappush` 函数无问题地将书籍添加到优先队列：

[点击此处查看代码图像](#ch12_images#f0515-02)

```python
queue = []
add_book(queue, Book("Pride and Prejudice", "2019-06-01"))
add_book(queue, Book("The Time Machine", "2019-05-30"))
add_book(queue, Book("Crime and Punishment", "2019-06-06"))
add_book(queue, Book("Wuthering Heights", "2019-06-12"))
```

或者，我可以创建一个包含所有书籍的列表，以任何顺序排列，然后使用 `list` 的 `sort` 方法来生成堆：

[点击此处查看代码图像](#ch12_images#f0515-03)

```python
queue = [
Book("Pride and Prejudice", "2019-06-01"),
Book("The Time Machine", "2019-05-30"),
Book("Crime and Punishment", "2019-06-06"),
Book("Wuthering Heights", "2019-06-12"),
]
queue.sort()
```

或者，我可以使用 `heapq.heapify` 函数以线性时间（与 `sort` 方法的 `len(queue) * log(len(queue))` 复杂度相对）创建堆：

[点击此处查看代码图像](#ch12_images#f0515-04)

```python
from heapq import heapify

queue = [
Book("Pride and Prejudice", "2019-06-01"),
Book("The Time Machine", "2019-05-30"),
Book("Crime and Punishment", "2019-06-06"),
Book("Wuthering Heights", "2019-06-12"),
]
heapify(queue)
```

要检查逾期书籍，我检查列表中的第一个元素而不是最后一个元素，然后使用 `heapq.heappop` 函数而不是 `list.pop` 函数从堆中移除书籍：

[点击此处查看代码图像](#ch12_images#f0516-01)

```python
from heapq import heappop

def next_overdue_book(queue, now):
if queue:
book = queue[0]     # 最逾期的先处理
if book.due_date < now:
heappop(queue)  # 移除逾期书籍
return book

raise NoOverdueBooks
```

现在我可以按顺序查找和移除逾期书籍，直到当前时间没有剩余的：

[点击此处查看代码图像](#ch12_images#f0516-02)

```python
now = "2019-06-02"

book = next_overdue_book(queue, now)
print(book.due_date, book.title)

book = next_overdue_book(queue, now)
print(book.due_date, book.title)

try:
next_overdue_book(queue, now)
except NoOverdueBooks:
pass          # 预期
else:
assert False  # 不会发生

>>>
2019-05-30 The Time Machine
2019-06-01 Pride and Prejudice
```

我还可以编写另一个微基准测试来测试此实现（使用 `heapq` 模块）的性能：

[点击此处查看代码图像](#ch12_images#f0516-03)

```python
def heap_overdue_benchmark(count):
def prepare():
to_add = list(range(count))
random.shuffle(to_add)
return [], to_add

def run(queue, to_add):
for i in to_add:
heappush(queue, i)
while queue:
heappop(queue)

return timeit.timeit(
setup="queue, to_add = prepare()",
stmt="run(queue, to_add)",
globals=locals(),
number=1,
)
```

此基准测试实验性地验证了基于堆的优先队列实现的可扩展性要好得多（大约 `len(queue) * math.log(len(queue))`），而不会出现超线性性能下降：

[点击此处查看代码图像](#ch12_images#f0517-02)

```python
for i in range(1, 6):
count = i * 10_000
delay = heap_overdue_benchmark(count)
print(f"Count {count:>5,} takes: {delay*1e3:>6.2f}ms")

>>>
Count 10,000 takes:   1.73ms
Count 20,000 takes:   3.83ms
Count 30,000 takes:   6.50ms
Count 40,000 takes:   8.85ms
Count 50,000 takes:  11.43ms
```

使用 `heapq` 实现，还有一个问题需要解决：我应该如何处理按时归还的书籍？解决方案是直到书籍到期日期才从优先队列中移除该书。届时，它将是列表中的第一个项，如果该书已被归还，我只需忽略它即可。我在此通过向 `Book` 类添加一个新字段来跟踪书籍的返回状态来实现此行为：

[点击此处查看代码图像](#ch12_images#f0517-03)

```python
@functools.total_ordering
class Book:
def __init__(self, title, due_date):
self.title = title
self.due_date = due_date
self.returned = False  # 新字段

...
```

然后，我更改 `next_overdue_book` 函数以重复忽略已退还的任何书籍：

[点击此处查看代码图像](#ch12_images#f0518-01)

```python
def next_overdue_book(queue, now):
while queue:
book = queue[0]
if book.returned:
heappop(queue)
continue

if book.due_date < now:
heappop(queue)
return book

break

raise NoOverdueBooks
```

此方法使 `return_book` 函数非常快速，因为它不对优先队列进行任何修改：

```python
def return_book(queue, book):
book.returned = True
```

此解决方案对于退货的缺点是，优先队列可能会增长到所需的最大大小，如果图书馆的所有书籍都被借出并已逾期。尽管由于 `heapq` 的原因，队列操作会很快，但这种存储开销可能需要大量内存（请参阅 [Item 115](#ch13#ch13lev1sec8)：“[使用 `tracemalloc` 理解内存使用和泄漏](#ch13#ch13lev1sec8)” 获取如何调试此类使用）：

如果您的目标是构建一个健壮的系统，您将需要为最坏情况进行计划；因此，您应该期望每本图书馆的书籍都可能因某种原因逾期（例如，自然灾害导致图书馆的道路关闭）。这种内存成本是您应该已经计划并已通过其他约束（例如，施加同时借阅书籍的最大数量）来缓解的设计考虑因素。

除了我在示例中使用的优先队列原语之外，`heapq` 模块还为高级用例提供了其他功能（请参阅 <https://docs.python.org/3/library/heapq.html>）。当其功能与您面临的问题匹配时，该模块是一个绝佳的选择（请参阅 `queue.PriorityQueue` 类以获取另一个线程安全的选项）。

#### 记住要点

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 优先队列允许您按重要性顺序处理项，而不是按先进先出顺序处理。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果您尝试使用 `list` 操作来实现优先队列，您的程序的性能将随着队列的增长而呈超线性下降。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `heapq` 内置模块提供了实现可有效扩展的优先队列所需的所有函数。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 要使用 `heapq`，被优先排序的项必须具有自然排序顺序，这需要为类定义特殊方法，如 `__lt__`。

### Item 105: 使用 `datetime` 而不是 `time` 来处理本地时钟

协调世界时（UTC）是时间的标准、与时区无关的表示。UTC 对于将时间表示为自 UNIX epoch 以来的秒数的计算机来说非常有用。但 UTC 对人类来说并不理想。人类根据他们当前的位置参考时间。人们说“中午”或“早上 8 点”，而不是“UTC 15:00 减去 7 小时”。如果您的程序处理时间，您可能会发现自己需要在 UTC 和本地时钟之间转换时间，以方便人类理解。

Python 提供了两种实现时区转换的方法。旧方法是使用 `time` 内置模块，它非常容易出错。新方法是使用 `datetime`，在内置 `zoneinfo` 模块的帮助下效果很好。

您应该熟悉 `time` 和 `datetime`，以便彻底了解为什么 `datetime` 是最佳选择而应避免使用 `time`。

#### `time` 模块

`time` 内置模块中的 `localtime` 函数允许您将 UNIX 时间戳（自 UTC UNIX epoch 以来的秒数）转换为与主机计算机的时区（在我看来是太平洋夏令时）匹配的本地时间。可以使用 `strftime` 函数以人类可读的格式打印此本地时间：

[点击此处查看代码图像](#ch12_images#f0519-01)

```python
import time

now = 1710047865.0
local_tuple = time.localtime(now)
time_format = "%Y-%m-%d %H:%M:%S"
time_str = time.strftime(time_format, local_tuple)
print(time_str)

>>>
2024-03-09 21:17:45
```

您通常也需要反向操作，从人类可读的本地时间用户输入开始，并将其转换为 UTC 时间。您可以通过使用 `strptime` 函数解析时间字符串，然后调用 `mktime` 将本地时间转换为 UNIX 时间戳来完成此操作：

[点击此处查看代码图像](#ch12_images#f0520-02)

```python
time_tuple = time.strptime(time_str, time_format)
utc_now = time.mktime(time_tuple)
print(utc_now)

>>>
1710047865.0
```

如何将一个时区中的本地时间转换为另一个时区中的本地时间？例如，假设我乘坐从旧金山到纽约的航班，我想知道当我抵达纽约时，旧金山的时间是什么。

我可能最初会认为我可以直接操作 `time`、`localtime` 和 `strptime` 函数的返回值来执行时区转换。但这非常糟糕。由于当地法律，时区会不断变化。自己管理它太复杂了，特别是如果您想处理所有全球城市以便航班起降。

许多操作系统都有配置文件，可以自动跟踪时区更改。如果您的平台支持，Python 允许您通过 `time` 模块使用这些时区。在其他平台（如 Windows）上，`time` 根本无法提供某些时区功能。例如，我在此解析旧金山时区太平洋标准时间（PST）的出发时间：

[点击此处查看代码图像](#ch12_images#f0520-03)

```python
parse_format = "%Y-%m-%d %H:%M:%S %Z"
depart_sfo = "2024-03-09 21:17:45 PST"
time_tuple = time.strptime(depart_sfo, parse_format)
time_str = time.strftime(time_format, time_tuple)
print(time_str)

>>>
2024-03-09 21:17:45
```

在看到 `"PST"` 可以与 `strptime` 函数一起使用后，我也可能假设我的计算机已知的其他时区也会起作用。不幸的是，事实并非如此。当 `strptime` 遇到东部夏令时（EDT）时，它会引发异常，这是纽约的时区（当航班在时间更改后抵达时）：

[点击此处查看代码图像](#ch12_images#f0521-01)

```python
arrival_nyc = "2024-03-10 03:31:18 EDT"
time_tuple = time.strptime(arrival_nyc, parse_format)

>>>
Traceback ...
ValueError: time data '2024-03-10 03:31:18 EDT' does not match
➥format '%Y-%m-%d %H:%M:%S %Z'
```

这里的问题在于 `time` 模块的平台依赖性。其实际行为取决于底层 C 函数如何与主机操作系统配合工作。这使得 `time` 模块的功能在 Python 中不可靠。`time` 模块无法一致地正确处理多个本地时间。因此，您应该避免为此目的使用 `time` 模块。如果您必须使用 `time`，请仅将其用于在 UTC 和主机计算机的本地时间之间进行转换。对于所有其他类型的转换，请使用 `datetime` 模块。

#### `datetime` 模块

在 Python 中表示时间的第二个选项是 `datetime` 内置模块中的 `datetime` 类。与 `time` 模块一样，`datetime` 可用于从当前的 UTC 时间转换为本地时间。

我在此将当前 UTC 时间转换为我计算机的本地时间 PDT：

[点击此处查看代码图像](#ch12_images#f0521-02)

```python
from datetime import datetime, timezone

now = datetime(2024, 3, 10, 5, 17, 45)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print(now_local)

>>>
2024-03-09 21:17:45-08:00
```

`datetime` 模块还可以轻松地将本地时间转换回 UTC 中的 UNIX 时间戳（与上面的值匹配）：

[点击此处查看代码图像](#ch12_images#f0521-03)

```python
time_str = "2024-03-09 21:17:45"
now = datetime.strptime(time_str, time_format)
time_tuple = now.timetuple()
utc_now = time.mktime(time_tuple)
print(utc_now)

>>>
1710047865.0
```

与 `time` 模块不同，`datetime` 模块提供了可靠地从一个本地时间转换为另一个本地时间的功能。但是，`datetime` 仅通过其 `tzinfo` 类和相关方法提供时区操作的机制。

幸运的是，自 Python 3.9 版本以来，在许多系统上，`zoneinfo` 内置模块包含一个完整的数据库，其中包含您可能需要的每个时区定义。在其他系统（如 Windows）上，可能需要安装官方推荐的 `tzdata` 社区包，以提供 `zoneinfo` 模块正常运行所需时区数据库（请参阅 [Item 116](#ch14#ch14lev1sec1)：“[了解社区构建的模块在哪里](#ch14#ch14lev1sec1)” 获取详细信息）。

要有效使用 `zoneinfo`，您应始终先将本地时间转换为 UTC。接下来，在 UTC 值上执行任何所需的 `datetime` 操作（例如偏移）。最后，转换为本地时间。

例如，我在此将纽约市的航班抵达时间转换为 UTC `datetime`：

[点击此处查看代码图像](#ch12_images#f0522-01)

```python
from zoneinfo import ZoneInfo

arrival_nyc = "2024-03-10 03:31:18"
nyc_dt_naive = datetime.strptime(arrival_nyc, time_format)
eastern = ZoneInfo("US/Eastern")
nyc_dt = nyc_dt_naive.replace(tzinfo=eastern)
utc_dt = nyc_dt.astimezone(timezone.utc)
print("EDT:", nyc_dt)
print("UTC:", utc_dt)

>>>
EDT: 2024-03-10 03:31:18-04:00
UTC: 2024-03-10 07:31:18+00:00
```

一旦我有了 UTC `datetime`，我就可以将其转换为旧金山的本地时间：

[点击此处查看代码图像](#ch12_images#f0522-02)

```python
pacific = ZoneInfo("US/Pacific")
sf_dt = utc_dt.astimezone(pacific)
print("PST:", sf_dt)

>>>
PST: 2024-03-09 23:31:18-08:00
```

同样，我可以轻松地将其转换为尼泊尔的本地时间：

[点击此处查看代码图像](#ch12_images#f0522-03)

```python
nepal = ZoneInfo("Asia/Katmandu")
nepal_dt = utc_dt.astimezone(nepal)
print("NPT", nepal_dt)

>>>
NPT 2024-03-10 13:16:18+05:45
```

使用 `datetime` 和 `zoneinfo`，这些转换在所有环境中都是一致的，无论主机计算机运行的是什么操作系统。

#### 记住要点

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 避免使用 `time` 模块在不同时区之间进行翻译。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `datetime` 和 `zoneinfo` 内置模块可靠地在不同时区的时间和日期之间进行转换。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 始终以 UTC 表示时间，并在呈现之前将转换到本地时间作为最后一步。

### Item 106: 在精度至关重要时使用 `decimal`

Python 是编写与数值数据交互代码的绝佳语言。Python 的整数类型可以表示任何实际大小的值。其双精度浮点类型符合 IEEE 754 标准。该语言还为虚数值提供了标准复数类型。但是，这些对于所有情况来说都还不够。

例如，假设我想计算通过便携式卫星电话向客户收取国际长途电话费的金额。我知道客户在电话上的时间（分钟和秒）（例如，3 分钟 42 秒）。我还知道从美国拨打南极洲的费率（例如，1.45 美元/分钟）。费用应该是多少？

使用浮点数数学，计算出的费用似乎是合理的：

```python
rate = 1.45
seconds = 3 * 60 + 42
cost = rate * seconds / 60
print(cost)

>>>
5.364999999999999
```

由于 IEEE 754 浮点数的表示方式，结果比正确值（5.365）短 0.0001。我可能希望将此值四舍五入到 5.37，以正确覆盖客户产生的所有费用。但是，由于浮点误差，四舍五入到最近的整数美分实际上会减少最终费用（从 5.364 到 5.36），而不是增加它（从 5.365 到 5.37）：

```python
print(round(cost, 2))

>>>
5.36
```

解决方案是使用 `decimal` 内置模块中的 `Decimal` 类。`Decimal` 类默认提供 28 位小数的定点数学——如果需要，还可以更高。这可以解决 IEEE 754 浮点数的精度问题。该类还为您提供了对舍入行为的更多控制。

例如，使用 `Decimal` 重做南极洲的计算，结果是预期的确切费用，而不是近似值：

```python
from decimal import Decimal

rate = Decimal("1.45")
seconds = Decimal(3 * 60 + 42)
cost = rate * seconds / Decimal(60)
print(cost)

>>>
5.365
```

`Decimal` 实例可以通过两种不同的方式提供初始值。第一种方法是通过将包含数字的 `str` 传递给 `Decimal` 构造函数。这确保了由于 Python 浮点值和数字常量的固有性质而不会丢失精度。第二种方法是通过直接将 `float` 或 `int` 实例传递给构造函数。您可以在此处看到这两种构造方法会导致不同的行为：

[点击此处查看代码图像](#ch12_images#f0524-02)

```python
print(Decimal("1.45"))
print(Decimal(1.45))

>>>
1.45
1.4499999999999999555910790149937383830547332763671875
```

如果我将整数提供给 `Decimal` 构造函数，则不会出现此问题：

```python
print("456")
print(456)

>>>
456
456
```

如果您关心精确答案，请谨慎行事，并始终为 `Decimal` 类型使用 `str` 构造函数。

回到电话通话示例，假设我还想支持非常短的电话，例如托莱多和底特律之间的电话，这些电话通过辅助蜂窝连接连接要便宜得多。我在此计算一个 5 秒长的电话费用，费率为 0.05 美元/分钟：

[点击此处查看代码图像](#ch12_images#f0525-01)

```python
rate = Decimal("0.05")
seconds = Decimal("5")
small_cost = rate * seconds / Decimal(60)
print(small_cost)

>>>
0.004166666666666666666666666667
```

结果如此之低，以至于当我尝试将其四舍五入到最近的整数美分时，它被减少到零。这不行！

```python
print(round(small_cost, 2))

>>>
0.00
```

幸运的是，`Decimal` 类有一个内置函数，可以以所需的舍入行为精确地舍入到所需的十进制位数。这适用于之前的较高成本情况：

[点击此处查看代码图像](#ch12_images#f0525-02)

```python
from decimal import ROUND_UP

rounded = cost.quantize(Decimal("0.01"), rounding=ROUND_UP)
print(f"Rounded {cost} to {rounded}")

>>>
Rounded 5.365 to 5.37
```

以这种方式使用 `quantize` 方法也能正确处理短时间、低成本电话的少量使用情况：

[点击此处查看代码图像](#ch12_images#f0525-03)

```python
rounded = small_cost.quantize(Decimal("0.01"), rounding=ROUND_UP)
print(f"Rounded {small_cost} to {rounded}")

>>>
Rounded 0.004166666666666666666666666667 to 0.01
```

虽然 `Decimal` 对于定点数效果很好，但它在精度方面仍然存在局限性（例如，`1/3` 将是一个近似值）。要表示没有精度限制的有理数，请考虑使用 `fractions` 内置模块中的 `Fraction` 类。

#### 记住要点

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 在模块中拥有内置类型和类，可以表示几乎所有类型的数值。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `Decimal` 类非常适合需要高精度和对舍入行为进行控制的情况，例如货币值的计算。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果计算精确答案而不是浮点近似值很重要，请将 `str` 实例传递给 `Decimal` 构造函数，而不是 `float` 实例。

### Item 107: 使用 `copyreg` 使 `pickle` 序列化可维护

`pickle` 内置模块可以将 Python 对象序列化为字节流，并将字节反序列化回对象（请参阅 [Item 10](#ch02#ch02lev1sec1)：“[了解 `bytes` 和 `str` 之间的区别](#ch02#ch02lev1sec1)” 获取背景信息）。Pickled 字节流不应用于不受信任的方之间进行通信。`pickle` 的目的是让您能够通过二进制通道在您控制的程序之间传递 Python 对象。

**注意**
`pickle` 模块的序列化格式在设计上是不安全的。序列化数据包含本质上是描述如何重建原始 Python 对象的程序。这意味着恶意的 `pickle` 有效负载可用于破坏尝试反序列化它的任何 Python 程序部分。

相比之下，`json` 模块在设计上是安全的。序列化 JSON 数据包含对象层次结构的简单描述。反序列化 JSON 数据不会使 Python 程序面临除内存不足错误之外的任何额外风险。JSON 等格式应用于不信任彼此的程序或人员之间的通信。

例如，假设我想使用 Python 对象来表示游戏中玩家进度的状态。游戏状态包括玩家所在的关卡和剩余的生命数：

```python
class GameState:
def __init__(self):
self.level = 0
self.lives = 4
```

程序在游戏运行时修改此对象：

[点击此处查看代码图像](#ch12_images#f0526-01)

```python
state = GameState()
state.level += 1  # 玩家通过了一个关卡
state.lives -= 1  # 玩家不得不再次尝试

print(state.__dict__)

>>>
{'level': 1, 'lives': 3}
```

当用户退出游戏时，程序可以将游戏状态保存到文件中，以便以后可以恢复。`pickle` 模块可以轻松完成此操作。我在此将 `GameState` 对象直接 `dump` 到文件中：

[点击此处查看代码图像](#ch12_images#f0527-02)

```python
import pickle

state_path = "game_state.bin"
with open(state_path, "wb") as f:
pickle.dump(state, f)
```

稍后，我可以加载文件并获取 `GameState` 对象，就好像它从未被序列化过一样：

[点击此处查看代码图像](#ch12_images#f0527-03)

```python
with open(state_path, "rb") as f:
state_after = pickle.load(f)

print(state_after.__dict__)

>>>
{'level': 1, 'lives': 3}
```

此方法的问题在于，随着游戏功能的扩展，会发生什么。想象一下我想让玩家获得分数以获得高分。为了跟踪玩家的分数，我可以在 `GameState` 类中添加一个新字段：

[点击此处查看代码图像](#ch12_images#f0527-04)

```python
class GameState:
def __init__(self):
self.level = 0
self.lives = 4
self.points = 0  # 新字段
```

使用 `pickle` 序列化新版本的 `GameState` 类将像以前一样工作。我在此通过使用 `dumps` 将其序列化为字符串，然后使用 `loads` 将其反序列化回 `GameState` 对象来模拟文件往返：

[点击此处查看代码图像](#ch12_images#f0527-05)

```python
state = GameState()
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)

print(state_after.__dict__)

>>>
{'level': 0, 'lives': 4, 'points': 0}
```

但是，用户可能想要恢复的旧 `GameState` 对象会怎样？我在此使用新 `GameState` 类定义的程序来反序列化旧游戏文件：

[点击此处查看代码图像](#ch12_images#f0528-01)

```python
with open(state_path, "rb") as f:
state_after = pickle.load(f)

print(state_after.__dict__)

>>>
{'level': 1, 'lives': 3}
```

`points` 属性丢失了！这尤其令人困惑，因为返回的对象是新 `GameState` 类的实例：

[点击此处查看代码图像](#ch12_images#f0528-02)

```python
assert isinstance(state_after, GameState)
```

这种行为是 `pickle` 模块工作方式的副产品。其主要用例是方便地序列化对象。一旦您对 `pickle` 的使用超出了简单的用法，该模块的功能就会以令人惊讶的方式开始崩溃。

修复这些问题使用 `copyreg` 内置模块非常简单。`copyreg` 模块允许您注册负责序列化和反序列化 Python 对象的函数，从而使您能够控制 `pickle` 的行为并使其更可靠和适应性更强。

#### 默认属性值

在最简单的情况下，您可以使用带有默认参数的构造函数（请参阅 [Item 35](#ch05#ch05lev1sec6)：“[使用关键字参数提供可选行为](#ch05#ch05lev1sec6)” 获取背景信息）来确保 `GameState` 对象在反序列化后始终具有所有属性。我在此这样重新定义了构造函数：

[点击此处查看代码图像](#ch12_images#f0528-03)

```python
class GameState:
def __init__(self, level=0, lives=4, points=0):
self.level = level
self.lives = lives
self.points = points
```

要将此构造函数用于 pickling，我定义了一个辅助函数，该函数接受一个 `GameState` 对象并将其转换为 `copyreg` 模块的参数元组。返回的元组包含用于反序列化的函数以及要传递给反序列化函数的参数：

[点击此处查看代码图像](#ch12_images#f0528-04)

```python
def pickle_game_state(game_state):
kwargs = game_state.__dict__
return unpickle_game_state, (kwargs,)
```

现在我需要定义 `unpickle_game_state` 辅助函数。此函数从 `pickle_game_state` 接收序列化数据和参数，并返回相应的 `GameState` 对象。它是构造函数的微小包装器：

[点击此处查看代码图像](#ch12_images#f0529-01)

```python
def unpickle_game_state(kwargs):
return GameState(**kwargs)
```

现在我将这些函数注册到 `copyreg` 内置模块：

[点击此处查看代码图像](#ch12_images#f0529-05)

```python
import copyreg

copyreg.pickle(GameState, pickle_game_state)
```

注册后，序列化和反序列化像以前一样工作：

[点击此处查看代码图像](#ch12_images#f0529-02)

```python
state = GameState()
state.points += 1000
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)

>>>
{'level': 0, 'lives': 4, 'points': 1000}
```

进行此注册后，我现在将再次更改 `GameState` 的定义，为玩家提供要使用的魔法数量。此更改类似于我将 `points` 字段添加到 `GameState` 时：

[点击此处查看代码图像](#ch12_images#f0529-03)

```python
class GameState:
def __init__(self, level=0, lives=4, points=0, magic=5):
self.level = level
self.lives = lives
self.points = points
self.magic = magic  # 新字段
```

但与之前不同的是，反序列化旧 `GameState` 对象将产生有效游戏数据，而不是丢失的属性。这是因为 `unpickle_game_state` 直接调用 `GameState` 构造函数，而不是使用 `pickle` 模块仅保存和恢复对象属性的默认行为。`GameState` 构造函数的关键字参数具有默认值，这些默认值将用于任何缺失的参数。当反序列化旧游戏状态文件时，这会导致它们为新的 `magic` 字段接收默认值：

[点击此处查看代码图像](#ch12_images#f0529-04)

```python
print("Before:", state.__dict__)
state_after = pickle.loads(serialized)
print("After: ", state_after.__dict__)

>>>
Before: {'level': 0, 'lives': 4, 'points': 1000}
After:  {'level': 0, 'lives': 4, 'points': 1000, 'magic': 5}
```

#### 版本化类

有时您需要通过删除字段来对 Python 对象进行不兼容的更改。这样做会阻止默认参数方法迁移序列化。

例如，假设我发现有限的生命数是个坏主意，我想从游戏中移除生命的概念。我在此重新定义 `GameState` 类，使其不再具有生命字段：

[点击此处查看代码图像](#ch12_images#f0530-02)

```python
class GameState:
def __init__(self, level=0, points=0, magic=5):
self.level = level
self.points = points
self.magic = magic
```

问题在于这会破坏旧游戏数据的反序列化。来自旧数据的所有字段——即使是类中已删除的字段——都将由 `unpickle_game_state` 函数传递给 `GameState` 构造函数：

[点击此处查看代码图像](#ch12_images#f0530-03)

```python
pickle.loads(serialized)

>>>
Traceback ...
TypeError: GameState.__init__() got an unexpected keyword
➥argument 'lives'. Did you mean 'level'?
```

我可以通过向提供给 `copyreg` 的函数添加版本参数来解决此问题。当 pickling 新的 `GameState` 对象时，旧版本的数据将指定版本 `2`：

[点击此处查看代码图像](#ch12_images#f0530-04)

```python
def pickle_game_state(game_state):
kwargs = game_state.__dict__
kwargs["version"] = 2
return unpickle_game_state, (kwargs,)
```

旧版本的数据将不存在 `version` 参数，这意味着我可以相应地操作传递给 `GameState` 构造函数的参数：

[点击此处查看代码图像](#ch12_images#f0530-05)

```python
def unpickle_game_state(kwargs):
version = kwargs.pop("version", 1)
if version == 1:
del kwargs["lives"]
return GameState(**kwargs)
```

现在反序列化旧对象可以正常工作：

[点击此处查看代码图像](#ch12_images#f0531-01)

```python
copyreg.pickle(GameState, pickle_game_state)
print("Before:", state.__dict__)
state_after = pickle.loads(serialized)
print("After: ", state_after.__dict__)

>>>
Before: {'level': 0, 'lives': 4, 'points': 1000}
After:  {'level': 0, 'points': 1000, 'magic': 5}
```

我可以通过继续使用此方法来处理同一类未来版本之间的更改。我需要将旧类版本适配到新类版本的任何逻辑都可以放在 `unpickle_game_state` 函数中。

#### 稳定的导入路径

您在使用 `pickle` 时可能遇到的另一个问题是由于重命名类而导致的损坏。通常在程序的生命周期中，您会通过重命名类并将其移动到其他模块来重构代码。不幸的是，这样做会破坏 `pickle` 模块，除非您小心。

我在此将 `GameState` 类重命名为 `BetterGameState`，并完全从程序中删除旧类：

[点击此处查看代码图像](#ch12_images#f0531-02)

```python
class BetterGameState:
def __init__(self, level=0, points=0, magic=5):
self.level = level
self.points = points
self.magic = magic
```

尝试反序列化旧 `GameState` 对象现在会失败，因为找不到该类：

[点击此处查看代码图像](#ch12_images#f0531-03)

```python
pickle.loads(serialized)

>>>
Traceback ...
AttributeError: Can't get attribute 'GameState'
➥on <module '__main__' from 'my_code.py'>
```

发生此异常是因为序列化对象的类的导入路径已编码在 pickled 数据中：

[点击此处查看代码图像](#ch12_images#f0531-04)

```python
print(serialized)

>>>
b'\x80\x04\x95A\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\
x94\x8c\tGameState\x94\x93\x94)\x81\x94}\x94(\x8c\x05level\
x94K\x00\x8c\x06points\x94K\x00\x8c\x05magic\x94K\x05ub.'
```

解决方案是再次使用 `copyreg`。我可以为用于反序列化对象的函数指定一个稳定的标识符。这允许我在反序列化时将 pickled 数据转换为不同的类，这些类具有不同的名称。它为我提供了一个间接级别：

[点击此处查看代码图像](#ch12_images#f0532-02)

```python
copyreg.pickle(BetterGameState, pickle_game_state)
```

在使用 `copyreg` 后，很明显 `unpickle_game_state` 的导入路径已编码在序列化数据中，而不是 `BetterGameState`：

[点击此处查看代码图像](#ch12_images#f0532-01)

```python
state = BetterGameState()
serialized = pickle.dumps(state)
print(serialized)

>>>
b'\x80\x04\x95W\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\
➥x94\x8c\x13unpickle_game_state\x94\x93\x94}\x94(\x8c\
➥x05level\x94K\x00\x8c\x06points\x94K\x00\x8c\x05magic\x94K\
➥x05\x8c\x07version\x94K\x02u\x85\x94R\x94.'
```

唯一的注意事项是，我不能更改 `unpickle_game_state` 函数所在的模块的路径。一旦我使用函数序列化数据，它在未来反序列化时必须保持在相同的导入路径上可用。

#### 记住要点

*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `pickle` 内置模块仅在序列化和反序列化受信任程序之间的对象时有用。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果涉及的类随时间发生变化（例如，添加或删除了属性），反序列化先前 pickled 对象可能会失败。
*   ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `copyreg` 内置模块与 `pickle` 一起使用，以确保序列化对象的向后兼容性。
---
<a role="toc_link" id="ch13"></a>

## Effective Python - 13

## 13

本章深入探讨了 Graph Neural Networks (GNNs) 的前沿进展，特别是 Graph Foundation Models (GFMs) 的兴起及其在各种图学习任务中的强大能力。我们将重点关注 GNNs 的核心机制，包括 Message Passing 和 Node Embedding 的生成，以及它们如何通过 Self-supervised Learning 和 Pre-training 等技术实现高效学习。

本章将详细介绍几种关键的 GNNs 架构，如 Graph Convolutional Networks (GCN) 和 Graph Attention Networks (GAT)，并阐述 GraphSAGE 等方法如何在动态和大规模图上进行有效的节点表示学习。我们将探讨如何利用这些模型进行 Graph Classification、Node Classification 和 Link Prediction 等下游任务。

此外，本章还将涵盖 GNNs 在处理 Heterogeneous Graph 和 Homogeneous Graph 时的挑战与解决方案，以及如何通过 Graph Pooling 等技术来聚合图结构信息。对于需要处理复杂关系数据的场景，我们将讨论 Knowledge Graph 的表示学习及其应用。

本章的另一重要主题是 GNNs 的迁移学习能力，包括 Fine-tuning、In-context Learning、Few-shot Learning 和 Zero-shot Learning。我们将探讨如何利用 Pre-training 的 GNNs 模型实现 Cross-domain Transfer 和 Domain Adaptation，从而在数据稀疏或领域差异较大的情况下依然取得优异性能。

最后，本章还将触及 GNNs 在 Graph Generation、Graph Anomaly Detection 和 Contrastive Learning 等新兴领域的应用，以及 Multi-modal Learning 与 GNNs 的结合，为读者提供一个全面而深入的 GNNs 技术图景。

## Effective Python - Testing and Debugging

## 测试与调试

Python 的动态特性及其默认情况下缺乏静态类型检查，既是福音也是诅咒（详见 [Item 3](#ch01#ch01lev1sec3)：“[永远不要期望 Python 在编译时检测到错误](#ch01#ch01lev1sec3)”）。然而，许多 Python 程序员认为，由此带来的简洁性和易用性带来的生产力提升是值得的。但大多数使用 Python 的人至少都有一次关于程序在运行时遇到愚蠢错误的恐怖经历。我听说过的最糟糕的例子之一是，在生产环境中，由于动态导入的副作用而引发了 `SyntaxError` 异常（详见 [Item 98](#ch11#ch11lev1sec7)：“[使用动态导入延迟加载模块以减少启动时间](#ch11#ch11lev1sec7)” 中的示例），导致服务器进程崩溃。我认识的程序员曾遭遇过这种令人惊讶的情况，此后他决定再也不使用 Python 了。

但我不得不怀疑：为什么在程序部署到生产环境之前，代码没有经过更充分的测试？编译时静态类型安全并非万能。无论你的代码是用什么语言编写的，都应该始终测试你的代码。然而，我承认，在 Python 中，编写测试来验证正确性可能比在其他语言中更重要。幸运的是，造成这些风险的动态特性也使得编写代码测试和调试故障程序变得异常容易。你可以利用 Python 的动态特性和易于重写的行为来实现测试，并确保你的程序按预期工作。

### Item 108: 在 `TestCase` 子类中验证相关行为

在 Python 中编写测试的典型方法是使用 `unittest` 内置模块。例如，假设我有一个如下定义的实用函数，我想验证它在各种输入下都能正常工作：
[点击此处查看代码图像](#ch13_images#f0534-01)
```
# utils.py
def to_str(data):
if isinstance(data, str):
return data
elif isinstance(data, bytes):
return data.decode("utf-8")
else:
raise TypeError(
f"Must supply str or bytes, found: {data}")
```
要定义测试，我创建一个名为 `test_utils.py` 或 `utils_test.py` 的第二个文件——命名方案是风格选择——其中包含对每个预期行为的测试：
[点击此处查看代码图像](#ch13_images#f0534-02)
```
# utils_test.py
from unittest import TestCase, main
from utils import to_str

class UtilsTestCase(TestCase):
def test_to_str_bytes(self):
self.assertEqual("hello", to_str(b"hello"))

def test_to_str_str(self):
self.assertEqual("hello", to_str("hello"))

def test_failing(self):
self.assertEqual("incorrect", to_str("hello"))

if __name__ == "__main__":
main()
```
然后我使用 Python 命令行运行测试文件。在这种情况下，两个测试方法通过，一个失败，并打印出关于出了什么问题的有用错误消息：
[点击此处查看代码图像](#ch13_images#f0534-03)
```
$ python3 utils_test.py
F..
===============================================================
FAIL: test_failing (__main__.UtilsTestCase)
---------------------------------------------------------------
Traceback (most recent call last):
File "utils_test.py", line 15, in test_failing
self.assertEqual('incorrect', to_str('hello'))
AssertionError: 'incorrect' != 'hello'

- incorrect
+ hello

---------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (failures=1)
```
测试被组织到 `TestCase` 子类中。每个测试用例是一个以 `test` 开头的方法。如果一个测试方法在没有引发任何异常（包括 `assert` 语句中的 `AssertionError`；详见 [Item 81](#ch10#ch10lev1sec2)：“[断言内部假设并抛出未满足的期望](#ch10#ch10lev1sec2)”）的情况下运行，则该测试被认为已成功通过。如果一个测试失败，`TestCase` 子类会继续运行其他测试方法，以便你能够全面了解所有测试的执行情况，而不是在遇到第一个问题时就停止。
如果你想快速迭代以修复或改进特定测试，可以通过在命令行中指定测试模块内的路径来仅运行该测试方法：
[点击此处查看代码图像](#ch13_images#f0535-02)
```
$ python3 utils_test.py UtilsTestCase.test_to_str_bytes
.
---------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
你还可以直接在测试方法中使用调试器，在特定的断点处深入了解失败的原因（详见 [Item 114](#ch13#ch13lev1sec7)：“[考虑使用 pdb 进行交互式调试](#ch13#ch13lev1sec7)” 以了解如何操作）。
`TestCase` 类提供了用于在测试中进行断言的辅助方法，例如 `assertEqual` 用于验证相等性，`assertTrue` 用于验证布尔表达式，`assertAlmostEqual` 用于精度问题（详见 [Item 113](#ch13#ch13lev1sec6)：“[使用 assertAlmostEqual 控制浮点数测试中的精度](#ch13#ch13lev1sec6)”），以及更多（详见 <https://docs.python.org/3/library/unittest.html> 获取完整列表）。这些方法优于内置的 `assert` 语句，因为它们会打印出所有输入和输出，帮助你确切地了解测试失败的原因。例如，这里我用和不使用辅助断言方法编写了相同的测试用例：
[点击此处查看代码图像](#ch13_images#f0535-03)
```
# assert_test.py
from unittest import TestCase, main
from utils import to_str

class AssertTestCase(TestCase):
def test_assert_helper(self):
expected = 12
found = 2 * 5
self.assertEqual(expected, found)

def test_assert_statement(self):
expected = 12
found = 2 * 5
assert expected == found

if __name__ == "__main__":
main()
```
你觉得哪个失败消息更有帮助？请注意第二个消息没有显示 `expected` 或 `found` 的值：
[点击此处查看代码图像](#ch13_images#f0536-02)
```
$ python3 assert_test.py
FF
===============================================================
FAIL: test_assert_helper (__main__.AssertTestCase)
---------------------------------------------------------------
Traceback (most recent call last):
File "assert_test.py", line 16, in test_assert_helper
self.assertEqual(expected, found)
AssertionError: 12 != 10

===============================================================
FAIL: test_assert_statement (__main__.AssertTestCase)
---------------------------------------------------------------
Traceback (most recent call last):
File "assert_test.py", line 11, in test_assert_statement
assert expected == found
AssertionError

---------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=2)
```
还有一个 `assertRaises` 辅助方法用于验证异常，它可以作为上下文管理器在 `with` 语句中使用（详见 [Item 82](#ch10#ch10lev1sec3)：“[考虑使用 contextlib 和 with 语句实现可重用的 try/finally 行为](#ch10#ch10lev1sec3)” 以了解其工作原理）。这看起来类似于 `try`/`except` 语句，并清楚地表明了异常的预期抛出位置：
[点击此处查看代码图像](#ch13_images#f0537-01)
```
# utils_error_test.py
from unittest import TestCase, main
from utils import to_str

class UtilsErrorTestCase(TestCase):
def test_to_str_bad(self):
with self.assertRaises(TypeError):
to_str(object())

def test_to_str_bad_encoding(self):
with self.assertRaises(UnicodeDecodeError):
to_str(b"\xfa\xfa")

if __name__ == "__main__":
main()
```
你还可以定义自己的辅助方法，在 `TestCase` 子类中包含复杂的逻辑，以使你的测试更具可读性。只需确保你的方法名称不以 `test` 开头，否则它们将被当作测试用例运行。除了调用 `TestCase` 的断言方法外，这些自定义测试辅助方法通常使用 `fail` 方法来阐明哪个假设或不变量未被满足。例如，这里我定义了一个自定义测试辅助方法来验证生成器的行为：
[点击此处查看代码图像](#ch13_images#f0537-02)
```
# helper_test.py
from unittest import TestCase, main

def sum_squares(values):
cumulative = 0
for value in values:
cumulative += value**2
yield cumulative

class HelperTestCase(TestCase):
def verify_complex_case(self, values, expected):
expect_it = iter(expected)
found_it = iter(sum_squares(values))
test_it = zip(expect_it, found_it, strict=True)

for i, (expect, found) in enumerate(test_it):
if found != expect:
self.fail(f"Index {i} is wrong: "
f"{found} != {expect}")

def test_too_short(self):
values = [1.1, 2.2]
expected = [1.1**2]
self.verify_complex_case(values, expected)

def test_too_long(self):
values = [1.1, 2.2]
expected = [
1.1**2,
1.1**2 + 2.2**2,
0,  # Value doesn't matter
]
self.verify_complex_case(values, expected)

def test_wrong_results(self):
values = [1.1, 2.2, 3.3]
expected = [
1.1**2,
1.1**2 + 2.2**2,
1.1**2 + 2.2**2 + 3.3**2 + 4.4**2,
]
self.verify_complex_case(values, expected)

if __name__ == "__main__":
main()
```
该辅助方法使测试用例简洁易读，并且输出的错误消息易于理解：
[点击此处查看代码图像](#ch13_images#f0538-02)
```
$ python3 helper_test.py
EEF
==============================================================
ERROR: test_too_long (__main__.HelperTestCase.test_too_long)
--------------------------------------------------------------
Traceback (most recent call last):
File "helper_test.py", line 36, in test_too_long
self.verify_complex_case(values, expected)
~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
File "helper_test.py", line 20, in verify_complex_case
for i, (expect, found) in enumerate(test_it):
~~~~~~~~~^^^^^^^^^
ValueError: zip() argument 2 is shorter than argument 1

==============================================================
ERROR: test_too_short (__main__.HelperTestCase.test_too_short)
--------------------------------------------------------------
Traceback (most recent call last):
File "helper_test.py", line 27, in test_too_short
self.verify_complex_case(values, expected)
~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
File "helper_test.py", line 20, in verify_complex_case
for i, (expect, found) in enumerate(test_it):
~~~~~~~~~^^^^^^^^^
ValueError: zip() argument 2 is longer than argument 1

==============================================================
FAIL: test_wrong_results
➥(__main__.HelperTestCase.test_wrong_results)
--------------------------------------------------------------
Traceback (most recent call last):
File "helper_test.py", line 45, in test_wrong_results
self.verify_complex_case(values, expected)
~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
File "helper_test.py", line 22, in verify_complex_case
self.fail(f"Index {i} is wrong: {found} != {expect}")
~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Index 2 is wrong: 16.939999999999998 != 36.3

--------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1, errors=2)
```
我通常为每一组相关的测试定义一个 `TestCase` 子类。有时，我为每个有许多边缘情况的函数定义一个 `TestCase` 子类。其他时候，一个 `TestCase` 子类会跨越单个模块中的所有函数。我经常为测试每个基本类及其所有方法创建一个 `TestCase` 子类（详见 [Item 109](#ch13#ch13lev1sec2)：“[优先集成测试而非单元测试](#ch13#ch13lev1sec2)” 以获取更多指导）。
`TestCase` 类还提供了一个 `subTest` 辅助方法，通过在单个测试方法中定义多个测试来避免样板代码。这对于编写数据驱动测试尤其有用，并且它允许测试方法在其中一个测试失败后继续测试其他情况（类似于 `TestCase` 及其包含的测试方法的行为；详见 [Item 110](#ch13#ch13lev1sec3)：“[使用 setUp、tearDown、setUpModule 和 tearDownModule 将测试彼此隔离](#ch13#ch13lev1sec3)” 以获取另一种方法）。为了说明这一点，这里我定义了一个数据驱动测试示例：
[点击此处查看代码图像](#ch13_images#f0540-01)
```
# data_driven_test.py
from unittest import TestCase, main
from utils import to_str

class DataDrivenTestCase(TestCase):
def test_good(self):
good_cases = [
(b"my bytes", "my bytes"),
("no error", b"no error"),  # This one will fail
("other str", "other str"),
...
]
for value, expected in good_cases:
with self.subTest(value):
self.assertEqual(expected, to_str(value))

def test_bad(self):
bad_cases = [
(object(), TypeError),
(b"\xfa\xfa", UnicodeDecodeError),
...
]
for value, exception in bad_cases:
with self.subTest(value):
with self.assertRaises(exception):
to_str(value)

if __name__ == "__main__":
main()
```
“no error” 测试用例失败，打印出有用的错误消息，但所有其他用例仍然被测试并确认通过：
[点击此处查看代码图像](#ch13_images#f0540-02)
```
$ python3 data_driven_test.py
.

===============================================================
FAIL: test_good (__main__.DataDrivenTestCase) [no error]
---------------------------------------------------------------
Traceback (most recent call last):
File "testing/data_driven_test.py", line 18, in test_good
self.assertEqual(expected, to_str(value))
AssertionError: b'no error' != 'no error'

---------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```
最终，根据你的项目复杂性和测试需求，你可能会超出 `unittest` 及其功能。如果发生这种情况，`pytest` (<https://pytest.org>) 开源包及其大量的社区插件可以作为替代测试运行器特别有用。

#### 记住
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 你可以通过继承 `unittest` 内置模块的 `TestCase` 类来创建测试，并为每个你想测试的行为定义一个方法。`TestCase` 类中的测试方法必须以 `test` 开头。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `TestCase` 类定义的各种辅助方法，例如 `assertEqual`，来确认测试中的预期行为，而不是使用内置的 `assert` 语句。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 考虑使用 `subTest` 辅助方法编写数据驱动测试，以减少样板代码。

### Item 109: 优先集成测试而非单元测试

有许多软件测试方法比 Python 更广泛，包括测试驱动开发、基于属性的测试、变异测试以及代码和分支覆盖率报告。你会在 Python 的内置和社区包中找到编写各种类型和风格的自动化测试的强大工具（详见 [Item 116](#ch14#ch14lev1sec1)：“[了解社区构建模块的位置](#ch14#ch14lev1sec1)”）。因此，Python 中的问题不是你是否可以并且应该编写测试，而是：多少测试才算足够？以及你的测试应该验证什么？

最好将 Python 中的测试视为代码的保险单。好的测试让你对代码的正确性有信心。如果你重构或扩展代码，验证行为——而不是实现——的测试可以轻松识别出已更改的内容。这听起来有些违反直觉，但拥有构建良好的测试实际上使修改 Python 代码更容易，而不是更难。

与其他语言一样，测试可以测试代码库的许多不同级别。_单元测试_验证一个更大系统中的专注部分。当你有许多边缘情况并且需要确保一切都得到妥善处理时，它们很有用。它们运行速度快，因为它们只使用程序的一小部分。通常它们是使用 mock 构建的（详见 [Item 111](#ch13#ch13lev1sec4)：“[使用 Mocks 测试具有复杂依赖关系的代码](#ch13#ch13lev1sec4)”）。

_集成测试_验证多个组件协同工作。它们通常运行速度较慢且编写起来更困难（详见 [Item 110](#ch13#ch13lev1sec3)：“[使用 setUp、tearDown、setUpModule 和 tearDownModule 将测试彼此隔离](#ch13#ch13lev1sec3)” 中的示例）。然而，集成测试在 Python 中尤为重要，因为你无法保证子系统能够实际互操作，除非你证明了这一点（详见 [Item 3](#ch01#ch01lev1sec3)：“[永远不要期望 Python 在编译时检测到错误](#ch01#ch01lev1sec3)”）。静态类型语言可以使用类型信息来近似组件的粗略匹配，但在动态语言中利用类型可能更加困难（详见 [Item 124](#ch14#ch14lev1sec9)：“[考虑通过 typing 进行静态分析以消除 bug](#ch14#ch14lev1sec9)”）或实际上不可行。

通常在 Python 中，最好编写集成测试。但是，如果你发现代码的某些部分也有许多边界条件需要探索，那么为这些行为编写单元测试可能也是值得的。你不希望只编写单元测试。例如，假设我正在构建嵌入式软件来控制烤面包机。这里我定义了一个 `Toaster` 类，它允许我设置“烘烤程度”，按下面包，或者弹出吐司：
[点击此处查看代码图像](#ch13_images#f0542-01)
```
class Toaster:
def __init__(self, timer):
self.timer = timer
self.doneness = 3
self.hot = False

def _get_duration(self):
return max(0.1, min(120, self.doneness * 10))

def push_down(self):
if self.hot:
return

self.hot = True
self.timer.countdown(self._get_duration(), self.pop_up)

def pop_up(self):
print("Pop!")  # Release the spring
self.hot = False
self.timer.end()
```
`Toaster` 类依赖于一个计时器，该计时器在完成时弹出吐司。应该可以重置计时器任意次数。这里我使用 `threading` 内置模块中的 `Timer` 类来实现这一点：
[点击此处查看代码图像](#ch13_images#f0543-01)
```
import threading

class ReusableTimer:
def __init__(self):
self.timer = None

def countdown(self, duration, callback):
self.end()
self.timer = threading.Timer(duration, callback)
self.timer.start()

def end(self):
if self.timer:
self.timer.cancel()
```
有了这两个类定义，我就可以轻松地测试烤面包机的功能，以显示它可以加热面包并在烧焦之前弹出：
[点击此处查看代码图像](#ch13_images#f0543-02)
```
toaster = Toaster(ReusableTimer())
print("Initially hot:  ", toaster.hot)
toaster.doneness = 5
toaster.push_down()
print("After push down:", toaster.hot)

# Time passes
...
print("After time:     ", toaster.hot)

>>>
Initially hot:   False
After push down: True
Pop!
After time:      False
```
如果我想为 `Toaster` 类编写单元测试，我可能会使用内置的 `unittest` 模块（详见 [Item 108](#ch13#ch13lev1sec1)：“[在 TestCase 子类中验证相关行为](#ch13#ch13lev1sec1)”）这样做，其中我完全 mock 了 `ReusableTimer` 类：
[点击此处查看代码图像](#ch13_images#f0544-02)
```
from unittest import TestCase
from unittest.mock import Mock

class ToasterUnitTest(TestCase):

def test_start(self):
timer = Mock(spec=ReusableTimer)
toaster = Toaster(timer)
toaster.push_down()
self.assertTrue(toaster.hot)
timer.countdown.assert_called_once_with(
30, toaster.pop_up)

def test_end(self):
timer = Mock(spec=ReusableTimer)
toaster = Toaster(timer)
toaster.hot = True
toaster.pop_up()
self.assertFalse(toaster.hot)
timer.end.assert_called_once()

...

>>>
Pop!
..
---------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
为 `ReusableTimer` 类编写单元测试也可以类似地 mock 其依赖项：
[点击此处查看代码图像](#ch13_images#f0544-03)
```
from unittest import mock

class ReusableTimerUnitTest(TestCase):

def test_countdown(self):
my_func = lambda: None
with mock.patch("threading.Timer"):
timer = ReusableTimer()
timer.countdown(0.1, my_func)
threading.Timer.assert_called_once_with(0.1, my_func)
timer.timer.start.assert_called_once()

def test_end(self):
my_func = lambda: None
with mock.patch("threading.Timer"):
timer = ReusableTimer()
timer.countdown(0.1, my_func)
timer.end()
timer.timer.cancel.assert_called_once()

...

>>>
..
---------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```
这些单元测试有效，但需要大量的设置和 mock 操作。相反，考虑这个单一的集成测试，它验证了 `Toaster` 和 `ReusableTimer` 类，而无需使用任何 mock：
[点击此处查看代码图像](#ch13_images#f0545-02)
```
class ToasterIntegrationTest(TestCase):

def setUp(self):
self.timer = ReusableTimer()
self.toaster = Toaster(self.timer)
self.toaster.doneness = 0

def test_wait_finish(self):
self.assertFalse(self.toaster.hot)
self.toaster.push_down()
self.assertTrue(self.toaster.hot)
self.timer.timer.join()
self.assertFalse(self.toaster.hot)

def test_cancel_early(self):
self.assertFalse(self.toaster.hot)
self.toaster.push_down()
self.assertTrue(self.toaster.hot)
self.toaster.pop_up()
self.assertFalse(self.toaster.hot)

...

>>>
Pop!
.Pop!
.
---------------------------------------------------------------
Ran 2 tests in 0.108s

OK
```
这个测试清晰、简洁，并且专注于端到端行为，而不是实现细节。也许我唯一抱怨的是它访问了 `ReusableTimer` 类的内部以正确等待 `threading.Timer` 实例完成（使用 `join` 方法）。但这是 Python，拥有这种用于测试的访问权限是该语言的主要优势之一。
前面分别为 `Toaster` 和 `ReusableTimer` 类编写的单元测试，与这个单一的集成测试相比，显得冗余且不必要地复杂。然而，单元测试可以为这段代码带来一个潜在的好处：测试 `doneness` 设置的边界，以确保它永远不会太长或太短：
[点击此处查看代码图像](#ch13_images#f0546-02)
```
class DonenessUnitTest(TestCase):
def setUp(self):
self.toaster = Toaster(ReusableTimer())

def test_min(self):
self.toaster.doneness = 0
self.assertEqual(0.1, self.toaster._get_duration())

def test_max(self):
self.toaster.doneness = 1000
self.assertEqual(120, self.toaster._get_duration())

...

>>>
..
---------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
这才是你应该在 Python 中编写测试的平衡点：绝对要有用于端到端行为的集成测试，并且可能要有用于复杂边缘情况的单元测试。很容易在大多数时候避免使用 mock，并且只有在有令人信服的理由时才使用它们（详见 [Item 112](#ch13#ch13lev1sec5)：“[封装依赖项以方便 Mock 和测试](#ch13#ch13lev1sec5)”）。否则，不要忘记你仍然需要更大的系统测试来验证你的 Python 程序如何与相应的 Web 客户端、API 端点、移动应用程序、数据库等进行交互。

#### 记住
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 集成测试验证多个组件的行为，而单元测试仅验证单个组件。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 由于 Python 高度动态的特性，集成测试是获得程序正确性信心的最佳方式——有时也是唯一方式。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 单元测试可以与集成测试一起使用，用于验证代码库中具有大量边缘情况或边界条件的部分。

### Item 110: 使用 `setUp`、`tearDown`、`setUpModule` 和 `tearDownModule` 将测试彼此隔离

`TestCase` 子类（详见 [Item 108](#ch13#ch13lev1sec1)：“[在 TestCase 子类中验证相关行为](#ch13#ch13lev1sec1)”）通常需要在运行测试方法之前设置测试环境；这有时被称为_测试框架_。要进行此设置，你可以重写 `TestCase` 父类的 `setUp` 和 `tearDown` 方法。这些方法分别在每个测试方法之前和之后调用，允许你确保每个测试都在隔离的环境中运行，这是正确测试的重要最佳实践。

例如，这里我定义了一个 `TestCase` 子类，它在每个测试之前创建一个临时目录，并在每个测试完成后删除其内容：
[点击此处查看代码图像](#ch13_images#f0547-01)
```
# environment_test.py
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, main

class EnvironmentTest(TestCase):
def setUp(self):
self.test_dir = TemporaryDirectory()
self.test_path = Path(self.test_dir.name)

def tearDown(self):
self.test_dir.cleanup()

def test_modify_file(self):
with open(self.test_path / "data.bin", "w") as f:
...

if __name__ == "__main__":
main()
```
当程序变得复杂时，你可以使用额外的测试来验证模块之间的端到端交互，而不仅仅是隔离地测试代码（详见 [Item 109](#ch13#ch13lev1sec2)：“[优先集成测试而非单元测试](#ch13#ch13lev1sec2)”）。一个常见的问题是，为集成测试设置测试环境可能计算成本高昂，并且可能需要大量实际时间。例如，你可能需要启动一个数据库进程并等待它完成索引加载，然后才能运行集成测试。这种延迟使得在 `TestCase` 子类的 `setUp` 和 `tearDown` 方法中进行测试准备和清理不切实际。

为了处理这种情况，`unittest` 模块还支持模块级别的测试框架初始化。你可以一次性配置昂贵的资源，然后让所有 `TestCase` 类及其测试方法运行，而无需重复该初始化。之后，当模块中的所有测试完成后，测试框架可以一次性拆卸。这里我通过在包含 `TestCase` 子类的模块中定义 `setUpModule` 和 `tearDownModule` 函数来利用这种行为：
[点击此处查看代码图像](#ch13_images#f0548-02)
```
# integration_test.py
from unittest import TestCase, main

def setUpModule():
print("* Module setup")

def tearDownModule():
print("* Module clean-up")

class IntegrationTest(TestCase):
def setUp(self):
print("* Test setup")

def tearDown(self):
print("* Test clean-up")

def test_end_to_end1(self):
print("* Test 1")

def test_end_to_end2(self):
print("* Test 2")

if __name__ == "__main__":
main()

$ python3 integration_test.py
* Module setup
* Test setup
* Test 1
* Test clean-up
.* Test setup
* Test 2
* Test clean-up
.* Module clean-up

---------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
`setUpModule` 函数仅由 `unittest` 运行一次，并且在任何 `setUp` 方法被调用之前发生。类似地，`tearDownModule` 在 `tearDown` 方法被调用之后发生。

#### 记住
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `TestCase` 的 `setUp` 和 `tearDown` 方法来确保你的测试彼此隔离并确保一个干净的测试环境。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 对于集成测试，使用 `setUpModule` 和 `tearDownModule` 模块级函数来管理整个测试模块及其包含的所有 `TestCase` 子类的测试框架。

### Item 111: 使用 Mocks 测试具有复杂依赖关系的代码

编写测试时（详见 [Item 108](#ch13#ch13lev1sec1)：“[在 TestCase 子类中验证相关行为](#ch13#ch13lev1sec1)”）另一个常见的需求是使用 mock 函数和类来模拟行为，当使用真实对象过于困难或缓慢时。例如，假设我需要一个程序来维护动物园动物的喂食计划。这里我定义了一个函数来查询数据库以获取特定物种的所有动物，然后返回它们最近一次进食的时间：
[点击此处查看代码图像](#ch13_images#f0550-01)
```
class DatabaseConnection:
...

def get_animals(database, species):
# Query the Database
...
# Return a list of (name, last_mealtime) tuples
```
我如何获得一个 `DatabaseConnection` 实例来测试这个函数？这里我尝试创建一个并将其传递给被测试的函数：
[点击此处查看代码图像](#ch13_images#f0550-02)
```
database = DatabaseConnection("localhost", "4444")

get_animals(database, "Meerkat")

>>>
Traceback ...
DatabaseConnectionError: Not connected
```
没有运行数据库，所以这当然会失败。一个解决方案是实际启动一个数据库服务器并在测试中连接到它。然而，要完全自动化启动数据库、配置其模式、填充数据等，以仅仅运行一个简单的单元测试，这需要大量的工作。此外，启动数据库服务器可能需要大量实际时间，这会减慢这些单元测试的速度并使其更难维护（详见 [Item 110](#ch13#ch13lev1sec3)：“[使用 setUp、tearDown、setUpModule 和 tearDownModule 将测试彼此隔离](#ch13#ch13lev1sec3)” 以获取一个潜在的解决方案）。

另一种方法是 mock 数据库。_mock_ 允许你在给定一组预期的调用时，为依赖函数提供预期的响应。重要的是不要混淆 mock 和 fake。一个_fake_会提供 `DatabaseConnection` 类的大部分行为，但实现更简单，例如一个基本的内存中、单线程数据库，没有持久性。

Python 有 `unittest.mock` 内置模块，用于创建 mock 并将其用于测试。这里我定义了一个 `Mock` 实例，它模拟 `get_animals` 函数，而无需实际连接到数据库：
[点击此处查看代码图像](#ch13_images#f0551-01)
```
from datetime import datetime
from unittest.mock import Mock

mock = Mock(spec=get_animals)
expected = [
("Spot", datetime(2024, 6, 5, 11, 15)),
("Fluffy", datetime(2024, 6, 5, 12, 30)),
("Jojo", datetime(2024, 6, 5, 12, 45)),
]
mock.return_value = expected
```
`Mock` 类创建一个 mock 函数。mock 的 `return_value` 属性是调用它时要返回的值。`spec` 参数表示 mock 应该像给定的对象一样行事，在本例中是一个函数，如果使用不当则会报错。例如，这里我尝试将 mock 函数当作一个带有属性的 mock 对象来使用：
[点击此处查看代码图像](#ch13_images#f0551-02)
```
mock.does_not_exist

>>>
Traceback ...
AttributeError: Mock object has no attribute 'does_not_exist'
```
一旦创建，我就可以调用 mock，获取它的返回值，并验证它的返回值是否符合预期。我使用一个唯一的 `object()` 值作为 `database` 参数，因为它实际上不会被 mock 用于任何操作；我只关心 `database` 参数是否已正确传递给任何需要 `DatabaseConnection` 实例才能工作的依赖函数：
[点击此处查看代码图像](#ch13_images#f0551-03)
```
database = object()
result = mock(database, "Meerkat")
assert result == expected
```
这验证了 mock 响应正确，但我如何知道调用 mock 的代码是否提供了正确的参数？为此，`Mock` 类提供了 `assert_called_once_with` 方法，该方法验证是否使用给定的参数进行了唯一调用：
[点击此处查看代码图像](#ch13_images#f0551-04)
```
mock.assert_called_once_with(database, "Meerkat")
```
如果我提供了错误的参数，就会引发异常，并且任何使用该断言的 `TestCase` 都会失败：
[点击此处查看代码图像](#ch13_images#f0552-01)
```
mock.assert_called_once_with(database, "Giraffe")

>>>
Traceback ...
AssertionError: expected call not found.
Expected: mock(<object object at 0x104728900>, 'Giraffe')
Actual: mock(<object object at 0x104728900>, 'Meerkat')
```
如果我实际上不关心某些单个参数，例如使用了哪个 `database` 对象，那么我可以使用 `unittest.mock.ANY` 常量来指示任何值都可以用于某个参数。我还可以使用 `Mock` 的 `assert_called_with` 方法来验证对 mock 的最近一次调用——在这种情况下可能有多项调用——是否符合我的预期：
[点击此处查看代码图像](#ch13_images#f0552-02)
```
from unittest.mock import ANY

mock = Mock(spec=get_animals)
mock("database 1", "Rabbit")
mock("database 2", "Bison")
mock("database 3", "Meerkat")

mock.assert_called_with(ANY, "Meerkat")
```
`ANY` 在测试中很有用，当某个参数不是被测试行为的核心时。使用 `ANY` 更宽松地指定测试通常比过度指定测试并需要传递各种测试参数期望更好。
`Mock` 类还可以轻松 mock 异常的引发：
[点击此处查看代码图像](#ch13_images#f0552-03)
```
class MyError(Exception):
pass

mock = Mock(spec=get_animals)
mock.side_effect = MyError("Whoops! Big problem")
result = mock(database, "Meerkat")

>>>
Traceback ...
MyError: Whoops! Big problem
```
还有许多其他功能可用，因此请务必查看模块文档以了解所有选项（<https://docs.python.org/3/library/unittest.mock.html>）。
现在我已经展示了 `Mock` 对象的工作原理，我可以将其应用于实际的测试场景，以展示如何有效地使用它来编写测试。这里我定义了一个函数来完成动物园动物的喂食轮次，给定一组与数据库交互的函数：
[点击此处查看代码图像](#ch13_images#f0553-01)
```
def get_food_period(database, species):
# Query the Database
...
# Return a time delta

def feed_animal(database, name, when):
# Write to the Database
...

def do_rounds(database, species):
now = datetime.now()
feeding_timedelta = get_food_period(database, species)
animals = get_animals(database, species)
fed = 0

for name, last_mealtime in animals:
if (now - last_mealtime) > feeding_timedelta:
feed_animal(database, name, now)
fed += 1

return fed
```
我的测试目标是验证当运行 `do_rounds` 时，正确的动物是否得到了喂食，最新的喂食时间是否已记录到数据库，以及函数返回的被喂食动物的总数是否与正确总数匹配。为了做到这一切，我需要 mock `datetime.now`，以便我的测试可以期望一个稳定的时间，而不受程序执行时间的影响。我需要 mock `get_food_period` 和 `get_animals` 以返回来自数据库的值。并且我需要 mock `feed_animal` 以接受写入数据库的数据。
问题是：即使我知道如何创建这些 mock 函数并设置期望，如何让被测试的 `do_rounds` 函数使用 mock 依赖函数而不是真实版本？一种方法是将所有内容作为仅关键字参数注入（详见 [Item 37](#ch05#ch05lev1sec8)：“[使用仅关键字参数和仅位置参数强制执行清晰性](#ch05#ch05lev1sec8)” 以获取背景信息）：
[点击此处查看代码图像](#ch13_images#f0553-02)
```
def do_rounds(
database,
species,
*,
now_func=datetime.now,
food_func=get_food_period,
animals_func=get_animals,
feed_func=feed_animal
):
now = now_func()
feeding_timedelta = food_func(database, species)
animals = animals_func(database, species)
fed = 0

for name, last_mealtime in animals:
if (now - last_mealtime) > feeding_timedelta:
feed_func(database, name, now)
fed += 1

return fed
```
要测试此函数，我需要预先创建所有 `Mock` 实例并设置它们的期望：
[点击此处查看代码图像](#ch13_images#f0554-02)
```
from datetime import timedelta

now_func = Mock(spec=datetime.now)
now_func.return_value = datetime(2024, 6, 5, 15, 45)

food_func = Mock(spec=get_food_period)
food_func.return_value = timedelta(hours=3)

animals_func = Mock(spec=get_animals)
animals_func.return_value = [
("Spot", datetime(2024, 6, 5, 11, 15)),
("Fluffy", datetime(2024, 6, 5, 12, 30)),
("Jojo", datetime(2024, 6, 5, 12, 45)),
]

feed_func = Mock(spec=feed_animal)
```
然后我可以通过将 mock 传递给 `do_rounds` 函数来覆盖默认值来运行测试：
[点击此处查看代码图像](#ch13_images#f0554-03)
```
result = do_rounds(
database,
"Meerkat",
now_func=now_func,
food_func=food_func,
animals_func=animals_func,
feed_func=feed_func,
)

assert result == 2
```
最后，我可以验证所有对依赖函数的调用是否符合我的期望：
[点击此处查看代码图像](#ch13_images#f0555-02)
```
from unittest.mock import call

food_func.assert_called_once_with(database, "Meerkat")

animals_func.assert_called_once_with(database, "Meerkat")

feed_func.assert_has_calls(
[
call(database, "Spot", now_func.return_value),
call(database, "Fluffy", now_func.return_value),
],
any_order=True,
)
```
我不会验证 `datetime.now` mock 的参数或调用次数，因为这会通过函数的返回值间接验证。对于 `get_food_period` 和 `get_animals`，我通过使用 `assert_called_once_with` 来验证具有指定参数的唯一调用。对于 `feed_animal` 函数，我使用 `unittest.mock.call` 辅助函数和 `assert_has_calls` 方法来验证是否进行了两次调用——并且它们的顺序无关紧要——以写入数据库。

这种使用仅关键字参数注入 mock 的方法有效，但它相当冗长，并且需要更改你想要测试的每个函数。`unittest.mock.patch` 系列函数使注入 mock 更容易。它临时重新分配模块或类的属性，例如我上面定义的数据库访问函数。例如，这里我使用 `patch` 覆盖 `get_animals` 为一个 mock：
[点击此处查看代码图像](#ch13_images#f0555-03)
```
from unittest.mock import patch

print("Outside patch:", get_animals)

with patch("__main__.get_animals"):
print("Inside patch: ", get_animals)

print("Outside again:", get_animals)

>>>
Outside patch: <function get_animals at 0x104eda160>
Inside patch:  <MagicMock name='get_animals' id='4397863264'>
Outside again: <function get_animals at 0x104eda160>
```
`patch` 可用于许多模块、类和属性。它可以用作 `with` 语句（详见 [Item 82](#ch10#ch10lev1sec3)：“[考虑使用 contextlib 和 with 语句实现可重用的 try/finally 行为](#ch10#ch10lev1sec3)”）、函数装饰器（详见 [Item 38](#ch05#ch05lev1sec9)：“[使用 functools.wraps 定义函数装饰器](#ch05#ch05lev1sec9)”）或 `TestCase` 类的 `setUp` 和 `tearDown` 方法中（详见 [Item 110](#ch13#ch13lev1sec3)：“[使用 setUp、tearDown、setUpModule 和 tearDownModule 将测试彼此隔离](#ch13#ch13lev1sec3)”）。

然而，`patch` 并非在所有情况下都有效。例如，要测试 `do_rounds`，我需要 mock 出 `datetime.now` 类方法返回的当前时间。Python 不允许我这样做，因为 `datetime` 类定义在 C 扩展模块中，无法以这种方式修改：
[点击此处查看代码图像](#ch13_images#f0556-02)
```
fake_now = datetime(2024, 6, 5, 15, 45)

with patch("datetime.datetime.now"):
datetime.now.return_value = fake_now

>>>
Traceback ...
TypeError: cannot set 'now' attribute of immutable type
➥'datetime.datetime'

The above exception was the direct cause of the following
➥exception:

Traceback ...
TypeError: cannot set 'now' attribute of immutable type
➥'datetime.datetime'
```
为了解决这个问题，我可以创建另一个辅助函数来获取时间，该函数可以被 patch：
[点击此处查看代码图像](#ch13_images#f0556-03)
```
def get_do_rounds_time():
return datetime.now()

def do_rounds(database, species):
now = get_do_rounds_time()
...

with patch("__main__.get_do_rounds_time"):
...
```
或者，我可以使用仅关键字参数来 mock `datetime.now`，并为所有其他 mock 使用 `patch`：
[点击此处查看代码图像](#ch13_images#f0557-02)
```
def do_rounds(database, species, *, now_func=datetime.now):
now = now_func()
feeding_timedelta = get_food_period(database, species)
animals = get_animals(database, species)
fed = 0

for name, last_mealtime in animals:
if (now - last_mealtime) > feeding_timedelta:
feed_animal(database, name, now)
fed += 1

return fed
```
我将采用后一种方法。现在我可以使用 `patch.multiple` 函数来创建多个 mock，然后设置它们的期望：
[点击此处查看代码图像](#ch13_images#f0557-03)
```
from unittest.mock import DEFAULT

with patch.multiple(
"__main__",
autospec=True,
get_food_period=DEFAULT,
get_animals=DEFAULT,
feed_animal=DEFAULT,
):
now_func = Mock(spec=datetime.now)
now_func.return_value = datetime(2024, 6, 5, 15, 45)
get_food_period.return_value = timedelta(hours=3)
get_animals.return_value = [
("Spot", datetime(2024, 6, 5, 11, 15)),
("Fluffy", datetime(2024, 6, 5, 12, 30)),
("Jojo", datetime(2024, 6, 5, 12, 45)),
]
```
`patch.multiple` 的关键字参数对应于 `__main__` 模块中我想在测试期间覆盖的名称。`DEFAULT` 值表示我想为每个名称创建一个标准的 `Mock` 实例。由于 `autospec=True` 参数，所有生成的 mock 都将遵循它们应该模拟的对象的规范。
设置就绪后，我可以在使用 `patch.multiple` 的 `with` 语句中运行测试并验证调用是否正确：
[点击此处查看代码图像](#ch13_images#f0558-01)
```
result = do_rounds(database, "Meerkat", now_func=now_func)
assert result == 2

get_food_period.assert_called_once_with(database, "Meerkat")
get_animals.assert_called_once_with(database, "Meerkat")
feed_animal.assert_has_calls(
[
call(database, "Spot", now_func.return_value),
call(database, "Fluffy", now_func.return_value),
],
any_order=True,
)
```
这些 mock 按预期工作，但重要的是要认识到，可以通过重构代码使其更易于测试来进一步提高这些测试的可读性并减少样板代码（详见 [Item 112](#ch13#ch13lev1sec5)：“[封装依赖项以方便 Mock 和测试](#ch13#ch13lev1sec5)”）。

#### 记住
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `unittest.mock` 模块提供了使用 `Mock` 类模拟接口行为的方法。当被测试代码所需的依赖项难以设置时，Mock 在测试中很有用。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 mock 时，重要的是要验证被测试代码的行为以及该代码如何调用依赖函数，使用 `Mock.assert_called_once_with` 系列方法。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 关键字参数和 `unittest.mock.patch` 系列函数可用于将 mock 注入被测试代码。

### Item 112: 封装依赖项以方便 Mock 和测试

在上一项（详见 [Item 111](#ch13#ch13lev1sec4)：“[使用 Mocks 测试具有复杂依赖关系的代码](#ch13#ch13lev1sec4)”）中，我展示了如何使用 `unittest.mock` 内置模块的工具——包括 `Mock` 类和 `patch` 系列函数——来编写具有复杂依赖项（如数据库）的测试。然而，生成的测试代码需要大量的样板代码，这可能使得新读者更难理解测试试图验证的内容。

改进这些测试的一种方法是使用包装器对象来封装数据库的接口，而不是将 `DatabaseConnection` 对象作为参数传递给函数。通过重构代码（详见 [Item 123](#ch14#ch14lev1sec8)：“[考虑使用警告来重构和迁移用法](#ch14#ch14lev1sec8)” 以获取一种方法）来使用更好的抽象通常是值得的，因为它有助于创建 mock 和编写测试。这里我将上一项中的各种数据库辅助函数重新定义为类的方法，而不是独立的函数：
[点击此处查看代码图像](#ch13_images#f0559-01)
```
class ZooDatabase:
...

def get_animals(self, species):
...

def get_food_period(self, species):
...

def feed_animal(self, name, when):
...
```
现在我可以重新定义 `do_rounds` 函数来调用 `ZooDatabase` 对象的方法：
[点击此处查看代码图像](#ch13_images#f0559-02)
```
from datetime import datetime

def do_rounds(database, species, *, now_func=datetime.now):
now = now_func()
feeding_timedelta = database.get_food_period(species)
animals = database.get_animals(species)
fed = 0

for name, last_mealtime in animals:
if (now - last_mealtime) >= feeding_timedelta:
database.feed_animal(name, now)
fed += 1

return fed
```
现在编写 `do_rounds` 的测试要容易得多，因为我不再需要使用 `unittest.mock.patch` 将 mock 注入被测试的代码。相反，我可以创建一个 `Mock` 实例来表示一个 `ZooDatabase`，并将其作为 `database` 参数传递。`Mock` 类会为访问的每个属性名称返回一个新的 mock 对象。这些属性可以像方法一样被调用，然后我可以使用它们来设置期望和验证调用。这使得 mock 一个类的所有方法变得容易：
[点击此处查看代码图像](#ch13_images#f0560-02)
```
from unittest.mock import Mock

database = Mock(spec=ZooDatabase)
print(database.feed_animal)
database.feed_animal()
database.feed_animal.assert_any_call()

>>>
<Mock name='mock.feed_animal' id='4386901024'>
```
我可以使用 `ZooDatabase` 封装来重写 `Mock` 设置代码：
[点击此处查看代码图像](#ch13_images#f0560-03)
```
from datetime import timedelta
from unittest.mock import call

now_func = Mock(spec=datetime.now)
now_func.return_value = datetime(2019, 6, 5, 15, 45)

database = Mock(spec=ZooDatabase)
database.get_food_period.return_value = timedelta(hours=3)
database.get_animals.return_value = [
("Spot", datetime(2019, 6, 5, 11, 15)),
("Fluffy", datetime(2019, 6, 5, 12, 30)),
("Jojo", datetime(2019, 6, 5, 12, 55)),
]
```
然后我可以运行被测试的函数，并验证所有依赖方法是否按预期调用：
[点击此处查看代码图像](#ch13_images#f0560-04)
```
result = do_rounds(database, "Meerkat", now_func=now_func)
assert result == 2

database.get_food_period.assert_called_once_with("Meerkat")
database.get_animals.assert_called_once_with("Meerkat")
database.feed_animal.assert_has_calls(
[
call("Spot", now_func.return_value),
call("Fluffy", now_func.return_value),
],
any_order=True,
)
```
使用 `Mock` 的 `spec` 参数在 mock 类时尤其有用，因为它确保被测试代码不会意外调用拼写错误的函数名。这可以帮助你避免一个常见的陷阱，即同一个 bug 同时存在于代码和单元测试中，从而掩盖了一个将在生产中显现出来的真实错误：
[点击此处查看代码图像](#ch13_images#f0561-02)
```
database.bad_method_name()

>>>
Traceback ...
AttributeError: Mock object has no attribute 'bad_method_name'
```
如果我想通过中级集成测试（详见 [Item 109](#ch13#ch13lev1sec2)：“[优先集成测试而非单元测试](#ch13#ch13lev1sec2)”）来端到端地测试这个程序，我仍然需要一种方法将 mock `ZooDatabase` 注入程序。我可以通过创建一个充当_依赖注入_的“缝隙”的辅助函数来实现这一点。这里我定义了一个这样的辅助函数，它使用 `global` 语句在模块作用域中缓存一个 `ZooDatabase` 对象（详见 [Item 120](#ch14#ch14lev1sec5)：“[考虑模块作用域代码来配置部署环境](#ch14#ch14lev1sec5)” 以获取背景信息）：
[点击此处查看代码图像](#ch13_images#f0561-03)
```
DATABASE = None

def get_database():
global DATABASE
if DATABASE is None:
DATABASE = ZooDatabase()
return DATABASE

def main(argv):
database = get_database()
species = argv[1]
count = do_rounds(database, species)
print(f"Fed {count} {species}(s)")
return 0
```
现在我可以使用 `patch` 注入 mock `ZooDatabase`，运行测试，并验证程序的输出。我这里没有使用 mock `datetime.now`；相反，我依赖于 mock 返回的数据库记录相对于当前时间，以产生与单元测试相似的行为。这种方法比 mock 所有内容更不稳定，但它也测试了更多的表面区域：
[点击此处查看代码图像](#ch13_images#f0562-01)
```
import contextlib
import io
from unittest.mock import patch

with patch("__main__.DATABASE", spec=ZooDatabase):
now = datetime.now()

DATABASE.get_food_period.return_value = timedelta(hours=3)
DATABASE.get_animals.return_value = [
("Spot", now - timedelta(minutes=4.5)),
("Fluffy", now - timedelta(hours=3.25)),
("Jojo", now - timedelta(hours=3)),
]

fake_stdout = io.StringIO()
with contextlib.redirect_stdout(fake_stdout):
main(["program name", "Meerkat"])

found = fake_stdout.getvalue()
expected = "Fed 2 Meerkat(s)\n"

assert found == expected
```
结果符合我的预期。创建这个集成测试很简单，因为我设计了实现以使其更容易测试。

#### 记住
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 当单元测试需要大量重复的样板代码来设置 mock 时，一种解决方案可能是将依赖项的功能封装到更易于 mock 的类中。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `unittest.mock` 内置模块的 `Mock` 类通过为访问的每个属性返回一个可以充当 mock 方法的新 mock 来模拟类。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 对于端到端测试，重构代码以拥有更多可以作为显式“缝隙”的辅助函数以用于在测试中注入 mock 依赖项是很有价值的。

### Item 113: 使用 `assertAlmostEqual` 控制浮点数测试中的精度

Python 的 `float` 类型是双精度浮点数（遵循 IEEE 754 标准）。这种方案有其局限性（详见 [Item 106](#ch12#ch12lev1sec7)：“[当精度至关重要时使用 decimal](#ch12#ch12lev1sec7)”），但浮点数在许多用途上都很有用，并且在 Python 中得到了很好的支持。

通常，在数学代码中测试边界条件和其他潜在的错误来源很重要（详见 [Item 109](#ch13#ch13lev1sec2)：“[优先集成测试而非单元测试](#ch13#ch13lev1sec2)” 以获取详细信息）。不幸的是，编写涉及浮点数的自动化测试可能很棘手。例如，这里我使用 `unittest` 内置模块来定义一个测试，该测试尝试（并失败）验证表达式 `5 / 3` 的结果：
[点击此处查看代码图像](#ch13_images#f0563-01)
```
import unittest

class MyTestCase(unittest.TestCase):
def test_equal(self):
n = 5
d = 3
self.assertEqual(1.667, n / d)  # Raises

...

>>>
Traceback ...
AssertionError: 1.667 != 1.6666666666666667
```
问题在于，在 Python 中，表达式 `5 / 3` 的结果是一个无法精确表示为 `float` 值的数字（小数点后重复的 `6` 就证明了这一点）。传递给 `assertEqual` 的预期值 `1.667` 不够精确，无法精确匹配计算结果。（它们相差 0.000333...。）因此，`assertEqual` 方法调用失败。我可以通过使预期结果更精确来解决这个问题，例如字面值 `1.6666666666666667`。但在实践中，使用这种精度会使数值测试难以维护。由于舍入行为，操作顺序可能会产生不同的结果。架构差异（例如 x86 与 AArch64）也可能影响结果。

这里我通过重新排序一个计算来展示这种舍入问题，该计算看起来不应该影响结果，但实际上却影响了（注意最后一位数字）：
```
print(5 / 3 * 0.1)
print(0.1 * 5 / 3)

>>>
0.16666666666666669
0.16666666666666666
```
为了在自动化测试中处理这个问题，`TestCase` 类中的 `assertAlmostEqual` 辅助方法可用于对浮点数进行近似比较。它能正确处理无穷大和 NaN 条件，并最大程度地减少由于舍入引入的误差。这里我使用此方法来验证当小数点后保留两位小数时数字是否相等：
[点击此处查看代码图像](#ch13_images#f0564-01)
```
class MyTestCase2(unittest.TestCase):
def test_equal(self):
...
# Changed
self.assertAlmostEqual(1.667, n / d, places=2)
...

>>>
.
---------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
`assertAlmostEqual` 的 `places` 参数在验证零到一之间带有小数部分的数字时效果很好。但是浮点数行为和重复小数也可能影响较大的数字。例如，考虑这两个计算之间绝对值上的巨大差异，尽管唯一的改变是其中一个系数增加了 `0.001`：
```
print(1e24 / 1.1e16)
print(1e24 / 1.101e16)

>>>
90909090.9090909
90826521.34423251
```
这些值之间的差异约为 82,569。根据用例，这个差值可能很重要，也可能不重要。为了让你能够表达对不精确的容忍度，你可以为 `assertAlmostEqual` 辅助方法提供一个 `delta` 参数。此参数会导致该方法考虑数字之间的绝对差值，并且仅当差值大于提供的 `delta` 时才引发 `AssertionError` 异常。

这里我使用此选项指定 100,000 的容差，这大于 82,569 的差值，从而允许两个断言都通过：
[点击此处查看代码图像](#ch13_images#f0565-01)
```
class MyTestCase3(unittest.TestCase):
def test_equal(self):
a = 1e24 / 1.1e16
b = 1e24 / 1.101e16
self.assertAlmostEqual(90.9e6, a, delta=0.1e6)
self.assertAlmostEqual(90.9e6, b, delta=0.1e6)
```
在某些情况下，你可能需要断言相反的情况：即两个数字在给定容差或小数位数的情况下不接近。`TestCase` 类还提供了 `assertNotAlmostEqual` 方法，使其易于实现。为了处理在测试代码或测试外部比较数字时更复杂的用例，`math` 内置模块提供了 `isclose` 函数，该函数具有类似的功能，并且更多。

#### 记住
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 由于舍入行为，浮点数，特别是它们的小数部分，可能会因应用的操作顺序而改变。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用 `assertEqual` 测试浮点值可能导致不稳定的测试，因为此方法会考虑被比较数字的完整精度。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `assertAlmostEqual` 和 `assertNotAlmostEqual` 方法允许你指定 `places` 或 `delta` 参数来指示在比较浮点数时对差异的容忍度。

### Item 114: 考虑使用 `pdb` 进行交互式调试

在开发程序时，每个人都会遇到代码中的 bug。使用 `print` 函数可以帮助你追踪许多问题的根源（详见 [Item 12](#ch02#ch02lev1sec3)：“[在打印对象时理解 repr 和 str 之间的区别](#ch02#ch02lev1sec3)”）。为导致问题的特定情况编写测试是识别问题的另一种好方法（详见 [Item 109](#ch13#ch13lev1sec2)：“[优先集成测试而非单元测试](#ch13#ch13lev1sec2)”）。

但这些工具不足以找到所有根本原因。当你需要更强大的功能时，是时候尝试 Python 内置的_交互式调试器_了。调试器允许你检查正在运行的程序的_状态_，打印局部变量，并逐条语句地单步执行。

在大多数其他编程语言中，你通过指定源文件中的哪一行要停止来使用调试器，然后执行程序。相比之下，在 Python 中，使用调试器的最简单方法是修改你的程序，在你认为可能出现需要调查的问题之前直接启动调试器。这意味着启动 Python 程序以运行调试器和正常启动它之间没有区别。

要启动调试器，你所要做的就是调用 `breakpoint` 内置函数。这等同于导入 `pdb` 内置模块并运行其 `set_trace` 函数：
[点击此处查看代码图像](#ch13_images#f0566-01)
```
# always_breakpoint.py
import math

def compute_rmse(observed, ideal):
total_err_2 = 0
count = 0
for got, wanted in zip(observed, ideal):
err_2 = (got - wanted) ** 2
breakpoint()  # Start the debugger here
total_err_2 += err_2
count += 1

mean_err = total_err_2 / count
rmse = math.sqrt(mean_err)
return rmse

result = compute_rmse(
[1.8, 1.7, 3.2, 6],
[2, 1.5, 3, 5],
)
print(result)
```
一旦 `breakpoint` 函数运行，程序就会暂停执行，停在 `breakpoint` 调用之后的代码行之前。启动程序的终端将变成一个 Python 调试 shell：
[点击此处查看代码图像](#ch13_images#f0566-02)
```
$ python3 always_breakpoint.py
> always_breakpoint.py(12)compute_rmse()
-> total_err_2 += err_2
(Pdb)
```
在 `(Pdb)` 提示符下，你可以输入局部变量的名称来查看它们的值（或使用 `p <name>`）。你可以通过调用 `locals` 内置函数来查看所有局部变量的列表。你可以导入模块，检查全局状态，构造新对象，甚至修改正在运行的程序的部分。此调试提示符不支持某些 Python 语句和语言功能，但你可以使用 `interact` 命令访问具有程序状态访问权限的标准 Python REPL。

此外，调试器有各种特殊命令来控制和理解程序执行；输入 `help` 查看完整列表。三个非常有用的命令可以更轻松地检查正在运行的程序：
* `**where**`**:** 打印当前的执行调用堆栈。这可以帮助你弄清楚你在程序中的位置以及你是如何到达 `breakpoint` 触发点的。
* `**up**`**:** 将你的作用域向上移动到当前函数的调用者。这允许你检查导致断点的程序更高层级的局部变量。
* `**down**`**:** 将作用域向下移动一个执行调用堆栈级别。

当你完成检查当前状态后，你可以使用以下五个调试器命令以不同的方式控制程序的执行：
* `**step**`**:** 运行程序直到程序中的下一行执行，然后将控制权返回给调试器提示符。如果下一行执行包括调用一个函数，调试器将停止在被调用的函数内部。
* `**next**`**:** 运行程序直到当前函数中的下一行执行，然后将控制权返回给调试器提示符。如果下一行执行包括调用一个函数，调试器将不会停止，直到被调用的函数返回。
* `**return**`**:** 运行程序直到当前函数返回，然后将控制权返回给调试器提示符。
* `**continue**`**:** 继续运行程序直到遇到下一个断点（通过显式的 `breakpoint` 调用或遇到先前调试器命令添加的断点）。
* `**quit**`**:** 退出调试器并结束程序。如果你找到了问题，走得太远，或者需要进行程序修改并重试，请运行此命令。

`breakpoint` 函数可以在程序的任何地方调用。如果你知道你要调试的问题仅在特殊情况下发生，那么你可以编写普通的 Python 代码来在满足特定条件后调用 `breakpoint`。例如，这里我仅当数据点的平方误差大于 `1` 时才启动调试器：
[点击此处查看代码图像](#ch13_images#f0568-01)
```
# conditional_breakpoint.py
def compute_rmse(observed, ideal):
...
for got, wanted in zip(observed, ideal):
err_2 = (got - wanted) ** 2
if err_2 >= 1:  # Start the debugger if True
breakpoint()
total_err_2 += err_2
count += 1
...

result = compute_rmse(
[1.8, 1.7, 3.2, 7],
[2, 1.5, 3, 5],
)
print(result)
```
当我运行程序并进入调试器时，我可以通过检查局部变量来确认条件为真：
[点击此处查看代码图像](#ch13_images#f0568-02)
```
$ python3 conditional_breakpoint.py
> conditional_breakpoint.py(14)compute_rmse()
-> total_err_2 += err_2
(Pdb) wanted
5
(Pdb) got
7
(Pdb) err_2
4
```
另一种到达调试器提示符的有用方法是使用_事后调试_。这允许你在程序引发异常并崩溃_之后_对其进行调试。当你不太确定在哪里放置 `breakpoint` 函数调用时，这特别有用。这里我有一个脚本，由于函数参数中存在复数 `7j` 而导致崩溃：
[点击此处查看代码图像](#ch13_images#f0568-03)
```
# postmortem_breakpoint.py
import math

def compute_rmse(observed, ideal):
...

result = compute_rmse(
[1.8, 1.7, 3.2, 7j],  # Bad input
[2, 1.5, 3, 5],
)
print(result)
```
我使用命令行 `python3 -m pdb -c continue <program path>` 在 `pdb` 模块的控制下运行程序。`continue` 命令告诉 `pdb` 立即开始程序。一旦程序开始运行，它就会遇到问题并自动进入交互式调试器，此时我可以检查程序状态：
[点击此处查看代码图像](#ch13_images#f0569-02)
```
$ python3 -m pdb -c continue postmortem_breakpoint.py
Traceback (most recent call last):
File "pdb.py", line 1944, in main
pdb._run(target)
File "pdb.py", line 1738, in _run
self.run(target.code)
File "bdb.py", line 606, in run
exec(cmd, globals, locals)
File "<string>", line 1, in <module>
File "postmortem_breakpoint.py", line 22, in <module>
result = compute_rmse(
[1.8, 1.7, 3.2, 7j],  # Bad input
[2, 1.5, 3, 5],
)
File "postmortem_breakpoint.py", line 17, in compute_rmse
rmse = math.sqrt(mean_err)
TypeError: must be real number, not complex
Uncaught exception. Entering post mortem debugging
Running 'cont' or 'step' will restart the program
> postmortem_breakpoint.py(17)compute_rmse()
-> rmse = math.sqrt(mean_err)
(Pdb) mean_err
(-5.97-17.5j)
```
你还可以通过调用 `pdb` 模块的 `pm` 函数在交互式 Python 解释器中遇到未捕获的异常后使用事后调试（通常在一行中完成，如 `import pdb; pdb.pm()`）：
[点击此处查看代码图像](#ch13_images#f0569-03)
```
$ python3
>>> import my_module
>>> my_module.compute_stddev([5])
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "my_module.py", line 20, in compute_stddev
variance = compute_variance(data)
^^^^^^^^^^^^^^^^^^^^^^
File "my_module.py", line 15, in compute_variance
variance = err_2_sum / (len(data) - 1)
~~~~~~~~~~^~~~~~~~~~~~~~~~~
ZeroDivisionError: float division by zero
>>> import pdb; pdb.pm()
> my_module.py(15)compute_variance()
-> variance = err_2_sum / (len(data) - 1)
(Pdb) err_2_sum
0.0
(Pdb) len(data)
1
```
#### 记住
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 你可以通过调用 `breakpoint` 内置函数在程序的兴趣点直接启动 Python 交互式调试器。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `pdb` shell 命令可以精确控制程序执行，并允许你在检查程序状态和推进程序执行之间进行切换。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `pdb` 模块可用于在独立 Python 程序（使用 `python -m pdb -c continue <program path>`）或交互式 Python 解释器（使用 `import pdb; pdb.pm()`）中调试异常。

### Item 115: 使用 `tracemalloc` 理解内存使用和泄漏

Python 的默认实现 CPython 中的内存管理使用引用计数。这确保了只要对象的所有引用都已过期，被引用的对象也会从内存中清除，从而为其他数据释放空间。CPython 还有一个内置的循环检测器，以确保自引用对象最终会被垃圾回收。

理论上，这意味着大多数 Python 开发人员不必担心在程序中分配或释放内存。它由语言和 CPython 运行时自动处理。然而，在实践中，当不再有用的引用仍然被持有，程序最终会耗尽内存。弄清楚 Python 程序在哪里使用或泄漏内存可能具有挑战性。

调试内存使用的一种方法是要求 `gc` 内置模块列出垃圾回收器当前知道的所有对象。虽然这是一个非常粗略的工具，但这种方法可以让你快速了解程序内存的使用情况。这里我定义了一个通过持有引用的模块来填满内存：
[点击此处查看代码图像](#ch13_images#f0571-01)
```
# waste_memory.py
import os

class MyObject:
def __init__(self):
self.data = os.urandom(100)

def get_data():
values = []
for _ in range(100):
obj = MyObject()
values.append(obj)
return values

def run():
deep_values = []
for _ in range(100):
deep_values.append(get_data())
return deep_values
```
然后我运行一个使用 `gc` 内置模块的程序，以打印出执行期间创建的对象数量，以及分配对象的少量样本：
[点击此处查看代码图像](#ch13_images#f0571-02)
```
# using_gc.py
import gc

found_objects = gc.get_objects()
print("Before:", len(found_objects))

import waste_memory

hold_reference = waste_memory.run()

found_objects = gc.get_objects()
print("After: ", len(found_objects))
for obj in found_objects[:3]:
print(repr(obj)[:100])

>>>
Before: 6207
After:  16801
<waste_memory.MyObject object at 0x10390aeb8>
<waste_memory.MyObject object at 0x10390aef0>
<waste_memory.MyObject object at 0x10390af28>
...
```
`gc.get_objects` 的问题在于它没有告诉你关于对象是如何分配的任何信息。在复杂的程序中，特定类的对象可以以多种不同的方式分配。了解对象的总数不如识别负责分配泄漏内存的对象的代码重要。

Python 3.4 引入了一个新的 `tracemalloc` 内置模块来解决这个问题。`tracemalloc` 可以将对象追溯到其分配位置。你可以通过获取内存使用情况的开始和结束快照并进行比较来了解发生了什么变化。这里我使用这种方法来打印程序中排名前三的内存使用“罪魁祸首”：
[点击此处查看代码图像](#ch13_images#f0572-02)
```
# top_n.py
import tracemalloc

tracemalloc.start(10)                      # Set stack depth
time1 = tracemalloc.take_snapshot()        # Before snapshot

import waste_memory

x = waste_memory.run()                     # Usage to debug
time2 = tracemalloc.take_snapshot()        # After snapshot

stats = time2.compare_to(time1, "lineno")  # Compare snapshots
for stat in stats[:3]:
print(stat)

>>>
waste_memory.py:5: size=2392 KiB (+2392 KiB), count=29994
➥(+29994), average=82 B
waste_memory.py:10: size=547 KiB (+547 KiB), count=10001
➥(+10001), average=56 B
waste_memory.py:11: size=82.8 KiB (+82.8 KiB), count=100
➥(+100), average=848 B
```
输出中的 size 和 count 标签清楚地表明了哪些对象主导了我的程序的内存使用，以及它们在源代码中的分配位置。
`tracemalloc` 模块还可以打印出每个分配的完整堆栈跟踪（最多到传递给 `tracemalloc.start` 函数的帧数）。这里我打印出程序中最大内存使用来源的堆栈跟踪：
[点击此处查看代码图像](#ch13_images#f0573-02)
```
# with_trace.py
import tracemalloc

tracemalloc.start(10)
time1 = tracemalloc.take_snapshot()

import waste_memory

x = waste_memory.run()
time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, "traceback")
top = stats[0]
print("Biggest offender is:")
print("\n".join(top.traceback.format()))

>>>
Biggest offender is:
File "with_trace.py", line 11
x = waste_memory.run()
File "waste_memory.py", line 20
deep_values.append(get_data())
File "waste_memory.py", line 12
obj = MyObject()
File "waste_memory.py", line 6
self.data = os.urandom(100)
```
像这样的堆栈跟踪对于弄清楚程序中特定函数或类的使用是导致内存消耗的原因最有价值。
对于更高级的内存分析需求，还有社区包（详见 [Item 116](#ch14#ch14lev1sec1)：“[了解社区构建模块的位置](#ch14#ch14lev1sec1)”）可供考虑，例如 Memray (<https://github.com/bloomberg/memray>)。

#### 记住
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 了解 Python 程序如何使用和泄漏内存可能很困难。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `gc` 模块可以帮助你了解哪些对象存在，但它没有关于它们如何分配的信息。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `tracemalloc` 内置模块提供了强大的工具来理解内存使用来源。
---
<a role="toc_link" id="ch14"></a>

## Effective Python - 14

## 14

本章深入探讨了 Graph Neural Networks (GNNs) 的前沿发展，重点关注 Graph Foundation Models (GFMs) 的兴起及其在处理复杂图结构数据方面的巨大潜力。我们将详细阐述 GFMs 的核心思想、架构设计以及它们如何通过大规模预训练和高效的微调策略，实现跨领域和多模态的学习能力。

**核心贡献与主要观点:**

本章的核心贡献在于系统性地梳理了 GFMs 的发展脉络，并重点突出了它们在以下几个方面的突破性进展：

*   **通用性与迁移学习:** GFMs 的出现标志着图学习领域向通用模型迈进的重要一步。通过在海量、多样化的图数据集上进行预训练，GFMs 能够学习到丰富的图结构和节点表示，从而在各种下游任务中展现出强大的迁移学习能力，包括但不限于 Node Classification, Link Prediction, Graph Classification 等。
*   **高效的预训练策略:** 本章将深入探讨 GFMs 所采用的各种预训练方法，例如基于 Message Passing 的自监督学习（Self-supervised Learning）和对比学习（Contrastive Learning）。这些方法旨在让模型在没有显式标签的情况下，学习到有意义的 Node Embedding 和图表示。
*   **灵活的微调与适应:** GFMs 的强大之处还在于其灵活的微调（Fine-tuning）能力。我们将介绍如何针对特定的下游任务和数据集，对预训练好的 GFMs 进行高效的微调，以达到最佳性能。此外，本章还将讨论 In-context Learning, Few-shot Learning 和 Zero-shot Learning 等技术在 GFMs 中的应用，以应对数据稀疏的挑战。
*   **处理异构与多模态数据:** 现代现实世界中的图数据往往是异构的（Heterogeneous Graph）且包含多模态信息（Multi-modal Learning）。本章将重点介绍 GFMs 如何有效地处理这些复杂性，例如通过专门的架构设计和注意力机制（如 Graph Attention Networks - GAT）来捕捉不同节点类型和边类型之间的关系，以及如何融合文本、图像等模态信息。
*   **与 Transformer 的融合:** Transformer 架构在自然语言处理领域取得了巨大成功，其自注意力机制也被引入到图学习中。本章将探讨 Transformer 如何与 GNNs 相结合，形成更强大的模型，例如 Graph Transformer，以及它们在处理长距离依赖和全局图结构方面的优势。

**逻辑顺序组织总结:**

本章将按照以下逻辑顺序组织内容，以确保内容的连贯性和深度：

1.  **GFMs 的概念与动机:** 首先，我们将介绍 GFMs 的基本概念，解释为什么需要 GFMs，以及它们与传统 GNNs 的区别和优势。
2.  **GFMs 的架构设计:** 接着，我们将深入探讨 GFMs 的典型架构，包括其编码器-解码器结构、预训练任务的设计以及如何处理大规模图数据。
3.  **预训练方法详解:** 本节将详细介绍各种用于 GFMs 的预训练方法，包括自监督学习、对比学习等，并分析它们的优缺点。
4.  **微调与适应策略:** 我们将重点介绍如何对 GFMs 进行微调，以适应不同的下游任务。同时，还将讨论 In-context Learning, Few-shot Learning 和 Zero-shot Learning 在 GFMs 中的应用。
5.  **处理异构图与多模态数据:** 本节将专门讨论 GFMs 如何处理异构图和多模态数据，包括相关的架构设计和学习策略。
6.  **GFMs 的应用场景:** 最后，我们将展示 GFMs 在各种实际应用中的成功案例，例如知识图谱（Knowledge Graph）推理、药物发现、社交网络分析等。

通过本章的学习，读者将能够深入理解 GFMs 的核心原理和技术细节，并掌握如何利用这些强大的模型来解决复杂的图结构数据问题。

## Effective Python - Collaboration

## 协作

Python 拥有语言特性，可以帮助您构建具有清晰接口边界的良好定义的 API。Python 社区已经建立了最佳实践，以最大程度地提高代码的长期可维护性。此外，一些随 Python 一起提供的标准工具使大型团队能够在不同的环境中协同工作。

与他人协作进行 Python 程序开发需要您在编写代码时深思熟虑。即使您独自工作，也很可能通过标准库或开源包使用他人编写的代码。理解使与其他 Python 程序员协作变得容易的机制非常重要。

### Item 116: 了解在哪里查找社区构建的模块

Python 有一个模块的中央存储库（<https://pypi.org>），您可以在程序中安装和使用这些模块。这些模块由像您一样的人构建和维护：Python 社区。当您面临一个不熟悉的挑战时，Python Package Index (PyPI) 是查找能让您更接近目标的代码的好地方。

要使用 Package Index，您需要使用名为 `pip` 的命令行工具（“`pip` installs packages” 的递归首字母缩写）。您可以运行 `python3 -m pip` 来确保包是为系统上正确版本的 Python 安装的（请参阅 [Item 1](#ch01#ch01lev1sec1)：“[了解您正在使用哪个 Python 版本](#ch01#ch01lev1sec1)”）。使用 `pip` 安装新模块很简单。例如，这里我安装 `numpy` 模块（有关相关信息，请参阅 [Item 94](#ch11#ch11lev1sec3)：“[了解何时以及如何用另一种编程语言替换 Python](#ch11#ch11lev1sec3)”）：

[点击此处查看代码图片](#ch14_images#f0575-01)

```
$ python3 -m pip install numpy
Collecting numpy
Downloading ...
Installing collected packages: numpy
Successfully installed numpy-2.0.0
```

`pip` 与内置模块 `venv` 一起使用效果最佳，可以一致地跟踪要为项目安装的包集（请参阅 [Item 117](#ch14#ch14lev1sec2)：“[为隔离和可重现的依赖项使用虚拟环境](#ch14#ch14lev1sec2)”）。您还可以创建自己的 PyPI 包与 Python 社区共享，或托管自己的私有包存储库以供 `pip` 使用。

PyPI 中的每个模块都有自己的软件许可证。对于大多数包，尤其是流行的包，许可证是免费或开源的（有关详细信息，请参阅 <https://opensource.org>）。此类许可证通常允许您将模块的副本包含在您的程序中（包括用于最终用户分发；请参阅 [Item 125](#ch14#ch14lev1sec10)：“[打包 Python 程序时，优先选择开源项目而非 zipimport 和 zipapp](#ch14#ch14lev1sec10)”）；如有疑问，请咨询律师。

#### 需牢记事项

* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python Package Index (PyPI) 包含大量由 Python 社区构建和维护的常用包。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `pip` 是您可以使用命令行工具从 PyPI 安装包。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 大多数 PyPI 模块是免费和开源软件。

### Item 117: 为隔离和可重现的依赖项使用虚拟环境

构建更大、更复杂的程序通常会使您依赖 Python 社区的各种包（请参阅 [Item 116](#ch14#ch14lev1sec1)：“[了解在哪里查找社区构建的模块](#ch14#ch14lev1sec1)”）。您会发现自己运行 `python3 -m pip` 命令行工具来安装 `numpy`、`pandas` 等包。

问题在于，默认情况下，`pip` 将新包安装在全局位置。这会导致您系统上的所有 Python 程序都受到这些已安装模块的影响。理论上，这不应该是一个问题。如果您安装了一个包但从未导入它，它怎么会影响您的程序呢？

麻烦来自于传递性依赖：您安装的包所依赖的包。例如，安装 `Sphinx` 包后，您可以通过询问 `pip` 来查看它依赖于什么：

[点击此处查看代码图片](#ch14_images#f0577-01)

```
$ python3 -m pip show Sphinx
Name: Sphinx
Version: 7.4.6
Summary: Python documentation generator
Location: /usr/local/lib/python3.13/site-packages
Requires: alabaster, babel, docutils, imagesize, Jinja2,
➥ packaging, Pygments, requests, snowballstemmer,
➥ sphinxcontrib-applehelp, sphinxcontrib-devhelp,
➥ sphinxcontrib-htmlhelp, sphinxcontrib-jsmath,
➥ sphinxcontrib-qthelp, sphinxcontrib-serializinghtml
```

如果您安装了另一个包，如 `flask`，您可以看到它也依赖于 `Jinja2` 包：

[点击此处查看代码图片](#ch14_images#f0577-02)

```
$ python3 -m pip show flask
Name: Flask
Version: 3.0.3
Summary: A simple framework for building complex web applications.
Location: /usr/local/lib/python3.13/site-packages
Requires: blinker, click, itsdangerous, Jinja2, Werkzeug
```

随着 `Sphinx` 和 `flask` 随时间推移而分歧，可能会出现依赖冲突。也许现在它们都要求相同版本的 `Jinja2`，一切都很好。但六个月或一年后，`Jinja2` 可能会发布一个新版本，该版本会对库的用户进行重大更改。如果您使用 `python3 -m pip install --upgrade Jinja2` 更新了全局 `Jinja2` 版本，您可能会发现 `Sphinx` 损坏了，而 `flask` 仍然正常工作。

造成这种损坏的原因是 Python 一次只能安装一个全局模块版本。如果您的一个已安装包必须使用新版本，而另一个包必须使用旧版本，则您的系统将无法正常工作；这种情况通常称为 _依赖地狱_。

即使包维护者尽最大努力在版本之间保持 API 兼容性，这种损坏也可能发生（请参阅 [Item 119](#ch14#ch14lev1sec4)：“[使用包来组织模块并提供稳定的 API](#ch14#ch14lev1sec4)”）。库的新版本可能会微妙地改变 API 消费代码所依赖的行为。系统上的用户可能会将一个包升级到一个新版本，但不会升级其他包，这可能会破坏依赖关系。如果您不小心，地面就会不断移动。

当您与其他在单独计算机上工作的开发人员协作时，这些困难会加剧。最好假设最坏的情况：他们在机器上安装的 Python 和全局包的版本将与您的略有不同。这些差异可能导致令人沮丧的情况，例如代码在一个程序员的机器上完美运行，而在另一个程序员的机器上完全损坏。

所有这些问题的解决方案是使用一个名为 `venv` 的工具，它提供了 _虚拟环境_。自 Python 3.4 起，`pip` 和 `venv` 模块已默认与 Python 安装一起提供（可以通过 `python -m venv` 访问）。

`venv` 允许您创建 Python 环境的隔离版本。使用 `venv`，您可以在同一系统上同时安装同一包的多个不同版本而不会发生冲突。这意味着您可以在同一台计算机上处理许多不同的项目并使用许多不同的工具。

`venv` 通过将包及其依赖项的显式版本安装到完全独立的文件目录结构中来实现这一点。这使得重现一个您知道可以与您的代码一起工作的 Python 环境成为可能。这是避免意外损坏的可靠方法。

#### 在命令行中使用 `venv`

以下是如何有效使用 `venv` 的快速教程。在使用该工具之前，重要的是要注意您系统上的 `python3` 命令的含义。在我的计算机上，`python3` 位于 `/usr/local/bin` 目录中，其版本评估为 3.13（请参阅 [Item 1](#ch01#ch01lev1sec1)：“[了解您正在使用哪个 Python 版本](#ch01#ch01lev1sec1)”）：

```
$ which python3
/usr/local/bin/python3
$ python3 --version
Python 3.13.0
```

为了演示我的环境设置，我可以测试运行导入 `numpy` 模块的命令不会导致错误。这之所以可行，是因为我已经将 `numpy` 包安装为全局模块：

```
$ python3 -c 'import numpy'
$
```

现在我使用 `venv` 创建一个名为 `myproject` 的新虚拟环境。每个虚拟环境都必须驻留在其自己的唯一目录中。命令的结果是用于管理虚拟环境的目录和文件的树：

[点击此处查看代码图片](#ch14_images#f0579-01)

```
$ python3 -m venv myproject
$ cd myproject
$ ls
bin     include     lib     pyvenv.cfg
```

要开始使用虚拟环境，我使用 shell 的 `source` 命令在 `bin/activate` 脚本上运行。`activate` 修改我所有的环境变量以匹配虚拟环境。它还会更新我的命令行提示符以包含虚拟环境名称（`myproject`），使其非常清楚我正在处理什么：

```
$ source bin/activate
(myproject)$
```

在 Windows 上，相同的脚本可作为：

[点击此处查看代码图片](#ch14_images#f0579-03)

```
C:\> myproject\Scripts\activate.bat
(myproject) C:>
```

在 PowerShell 中，它可作为：

[点击此处查看代码图片](#ch14_images#f0579-04)

```
PS C:\> myproject\Scripts\activate.ps1
(myproject) PS C:>
```

激活后，您可以看到 `python3` 命令的路径已移至虚拟环境目录内：

[点击此处查看代码图片](#ch14_images#f0579-05)

```
(myproject)$ which python3
/tmp/myproject/bin/python3
(myproject)$ ls -l /tmp/myproject/bin/python3
... -> /usr/local/bin/python3
```

这确保了对外部系统的更改不会影响虚拟环境。即使外部系统将其默认的 `python3` 升级到 3.14 版本，我的虚拟环境仍将显式指向 3.13 版本。

我用 `venv` 创建的虚拟环境启动时，除了 `pip` 和 `setuptools` 之外，没有安装任何包。尝试使用在外部系统上安装的全局模块 `numpy` 包将失败，因为它对虚拟环境来说是未知的：

[点击此处查看代码图片](#ch14_images#f0579-06)

```
(myproject)$ python3 -c 'import numpy'
Traceback (most recent call last):
File "<string>", line 1, in <module>
import numpy
ModuleNotFoundError: No module named 'numpy'
```

我可以使用 `pip` 命令行工具将 `numpy` 模块安装到我的虚拟环境中：

[点击此处查看代码图片](#ch14_images#f0580-02)

```
(myproject)$ python3 -m pip install numpy
Collecting numpy
Downloading ...
Installing collected packages: numpy
Successfully installed numpy-2.0.0
```

安装后，我可以通过使用相同的测试导入命令来验证它是否正常工作：

[点击此处查看代码图片](#ch14_images#f0580-03)

```
(myproject)$ python3 -c 'import numpy'
(myproject)$
```

当我完成虚拟环境并想返回到我的默认系统时，我使用 `deactivate` 命令。这将我的环境恢复到系统默认值，包括 `python3` 命令的路径：

```
(myproject)$ which python3
/tmp/myproject/bin/python3
(myproject)$ deactivate
$ which python3
/usr/local/bin/python3
```

如果我以后想再次使用 `myproject` 环境，我只需在目录中运行 `source bin/activate`（或 Windows 上的类似命令），就像以前一样。

#### 重现依赖项

一旦进入虚拟环境，您就可以继续使用 `pip` 按需安装包。最终，您可能希望将环境复制到其他地方。例如，假设我想将我的工作站的开发环境重现在数据中心的服务器上。或者，也许我想在我自己的机器上克隆别人的环境，以便我可以帮助调试他们的代码。`venv` 使这些任务变得容易。

我可以使用 `python3 -m pip freeze` 命令将我所有的显式包依赖项保存到文件中（根据约定，该文件名为 `requirements.txt`）：

[点击此处查看代码图片](#ch14_images#f0580-05)

```
(myproject)$ python3 -m pip freeze > requirements.txt
(myproject)$ cat requirements.txt
certifi==2024.7.4
charset-normalizer==3.3.2
idna==3.7
numpy==2.0.0
requests==2.32.3
urllib3==2.2.2
```

现在想象一下，我想拥有另一个与 `myproject` 环境匹配的虚拟环境。我可以通过使用 `venv` 并激活它来像以前一样创建一个新目录：

[点击此处查看代码图片](#ch14_images#f0581-02)

```
$ python3 -m venv otherproject
$ cd otherproject
$ source bin/activate
(otherproject)$
```

新环境将不会安装任何额外的包：

[点击此处查看代码图片](#ch14_images#f0581-03)

```
(otherproject)$ python3 -m pip list
Package Version
------- -------
pip     24.1.1
```

我可以通过在 `requirements.txt` 文件上运行 `python3 -m pip install` 来安装第一个环境中的所有包，该文件是我使用 `python3 -m pip freeze` 命令生成的：

[点击此处查看代码图片](#ch14_images#f0581-04)

```
(otherproject)$ python3 -m pip install -r
➥/tmp/myproject/ requirements.txt
```

此命令运行一段时间，因为它检索并安装了重现第一个环境所需的所有包。完成后，我可以列出第二个虚拟环境中已安装的包集，并应看到与第一个虚拟环境中相同的依赖项列表：

[点击此处查看代码图片](#ch14_images#f0581-05)

```
(otherproject)$ python3 -m pip list
Package            Version
------------------ --------
certifi            2024.7.4
charset-normalizer 3.3.2
idna               3.7
pip                24.1.1
urllib3            2.2.2
```

使用 `requirements.txt` 文件非常适合通过修订控制系统与他人协作。您可以在提交代码更改的同时更新您的包依赖项列表，确保它们同步进行。但是，重要的是要注意，您正在使用的 Python 的特定版本 _未_ 包含在 `requirements.txt` 文件中，因此必须单独管理。

虚拟环境的陷阱是移动它们会破坏一切，因为所有路径，包括 `python3` 命令，都已硬编码到环境的安装目录。但最终这个限制无关紧要。虚拟环境的整个目的是使重现设置变得容易。与其移动虚拟环境目录，不如在旧环境上使用 `python3 -m pip freeze`，在其他地方创建一个新的虚拟环境，然后从 `requirements.txt` 文件重新安装所有内容。

#### 需牢记事项

* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 虚拟环境允许您使用 `pip` 在同一台机器上安装同一包的多个不同版本而不会发生冲突。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 虚拟环境使用 `python -m venv` 创建，使用 `source bin/activate` 启用，并使用 `deactivate` 禁用。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 您可以使用 `python3 -m pip freeze` 转储环境的所有需求。您可以通过运行 `python3 -m pip install -r requirements.txt` 来重现环境。

### Item 118: 为每个函数、类和模块编写文档字符串

由于 Python 语言的动态特性，文档非常重要。Python 提供了内置支持，可以将文档附加到代码块。与许多其他语言不同，程序源代码中的文档在程序运行时是直接可访问的。

例如，您可以通过在函数 `def` 语句之后提供 _文档字符串_ 来添加文档：

[点击此处查看代码图片](#ch14_images#f0582-01)

```
def palindrome(word):
"""Return True if the given word is a palindrome."""
return word == word[::-1]

assert palindrome("tacocat")
assert not palindrome("banana")
```

您可以通过访问函数的 `__doc__` 特殊属性，在 Python 程序本身内部检索文档字符串：

[点击此处查看代码图片](#ch14_images#f0582-02)

```
print(palindrome.__doc__)

>>>
Return True if the given word is a palindrome.
```

您还可以从命令行使用内置的 `pydoc` 模块，在您的计算机上运行一个本地 Web 服务器，该服务器托管您的解释器可访问的所有 Python 文档，包括您编写的模块：

[点击此处查看代码图片](#ch14_images#f0583-02)

```
$ python3 -m pydoc -p 1234
Server ready at http://localhost:1234/
Server commands: [b]rowser, [q]uit
server> b
```

文档字符串可以附加到函数、类和模块。建立这种联系是编译和运行 Python 程序过程的一部分。对文档字符串和 `__doc__` 属性的支持有三个后果：

* 文档的可访问性使交互式开发更加容易。您可以通过使用 `help` 内置函数来检查函数、类和模块以查看它们的文档。这使得 Python 交互式解释器和 Jupyter (<https://jupyter.org>) 等工具在您开发算法、测试 API 和编写代码片段时非常有用。
* 使用标准化的文档定义方式可以轻松构建将文本转换为更吸引人格式（如 HTML）的工具。这为 Python 社区带来了出色的文档生成工具，例如 Sphinx (<https://www.sphinx-doc.org>)。它还支持 Read the Docs (<https://readthedocs.org>) 等服务，这些服务为开源 Python 项目提供免费托管的精美文档。
* Python 的一流、可访问且外观良好的文档鼓励人们编写更多文档。Python 社区的成员坚信文档的重要性。人们普遍认为“好代码”也意味着文档齐全的代码，因此您可以期望大多数开源 Python 库都有不错的文档。

要参与这种出色的文档文化，您在编写文档字符串时需要遵循一些准则。完整详细信息在线 PEP 257 (<https://www.python.org/dev/peps/pep-0257/>) 中讨论。以下是一些您应确保遵循的最佳实践。

#### 文档化模块

每个模块都应有一个顶层文档字符串——一个作为源文件第一条语句的字符串文字。它应使用三个双引号（`"""`）。此文档字符串的目的是介绍模块及其内容。

文档字符串的第一行应是一个描述模块用途的单句。随后的段落应包含所有模块用户应了解的有关其操作的详细信息。模块文档字符串也是一个起点，您可以在其中突出显示模块中的重要类和函数。

以下是模块文档字符串的示例：

[点击此处查看代码图片](#ch14_images#f0584-01)

```
# words.py
#!/usr/bin/env python3
"""Library for finding linguistic patterns in words.

Testing how words relate to each other can be tricky sometimes!
This module provides easy ways to determine when words you've
found have special properties.

Available functions:
- palindrome: Determine if a word is a palindrome.
- check_anagram: Determine if two words are anagrams.
...
"""

...
```

如果模块是命令行实用程序，模块文档字符串也是放置运行该工具的用法信息的绝佳位置。

#### 文档化类

每个类都应有一个类级别文档字符串，其模式在很大程度上与模块级别文档字符串相同。第一行是类的单句用途。随后的段落讨论了类操作的重要细节。

类文档字符串中应突出显示类的重要公共属性和方法。它还应为子类提供有关如何正确与受保护属性（请参阅 [Item 55](#ch07#ch07lev1sec8)：“[优先使用公共属性而非私有属性](#ch07#ch07lev1sec8)”）和超类方法（请参阅 [Item 53](#ch07#ch07lev1sec6)：“[使用 super 初始化父类](#ch07#ch07lev1sec6)”）交互的指导。

以下是类文档字符串的示例：

[点击此处查看代码图片](#ch14_images#f0585-01)

```
class Player:
"""Represents a player of the game.

Subclasses may override the 'tick' method to provide
custom animations for the player's movement depending
on their power level, etc.

Public attributes:
- power: Unused power-ups (float between 0 and 1).
- coins: Coins found during the level (integer).
"""

...
```

#### 文档化函数

每个公共函数和方法都应有一个文档字符串，其模式与模块和类的文档字符串相同。第一行是描述函数功能的单句。随后的段落描述了任何特定行为和函数的参数。应提及任何返回值，并解释调用者作为函数接口一部分必须处理的任何异常（有关示例，请参阅 [Item 32](#ch05#ch05lev1sec3)：“[优先抛出异常而非返回 None](#ch05#ch05lev1sec3)”）。

以下是函数文档字符串的示例：

[点击此处查看代码图片](#ch14_images#f0585-02)

```
def find_anagrams(word, dictionary):
"""Find all anagrams for a word.

This function only runs as fast as the test for
membership in the 'dictionary' container.

Args:
word: String of the target word.
dictionary: collections.abc.Container with all
strings that are known to be actual words.

Returns:
List of anagrams that were found. Empty if
none were found.
"""
...
```

编写函数文档字符串时，还有一些重要的特殊情况需要了解：

* 如果函数没有参数且返回值简单，单句描述可能就足够了。
* 如果函数不返回任何内容，最好省略任何关于返回值的提及，而不是说“返回 `None`”。
* 如果函数的接口包括抛出异常，那么您的文档字符串应描述每个抛出的异常以及何时抛出。
* 如果您不希望函数在正常操作期间抛出异常，则不要提及该事实。
* 如果函数接受可变数量的参数（请参阅 [Item 34](#ch05#ch05lev1sec5)：“[使用可变位置参数减少视觉混乱](#ch05#ch05lev1sec5)”）或关键字参数（请参阅 [Item 35](#ch05#ch05lev1sec6)：“[通过关键字参数提供可选行为](#ch05#ch05lev1sec6)”），请在文档化的参数列表中使用 `*args` 和 `**kwargs` 来描述它们的用途。
* 如果函数具有带有默认值的参数，则应提及这些默认值（请参阅 [Item 36](#ch05#ch05lev1sec7)：“[使用 None 和文档字符串指定动态默认参数](#ch05#ch05lev1sec7)”）。
* 如果函数是生成器（请参阅 [Item 43](#ch06#ch06lev1sec4)：“[考虑使用生成器而非返回列表](#ch06#ch06lev1sec4)”），其文档字符串应描述生成器在迭代时产生的内容。
* 如果函数是异步协程（请参阅 [Item 75](#ch09#ch09lev1sec9)：“[使用协程实现高度并发的 I/O](#ch09#ch09lev1sec9)”），其文档字符串应解释何时停止执行。

#### 使用文档字符串和类型注解

Python 现在支持各种用途的类型注解（有关如何使用它们，请参阅 [Item 124](#ch14#ch14lev1sec9)：“[通过 typing 考虑静态分析以消除错误](#ch14#ch14lev1sec9)”）。它们包含的信息可能与典型的文档字符串冗余。例如，这是 `find_anagrams` 函数签名，应用了类型注解：

[点击此处查看代码图片](#ch14_images#f0586-01)

```
from collections.abc import Container

def find_anagrams(word: str,
dictionary: Container[str]) -> list[str]:
...
```

不再需要在文档字符串中指定 `word` 参数是字符串，因为类型注解已包含该信息。`dictionary` 参数是 `collections.abc.Container` 也是如此。没有必要提及返回值将是列表，因为事实已被清楚地注解。当没有找到字谜时，返回值仍然必须是列表，因此可以推断它将是空的；这不需要在文档字符串中说明。在这里，我写了上面相同的函数签名以及相应缩短的文档字符串：

[点击此处查看代码图片](#ch14_images#f0587-01)

```
def find_anagrams(word: str,
dictionary: Container[str]) -> list[str]:
"""Find all anagrams for a word.

This function only runs as fast as the test for
membership in the 'dictionary' container.

Args:
word: Target word.
dictionary: All known actual words.

Returns:
Anagrams that were found.
"""
...
```

类型注解和文档字符串之间的冗余应同样避免用于实例字段、类属性和方法。最好将类型信息放在一个地方，这样发生偏差的风险就更小。

#### 需牢记事项

* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 使用文档字符串为每个模块、类、方法和函数编写文档。随着代码的变化，请保持其最新。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 对于模块，介绍模块的内容以及所有用户应了解的任何重要类或函数。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 对于类，在 `class` 语句之后的文档字符串中记录行为、重要属性和子类行为。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 对于函数或方法，在 `def` 语句之后的文档字符串中记录每个参数、返回值、抛出的异常和其他行为。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 如果您正在使用类型注解，请从文档字符串中省略该信息，因为在两个地方都包含它会是多余的。

### Item 119: 使用包来组织模块并提供稳定的 API

随着程序代码库规模的增长，重组其结构是很自然的。您会将较大的函数拆分成较小的函数。您会将数据结构重构为辅助类（有关示例，请参阅 [Item 29](#ch04#ch04lev1sec5)：“[组合类而非深度嵌套字典、列表和元组](#ch04#ch04lev1sec5)”）。您会将功能分离到相互依赖的各种模块中。

在某个时候，您会发现自己拥有如此多的模块，以至于需要程序中的另一层来使其易于理解。为此，Python 提供了 _包_。包是包含其他模块的模块。

在大多数情况下，包是通过将一个名为 `__init__.py` 的空文件放入目录来定义的。一旦存在 `__init__.py`，该目录中的任何其他 Python 文件都将可以通过相对于该目录的路径进行导入。例如，假设我的程序中有以下目录结构：

```
main.py
mypackage/__init__.py
mypackage/models.py
mypackage/utils.py
```

要导入 `utils` 模块，我可以使用包含包目录名称的绝对模块名称：

```
# main.py
import mypackage.utils
```

我还可以使用 `from` 子句导入相对于其包含包的子模块名称：

```
# main2.py
from mypackage import utils
```

当我在其他包中嵌套包目录时，此 `import` 语句的点路径模式会继续（例如 `import mypackage.foo.bar` 和 `from mypackage.foo import bar`）。

包提供的功能在 Python 程序中有两个主要目的。

#### 命名空间

包的第一个用途是帮助将模块划分为单独的命名空间。它们使您能够拥有许多具有相同文件名但具有不同且唯一的绝对路径的模块。例如，这是一个导入具有相同文件名 `utils.py` 的两个模块属性的程序：

[点击此处查看代码图片](#ch14_images#f0589-01)

```
# main.py
from analysis.utils import log_base2_bucket
from frontend.utils import stringify

bucket = stringify(log_base2_bucket(33))
```

当包中定义的函数、类或子模块具有相同的名称时，此方法会失败。例如，假设我想使用 `analysis.utils` 和 `frontend.utils` 模块中的 `inspect` 函数。直接导入属性将不起作用，因为第二个 `import` 语句将覆盖当前作用域中 `inspect` 的值。

[点击此处查看代码图片](#ch14_images#f0589-02)

```
# main2.py
from analysis.utils import inspect
from frontend.utils import inspect  # Overwrites!
```

解决方案是使用 `import` 语句的 `as` 子句来重命名当前作用域中导入的任何内容：

[点击此处查看代码图片](#ch14_images#f0589-03)

```
# main3.py
from analysis.utils import inspect as analysis_inspect
from frontend.utils import inspect as frontend_inspect

value = 33
if analysis_inspect(value) == frontend_inspect(value):
print("Inspection equal!")
```

`as` 子句可用于重命名使用 `import` 语句检索的任何内容，包括整个模块。这有助于访问命名空间代码并在使用时使其身份清晰。

避免导入名称冲突的另一种方法是始终通过其最高唯一模块名称访问名称。对于上面的示例，这意味着我将使用基本 `import` 语句而不是 `from` 子句：

[点击此处查看代码图片](#ch14_images#f0589-04)

```
# main4.py
import analysis.utils
import frontend.utils

value = 33
if (analysis.utils.inspect(value) ==
frontend.utils.inspect(value)):
print("Inspection equal!")
```

这种方法使您无需使用 `as` 子句。它还使代码的新读者清楚地知道每个同名函数定义在哪里。

#### 稳定的 API

包在 Python 中的第二个用途是为外部使用者提供严格、稳定的 API。

当您为更广泛的消费编写 API 时，例如开源包（有关示例，请参阅 [Item 116](#ch14#ch14lev1sec1)：“[了解在哪里查找社区构建的模块](#ch14#ch14lev1sec1)”），您将希望提供稳定的功能，这些功能在版本之间不会改变。为确保这种情况发生，隐藏您的内部代码组织不被外部用户访问非常重要。这样，您就可以在不破坏现有用户的情况下重构和改进您包的内部模块。

Python 可以通过使用模块或包的 `__all__` 特殊属性来限制暴露给 API 使用者的表面区域。`__all__` 的值是导出为公共 API 一部分的每个名称的 `list`。当消费代码执行 `from foo import *` 时——有关此内容的详细信息如下——只有 `foo.__all__` 中的属性才会从 `foo` 导入。如果 `foo` 中不存在 `__all__`，则只导入公共属性——那些没有前导下划线的属性（有关该约定的详细信息，请参阅 [Item 55](#ch07#ch07lev1sec8)：“[优先使用公共属性而非私有属性](#ch07#ch07lev1sec8)”）。

例如，假设我想提供一个用于计算运动弹丸之间碰撞的包。在这里，我定义了 `mypackage` 的 `models` 模块来包含弹丸的表示：

[点击此处查看代码图片](#ch14_images#f0590-01)

```
# models.py
__all__ = ["Projectile"]

class Projectile:
def __init__(self, mass, velocity):
self.mass = mass
self.velocity = velocity
```

我还定义了 `mypackage` 中的 `utils` 模块来对 `Projectile` 实例执行操作，例如模拟它们之间的碰撞：

[点击此处查看代码图片](#ch14_images#f0590-02)

```
# utils.py
from .models import Projectile

__all__ = ["simulate_collision"]

def _dot_product(a, b):
...

def simulate_collision(a, b):
...
```

现在我想将此 API 的所有公共部分作为一组属性提供，这些属性在 `mypackage` 模块上可用。这将允许下游使用者始终直接从 `mypackage` 导入，而不是从 `mypackage.models` 或 `mypackage.utils` 导入。这确保了 API 使用者的代码将继续工作，即使 `mypackage` 的内部组织发生更改（例如，如果删除了 `models.py`）。

要使用 Python 包实现此目的，您需要修改 `mypackage` 目录中的 `__init__.py` 文件。此文件实际上是在导入 `mypackage` 模块时成为其内容的。因此，您可以通过限制在 `__init__.py` 中导入的内容来为 `mypackage` 指定显式 API。由于我所有的内部模块都已指定 `__all__`，我可以通过简单地导入内部模块中的所有内容并相应地更新 `__all__` 来公开 `mypackage` 的公共接口：

```
# __init__.py
__all__ = []
from .models import *

__all__ += models.__all__
from .utils import *

__all__ += utils.__all__
```

这是一个直接从 `mypackage` 导入而不是访问内部模块的 API 消费者：

[点击此处查看代码图片](#ch14_images#f0591-02)

```
# api_consumer.py
from mypackage import *

a = Projectile(1.5, 3)
b = Projectile(4, 1.7)
after_a, after_b = simulate_collision(a, b)
```

值得注意的是，像 `mypackage.utils._dot_product` 这样的内部专用函数将无法被 API 消费者在 `mypackage` 上访问，因为它们不在 `__all__` 中。从 `__all__` 中省略它们也意味着它们没有被 `from mypackage import *` 语句导入。内部专用名称被有效地隐藏了。

当提供显式、稳定的 API 很重要时，整个方法效果很好。但是，如果您正在为自己的模块之间的使用编写 API，那么 `__all__` 的功能可能是不必要的，应该避免。包提供的命名空间通常足以让一个程序员团队在维护合理的接口边界的同时，协作处理大量代码。

注意 `import *`

像 `from x import y` 这样的导入语句很清晰，因为 `y` 的来源明确是 `x` 包或模块。像 `from foo import *` 这样的通配符导入也很有用，尤其是在交互式 Python 会话中。但是，通配符使代码更难理解：

* `from foo import *` 向代码的新读者隐藏了名称的来源。如果一个模块有多个 `import *` 语句，读者需要检查所有引用的模块才能弄清楚名称是在哪里定义的。
* 来自 `import *` 语句的名称将覆盖包含模块中的任何冲突名称。这可能导致意外的交互，例如由于您的代码与连续的 `import *` 语句重新分配的名称之间的意外交互而导致的奇怪错误。

最安全的方法是避免在代码中使用 `import *`，并使用 `from x import y` 样式显式导入名称。

#### 需牢记事项

* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 中的包是包含其他模块的模块。包允许您将代码组织到单独的、无冲突的命名空间中，并具有唯一的绝对模块名称。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 简单的包是通过将 `__init__.py` 文件添加到包含其他源文件的目录来定义的。这些文件成为目录包的子模块。包目录也可以包含其他包。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 您可以通过在其 `__all__` 特殊属性中列出其公共可见名称来为模块提供显式 API。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 您可以通过在包的 `__init__.py` 文件中仅导入公共名称或通过使用前导下划线命名内部专用成员来隐藏包的内部实现。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 当在单个团队或单个代码库中进行协作时，为显式 API 使用 `__all__` 可能是不必要的。

### Item 120: 考虑使用模块范围的代码来配置部署环境

部署环境是程序运行的配置。每个程序至少有一个部署环境：_生产环境_。编写程序的根本目的是让它在生产环境中工作并取得某种成果。

编写或修改程序需要能够在您用于开发的计算机上运行它。您的 _开发环境_ 的配置可能与您的生产环境的配置大不相同。例如，您可能正在使用一台小型单板计算机来开发一个旨在运行在巨型超级计算机上的程序。

像 `venv` 这样的工具（请参阅 [Item 117](#ch14#ch14lev1sec2)：“[为隔离和可重现的依赖项使用虚拟环境](#ch14#ch14lev1sec2)”）可以轻松确保所有环境都安装了相同的 Python 包。麻烦在于生产环境通常需要许多难以在开发环境中重现的外部假设。

例如，假设我想在 Web 服务器容器中运行一个程序，并授予它访问数据库的权限。每次我想修改程序的代码时，我都需要运行一个服务器容器，必须正确设置数据库模式，并且我的程序需要访问密码。如果我只想验证程序的一行更改是否正常工作，这是一个非常高的成本。

解决此类问题的最佳方法是在启动时覆盖程序的部分内容，以便根据部署环境提供不同的功能。例如，我可以有两个不同的 `__main__` 文件——一个用于生产，一个用于开发：

```
# dev_main.py
TESTING = True

import db_connection

db = db_connection.Database()

# prod_main.py
TESTING = False

import db_connection

db = db_connection.Database()
```

这两个文件之间的唯一区别是 `TESTING` 常量的值。我的程序中的其他模块可以导入 `__main__` 模块，并使用 `TESTING` 的值来决定它们如何定义自己的属性：

[点击此处查看代码图片](#ch14_images#f0594-01)

```
# db_connection.py
import __main__

class TestingDatabase:
...

class RealDatabase:
...

if __main__.TESTING:
Database = TestingDatabase
else:
Database = RealDatabase
```

这里要注意的关键行为是，在模块范围中运行的代码——不在函数或方法内部——只是普通的 Python 代码（有关详细信息，请参阅 [Item 98](#ch11#ch11lev1sec7)：“[使用动态导入延迟加载模块以减少启动时间](#ch11#ch11lev1sec7)”）。您可以使用模块级别的 `if` 语句来决定模块将如何定义名称。这使得根据您的各种部署环境定制模块变得容易。您可以避免在不需要时重现昂贵的假设，如数据库配置。您可以注入本地或模拟实现，以简化交互式开发，或者您可以使用模拟来编写测试（请参阅 [Item 111](#ch13#ch13lev1sec4)：“[使用模拟来测试具有复杂依赖项的代码](#ch13#ch13lev1sec4)”）。

注意
当您的部署环境配置变得非常复杂时，您应该考虑将其从 Python 常量（如 `TESTING`）移到专用的配置文件中。像 `configparser` 内置模块这样的工具允许您将生产配置与代码分开维护，这是与运营团队协作的关键区别。

模块范围的代码可用于处理外部配置。例如，如果我知道我的程序必须根据其主机平台不同地工作，我可以在模块中定义顶层结构之前检查 `sys` 模块：

[点击此处查看代码图片](#ch14_images#f0594-02)

```
# db_connection.py
import sys

class Win32Database:
...

class PosixDatabase:
...

if sys.platform.startswith("win32"):
Database = Win32Database
else:
Database = PosixDatabase
```

类似地，我可以使用 `os.environ` 中的环境变量来指导我的模块定义，以匹配系统的其他约束和要求。

#### 需牢记事项

* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 程序通常需要在多个部署环境中运行，每个环境都有独特的假设和配置。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 您可以使用模块范围内的普通 Python 语句来定制模块的内容以适应不同的部署环境。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 模块内容可以是任何外部条件的产物，包括通过 `sys` 和 `os` 模块的主机自省。

### Item 121: 定义根 `Exception` 以隔离调用者免受 API 影响

当您定义模块的 API 时，您抛出的异常与您定义的函数和类一样是您接口的一部分（有关原因的示例，请参阅 [Item 32](#ch05#ch05lev1sec3)：“[优先抛出异常而非返回 None](#ch05#ch05lev1sec3)”）。

Python 为语言和标准库提供了一个内置的异常层次结构（有关背景信息，请参阅 [Item 86](#ch10#ch10lev1sec7)：“[理解 Exception 和 BaseException 之间的区别](#ch10#ch10lev1sec7)”）。人们倾向于使用内置异常类型来报告错误，而不是定义自己的新类型。例如，当向我的模块中的函数传递无效参数时，我可以抛出 `ValueError` 异常：

[点击此处查看代码图片](#ch14_images#f0595-02)

```
# my_module.py
def determine_weight(volume, density):
if density <= 0:
raise ValueError("Density must be positive")
...
```

在某些情况下，使用 `ValueError` 是有意义的，但对于 API 来说，定义新的异常层次结构要强大得多。我可以通过在我的模块中提供一个根 `Exception` 类来实现这一点，并让该模块抛出的所有其他异常都继承自根异常：

[点击此处查看代码图片](#ch14_images#f0596-01)

```
# my_module.py
class Error(Exception):
"""Base-class for all exceptions raised by this module."""

class InvalidDensityError(Error):
"""There was a problem with a provided density value."""

class InvalidVolumeError(Error):
"""There was a problem with the provided weight value."""

def determine_weight(volume, density):
if density < 0:
raise InvalidDensityError("Density must be positive")
if volume < 0:
raise InvalidVolumeError("Volume must be positive")
if volume == 0:
density / volume
```

在模块中拥有一个根异常，可以方便 API 的使用者捕获所有故意抛出的异常。例如，这里一个 API 的使用者使用带有 `try`/`except` 语句的函数调用，该语句捕获我的根异常：

[点击此处查看代码图片](#ch14_images#f0596-02)

```
try:
weight = my_module.determine_weight(1, -1)
except my_module.Error:
logging.exception("Unexpected error")

>>>
Unexpected error
Traceback (most recent call last):
File ".../example.py", line 3, in <module>
weight = my_module.determine_weight(1, -1)
File ".../my_module.py", line 10, in determine_weight
raise InvalidDensityError("Density must be positive")
InvalidDensityError: Density must be positive
```

`logging.exception` 函数打印捕获异常的完整堆栈跟踪，以便在此情况下更容易调试。`try`/`except` 还阻止了我的 API 异常传播得太远，从而破坏了调用程序。它将调用代码与我的 API 隔离开来。这种隔离有三个有益的影响。

首先，根异常让调用者了解其 API 用法存在问题。如果调用者正确使用我的 API，他们应该捕获我故意抛出的各种异常。如果他们不处理此类异常，它将一直传播到捕获我的模块根异常的绝缘 `except` 块。该块可以将异常引起 API 消费者的注意，为他们提供添加对遗漏异常类型正确处理的机会：

[点击此处查看代码图片](#ch14_images#f0597-01)

```
try:
weight = my_module.determine_weight(-1, 1)
except my_module.InvalidDensityError:
weight = 0
except my_module.Error:
logging.exception("Bug in the calling code")

>>>
Bug in the calling code
Traceback (most recent call last):
File ".../example.py", line 3, in <module>
weight = my_module.determine_weight(-1, 1)
File ".../my_module.py", line 12, in determine_weight
raise InvalidVolumeError("Volume must be positive")
InvalidVolumeError: Volume must be positive
```

第二个优点是根异常可以帮助查找 API 模块代码中的错误。如果我的代码仅故意抛出我在模块层次结构中定义的异常，那么我的模块抛出的所有其他类型的异常都必须是我未打算抛出的异常。这些是我的 API 代码中的错误。

使用上面的 `try`/`except` 语句不会将 API 消费者与我的 API 模块代码中的错误隔离开来。要做到这一点，调用者需要添加另一个 `except` 块来捕获 Python 的 `Exception` 基类（有关详细信息，请参阅 [Item 85](#ch10#ch10lev1sec6)：“[小心捕获 Exception 类](#ch10#ch10lev1sec6)”）。这允许 API 消费者检测到 API 模块实现中存在需要修复的错误。

此示例的输出包括 `logging.exception` 消息和异常的默认解释器输出，因为它被重新抛出：

[点击此处查看代码图片](#ch14_images#f0597-02)

```
try:
weight = my_module.determine_weight(0, 1)
except my_module.InvalidDensityError:
weight = 0
except my_module.Error:
logging.exception("Bug in the calling code")
except Exception:
logging.exception("Bug in the API code!")
raise  # Re-raise exception to the caller

>>>
Bug in the API code!
Traceback (most recent call last):
File ".../example.py", line 3, in <module>
weight = my_module.determine_weight(0, 1)
File ".../my_module.py", line 14, in determine_weight
density / volume
~~~~~~~~^~~~~~~~
ZeroDivisionError: division by zero
Traceback ...
ZeroDivisionError: division by zero
```

第三个影响是 API 的未来证明。随着时间的推移，我可能希望扩展我的 API 以在某些情况下提供更具体的异常。例如，我可以添加一个 `Exception` 子类来指示提供负密度时的错误条件：

[点击此处查看代码图片](#ch14_images#f0598-02)

```
# my_module.py
...

class NegativeDensityError(InvalidDensityError):
"""A provided density value was negative."""

...

def determine_weight(volume, density):
if density < 0:
raise NegativeDensityError("Density must be positive")
...
```

调用代码将继续像以前一样工作，因为它已经捕获了 `InvalidDensityError` 异常（`NegativeDensityError` 的父类）。将来，调用者可以决定对新类型的异常进行特殊处理，并相应地更改处理行为：

[点击此处查看代码图片](#ch14_images#f0598-03)

```
try:
weight = my_module.determine_weight(1, -1)
except my_module.NegativeDensityError:
raise ValueError("Must supply non-negative density")
except my_module.InvalidDensityError:
weight = 0
except my_module.Error:
logging.exception("Bug in the calling code")
except Exception:
logging.exception("Bug in the API code!")
raise

>>>
Traceback ...
NegativeDensityError: Density must be positive

The above exception was the direct cause of the following
➥ exception:

Traceback ...
ValueError: Must supply non-negative density
```

我可以通过在根异常下方提供更广泛的异常集来进一步进行 API 未来证明。例如，想象一下我有一组与计算权重相关的错误，另一组与计算体积相关的错误，第三组与计算密度相关的错误：

[点击此处查看代码图片](#ch14_images#f0599-02)

```
# my_module.py
class Error(Exception):
"""Base-class for all exceptions raised by this module."""

class WeightError(Error):
"""Base-class for weight calculation errors."""

class VolumeError(Error):
"""Base-class for volume calculation errors."""

class DensityError(Error):
"""Base-class for density calculation errors."""

...
```

特定异常将继承自这些通用异常。每个中间异常都充当其自身的根异常。这使得根据广泛的功能更容易将调用代码层与 API 代码隔离开来。这比让所有调用者捕获一长串非常具体的 `Exception` 子类要好得多。

#### 需牢记事项

* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 当模块定义根异常并仅抛出其子类时，API 消费者有一种简单的方法可以使自己免受模块遇到的意外情况的影响。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 捕获根异常可以帮助您查找使用 API 的代码中的错误。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 捕获 Python `Exception` 基类可以帮助您查找 API 实现中的错误。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 中间根异常允许您将来抛出更具体的异常类型，而不会破坏 API 消费者。

### Item 122: 了解如何打破循环依赖

不可避免地，当您与他人协作时，您会发现模块之间存在相互依赖。即使您自己处理单个程序的各个部分，这种情况也可能发生。

例如，假设我想让我的 GUI 应用程序显示一个对话框来选择保存文档的位置。对话框显示的数据可以通过参数传递给我的事件处理程序。但是对话框还需要读取全局状态，例如用户偏好设置，以了解如何正确渲染。

这里我定义了一个对话框，它从全局偏好设置中检索默认文档保存位置：

[点击此处查看代码图片](#ch14_images#f0600-01)

```
# dialog.py
import app

class Dialog:
def __init__(self, save_dir):
self.save_dir = save_dir

...

save_dialog = Dialog(app.prefs.get("save_dir"))

def show():
...
```

问题在于包含 `prefs` 对象的 `app` 模块也导入了 `dialog` 类，以便在程序启动时显示相同的对话框：

```
# app.py
import dialog

class Prefs:
...
def get(self, name):
...

prefs = Prefs()
dialog.show()
```

这是一个循环依赖。如果我像这样从我的主程序导入 `app` 模块：

```
# main.py
import app
```

我收到一个异常：

[点击此处查看代码图片](#ch14_images#f0601-01)

```
$ python3 main.py
Traceback (most recent call last):
File ".../main.py", line 4, in <module>
import app
File ".../app.py", line 4, in <module>
import dialog
File ".../dialog.py", line 15, in <module>
save_dialog = Dialog(app.prefs.get("save_dir"))
^^^^^
AttributeError: partially initialized module 'app' has no
➥ attribute 'prefs' (most likely due to a circular import)
```

要理解这里发生了什么，您需要了解 Python 的导入机制通常是如何工作的。当导入一个模块时，Python 实际上会做什么，按深度优先顺序（有关完整详细信息，请参阅 <https://docs.python.org/3/library/importlib.html>）：

1. 在 `sys.path` 中的位置搜索模块
2. 加载模块的代码并确保其编译
3. 创建一个对应的空模块对象
4. 将模块插入 `sys.modules`
5. 运行模块对象中的代码以定义其内容

循环依赖的问题在于，模块的属性直到这些属性的代码执行后（步骤 5 之后）才被定义。但是，在模块插入 `sys.modules`（步骤 4 之后）后，可以立即使用 `import` 语句加载该模块。在上面的示例中，`app` 模块在定义任何内容之前导入 `dialog`。然后 `dialog` 模块导入 `app`。由于 `app` 尚未完成运行——它正在导入 `dialog`——`app` 模块是空的（来自步骤 4）。`AttributeError` 异常被抛出（在 `dialog` 的步骤 5 期间），因为定义 `prefs` 的代码尚未运行（即，`app` 的步骤 5 尚未完成）。

解决此问题的最佳方法是重构代码，使 `prefs` 数据结构位于依赖树的底部。然后，`app` 和 `dialog` 都可以导入相同的实用程序模块，并避免任何循环依赖。但是，并非总是可能进行如此清晰的划分，或者重构可能需要太多工作而不值得付出努力。

还有三种打破循环依赖的方法。

#### 重新排序导入

处理循环导入问题的第一种方法是更改导入顺序。例如，如果我在 `app` 模块的底部导入 `dialog` 模块，在 `app` 模块的其他内容运行之后，`AttributeError` 异常就会消失：

```
# app.py
class Prefs:
...

prefs = Prefs()

import dialog  # Moved

dialog.show()
```

这是可行的，因为当 `dialog` 模块稍后加载时，它对 `app` 的递归导入会发现 `app.prefs` 已经被定义（即，`app` 的步骤 5 大部分已完成）。

尽管此解决方案避免了 `AttributeError` 异常，但它违反了 PEP 8 风格指南（请参阅 [Item 2](#ch01#ch01lev1sec2)：“[遵循 PEP 8 风格指南](#ch01#ch01lev1sec2)”）。风格指南建议您始终将导入放在 Python 文件的顶部。这使得代码的新读者能够清楚地了解您模块的依赖关系。它还确保您依赖的任何模块都在作用域内，并且对您模块中的所有代码都可用。

将导入放在文件靠后的位置可能很脆弱，并且可能导致代码顺序的微小更改完全破坏模块。我建议不要使用导入重新排序来解决您的循环依赖问题。

#### 导入、配置、运行

解决循环导入问题的第二种解决方案是让模块在导入时尽量减少副作用。例如，我可以让我的模块仅定义函数、类和常量。我特意避免在导入时运行任何函数。然后，我让每个模块提供一个 `configure` 函数，在所有其他模块完成导入后调用它。`configure` 的目的是通过访问其他模块的属性来准备每个模块的状态。在所有模块导入后（即，当步骤 5 完成时）运行 `configure`，因此所有属性都必须已定义。

这里我重新定义了 `dialog` 模块，使其仅在调用 `configure` 时访问 `prefs` 对象：

[点击此处查看代码图片](#ch14_images#f0603-01)

```
# dialog.py
import app

class Dialog:
...

save_dialog = Dialog()

def show():
...

def configure():
save_dialog.save_dir = app.prefs.get("save_dir")
```

我还重新定义了 `app` 模块，使其在导入时不执行任何活动：

```
# app.py
import dialog

class Prefs:
...

prefs = Prefs()

def configure():
...
```

最后，`main` 模块具有三个不同的执行阶段——导入所有内容，`configure` 所有内容，然后运行第一个活动：

```
# main.py
import app
import dialog

app.configure()
dialog.configure()

dialog.show()
```

这在许多情况下都有效，并支持 _依赖注入_ 等模式（有关类似示例，请参阅 [Item 112](#ch13#ch13lev1sec5)：“[封装依赖项以方便模拟和测试](#ch13#ch13lev1sec5)”）。但有时很难将代码结构化，以便可以进行显式的 `configure` 步骤。在模块中拥有两个不同的阶段也可能使您的代码更难阅读，因为它将对象的定义与其配置分开了。

#### 动态导入

解决循环导入问题的第三种——通常也是最简单——方法是在函数或方法中使用 `import` 语句。这称为 _动态导入_，因为模块导入发生在程序运行时，而不是在程序首次启动和初始化其模块时。

这里我重新定义了 `dialog` 模块以使用动态导入。`dialog.show` 函数在运行时导入 `app` 模块，而不是 `dialog` 模块在初始化时导入 `app`：

[点击此处查看代码图片](#ch14_images#f0604-01)

```
# dialog.py
class Dialog:
...

save_dialog = Dialog()

def show():
import app  # Dynamic import

save_dialog.save_dir = app.prefs.get("save_dir")
...
```

`app` 模块现在可以与原始示例中的相同。它在顶部导入 `dialog` 并在底部调用 `dialog.show`：

```
# app.py
import dialog

class Prefs:
...

prefs = Prefs()
dialog.show()
```

这种方法具有与之前的导入、配置和运行步骤类似的效果。区别在于它不需要对模块的定义和导入方式进行结构性更改。我只是将循环导入推迟到我必须访问另一个模块的那一刻。在那时，我可以很有把握地认为所有其他模块都已初始化（因为对所有模块的步骤 5 都已完成）。

总的来说，最好避免这种动态导入。`import` 语句的成本不可忽略，并且在紧密循环中可能尤其糟糕（有关示例，请参阅 [Item 98](#ch11#ch11lev1sec7)：“[使用动态导入延迟加载模块以减少启动时间](#ch11#ch11lev1sec7)”）。通过延迟执行，动态导入还会导致运行时出现意外故障，例如程序运行很久后出现 `SyntaxError` 异常（有关如何避免这种情况，请参阅 [Item 108](#ch13#ch13lev1sec1)：“[在 TestCase 子类中验证相关行为](#ch13#ch13lev1sec1)”）。但是，这些缺点通常比重构整个程序的替代方案要好。

#### 需牢记事项

* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 循环依赖发生在两个模块在导入时必须相互调用时。它们可能导致您的程序在启动时崩溃。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 打破循环依赖的最佳方法是将相互依赖关系重构到依赖树底部的单独模块中。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 动态导入是打破模块之间循环依赖的最简单解决方案，同时最大限度地减少重构和复杂性。

### Item 123: 考虑使用 `warnings` 来重构和迁移用法

API 随着满足新的需求而变化是很自然的，这些需求满足了以前未预料到的需求。当 API 很小且上下游依赖项很少时，进行此类更改很简单。一个程序员通常可以在一次源代码库提交中更新一个小型 API 及其所有调用者。

但是，随着代码库的增长，API 的调用者数量可能变得非常庞大或分散在各个存储库中，以至于同步进行 API 更改和更新调用者以匹配是不切实际或不可行的。相反，您需要一种方法来通知和鼓励您协作的其他人重构他们的代码，并将他们的 API 用法迁移到最新的形式。

例如，假设我想提供一个模块来计算汽车在给定平均速度和持续时间下行驶的距离。这里我定义了这样一个函数，并假设速度以英里/小时为单位，持续时间以小时为单位：

[点击此处查看代码图片](#ch14_images#f0606-01)

```
def print_distance(speed, duration):
distance = speed * duration
print(f"{distance} miles")

print_distance(5, 2.5)

>>>
12.5 miles
```

想象一下，这非常成功，以至于我很快就积累了对该函数的大量依赖。我协作的其他程序员需要在我们共享的代码库中计算和打印距离。

尽管取得了成功，但此实现容易出错，因为参数的单位是隐式的。例如，如果我想看看子弹在 3 秒内以每秒 1000 米的速度行驶多远，我会得到错误的结果：

```
print_distance(1000, 3)

>>>
3000 miles
```

我可以通过扩展 `print_distance` 的 API 来包含可选的关键字参数来解决此问题（请参阅 [Item 37](#ch05#ch05lev1sec8)：“[使用关键字专用和位置专用参数强制执行清晰性](#ch05#ch05lev1sec8)”），以指定 `speed`、`duration` 的单位以及要打印的计算距离：

[点击此处查看代码图片](#ch14_images#f0606-02)

```
CONVERSIONS = {
"mph": 1.60934 / 3600 * 1000,  # m/s
"hours": 3600,                 # seconds
"miles": 1.60934 * 1000,       # m
"meters": 1,                   # m
"m/s": 1,                      # m/s
"seconds": 1,                  # s
}

def convert(value, units):
rate = CONVERSIONS[units]
return rate * value

def localize(value, units):
rate = CONVERSIONS[units]
return value / rate

def print_distance(
speed,
duration,
*,
speed_units="mph",
time_units="hours",
distance_units="miles",
):
norm_speed = convert(speed, speed_units)
norm_duration = convert(duration, time_units)
norm_distance = norm_speed * norm_distance
distance = localize(norm_distance, distance_units)
print(f"{distance} {distance_units}")
```

现在我可以修改子弹加速调用，并通过单位转换为英里产生准确的结果：

```
print_distance(
1000,
3,
speed_units="meters",
time_units="seconds",
)

>>>
1.8641182099494205 miles
```

对于此函数，要求指定单位似乎是更好的方法。使其明确可以减少错误的可能性，并且对于代码的新读者来说更容易理解。但是，我如何将 API 的所有调用者迁移到始终指定单位？我如何最大限度地减少依赖于 `print_distance` 的任何代码的损坏，同时鼓励调用者尽快采用新的单位参数？

为此，Python 提供了内置的 `warnings` 模块。使用 `warnings` 是一种以编程方式通知其他程序员他们需要修改代码的方法，因为他们依赖的底层库发生了更改。虽然异常主要用于机器的自动错误处理（请参阅 [Item 81](#ch10#ch10lev1sec2)：“[断言内部假设并抛出未满足的期望](#ch10#ch10lev1sec2)”），但警告主要用于人与人之间关于在他们协作中期望什么的沟通。

我可以修改 `print_distance`，当未提供可选关键字参数以指定单位时发出警告。这样，参数可以暂时保持可选，同时为运行依赖程序的 people 提供明确的通知，如果他们不采取行动，他们应该期望将来会发生中断：

[点击此处查看代码图片](#ch14_images#f0608-01)

```
import warnings

def print_distance(
speed,
duration,
*,
speed_units=None,
time_units=None,
distance_units=None,
):
if speed_units is None:
warnings.warn(
"speed_units required",
DeprecationWarning,
)
speed_units = "mph"

if time_units is None:
warnings.warn(
"time_units required",
DeprecationWarning,
)
time_units = "hours"

if distance_units is None:
warnings.warn(
"distance_units required",
DeprecationWarning,
)
distance_units = "miles"

norm_speed = convert(speed, speed_units)
norm_duration = convert(duration, time_units)
norm_distance = norm_speed * norm_distance
distance = localize(norm_distance, distance_units)
print(f"{distance} {distance_units}")
```

我可以通过调用函数并使用与以前相同的参数，并捕获 `warnings` 模块的 `sys.stderr` 输出来验证此代码是否发出警告：

[点击此处查看代码图片](#ch14_images#f0609-02)

```
import contextlib
import io

fake_stderr = io.StringIO()
with contextlib.redirect_stderr(fake_stderr):
print_distance(
1000,
3,
speed_units="meters",
time_units="seconds",
)

print(fake_stderr.getvalue())

>>>
1.8641182099494205 miles
.../example.py:121: DeprecationWarning: distance_units required
warnings.warn(
```

向此函数添加警告需要大量的重复样板代码，这些代码难以阅读和维护。此外，警告消息指示了调用 `warning.warn` 的行，但我真正想指出的是调用 `print_distance` 的位置 _未_ 使用即将需要的关键字参数。

幸运的是，`warnings.warn` 函数支持 `stacklevel` 参数，这使得报告堆栈中作为警告原因的正确位置成为可能。`stacklevel` 还使得编写可以代表其他代码发出警告的函数变得容易，从而减少了样板代码。这里我定义了一个辅助函数，如果可选参数未提供，它会发出警告，然后为它提供一个默认值：

[点击此处查看代码图片](#ch14_images#f0609-03)

```
def require(name, value, default):
if value is not None:
return value
warnings.warn(
f"{name} will be required soon, update your code",
DeprecationWarning,
stacklevel=3,
)
return default

def print_distance(
speed,
duration,
*,
speed_units=None,
time_units=None,
distance_units=None,
):
speed_units = require(
"speed_units",
speed_units,
"mph",
)
time_units = require(
"time_units",
time_units,
"hours",
)
distance_units = require(
"distance_units",
distance_units,
"miles",
)

norm_speed = convert(speed, speed_units)
norm_duration = convert(duration, time_units)
norm_distance = norm_speed * norm_duration
distance = localize(norm_distance, distance_units)
print(f"{distance} {distance_units}")
```

我可以通过检查捕获的输出来验证这是否传播了正确的违规行：

[点击此处查看代码图片](#ch14_images#f0610-02)

```
import contextlib
import io

fake_stderr = io.StringIO()
with contextlib.redirect_stderr(fake_stderr):
print_distance(
1000,
3,
speed_units="meters",
time_units="seconds",
)

print(fake_stderr.getvalue())

>>>
1.8641182099494205 miles
.../example.py:208: DeprecationWarning: distance_units will be
➥required soon, update your code
print_distance(
```

`warnings` 模块还允许您配置遇到警告时应执行的操作。一种选择是将所有警告变成错误，这将警告作为异常抛出，而不是将其打印到 `sys.stderr`：

[点击此处查看代码图片](#ch14_images#f0611-02)

```
warnings.simplefilter("error")
try:
warnings.warn(
"This usage is deprecated",
DeprecationWarning,
)
except DeprecationWarning:
pass  # Expected
```

这种异常抛出行为对于自动化测试特别有用，可以检测上游依赖项中的更改并相应地失败测试。使用此类测试失败是让您协作的人员清楚他们将需要更新代码的好方法。您可以使用 Python 解释器的 `-W error` 命令行参数或 `PYTHONWARNINGS` 环境变量来应用此策略：

[点击此处查看代码图片](#ch14_images#f0611-03)

```
$ python3 -W error example_test.py
Traceback (most recent call last):
File ".../example_test.py", line 6, in <module>
warnings.warn("This might raise an exception!")
UserWarning: This might raise an exception!
```

一旦负责使用已弃用 API 的代码的人员意识到他们需要进行迁移，他们就可以使用 `simplefilter` 和 `filterwarnings` 函数（有关详细信息，请参阅 <https://docs.python.org/3/library/warnings>）告诉警告模块忽略该错误：

[点击此处查看代码图片](#ch14_images#f0611-04)

```
warnings.simplefilter("ignore")
warnings.warn("This will not be printed to stderr")
```

程序部署到生产环境后，让警告导致错误是没有意义的，因为它们可能会在关键时刻导致程序崩溃。相反，更好的方法是将警告复制到 `logging` 内置模块。这里我通过调用 `logging.captureWarnings` 函数并配置相应的 `"py.warnings"` 日志记录器来实现这一点：

[点击此处查看代码图片](#ch14_images#f0612-01)

```
import logging

fake_stderr = io.StringIO()
handler = logging.StreamHandler(fake_stderr)
formatter = logging.Formatter(
"%(asctime)-15s WARNING] %(message)s")
handler.setFormatter(formatter)

logging.captureWarnings(True)
logger = logging.getLogger("py.warnings")
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

warnings.resetwarnings()
warnings.simplefilter("default")
warnings.warn("This will go to the logs output")

print(fake_stderr.getvalue())

>>>
2019-06-11 19:48:19,132 WARNING] .../example.py:227:
➥UserWarning: This will go to the logs output
warnings.warn("This will go to the logs output")
```

使用日志记录来捕获警告可确保我的程序已有的任何错误报告系统也将收到生产中重要警告的通知。如果我的测试没有涵盖程序在实际使用中可能遇到的所有边缘情况，这一点尤其有用。

API 库维护者还应编写单元测试来验证警告是否在正确的情况下生成，并带有清晰且可操作的消息（请参阅 [Item 108](#ch13#ch13lev1sec1)：“[在 TestCase 子类中验证相关行为](#ch13#ch13lev1sec1)”）。这里我使用 `warnings.catch_warnings` 函数作为上下文管理器（有关背景信息，请参阅 [Item 82](#ch10#ch10lev1sec3)：“[考虑使用 contextlib 和 with 语句实现可重用的 try/finally 行为](#ch10#ch10lev1sec3)”）来包装对上面定义的 `require` 函数的调用：

[点击此处查看代码图片](#ch14_images#f0612-02)

```
with warnings.catch_warnings(record=True) as found_warnings:
found = require("my_arg", None, "fake units")
expected = "fake units"
assert found == expected
```

一旦我收集了警告消息，我就可以验证它们的数量、详细消息和类别是否符合我的预期：

[点击此处查看代码图片](#ch14_images#f0613-02)

```
assert len(found_warnings) == 1
single_warning = found_warnings[0]
assert str(single_warning.message) == (
"my_arg will be required soon, update your code"
)
assert single_warning.category == DeprecationWarning
```

#### 需牢记事项

* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) `warnings` 模块可用于通知您的 API 的调用者有关已弃用的用法。警告消息鼓励这些调用者在将来的更改破坏他们的程序之前修复他们的代码。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 通过使用 Python 解释器的 `-W error` 命令行参数将警告作为错误引发。这在自动化测试中尤其有用，可以捕获依赖项的潜在回归。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 在生产环境中，您可以将警告复制到 `logging` 模块，以确保您现有的错误报告系统将在运行时捕获警告。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 编写测试以验证您的代码生成的警告很有用，以确保它们将在任何下游依赖项的正确时间触发。

### Item 124: 通过 `typing` 考虑静态分析以消除错误

提供文档是帮助 API 用户了解如何正确使用它的好方法（请参阅 [Item 118](#ch14#ch14lev1sec3)：“[为每个函数、类和模块编写文档字符串](#ch14#ch14lev1sec3)”），但通常还不够，不正确的用法仍然会导致错误。理想情况下，应该有一种编程机制来验证调用者是否正确使用您的 API，以及您是否也正确使用了您的下游依赖项。许多编程语言通过编译时类型检查来解决这一需求的一部分，这可以识别和消除某些类别的错误。

历史上，Python 侧重于动态特性，并且没有提供任何形式的编译时类型安全（请参阅 [Item 3](#ch01#ch01lev1sec3)：“[切勿期望 Python 在编译时检测错误](#ch01#ch01lev1sec3)”）。然而，最近 Python 引入了特殊语法和内置的 `typing` 模块，允许您使用类型信息注解变量、类字段、函数和方法。这些 _类型提示_ 支持 _渐进式类型化_，这意味着代码库可以根据需要逐步更新以指定类型。

为 Python 程序添加类型信息的优势在于，您可以运行 _静态分析_ 工具来解析程序的源代码并识别最有可能发生错误的地点。`typing` 内置模块本身并不实现任何类型检查功能。它仅提供一个用于定义可应用于 Python 代码并由单独工具使用的类型的通用库。

就像有多种不同的 Python 解释器实现一样（例如，CPython、PyPy；请参阅 [Item 1](#ch01#ch01lev1sec1)：“[了解您正在使用哪个 Python 版本](#ch01#ch01lev1sec1)”），有多种 Python 静态分析工具实现使用 `typing`。截至本文撰写之时，最流行的工具是 `mypy` (<https://github.com/python/mypy>)、`pyright` (<https://github.com/microsoft/pyright>)、`pyre` (<https://pyre-check.org>) 和 `pytype` (<https://github.com/google/pytype>)。对于本书中的 `typing` 示例，我使用了带有 `--strict` 标志的 `mypy`，它启用了该工具支持的所有各种警告。以下是运行命令行示例：

[点击此处查看代码图片](#ch14_images#f0614-01)

```
$ python3 -m mypy --strict example.py
```

这些工具可以在程序运行之前检测大量常见错误，这可以提供额外的安全层，除了拥有良好的测试（请参阅 [Item 109](#ch13#ch13lev1sec2)：“[优先集成测试而非单元测试](#ch13#ch13lev1sec2)”）。例如，您能找到导致此简单函数编译正常但运行时抛出异常的错误吗？

[点击此处查看代码图片](#ch14_images#f0614-02)

```
def subtract(a, b):
return a - b

subtract(10, "5")

>>>
Traceback ...
TypeError: unsupported operand type(s) for -: 'int' and 'str'
```

参数和变量类型注解用冒号分隔（例如 `name: type`）。返回值类型使用 `-> type` 指定，位于参数列表之后。使用此类类型注解和 `mypy`，我可以轻松发现错误：

[点击此处查看代码图片](#ch14_images#f0614-03)

```
def subtract(a: int, b: int) -> int:  # Function annotation
return a - b

subtract(10, "5")  # Oops: passed string value

$ python3 -m mypy --strict example.py
.../example.py:4: error: Argument 2 to "subtract" has
➥incompatible type "str"; expected "int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```

类型注解也可以应用于类。例如，这个类中有两个错误，运行程序时会抛出异常：

```
class Counter:
def __init__(self):
self.value = 0

def add(self, offset):
value += offset

def get(self) -> int:
self.value
```

第一个错误发生在调用 `add` 方法时：

[点击此处查看代码图片](#ch14_images#f0615-02)

```
counter = Counter()
counter.add(5)

>>>
Traceback ...
UnboundLocalError: cannot access local variable 'value' where
➥it is not associated with a value
```

第二个错误发生在调用 `get` 时：

```
counter = Counter()
found = counter.get()
assert found == 0, found

>>>
Traceback ...
AssertionError: None
```

这两个问题都可以通过 `mypy` 轻松提前发现：

[点击此处查看代码图片](#ch14_images#f0615-03)

```
class Counter:
def __init__(self) -> None:
self.value: int = 0  # Field / variable annotation

def add(self, offset: int) -> None:
value += offset      # Oops: forgot "self."

def get(self) -> int:
self.value           # Oops: forgot "return"

counter = Counter()
counter.add(5)
counter.add(3)
assert counter.get() == 8

$ python3 -m mypy --strict example.py
.../example.py:9: error: Name "value" is not defined
➥[name-defined]
.../example.py:11: error: Missing return statement  [return]
Found 2 errors in 1 file (checked 1 source file)
```

Python 动态性的一个优势是能够编写操作鸭子类型的通用功能（请参阅 [Item 25](#ch04#ch04lev1sec1)：“[谨慎依赖字典插入顺序](#ch04#ch04lev1sec1)” 和 [Item 57](#ch07#ch07lev1sec10)：“[继承 collections.abc 类以创建自定义容器类型](#ch07#ch07lev1sec10)”）。这使得一个实现可以接受多种类型，从而节省了大量重复工作并简化了测试。这里我定义了一个这样的通用函数，用于将列表中的值组合在一起，但最后一行上的 `assert` 语句由于一个不明显的原因而失败：

[点击此处查看代码图片](#ch14_images#f0616-02)

```
def combine(func, values):
assert len(values) > 0

result = values[0]
for next_value in values[1:]:
result = func(result, next_value)

return result

def add(x, y):
return x + y

inputs = [1, 2, 3, 4j]
result = combine(add, inputs)
assert result == 10, result  # Fails

>>>
Traceback ...
AssertionError: (6+4j)
```

我可以使用 `typing` 模块对泛型的支持来注解此函数并静态检测问题：

[点击此处查看代码图片](#ch14_images#f0616-03)

```
from collections.abc import Callable
from typing import TypeVar

Value = TypeVar("Value")
Func = Callable[[Value, Value], Value]

def combine(func: Func[Value], values: list[Value]) -> Value:
assert len(values) > 0

result = values[0]
for next_value in values[1:]:
result = func(result, next_value)

return result

Real = TypeVar("Real", int, float)

def add(x: Real, y: Real) -> Real:
return x + y

inputs = [1, 2, 3, 4j]  # Oops: included a complex number
result = combine(add, inputs)
assert result == 10

$ python3 -m mypy --strict example.py
.../example.py:22: error: Argument 1 to "combine" has
➥incompatible type "Callable[[Real, Real], Real]"; expected
➥"Callable[[complex, complex], complex]"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```

另一个非常常见的错误是 `None` 值出现在您认为会有有效对象的地方（请参阅 [Item 32](#ch05#ch05lev1sec3)：“[优先抛出异常而非返回 None](#ch05#ch05lev1sec3)”）。这个问题会影响看似简单的代码，例如下面的片段，其中最后一个 `assert` 语句失败：

[点击此处查看代码图片](#ch14_images#f0617-02)

```
def get_or_default(value, default):
if value is not None:
return value
return value

found = get_or_default(3, 5)
assert found == 3

found = get_or_default(None, 5)
assert found == 5, found  # Fails

>>>
Traceback ...
AssertionError: None
```

`typing` 模块支持 _可选类型_——用 `type | None` 表示——它确保程序仅在执行了适当的 null 检查后才与值进行交互。这使得 `mypy` 可以推断此代码中存在错误。返回语句中使用的类型必须是 `None`，这与函数签名所需的 `int` 类型不匹配：

[点击此处查看代码图片](#ch14_images#f0618-01)

```
def get_or_default(value: int | None, default: int) -> int:
if value is not None:
return value
return value  # Oops: should have returned "default"

$ python3 -m mypy --strict example.py
.../example.py:4: error: Incompatible return value type
➥ (got "None", expected "int")  [return-value]
Found 1 error in 1 file (checked 1 source file)
```

`typing` 模块中提供了各种其他选项。（有关所有详细信息，请参阅 <https://docs.python.org/3/library/typing.html>。）值得注意的是，不包括异常。与 Java 不同，Java 有受检查的异常，这些异常在每个方法的 API 边界强制执行，Python 的类型注解更类似于 C#：异常不被视为接口定义的一部分。因此，如果您想验证您是否正确地抛出和捕获异常，您需要编写测试。

使用 `typing` 模块时一个常见的陷阱是处理前向引用（有关类似问题，请参阅 [Item 122](#ch14#ch14lev1sec7)：“[了解如何打破循环依赖](#ch14#ch14lev1sec7)”）。例如，假设我有两个类，其中一个类持有一个对另一个类的引用。通常，这些类的定义顺序无关紧要，因为它们都将在稍后创建它们的实例之前被定义：

[点击此处查看代码图片](#ch14_images#f0618-02)

```
class FirstClass:
def __init__(self, value):
self.value = value

class SecondClass:
def __init__(self, value):
self.value = value

second = SecondClass(5)
first = FirstClass(second)
```

如果您将类型提示应用于此程序并运行 `mypy`，它将显示没有问题：

[点击此处查看代码图片](#ch14_images#f0619-01)

```
class FirstClass:
def __init__(self, value: SecondClass) -> None:
self.value = value

class SecondClass:
def __init__(self, value: int) -> None:
self.value = value

second = SecondClass(5)
first = FirstClass(second)

$ python3 -m mypy --strict example.py
Success: no issues found in 1 source file
```

但是，如果您尝试运行此代码，它会失败，因为 `SecondClass` 在 `FirstClass.__init__` 方法的参数中的类型注解中被引用，而它尚未被定义：

[点击此处查看代码图片](#ch14_images#f0619-02)

```
class FirstClass:
def __init__(self, value: SecondClass) -> None:  # Breaks
self.value = value

class SecondClass:
def __init__(self, value: int) -> None:
self.value = value

second = SecondClass(5)
first = FirstClass(second)

>>>
Traceback ...
NameError: name 'SecondClass' is not defined
```

这些静态分析工具支持的推荐的解决方法是使用字符串作为包含前向引用的类型注解。字符串值稍后会被解析和评估，以提取要检查的类型信息：

[点击此处查看代码图片](#ch14_images#f0619-03)

```
class FirstClass:
def __init__(self, value: "SecondClass") -> None:  # OK
self.value = value

class SecondClass:
def __init__(self, value: int) -> None:
self.value = value

second = SecondClass(5)
first = FirstClass(second)
```

现在您已经了解了如何使用类型提示及其潜在好处，重要的是要考虑何时使用它们。以下是一些需要牢记的最佳实践：

* 在编写新代码时从一开始就尝试使用类型注解会减慢您的速度。一个通用的策略是先编写一个没有注解的版本，然后编写测试，然后将类型信息添加到最有价值的地方。
* 类型提示在代码库的边界处最为重要，例如您提供的许多调用者（以及因此其他人）依赖的 API。类型提示是对测试（请参阅 [Item 108](#ch13#ch13lev1sec1)：“[在 TestCase 子类中验证相关行为](#ch13#ch13lev1sec1)”）和警告（请参阅 [Item 123](#ch14#ch14lev1sec8)：“[考虑使用 warnings 来重构和迁移用法](#ch14#ch14lev1sec8)”）的补充，以确保您的 API 调用者不会因您的更改而感到惊讶或损坏。
* 将类型提示应用于代码库中最复杂且最容易出错的部分（不属于 API 的部分）可能很有用。但是，为类型注解争取 100% 的覆盖率可能不值得，因为您会很快遇到收益递减。
* 如果可能，您应该将静态分析包含在您的自动化构建和测试系统的一部分，以确保您代码库中的每个提交都经过错误检查。此外，用于类型检查的配置应维护在存储库中，以确保您协作的所有人都使用相同的规则。
* 在添加类型信息时运行类型检查器很重要。如果您不这样做，您可能会几乎完成在所有地方添加类型提示，然后遇到类型检查工具的大量错误，这可能会令人沮丧，并让您想要完全放弃类型提示。

最后，重要的是要认识到在许多情况下，您可能不需要或不想使用类型注解。对于中小型程序、临时代码、遗留代码库和原型，类型提示可能比它们应有的价值需要更多的努力。

#### 需牢记事项

* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 有特殊语法和 `typing` 内置模块，用于使用类型信息注解变量、字段、函数和方法。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 静态类型检查器可以利用此类型信息来帮助您避免许多否则会在运行时发生的常见错误。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 有各种最佳实践可用于在程序中采用类型、在 API 中使用它们，并确保它们不会妨碍您的生产力。

### Item 125: 打包 Python 程序时，优先选择开源项目而非 `zipimport` 和 `zipapp`

想象一下，您已经完成了使用 `flask` 开源项目在 Python 中构建 Web 应用程序，现在是时候将其交付给生产环境供实际用户使用了（有关背景信息，请参阅 [Item 120](#ch14#ch14lev1sec5)：“[考虑使用模块范围的代码来配置部署环境](#ch14#ch14lev1sec5)”）。有多种选项可用于使用包管理器执行此操作（请参阅 [Item 116](#ch14#ch14lev1sec1)：“[了解在哪里查找社区构建的模块](#ch14#ch14lev1sec1)”）。但是，一种通常更简单的方法是将源代码和依赖项复制到服务器（或容器镜像）中。

为此，我将我的应用程序及其所有相关模块打包到一个目录中——类似于 `pip` 等工具创建的 `site-packages` 目录（请参阅 [Item 117](#ch14#ch14lev1sec2)：“[为隔离和可重现的依赖项使用虚拟环境](#ch14#ch14lev1sec2)”）：

```
$ ls flask_deps
Jinja2-3.1.3.dist-info
MarkupSafe-2.1.5.dist-info
blinker
blinker-1.7.0.dist-info
click
click-8.1.7.dist-info
flask
flask-3.0.2.dist-info
itsdangerous
itsdangerous-2.1.2.dist-info
jinja2
markupsafe
myapp.py
werkzeug
werkzeug-3.0.1.dist-info
```

这些依赖项包括超过 330 个文件和 56,000 行源代码，未压缩大小为 5.1 MB。将如此多相对较小的文件复制到另一台服务器可能会非常缓慢。此类传输还可能意外更改重要细节，如文件权限。过去，一种常见的解决方法是将代码库归档到 zip 文件中，然后再进行部署。

为了使此类存档更容易处理，Python 提供了 `zipimport` 内置模块。它允许程序在 `PYTHONPATH` 环境变量或 `sys.path` 列表中出现的 zip 文件中即时解压缩和加载。这里我创建了一个 `flask_deps` 目录的 zip 存档，然后验证它在直接从 zip 文件执行时是否正常工作：

[点击此处查看代码图片](#ch14_images#f0622-01)

```
$ cd flask_deps
$ zip -r ../flask_deps.zip *
$ cd ..
$ PYTHONPATH=flask_deps.zip python3 -m flask --app=myapp routes
Endpoint     Methods  Rule
-----------  -------  -----------------------
hello_world  GET      /
static       GET      /static/<path:filename>
```

您可能会期望从 zip 文件加载 Python 模块会因解压缩的 CPU 开销而产生性能损失。这里我测量了从 zip 存档加载的启动时间：

[点击此处查看代码图片](#ch14_images#f0622-02)

```
$ time PYTHONPATH=flask_deps.zip python3 -m flask --app=myapp
➥routes
...
real    0m0.123s
user    0m0.097s
sys     0m0.022s
```

这里我测量了从磁盘上的普通文件加载的启动时间：

[点击此处查看代码图片](#ch14_images#f0622-03)

```
$ time PYTHONPATH=flask_deps python3 -m flask --app=myapp
➥routes
Endpoint     Methods  Rule
-----------  -------  -----------------------
hello_world  GET      /
static       GET      /static/<path:filename>

real    0m0.126s
user    0m0.098s
sys     0m0.023s
```

性能几乎相同。这有两个主要原因。首先，现代计算机的处理能力与其 I/O 容量和内存带宽相比非常强大，因此额外的解压缩造成的减慢通常可以忽略不计。其次，大型文件系统缓存和 SSD（固态硬盘）性能几乎可以隐藏相对少量数据的 I/O 延迟（有关详细信息，请参阅 [Item 97](#ch11#ch11lev1sec6)：“[依赖预编译字节码和文件系统缓存来提高启动时间](#ch11#ch11lev1sec6)”）。尽管 `flask_deps.zip` 文件为 1.6 MB，而未压缩目录大小为 5.1 MB，但性能差异实际上为零。

一个结论可能是您应该始终将 Python 程序压缩到 zip 文件中，因为似乎没有任何缺点。Python 甚至提供了 `zipapp` 内置模块，用于快速归档整个应用程序，因为这个好处。这里我使用此工具为我之前的 Django Web 应用程序创建了一个压缩的、单文件可执行文件（带有 `.pyz` 后缀），该文件易于复制和交互：

[点击此处查看代码图片](#ch14_images#f0623-01)

```
$ python -m zipapp flask_deps -m "flask.__main__:main" -p
➥'/usr/bin/env python3' -c
$ ./flask_deps.pyz --app myapp routes
Endpoint     Methods  Rule
-----------  -------  -----------------------
hello_world  GET      /
static       GET      /static/<path:filename>
```

不幸的是，从 zip 文件执行 Python 代码会导致实际程序在两个方面中断：数据文件访问和扩展模块。

作为第一个问题的示例，这里我创建了一个 Django Web 框架的 zip 存档，并尝试运行一个依赖于它的 Web 应用程序：

[点击此处查看代码图片](#ch14_images#f0623-02)

```
$ python3 -m compileall django
$ zip -r django.zip Django-5.0.3.dist-info django
$ rm -R Django-5.0.3.dist-info django
$ PYTHONPATH=django.zip python3 django_project/manage.py check
Traceback (most recent call last):
...
OSError: No translation files found for default language en-us.
```

这不起作用，因为 Django 正在查找位于源代码文件旁边的翻译数据文件。在下面的 Django 代码片段中，`localedir` 变量的值是 `".../django.zip/django/conf/locale"`，它不是文件系统上的目录。当该路径传递给 `gettext` 模块加载翻译时，Django 库代码找不到文件，导致上述 `OSError` 异常：

[点击此处查看代码图片](#ch14_images#f0624-01)

```
# trans_real.py
# Copyright (c) Django Software Foundation and
# individual contributors. All rights reserved.
class DjangoTranslation(gettext_module.GNUTranslations):
...

def _init_translation_catalog(self):
settingsfile = \    sys.modules[settings.__module__].__file__
localedir = os.path.join(
os.path.dirname(settingsfile),
"locale",
)
translation = self._new_gnu_trans(localedir)
self.merge(translation)

...
```

Python 提供了 `pkgutil` 内置模块来解决此问题。它智能地检查模块以确定如何正确访问其数据资源，即使它们在 zip 存档中或需要自定义模块加载器。这里我使用 `pkgutil` 来加载 Django 因 zip 存档而找不到的翻译文件：

[点击此处查看代码图片](#ch14_images#f0624-02)

```
# django_pkgutil.py
import pkgutil

data = pkgutil.get_data(
"django.conf.locale",
"en/LC_MESSAGES/django.po",
)
print(data.decode("utf-8"))

>>>
# This file is distributed under the same license as the Django
➥ package.
#
msgid ""
msgstr ""
"Project-Id-Version: Django\n"
"Report-Msgid-Bugs-To: \n"
...
```

很少有项目实际使用 `pkgutil`；即使是像 Django 这样非常受欢迎的项目也不使用它。Python 程序最常作为文件在磁盘上执行，并保留其原始目录结构。相比之下，其他语言将程序编译成一个可执行文件，该文件放置在一个单独的构建工件目录中，远离代码。这导致程序员假设他们无法访问源树，并且需要更显式地处理数据依赖项。但是，对于 Python 代码，假设代码就在附近，因此源树中的数据文件也必须就在附近。不要期望从 zip 存档导入的常见包能够正常工作。

第二个问题是，由于操作系统限制，您无法从 zip 存档导入本机扩展模块（请参阅 [Item 96](#ch11#ch11lev1sec5)：“[考虑使用扩展模块以最大化性能和人体工程学](#ch11#ch11lev1sec5)”）。这里我展示了 NumPy 包如何因此而中断：

[点击此处查看代码图片](#ch14_images#f0625-01)

```
$ zip -r ./numpy.zip numpy numpy-1.26.4.dist-info
$ rm -R numpy numpy-1.26.4.dist-info
$ PYTHONPATH=numpy.zip python -c 'import numpy'
Traceback (most recent call last):
...
ModuleNotFoundError: No module named
➥'numpy.core._multiarray_umath'

During handling of the above exception, another exception
➥ occurred:

Traceback (most recent call last):
...
ImportError:

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS
➥ ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.
...
```

扩展模块非常有价值和受欢迎，因为它们有助于 Python 在 CPU 密集型任务上运行得更快（请参阅 [Item 96](#ch11#ch11lev1sec5)：“[考虑使用扩展模块以最大化性能和人体工程学](#ch11#ch11lev1sec5)”）。这最终是 `zipimport` 和 `zipapps` 的最大障碍。

幸运的是，Python 社区已经构建了各种开源解决方案，它们在部署 Python 应用程序方面表现更好。Pex 工具 (<https://github.com/pex-tool/pex>) 和衍生项目 Shiv (<https://github.com/linkedin/shiv>) 提供与 `zipapp` 类似的功能，但这些工具会自动解决数据文件和本机模块的问题。例如，这里我使用 Pex 为前面提到的同一个 Django Web 应用程序创建了一个单一的可执行文件——而且这个实际上是有效的：

[点击此处查看代码图片](#ch14_images#f0626-01)

```
$ pip install -e django_project
$ pex django_project -o myapp.pex
$ ./django_project.pex -m manage check
System check identified no issues (0 silenced).
```

另一个选择是 PyInstaller (<https://pyinstaller.org>)，它更进一步，通过捆绑 Python 可执行文件本身，这样用户就不需要安装任何其他东西就可以运行应用程序。无论您选择哪种方式，请务必仔细阅读文档，并通过实验验证它与您需要使用的模块及其对执行环境的假设兼容。

#### 需牢记事项

* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) Python 能够直接从 zip 存档加载模块，这使得将整个应用程序部署为单个文件更加容易。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 许多常见的开源 Python 包在从 zip 存档导入时会因依赖数据文件和扩展模块而中断。
* ![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/sq-s_e5535f29.jpg) 社区已经构建了 Python 内置 `zipapp` 模块的替代方案，例如 Pex，它们提供了 zip 存档的部署优势，而没有缺点。
---
<a role="toc_link" id="index"></a>

## Effective Python - Index

## 索引

### 符号

*   `|` 管道操作符, [36](#ch01#page_36)
*   `+` 操作符, [43](#ch02#page_43)
*   `--version` 标志, [1](#ch01#page_1)
*   `%` 操作符, [44](#ch02#page_44), [50](#ch02#page_50)
*   `*` 操作符, [151](#ch05#page_151)–[152](#ch05#page_152)
*   `**` 操作符, [153](#ch05#page_153)–[154](#ch05#page_154)
*   `@` 符号, [167](#ch05#page_167)
*   `_asdict` 方法, [226](#ch07#page_226)
*   `_astuple` 方法, [225](#ch07#page_225), [227](#ch07#page_227), [228](#ch07#page_228)–[229](#ch07#page_229)
*   `__call__` 方法, [204](#ch07#page_204)–[205](#ch07#page_205)
*   `__debug__` 变量, [443](#ch10#page_443)–[444](#ch10#page_444)
*   `__delattr__` 方法, [252](#ch07#page_252)
*   `__dict__`, [306](#ch08#page_306)–[310](#ch08#page_310)
*   `__eq__` 方法, [226](#ch07#page_226)
*   `__getattr__` 方法, [279](#ch08#page_279)–[281](#ch08#page_281)
*   `__getattribute__` 方法, [281](#ch08#page_281)–[283](#ch08#page_283)
*   `__getitem__` 方法, [261](#ch07#page_261)–[263](#ch07#page_263)
*   `__hash__` 方法, [258](#ch07#page_258)
*   `__init__` 方法, [217](#ch07#page_217)–[219](#ch07#page_219), [235](#ch07#page_235)–[236](#ch07#page_236)
*   `__init_subclass__` 方法, [288](#ch08#page_288)–[299](#ch08#page_299), [306](#ch08#page_306)–[310](#ch08#page_310)
*   `__missing__` 方法, [124](#ch04#page_124)–[127](#ch04#page_127)
*   `@property` 装饰器
*   与重构属性的对比, [270](#ch08#page_270)–[274](#ch08#page_274)
*   重用, [274](#ch08#page_274)–[279](#ch08#page_279)
*   setter 和 getter, [266](#ch08#page_266)–[269](#ch08#page_269)
*   `_replace` 方法, [255](#ch07#page_255)
*   `__repr__` 方法, [223](#ch07#page_223)–[224](#ch07#page_224)
*   `__set_name__` 方法, [278](#ch08#page_278), [302](#ch08#page_302)–[303](#ch08#page_303)
*   `__setattr__` 方法, [252](#ch07#page_252), [283](#ch08#page_283)–[285](#ch08#page_285)

### A

*   `accumulate` 函数, [106](#ch03#page_106)–[107](#ch03#page_107)
*   `adjust` 模块, [479](#ch11#page_479)–[482](#ch11#page_482)
*   高级字符串格式化, [52](#ch02#page_52)–[55](#ch02#page_55)
*   算法, [493](#ch12#page_493)
*   二分查找, [502](#ch12#page_502)–[503](#ch12#page_503)
*   leaky-bucket, [270](#ch08#page_270)–[273](#ch08#page_273)
*   别名, [136](#ch05#page_136)
*   `all` 函数, [98](#ch03#page_98)–[100](#ch03#page_100)
*   `animate` 函数, [187](#ch06#page_187)
*   动画生成器, [186](#ch06#page_186)–[188](#ch06#page_188)
*   `any` 函数, [100](#ch03#page_100)–[101](#ch03#page_101)
*   API
*   异常, [595](#ch14#page_595)
*   hooks, [201](#ch07#page_201)–[203](#ch07#page_203)
*   Python, [468](#ch11#page_468), [471](#ch11#page_471)–[472](#ch11#page_472)
*   Python C 扩展, [460](#ch11#page_460), [465](#ch11#page_465)
*   稳定性, [590](#ch14#page_590)–[592](#ch14#page_592)
*   `append` 方法, [182](#ch06#page_182), [506](#ch12#page_506)
*   `argparse` 模块, [479](#ch11#page_479)–[481](#ch11#page_481)
*   参数
*   函数, [111](#ch04#page_111)–[112](#ch04#page_112), [135](#ch05#page_135)–[137](#ch05#page_137)
*   迭代参数, [87](#ch03#page_87)–[92](#ch03#page_92)
*   关键字参数, [153](#ch05#page_153)–[157](#ch05#page_157), [161](#ch05#page_161)–[162](#ch05#page_162), [219](#ch07#page_219)–[221](#ch07#page_221)
*   仅关键字参数, [162](#ch05#page_162)–[164](#ch05#page_164)
*   `None` 作为默认值, [157](#ch05#page_157)–[160](#ch05#page_160)
*   按引用传递, [251](#ch07#page_251)
*   位置参数, [150](#ch05#page_150)–[152](#ch05#page_152)
*   仅位置参数, [164](#ch05#page_164)–[166](#ch05#page_166)
*   `asdict` 函数, [226](#ch07#page_226)
*   `assert` 语句, [404](#ch10#page_404)–[408](#ch10#page_408), [442](#ch10#page_442)–[443](#ch10#page_443)
*   `assertAlmostEqual` 方法, [564](#ch13#page_564)–[565](#ch13#page_565)
*   `assertNotAlmostEqual` 方法, [565](#ch13#page_565)
*   赋值表达式, [22](#ch01#page_22)–[23](#ch01#page_23), [24](#ch01#page_24)–[30](#ch01#page_30), [86](#ch03#page_86)
*   异常, [180](#ch06#page_180)
*   在列表推导式中, [178](#ch06#page_178)–[181](#ch06#page_181)
*   切片, [68](#ch02#page_68)–[69](#ch02#page_69)
*   AST (抽象语法树), [205](#ch07#page_205)–[206](#ch07#page_206), [208](#ch07#page_208)–[210](#ch07#page_210)
*   异步协程, [319](#ch09#page_319)
*   异步 I/O, [368](#ch09#page_368), [376](#ch09#page_376)
*   `asyncio` 模块, [329](#ch09#page_329), [366](#ch09#page_366)–[367](#ch09#page_367), [368](#ch09#page_368)–[384](#ch09#page_384). _参见_ [协程](#index#idx115)
*   事件循环, [389](#ch09#page_389)–[392](#ch09#page_392)
*   线程/协程互操作性, [381](#ch09#page_381)–[384](#ch09#page_384)
*   属性, [306](#ch08#page_306)
*   注解, [299](#ch08#page_299)–[303](#ch08#page_303)
*   描述符协议, [274](#ch08#page_274). _参见_ [描述符](#index#idx140)
*   建立属性间的关系, [303](#ch08#page_303)–[310](#ch08#page_310)
*   惰性属性, [279](#ch08#page_279)–[285](#ch08#page_285)
*   修改属性, [299](#ch08#page_299)–[303](#ch08#page_303)
*   保护属性, [247](#ch07#page_247)–[250](#ch07#page_250)
*   公共属性, [245](#ch07#page_245)–[250](#ch07#page_250), [266](#ch08#page_266)–[269](#ch08#page_269)
*   更新值, [254](#ch07#page_254)–[256](#ch07#page_256)
*   自动格式化, black, [5](#ch01#page_5)–[6](#ch01#page_6)

### B

*   `BaseException` 类, [419](#ch10#page_419)–[424](#ch10#page_424)
*   `batched` 函数, [105](#ch03#page_105)–[106](#ch03#page_106)
*   二元运算符, [44](#ch02#page_44)
*   二分查找算法, bisect 模块, [502](#ch12#page_502)–[503](#ch12#page_503)
*   二进制到 Unicode 转换, [42](#ch02#page_42)
*   `bisect` 模块, [501](#ch12#page_501)–[503](#ch12#page_503)
*   `black`, [5](#ch01#page_5)–[6](#ch01#page_6)
*   阻塞 I/O, [324](#ch09#page_324)–[329](#ch09#page_329), [348](#ch09#page_348), [348](#ch09#page_348)–[349](#ch09#page_349). _参见_ [协程](#index#idx115)
*   块, [399](#ch10#page_399)
*   else 块, [82](#ch03#page_82)–[84](#ch03#page_84)
*   try 块, [412](#ch10#page_412)–[414](#ch10#page_414)
*   try/except/else 块, [400](#ch10#page_400)–[402](#ch10#page_402)
*   try/except/else/finally 块, [402](#ch10#page_402)–[404](#ch10#page_404)
*   try/finally 块, [399](#ch10#page_399)–[400](#ch10#page_400)
*   布尔逻辑, _De Morgan 定律_, [101](#ch03#page_101)
*   `break` 语句, [82](#ch03#page_82)–[83](#ch03#page_83), [85](#ch03#page_85)–[86](#ch03#page_86)
*   打破循环依赖, [600](#ch14#page_600)–[602](#ch14#page_602)
*   动态导入, [604](#ch14#page_604)–[605](#ch14#page_605)
*   导入配置运行, [603](#ch14#page_603)–[604](#ch14#page_604)
*   重新排序导入, [602](#ch14#page_602)
*   `breakpoint` 函数, [566](#ch13#page_566)–[568](#ch13#page_568)
*   `Bucket` 类, [270](#ch08#page_270)–[273](#ch08#page_273)
*   缓冲区协议, CPython, [487](#ch11#page_487)
*   内置函数
*   `enumerate`, [78](#ch03#page_78)–[79](#ch03#page_79)
*   `filter`, [174](#ch06#page_174)–[175](#ch06#page_175)
*   `format`, [52](#ch02#page_52)–[53](#ch02#page_53)
*   `hash`, [110](#ch04#page_110)
*   `help`, [168](#ch05#page_168)
*   `isinstance`, [206](#ch07#page_206)
*   `iter`, [89](#ch03#page_89)–[91](#ch03#page_91)
*   `map`, [174](#ch06#page_174), [175](#ch06#page_175)
*   `range`, [77](#ch03#page_77)–[78](#ch03#page_78)
*   `super`, [238](#ch07#page_238)–[240](#ch07#page_240)
*   `zip`, [80](#ch03#page_80)–[81](#ch03#page_81)
*   内置模块, [217](#ch07#page_217)
*   `bytearray`, [489](#ch11#page_489)–[491](#ch11#page_491)
*   字节码, [324](#ch09#page_324)–[325](#ch09#page_325), [475](#ch11#page_475)–[478](#ch11#page_478)
*   `bytes`, [41](#ch02#page_41)–[46](#ch02#page_46)

### C

*   C3 线性化, [238](#ch07#page_238)
*   捕获模式, [32](#ch01#page_32)–[33](#ch01#page_33)
*   基数, [505](#ch12#page_505)–[506](#ch12#page_506)
*   `careful_divide` 函数, [142](#ch05#page_142)
*   `case` 子句, [33](#ch01#page_33)–[34](#ch01#page_34), [36](#ch01#page_36)–[37](#ch01#page_37)
*   捕获式解包, [72](#ch02#page_72)–[76](#ch02#page_76), [138](#ch05#page_138)–[139](#ch05#page_139)
*   `CFFI` 模块, [461](#ch11#page_461)
*   `chain` 函数, [102](#ch03#page_102)
*   链式异常, [428](#ch10#page_428)–[436](#ch10#page_436)
*   子进程
*   链接, [322](#ch09#page_322)–[323](#ch09#page_323)
*   与父进程解耦, [321](#ch09#page_321)
*   管理, [320](#ch09#page_320)–[324](#ch09#page_324)
*   轮询, [320](#ch09#page_320)–[321](#ch09#page_321)
*   循环依赖, 打破, [600](#ch14#page_600)–[602](#ch14#page_602)
*   动态导入, [604](#ch14#page_604)–[605](#ch14#page_605)
*   导入配置运行, [603](#ch14#page_603)–[604](#ch14#page_604)
*   重新排序导入, [602](#ch14#page_602)
*   类方法多态, [230](#ch07#page_230)–[235](#ch07#page_235)
*   类/别
*   `BaseException`, [419](#ch10#page_419)–[424](#ch10#page_424)
*   `Bucket`, [270](#ch08#page_270)–[273](#ch08#page_273)
*   可组合性, [310](#ch08#page_310)–[317](#ch08#page_317)
*   `CountMissing`, [204](#ch07#page_204)–[205](#ch07#page_205)
*   `Decimal`, [523](#ch12#page_523)–[525](#ch12#page_525)
*   装饰器类, [315](#ch08#page_315)–[317](#ch08#page_317)
*   `defaultdict`, [123](#ch04#page_123)–[124](#ch04#page_124), [202](#ch07#page_202)–[204](#ch07#page_204)
*   定义, [211](#ch07#page_211)–[212](#ch07#page_212)
*   `deque`, [504](#ch12#page_504)–[509](#ch12#page_509)
*   描述符, [269](#ch08#page_269), [275](#ch08#page_275)–[279](#ch08#page_279), [299](#ch08#page_299)–[303](#ch08#page_303), [306](#ch08#page_306), [307](#ch08#page_307)
*   文档字符串, [584](#ch14#page_584)–[585](#ch14#page_585)
*   `Exception`, [416](#ch10#page_416)–[424](#ch10#page_424)
*   辅助类, [204](#ch07#page_204)
*   层级结构, [130](#ch04#page_130)
*   继承, [286](#ch08#page_286)–[287](#ch08#page_287)
*   `JsonMixin`, [243](#ch07#page_243)–[244](#ch07#page_244)
*   轻量级类, [140](#ch05#page_140)–[141](#ch05#page_141)
*   `Lock`, [332](#ch09#page_332)–[333](#ch09#page_333)
*   混入类, [240](#ch07#page_240)–[245](#ch07#page_245)
*   `OrderedDict`, [112](#ch04#page_112)
*   父类, [235](#ch07#page_235)–[236](#ch07#page_236), [237](#ch07#page_237)–[240](#ch07#page_240)
*   `Point`, [256](#ch07#page_256)–[258](#ch07#page_258)
*   公共属性类, [245](#ch07#page_245)–[250](#ch07#page_250)
*   `Queue`, [337](#ch09#page_337)–[344](#ch09#page_344), [353](#ch09#page_353)–[360](#ch09#page_360)
*   重构, [131](#ch04#page_131)–[133](#ch04#page_133)
*   注册, [293](#ch08#page_293)–[299](#ch08#page_299)
*   序列化到和从 JSON, [244](#ch07#page_244)
*   在属性中存储值, [131](#ch04#page_131)–[133](#ch04#page_133)
*   `ThreadPoolExecutor`, [361](#ch09#page_361)–[363](#ch09#page_363), [394](#ch09#page_394)–[397](#ch09#page_397)
*   用户自定义类, [137](#ch05#page_137)
*   版本控制, [530](#ch12#page_530)–[531](#ch12#page_531)
*   子句
*   `case`, [33](#ch01#page_33)–[34](#ch01#page_34), [36](#ch01#page_36)–[37](#ch01#page_37)
*   `finally`, [436](#ch10#page_436)–[442](#ch10#page_442)
*   `if`, [20](#ch01#page_20), [36](#ch01#page_36), [174](#ch06#page_174)
*   闭包, [145](#ch05#page_145)–[149](#ch05#page_149), [203](#ch07#page_203), [383](#ch09#page_383)
*   代码. _参见_ [语句](#index#idx393)
*   并发代码, [319](#ch09#page_319)
*   表达式, [4](#ch01#page_4)–[5](#ch01#page_5)
*   格式化, [4](#ch01#page_4)
*   微基准测试, [453](#ch11#page_453)–[458](#ch11#page_458)
*   模块, [5](#ch01#page_5)
*   模块作用域代码, [593](#ch14#page_593)–[595](#ch14#page_595)
*   组织, [212](#ch07#page_212)
*   多态, [207](#ch07#page_207)–[210](#ch07#page_210)
*   移植到协程和异步 I/O, [368](#ch09#page_368)–[381](#ch09#page_381)
*   Pythonic 代码, [1](#ch01#page_1)
*   重构, [131](#ch04#page_131)–[133](#ch04#page_133), [387](#ch09#page_387)
*   测试, [533](#ch13#page_533)
*   空白字符, [3](#ch01#page_3)–[4](#ch01#page_4)
*   代码点, [42](#ch02#page_42)
*   抛硬币循环, [98](#ch03#page_98)–[101](#ch03#page_101)
*   冷启动, [475](#ch11#page_475)
*   `collections.abc` 模块, [91](#ch03#page_91), [114](#ch04#page_114)
*   `defaultdict` 类, [123](#ch04#page_123)–[124](#ch04#page_124)
*   继承类以创建自定义容器类型, [260](#ch07#page_260)–[264](#ch07#page_264)
*   `combinations` 函数, [108](#ch03#page_108)
*   `combinations_with_replacement` 函数, [108](#ch03#page_108)
*   命令行工具, timeit, [457](#ch11#page_457)–[458](#ch11#page_458)
*   命令, 交互式调试器, [567](#ch13#page_567)
*   逗号/s. _参见_ [语法](#index#idx407)
*   隐式字符串连接, [64](#ch02#page_64)
*   单元素元组, [17](#ch01#page_17)–[18](#ch01#page_18)
*   `communicate` 方法, [321](#ch09#page_321)
*   社区构建的模块, [575](#ch14#page_575)–[576](#ch14#page_576)
*   比较对象, [227](#ch07#page_227)–[230](#ch07#page_230)
*   编译时错误检测, [6](#ch01#page_6)–[8](#ch01#page_8)
*   可组合性, [310](#ch08#page_310)–[317](#ch08#page_317)
*   推导式, [173](#ch06#page_173)
*   赋值表达式, [178](#ch06#page_178)–[181](#ch06#page_181)
*   字典推导式, [174](#ch06#page_174), [179](#ch06#page_179)
*   生成器表达式, [184](#ch06#page_184)–[186](#ch06#page_186)
*   列表推导式, [79](#ch03#page_79)–[80](#ch03#page_80), [86](#ch03#page_86), [98](#ch03#page_98), [173](#ch06#page_173)–[174](#ch06#page_174)
*   包含多于两个子表达式的列表推导式, [176](#ch06#page_176)–[177](#ch06#page_177)
*   连接, 字符串, [62](#ch02#page_62)–[66](#ch02#page_66)
*   并发, [319](#ch09#page_319)
*   协调线程间的工作, [333](#ch09#page_333)–[344](#ch09#page_344)
*   协程, [364](#ch09#page_364)–[368](#ch09#page_368)
*   扇入, [348](#ch09#page_348)
*   扇出, [348](#ch09#page_348), [349](#ch09#page_349)–[353](#ch09#page_353)
*   何时使用, [344](#ch09#page_344)–[349](#ch09#page_349)
*   `concurrent.futures` 模块, [361](#ch09#page_361), [393](#ch09#page_393)–[397](#ch09#page_397)
*   条件表达式, [10](#ch01#page_10), [19](#ch01#page_19)–[23](#ch01#page_23)
*   容器, [261](#ch07#page_261)–[263](#ch07#page_263)
*   迭代容器, [95](#ch03#page_95)–[98](#ch03#page_98)
*   迭代器协议, [89](#ch03#page_89)–[92](#ch03#page_92)
*   暂存修改, [96](#ch03#page_96)–[97](#ch03#page_97)
*   `contains` 函数, [37](#ch01#page_37)
*   上下文管理器, [409](#ch10#page_409)–[412](#ch10#page_412)
*   `contextlib` 模块, [409](#ch10#page_409)–[412](#ch10#page_412)
*   转换
*   对象为元组, [224](#ch07#page_224)–[225](#ch07#page_225)
*   Unicode 为二进制, [42](#ch02#page_42)
*   Conway 的生命游戏, [344](#ch09#page_344)–[348](#ch09#page_348), [364](#ch09#page_364)
*   协调线程间的工作, [333](#ch09#page_333)–[344](#ch09#page_344)
*   `copy` 方法, [136](#ch05#page_136)
*   `copyreg` 模块, [528](#ch12#page_528), [532](#ch12#page_532)
*   协程, [364](#ch09#page_364)–[368](#ch09#page_368)
*   与线程的互操作性, [381](#ch09#page_381)–[384](#ch09#page_384)
*   将代码迁移到协程, [368](#ch09#page_368)–[381](#ch09#page_381)
*   与线程的对比, [364](#ch09#page_364)
*   `count` 变量, [24](#ch01#page_24)–[26](#ch01#page_26)
*   `CountMissing` 类, [204](#ch07#page_204)–[205](#ch07#page_205)
*   CPU. _参见_ [并发](#index#idx103); [并行](#index#idx308); [性能](#index#idx315); [线程](#index#idx420)
*   并行, [319](#ch09#page_319)
*   流水线, [333](#ch09#page_333)–[337](#ch09#page_337)
*   线程, [319](#ch09#page_319)
*   CPython, [324](#ch09#page_324)–[325](#ch09#page_325)
*   缓冲区协议, [487](#ch11#page_487)
*   不带 GIL 编译 Python, [327](#ch09#page_327)
*   扩展模块, [467](#ch11#page_467)–[474](#ch11#page_474)
*   GIL (全局解释器锁), [324](#ch09#page_324)–[327](#ch09#page_327), [329](#ch09#page_329), [330](#ch09#page_330)
*   性能, [475](#ch11#page_475)
*   创建对象, [217](#ch07#page_217)–[218](#ch07#page_218), [219](#ch07#page_219)–[223](#ch07#page_223), [250](#ch07#page_250)–[251](#ch07#page_251), [254](#ch07#page_254)–[256](#ch07#page_256)
*   C 风格格式化, [47](#ch02#page_47)–[52](#ch02#page_52)
*   `csv` 模块, [303](#ch08#page_303)–[306](#ch08#page_306)
*   `ctypes` 模块, [460](#ch11#page_460), [462](#ch11#page_462)–[467](#ch11#page_467)
*   Currying, [171](#ch05#page_171)–[172](#ch05#page_172)
*   `cycle` 函数, [103](#ch03#page_103)
*   Cython, [461](#ch11#page_461)

### D

*   数据, 半结构化 vs. 封装化, [37](#ch01#page_37)–[39](#ch01#page_39)
*   数据竞争, 防止, [330](#ch09#page_330)–[333](#ch09#page_333)
*   `dataclasses` 模块, [131](#ch04#page_131), [217](#ch07#page_217). _参见_ [对象/s](#index#idx296)
*   装饰器, [218](#ch07#page_218), [223](#ch07#page_223)
*   关键字参数, [219](#ch07#page_219)–[221](#ch07#page_221)
*   类型检查器, [218](#ch07#page_218)–[219](#ch07#page_219)
*   `datetime` 模块, [521](#ch12#page_521)–[523](#ch12#page_523)
*   _De Morgan 定律_, [101](#ch03#page_101)
*   调试. _参见_ [异常/异常处理](#index#idx171)
*   交互式调试, [565](#ch13#page_565)–[570](#ch13#page_570)
*   内存使用, [570](#ch13#page_570)–[573](#ch13#page_573)
*   事后调试, [568](#ch13#page_568)–[570](#ch13#page_570)
*   `print` 函数, [58](#ch02#page_58)–[62](#ch02#page_62)
*   堆栈跟踪, [424](#ch10#page_424)–[436](#ch10#page_436)
*   `Decimal` 类, [523](#ch12#page_523)–[525](#ch12#page_525)
*   装饰器/s, [166](#ch05#page_166)–[169](#ch05#page_169), [309](#ch08#page_309), [309](#ch08#page_309)–[310](#ch08#page_310)
*   `@property`, [266](#ch08#page_266)–[269](#ch08#page_269), [270](#ch08#page_270)–[279](#ch08#page_279)
*   类装饰器, [315](#ch08#page_315)–[317](#ch08#page_317)
*   `contextmanager`, [409](#ch10#page_409)–[410](#ch10#page_410)
*   `dataclasses` 模块装饰器, [218](#ch07#page_218)
*   函数装饰器, [166](#ch05#page_166)–[169](#ch05#page_169), [309](#ch08#page_309), [310](#ch08#page_310)–[312](#ch08#page_312)
*   `singledispatch`, [212](#ch07#page_212)–[216](#ch07#page_216)
*   `trace_func` 装饰器, [312](#ch08#page_312)–[313](#ch08#page_313)
*   解耦, 子进程与父进程, [321](#ch09#page_321)
*   `defaultdict` 类, [123](#ch04#page_123)–[124](#ch04#page_124), [202](#ch07#page_202)–[204](#ch07#page_204)
*   依赖/ies, [212](#ch07#page_212), [481](#ch11#page_481). _参见_ [打破循环依赖](#index#idx62)
*   循环依赖, 打破, [600](#ch14#page_600)–[605](#ch14#page_605)
*   封装依赖, [559](#ch13#page_559)–[562](#ch13#page_562)
*   依赖地狱, [577](#ch14#page_577)
*   依赖注入, [604](#ch14#page_604)
*   复现依赖, [580](#ch14#page_580)–[582](#ch14#page_582)
*   部署环境, [593](#ch14#page_593)–[595](#ch14#page_595)
*   `deque` 类, [504](#ch12#page_504)–[509](#ch12#page_509)
*   描述符, [269](#ch08#page_269), [275](#ch08#page_275)–[279](#ch08#page_279), [299](#ch08#page_299)–[303](#ch08#page_303), [306](#ch08#page_306), [307](#ch08#page_307)
*   `deserialize` 函数, [296](#ch08#page_296)–[297](#ch08#page_297)
*   解构, [34](#ch01#page_34)–[37](#ch01#page_37)
*   确定性行为, [203](#ch07#page_203)
*   开发环境, [593](#ch14#page_593)
*   菱形继承, [237](#ch07#page_237)–[240](#ch07#page_240)
*   字典/ies, [109](#ch04#page_109), [306](#ch08#page_306)
*   `__dict__`, [306](#ch08#page_306)–[310](#ch08#page_310)
*   推导式, [174](#ch06#page_174), [179](#ch06#page_179)
*   将对象转换为字典, [225](#ch07#page_225)–[226](#ch07#page_226)
*   格式化字符串, [50](#ch02#page_50)–[52](#ch02#page_52)
*   处理缺失的键, [117](#ch04#page_117)–[121](#ch04#page_121), [122](#ch04#page_122)–[127](#ch04#page_127)
*   不可变对象, [256](#ch07#page_256)–[260](#ch07#page_260)
*   迭代字典, [92](#ch03#page_92)–[93](#ch03#page_93), [109](#ch04#page_109)–[116](#ch04#page_116)
*   `KeyError` 异常, [117](#ch04#page_117)–[118](#ch04#page_118)
*   键/值对, [12](#ch01#page_12)
*   嵌套字典, [127](#ch04#page_127)–[130](#ch04#page_130)
*   空白字符, [4](#ch01#page_4)
*   文档字符串, [158](#ch05#page_158)–[160](#ch05#page_160), [582](#ch14#page_582)–[583](#ch14#page_583)
*   类文档字符串, [584](#ch14#page_584)–[585](#ch14#page_585)
*   函数文档字符串, [585](#ch14#page_585)–[586](#ch14#page_586)
*   模块文档字符串, [584](#ch14#page_584)
*   `dot_product` 函数, [463](#ch11#page_463)–[464](#ch11#page_464)
*   双端队列, [507](#ch12#page_507)
*   `dropwhile` 函数, [105](#ch03#page_105)
*   鸭子类型, [113](#ch04#page_113), [500](#ch12#page_500)–[501](#ch12#page_501), [616](#ch14#page_616)
*   `dumps` 函数, [225](#ch07#page_225)–[226](#ch07#page_226)
*   动态属性, [265](#ch08#page_265)
*   动态导入, [604](#ch14#page_604)–[605](#ch14#page_605)
*   动态检查, [240](#ch07#page_240)–[241](#ch07#page_241)

### E

*   else 块, [82](#ch03#page_82)–[84](#ch03#page_84), [400](#ch10#page_400)–[402](#ch10#page_402)
*   空序列, 循环遍历, [83](#ch03#page_83)
*   空元组, [16](#ch01#page_16)
*   封装数据, [37](#ch01#page_37)–[39](#ch01#page_39)
*   封装依赖, [559](#ch13#page_559)–[562](#ch13#page_562)
*   编码, open, [46](#ch02#page_46)
*   `enhance` 模块, [479](#ch11#page_479)–[482](#ch11#page_482)
*   `enumerate` 函数, [78](#ch03#page_78)–[79](#ch03#page_79). _参见_ [迭代](#index#idx240)
*   等价性检查, 对象, [226](#ch07#page_226)–[227](#ch07#page_227)
*   错误/s. _参见_ [异常/异常处理](#index#idx171)
*   检查错误, [6](#ch01#page_6)–[8](#ch01#page_8)
*   隐式连接错误, [63](#ch02#page_63)–[64](#ch02#page_64)
*   转义错误, [63](#ch02#page_63)
*   `eval` 函数, [445](#ch10#page_445)–[446](#ch10#page_446)
*   `evaluate` 函数, [206](#ch07#page_206)–[208](#ch07#page_208)
*   事件循环, [364](#ch09#page_364)–[365](#ch09#page_365)
*   事件循环, [389](#ch09#page_389)–[392](#ch09#page_392)
*   异常/异常处理, [268](#ch08#page_268), [399](#ch10#page_399)
*   `assert` 语句, [404](#ch10#page_404)–[408](#ch10#page_408)
*   在赋值表达式中, [180](#ch06#page_180)
*   `BaseException` 类, [419](#ch10#page_419)–[424](#ch10#page_424)
*   链式异常, [428](#ch10#page_428)–[436](#ch10#page_436)
*   `Exception` 类, [416](#ch10#page_416)–[424](#ch10#page_424)
*   生成器异常, [195](#ch06#page_195)–[199](#ch06#page_199)
*   `GeneratorExit`, [420](#ch10#page_420), [438](#ch10#page_438)–[442](#ch10#page_442)
*   `IndexError`, [336](#ch09#page_336)
*   `KeyboardInterrupt`, [419](#ch10#page_419)
*   `KeyError`, [117](#ch04#page_117)–[118](#ch04#page_118), [433](#ch10#page_433)
*   `MissingError`, [429](#ch10#page_429)–[436](#ch10#page_436)
*   `NameError`, [147](#ch05#page_147)
*   `OSError`, [353](#ch09#page_353)
*   `raise` 语句, [405](#ch10#page_405)–[408](#ch10#page_408)
*   抛出异常, [142](#ch05#page_142)–[145](#ch05#page_145)
*   `Reset`, [197](#ch06#page_197)
*   根异常, [595](#ch14#page_595)–[600](#ch14#page_600)
*   `ServerMissingKeyError`, [433](#ch10#page_433)
*   `StopIteration`, [88](#ch03#page_88), [198](#ch06#page_198), [438](#ch10#page_438)
*   `SyntaxError`, [533](#ch13#page_533)
*   堆栈跟踪, [424](#ch10#page_424)–[428](#ch10#page_428)
*   try 块, [412](#ch10#page_412)–[414](#ch10#page_414)
*   try/except/else 块, [400](#ch10#page_400)–[402](#ch10#page_402)
*   try/except/else/finally 块, [402](#ch10#page_402)–[404](#ch10#page_404)
*   try/finally 块, [399](#ch10#page_399)–[400](#ch10#page_400)
*   `ValueError`, [401](#ch10#page_401)
*   变量异常, [414](#ch10#page_414)–[416](#ch10#page_416)
*   `exec` 函数, [445](#ch10#page_445)–[446](#ch10#page_446)
*   显式字符串连接, [66](#ch02#page_66)
*   表达式/s, [4](#ch01#page_4)–[5](#ch01#page_5)
*   赋值表达式, [22](#ch01#page_22)–[23](#ch01#page_23), [24](#ch01#page_24)–[30](#ch01#page_30), [68](#ch02#page_68)–[69](#ch02#page_69), [86](#ch03#page_86), [178](#ch06#page_178)–[181](#ch06#page_181)
*   条件表达式, [10](#ch01#page_10), [19](#ch01#page_19)–[23](#ch01#page_23)
*   C 风格格式化表达式, [47](#ch02#page_47)–[52](#ch02#page_52)
*   生成器表达式, [181](#ch06#page_181), [184](#ch06#page_184)–[186](#ch06#page_186)
*   `lambda` 表达式, [172](#ch05#page_172)
*   星号表达式, [73](#ch02#page_73)–[76](#ch02#page_76), [140](#ch05#page_140)
*   `yield` 表达式, [187](#ch06#page_187)–[188](#ch06#page_188), [409](#ch10#page_409)–[410](#ch10#page_410)
*   扩展元组, [131](#ch04#page_131)
*   扩展模块, [467](#ch11#page_467)–[474](#ch11#page_474), [625](#ch14#page_625)

### F

*   `fail` 函数, [19](#ch01#page_19)–[20](#ch01#page_20)
*   扇入, [348](#ch09#page_348)
*   扇出, [348](#ch09#page_348), [349](#ch09#page_349)–[353](#ch09#page_353)
*   FIFO (先进先出) 队列, [504](#ch12#page_504)–[509](#ch12#page_509). _参见_ [生产者-消费者队列](#index#idx337); [队列](#index#idx350)
*   文件系统缓存, [477](#ch11#page_477)
*   文件
*   读取模式, [46](#ch02#page_46)
*   写入模式, [45](#ch02#page_45)
*   `filter` 函数, [174](#ch06#page_174)–[175](#ch06#page_175)
*   过滤迭代器中的项
*   `dropwhile` 函数, [105](#ch03#page_105)
*   `filterfalse` 函数, [105](#ch03#page_105)
*   `islice` 函数, [104](#ch03#page_104)
*   `takewhile` 函数, [104](#ch03#page_104)–[105](#ch03#page_105)
*   `finally` 块, [399](#ch10#page_399)–[400](#ch10#page_400)
*   `finally` 子句, [436](#ch10#page_436)–[442](#ch10#page_442)
*   一等函数, [202](#ch07#page_202)
*   浮点数测试, [563](#ch13#page_563)–[565](#ch13#page_565)
*   `for` 循环, [14](#ch01#page_14)–[15](#ch01#page_15), [173](#ch06#page_173)–[174](#ch06#page_174)
*   避免 else 块, [82](#ch03#page_82)–[84](#ch03#page_84)
*   迭代器协议, [89](#ch03#page_89)–[92](#ch03#page_92)
*   变量, [85](#ch03#page_85)–[86](#ch03#page_86)
*   `for` 语句, [79](#ch03#page_79), [80](#ch03#page_80)
*   格式化
*   代码格式化, [4](#ch01#page_4)
*   格式说明符, [47](#ch02#page_47)–[48](#ch02#page_48), [53](#ch02#page_53)
*   `format` 内置函数, [52](#ch02#page_52)–[53](#ch02#page_53)
*   格式化, [47](#ch02#page_47)
*   高级字符串格式化, [52](#ch02#page_52)–[55](#ch02#page_55)
*   C 风格格式化, [47](#ch02#page_47)–[52](#ch02#page_52)
*   f-string 格式化, [56](#ch02#page_56)–[58](#ch02#page_58)
*   函数式编程, [250](#ch07#page_250)–[251](#ch07#page_251)
*   动态检查, [240](#ch07#page_240)–[241](#ch07#page_241)
*   混入类, [240](#ch07#page_240)–[245](#ch07#page_245)
*   单分派, [212](#ch07#page_212)–[216](#ch07#page_216)
*   函数/s, [175](#ch06#page_175), [238](#ch07#page_238)–[240](#ch07#page_240), [315](#ch08#page_315)–[317](#ch08#page_317)
*   `accumulate`, [106](#ch03#page_106)–[107](#ch03#page_107)
*   `all`, [98](#ch03#page_98)–[100](#ch03#page_100)
*   `animate`, [187](#ch06#page_187)
*   `any`, [100](#ch03#page_100)–[101](#ch03#page_101)
*   参数, [111](#ch04#page_111)–[112](#ch04#page_112), [135](#ch05#page_135)–[137](#ch05#page_137), [153](#ch05#page_153)–[160](#ch05#page_160), [161](#ch05#page_161)–[166](#ch05#page_166)
*   `asdict`, [226](#ch07#page_226)
*   `async`, [364](#ch09#page_364)–[365](#ch09#page_365)
*   `batched`, [105](#ch03#page_105)–[106](#ch03#page_106)
*   `bisect_left`, [502](#ch12#page_502)–[503](#ch12#page_503)
*   `breakpoint`, [566](#ch13#page_566)–[568](#ch13#page_568)
*   `careful_divide`, [142](#ch05#page_142)
*   `chain`, [102](#ch03#page_102)
*   闭包函数, [145](#ch05#page_145)–[149](#ch05#page_149), [203](#ch07#page_203), [383](#ch09#page_383)
*   `combinations`, [108](#ch03#page_108)
*   `combinations_with_replacement`, [108](#ch03#page_108)
*   `contains`, [37](#ch01#page_37)
*   协程函数, [364](#ch09#page_364)–[368](#ch09#page_368)
*   `cycle`, [103](#ch03#page_103)
*   装饰器函数, [166](#ch05#page_166)–[169](#ch05#page_169), [309](#ch08#page_309), [310](#ch08#page_310)–[312](#ch08#page_312)
*   `deserialize`, [296](#ch08#page_296)–[297](#ch08#page_297)
*   函数文档字符串, [585](#ch14#page_585)–[586](#ch14#page_586)
*   `dot_product`, [463](#ch11#page_463)–[464](#ch11#page_464)
*   `dropwhile`, [105](#ch03#page_105)
*   `dumps`, [225](#ch07#page_225)–[226](#ch07#page_226)
*   `enumerate`, [78](#ch03#page_78)–[79](#ch03#page_79)
*   `eval`, [445](#ch10#page_445)–[446](#ch10#page_446)
*   `evaluate`, [206](#ch07#page_206)–[208](#ch07#page_208)
*   `exec`, [445](#ch10#page_445)–[446](#ch10#page_446)
*   `fail`, [19](#ch01#page_19)–[20](#ch01#page_20)
*   `filter`, [174](#ch06#page_174)–[175](#ch06#page_175)
*   `filterfalse`, [105](#ch03#page_105)
*   `finally` 子句函数, [436](#ch10#page_436)–[437](#ch10#page_437)
*   一等函数, [202](#ch07#page_202)
*   `format`, [52](#ch02#page_52)–[53](#ch02#page_53)
*   生成器函数, [87](#ch03#page_87), [173](#ch06#page_173), [182](#ch06#page_182)–[184](#ch06#page_184). _参见_ [生成器/s](#index#idx199)
*   `get_cause`, [435](#ch10#page_435)
*   `get_stats`, [139](#ch05#page_139)–[140](#ch05#page_140)
*   `hash`, [110](#ch04#page_110)
*   `help`, [168](#ch05#page_168)
*   辅助函数, [8](#ch01#page_8)–[11](#ch01#page_11), [21](#ch01#page_21), [42](#ch02#page_42)–[43](#ch02#page_43), [84](#ch03#page_84), [126](#ch04#page_126), [145](#ch05#page_145)–[146](#ch05#page_146), [168](#ch05#page_168)–[169](#ch05#page_169), [232](#ch07#page_232), [251](#ch07#page_251)
*   hooks 函数, [201](#ch07#page_201)–[203](#ch07#page_203)
*   `index_words`, [182](#ch06#page_182), [183](#ch06#page_183)–[184](#ch06#page_184)
*   `isinstance`, [206](#ch07#page_206)
*   `islice`, [104](#ch03#page_104)
*   `iter`, [89](#ch03#page_89)–[91](#ch03#page_91)
*   内核函数, [460](#ch11#page_460)
*   键函数, [494](#ch12#page_494)–[499](#ch12#page_499)
*   `lambda` 函数, [170](#ch05#page_170)–[171](#ch05#page_171), [495](#ch12#page_495)
*   `log_missing`, [202](#ch07#page_202)
*   查找函数, [431](#ch10#page_431)–[436](#ch10#page_436)
*   `map`, [174](#ch06#page_174)
*   `mapreduce`, [233](#ch07#page_233)–[235](#ch07#page_235)
*   `my_print`, [213](#ch07#page_213)
*   `namedtuple`, [259](#ch07#page_259)
*   None 返回值函数, [142](#ch05#page_142)
*   归一化函数, [87](#ch03#page_87), [89](#ch03#page_89)
*   `normalize_defensive`, [91](#ch03#page_91)–[92](#ch03#page_92)
*   `pairwise`, [106](#ch03#page_106)
*   `partial`, [171](#ch05#page_171)–[172](#ch05#page_172)
*   `patch`, [555](#ch13#page_555)–[558](#ch13#page_558)
*   `permutations`, [107](#ch03#page_107)
*   位置参数函数, [150](#ch05#page_150)–[152](#ch05#page_152)
*   `print`, [58](#ch02#page_58)–[62](#ch02#page_62)
*   `product`, [107](#ch03#page_107)
*   抛出异常函数, [142](#ch05#page_142)–[145](#ch05#page_145)
*   `range`, [77](#ch03#page_77)–[78](#ch03#page_78)
*   `repeat`, [103](#ch03#page_103)
*   返回多个值函数, [138](#ch05#page_138)–[141](#ch05#page_141)
*   `run_report`, [416](#ch10#page_416)–[418](#ch10#page_418)
*   `setUpModule`, [548](#ch13#page_548)–[549](#ch13#page_549)
*   `sorted`, [499](#ch12#page_499)–[501](#ch12#page_501)
*   `with` 语句函数, [408](#ch10#page_408)–[412](#ch10#page_412)
*   `takewhile`, [104](#ch03#page_104)–[105](#ch03#page_105)
*   `tearDownModule`, [548](#ch13#page_548)–[549](#ch13#page_549)
*   `tee`, [103](#ch03#page_103)
*   工具函数, [451](#ch11#page_451)
*   包装器函数, [168](#ch05#page_168)
*   `zip`, [80](#ch03#page_80)–[81](#ch03#page_81)
*   `zip_longest`, [81](#ch03#page_81), [103](#ch03#page_103)–[104](#ch03#page_104)
*   `functools` 模块, [170](#ch05#page_170), [171](#ch05#page_171)–[172](#ch05#page_172)

### G

*   `gc` 模块, [571](#ch13#page_571)–[572](#ch13#page_572)
*   `GeneratorExit` 异常, [420](#ch10#page_420), [438](#ch10#page_438)–[442](#ch10#page_442)
*   生成器/s, [87](#ch03#page_87), [173](#ch06#page_173), [182](#ch06#page_182)–[184](#ch06#page_184), [189](#ch06#page_189)–[191](#ch06#page_191)
*   动画生成器, [186](#ch06#page_186)–[188](#ch06#page_188)
*   赋值表达式生成器, [181](#ch06#page_181)
*   与 yield from 表达式组合, [186](#ch06#page_186)–[188](#ch06#page_188)
*   生成器表达式, [184](#ch06#page_184)–[186](#ch06#page_186)
*   惰性生成器, [80](#ch03#page_80)–[81](#ch03#page_81)
*   将迭代器作为参数传递给生成器, [188](#ch06#page_188)–[195](#ch06#page_195)
*   `throw` 方法, [195](#ch06#page_195)–[199](#ch06#page_199)
*   波形生成器, [189](#ch06#page_189)–[195](#ch06#page_195)
*   `get` 方法, [9](#ch01#page_9)–[11](#ch01#page_11), [118](#ch04#page_118)–[120](#ch04#page_120)
*   `get_cause` 函数, [435](#ch10#page_435)
*   `get_stats` 函数, [139](#ch05#page_139)–[140](#ch05#page_140)
*   getter 方法, [266](#ch08#page_266)–[269](#ch08#page_269)
*   GIL (全局解释器锁), [324](#ch09#page_324)–[327](#ch09#page_327), [329](#ch09#page_329), [330](#ch09#page_330)
*   滑翔机, [345](#ch09#page_345)–[346](#ch09#page_346)
*   全局作用域, [147](#ch05#page_147)
*   保护表达式, [36](#ch01#page_36)

### H

*   `hash` 函数, [110](#ch04#page_110)
*   堆, [514](#ch12#page_514)
*   `heapq` 模块, [514](#ch12#page_514)–[519](#ch12#page_519)
*   `help` 函数, [168](#ch05#page_168)
*   辅助类, [204](#ch07#page_204)
*   辅助函数, [8](#ch01#page_8)–[11](#ch01#page_11), [21](#ch01#page_21), [42](#ch02#page_42)–[43](#ch02#page_43), [84](#ch03#page_84), [126](#ch04#page_126), [145](#ch05#page_145)–[146](#ch05#page_146), [168](#ch05#page_168)–[169](#ch05#page_169), [232](#ch07#page_232), [251](#ch07#page_251)
*   辅助方法, [123](#ch04#page_123)
*   `open_picture`, [126](#ch04#page_126)–[127](#ch04#page_127)
*   `TestCase` 类, [535](#ch13#page_535)–[541](#ch13#page_541)
*   hooks, [201](#ch07#page_201)–[203](#ch07#page_203)
*   `__getattr__`, [279](#ch08#page_279)–[281](#ch08#page_281)
*   `__getattribute__`, [281](#ch08#page_281)–[283](#ch08#page_283)
*   `__setattr__`, [283](#ch08#page_283)–[285](#ch08#page_285)

### I

*   `if` 子句, [36](#ch01#page_36), [174](#ch06#page_174)
*   `if` 语句, [19](#ch01#page_19)
*   不可变对象
*   创建, [250](#ch07#page_250)–[251](#ch07#page_251)
*   在字典和集合中使用, [256](#ch07#page_256)–[260](#ch07#page_260)
*   隐式字符串连接, [62](#ch02#page_62)–[66](#ch02#page_66)
*   导入, [5](#ch01#page_5), [592](#ch14#page_592), [601](#ch14#page_601), [604](#ch14#page_604)–[605](#ch14#page_605)
*   `in` 操作符, [117](#ch04#page_117), [119](#ch04#page_119)
*   `index_words` 函数, [182](#ch06#page_182), [183](#ch06#page_183)–[184](#ch06#page_184)
*   `IndexError` 异常, [336](#ch09#page_336)
*   索引, [72](#ch02#page_72)–[73](#ch02#page_73). _参见_ [切片](#index#idx386)
*   负数索引, [68](#ch02#page_68)
*   并行索引, [79](#ch03#page_79)–[80](#ch03#page_80)
*   与切片结合, [67](#ch02#page_67)–[69](#ch02#page_69)
*   字符串索引, [10](#ch01#page_10)–[11](#ch01#page_11)
*   继承
*   类继承, [286](#ch08#page_286)–[287](#ch08#page_287)
*   菱形继承, [237](#ch07#page_237)–[240](#ch07#page_240)
*   多重继承, [236](#ch07#page_236), [239](#ch07#page_239), [240](#ch07#page_240)
*   继承类以创建自定义容器类型, [260](#ch07#page_260)–[264](#ch07#page_264)
*   初始化父类, [235](#ch07#page_235)–[236](#ch07#page_236)
*   内联否定, [5](#ch01#page_5)
*   `insert_value`, 性能分析, [448](#ch11#page_448)–[451](#ch11#page_451)
*   插入顺序, 字典, [109](#ch04#page_109)–[116](#ch04#page_116)
*   `insertion_sort`, 性能分析, [448](#ch11#page_448)–[451](#ch11#page_451)
*   集成测试, [541](#ch13#page_541)–[542](#ch13#page_542)
*   交互式调试, [565](#ch13#page_565)–[568](#ch13#page_568)
*   插值格式化字符串, [56](#ch02#page_56)–[58](#ch02#page_58)
*   I/O
*   异步 I/O, [368](#ch09#page_368), [376](#ch09#page_376)
*   阻塞 I/O, [324](#ch09#page_324)–[329](#ch09#page_329), [348](#ch09#page_348)
*   线程 I/O, 移植到 asyncio, [368](#ch09#page_368)–[381](#ch09#page_381)
*   `isinstance` 函数, [206](#ch07#page_206)
*   `islice` 函数, [104](#ch03#page_104)
*   `islice` 方法, [72](#ch02#page_72)
*   `iter` 内置函数, [89](#ch03#page_89)–[91](#ch03#page_91)
*   迭代/迭代器, [77](#ch03#page_77), [182](#ch06#page_182)–[183](#ch06#page_183). _参见_ [循环/s](#index#idx262)
*   异常迭代, [88](#ch03#page_88)
*   生成器迭代, [87](#ch03#page_87)
*   列表迭代, [79](#ch03#page_79)–[80](#ch03#page_80), [87](#ch03#page_87)
*   迭代参数, [87](#ch03#page_87)–[92](#ch03#page_92)
*   迭代容器, [95](#ch03#page_95)–[98](#ch03#page_98)
*   迭代字典, [92](#ch03#page_92)–[93](#ch03#page_93), [109](#ch04#page_109)–[116](#ch04#page_116)
*   迭代列表, [94](#ch03#page_94)–[95](#ch03#page_95)
*   迭代集合, [93](#ch03#page_93), [96](#ch03#page_96)
*   将迭代器作为参数传递给生成器, [188](#ch06#page_188)–[195](#ch06#page_195)
*   传递给 `all` 内置函数, [98](#ch03#page_98)–[100](#ch03#page_100)
*   传递给 `any` 内置函数, [100](#ch03#page_100)–[101](#ch03#page_101)
*   `StopIteration` 异常, [88](#ch03#page_88)
*   `zip` 生成器, [80](#ch03#page_80)–[81](#ch03#page_81)
*   迭代器协议, [89](#ch03#page_89)–[92](#ch03#page_92)
*   `itertools`, [72](#ch02#page_72), [185](#ch06#page_185)–[186](#ch06#page_186)
*   `accumulate` 函数, [106](#ch03#page_106)–[107](#ch03#page_107)
*   `batched` 函数, [105](#ch03#page_105)–[106](#ch03#page_106)
*   `chain` 函数, [102](#ch03#page_102)
*   `combinations` 函数, [108](#ch03#page_108)
*   `combinations_with_replacement` 函数, [108](#ch03#page_108)
*   `cycle` 函数, [103](#ch03#page_103)
*   `dropwhile` 函数, [105](#ch03#page_105)
*   `filterfalse` 函数, [105](#ch03#page_105)
*   `islice` 函数, [104](#ch03#page_104)
*   `pairwise` 函数, [106](#ch03#page_106)
*   `permutations` 函数, [107](#ch03#page_107)
*   `product` 函数, [107](#ch03#page_107)
*   `repeat` 函数, [103](#ch03#page_103)
*   `takewhile` 函数, [104](#ch03#page_104)–[105](#ch03#page_105)
*   `tee` 函数, [103](#ch03#page_103)
*   `zip_longest` 函数, [81](#ch03#page_81), [103](#ch03#page_103)–[104](#ch03#page_104)

### J-K

*   JSON, [37](#ch01#page_37)–[38](#ch01#page_38), [244](#ch07#page_244), [293](#ch08#page_293)–[297](#ch08#page_297)
*   `JsonMixin` 类, [243](#ch07#page_243)–[244](#ch07#page_244)
*   内核函数, [460](#ch11#page_460)
*   键函数, [494](#ch12#page_494)–[499](#ch12#page_499)
*   `KeyboardInterrupt` 异常, [419](#ch10#page_419)
*   `KeyError` 异常, [117](#ch04#page_117)–[118](#ch04#page_118), [433](#ch10#page_433)
*   关键字
*   参数, [153](#ch05#page_153)–[157](#ch05#page_157), [161](#ch05#page_161)–[162](#ch05#page_162), [219](#ch07#page_219)–[221](#ch07#page_221)
*   仅关键字参数, [162](#ch05#page_162)–[164](#ch05#page_164)
*   严格关键字, `zip` 函数, [81](#ch03#page_81)

### L

*   `lambda` 函数, [170](#ch05#page_170)–[171](#ch05#page_171), [495](#ch12#page_495)
*   惰性属性, [279](#ch08#page_279)–[285](#ch08#page_285)
*   惰性生成器, [80](#ch03#page_80)–[81](#ch03#page_81)
*   惰性加载, [478](#ch11#page_478)–[485](#ch11#page_485)
*   leaky-bucket 算法, [270](#ch08#page_270)–[273](#ch08#page_273)
*   轻量级类, [140](#ch05#page_140)–[141](#ch05#page_141)
*   链接迭代器
*   `chain` 函数, [102](#ch03#page_102)
*   `cycle` 函数, [103](#ch03#page_103)
*   `repeat` 函数, [103](#ch03#page_103)
*   `tee` 函数, [103](#ch03#page_103)
*   `zip_longest` 函数, [103](#ch03#page_103)–[104](#ch03#page_104)
*   列表/s, [260](#ch07#page_260)–[261](#ch07#page_261). _参见_ [索引](#index#idx224)
*   基数, [505](#ch12#page_505)–[506](#ch12#page_506)
*   推导式, [79](#ch03#page_79)–[80](#ch03#page_80), [86](#ch03#page_86), [98](#ch03#page_98), [173](#ch06#page_173)–[177](#ch06#page_177), [178](#ch06#page_178)–[181](#ch06#page_181), [184](#ch06#page_184)–[186](#ch06#page_186)
*   出队操作, [504](#ch12#page_504)–[509](#ch12#page_509)
*   字典值列表, [119](#ch04#page_119)–[121](#ch04#page_121)
*   迭代列表, [94](#ch03#page_94)–[95](#ch03#page_95)
*   列表迭代, [78](#ch03#page_78), [87](#ch03#page_87)
*   嵌套列表, [127](#ch04#page_127)–[130](#ch04#page_130)
*   优先级队列, [509](#ch12#page_509)–[514](#ch12#page_514)
*   排序列表项, [145](#ch05#page_145), [493](#ch12#page_493)–[499](#ch12#page_499)
*   字面值, [16](#ch01#page_16)
*   `Lock` 类, [332](#ch09#page_332)–[333](#ch09#page_333)
*   `log_missing` 函数, [202](#ch07#page_202)
*   查找函数, [431](#ch10#page_431)–[436](#ch10#page_436)
*   循环/s, [77](#ch03#page_77)
*   `break` 语句, [82](#ch03#page_82)–[83](#ch03#page_83), [85](#ch03#page_85)–[86](#ch03#page_86)
*   抛硬币循环, [98](#ch03#page_98)–[101](#ch03#page_101)
*   在推导式中循环, [176](#ch06#page_176)–[177](#ch06#page_177)
*   避免 else 块, [82](#ch03#page_82)–[84](#ch03#page_84)
*   事件循环, [364](#ch09#page_364)–[365](#ch09#page_365), [389](#ch09#page_389)–[392](#ch09#page_392)
*   `for` 循环, [14](#ch01#page_14)–[15](#ch01#page_15), [85](#ch03#page_85)–[86](#ch03#page_86), [173](#ch06#page_173)–[174](#ch06#page_174)
*   “一个半”习语, [29](#ch01#page_29)–[30](#ch01#page_30)
*   迭代器协议, [89](#ch03#page_89)–[92](#ch03#page_92)
*   `range` 函数循环, [77](#ch03#page_77)–[78](#ch03#page_78)
*   `while` 循环, [29](#ch01#page_29), [382](#ch09#page_382)–[383](#ch09#page_383)

### M

*   管理, 子进程, [320](#ch09#page_320)–[324](#ch09#page_324)
*   `map` 函数, [174](#ch06#page_174), [175](#ch06#page_175)
*   `mapreduce` 函数, [233](#ch07#page_233)–[235](#ch07#page_235)
*   `match` 语句, [30](#ch01#page_30)–[34](#ch01#page_34), [370](#ch09#page_370)
*   解构, [34](#ch01#page_34)–[37](#ch01#page_37)
*   半结构化 vs. 封装化数据, [37](#ch01#page_37)–[39](#ch01#page_39)
*   内存
*   字节码缓存, [475](#ch11#page_475)–[478](#ch11#page_478)
*   文件系统缓存, [477](#ch11#page_477)
*   惰性加载, [478](#ch11#page_478)–[485](#ch11#page_485)
*   内存泄漏, [278](#ch08#page_278)–[279](#ch08#page_279)
*   内存使用调试, [570](#ch13#page_570)–[573](#ch13#page_573)
*   `memoryview` 类型, [487](#ch11#page_487)–[491](#ch11#page_491)
*   元类, [265](#ch08#page_265), [285](#ch08#page_285)–[287](#ch08#page_287)
*   类注册, [293](#ch08#page_293)–[299](#ch08#page_299)
*   修改类的属性, [299](#ch08#page_299)–[303](#ch08#page_303)
*   子类验证, [287](#ch08#page_287)–[291](#ch08#page_291)
*   `TraceMeta`, [313](#ch08#page_313)–[314](#ch08#page_314)
*   方法/s
*   `@property`. _参见_ [@property 装饰器](#index#idx22)
*   `_asdict`, [226](#ch07#page_226)
*   `_astuple`, [225](#ch07#page_225), [227](#ch07#page_227), [228](#ch07#page_228)–[229](#ch07#page_229)
*   `__call__`, [204](#ch07#page_204)–[205](#ch07#page_205)
*   `__delattr__`, [252](#ch07#page_252)
*   `__eq__`, [226](#ch07#page_226)
*   `__getattr__`, [279](#ch08#page_279)–[281](#ch08#page_281)
*   `__getitem__`, [261](#ch07#page_261)–[263](#ch07#page_263)
*   `__hash__`, [258](#ch07#page_258)
*   `__init__`, [217](#ch07#page_217)–[219](#ch07#page_219), [235](#ch07#page_235)–[236](#ch07#page_236)
*   `__init_subclass__`, [288](#ch08#page_288)–[299](#ch08#page_299), [306](#ch08#page_306)–[310](#ch08#page_310)
*   `__iter__`, [89](#ch03#page_89)–[91](#ch03#page_91)
*   `__missing__`, [124](#ch04#page_124)–[127](#ch04#page_127)
*   `_replace`, [255](#ch07#page_255)
*   `__repr__`, [223](#ch07#page_223)–[224](#ch07#page_224)
*   `__set_name__`, [278](#ch08#page_278), [302](#ch08#page_302)–[303](#ch08#page_303)
*   `__setattr__`, [252](#ch07#page_252), [283](#ch08#page_283)–[285](#ch08#page_285)
*   `append`, [182](#ch06#page_182), [506](#ch12#page_506)
*   `assertAlmostEqual`, [564](#ch13#page_564)–[565](#ch13#page_565)
*   `assertNotAlmostEqual`, [565](#ch13#page_565)
*   `communicate`, [321](#ch09#page_321)
*   `copy`, [136](#ch05#page_136)
*   `get`, [9](#ch01#page_9)–[11](#ch01#page_11), [118](#ch04#page_118)–[120](#ch04#page_120)
*   getter 方法, [266](#ch08#page_266)–[269](#ch08#page_269), [276](#ch08#page_276)
*   辅助方法, [123](#ch04#page_123)
*   `islice`, [72](#ch02#page_72)
*   `open_picture`, [126](#ch04#page_126)–[127](#ch04#page_127)
*   `pretty`, [209](#ch07#page_209)
*   `print_callees`, [452](#ch11#page_452)–[453](#ch11#page_453)
*   `print_callers`, [452](#ch11#page_452)
*   公共属性方法, [246](#ch07#page_246)
*   `quantize`, [525](#ch12#page_525)
*   `read`, [230](#ch07#page_230)–[231](#ch07#page_231)
*   `register`, [213](#ch07#page_213)
*   `run`, [198](#ch06#page_198)–[199](#ch06#page_199)
*   `send`, [189](#ch06#page_189)–[191](#ch06#page_191)
*   `setdefault`, [120](#ch04#page_120)–[121](#ch04#page_121), [122](#ch04#page_122)–[123](#ch04#page_123), [125](#ch04#page_125)
*   setter 方法, [266](#ch08#page_266)–[269](#ch08#page_269), [276](#ch08#page_276)
*   `sort`, [145](#ch05#page_145)–[149](#ch05#page_149), [201](#ch07#page_201)–[202](#ch07#page_202), [493](#ch12#page_493)–[499](#ch12#page_499)
*   `str.format`, [54](#ch02#page_54)–[55](#ch02#page_55)
*   `throw`, [195](#ch06#page_195)–[199](#ch06#page_199)
*   `title`, [50](#ch02#page_50)
*   `update`, [96](#ch03#page_96)
*   空白字符方法, [4](#ch01#page_4)
*   度量, [447](#ch11#page_447)
*   微基准测试, [453](#ch11#page_453)–[458](#ch11#page_458), [490](#ch11#page_490)–[491](#ch11#page_491), [512](#ch12#page_512)–[517](#ch12#page_517)
*   `MissingError` 异常, [429](#ch10#page_429)–[436](#ch10#page_436)
*   混入类, [240](#ch07#page_240)–[245](#ch07#page_245)
*   模拟对象, [550](#ch13#page_550)–[558](#ch13#page_558). _参见_ [测试/s](#index#idx416)
*   模块/s, [5](#ch01#page_5), [109](#ch04#page_109)
*   `adjust`, [479](#ch11#page_479)–[482](#ch11#page_482)
*   `argparse`, [479](#ch11#page_479)–[481](#ch11#page_481)
*   `asyncio`, [329](#ch09#page_329), [366](#ch09#page_366)–[367](#ch09#page_367), [368](#ch09#page_368)–[384](#ch09#page_384)
*   `bisect`, [501](#ch12#page_501)–[503](#ch12#page_503)
*   内置模块, [217](#ch07#page_217)
*   字节码缓存模块, [475](#ch11#page_475)–[478](#ch11#page_478)
*   `CFFI`, [461](#ch11#page_461)
*   `collections.abc`, [91](#ch03#page_91), [114](#ch04#page_114), [260](#ch07#page_260)–[264](#ch07#page_264)
*   社区构建模块, [575](#ch14#page_575)–[576](#ch14#page_576)
*   `concurrent.futures`, [361](#ch09#page_361), [393](#ch09#page_393)–[397](#ch09#page_397)
*   `contextlib`, [409](#ch10#page_409)–[412](#ch10#page_412)
*   `copyreg`, [528](#ch12#page_528), [532](#ch12#page_532)
*   `CProfile`, [449](#ch11#page_449)–[450](#ch11#page_450)
*   `csv`, [303](#ch08#page_303)–[306](#ch08#page_306)
*   `ctypes`, [460](#ch11#page_460), [462](#ch11#page_462)–[467](#ch11#page_467)
*   `dataclasses`, [131](#ch04#page_131), [217](#ch07#page_217), [218](#ch07#page_218)–[219](#ch07#page_219)
*   `datetime`, [521](#ch12#page_521)–[523](#ch12#page_523)
*   `decimal`, [523](#ch12#page_523)–[525](#ch12#page_525)
*   模块文档字符串, [584](#ch14#page_584)
*   `enhance`, [479](#ch11#page_479)–[482](#ch11#page_482)
*   扩展模块, [467](#ch11#page_467)–[474](#ch11#page_474), [625](#ch14#page_625)
*   `functools`, [170](#ch05#page_170), [171](#ch05#page_171)–[172](#ch05#page_172)
*   `gc`, [571](#ch13#page_571)–[572](#ch13#page_572)
*   `heapq`, [514](#ch12#page_514)–[519](#ch12#page_519)
*   惰性加载模块, [478](#ch11#page_478)–[485](#ch11#page_485)
*   `multiprocessing`, [393](#ch09#page_393)–[397](#ch09#page_397)
*   `Numba`, [461](#ch11#page_461)
*   `Numby`, [461](#ch11#page_461)
*   `pdb`, [566](#ch13#page_568)–[568](#ch13#page_568)
*   `pickle`, [526](#ch12#page_526)–[532](#ch12#page_532)
*   `pkgutil`, [624](#ch14#page_624)–[626](#ch14#page_626)
*   根异常模块, [595](#ch14#page_595)–[600](#ch14#page_600)
*   模块作用域代码, [593](#ch14#page_593)–[595](#ch14#page_595)
*   `subprocess` 模块, 管理子进程, [320](#ch09#page_320)–[324](#ch09#page_324)
*   `threading`, [332](#ch09#page_332)
*   `time`, [519](#ch12#page_519)–[521](#ch12#page_521)
*   `timeit`, [453](#ch11#page_453)–[458](#ch11#page_458)
*   堆栈跟踪模块, [424](#ch10#page_424)–[428](#ch10#page_428)
*   `tracemalloc`, [572](#ch13#page_572)–[573](#ch13#page_573)
*   `typing`, [613](#ch14#page_613)–[621](#ch14#page_621)
*   `unittest`, [533](#ch13#page_533)–[535](#ch13#page_535), [548](#ch13#page_548)
*   版本模块, [577](#ch14#page_577)–[578](#ch14#page_578)
*   `warnings`, [605](#ch14#page_605)–[613](#ch14#page_613)
*   `zipimport`, [622](#ch14#page_622)–[624](#ch14#page_624)
*   `zoneinfo`, [522](#ch12#page_522)–[523](#ch12#page_523)
*   MRO (方法解析顺序), [238](#ch07#page_238)
*   多重继承, [236](#ch07#page_236), [239](#ch07#page_239), [240](#ch07#page_240)
*   多个返回值, 解包, [138](#ch05#page_138)–[141](#ch05#page_141)
*   多重赋值解包, [11](#ch01#page_11)–[15](#ch01#page_15)
*   `multiprocessing` 模块, [393](#ch09#page_393)–[397](#ch09#page_397)
*   多线程, 抢占式, [325](#ch09#page_325), [331](#ch09#page_331)–[333](#ch09#page_333)
*   互斥锁, [325](#ch09#page_325), [330](#ch09#page_330), [332](#ch09#page_332)–[333](#ch09#page_333), [408](#ch10#page_408)
*   `my_print` 函数, [213](#ch07#page_213)
*   `mypy` 工具, [115](#ch04#page_115)–[116](#ch04#page_116)
*   `Mypyc`, [461](#ch11#page_461)

### N

*   `namedtuple` 函数, [259](#ch07#page_259)
*   `NameError` 异常, [147](#ch05#page_147)
*   负数索引, [68](#ch02#page_68)
*   `None`, 作为默认参数值, [157](#ch05#page_157)–[160](#ch05#page_160)
*   `nonlocal` 语句, [148](#ch05#page_148)–[149](#ch05#page_149)
*   归一化函数, [87](#ch03#page_87), [89](#ch03#page_89)
*   `normalize_defensive` 函数, [91](#ch03#page_91)–[92](#ch03#page_92)
*   `Numba` 模块, [461](#ch11#page_461)
*   `Numby` 模块, [461](#ch11#page_461)

### O

*   对象/s, [60](#ch02#page_60)
*   AST (抽象语法树), [208](#ch07#page_208)–[210](#ch07#page_210)
*   将对象转换为字典, [225](#ch07#page_225)–[226](#ch07#page_226)
*   将对象转换为元组, [224](#ch07#page_224)–[225](#ch07#page_225)
*   创建对象, [217](#ch07#page_217)–[218](#ch07#page_218), [219](#ch07#page_219)–[223](#ch07#page_223)
*   创建具有替换属性的对象副本, [254](#ch07#page_254)–[256](#ch07#page_256)
*   菱形继承, [237](#ch07#page_237)–[240](#ch07#page_240)
*   对象动态内部状态, [127](#ch04#page_127)
*   启用对象比较, [227](#ch07#page_227)–[230](#ch07#page_230)
*   对象等价性检查, [226](#ch07#page_226)–[227](#ch07#page_227)
*   不可变对象, [250](#ch07#page_250)–[251](#ch07#page_251), [256](#ch07#page_256)–[260](#ch07#page_260)
*   面向对象多态, [207](#ch07#page_207)–[210](#ch07#page_210)
*   防止对象被修改, [251](#ch07#page_251)–[254](#ch07#page_254)
*   将对象表示为字符串, [223](#ch07#page_223)–[224](#ch07#page_224)
*   序列化, [168](#ch05#page_168), [528](#ch12#page_528)–[530](#ch12#page_530)
*   对象排序, [494](#ch12#page_494)–[495](#ch12#page_495)
*   OOP (面向对象编程)
*   类定义, [211](#ch07#page_211)–[212](#ch07#page_212)
*   依赖关系, [212](#ch07#page_212). _参见_ [依赖/ies](#index#idx137)
*   多态, [207](#ch07#page_207)–[210](#ch07#page_210)
*   open 编码模式, [46](#ch02#page_46)
*   开源项目, [621](#ch14#page_621)–[626](#ch14#page_626)
*   `open_picture` 方法, [126](#ch04#page_126)–[127](#ch04#page_127)
*   操作系统
*   阻塞 I/O, [327](#ch09#page_327), [348](#ch09#page_348)–[349](#ch09#page_349)
*   系统调用, [327](#ch09#page_327)–[329](#ch09#page_329)
*   操作符
*   `%`, [44](#ch02#page_44), [50](#ch02#page_50)
*   `*`, [151](#ch05#page_151)–[152](#ch05#page_152)
*   `**`, [153](#ch05#page_153)–[154](#ch05#page_154)
*   `|` 管道操作符, [36](#ch01#page_36)
*   `+` 操作符, [43](#ch02#page_43)
*   二元操作符, [44](#ch02#page_44)
*   `in` 操作符, [117](#ch04#page_117), [119](#ch04#page_119)
*   三元操作符, [19](#ch01#page_19)–[20](#ch01#page_20)
*   海象操作符, [24](#ch01#page_24)–[30](#ch01#page_30), [179](#ch06#page_179)–[181](#ch06#page_181). _参见_ [赋值表达式](#index#idx44)
*   `OrderedDict` 类, [112](#ch04#page_112)
*   `OSError` 异常, [353](#ch09#page_353)

### P

*   包, [588](#ch14#page_588)
*   命名空间, [588](#ch14#page_588)–[590](#ch14#page_590)
*   稳定的 API, [590](#ch14#page_590)–[592](#ch14#page_592)
*   `pairwise` 函数, [106](#ch03#page_106)
*   并行索引, [79](#ch03#page_79)–[80](#ch03#page_80)
*   并行性, [319](#ch09#page_319)
*   `concurrent.futures`, [393](#ch09#page_393)–[397](#ch09#page_397)
*   数据竞争防止, [330](#ch09#page_330)–[333](#ch09#page_333)
*   扇出, [350](#ch09#page_350)–[353](#ch09#page_353)
*   管理子进程, [320](#ch09#page_320)–[324](#ch09#page_324)
*   父类
*   菱形继承, [237](#ch07#page_237)–[240](#ch07#page_240)
*   初始化父类, [235](#ch07#page_235)–[236](#ch07#page_236)
*   父进程, 子进程与父进程解耦, [321](#ch09#page_321)
*   括号
*   赋值表达式括号, [22](#ch01#page_22)–[23](#ch01#page_23)
*   单元素元组括号, [16](#ch01#page_16)–[19](#ch01#page_19)
*   `partial` 函数, [171](#ch05#page_171)–[172](#ch05#page_172)
*   `patch` 函数, [555](#ch13#page_555)–[558](#ch13#page_558)
*   PEP 8 (Python 增强提案 #8), [3](#ch01#page_3)
*   自动化, [5](#ch01#page_5)–[6](#ch01#page_6)
*   表达式和语句, [4](#ch01#page_4)–[5](#ch01#page_5)
*   导入, [5](#ch01#page_5)
*   命名, [4](#ch01#page_4)
*   空白字符, [3](#ch01#page_3)–[4](#ch01#page_4)
*   性能. _参见_ [性能分析](#index#idx340)
*   CPython 性能, [475](#ch11#page_475)
*   工程性能, [447](#ch11#page_447)
*   扩展模块性能, [467](#ch11#page_467)–[474](#ch11#page_474)
*   惰性加载模块性能, [478](#ch11#page_478)–[485](#ch11#page_485)
*   从 zip 存档加载模块性能, [622](#ch14#page_622)–[623](#ch14#page_623)
*   度量, [447](#ch11#page_447)
*   微基准测试, [490](#ch11#page_490)–[491](#ch11#page_491), [512](#ch12#page_512)–[517](#ch12#page_517)
*   生产者-消费者队列, [504](#ch12#page_504)–[509](#ch12#page_509)
*   性能分析, [448](#ch11#page_448)–[453](#ch11#page_453)
*   将 Python 替换为其他编程语言, [458](#ch11#page_458)–[462](#ch11#page_462)
*   搜索性能, [501](#ch12#page_501)–[503](#ch12#page_503)
*   timeit 微基准测试, [453](#ch11#page_453)–[458](#ch11#page_458)
*   `permutations` 函数, [107](#ch03#page_107)
*   `pickle` 模块, [526](#ch12#page_526)–[528](#ch12#page_528)
*   默认属性值, [528](#ch12#page_528)–[530](#ch12#page_530)
*   稳定的导入路径, [531](#ch12#page_531)–[532](#ch12#page_532)
*   版本控制类, [530](#ch12#page_530)–[531](#ch12#page_531)
*   `pip` 工具, [575](#ch14#page_575)–[577](#ch14#page_577)
*   流水线, [333](#ch09#page_333)–[337](#ch09#page_337), [416](#ch10#page_416)–[417](#ch10#page_417)
*   将数据输入子进程, [321](#ch09#page_321)–[322](#ch09#page_322)
*   `pkgutil` 模块, [624](#ch14#page_624)–[626](#ch14#page_626)
*   `Point` 对象, [256](#ch07#page_256)–[258](#ch07#page_258)
*   多态, [207](#ch07#page_207)–[210](#ch07#page_210), [230](#ch07#page_230)–[235](#ch07#page_235)
*   移植代码使用协程和 asyncio, [368](#ch09#page_368)–[384](#ch09#page_384)
*   自下而上方法, [387](#ch09#page_387)–[388](#ch09#page_388)
*   自顶向下方法, [384](#ch09#page_384)–[387](#ch09#page_387)
*   可变位置参数, [150](#ch05#page_150)–[152](#ch05#page_152)
*   仅位置参数, [164](#ch05#page_164)–[166](#ch05#page_166)
*   事后调试, [568](#ch13#page_568)–[570](#ch13#page_570)
*   抢占式多线程, [325](#ch09#page_325), [331](#ch09#page_331)–[333](#ch09#page_333)
*   `pretty` 方法, [209](#ch07#page_209)
*   美观打印, [215](#ch07#page_215)
*   防止对象被修改, [251](#ch07#page_251)–[254](#ch07#page_254)
*   `print` 函数, [58](#ch02#page_58)–[62](#ch02#page_62)
*   `print_callees` 方法, [452](#ch11#page_452)–[453](#ch11#page_453)
*   `print_callers` 方法, [452](#ch11#page_452)
*   优先级队列, [509](#ch12#page_509)–[519](#ch12#page_519)
*   私有属性, [246](#ch07#page_246)–[247](#ch07#page_247)
*   生产者-消费者队列, [504](#ch12#page_504)–[509](#ch12#page_509)
*   生成迭代器组合
*   `accumulate` 函数, [106](#ch03#page_106)–[107](#ch03#page_107)
*   `batched` 函数, [105](#ch03#page_105)–[106](#ch03#page_106)
*   `combinations` 函数, [108](#ch03#page_108)
*   `combinations_with_replacement` 函数, [108](#ch03#page_108)
*   `pairwise` 函数, [106](#ch03#page_106)
*   `permutations` 函数, [107](#ch03#page_107)
*   `product` 函数, [107](#ch03#page_107)
*   `product` 函数, [107](#ch03#page_107)
*   性能分析, [448](#ch11#page_448)
*   `insertion_sort` 和 `insert_value`, [448](#ch11#page_448)–[451](#ch11#page_451)
*   `print_callees` 方法, [452](#ch11#page_452)–[453](#ch11#page_453)
*   `print_callers` 方法, [452](#ch11#page_452)
*   工具函数性能分析, [451](#ch11#page_451)
*   程序. _参见_ [代码](#index#idx86); [性能](#index#idx315)
*   字节码程序, [324](#ch09#page_324)–[325](#ch09#page_325)
*   并发程序, [319](#ch09#page_319). _参见_ [并发](#index#idx103)
*   部署环境程序, [593](#ch14#page_593)–[595](#ch14#page_595)
*   开发环境程序, [593](#ch14#page_593)
*   流水线程序, [333](#ch09#page_333)–[337](#ch09#page_337)
*   将数据输入子进程程序, [321](#ch09#page_321)–[322](#ch09#page_322)
*   抢占式多线程程序, [325](#ch09#page_325)
*   加速程序, [319](#ch09#page_319)
*   保护属性, [247](#ch07#page_247)–[250](#ch07#page_250)
*   公共属性, [245](#ch07#page_245)–[250](#ch07#page_250), [266](#ch08#page_266)–[269](#ch08#page_269)
*   `pylint`, [6](#ch01#page_6)
*   PyPI (Python 包索引), [575](#ch14#page_575)
*   Python
*   C 扩展 API, [460](#ch11#page_460), [465](#ch11#page_465)
*   了解你正在使用的版本, [1](#ch01#page_1)–[3](#ch01#page_3)
*   将 Python 替换为其他编程语言, [458](#ch11#page_458)–[462](#ch11#page_462)
*   Python 对线程的支持, [327](#ch09#page_327)–[329](#ch09#page_329)
*   Pythonic 风格, [1](#ch01#page_1)

### Q

*   `quantize` 方法, [525](#ch12#page_525)
*   查询字符串参数, [8](#ch01#page_8)–[9](#ch01#page_9)
*   队列
*   优先级队列, [509](#ch12#page_509)–[519](#ch12#page_519)
*   生产者-消费者队列, [504](#ch12#page_504)–[509](#ch12#page_509)
*   `Queue` 类, [337](#ch09#page_337)–[344](#ch09#page_344), [353](#ch09#page_353)–[360](#ch09#page_360)
*   配额, leaky-bucket 算法, [270](#ch08#page_270)–[273](#ch08#page_273)

### R

*   `raise` 语句, [405](#ch10#page_405)–[408](#ch10#page_408)
*   抛出异常, [142](#ch05#page_142)–[145](#ch05#page_145). _参见_ [异常/异常处理](#index#idx171)
*   `assert` 语句, [404](#ch10#page_404)–[408](#ch10#page_408)
*   生成器异常, [195](#ch06#page_195)–[199](#ch06#page_199)
*   `raise` 语句, [405](#ch10#page_405)–[408](#ch10#page_408)
*   try 块, [412](#ch10#page_412)–[414](#ch10#page_414)
*   `range` 函数, [77](#ch03#page_77)–[78](#ch03#page_78)
*   读取二进制模式, [46](#ch02#page_46)
*   `read` 方法, [230](#ch07#page_230)–[231](#ch07#page_231)
*   重构, [131](#ch04#page_131)–[133](#ch04#page_133), [387](#ch09#page_387)
*   `register` 方法, [213](#ch07#page_213)
*   注册, 类注册, [293](#ch08#page_293)–[299](#ch08#page_299)
*   `repeat` 函数, [103](#ch03#page_103)
*   将 Python 替换为其他编程语言, [458](#ch11#page_458)–[462](#ch11#page_462)
*   `repr`, `str` 和 `repr` 的区别, [58](#ch02#page_58)–[62](#ch02#page_62)
*   复现依赖, [580](#ch14#page_580)–[582](#ch14#page_582)
*   `Reset` 异常, [197](#ch06#page_197)
*   根异常, [595](#ch14#page_595)–[600](#ch14#page_600)
*   最小惊讶原则, [265](#ch08#page_265)
*   `run` 方法, [198](#ch06#page_198)–[199](#ch06#page_199)
*   `run_report` 函数, [416](#ch10#page_416)–[418](#ch10#page_418)
*   运行时错误检查, [6](#ch01#page_6)–[8](#ch01#page_8)

### S

*   作用域, 全局作用域, [147](#ch05#page_147)
*   作用域错误, [147](#ch05#page_147)–[148](#ch05#page_148)
*   脚本, [399](#ch10#page_399)
*   安全
*   `eval` 和 `exec` 内置函数, [446](#ch10#page_446)
*   `pickle` 模块, [526](#ch12#page_526)
*   半结构化数据, [37](#ch01#page_37)–[39](#ch01#page_39)
*   `send` 方法, [189](#ch06#page_189)–[191](#ch06#page_191)
*   序列, [261](#ch07#page_261)–[264](#ch07#page_264). _参见_ [列表/s](#index#idx257)
*   空序列, 循环遍历, [83](#ch03#page_83)
*   切片, [67](#ch02#page_67)–[70](#ch02#page_70)
*   `ServerMissingKeyError` 异常, [433](#ch10#page_433)
*   `setdefault` 方法, [120](#ch04#page_120)–[121](#ch04#page_121), [122](#ch04#page_122)–[123](#ch04#page_123), [125](#ch04#page_125)
*   集合
*   不可变对象, [256](#ch07#page_256)–[260](#ch07#page_260)
*   迭代集合, [93](#ch03#page_93), [96](#ch03#page_96)
*   setter 方法, [266](#ch08#page_266)–[269](#ch08#page_269)
*   `setUpModule` 函数, [548](#ch13#page_548)–[549](#ch13#page_549)
*   `simulate` 函数, [365](#ch09#page_365)–[367](#ch09#page_367)
*   单分派, [212](#ch07#page_212)–[216](#ch07#page_216). _参见_ [OOP (面向对象编程)](#index#idx297)
*   单元素元组
*   括号, [16](#ch01#page_16)–[17](#ch01#page_17)
*   尾部逗号, [17](#ch01#page_17)–[18](#ch01#page_18)
*   切片, [67](#ch02#page_67)–[68](#ch02#page_68), [70](#ch02#page_70)
*   索引, [67](#ch02#page_67)–[69](#ch02#page_69)
*   `memoryview`, [487](#ch11#page_487)–[488](#ch11#page_488)
*   步幅语法, [70](#ch02#page_70)–[72](#ch02#page_72)
*   语法, [67](#ch02#page_67)
*   `sort` 方法, [145](#ch05#page_145)–[149](#ch05#page_149), [201](#ch07#page_201)–[202](#ch07#page_202), [493](#ch12#page_493)–[501](#ch12#page_501)
*   `sorted` 函数, [499](#ch12#page_499)–[501](#ch12#page_501)
*   加速, [319](#ch09#page_319)
*   暂存修改, [96](#ch03#page_96)–[97](#ch03#page_97)
*   星号参数, [150](#ch05#page_150)–[152](#ch05#page_152)
*   星号表达式, [73](#ch02#page_73)–[76](#ch02#page_76), [140](#ch05#page_140)
*   语句/s, [4](#ch01#page_4)–[5](#ch01#page_5)
*   `assert`, [404](#ch10#page_404)–[408](#ch10#page_408), [442](#ch10#page_442)–[443](#ch10#page_443)
*   `break`, [82](#ch03#page_82)–[83](#ch03#page_83), [85](#ch03#page_85)–[86](#ch03#page_86)
*   `for`, [79](#ch03#page_79), [80](#ch03#page_80)
*   `if`, [19](#ch01#page_19)
*   `import`, [5](#ch01#page_5), [592](#ch14#page_592)
*   `match`, [30](#ch01#page_30)–[39](#ch01#page_39), [370](#ch09#page_370)
*   `nonlocal`, [148](#ch05#page_148)–[149](#ch05#page_149)
*   `raise`, [405](#ch10#page_405)–[408](#ch10#page_408)
*   `with`, [408](#ch10#page_408)–[412](#ch10#page_412)
*   静态分析, [613](#ch14#page_613)–[621](#ch14#page_621)
*   静态错误, [7](#ch01#page_7)
*   `StopIteration` 异常, [88](#ch03#page_88), [198](#ch06#page_198), [438](#ch10#page_438)
*   `str`, [41](#ch02#page_41)–[46](#ch02#page_46), [58](#ch02#page_58)–[62](#ch02#page_62), [524](#ch12#page_524)
*   `str.format` 方法, [54](#ch02#page_54)–[55](#ch02#page_55)
*   严格关键字, `zip` 函数, [81](#ch03#page_81)
*   步幅切片, [70](#ch02#page_70)–[72](#ch02#page_72)
*   字符串/s
*   高级格式化, [52](#ch02#page_52)–[55](#ch02#page_55)
*   连接, [62](#ch02#page_62)–[66](#ch02#page_66)
*   C 风格格式化, [47](#ch02#page_47)–[52](#ch02#page_52)
*   索引, [10](#ch01#page_10)–[11](#ch01#page_11)
*   插值格式化, [56](#ch02#page_56)–[58](#ch02#page_58)
*   字面值, [63](#ch02#page_63)
*   `repr`, [58](#ch02#page_58)–[62](#ch02#page_62)
*   表示对象为字符串, [223](#ch07#page_223)–[224](#ch07#page_224)
*   子类/es
*   保护属性, [247](#ch07#page_247)–[250](#ch07#page_250)
*   验证, [287](#ch08#page_287)–[291](#ch08#page_291)
*   `subprocess` 模块, 管理子进程, [320](#ch09#page_320)–[324](#ch09#page_324)
*   `super` 函数, [238](#ch07#page_238)–[240](#ch07#page_240)
*   超类, [207](#ch07#page_207), [297](#ch08#page_297)
*   SWIG, [461](#ch11#page_461)
*   语法
*   切片语法, [67](#ch02#page_67)–[68](#ch02#page_68)
*   步幅语法, [70](#ch02#page_70)–[72](#ch02#page_72)
*   解包语法, [12](#ch01#page_12)–[15](#ch01#page_15), [138](#ch05#page_138)–[139](#ch05#page_139)
*   `SyntaxError` 异常, [533](#ch13#page_533)
*   系统调用, [327](#ch09#page_327)–[329](#ch09#page_329)

### T

*   `takewhile` 函数, [104](#ch03#page_104)–[105](#ch03#page_105)
*   作为目标启用, [410](#ch10#page_410)–[412](#ch10#page_412)
*   `tearDownModule` 函数, [548](#ch13#page_548)–[549](#ch13#page_549)
*   `tee` 函数, [103](#ch03#page_103)
*   三元操作符, [19](#ch01#page_19)–[20](#ch01#page_20)
*   `TestCase` 子类, [535](#ch13#page_535)–[541](#ch13#page_541), [547](#ch13#page_547)–[548](#ch13#page_548)
*   测试/s, [533](#ch13#page_533). _参见_ [调试](#index#idx132)
*   封装依赖测试, [559](#ch13#page_559)–[562](#ch13#page_562)
*   浮点数测试, [563](#ch13#page_563)–[565](#ch13#page_565)
*   测试框架, [547](#ch13#page_547)–[549](#ch13#page_549)
*   集成测试, [541](#ch13#page_541)–[542](#ch13#page_542)
*   模拟对象测试, [550](#ch13#page_550)–[558](#ch13#page_558)
*   `TestCase` 子类测试, [535](#ch13#page_535)–[541](#ch13#page_541)
*   单元测试, [542](#ch13#page_542)–[547](#ch13#page_547)
*   `unittest` 模块, [533](#ch13#page_533)–[535](#ch13#page_535)
*   线程 I/O, 移植到 asyncio, [368](#ch09#page_368)–[381](#ch09#page_381)
*   `threading` 模块, [332](#ch09#page_332)
*   `ThreadPoolExecutor` 类, [361](#ch09#page_361)–[363](#ch09#page_363), [394](#ch09#page_394)–[397](#ch09#page_397)
*   线程/s, [319](#ch09#page_319). _参见_ [并发](#index#idx103); [并行](#index#idx308)
*   避免用于按需扇出, [349](#ch09#page_349)–[353](#ch09#page_353)
*   阻塞 I/O 线程, [327](#ch09#page_327)–[329](#ch09#page_329)
*   与协程结合, [381](#ch09#page_381)–[384](#ch09#page_384)
*   协调线程间工作, [333](#ch09#page_333)–[344](#ch09#page_344)
*   与协程的对比, [364](#ch09#page_364)
*   与协程的互操作性, [381](#ch09#page_381)–[384](#ch09#page_384)
*   锁, [332](#ch09#page_332)–[333](#ch09#page_333)
*   抢占式线程, [331](#ch09#page_331)–[333](#ch09#page_333)
*   防止数据竞争, [330](#ch09#page_330)–[333](#ch09#page_333)
*   Python 对线程的支持, [327](#ch09#page_327)–[329](#ch09#page_329)
*   工作线程, [330](#ch09#page_330)–[331](#ch09#page_331), [335](#ch09#page_335)–[337](#ch09#page_337), [339](#ch09#page_339)–[340](#ch09#page_340), [342](#ch09#page_342), [354](#ch09#page_354), [358](#ch09#page_358), [389](#ch09#page_389)–[392](#ch09#page_392)
*   `throw` 方法, [195](#ch06#page_195)–[199](#ch06#page_199)
*   `time` 模块, [519](#ch12#page_519)–[521](#ch12#page_521)
*   `timeit` 微基准测试, [453](#ch11#page_453)–[458](#ch11#page_458)
*   `title` 方法, [50](#ch02#page_50)
*   工具. _参见_ [itertools](#index#idx242); [模块](#index#idx276)
*   `black`, [5](#ch01#page_5)–[6](#ch01#page_6)
*   Cython, [461](#ch11#page_461)
*   错误检查工具, [8](#ch01#page_8)
*   `mypy`, [115](#ch04#page_115)–[116](#ch04#page_116)
*   `Mypyc`, [461](#ch11#page_461)
*   `pip`, [575](#ch14#page_575)–[577](#ch14#page_577)
*   静态分析工具, [614](#ch14#page_614)–[621](#ch14#page_621)
*   SWIG, [461](#ch11#page_461)
*   `timeit`, [457](#ch11#page_457)–[458](#ch11#page_458)
*   `venv`, [578](#ch14#page_578)–[580](#ch14#page_580)
*   `trace_func` 装饰器, [312](#ch08#page_312)–[313](#ch08#page_313)
*   堆栈跟踪, [424](#ch10#page_424)–[436](#ch10#page_436)
*   `tracemalloc` 模块, [572](#ch13#page_572)–[573](#ch13#page_573)
*   `TraceMeta` 元类, [313](#ch08#page_313)–[314](#ch08#page_314)
*   尾部逗号, 单元素元组, [17](#ch01#page_17)–[18](#ch01#page_18)
*   树遍历, [206](#ch07#page_206)
*   try 块, [412](#ch10#page_412)–[414](#ch10#page_414)
*   try/except/else 块, [400](#ch10#page_400)–[402](#ch10#page_402)
*   try/except/else/finally 块, [402](#ch10#page_402)–[404](#ch10#page_404)
*   try/finally 块, [399](#ch10#page_399)–[400](#ch10#page_400)
*   元组/s, [11](#ch01#page_11)–[12](#ch01#page_12), [131](#ch04#page_131)
*   比较器方法, [496](#ch12#page_496)
*   将对象转换为元组, [224](#ch07#page_224)–[225](#ch07#page_225)
*   空元组, [16](#ch01#page_16)
*   扩展元组, [131](#ch04#page_131)
*   字面值元组, [16](#ch01#page_16)
*   嵌套元组, [127](#ch04#page_127)–[130](#ch04#page_130)
*   单元素元组, [16](#ch01#page_16)
*   括号, [16](#ch01#page_16)–[17](#ch01#page_17)
*   尾部逗号, [17](#ch01#page_17)–[18](#ch01#page_18)
*   双元素元组, [143](#ch05#page_143)
*   类型注解, [115](#ch04#page_115)–[116](#ch04#page_116), [144](#ch05#page_144)–[145](#ch05#page_145), [254](#ch07#page_254), [586](#ch14#page_586)–[587](#ch14#page_587)
*   类型检查器, 静态类型检查器, [613](#ch14#page_613)–[621](#ch14#page_621)
*   类型注册, [293](#ch08#page_293)–[299](#ch08#page_299)
*   `typing` 模块, [613](#ch14#page_613)–[621](#ch14#page_621)

### U

*   下划线 (`_`), [213](#ch07#page_213)
*   Unicode
*   Unicode 到二进制转换, [42](#ch02#page_42)
*   代码点, [42](#ch02#page_42)
*   Unicode 夹心, [42](#ch02#page_42)–[43](#ch02#page_43)
*   单元测试, [542](#ch13#page_542)–[547](#ch13#page_547)
*   `unittest` 模块, [533](#ch13#page_533)–[535](#ch13#page_535), [548](#ch13#page_548)
*   解包, [12](#ch01#page_12)–[15](#ch01#page_15)
*   捕获式解包, [72](#ch02#page_72)–[76](#ch02#page_76), [138](#ch05#page_138)–[139](#ch05#page_139)
*   多个返回值解包, [138](#ch05#page_138)–[141](#ch05#page_141)
*   多重赋值解包, [11](#ch01#page_11)–[15](#ch01#page_15)
*   `update` 方法, [96](#ch03#page_96)
*   用户自定义类, [137](#ch05#page_137)
*   UTC (协调世界时), [519](#ch12#page_519)
*   工具函数, [451](#ch11#page_451)

### V

*   验证, 子类验证, [287](#ch08#page_287)–[291](#ch08#page_291)
*   `ValueError` 异常, [401](#ch10#page_401)
*   可变参数, [150](#ch05#page_150)–[152](#ch05#page_152)
*   变量/s
*   `__debug__`, [443](#ch10#page_443)–[444](#ch10#page_444)
*   别名变量, [136](#ch05#page_136)
*   `count` 变量, [24](#ch01#page_24)–[26](#ch01#page_26)
*   异常变量, [414](#ch10#page_414)–[416](#ch10#page_416)
*   `for` 循环变量, [85](#ch03#page_85)–[86](#ch03#page_86)
*   作用域变量, [147](#ch05#page_147)–[148](#ch05#page_148)
*   `venv`, [578](#ch14#page_578)–[580](#ch14#page_580)
*   版本
*   类版本, [530](#ch12#page_530)–[531](#ch12#page_531)
*   模块版本, [577](#ch14#page_577)–[578](#ch14#page_578)
*   Python 版本 [2](#ch01#page_2), [2](#ch01#page_2)
*   Python 版本 [3](#ch01#page_3), [2](#ch01#page_2)–[3](#ch01#page_3)

### W

*   海象操作符, [24](#ch01#page_24)–[30](#ch01#page_30), [179](#ch06#page_179). _参见_ [赋值表达式](#index#idx44)
*   `warnings` 模块, [605](#ch14#page_605)–[613](#ch14#page_613)
*   波形生成器, [189](#ch06#page_189)–[195](#ch06#page_195)
*   `while` 循环, [29](#ch01#page_29), [82](#ch03#page_82)–[84](#ch03#page_84), [382](#ch09#page_382)–[383](#ch09#page_383)
*   空白字符, [3](#ch01#page_3)–[4](#ch01#page_4)
*   `with` 语句, [408](#ch10#page_408)–[412](#ch10#page_412)
*   wordcode, [324](#ch09#page_324)–[325](#ch09#page_325)
*   工作线程, [330](#ch09#page_330)–[331](#ch09#page_331), [335](#ch09#page_335)–[337](#ch09#page_337), [339](#ch09#page_339)–[340](#ch09#page_340), [342](#ch09#page_342), [354](#ch09#page_354), [358](#ch09#page_358), [389](#ch09#page_389)–[392](#ch09#page_392)
*   包装器函数, [168](#ch05#page_168)
*   `wraps` 函数, [168](#ch05#page_168)–[169](#ch05#page_169)
*   写入二进制模式, [45](#ch02#page_45)
*   写入文本模式, [45](#ch02#page_45)

### X-Y-Z

*   `yield` 表达式, [187](#ch06#page_187)–[188](#ch06#page_188), [409](#ch10#page_409)–[410](#ch10#page_410)
*   《Python 之禅》, [4](#ch01#page_4)
*   零拷贝操作, [487](#ch11#page_487)–[491](#ch11#page_491)
*   `zip` 函数, [80](#ch03#page_80)–[81](#ch03#page_81)
*   `zip_longest` 函数, [81](#ch03#page_81), [103](#ch03#page_103)–[104](#ch03#page_104)
*   `zipimport` 模块, [622](#ch14#page_622)–[624](#ch14#page_624)
*   `zoneinfo` 模块, [522](#ch12#page_522)–[523](#ch12#page_523)

---
<a role="toc_link" id="bm01"></a>
![Images](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/bm01_c1bc3d50.jpg)
---
<a role="toc_link" id="ch01_images"></a>

## Effective Python - Code Snippets

## 代码片段

许多标题包含编程代码或配置示例。为了优化这些元素的呈现，请在单栏横向模式下查看电子书，并将字体大小调整到最小。除了以可重排文本格式呈现代码和配置外，我们还包含了代码的图像，这些图像模仿了印刷书籍中的呈现方式；因此，在可重排格式可能影响代码列表呈现效果的地方，您会看到一个“点击此处查看代码图像”的链接。点击该链接即可查看与印刷版一致的代码图像。要返回到之前查看的页面，请点击设备或应用程序上的“返回”按钮。

[![Images](./images/#af0002-01)](ch01.xhtml#f0002-01a)
[![Images](./images/#af0002-02)](ch01.xhtml#f0002-02a)
[![Images](./images/#af0002-03)](ch01.xhtml#f0002-03a)
[![Images](./images/#af0006-01)](ch01.xhtml#f0006-01a)
[![Images](./images/#af0007-01)](ch01.xhtml#f0007-01a)
[![Images](./images/#af0007-02)](ch01.xhtml#f0007-02a)
[![Images](./images/#af0008-01)](ch01.xhtml#f0008-01a)
[![Images](./images/#af0009-01)](ch01.xhtml#f0009-01a)
[![Images](./images/#af0009-02)](ch01.xhtml#f0009-02a)
[![Images](./images/#af0009-03)](ch01.xhtml#f0009-03a)
[![Images](./images/#af0010-01)](ch01.xhtml#f0010-01a)
[![Images](./images/#af0010-02)](ch01.xhtml#f0010-02a)
[![Images](./images/#af0011-01)](ch01.xhtml#f0011-01a)
[![Images](./images/#af0011-02)](ch01.xhtml#f0011-02a)
[![Images](./images/#af0011-03)](ch01.xhtml#f0011-03a)
[![Images](./images/#af0012-01)](ch01.xhtml#f0012-01a)
[![Images](./images/#af0012-02)](ch01.xhtml#f0012-02a)
[![Images](./images/#af0012-03)](ch01.xhtml#f0012-03a)
[![Images](./images/#af0013-01)](ch01.xhtml#f0013-01a)
[![Images](./images/#af0013-02)](ch01.xhtml#f0013-02a)
[![Images](./images/#af0013-03)](ch01.xhtml#f0013-03a)
[![Images](./images/#af0014-01)](ch01.xhtml#f0013-03a)
[![Images](./images/#af0014-01a)](ch01.xhtml#f0014-01aa)
[![Images](./images/#af0014-02)](ch01.xhtml#f0014-02a)
[![Images](./images/#af0015-01)](ch01.xhtml#f0014-02a)
[![Images](./images/#af0015-02)](ch01.xhtml#f0015-02a)
[![Images](./images/#af0016-01)](ch01.xhtml#f0016-01a)
[![Images](./images/#af0016-02)](ch01.xhtml#f0016-02a)
[![Images](./images/#af0017-01)](ch01.xhtml#f0017-01a)
[![Images](./images/#af0017-02)](ch01.xhtml#f0017-02a)
[![Images](./images/#af0017-03)](ch01.xhtml#f0017-03a)
[![Images](./images/#af0018-01)](ch01.xhtml#f0018-01a)
[![Images](./images/#af0018-02)](ch01.xhtml#f0018-02a)
[![Images](./images/#af0019-01)](ch01.xhtml#f0019-01a)
[![Images](./images/#af0020-01)](ch01.xhtml#f0020-01a)
[![Images](./images/#af0020-02)](ch01.xhtml#f0020-02a)
[![Images](./images/#af0021-01)](ch01.xhtml#f0021-01a)
[![Images](./images/#af0021-02)](ch01.xhtml#f0021-02a)
[![Images](./images/#af0021-03)](ch01.xhtml#f0021-03a)
[![Images](./images/#af0022-01)](ch01.xhtml#f0022-01a)
[![Images](./images/#af0022-02a)](ch01.xhtml#f0022-02aa)
[![Images](./images/#af0022-02)](ch01.xhtml#f0022-02a)
[![Images](./images/#af0024-01)](ch01.xhtml#f0024-01a)
[![Images](./images/#af0025-01)](ch01.xhtml#f0025-01a)
[![Images](./images/#af0025-02)](ch01.xhtml#f0025-02a)
[![Images](./images/#af0026-01)](ch01.xhtml#f0026-01a)
[![Images](./images/#af0026-02)](ch01.xhtml#f0026-02a)
[![Images](./images/#af0027-01)](ch01.xhtml#f0027-01a)
[![Images](./images/#af0027-02)](ch01.xhtml#f0027-02a)
[![Images](./images/#af0027-03)](ch01.xhtml#f0027-03a)
[![Images](./images/#af0028-01)](ch01.xhtml#f0027-03a)
[![Images](./images/#af0028-02)](ch01.xhtml#f0028-02a)
[![Images](./images/#af0028-03)](ch01.xhtml#f0028-03a)
[![Images](./images/#af0029-01)](ch01.xhtml#f0029-01a)
[![Images](./images/#af0029-02)](ch01.xhtml#f0029-02a)
[![Images](./images/#af0030-01)](ch01.xhtml#f0030-01a)
[![Images](./images/#af0031-01)](ch01.xhtml#f0031-01a)
[![Images](./images/#af0031-03)](ch01.xhtml#f0031-03a)
[![Images](./images/#af0032-01)](ch01.xhtml#f0032-01a)
[![Images](./images/#af0032-02)](ch01.xhtml#f0032-02a)
[![Images](./images/#af0033-01)](ch01.xhtml#f0033-01a)
[![Images](./images/#af0033-02)](ch01.xhtml#f0033-02a)
[![Images](./images/#af0033-03)](ch01.xhtml#f0033-03a)
[![Images](./images/#af0034-01)](ch01.xhtml#f0033-03a)
[![Images](./images/#af0034-02)](ch01.xhtml#f0034-02a)
[![Images](./images/#af0035-01)](ch01.xhtml#f0035-01a)
[![Images](./images/#af0035-02)](ch01.xhtml#f0035-02a)
[![Images](./images/#af0035-03)](ch01.xhtml#f0035-03a)
[![Images](./images/#af0035-04)](ch01.xhtml#f0035-04a)
[![Images](./images/#af0036-01)](ch01.xhtml#f0036-01a)
[![Images](./images/#af0036-02)](ch01.xhtml#f0036-02a)
[![Images](./images/#af0037-01)](ch01.xhtml#f0037-01a)
[![Images](./images/#af0037-02)](ch01.xhtml#f0037-02a)
[![Images](./images/#af0038-01)](ch01.xhtml#f0038-01a)
[![Images](./images/#af0038-02)](ch01.xhtml#f0038-02a)
[![Images](./images/#af0038-03)](ch01.xhtml#f0038-03a)
[![Images](./images/#af0039-01)](ch01.xhtml#f0039-01a)
---
<a role="toc_link" id="ch02_images"></a>
[![Images](./images/#af0042-01)](ch02.xhtml#f0042-01a)
[![Images](./images/#af0042-02)](ch02.xhtml#f0042-02a)
[![Images](./images/#af0043-01)](ch02.xhtml#f0042-02a)
[![Images](./images/#af0043-02)](ch02.xhtml#f0043-02a)
[![Images](./images/#af0043-03)](ch02.xhtml#f0043-03a)
[![Images](./images/#af0044-01)](ch02.xhtml#f0044-01a)
[![Images](./images/#af0044-02)](ch02.xhtml#f0044-02a)
[![Images](./images/#af0044-03)](ch02.xhtml#f0044-03a)
[![Images](./images/#af0045-01)](ch02.xhtml#f0045-01a)
[![Images](./images/#af0045-02)](ch02.xhtml#f0045-02a)
[![Images](./images/#af0045-03)](ch02.xhtml#f0045-03a)
[![Images](./images/#af0046-01)](ch02.xhtml#f0046-01a)
[![Images](./images/#af0046-02)](ch02.xhtml#f0046-02a)
[![Images](./images/#af0046-03)](ch02.xhtml#f0046-03a)
[![Images](./images/#af0047-01)](ch02.xhtml#f0047-01a)
[![Images](./images/#af0048-01)](ch02.xhtml#f0048-01a)
[![Images](./images/#af0048-02)](ch02.xhtml#f0048-02a)
[![Images](./images/#af0048-03)](ch02.xhtml#f0048-03a)
[![Images](./images/#af0049-01)](ch02.xhtml#f0049-01a)
[![Images](./images/#af0049-02)](ch02.xhtml#f0049-02a)
[![Images](./images/#af0049-03)](ch02.xhtml#f0049-03a)
[![Images](./images/#af0050-01)](ch02.xhtml#f0050-01a)
[![Images](./images/#af0050-02)](ch02.xhtml#f0050-02a)
[![Images](./images/#af0050-03)](ch02.xhtml#f0050-03a)
[![Images](./images/#af0051-01)](ch02.xhtml#f0050-03a)
[![Images](./images/#af0051-02)](ch02.xhtml#f0051-02a)
[![Images](./images/#af0051-03)](ch02.xhtml#f0051-03a)
[![Images](./images/#af0052-01)](ch02.xhtml#f0052-01a)
[![Images](./images/#af0053-01)](ch02.xhtml#f0053-01a)
[![Images](./images/#af0053-02)](ch02.xhtml#f0053-02a)
[![Images](./images/#af0053-03)](ch02.xhtml#f0053-03a)
[![Images](./images/#af0054-01)](ch02.xhtml#f0054-01a)
[![Images](./images/#af0054-02)](ch02.xhtml#f0054-02a)
[![Images](./images/#af0054-03)](ch02.xhtml#f0054-03a)
[![Images](./images/#af0054-04)](ch02.xhtml#f0054-04a)
[![Images](./images/#af0055-01)](ch02.xhtml#f0055-01a)
[![Images](./images/#af0056-01)](ch02.xhtml#f0056-01a)
[![Images](./images/#af0056-02)](ch02.xhtml#f0056-02a)
[![Images](./images/#af0056-03)](ch02.xhtml#f0056-03a)
[![Images](./images/#af0057-01)](ch02.xhtml#f0056-03a)
[![Images](./images/#af0057-02)](ch02.xhtml#f0057-02a)
[![Images](./images/#af0057-03)](ch02.xhtml#f0057-03a)
[![Images](./images/#af0058-01)](ch02.xhtml#f0058-01a)
[![Images](./images/#af0059-01)](ch02.xhtml#f0059-01a)
[![Images](./images/#af0059-03)](ch02.xhtml#f0059-03a)
[![Images](./images/#af0060-01)](ch02.xhtml#f0059-03a)
[![Images](./images/#af0060-02)](ch02.xhtml#f0060-02a)
[![Images](./images/#af0061-01)](ch02.xhtml#f0061-01a)
[![Images](./images/#af0061-02)](ch02.xhtml#f0061-02a)
[![Images](./images/#af0062-01)](ch02.xhtml#f0062-01a)
[![Images](./images/#af0062-02)](ch02.xhtml#f0062-02a)
[![Images](./images/#af0063-01)](ch02.xhtml#f0063-01a)
[![Images](./images/#af0063-02)](ch02.xhtml#f0063-02a)
[![Images](./images/#af0064-01)](ch02.xhtml#f0064-01a)
[![Images](./images/#af0064-02)](ch02.xhtml#f0064-02a)
[![Images](./images/#af0064-03)](ch02.xhtml#f0064-03a)
[![Images](./images/#af0064-04)](ch02.xhtml#f0064-04a)
[![Images](./images/#af0065-01)](ch02.xhtml#f0065-01a)
[![Images](./images/#af0065-02)](ch02.xhtml#f0065-02a)
[![Images](./images/#af0065-03)](ch02.xhtml#f0065-03a)
[![Images](./images/#af0065-04)](ch02.xhtml#f0065-04a)
[![Images](./images/#af0065-05)](ch02.xhtml#f0065-05a)
[![Images](./images/#af0066-01)](ch02.xhtml#f0065-05a)
[![Images](./images/#af0066-02)](ch02.xhtml#f0066-02a)
[![Images](./images/#af0067-01)](ch02.xhtml#f0067-01a)
[![Images](./images/#af0067-02)](ch02.xhtml#f0067-02a)
[![Images](./images/#af0068-01)](ch02.xhtml#f0068-01a)
[![Images](./images/#af0068-02)](ch02.xhtml#f0068-02a)
[![Images](./images/#af0069-01)](ch02.xhtml#f0069-01a)
[![Images](./images/#af0069-02)](ch02.xhtml#f0069-02a)
[![Images](./images/#af0069-03)](ch02.xhtml#f0069-03a)
[![Images](./images/#af0070-01)](ch02.xhtml#f0070-01a)
[![Images](./images/#af0071-01)](ch02.xhtml#f0071-01a)
[![Images](./images/#af0071-02)](ch02.xhtml#f0071-02a)
[![Images](./images/#af0071-03)](ch02.xhtml#f0071-03a)
[![Images](./images/#af0071-04)](ch02.xhtml#f0071-04a)
[![Images](./images/#af0072-01)](ch02.xhtml#f0072-01a)
[![Images](./images/#af0072-02)](ch02.xhtml#f0072-02a)
[![Images](./images/#af0073-01)](ch02.xhtml#f0073-01a)
[![Images](./images/#af0073-02)](ch02.xhtml#f0073-02a)
[![Images](./images/#af0073-03)](ch02.xhtml#f0073-03a)
[![Images](./images/#af0074-01)](ch02.xhtml#f0074-01a)
[![Images](./images/#af0074-02)](ch02.xhtml#f0074-02a)
[![Images](./images/#af0074-03)](ch02.xhtml#f0074-03a)
[![Images](./images/#af0075-01)](ch02.xhtml#f0075-01a)
[![Images](./images/#af0075-02)](ch02.xhtml#f0075-02a)
[![Images](./images/#af0075-03)](ch02.xhtml#f0075-03a)
[![Images](./images/#af0075-04)](ch02.xhtml#f0075-04a)
---
<a role="toc_link" id="ch03_images"></a>
[![Images](./images/#af0077-01)](ch03.xhtml#f0077-01a)
[![Images](./images/#af0078-01)](ch03.xhtml#f0077-01a)
[![Images](./images/#af0078-02)](ch03.xhtml#f0078-02a)
[![Images](./images/#af0078-03)](ch03.xhtml#f0078-03a)
[![Images](./images/#af0079-01)](ch03.xhtml#f0079-01a)
[![Images](./images/#af0079-02)](ch03.xhtml#f0079-02a)
[![Images](./images/#af0079-03)](ch03.xhtml#f0079-03a)
[![Images](./images/#af0080-01)](ch03.xhtml#f0080-01a)
[![Images](./images/#af0080-02)](ch03.xhtml#f0080-02a)
[![Images](./images/#af0080-03)](ch03.xhtml#f0080-03a)
[![Images](./images/#af0081-01)](ch03.xhtml#f0081-01a)
[![Images](./images/#af0081-02)](ch03.xhtml#f0081-02a)
[![Images](./images/#af0083-01)](ch03.xhtml#f0083-01a)
[![Images](./images/#af0083-02)](ch03.xhtml#f0083-02a)
[![Images](./images/#af0084-01)](ch03.xhtml#f0084-01a)
[![Images](./images/#af0084-02)](ch03.xhtml#f0084-02a)
[![Images](./images/#af0085-01)](ch03.xhtml#f0085-01a)
[![Images](./images/#af0085-02)](ch03.xhtml#f0085-02a)
[![Images](./images/#af0086-01)](ch03.xhtml#f0086-01a)
[![Images](./images/#af0086-02)](ch03.xhtml#f0086-02a)
[![Images](./images/#af0087-01)](ch03.xhtml#f0087-01a)
[![Images](./images/#af0087-02)](ch03.xhtml#f0087-02a)
[![Images](./images/#af0087-03)](ch03.xhtml#f0087-03a)
[![Images](./images/#af0088-01)](ch03.xhtml#f0088-01a)
[![Images](./images/#af0088-02)](ch03.xhtml#f0088-02a)
[![Images](./images/#af0088-03)](ch03.xhtml#f0088-03a)
[![Images](./images/#af0088-04)](ch03.xhtml#f0088-04a)
[![Images](./images/#af0089-01)](ch03.xhtml#f0088-04a)
[![Images](./images/#af0089-02)](ch03.xhtml#f0089-02a)
[![Images](./images/#af0089-03)](ch03.xhtml#f0089-03a)
[![Images](./images/#af0090-01)](ch03.xhtml#f0090-01a)
[![Images](./images/#af0090-02)](ch03.xhtml#f0090-02a)
[![Images](./images/#af0090-03)](ch03.xhtml#f0090-03a)
[![Images](./images/#af0091-01)](ch03.xhtml#f0090-03a)
[![Images](./images/#af0091-02)](ch03.xhtml#f0091-02a)
[![Images](./images/#af0091-03)](ch03.xhtml#f0091-03a)
[![Images](./images/#af0091-04)](ch03.xhtml#f0091-04a)
[![Images](./images/#af0092-01)](ch03.xhtml#f0092-01a)
[![Images](./images/#af0092-02)](ch03.xhtml#f0092-02a)
[![Images](./images/#af0093-01)](ch03.xhtml#f0092-02a)
[![Images](./images/#af0093-02)](ch03.xhtml#f0093-02a)
[![Images](./images/#af0093-03)](ch03.xhtml#f0093-03a)
[![Images](./images/#af0093-04)](ch03.xhtml#f0093-04a)
[![Images](./images/#af0094-01)](ch03.xhtml#f0094-01a)
[![Images](./images/#af0094-02)](ch03.xhtml#f0094-02a)
[![Images](./images/#af0094-03)](ch03.xhtml#f0094-03a)
[![Images](./images/#af0095-01)](ch03.xhtml#f0094-03a)
[![Images](./images/#af0095-02)](ch03.xhtml#f0095-02a)
[![Images](./images/#af0095-03)](ch03.xhtml#f0095-03a)
[![Images](./images/#af0096-01)](ch03.xhtml#f0096-01a)
[![Images](./images/#af0096-02)](ch03.xhtml#f0096-02a)
[![Images](./images/#af0096-03)](ch03.xhtml#f0096-03a)
[![Images](./images/#af0097-01)](ch03.xhtml#f0096-03a)
[![Images](./images/#af0097-02)](ch03.xhtml#f0097-02a)
[![Images](./images/#af0098-01)](ch03.xhtml#f0098-01a)
[![Images](./images/#af0098-02)](ch03.xhtml#f0098-02a)
[![Images](./images/#af0099-01)](ch03.xhtml#f0099-01a)
[![Images](./images/#af0099-02)](ch03.xhtml#f0099-02a)
[![Images](./images/#af0100-01)](ch03.xhtml#f0100-01a)
[![Images](./images/#af0100-02)](ch03.xhtml#f0100-02a)
[![Images](./images/#af0101-01)](ch03.xhtml#f0101-01a)
[![Images](./images/#af0101-02)](ch03.xhtml#f0101-02a)
[![Images](./images/#af0101-03)](ch03.xhtml#f0101-03a)
[![Images](./images/#af0102-01)](ch03.xhtml#f0102-01a)
[![Images](./images/#af0102-02)](ch03.xhtml#f0102-02a)
[![Images](./images/#af0103-01)](ch03.xhtml#f0103-01a)
[![Images](./images/#af0103-02)](ch03.xhtml#f0103-02a)
[![Images](./images/#af0103-03)](ch03.xhtml#f0103-03a)
[![Images](./images/#af0103-04)](ch03.xhtml#f0103-04a)
[![Images](./images/#af0104-01)](ch03.xhtml#f0103-04a)
[![Images](./images/#af0104-02)](ch03.xhtml#f0104-02a)
[![Images](./images/#af0104-03)](ch03.xhtml#f0104-03a)
[![Images](./images/#af0105-01)](ch03.xhtml#f0104-03a)
[![Images](./images/#af0105-02)](ch03.xhtml#f0105-02a)
[![Images](./images/#af0105-03)](ch03.xhtml#f0105-03a)
[![Images](./images/#af0106-01)](ch03.xhtml#f0106-01a)
[![Images](./images/#af0106-02)](ch03.xhtml#f0106-02a)
[![Images](./images/#af0106-03)](ch03.xhtml#f0106-03a)
[![Images](./images/#af0106-04)](ch03.xhtml#f0106-04a)
[![Images](./images/#af0107-01)](ch03.xhtml#f0106-04a)
[![Images](./images/#af0107-02)](ch03.xhtml#f0107-02a)
[![Images](./images/#af0107-03)](ch03.xhtml#f0107-03a)
[![Images](./images/#af0108-01)](ch03.xhtml#f0108-01a)
[![Images](./images/#af0108-02)](ch03.xhtml#f0108-02a)
---
<a role="toc_link" id="ch04_images"></a>
[![Images](./images/#af0109-01)](ch04.xhtml#f0109-01a)
[![Images](./images/#af0110-01)](ch04.xhtml#f0109-01a)
[![Images](./images/#af0110-02)](ch04.xhtml#f0110-02a)
[![Images](./images/#af0110-03)](ch04.xhtml#f0110-03a)
[![Images](./images/#af0111-01)](ch04.xhtml#f0111-01a)
[![Images](./images/#af0111-02)](ch04.xhtml#f0111-02a)
[![Images](./images/#af0111-03)](ch04.xhtml#f0111-03a)
[![Images](./images/#af0112-02)](ch04.xhtml#f0112-02a)
[![Images](./images/#af0112-03)](ch04.xhtml#f0112-03a)
[![Images](./images/#af0113-01)](ch04.xhtml#f0113-01a)
[![Images](./images/#af0113-02)](ch04.xhtml#f0113-02a)
[![Images](./images/#af0114-01)](ch04.xhtml#f0114-01a)
[![Images](./images/#af0114-02)](ch04.xhtml#f0114-02a)
[![Images](./images/#af0115-01)](ch04.xhtml#f0115-01a)
[![Images](./images/#af0115-02)](ch04.xhtml#f0115-02a)
[![Images](./images/#af0115-03)](ch04.xhtml#f0115-03a)
[![Images](./images/#af0116-01)](ch04.xhtml#f0115-03a)
[![Images](./images/#af0117-01)](ch04.xhtml#f0117-01a)
[![Images](./images/#af0119-01)](ch04.xhtml#f0119-01a)
[![Images](./images/#af0120-01)](ch04.xhtml#f0120-01a)
[![Images](./images/#af0120-02)](ch04.xhtml#f0120-02a)
[![Images](./images/#af0121-01)](ch04.xhtml#f0121-01a)
[![Images](./images/#af0122-01)](ch04.xhtml#f0122-01a)
[![Images](./images/#af0122-02)](ch04.xhtml#f0122-02a)
[![Images](./images/#af0123-01)](ch04.xhtml#f0123-01a)
[![Images](./images/#af0123-02)](ch04.xhtml#f0123-02a)
[![Images](./images/#af0123-03)](ch04.xhtml#f0123-03a)
[![Images](./images/#af0124-01)](ch04.xhtml#f0123-03a)
[![Images](./images/#af0125-01)](ch04.xhtml#f0125-01a)
[![Images](./images/#af0125-02)](ch04.xhtml#f0125-02a)
[![Images](./images/#af0126-01)](ch04.xhtml#f0126-01a)
[![Images](./images/#af0126-02)](ch04.xhtml#f0126-02a)
[![Images](./images/#af0127-01)](ch04.xhtml#f0126-02a)
[![Images](./images/#af0127-02)](ch04.xhtml#f0127-02a)
[![Images](./images/#af0128-01)](ch04.xhtml#f0127-02a)
[![Images](./images/#af0128-02)](ch04.xhtml#f0128-02a)
[![Images](./images/#af0128-03)](ch04.xhtml#f0128-03a)
[![Images](./images/#af0129-01)](ch04.xhtml#f0128-03a)
[![Images](./images/#af0129-02)](ch04.xhtml#f0129-02a)
[![Images](./images/#af0129-03)](ch04.xhtml#f0129-03a)
[![Images](./images/#af0130-01)](ch04.xhtml#f0129-03a)
[![Images](./images/#af0130-02)](ch04.xhtml#f0130-02a)
[![Images](./images/#af0131-01)](ch04.xhtml#f0131-01a)
[![Images](./images/#af0131-02)](ch04.xhtml#f0131-02a)
[![Images](./images/#af0131-03)](ch04.xhtml#f0131-03a)
[![Images](./images/#af0132-01)](ch04.xhtml#f0132-01a)
[![Images](./images/#af0132-02)](ch04.xhtml#f0132-02a)
[![Images](./images/#af0132-03)](ch04.xhtml#f0132-03a)
[![Images](./images/#af0133-01)](ch04.xhtml#f0133-01a)
---
<a role="toc_link" id="ch05_images"></a>
[![Images](./images/#af0135-01)](ch05.xhtml#f0135-01a)
[![Images](./images/#af0136-01)](ch05.xhtml#f0135-01a)
[![Images](./images/#af0136-02)](ch05.xhtml#f0136-02a)
[![Images](./images/#af0136-03)](ch05.xhtml#f0136-03a)
[![Images](./images/#af0136-04)](ch05.xhtml#f0136-04a)
[![Images](./images/#af0137-01)](ch05.xhtml#f0137-01a)
[![Images](./images/#af0138-01)](ch05.xhtml#f0138-01a)
[![Images](./images/#af0138-02)](ch05.xhtml#f0138-02a)
[![Images](./images/#af0139-01)](ch05.xhtml#f0139-01a)
[![Images](./images/#af0139-02)](ch05.xhtml#f0139-02a)
[![Images](./images/#af0140-01)](ch05.xhtml#f0139-02a)
[![Images](./images/#af0140-02)](ch05.xhtml#f0140-02a)
[![Images](./images/#af0140-03)](ch05.xhtml#f0140-03a)
[![Images](./images/#af0141-01)](ch05.xhtml#f0141-01a)
[![Images](./images/#af0142-01)](ch05.xhtml#f0142-01a)
[![Images](./images/#af0142-02)](ch05.xhtml#f0142-02a)
[![Images](./images/#af0142-03)](ch05.xhtml#f0142-03a)
[![Images](./images/#af0143-01)](ch05.xhtml#f0143-01a)
[![Images](./images/#af0143-02)](ch05.xhtml#f0143-02a)
[![Images](./images/#af0143-03)](ch05.xhtml#f0143-03a)
[![Images](./images/#af0143-04)](ch05.xhtml#f0143-04a)
[![Images](./images/#af0144-01)](ch05.xhtml#f0144-01a)
[![Images](./images/#af0144-02)](ch05.xhtml#f0144-02a)
[![Images](./images/#af0145-01)](ch05.xhtml#f0145-01a)
[![Images](./images/#af0145-02)](ch05.xhtml#f0145-02a)
[![Images](./images/#af0146-01)](ch05.xhtml#f0146-01a)
[![Images](./images/#af0146-02)](ch05.xhtml#f0146-02a)
[![Images](./images/#af0147-01)](ch05.xhtml#f0146-02a)
[![Images](./images/#af0147-02)](ch05.xhtml#f0147-02a)
[![Images](./images/#af0147-03)](ch05.xhtml#f0147-03a)
[![Images](./images/#af0148-01)](ch05.xhtml#f0147-03a)
[![Images](./images/#af0148-02)](ch05.xhtml#f0148-02a)
[![Images](./images/#af0148-03)](ch05.xhtml#f0148-03a)
[![Images](./images/#af0149-01)](ch05.xhtml#f0149-01a)
[![Images](./images/#af0150-01)](ch05.xhtml#f0150-01a)
[![Images](./images/#af0150-02)](ch05.xhtml#f0150-02a)
[![Images](./images/#af0151-01)](ch05.xhtml#f0150-02a)
[![Images](./images/#af0151-02)](ch05.xhtml#f0151-02a)
[![Images](./images/#af0151-03)](ch05.xhtml#f0151-03a)
[![Images](./images/#af0152-01)](ch05.xhtml#f0152-01a)
[![Images](./images/#af0153-01)](ch05.xhtml#f0153-01a)
[![Images](./images/#af0153-02)](ch05.xhtml#f0153-02a)
[![Images](./images/#af0153-03)](ch05.xhtml#f0153-03a)
[![Images](./images/#af0153-04)](ch05.xhtml#f0153-04a)
[![Images](./images/#af0154-01)](ch05.xhtml#f0154-01a)
[![Images](./images/#af0154-02)](ch05.xhtml#f0154-02a)
[![Images](./images/#af0154-03)](ch05.xhtml#f0154-03a)
[![Images](./images/#af0154-04)](ch05.xhtml#f0154-04a)
[![Images](./images/#af0155-01)](ch05.xhtml#f0155-01a)
[![Images](./images/#af0155-02)](ch05.xhtml#f0155-02a)
[![Images](./images/#af0155-03)](ch05.xhtml#f0155-03a)
[![Images](./images/#af0156-01)](ch05.xhtml#f0156-01a)
[![Images](./images/#af0156-02)](ch05.xhtml#f0156-02a)
[![Images](./images/#af0156-03)](ch05.xhtml#f0156-03a)
[![Images](./images/#af0156-04)](ch05.xhtml#f0156-04a)
[![Images](./images/#af0157-01)](ch05.xhtml#f0157-01a)
[![Images](./images/#af0157-02)](ch05.xhtml#f0157-02a)
[![Images](./images/#af0158-01)](ch05.xhtml#f0157-02a)
[![Images](./images/#af0158-02)](ch05.xhtml#f0158-02a)
[![Images](./images/#af0158-03)](ch05.xhtml#f0158-03a)
[![Images](./images/#af0159-01)](ch05.xhtml#f0159-01a)
[![Images](./images/#af0159-02)](ch05.xhtml#f0159-02a)
[![Images](./images/#af0159-03)](ch05.xhtml#f0159-03a)
[![Images](./images/#af0160-01)](ch05.xhtml#f0159-03a)
[![Images](./images/#af0160-02)](ch05.xhtml#f0160-02a)
[![Images](./images/#af0160-03)](ch05.xhtml#f0160-03a)
[![Images](./images/#af0161-01)](ch05.xhtml#f0161-01a)
[![Images](./images/#af0161-02)](ch05.xhtml#f0161-02a)
[![Images](./images/#af0162-01)](ch05.xhtml#f0162-01a)
[![Images](./images/#af0162-02)](ch05.xhtml#f0162-02a)
[![Images](./images/#af0162-03)](ch05.xhtml#f0162-03a)
[![Images](./images/#af0162-04)](ch05.xhtml#f0162-04a)
[![Images](./images/#af0163-01)](ch05.xhtml#f0163-01a)
[![Images](./images/#af0163-02)](ch05.xhtml#f0163-02a)
[![Images](./images/#af0163-03)](ch05.xhtml#f0163-03a)
[![Images](./images/#af0163-04)](ch05.xhtml#f0163-04a)
[![Images](./images/#af0164-01)](ch05.xhtml#f0164-01a)
[![Images](./images/#af0164-02)](ch05.xhtml#f0164-02a)
[![Images](./images/#af0164-03)](ch05.xhtml#f0164-03a)
[![Images](./images/#af0165-01)](ch05.xhtml#f0165-01a)
[![Images](./images/#af0165-02)](ch05.xhtml#f0165-02a)
[![Images](./images/#af0165-03)](ch05.xhtml#f0165-03a)
[![Images](./images/#af0166-01)](ch05.xhtml#f0166-01a)
[![Images](./images/#af0167-01)](ch05.xhtml#f0167-01a)
[![Images](./images/#af0167-02)](ch05.xhtml#f0167-02a)
[![Images](./images/#af0168-01)](ch05.xhtml#f0168-01a)
[![Images](./images/#af0168-02)](ch05.xhtml#f0168-02a)
[![Images](./images/#af0168-03)](ch05.xhtml#f0168-03a)
[![Images](./images/#af0168-04)](ch05.xhtml#f0168-04a)
[![Images](./images/#af0169-01)](ch05.xhtml#f0168-04a)
[![Images](./images/#af0169-02)](ch05.xhtml#f0169-02a)
[![Images](./images/#af0169-03)](ch05.xhtml#f0169-03a)
[![Images](./images/#af0170-01)](ch05.xhtml#f0170-01a)
[![Images](./images/#af0170-02)](ch05.xhtml#f0170-02a)
[![Images](./images/#af0170-03)](ch05.xhtml#f0170-03a)
[![Images](./images/#af0170-04)](ch05.xhtml#f0170-04a)
[![Images](./images/#af0171-01)](ch05.xhtml#f0171-01a)
[![Images](./images/#af0171-02)](ch05.xhtml#f0171-02a)
[![Images](./images/#af0171-03)](ch05.xhtml#f0171-03a)
[![Images](./images/#af0171-04)](ch05.xhtml#f0171-04a)
[![Images](./images/#af0172-01)](ch05.xhtml#f0172-01a)
[![Images](./images/#af0172-02)](ch05.xhtml#f0172-02a)
[![Images](./images/#af0172-03)](ch05.xhtml#f0172-03a)
---
<a role="toc_link" id="ch06_images"></a>
[![Images](./images/#af0173-01)](ch06.xhtml#f0173-01a)
[![Images](./images/#af0174-01)](ch06.xhtml#f0174-01a)
[![Images](./images/#af0174-02)](ch06.xhtml#f0174-02a)
[![Images](./images/#af0174-03)](ch06.xhtml#f0174-03a)
[![Images](./images/#af0174-04)](ch06.xhtml#f0174-04a)
[![Images](./images/#af0175-01)](ch06.xhtml#f0175-01a)
[![Images](./images/#af0176-01)](ch06.xhtml#f0176-01a)
[![Images](./images/#af0176-02)](ch06.xhtml#f0176-02a)
[![Images](./images/#af0176-03)](ch06.xhtml#f0176-03a)
[![Images](./images/#af0177-02)](ch06.xhtml#f0177-02a)
[![Images](./images/#af0177-03)](ch06.xhtml#f0177-03a)
[![Images](./images/#af0178-01)](ch06.xhtml#f0178-01a)
[![Images](./images/#af0179-01)](ch06.xhtml#f0179-01a)
[![Images](./images/#af0179-02)](ch06.xhtml#f0179-02a)
[![Images](./images/#af0179-03)](ch06.xhtml#f0179-03a)
[![Images](./images/#af0180-01)](ch06.xhtml#f0180-01a)
[![Images](./images/#af0180-02)](ch06.xhtml#f0180-02a)
[![Images](./images/#af0180-03)](ch06.xhtml#f0180-03a)
[![Images](./images/#af0180-04)](ch06.xhtml#f0180-04a)
[![Images](./images/#af0181-01)](ch06.xhtml#f0181-01a)
[![Images](./images/#af0181-02)](ch06.xhtml#f0181-02a)
[![Images](./images/#af0182-01)](ch06.xhtml#f0182-01a)
[![Images](./images/#af0182-02)](ch06.xhtml#f0182-02a)
[![Images](./images/#af0182-03)](ch06.xhtml#f0182-03a)
[![Images](./images/#af0183-01)](ch06.xhtml#f0183-01a)
[![Images](./images/#af0183-02)](ch06.xhtml#f0183-02a)
[![Images](./images/#af0184-01)](ch06.xhtml#f0184-01a)
[![Images](./images/#af0184-02)](ch06.xhtml#f0184-02a)
[![Images](./images/#af0185-01)](ch06.xhtml#f0185-01a)
[![Images](./images/#af0185-02)](ch06.xhtml#f0185-02a)
[![Images](./images/#af0187-01)](ch06.xhtml#f0187-01a)
[![Images](./images/#af0187-02)](ch06.xhtml#f0187-02a)
[![Images](./images/#af0189-01)](ch06.xhtml#f0189-01a)
[![Images](./images/#af0189-02)](ch06.xhtml#f0189-02a)
[![Images](./images/#af0190-01)](ch06.xhtml#f0190-01a)
[![Images](./images/#af0190-02)](ch06.xhtml#f0190-02a)
[![Images](./images/#af0191-01)](ch06.xhtml#f0191-01a)
[![Images](./images/#af0191-02)](ch06.xhtml#f0191-02a)
[![Images](./images/#af0192-01)](ch06.xhtml#f0192-01a)
[![Images](./images/#af0193-01)](ch06.xhtml#f0192-01a)
[![Images](./images/#af0193-02)](ch06.xhtml#f0193-02a)
[![Images](./images/#af0194-01)](ch06.xhtml#f0193-02a)
[![Images](./images/#af0194-02)](ch06.xhtml#f0194-02a)
[![Images](./images/#af0194-03)](ch06.xhtml#f0194-03a)
[![Images](./images/#af0195-01)](ch06.xhtml#f0195-01a)
[![Images](./images/#af0196-01)](ch06.xhtml#f0196-01a)
[![Images](./images/#af0196-02)](ch06.xhtml#f0196-02a)
[![Images](./images/#af0197-01)](ch06.xhtml#f0197-01a)
[![Images](./images/#af0198-01)](ch06.xhtml#f0198-01a)
[![Images](./images/#af0198-02)](ch06.xhtml#f0198-02a)
[![Images](./images/#af0199-01)](ch06.xhtml#f0198-02a)
---
<a role="toc_link" id="ch07_images"></a>
[![Images](./images/#af0201-01)](ch07.xhtml#f0201-01a)
[![Images](./images/#af0202-01)](ch07.xhtml#f0201-01a)
[![Images](./images/#af0202-03)](ch07.xhtml#f0202-03a)
[![Images](./images/#af0203-01)](ch07.xhtml#f0203-01a)
[![Images](./images/#af0203-02)](ch07.xhtml#f0203-02a)
[![Images](./images/#af0204-01)](ch07.xhtml#f0204-01a)
[![Images](./images/#af0204-02)](ch07.xhtml#f0204-02a)
[![Images](./images/#af0204-03)](ch07.xhtml#f0204-03a)
[![Images](./images/#af0205-01)](ch07.xhtml#f0205-01a)
[![Images](./images/#af0206-01)](ch07.xhtml#f0206-01a)
[![Images](./images/#af0206-02)](ch07.xhtml#f0206-02a)
[![Images](./images/#af0207-01)](ch07.xhtml#f0207-01a)
[![Images](./images/#af0207-02)](ch07.xhtml#f0207-02a)
[![Images](./images/#af0207-03)](ch07.xhtml#f0207-03a)
[![Images](./images/#af0208-01)](ch07.xhtml#f0207-03a)
[![Images](./images/#af0208-02)](ch07.xhtml#f0208-02a)
[![Images](./images/#af0208-03)](ch07.xhtml#f0208-03a)
[![Images](./images/#af0209-01)](ch07.xhtml#f0209-01a)
[![Images](./images/#af0209-02)](ch07.xhtml#f0209-02a)
[![Images](./images/#af0209-03)](ch07.xhtml#f0209-03a)
[![Images](./images/#af0210-01)](ch07.xhtml#f0210-01a)
[![Images](./images/#af0211-01)](ch07.xhtml#f0210-01a)
[![Images](./images/#af0211-02)](ch07.xhtml#f0211-02a)
[![Images](./images/#af0213-01)](ch07.xhtml#f0213-01a)
[![Images](./images/#af0214-01)](ch07.xhtml#f0214-01a)
[![Images](./images/#af0214-01a)](ch07.xhtml#f0214-01aa)
[![Images](./images/#af0214-02)](ch07.xhtml#f0214-02a)
[![Images](./images/#af0215-01)](ch07.xhtml#f0214-02a)
[![Images](./images/#af0215-02)](ch07.xhtml#f0215-02a)
[![Images](./images/#af0215-03)](ch07.xhtml#f0215-03a)
[![Images](./images/#af0217-01)](ch07.xhtml#f0217-01a)
[![Images](./images/#af0218-01)](ch07.xhtml#f0217-01a)
[![Images](./images/#af0218-02)](ch07.xhtml#f0218-02a)
[![Images](./images/#af0218-03)](ch07.xhtml#f0218-03a)
[![Images](./images/#af0218-04)](ch07.xhtml#f0218-04a)
[![Images](./images/#af0219-01)](ch07.xhtml#f0218-04a)
[![Images](./images/#af0219-02)](ch07.xhtml#f0219-02a)
[![Images](./images/#af0219-03)](ch07.xhtml#f0219-03a)
[![Images](./images/#af0220-01)](ch07.xhtml#f0220-01a)
[![Images](./images/#af0220-02)](ch07.xhtml#f0220-02a)
[![Images](./images/#af0220-03)](ch07.xhtml#f0220-03a)
[![Images](./images/#af0220-04)](ch07.xhtml#f0220-04a)
[![Images](./images/#af0220-06)](ch07.xhtml#f0220-06a)
[![Images](./images/#af0221-01)](ch07.xhtml#f0221-01a)
[![Images](./images/#af0221-02)](ch07.xhtml#f0221-02a)
[![Images](./images/#af0221-03)](ch07.xhtml#f0221-03a)
[![Images](./images/#af0222-01)](ch07.xhtml#f0222-01a)
[![Images](./images/#af0222-02)](ch07.xhtml#f0222-02a)
[![Images](./images/#af0222-03)](ch07.xhtml#f0222-03a)
[![Images](./images/#af0223-01)](ch07.xhtml#f0223-01a)
[![Images](./images/#af0223-02)](ch07.xhtml#f0223-02a)
[![Images](./images/#af0223-03)](ch07.xhtml#f0223-03a)
[![Images](./images/#af0224-01)](ch07.xhtml#f0223-03a)
[![Images](./images/#af0224-02)](ch07.xhtml#f0224-02a)
[![Images](./images/#af0224-03)](ch07.xhtml#f0224-03a)
[![Images](./images/#af0224-04)](ch07.xhtml#f0224-04a)
[![Images](./images/#af0225-01)](ch07.xhtml#f0225-01a)
[![Images](./images/#af0225-02)](ch07.xhtml#f0225-02a)
[![Images](./images/#af0225-03)](ch07.xhtml#f0225-03a)
[![Images](./images/#af0225-04)](ch07.xhtml#f0225-04a)
[![Images](./images/#af0226-01)](ch07.xhtml#f0225-04a)
[![Images](./images/#af0226-02)](ch07.xhtml#f0226-02a)
[![Images](./images/#af0226-03)](ch07.xhtml#f0226-03a)
[![Images](./images/#af0227-01)](ch07.xhtml#f0227-01a)
[![Images](./images/#af0227-02)](ch07.xhtml#f0227-02a)
[![Images](./images/#af0227-03)](ch07.xhtml#f0227-03a)
[![Images](./images/#af0228-01)](ch07.xhtml#f0227-03a)
[![Images](./images/#af0228-02)](ch07.xhtml#f0228-02a)
[![Images](./images/#af0228-03)](ch07.xhtml#f0228-03a)
[![Images](./images/#af0229-01)](ch07.xhtml#f0228-03a)
[![Images](./images/#af0229-02)](ch07.xhtml#f0229-02a)
[![Images](./images/#af0230-01)](ch07.xhtml#f0230-01a)
[![Images](./images/#af0231-01)](ch07.xhtml#f0231-01a)
[![Images](./images/#af0231-02)](ch07.xhtml#f0231-02a)
[![Images](./images/#af0231-03)](ch07.xhtml#f0231-03a)
[![Images](./images/#af0232-01)](ch07.xhtml#f0232-01a)
[![Images](./images/#af0232-02)](ch07.xhtml#f0232-02a)
[![Images](./images/#af0232-03)](ch07.xhtml#f0232-03a)
[![Images](./images/#af0232-04)](ch07.xhtml#f0232-04a)
[![Images](./images/#af0233-01)](ch07.xhtml#f0233-01a)
[![Images](./images/#af0233-02)](ch07.xhtml#f0233-02a)
[![Images](./images/#af0234-01)](ch07.xhtml#f0233-02a)
[![Images](./images/#af0234-02)](ch07.xhtml#f0234-02a)
[![Images](./images/#af0234-03)](ch07.xhtml#f0234-03a)
[![Images](./images/#af0235-01)](ch07.xhtml#f0235-01a)
[![Images](./images/#af0235-02)](ch07.xhtml#f0235-02a)
[![Images](./images/#af0235-03)](ch07.xhtml#f0235-03a)
[![Images](./images/#af0235-04)](ch07.xhtml#f0235-04a)
[![Images](./images/#af0236-02)](ch07.xhtml#f0236-02a)
[![Images](./images/#af0236-03)](ch07.xhtml#f0236-03a)
[![Images](./images/#af0236-04)](ch07.xhtml#f0236-04a)
[![Images](./images/#af0237-01)](ch07.xhtml#f0237-01a)
[![Images](./images/#af0237-02)](ch07.xhtml#f0237-02a)
[![Images](./images/#af0237-03)](ch07.xhtml#f0237-03a)
[![Images](./images/#af0238-01)](ch07.xhtml#f0238-01a)
[![Images](./images/#af0238-02)](ch07.xhtml#f0238-02a)
[![Images](./images/#af0238-03)](ch07.xhtml#f0238-03a)
[![Images](./images/#af0239-01)](ch07.xhtml#f0239-01a)
[![Images](./images/#af0239-02)](ch07.xhtml#f0239-02a)
[![Images](./images/#af0240-01)](ch07.xhtml#f0240-01a)
[![Images](./images/#af0241-01)](ch07.xhtml#f0240-01a)
[![Images](./images/#af0241-02)](ch07.xhtml#f0241-02a)
[![Images](./images/#af0241-03)](ch07.xhtml#f0241-03a)
[![Images](./images/#af0242-01)](ch07.xhtml#f0242-01a)
[![Images](./images/#af0242-02)](ch07.xhtml#f0242-02a)
[![Images](./images/#af0243-01)](ch07.xhtml#f0242-02a)
[![Images](./images/#af0243-02)](ch07.xhtml#f0243-02a)
[![Images](./images/#af0243-03)](ch07.xhtml#f0243-03a)
[![Images](./images/#af0244-01)](ch07.xhtml#f0244-01a)
[![Images](./images/#af0244-02)](ch07.xhtml#f0244-02a)
[![Images](./images/#af0245-01)](ch07.xhtml#f0245-01a)
[![Images](./images/#af0245-03)](ch07.xhtml#f0245-03a)
[![Images](./images/#af0245-02)](ch07.xhtml#f0245-02a)
[![Images](./images/#af0246-01)](ch07.xhtml#f0246-01a)
[![Images](./images/#af0246-02)](ch07.xhtml#f0246-02a)
[![Images](./images/#af0247-01)](ch07.xhtml#f0247-01a)
[![Images](./images/#af0247-02)](ch07.xhtml#f0247-02a)
[![Images](./images/#af0247-03)](ch07.xhtml#f0247-03a)
[![Images](./images/#af0248-01)](ch07.xhtml#f0248-01a)
[![Images](./images/#af0248-02)](ch07.xhtml#f0248-02a)
[![Images](./images/#af0248-03)](ch07.xhtml#f0248-03a)
[![Images](./images/#af0249-01)](ch07.xhtml#f0249-01a)
[![Images](./images/#af0249-02)](ch07.xhtml#f0249-02a)
[![Images](./images/#af0250-01)](ch07.xhtml#f0250-01a)
[![Images](./images/#af0251-01)](ch07.xhtml#f0251-01a)
[![Images](./images/#af0251-02)](ch07.xhtml#f0251-02a)
[![Images](./images/#af0252-01)](ch07.xhtml#f0252-01a)
[![Images](./images/#af0252-02)](ch07.xhtml#f0252-02a)
[![Images](./images/#af0252-03)](ch07.xhtml#f0252-03a)
[![Images](./images/#af0252-04)](ch07.xhtml#f0252-04a)
[![Images](./images/#af0252-05)](ch07.xhtml#f0252-05a)
[![Images](./images/#af0253-01)](ch07.xhtml#f0253-01a)
[![Images](./images/#af0253-02)](ch07.xhtml#f0253-02a)
[![Images](./images/#af0253-03)](ch07.xhtml#f0253-03a)
[![Images](./images/#af0254-01)](ch07.xhtml#f0254-01a)
[![Images](./images/#af0254-02)](ch07.xhtml#f0254-02a)
[![Images](./images/#af0254-03)](ch07.xhtml#f0254-03a)
[![Images](./images/#af0255-01)](ch07.xhtml#f0255-01a)
[![Images](./images/#af0255-02)](ch07.xhtml#f0255-02a)
[![Images](./images/#af0255-03)](ch07.xhtml#f0255-03a)
[![Images](./images/#af0256-01)](ch07.xhtml#f0256-01a)
[![Images](./images/#af0257-01)](ch07.xhtml#f0257-01a)
[![Images](./images/#af0257-02)](ch07.xhtml#f0257-02a)
[![Images](./images/#af0258-01)](ch07.xhtml#f0258-01a)
[![Images](./images/#af0258-02)](ch07.xhtml#f0258-02a)
[![Images](./images/#af0259-01)](ch07.xhtml#f0259-01a)
[![Images](./images/#af0260-01)](ch07.xhtml#f0260-01a)
[![Images](./images/#af0260-02)](ch07.xhtml#f0260-02a)
[![Images](./images/#af0261-01)](ch07.xhtml#f0260-02a)
[![Images](./images/#af0261-02)](ch07.xhtml#f0261-02a)
[![Images](./images/#af0261-03)](ch07.xhtml#f0261-03a)
[![Images](./images/#af0262-01)](ch07.xhtml#f0262-01a)
[![Images](./images/#af0262-02)](ch07.xhtml#f0262-02a)
[![Images](./images/#af0262-03)](ch07.xhtml#f0262-03a)
[![Images](./images/#af0262-04)](ch07.xhtml#f0262-04a)
[![Images](./images/#af0263-01)](ch07.xhtml#f0262-04a)
[![Images](./images/#af0263-02)](ch07.xhtml#f0263-02a)
[![Images](./images/#af0263-03)](ch07.xhtml#f0263-03a)
[![Images](./images/#af0264-01)](ch07.xhtml#f0263-03a)
---
<a role="toc_link" id="ch08_images"></a>
[![Images](./images/#af0266-01)](ch08.xhtml#f0266-01a)
[![Images](./images/#af0266-02)](ch08.xhtml#f0266-02a)
[![Images](./images/#af0267-01)](ch08.xhtml#f0267-01a)
[![Images](./images/#af0267-02)](ch08.xhtml#f0267-02a)
[![Images](./images/#af0267-03)](ch08.xhtml#f0267-03a)
[![Images](./images/#af0268-01)](ch08.xhtml#f0268-01a)
[![Images](./images/#af0268-02)](ch08.xhtml#f0268-02a)
[![Images](./images/#af0268-03)](ch08.xhtml#f0268-03a)
[![Images](./images/#af0268-04)](ch08.xhtml#f0268-04a)
[![Images](./images/#af0269-01)](ch08.xhtml#f0269-01a)
[![Images](./images/#af0269-02)](ch08.xhtml#f0269-02a)
[![Images](./images/#af0270-01)](ch08.xhtml#f0270-01a)
[![Images](./images/#af0270-02)](ch08.xhtml#f0270-02a)
[![Images](./images/#af0271-01)](ch08.xhtml#f0271-01a)
[![Images](./images/#af0271-02)](ch08.xhtml#f0271-02a)
[![Images](./images/#af0271-03)](ch08.xhtml#f0271-03a)
[![Images](./images/#af0272-01)](ch08.xhtml#f0272-01a)
[![Images](./images/#af0272-02)](ch08.xhtml#f0272-02a)
[![Images](./images/#af0272-03)](ch08.xhtml#f0272-03a)
[![Images](./images/#af0273-02)](ch08.xhtml#f0273-02a)
[![Images](./images/#af0274-01)](ch08.xhtml#f0274-01a)
[![Images](./images/#af0274-02)](ch08.xhtml#f0274-02a)
[![Images](./images/#af0275-01)](ch08.xhtml#f0274-02a)
[![Images](./images/#af0275-02)](ch08.xhtml#f0275-02a)
[![Images](./images/#af0275-03)](ch08.xhtml#f0275-03a)
[![Images](./images/#af0276-01)](ch08.xhtml#f0275-03a)
[![Images](./images/#af0276-02)](ch08.xhtml#f0276-02a)
[![Images](./images/#af0276-03)](ch08.xhtml#f0276-03a)
[![Images](./images/#af0276-04)](ch08.xhtml#f0276-04a)
[![Images](./images/#af0277-01)](ch08.xhtml#f0277-01a)
[![Images](./images/#af0277-02)](ch08.xhtml#f0277-02a)
[![Images](./images/#af0277-03)](ch08.xhtml#f0277-03a)
[![Images](./images/#af0278-01)](ch08.xhtml#f0277-03a)
[![Images](./images/#af0278-02)](ch08.xhtml#f0278-02a)
[![Images](./images/#af0278-03)](ch08.xhtml#f0278-03a)
[![Images](./images/#af0278-04)](ch08.xhtml#f0278-04a)
[![Images](./images/#af0279-01)](ch08.xhtml#f0278-04a)
[![Images](./images/#af0280-01)](ch08.xhtml#f0280-01a)
[![Images](./images/#af0280-02)](ch08.xhtml#f0280-02a)
[![Images](./images/#af0280-03)](ch08.xhtml#f0280-03a)
[![Images](./images/#af0281-01)](ch08.xhtml#f0280-03a)
[![Images](./images/#af0281-02)](ch08.xhtml#f0281-02a)
[![Images](./images/#af0282-01)](ch08.xhtml#f0281-02a)
[![Images](./images/#af0282-02)](ch08.xhtml#f0282-02a)
[![Images](./images/#af0282-03)](ch08.xhtml#f0282-03a)
[![Images](./images/#af0283-01)](ch08.xhtml#f0282-03a)
[![Images](./images/#af0283-02)](ch08.xhtml#f0283-02a)
[![Images](./images/#af0283-03)](ch08.xhtml#f0283-03a)
[![Images](./images/#af0283-05)](ch08.xhtml#f0283-05a)
[![Images](./images/#af0284-01)](ch08.xhtml#f0283-05a)
[![Images](./images/#af0284-02)](ch08.xhtml#f0284-02a)
[![Images](./images/#af0284-04)](ch08.xhtml#f0284-04a)
[![Images](./images/#af0285-01)](ch08.xhtml#f0285-01a)
[![Images](./images/#af0286-01)](ch08.xhtml#f0286-01a)
[![Images](./images/#af0287-02)](ch08.xhtml#f0287-02a)
[![Images](./images/#af0288-01)](ch08.xhtml#f0288-01a)
[![Images](./images/#af0288-02)](ch08.xhtml#f0288-02a)
[![Images](./images/#af0289-01)](ch08.xhtml#f0289-01a)
[![Images](./images/#af0289-02)](ch08.xhtml#f0289-02a)
[![Images](./images/#af0289-03)](ch08.xhtml#f0289-03a)
[![Images](./images/#af0290-01)](ch08.xhtml#f0290-01a)
[![Images](./images/#af0290-02)](ch08.xhtml#f0290-02a)
[![Images](./images/#af0290-03)](ch08.xhtml#f0290-03a)
[![Images](./images/#af0291-01)](ch08.xhtml#f0291-01a)
[![Images](./images/#af0291-03)](ch08.xhtml#f0291-03a)
[![Images](./images/#af0291-04)](ch08.xhtml#f0291-04a)
[![Images](./images/#af0292-01)](ch08.xhtml#f0292-01a)
[![Images](./images/#af0292-02)](ch08.xhtml#f0292-02a)
[![Images](./images/#af0292-03)](ch08.xhtml#f0292-03a)
[![Images](./images/#af0293-01)](ch08.xhtml#f0292-03a)
[![Images](./images/#af0294-01)](ch08.xhtml#f0294-01a)
[![Images](./images/#af0294-02)](ch08.xhtml#f0294-02a)
[![Images](./images/#af0294-03)](ch08.xhtml#f0294-03a)
[![Images](./images/#af0295-01)](ch08.xhtml#f0295-01a)
[![Images](./images/#af0295-02)](ch08.xhtml#f0295-02a)
[![Images](./images/#af0296-01)](ch08.xhtml#f0295-02a)
[![Images](./images/#af0296-02)](ch08.xhtml#f0296-02a)
[![Images](./images/#af0296-03)](ch08.xhtml#f0296-03a)
[![Images](./images/#af0296-04)](ch08.xhtml#f0296-04a)
[![Images](./images/#af0297-01)](ch08.xhtml#f0297-01a)
[![Images](./images/#af0297-02)](ch08.xhtml#f0297-02a)
[![Images](./images/#af0298-01)](ch08.xhtml#f0298-01a)
[![Images](./images/#af0298-02)](ch08.xhtml#f0298-02a)
[![Images](./images/#af0298-03)](ch08.xhtml#f0298-03a)
[![Images](./images/#af0299-01)](ch08.xhtml#f0299-01a)
[![Images](./images/#af0299-02)](ch08.xhtml#f0299-02a)
[![Images](./images/#af0300-01)](ch08.xhtml#f0299-02a)
[![Images](./images/#af0300-02)](ch08.xhtml#f0300-02a)
[![Images](./images/#af0300-03)](ch08.xhtml#f0300-03a)
[![Images](./images/#af0300-04)](ch08.xhtml#f0300-04a)
[![Images](./images/#af0301-01)](ch08.xhtml#f0301-01a)
[![Images](./images/#af0301-02)](ch08.xhtml#f0301-02a)
[![Images](./images/#af0301-03)](ch08.xhtml#f0301-03a)
[![Images](./images/#af0301-04)](ch08.xhtml#f0301-04a)
[![Images](./images/#af0302-01)](ch08.xhtml#f0302-01a)
[![Images](./images/#af0302-02)](ch08.xhtml#f0302-02a)
[![Images](./images/#af0302-03)](ch08.xhtml#f0302-03a)
[![Images](./images/#af0303-01)](ch08.xhtml#f0302-03a)
[![Images](./images/#af0303-02)](ch08.xhtml#f0303-02a)
[![Images](./images/#af0304-01)](ch08.xhtml#f0304-01a)
[![Images](./images/#af0304-02)](ch08.xhtml#f0304-02a)
[![Images](./images/#af0304-03)](ch08.xhtml#f0304-03a)
[![Images](./images/#af0305-01)](ch08.xhtml#f0305-01a)
[![Images](./images/#af0305-02)](ch08.xhtml#f0305-02a)
[![Images](./images/#af0305-03)](ch08.xhtml#f0305-03a)
[![Images](./images/#af0306-01)](ch08.xhtml#f0306-01a)
[![Images](./images/#af0306-02)](ch08.xhtml#f0306-02a)
[![Images](./images/#af0307-01)](ch08.xhtml#f0307-01a)
[![Images](./images/#af0307-02)](ch08.xhtml#f0307-02a)
[![Images](./images/#af0308-01)](ch08.xhtml#f0308-01a)
[![Images](./images/#af0308-02)](ch08.xhtml#f0308-02a)
[![Images](./images/#af0308-03)](ch08.xhtml#f0308-03a)
[![Images](./images/#af0308-04)](ch08.xhtml#f0308-04a)
[![Images](./images/#af0309-01)](ch08.xhtml#f0308-04a)
[![Images](./images/#af0309-02)](ch08.xhtml#f0309-02a)
[![Images](./images/#af0309-03)](ch08.xhtml#f0309-03a)
[![Images](./images/#af0309-04)](ch08.xhtml#f0309-04a)
[![Images](./images/#af0310-01)](ch08.xhtml#f0309-04a)
[![Images](./images/#af0311-01)](ch08.xhtml#f0311-01a)
[![Images](./images/#af0311-02)](ch08.xhtml#f0311-02a)
[![Images](./images/#af0312-01)](ch08.xhtml#f0312-01a)
[![Images](./images/#af0312-02)](ch08.xhtml#f0312-02a)
[![Images](./images/#af0313-01)](ch08.xhtml#f0312-02a)
[![Images](./images/#af0313-02)](ch08.xhtml#f0313-02a)
[![Images](./images/#af0313-03)](ch08.xhtml#f0313-03a)
[![Images](./images/#af0314-01)](ch08.xhtml#f0313-03a)
[![Images](./images/#af0314-02)](ch08.xhtml#f0314-02a)
[![Images](./images/#af0315-01)](ch08.xhtml#f0315-01a)
[![Images](./images/#af0315-02)](ch08.xhtml#f0315-02a)
[![Images](./images/#af0315-03)](ch08.xhtml#f0315-03a)
[![Images](./images/#af0316-01)](ch08.xhtml#f0315-03a)
[![Images](./images/#af0316-02)](ch08.xhtml#f0316-02a)
---
<a role="toc_link" id="ch09_images"></a>
[![Images](./images/#af0320-01)](ch09.xhtml#f0320-01a)
[![Images](./images/#af0321-01)](ch09.xhtml#f0321-01a)
[![Images](./images/#af0321-02)](ch09.xhtml#f0321-02a)
[![Images](./images/#af0321-03)](ch09.xhtml#f0321-03a)
[![Images](./images/#af0322-01)](ch09.xhtml#f0322-01a)
[![Images](./images/#af0322-02)](ch09.xhtml#f0322-02a)
[![Images](./images/#af0323-01)](ch09.xhtml#f0323-01a)
[![Images](./images/#af0323-02)](ch09.xhtml#f0323-02a)
[![Images](./images/#af0323-03)](ch09.xhtml#f0323-03a)
[![Images](./images/#af0324-01)](ch09.xhtml#f0323-03a)
[![Images](./images/#af0324-02)](ch09.xhtml#f0324-02a)
[![Images](./images/#af0325-01)](ch09.xhtml#f0325-01a)
[![Images](./images/#af0325-02)](ch09.xhtml#f0325-02a)
[![Images](./images/#af0326-01)](ch09.xhtml#f0325-02a)
[![Images](./images/#af0326-02)](ch09.xhtml#f0326-02a)
[![Images](./images/#af0326-03)](ch09.xhtml#f0326-03a)
[![Images](./images/#af0326-04)](ch09.xhtml#f0326-04a)
[![Images](./images/#af0328-01)](ch09.xhtml#f0328-01a)
[![Images](./images/#af0328-02)](ch09.xhtml#f0328-02a)
[![Images](./images/#af0328-03)](ch09.xhtml#f0328-03a)
[![Images](./images/#af0329-01)](ch09.xhtml#f0329-01a)
[![Images](./images/#af0330-01)](ch09.xhtml#f0330-01a)
[![Images](./images/#af0330-02)](ch09.xhtml#f0330-02a)
[![Images](./images/#af0331-01)](ch09.xhtml#f0330-02a)
[![Images](./images/#af0332-01)](ch09.xhtml#f0332-01a)
[![Images](./images/#af0332-02)](ch09.xhtml#f0332-02a)
[![Images](./images/#af0333-01)](ch09.xhtml#f0333-01a)
[![Images](./images/#af0334-01)](ch09.xhtml#f0334-01a)
[![Images](./images/#af0335-01)](ch09.xhtml#f0335-01a)
[![Images](./images/#af0335-02)](ch09.xhtml#f0335-02a)
[![Images](./images/#af0335-03)](ch09.xhtml#f0335-03a)
[![Images](./images/#af0335-04)](ch09.xhtml#f0335-04a)
[![Images](./images/#af0336-01)](ch09.xhtml#f0335-04a)
[![Images](./images/#af0336-02)](ch09.xhtml#f0336-02a)
[![Images](./images/#af0336-03)](ch09.xhtml#f0336-03a)
[![Images](./images/#af0336-04)](ch09.xhtml#f0336-04a)
[![Images](./images/#af0337-01)](ch09.xhtml#f0337-01a)
[![Images](./images/#af0337-02)](ch09.xhtml#f0337-02a)
[![Images](./images/#af0338-01)](ch09.xhtml#f0338-01a)
[![Images](./images/#af0338-02)](ch09.xhtml#f0338-02a)
[![Images](./images/#af0339-01)](ch09.xhtml#f0339-01a)
[![Images](./images/#af0339-02)](ch09.xhtml#f0339-02a)
[![Images](./images/#af0340-01)](ch09.xhtml#f0340-01a)
[![Images](./images/#af0340-02)](ch09.xhtml#f0340-02a)
[![Images](./images/#af0341-01)](ch09.xhtml#f0340-02a)
[![Images](./images/#af0341-02)](ch09.xhtml#f0341-02a)
[![Images](./images/#af0341-03)](ch09.xhtml#f0341-03a)
[![Images](./images/#af0342-01)](ch09.xhtml#f0342-01a)
[![Images](./images/#af0342-02)](ch09.xhtml#f0342-02a)
[![Images](./images/#af0343-01)](ch09.xhtml#f0342-02a)
[![Images](./images/#af0343-02)](ch09.xhtml#f0343-02a)
[![Images](./images/#af0343-03)](ch09.xhtml#f0343-03a)
[![Images](./images/#af0344-01)](ch09.xhtml#f0343-03a)
[![Images](./images/#af0345-01)](ch09.xhtml#f0345-01a)
[![Images](./images/#af0345-02)](ch09.xhtml#f0345-02a)
[![Images](./images/#af0346-01)](ch09.xhtml#f0346-01a)
[![Images](./images/#af0346-02)](ch09.xhtml#f0346-02a)
[![Images](./images/#af0347-01)](ch09.xhtml#f0347-01a)
[![Images](./images/#af0347-02)](ch09.xhtml#f0347-02a)
[![Images](./images/#af0347-03)](ch09.xhtml#f0347-03a)
[![Images](./images/#af0348-01)](ch09.xhtml#f0347-03a)
[![Images](./images/#af0348-02)](ch09.xhtml#f0348-02a)
[![Images](./images/#af0349-01)](ch09.xhtml#f0349-01a)
[![Images](./images/#af0350-01)](ch09.xhtml#f0349-01a)
[![Images](./images/#af0350-02)](ch09.xhtml#f0350-02a)
[![Images](./images/#af0351-01)](ch09.xhtml#f0350-02a)
[![Images](./images/#af0351-02)](ch09.xhtml#f0351-02a)
[![Images](./images/#af0352-01)](ch09.xhtml#f0352-01a)
[![Images](./images/#af0352-02)](ch09.xhtml#f0352-02a)
[![Images](./images/#af0353-01)](ch09.xhtml#f0352-02a)
[![Images](./images/#af0354-01)](ch09.xhtml#f0354-01a)
[![Images](./images/#af0355-01)](ch09.xhtml#f0354-01a)
[![Images](./images/#af0355-02)](ch09.xhtml#f0355-02a)
[![Images](./images/#af0356-01)](ch09.xhtml#f0356-01a)
[![Images](./images/#af0356-02)](ch09.xhtml#f0356-02a)
[![Images](./images/#af0357-01)](ch09.xhtml#f0356-02a)
[![Images](./images/#af0357-02)](ch09.xhtml#f0357-02a)
[![Images](./images/#af0358-01)](ch09.xhtml#f0358-01a)
[![Images](./images/#af0358-02)](ch09.xhtml#f0358-02a)
[![Images](./images/#af0359-01)](ch09.xhtml#f0358-02a)
[![Images](./images/#af0359-02)](ch09.xhtml#f0359-02a)
[![Images](./images/#af0359-03)](ch09.xhtml#f0359-03a)
[![Images](./images/#af0360-01)](ch09.xhtml#f0359-03a)
[![Images](./images/#af0361-01)](ch09.xhtml#f0361-01a)
[![Images](./images/#af0362-01)](ch09.xhtml#f0362-01a)
[![Images](./images/#af0362-02)](ch09.xhtml#f0362-02a)
[![Images](./images/#af0363-01)](ch09.xhtml#f0362-02a)
[![Images](./images/#af0363-02)](ch09.xhtml#f0363-02a)
[![Images](./images/#af0365-01)](ch09.xhtml#f0365-01a)
[![Images](./images/#af0365-02)](ch09.xhtml#f0365-02a)
[![Images](./images/#af0365-03)](ch09.xhtml#f0365-03a)
[![Images](./images/#af0366-01)](ch09.xhtml#f0365-03a)
[![Images](./images/#af0366-02)](ch09.xhtml#f0366-02a)
[![Images](./images/#af0367-01)](ch09.xhtml#f0366-02a)
[![Images](./images/#af0367-02)](ch09.xhtml#f0367-02a)
[![Images](./images/#af0368-01)](ch09.xhtml#f0367-02a)
[![Images](./images/#af0369-01)](ch09.xhtml#f0369-01a)
[![Images](./images/#af0369-02)](ch09.xhtml#f0369-02a)
[![Images](./images/#af0370-01)](ch09.xhtml#f0370-01a)
[![Images](./images/#af0370-02)](ch09.xhtml#f0370-02a)
[![Images](./images/#af0370-03)](ch09.xhtml#f0370-03a)
[![Images](./images/#af0371-01)](ch09.xhtml#f0371-01a)
[![Images](./images/#af0371-02)](ch09.xhtml#f0371-02a)
[![Images](./images/#af0372-01)](ch09.xhtml#f0372-01a)
[![Images](./images/#af0372-02)](ch09.xhtml#f0372-02a)
[![Images](./images/#af0373-01)](ch09.xhtml#f0373-01a)
[![Images](./images/#af0373-02)](ch09.xhtml#f0373-02a)
[![Images](./images/#af0374-01)](ch09.xhtml#f0374-01a)
[![Images](./images/#af0374-02)](ch09.xhtml#f0374-02a)
[![Images](./images/#af0375-01)](ch09.xhtml#f0374-02a)
[![Images](./images/#af0375-02)](ch09.xhtml#f0375-02a)
[![Images](./images/#af0376-01)](ch09.xhtml#f0376-01a)
[![Images](./images/#af0376-02)](ch09.xhtml#f0376-02a)
[![Images](./images/#af0376-05)](ch09.xhtml#f0376-05a)
[![Images](./images/#af0376-03)](ch09.xhtml#f0376-03a)
[![Images](./images/#af0376-04)](ch09.xhtml#f0376-04a)
[![Images](./images/#af0377-01)](ch09.xhtml#f0377-01a)
[![Images](./images/#af0377-02)](ch09.xhtml#f0377-02a)
[![Images](./images/#af0377-03)](ch09.xhtml#f0377-03a)
[![Images](./images/#af0377-04)](ch09.xhtml#f0377-04a)
[![Images](./images/#af0378-01)](ch09.xhtml#f0377-04a)
[![Images](./images/#af0378-02)](ch09.xhtml#f0378-02a)
[![Images](./images/#af0378-03)](ch09.xhtml#f0378-03a)
[![Images](./images/#af0379-01)](ch09.xhtml#f0379-01a)
[![Images](./images/#af0380-01)](ch09.xhtml#f0380-01a)
[![Images](./images/#af0381-01)](ch09.xhtml#f0380-01a)
[![Images](./images/#af0382-01)](ch09.xhtml#f0382-01a)
[![Images](./images/#af0383-01)](ch09.xhtml#f0382-01a)
[![Images](./images/#af0383-02)](ch09.xhtml#f0383-02a)
[![Images](./images/#af0383-03)](ch09.xhtml#f0383-03a)
[![Images](./images/#af0384-01)](ch09.xhtml#f0383-03a)
[![Images](./images/#af0384-02)](ch09.xhtml#f0384-02a)
[![Images](./images/#af0385-01)](ch09.xhtml#f0384-02a)
[![Images](./images/#af0385-02)](ch09.xhtml#f0385-02a)
[![Images](./images/#af0386-01)](ch09.xhtml#f0385-02a)
[![Images](./images/#af0386-02)](ch09.xhtml#f0386-02a)
[![Images](./images/#af0386-03)](ch09.xhtml#f0386-03a)
[![Images](./images/#af0387-01)](ch09.xhtml#f0387-01a)
[![Images](./images/#af0388-01)](ch09.xhtml#f0388-01a)
[![Images](./images/#af0388-02)](ch09.xhtml#f0388-02a)
[![Images](./images/#af0389-01)](ch09.xhtml#f0389-01a)
[![Images](./images/#af0389-02)](ch09.xhtml#f0389-02a)
[![Images](./images/#af0390-01)](ch09.xhtml#f0390-01a)
[![Images](./images/#af0390-02)](ch09.xhtml#f0390-02a)
[![Images](./images/#af0391-01)](ch09.xhtml#f0390-02a)
[![Images](./images/#af0391-02)](ch09.xhtml#f0391-02a)
[![Images](./images/#af0391-03)](ch09.xhtml#f0391-03a)
[![Images](./images/#af0391-04)](ch09.xhtml#f0391-04a)
[![Images](./images/#af0392-01)](ch09.xhtml#f0391-04a)
[![Images](./images/#af0392-02)](ch09.xhtml#f0392-02a)
[![Images](./images/#af0392-03)](ch09.xhtml#f0392-03a)
[![Images](./images/#af0393-01)](ch09.xhtml#f0393-01a)
[![Images](./images/#af0394-01)](ch09.xhtml#f0394-01a)
[![Images](./images/#af0394-02)](ch09.xhtml#f0394-02a)
[![Images](./images/#af0395-01)](ch09.xhtml#f0394-02a)
[![Images](./images/#af0395-02)](ch09.xhtml#f0395-02a)
---
<a role="toc_link" id="ch10_images"></a>
[![Images](./images/#af0399-01)](ch10.xhtml#f0399-01a)
[![Images](./images/#af0400-01)](ch10.xhtml#f0399-01a)
[![Images](./images/#af0400-02)](ch10.xhtml#f0400-02a)
[![Images](./images/#af0400-03)](ch10.xhtml#f0400-03a)
[![Images](./images/#af0401-01)](ch10.xhtml#f0401-01a)
[![Images](./images/#af0401-02)](ch10.xhtml#f0401-02a)
[![Images](./images/#af0401-03)](ch10.xhtml#f0401-03a)
[![Images](./images/#af0402-01)](ch10.xhtml#f0402-01a)
[![Images](./images/#af0402-02)](ch10.xhtml#f0402-02a)
[![Images](./images/#af0403-01)](ch10.xhtml#f0403-01a)
[![Images](./images/#af0403-02)](ch10.xhtml#f0403-02a)
[![Images](./images/#af0403-03)](ch10.xhtml#f0403-03a)
[![Images](./images/#af0404-01)](ch10.xhtml#f0404-01a)
[![Images](./images/#af0404-02)](ch10.xhtml#f0404-02a)
[![Images](./images/#af0405-01)](ch10.xhtml#f0404-02a)
[![Images](./images/#af0405-02)](ch10.xhtml#f0405-02a)
[![Images](./images/#af0405-03)](ch10.xhtml#f0405-03a)
[![Images](./images/#af0405-04)](ch10.xhtml#f0405-04a)
[![Images](./images/#af0406-01)](ch10.xhtml#f0406-01a)
[![Images](./images/#af0407-01)](ch10.xhtml#f0407-01a)
[![Images](./images/#af0407-02)](ch10.xhtml#f0407-02a)
[![Images](./images/#af0408-01)](ch10.xhtml#f0408-01a)
[![Images](./images/#af0408-02)](ch10.xhtml#f0408-02a)
[![Images](./images/#af0409-01)](ch10.xhtml#f0409-01a)
[![Images](./images/#af0409-02)](ch10.xhtml#f0409-02a)
[![Images](./images/#af0410-01)](ch10.xhtml#f0410-01a)
[![Images](./images/#af0410-02)](ch10.xhtml#f0410-02a)
[![Images](./images/#af0410-03)](ch10.xhtml#f0410-03a)
[![Images](./images/#af0411-01)](ch10.xhtml#f0411-01a)
[![Images](./images/#af0411-02)](ch10.xhtml#f0411-02a)
[![Images](./images/#af0411-03)](ch10.xhtml#f0411-03a)
[![Images](./images/#af0411-04)](ch10.xhtml#f0411-04a)
[![Images](./images/#af0412-01)](ch10.xhtml#f0411-04a)
[![Images](./images/#af0412-02)](ch10.xhtml#f0412-02a)
[![Images](./images/#af0413-01)](ch10.xhtml#f0413-01a)
[![Images](./images/#af0413-02)](ch10.xhtml#f0413-02a)
[![Images](./images/#af0413-03)](ch10.xhtml#f0413-03a)
[![Images](./images/#af0414-01)](ch10.xhtml#f0414-01a)
[![Images](./images/#af0414-02)](ch10.xhtml#f0414-02a)
[![Images](./images/#af0415-01)](ch10.xhtml#f0415-01a)
[![Images](./images/#af0415-02)](ch10.xhtml#f0415-02a)
[![Images](./images/#af0416-02)](ch10.xhtml#f0416-02a)
[![Images](./images/#af0417-01)](ch10.xhtml#f0417-01a)
[![Images](./images/#af0417-02)](ch10.xhtml#f0417-02a)
[![Images](./images/#af0417-03)](ch10.xhtml#f0417-03a)
[![Images](./images/#af0418-01)](ch10.xhtml#f0417-03a)
[![Images](./images/#af0418-02)](ch10.xhtml#f0418-02a)
[![Images](./images/#af0419-01)](ch10.xhtml#f0419-01a)
[![Images](./images/#af0420-01)](ch10.xhtml#f0420-01a)
[![Images](./images/#af0421-01)](ch10.xhtml#f0421-01a)
[![Images](./images/#af0421-02)](ch10.xhtml#f0421-02a)
[![Images](./images/#af0422-01)](ch10.xhtml#f0421-02a)
[![Images](./images/#af0422-02)](ch10.xhtml#f0422-02a)
[![Images](./images/#af0422-03)](ch10.xhtml#f0422-03a)
[![Images](./images/#af0423-01)](ch10.xhtml#f0423-01a)
[![Images](./images/#af0423-02)](ch10.xhtml#f0423-02a)
[![Images](./images/#af0424-01)](ch10.xhtml#f0423-02a)
[![Images](./images/#af0424-02)](ch10.xhtml#f0424-02a)
[![Images](./images/#af0425-01)](ch10.xhtml#f0425-01a)
[![Images](./images/#af0425-02)](ch10.xhtml#f0425-02a)
[![Images](./images/#af0426-01)](ch10.xhtml#f0425-02a)
[![Images](./images/#af0426-02)](ch10.xhtml#f0426-02a)
[![Images](./images/#af0427-01)](ch10.xhtml#f0427-01a)
[![Images](./images/#af0427-02)](ch10.xhtml#f0427-02a)
[![Images](./images/#af0428-01)](ch10.xhtml#f0428-01a)
[![Images](./images/#af0428-02)](ch10.xhtml#f0428-02a)
[![Images](./images/#af0429-01)](ch10.xhtml#f0429-01a)
[![Images](./images/#af0429-02)](ch10.xhtml#f0429-02a)
[![Images](./images/#af0429-03)](ch10.xhtml#f0429-03a)
[![Images](./images/#af0430-01)](ch10.xhtml#f0429-03a)
[![Images](./images/#af0430-02)](ch10.xhtml#f0430-02a)
[![Images](./images/#af0430-03)](ch10.xhtml#f0430-03a)
[![Images](./images/#af0431-01)](ch10.xhtml#f0431-01a)
[![Images](./images/#af0431-02)](ch10.xhtml#f0431-02a)
[![Images](./images/#af0431-03)](ch10.xhtml#f0431-03a)
[![Images](./images/#af0432-01)](ch10.xhtml#f0432-01a)
[![Images](./images/#af0432-02)](ch10.xhtml#f0432-02a)
[![Images](./images/#af0432-03)](ch10.xhtml#f0432-03a)
[![Images](./images/#af0433-01)](ch10.xhtml#f0432-03a)
[![Images](./images/#af0433-02)](ch10.xhtml#f0433-02a)
[![Images](./images/#af0433-03)](ch10.xhtml#f0433-03a)
[![Images](./images/#af0434-01)](ch10.xhtml#f0433-03a)
[![Images](./images/#af0434-02)](ch10.xhtml#f0434-02a)
[![Images](./images/#af0434-03)](ch10.xhtml#f0434-03a)
[![Images](./images/#af0435-01)](ch10.xhtml#f0434-03a)
[![Images](./images/#af0435-02)](ch10.xhtml#f0435-02a)
[![Images](./images/#af0435-03)](ch10.xhtml#f0435-03a)
[![Images](./images/#af0436-01)](ch10.xhtml#f0436-01a)
[![Images](./images/#af0436-02)](ch10.xhtml#f0436-02a)
[![Images](./images/#af0437-01)](ch10.xhtml#f0437-01a)
[![Images](./images/#af0437-02)](ch10.xhtml#f0437-02a)
[![Images](./images/#af0438-01)](ch10.xhtml#f0437-02a)
[![Images](./images/#af0438-02)](ch10.xhtml#f0438-02a)
[![Images](./images/#af0439-01)](ch10.xhtml#f0438-02a)
[![Images](./images/#af0439-02)](ch10.xhtml#f0439-02a)
[![Images](./images/#af0439-03)](ch10.xhtml#f0439-03a)
[![Images](./images/#af0440-01)](ch10.xhtml#f0439-03a)
[![Images](./images/#af0440-02)](ch10.xhtml#f0440-02a)
[![Images](./images/#af0440-03)](ch10.xhtml#f0440-03a)
[![Images](./images/#af0441-01)](ch10.xhtml#f0440-03a)
[![Images](./images/#af0441-02)](ch10.xhtml#f0441-02a)
[![Images](./images/#af0441-03)](ch10.xhtml#f0441-03a)
[![Images](./images/#af0442-01)](ch10.xhtml#f0441-03a)
[![Images](./images/#af0442-02)](ch10.xhtml#f0442-02a)
[![Images](./images/#af0443-01)](ch10.xhtml#f0443-01a)
[![Images](./images/#af0443-02)](ch10.xhtml#f0443-02a)
[![Images](./images/#af0443-03)](ch10.xhtml#f0443-03a)
[![Images](./images/#af0443-05)](ch10.xhtml#f0443-05a)
[![Images](./images/#af0443-04)](ch10.xhtml#f0443-04a)
[![Images](./images/#af0445-01)](ch10.xhtml#f0445-01a)
[![Images](./images/#af0445-02)](ch10.xhtml#f0445-02a)
[![Images](./images/#af0446-01)](ch10.xhtml#f0445-02a)
---
<a role="toc_link" id="ch11_images"></a>
[![Images](./images/#af0448-01)](ch11.xhtml#f0448-01a)
[![Images](./images/#af0448-02)](ch11.xhtml#f0448-02a)
[![Images](./images/#af0448-03)](ch11.xhtml#f0448-03a)
[![Images](./images/#af0449-02)](ch11.xhtml#f0449-02a)
[![Images](./images/#af0450-01)](ch11.xhtml#f0449-02a)
[![Images](./images/#af0450-02)](ch11.xhtml#f0450-02a)
[![Images](./images/#af0450-03)](ch11.xhtml#f0450-03a)
[![Images](./images/#af0451-01)](ch11.xhtml#f0451-01a)
[![Images](./images/#af0452-01)](ch11.xhtml#f0452-01a)
[![Images](./images/#af0452-02)](ch11.xhtml#f0452-02a)
[![Images](./images/#af0454-01)](ch11.xhtml#f0454-01a)
[![Images](./images/#af0454-02)](ch11.xhtml#f0454-02a)
[![Images](./images/#af0454-03)](ch11.xhtml#f0454-03a)
[![Images](./images/#af0455-01)](ch11.xhtml#f0455-01a)
[![Images](./images/#af0455-02)](ch11.xhtml#f0455-02a)
[![Images](./images/#af0456-01)](ch11.xhtml#f0455-02a)
[![Images](./images/#af0456-02)](ch11.xhtml#f0456-02a)
[![Images](./images/#af0457-01)](ch11.xhtml#f0457-01a)
[![Images](./images/#af0457-02)](ch11.xhtml#f0457-02a)
[![Images](./images/#af0457-03)](ch11.xhtml#f0457-03a)
[![Images](./images/#af0457-04)](ch11.xhtml#f0457-04a)
[![Images](./images/#af0460-01)](ch11.xhtml#f0460-01a)
[![Images](./images/#af0463-01)](ch11.xhtml#f0463-01a)
[![Images](./images/#af0463-02)](ch11.xhtml#f0463-02a)
[![Images](./images/#af0463-03)](ch11.xhtml#f0463-03a)
[![Images](./images/#af0463-04)](ch11.xhtml#f0463-04a)
[![Images](./images/#af0464-01)](ch11.xhtml#f0464-01a)
[![Images](./images/#af0464-02)](ch11.xhtml#f0464-02a)
[![Images](./images/#af0464-03)](ch11.xhtml#f0464-03a)
[![Images](./images/#af0464-04)](ch11.xhtml#f0464-04a)
[![Images](./images/#af0465-01)](ch11.xhtml#f0465-01a)
[![Images](./images/#af0466-01)](ch11.xhtml#f0466-01a)
[![Images](./images/#af0467-01)](ch11.xhtml#f0466-01a)
[![Images](./images/#af0468-01)](ch11.xhtml#f0468-01a)
[![Images](./images/#af0468-02)](ch11.xhtml#f0468-02a)
[![Images](./images/#af0469-01)](ch11.xhtml#f0468-02a)
[![Images](./images/#af0469-02)](ch11.xhtml#f0469-02a)
[![Images](./images/#af0470-01)](ch11.xhtml#f0469-02a)
[![Images](./images/#af0470-02)](ch11.xhtml#f0470-02a)
[![Images](./images/#af0471-01)](ch11.xhtml#f0471-01a)
[![Images](./images/#af0472-01)](ch11.xhtml#f0472-01a)
[![Images](./images/#af0473-01)](ch11.xhtml#f0472-01a)
[![Images](./images/#af0473-02)](ch11.xhtml#f0473-02a)
[![Images](./images/#af0474-01)](ch11.xhtml#f0473-02a)
[![Images](./images/#af0476-01)](ch11.xhtml#f0476-01a)
[![Images](./images/#af0476-02)](ch11.xhtml#f0476-02a)
[![Images](./images/#af0476-03)](ch11.xhtml#f0476-03a)
[![Images](./images/#af0476-04)](ch11.xhtml#f0476-04a)
[![Images](./images/#af0477-01)](ch11.xhtml#f0476-04a)
[![Images](./images/#af0477-02)](ch11.xhtml#f0477-02a)
[![Images](./images/#af0477-03)](ch11.xhtml#f0477-03a)
[![Images](./images/#af0478-01)](ch11.xhtml#f0477-03a)
[![Images](./images/#af0478-02)](ch11.xhtml#f0478-02a)
[![Images](./images/#af0479-02)](ch11.xhtml#f0479-02a)
[![Images](./images/#af0479-03)](ch11.xhtml#f0479-03a)
[![Images](./images/#af0480-01)](ch11.xhtml#f0479-03a)
[![Images](./images/#af0480-02)](ch11.xhtml#f0480-02a)
[![Images](./images/#af0480-03)](ch11.xhtml#f0480-03a)
[![Images](./images/#af0480-04)](ch11.xhtml#f0480-04a)
[![Images](./images/#af0481-01)](ch11.xhtml#f0480-04a)
[![Images](./images/#af0481-02)](ch11.xhtml#f0481-02a)
[![Images](./images/#af0481-03)](ch11.xhtml#f0481-03a)
[![Images](./images/#af0482-01)](ch11.xhtml#f0481-03a)
[![Images](./images/#af0482-02)](ch11.xhtml#f0482-02a)
[![Images](./images/#af0482-03)](ch11.xhtml#f0482-03a)
[![Images](./images/#af0482-04)](ch11.xhtml#f0482-04a)
[![Images](./images/#af0483-01)](ch11.xhtml#f0482-04a)
[![Images](./images/#af0483-02)](ch11.xhtml#f0483-02a)
[![Images](./images/#af0484-01)](ch11.xhtml#f0484-01a)
[![Images](./images/#af0485-01)](ch11.xhtml#f0485-01a)
[![Images](./images/#af0486-01)](ch11.xhtml#f0485-01a)
[![Images](./images/#af0486-02)](ch11.xhtml#f0486-02a)
[![Images](./images/#af0486-03)](ch11.xhtml#f0486-03a)
[![Images](./images/#af0487-01)](ch11.xhtml#f0486-03a)
[![Images](./images/#af0487-02)](ch11.xhtml#f0487-02a)
[![Images](./images/#af0488-01)](ch11.xhtml#f0488-01a)
[![Images](./images/#af0488-02)](ch11.xhtml#f0488-02a)
[![Images](./images/#af0489-01)](ch11.xhtml#f0489-01a)
[![Images](./images/#af0489-02)](ch11.xhtml#f0489-02a)
[![Images](./images/#af0490-01)](ch11.xhtml#f0490-01a)
[![Images](./images/#af0490-02)](ch11.xhtml#f0490-02a)
[![Images](./images/#af0490-03)](ch11.xhtml#f0490-03a)
[![Images](./images/#af0490-04)](ch11.xhtml#f0490-04a)
[![Images](./images/#af0491-01)](ch11.xhtml#f0489-02a)
---
<a role="toc_link" id="ch12_images"></a>
[![Images](./images/#af0493-01)](ch12.xhtml#f0493-01a)
[![Images](./images/#af0494-01)](ch12.xhtml#f0494-01a)
[![Images](./images/#af0494-02)](ch12.xhtml#f0494-02a)
[![Images](./images/#af0495-01)](ch12.xhtml#f0495-01a)
[![Images](./images/#af0495-02)](ch12.xhtml#f0495-02a)
[![Images](./images/#af0495-03)](ch12.xhtml#f0495-03a)
[![Images](./images/#af0496-01)](ch12.xhtml#f0496-01a)
[![Images](./images/#af0496-02)](ch12.xhtml#f0496-02a)
[![Images](./images/#af0496-03)](ch12.xhtml#f0496-03a)
[![Images](./images/#af0497-01)](ch12.xhtml#f0497-01a)
[![Images](./images/#af0497-02)](ch12.xhtml#f0497-02a)
[![Images](./images/#af0497-03)](ch12.xhtml#f0497-03a)
[![Images](./images/#af0498-01)](ch12.xhtml#f0498-01a)
[![Images](./images/#af0498-02)](ch12.xhtml#f0498-02a)
[![Images](./images/#af0498-03)](ch12.xhtml#f0498-03a)
[![Images](./images/#af0499-01)](ch12.xhtml#f0499-01a)
[![Images](./images/#af0500-01)](ch12.xhtml#f0500-01a)
[![Images](./images/#af0500-02)](ch12.xhtml#f0500-02a)
[![Images](./images/#af0500-03)](ch12.xhtml#f0500-03a)
[![Images](./images/#af0501-01)](ch12.xhtml#f0501-01a)
[![Images](./images/#af0502-01)](ch12.xhtml#f0501-01a)
[![Images](./images/#af0502-02)](ch12.xhtml#f0502-02a)
[![Images](./images/#af0502-03)](ch12.xhtml#f0502-03a)
[![Images](./images/#af0503-01)](ch12.xhtml#f0502-03a)
[![Images](./images/#af0504-01)](ch12.xhtml#f0504-01a)
[![Images](./images/#af0504-02)](ch12.xhtml#f0504-02a)
[![Images](./images/#af0504-03)](ch12.xhtml#f0504-03a)
[![Images](./images/#af0505-01)](ch12.xhtml#f0505-01a)
[![Images](./images/#af0505-02)](ch12.xhtml#f0505-02a)
[![Images](./images/#af0506-01)](ch12.xhtml#f0506-01a)
[![Images](./images/#af0506-02)](ch12.xhtml#f0506-02a)
[![Images](./images/#af0506-03)](ch12.xhtml#f0506-03a)
[![Images](./images/#af0507-01)](ch12.xhtml#f0506-03a)
[![Images](./images/#af0507-02)](ch12.xhtml#f0507-02a)
[![Images](./images/#af0507-03)](ch12.xhtml#f0507-03a)
[![Images](./images/#af0508-01)](ch12.xhtml#f0507-03a)
[![Images](./images/#af0508-02)](ch12.xhtml#f0508-02a)
[![Images](./images/#af0508-03)](ch12.xhtml#f0508-03a)
[![Images](./images/#af0509-01)](ch12.xhtml#f0508-03a)
[![Images](./images/#af0510-01)](ch12.xhtml#f0510-01a)
[![Images](./images/#af0510-02)](ch12.xhtml#f0510-02a)
[![Images](./images/#af0510-03)](ch12.xhtml#f0510-03a)
[![Images](./images/#af0511-01)](ch12.xhtml#f0510-03a)
[![Images](./images/#af0511-02)](ch12.xhtml#f0511-02a)
[![Images](./images/#af0511-03)](ch12.xhtml#f0511-03a)
[![Images](./images/#af0511-04)](ch12.xhtml#f0511-04a)
[![Images](./images/#af0512-01)](ch12.xhtml#f0512-01a)
[![Images](./images/#af0512-02)](ch12.xhtml#f0512-02a)
[![Images](./images/#af0513-01)](ch12.xhtml#f0512-02a)
[![Images](./images/#af0513-02)](ch12.xhtml#f0513-02a)
[![Images](./images/#af0513-03)](ch12.xhtml#f0513-03a)
[![Images](./images/#af0514-01)](ch12.xhtml#f0513-03a)
[![Images](./images/#af0514-02)](ch12.xhtml#f0514-02a)
[![Images](./images/#af0515-01)](ch12.xhtml#f0515-01a)
[![Images](./images/#af0515-02)](ch12.xhtml#f0515-02a)
[![Images](./images/#af0515-03)](ch12.xhtml#f0515-03a)
[![Images](./images/#af0515-04)](ch12.xhtml#f0515-04a)
[![Images](./images/#af0516-01)](ch12.xhtml#f0516-01a)
[![Images](./images/#af0516-02)](ch12.xhtml#f0516-02a)
[![Images](./images/#af0516-03)](ch12.xhtml#f0516-03a)
[![Images](./images/#af0517-01)](ch12.xhtml#f0516-03a)
[![Images](./images/#af0517-02)](ch12.xhtml#f0517-02a)
[![Images](./images/#af0517-03)](ch12.xhtml#f0517-03a)
[![Images](./images/#af0518-01)](ch12.xhtml#f0518-01a)
[![Images](./images/#af0519-01)](ch12.xhtml#f0519-01a)
[![Images](./images/#af0520-01)](ch12.xhtml#f0519-01a)
[![Images](./images/#af0520-02)](ch12.xhtml#f0520-02a)
[![Images](./images/#af0520-03)](ch12.xhtml#f0520-03a)
[![Images](./images/#af0521-01)](ch12.xhtml#f0521-01a)
[![Images](./images/#af0521-02)](ch12.xhtml#f0521-02a)
[![Images](./images/#af0521-03)](ch12.xhtml#f0521-03a)
[![Images](./images/#af0522-01)](ch12.xhtml#f0522-01a)
[![Images](./images/#af0522-02)](ch12.xhtml#f0522-02a)
[![Images](./images/#af0522-03)](ch12.xhtml#f0522-03a)
[![Images](./images/#af0524-02)](ch12.xhtml#f0524-02a)
[![Images](./images/#af0525-01)](ch12.xhtml#f0525-01a)
[![Images](./images/#af0525-02)](ch12.xhtml#f0525-02a)
[![Images](./images/#af0525-03)](ch12.xhtml#f0525-03a)
[![Images](./images/#af0526-01)](ch12.xhtml#f0526-01a)
[![Images](./images/#af0527-01)](ch12.xhtml#f0526-01a)
[![Images](./images/#af0527-02)](ch12.xhtml#f0527-02a)
[![Images](./images/#af0527-03)](ch12.xhtml#f0527-03a)
[![Images](./images/#af0527-04)](ch12.xhtml#f0527-04a)
[![Images](./images/#af0527-05)](ch12.xhtml#f0527-05a)
[![Images](./images/#af0528-01)](ch12.xhtml#f0528-01a)
[![Images](./images/#af0528-02)](ch12.xhtml#f0528-02a)
[![Images](./images/#af0528-03)](ch12.xhtml#f0528-03a)
[![Images](./images/#af0528-04)](ch12.xhtml#f0528-04a)
[![Images](./images/#af0529-01)](ch12.xhtml#f0529-01a)
[![Images](./images/#af0529-05)](ch12.xhtml#f0529-05a)
[![Images](./images/#af0529-02)](ch12.xhtml#f0529-02a)
[![Images](./images/#af0529-03)](ch12.xhtml#f0529-03a)
[![Images](./images/#af0529-04)](ch12.xhtml#f0529-04a)
[![Images](./images/#af0530-01)](ch12.xhtml#f0529-04a)
[![Images](./images/#af0530-02)](ch12.xhtml#f0530-02a)
[![Images](./images/#af0530-03)](ch12.xhtml#f0530-03a)
[![Images](./images/#af0530-04)](ch12.xhtml#f0530-04a)
[![Images](./images/#af0530-05)](ch12.xhtml#f0530-05a)
[![Images](./images/#af0531-01)](ch12.xhtml#f0531-01a)
[![Images](./images/#af0531-02)](ch12.xhtml#f0531-02a)
[![Images](./images/#af0531-03)](ch12.xhtml#f0531-03a)
[![Images](./images/#af0531-04)](ch12.xhtml#f0531-04a)
[![Images](./images/#af0532-02)](ch12.xhtml#f0532-02a)
[![Images](./images/#af0532-01)](ch12.xhtml#f0532-01a)
---
<a role="toc_link" id="ch13_images"></a>
[![Images](./images/#af0534-01)](ch13.xhtml#f0534-01a)
[![Images](./images/#af0534-02)](ch13.xhtml#f0534-02a)
[![Images](./images/#af0534-03)](ch13.xhtml#f0534-03a)
[![Images](./images/#af0535-01)](ch13.xhtml#f0534-03a)
[![Images](./images/#af0535-02)](ch13.xhtml#f0535-02a)
[![Images](./images/#af0535-03)](ch13.xhtml#f0535-03a)
[![Images](./images/#af0536-01)](ch13.xhtml#f0535-03a)
[![Images](./images/#af0536-02)](ch13.xhtml#f0536-02a)
[![Images](./images/#af0537-01)](ch13.xhtml#f0537-01a)
[![Images](./images/#af0537-02)](ch13.xhtml#f0537-02a)
[![Images](./images/#af0538-01)](ch13.xhtml#f0537-02a)
[![Images](./images/#af0538-02)](ch13.xhtml#f0538-02a)
[![Images](./images/#af0539-01)](ch13.xhtml#f0538-02a)
[![Images](./images/#af0540-01)](ch13.xhtml#f0540-01a)
[![Images](./images/#af0540-02)](ch13.xhtml#f0540-02a)
[![Images](./images/#af0541-01)](ch13.xhtml#f0540-01a)
[![Images](./images/#af0542-01)](ch13.xhtml#f0542-01a)
[![Images](./images/#af0543-01)](ch13.xhtml#f0542-01a)
[![Images](./images/#af0543-02)](ch13.xhtml#f0543-01a)
[![Images](./images/#af0543-03)](ch13.xhtml#f0543-02a)
[![Images](./images/#af0544-01)](ch13.xhtml#f0543-02a)
[![Images](./images/#af0544-02)](ch13.xhtml#f0544-02a)
[![Images](./images/#af0544-03)](ch13.xhtml#f0544-03a)
[![Images](./images/#af0545-01)](ch13.xhtml#f0544-03a)
[![Images](./images/#af0545-02)](ch13.xhtml#f0545-02a)
[![Images](./images/#af0546-01)](ch13.xhtml#f0545-02a)
[![Images](./images/#af0546-02)](ch13.xhtml#f0546-02a)
[![Images](./images/#af0547-01)](ch13.xhtml#f0546-02a)
[![Images](./images/#af0547-02)](ch13.xhtml#f0547-01a)
[![Images](./images/#af0548-01)](ch13.xhtml#f0547-01a)
[![Images](./images/#af0548-02)](ch13.xhtml#f0548-02a)
[![Images](./images/#af0549-01)](ch13.xhtml#f0548-02a)
[![Images](./images/#af0550-01)](ch13.xhtml#f0550-01a)
[![Images](./images/#af0550-02)](ch13.xhtml#f0550-02a)
[![Images](./images/#af0551-01)](ch13.xhtml#f0551-01a)
[![Images](./images/#af0551-02)](ch13.xhtml#f0551-02a)
[![Images](./images/#af0551-03)](ch13.xhtml#f0551-03a)
[![Images](./images/#af0551-04)](ch13.xhtml#f0551-04a)
[![Images](./images/#af0552-01)](ch13.xhtml#f0552-01a)
[![Images](./images/#af0552-02)](ch13.xhtml#f0552-02a)
[![Images](./images/#af0552-03)](ch13.xhtml#f0552-03a)
[![Images](./images/#af0553-01)](ch13.xhtml#f0553-01a)
[![Images](./images/#af0553-02)](ch13.xhtml#f0553-02a)
[![Images](./images/#af0554-01)](ch13.xhtml#f0553-02a)
[![Images](./images/#af0554-02)](ch13.xhtml#f0554-02a)
[![Images](./images/#af0554-03)](ch13.xhtml#f0554-03a)
[![Images](./images/#af0555-01)](ch13.xhtml#f0554-03a)
[![Images](./images/#af0555-02)](ch13.xhtml#f0555-02a)
[![Images](./images/#af0555-03)](ch13.xhtml#f0555-03a)
[![Images](./images/#af0556-01)](ch13.xhtml#f0555-03a)
[![Images](./images/#af0556-02)](ch13.xhtml#f0556-02a)
[![Images](./images/#af0556-03)](ch13.xhtml#f0556-03a)
[![Images](./images/#af0557-01)](ch13.xhtml#f0556-03a)
[![Images](./images/#af0557-02)](ch13.xhtml#f0557-02a)
[![Images](./images/#af0557-03)](ch13.xhtml#f0557-03a)
[![Images](./images/#af0558-01)](ch13.xhtml#f0558-01a)
[![Images](./images/#af0559-01)](ch13.xhtml#f0559-01a)
[![Images](./images/#af0559-02)](ch13.xhtml#f0559-02a)
[![Images](./images/#af0560-01)](ch13.xhtml#f0559-02a)
[![Images](./images/#af0560-02)](ch13.xhtml#f0560-02a)
[![Images](./images/#af0560-03)](ch13.xhtml#f0560-03a)
[![Images](./images/#af0560-04)](ch13.xhtml#f0560-04a)
[![Images](./images/#af0561-01)](ch13.xhtml#f0560-04a)
[![Images](./images/#af0561-02)](ch13.xhtml#f0561-02a)
[![Images](./images/#af0561-03)](ch13.xhtml#f0561-03a)
[![Images](./images/#af0562-01)](ch13.xhtml#f0562-01a)
[![Images](./images/#af0563-01)](ch13.xhtml#f0563-01a)
[![Images](./images/#af0564-01)](ch13.xhtml#f0564-01a)
[![Images](./images/#af0565-01)](ch13.xhtml#f0565-01a)
[![Images](./images/#af0566-01)](ch13.xhtml#f0566-01a)
[![Images](./images/#af0566-02)](ch13.xhtml#f0566-02a)
[![Images](./images/#af0568-01)](ch13.xhtml#f0568-01a)
[![Images](./images/#af0568-02)](ch13.xhtml#f0568-02a)
[![Images](./images/#af0568-03)](ch13.xhtml#f0568-03a)
[![Images](./images/#af0569-01)](ch13.xhtml#f0568-03a)
[![Images](./images/#af0569-02)](ch13.xhtml#f0569-02a)
[![Images](./images/#af0569-03)](ch13.xhtml#f0569-03a)
[![Images](./images/#af0570-01)](ch13.xhtml#f0569-03a)
[![Images](./images/#af0571-01)](ch13.xhtml#f0571-01a)
[![Images](./images/#af0571-02)](ch13.xhtml#f0571-02a)
[![Images](./images/#af0572-01)](ch13.xhtml#f0571-02a)
[![Images](./images/#af0572-02)](ch13.xhtml#f0572-02a)
[![Images](./images/#af0573-01)](ch13.xhtml#f0572-02a)
[![Images](./images/#af0573-02)](ch13.xhtml#f0573-02a)
---
<a role="toc_link" id="ch14_images"></a>
[![Images](./images/#af0575-01)](ch14.xhtml#f0575-01a)
[![Images](./images/#af0576-01)](ch14.xhtml#f0575-01a)
[![Images](./images/#af0577-01)](ch14.xhtml#f0577-01a)
[![Images](./images/#af0577-02)](ch14.xhtml#f0577-02a)
[![Images](./images/#af0579-01)](ch14.xhtml#f0579-01a)
[![Images](./images/#af0579-03a)](ch14.xhtml#f0579-03a)
[![Images](./images/#af0579-04a)](ch14.xhtml#f0579-04a)
[![Images](./images/#af0579-03)](ch14.xhtml#f0579-05a)
[![Images](./images/#af0579-04)](ch14.xhtml#f0579-06a)
[![Images](./images/#af0580-01)](ch14.xhtml#f0579-06a)
[![Images](./images/#af0580-02)](ch14.xhtml#f0580-02a)
[![Images](./images/#af0580-03)](ch14.xhtml#f0580-03a)
[![Images](./images/#af0580-04)](ch14.xhtml#f0580-05a)
[![Images](./images/#af0581-01)](ch14.xhtml#f0580-05a)
[![Images](./images/#af0581-02)](ch14.xhtml#f0581-02a)
[![Images](./images/#af0581-03)](ch14.xhtml#f0581-03a)
[![Images](./images/#af0581-04)](ch14.xhtml#f0581-04a)
[![Images](./images/#af0581-05)](ch14.xhtml#f0581-05a)
[![Images](./images/#af0582-01)](ch14.xhtml#f0582-01a)
[![Images](./images/#af0582-02)](ch14.xhtml#f0582-02a)
[![Images](./images/#af0583-01)](ch14.xhtml#f0582-02a)
[![Images](./images/#af0583-02)](ch14.xhtml#f0583-02a)
[![Images](./images/#af0584-01)](ch14.xhtml#f0584-01a)
[![Images](./images/#af0585-01)](ch14.xhtml#f0585-01a)
[![Images](./images/#af0585-02)](ch14.xhtml#f0585-02a)
[![Images](./images/#af0586-01)](ch14.xhtml#f0586-01a)
[![Images](./images/#af0587-01)](ch14.xhtml#f0587-01a)
[![Images](./images/#af0589-01)](ch14.xhtml#f0589-01a)
[![Images](./images/#af0589-02)](ch14.xhtml#f0589-02a)
[![Images](./images/#af0589-03)](ch14.xhtml#f0589-03a)
[![Images](./images/#af0589-04)](ch14.xhtml#f0589-04a)
[![Images](./images/#af0590-01)](ch14.xhtml#f0590-01a)
[![Images](./images/#af0590-02)](ch14.xhtml#f0590-02a)
[![Images](./images/#af0591-01)](ch14.xhtml#f0590-02a)
[![Images](./images/#af0591-02)](ch14.xhtml#f0591-02a)
[![Images](./images/#af0594-01)](ch14.xhtml#f0594-01a)
[![Images](./images/#af0594-02)](ch14.xhtml#f0594-02a)
[![Images](./images/#af0595-01)](ch14.xhtml#f0594-02a)
[![Images](./images/#af0595-02)](ch14.xhtml#f0595-02a)
[![Images](./images/#af0596-01)](ch14.xhtml#f0596-01a)
[![Images](./images/#af0596-02)](ch14.xhtml#f0596-02a)
[![Images](./images/#af0597-01)](ch14.xhtml#f0597-01a)
[![Images](./images/#af0597-02)](ch14.xhtml#f0597-02a)
[![Images](./images/#af0598-01)](ch14.xhtml#f0597-02a)
[![Images](./images/#af0598-02)](ch14.xhtml#f0598-02a)
[![Images](./images/#af0598-03)](ch14.xhtml#f0598-03a)
[![Images](./images/#af0599-01)](ch14.xhtml#f0598-03a)
[![Images](./images/#af0599-02)](ch14.xhtml#f0599-02a)
[![Images](./images/#af0600-01)](ch14.xhtml#f0600-01a)
[![Images](./images/#af0601-01)](ch14.xhtml#f0601-01a)
[![Images](./images/#af0603-01)](ch14.xhtml#f0603-01a)
[![Images](./images/#af0604-01)](ch14.xhtml#f0604-01a)
[![Images](./images/#af0606-01)](ch14.xhtml#f0606-01a)
[![Images](./images/#af0606-02)](ch14.xhtml#f0606-02a)
[![Images](./images/#af0607-01)](ch14.xhtml#f0606-02a)
[![Images](./images/#af0608-01)](ch14.xhtml#f0608-01a)
[![Images](./images/#af0609-01)](ch14.xhtml#f0608-01a)
[![Images](./images/#af0609-02)](ch14.xhtml#f0609-02a)
[![Images](./images/#af0609-03)](ch14.xhtml#f0609-03a)
[![Images](./images/#af0610-01)](ch14.xhtml#f0609-03a)
[![Images](./images/#af0610-02)](ch14.xhtml#f0610-02a)
[![Images](./images/#af0611-01)](ch14.xhtml#f0610-02a)
[![Images](./images/#af0611-02)](ch14.xhtml#f0611-02a)
[![Images](./images/#af0611-03)](ch14.xhtml#f0611-03a)
[![Images](./images/#af0611-04)](ch14.xhtml#f0611-04a)
[![Images](./images/#af0612-01)](ch14.xhtml#f0612-01a)
[![Images](./images/#af0612-02)](ch14.xhtml#f0612-02a)
[![Images](./images/#af0613-01)](ch14.xhtml#f0612-02a)
[![Images](./images/#af0613-02)](ch14.xhtml#f0613-02a)
[![Images](./images/#af0614-01)](ch14.xhtml#f0614-01a)
[![Images](./images/#af0614-02)](ch14.xhtml#f0614-02a)
[![Images](./images/#af0614-03)](ch14.xhtml#f0614-03a)
[![Images](./images/#af0615-01)](ch14.xhtml#f0614-03a)
[![Images](./images/#af0615-02)](ch14.xhtml#f0615-02a)
[![Images](./images/#af0615-03)](ch14.xhtml#f0615-03a)
[![Images](./images/#af0616-01)](ch14.xhtml#f0615-03a)
[![Images](./images/#af0616-02)](ch14.xhtml#f0616-02a)
[![Images](./images/#af0616-03)](ch14.xhtml#f0616-03a)
[![Images](./images/#af0617-01)](ch14.xhtml#f0616-03a)
[![Images](./images/#af0617-02)](ch14.xhtml#f0617-02a)
[![Images](./images/#af0618-01)](ch14.xhtml#f0618-01a)
[![Images](./images/#af0618-02)](ch14.xhtml#f0618-02a)
[![Images](./images/#af0619-01)](ch14.xhtml#f0619-01a)
[![Images](./images/#af0619-02)](ch14.xhtml#f0619-02a)
[![Images](./images/#af0619-03)](ch14.xhtml#f0619-03a)
[![Images](./images/#af0620-01)](ch14.xhtml#f0619-03a)
[![Images](./images/#af0622-01)](ch14.xhtml#f0622-01a)
[![Images](./images/#af0622-02)](ch14.xhtml#f0622-02a)
[![Images](./images/#af0622-03)](ch14.xhtml#f0622-03a)
[![Images](./images/#af0623-01)](ch14.xhtml#f0623-01a)
[![Images](./images/#af0623-02)](ch14.xhtml#f0623-02a)
[![Images](./images/#af0624-01)](ch14.xhtml#f0624-01a)
[![Images](./images/#af0624-02)](ch14.xhtml#f0624-02a)
[![Images](./images/#af0625-01)](ch14.xhtml#f0625-01a)
[![Images](./images/#af0626-01)](ch14.xhtml#f0626-01a)

---

## 统计信息

- **总处理块数**: 37
- **原始总token数**: 164,028
- **总结总token数**: 56,615
- **整体压缩比**: 34.52%
- **平均压缩比**: 12946.53%
- **处理章节数**: 37


*此文档由MinerU内容总结器V2自动生成，基于Langchain Markdown分割技术。*