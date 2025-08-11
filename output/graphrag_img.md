# Retrieval-Augmented Generation with Graphs (GraphRAG) (标准版) - 中文总结 (70%)

## 生成信息
- **压缩级别**: 70%
- **生成时间**: 2025-08-10 13:15:24
- **工具**: MinerU内容总结器 V2
- **原始块数**: 90
- **处理章节数**: 90
- **压缩比**: 8.56%

## 目录
- [Retrieval-Augmented Generation with Graphs (GraphRAG)](#retrieval-augmented-generation-with-graphs-graphrag)
- [Abstract](#abstract)
- [1 Introduction](#1-introduction)
- [2 A Holistic Framework of GraphRAG](#2-a-holistic-framework-of-graphrag)
- [2.1 Problem Setting and Notations](#21-problem-setting-and-notations)
- [2.2 Task Applications and Example Query  $Q$](#22-task-applications-and-example-query-q)
- [2.3 Query Processor  $\Omega^{\mathrm{Processor}}$](#23-query-processor-omegamathrmprocessor)
- [2.3.1 Name Entity Recognition](#231-name-entity-recognition)
- [2.3.2 Relational Extraction](#232-relational-extraction)
- [2.3.3 Query Structuration](#233-query-structuration)
- [2.3.4 Query Decomposition](#234-query-decomposition)
- [2.3.5 Query Expansion](#235-query-expansion)
- [2.4 Retriever  $\Omega^{\mathrm{Retriever}}$](#24-retriever-omegamathrmretriever)
- [2.4.1 Heuristic-based Retriever](#241-heuristic-based-retriever)
- [2.4.2 Learning-based Retriever](#242-learning-based-retriever)
- [2.4.3 Advanced Retrieval Strategies](#243-advanced-retrieval-strategies)
- [2.5 Organizer](#25-organizer)
- [2.5.1 Graph Pruning](#251-graph-pruning)
- [2.5.2 Reranker](#252-reranker)
- [2.5.3 Graph Augmentation](#253-graph-augmentation)
- [2.5.4 Verbalizing](#254-verbalizing)
- [2.6 Generator](#26-generator)
- [2.6.1 Discrimination-based Generator](#261-discrimination-based-generator)
- [2.6.2 LLM-based Generator](#262-llm-based-generator)
- [2.6.3 Graph-based Generator](#263-graph-based-generator)
- [2.7 Graph Datasources](#27-graph-datasources)
- [3 Knowledge Graph](#3-knowledge-graph)
- [3.1 Application Tasks](#31-application-tasks)
- [3.2 Knowledge Graph Construction](#32-knowledge-graph-construction)
- [3.3 Retriever](#33-retriever)
- [3.4 Organizer](#34-organizer)
- [3.5 Generator](#35-generator)
- [3.6 Resources and Tools](#36-resources-and-tools)
- [3.6.1 Data Resources](#361-data-resources)
- [3.6.2 Tools](#362-tools)
- [4 Document Graph](#4-document-graph)
- [4.1 Application Tasks](#41-application-tasks)
- [4.2 Document Graph Construction](#42-document-graph-construction)
- [4.3 Retriever](#43-retriever)
- [4.4 Organizer](#44-organizer)
- [4.5 Generator](#45-generator)
- [4.6 Resources and Tools](#46-resources-and-tools)
- [5 Scientific Graph](#5-scientific-graph)
- [5.1 Application Tasks](#51-application-tasks)
- [5.2 Scientific Graph Construction](#52-scientific-graph-construction)
- [5.3 Retriever](#53-retriever)
- [5.4 Organizer](#54-organizer)
- [5.5 Generator](#55-generator)
- [5.6 Resources and Tools](#56-resources-and-tools)
- [5.6.1 Data Resources](#561-data-resources)
- [5.6.2 Tools](#562-tools)
- [6 Social Graph](#6-social-graph)
- [6.1 Application Tasks](#61-application-tasks)
- [6.2 Social Graph Construction](#62-social-graph-construction)
- [6.3 Retriever](#63-retriever)
- [6.4Organizer](#64organizer)
- [6.5 Generator](#65-generator)
- [6.6Resources and Tools](#66resources-and-tools)
- [6.6.1 Data Resources](#661-data-resources)
- [6.6.2 Tools](#662-tools)
- [7 Planning and Reasoning Graph](#7-planning-and-reasoning-graph)
- [7.1 Application Tasks](#71-application-tasks)
- [7.2 Reasoning and Planning Graph Construction](#72-reasoning-and-planning-graph-construction)
- [7.3 Retriever](#73-retriever)
- [7.4 Organizer](#74-organizer)
- [7.5 Generator](#75-generator)
- [7.6 Resources and Tools](#76-resources-and-tools)
- [7.7 Data Resources](#77-data-resources)
- [7.7.1 Tools](#771-tools)
- [8 Tabular Graph](#8-tabular-graph)
- [8.1 Application Tasks](#81-application-tasks)
- [8.2 Tabular Graph Construction](#82-tabular-graph-construction)
- [8.3 Retriever](#83-retriever)
- [8.4 Generator](#84-generator)
- [8.5 Resources and Tools](#85-resources-and-tools)
- [8.5.1 Data Resources](#851-data-resources)
- [8.5.2 Tools](#852-tools)
- [9 Other Domains](#9-other-domains)
- [9.1 Infrastructure Graph](#91-infrastructure-graph)
- [9.2 Single-cell Graph](#92-single-cell-graph)
- [9.3 Scene Graph](#93-scene-graph)
- [10 Challenges and Future Work](#10-challenges-and-future-work)
- [10.1 Graph Construction](#101-graph-construction)
- [10.2 Retriever](#102-retriever)
- [10.3Organizer](#103organizer)
- [10.4Generator](#104generator)
- [10.5 GraphRAG as a System](#105-graphrag-as-a-system)
- [10.6 Evaluation of GraphRAG.](#106-evaluation-of-graphrag)
- [10.7 New Applications](#107-new-applications)
- [11 Conclusion](#11-conclusion)

## Retrieval-Augmented Generation with Graphs (GraphRAG)

该章节介绍了一个名为GraphRAG（Retrieval-Augmented Generation with Graphs）的框架，其核心贡献在于将图结构深度整合到检索增强生成（Retrieval-Augmented Generation, RAG）流程中。

该研究的主要论点是，传统的RAG系统在检索时通常处理的是独立的文本区块，这可能导致上下文信息不完整或缺乏深层联系。GraphRAG框架旨在通过构建和利用数据的底层图结构来解决这一问题。其核心方法论是，首先将源数据（如文档集合）转换为一个知识图谱（Knowledge Graph），其中实体为节点，关系为边。在生成答案的检索阶段，系统不再是简单地寻找相似的文本片段，而是在图上进行检索，以获取与问题相关的、结构化的、互联的上下文信息。这种基于图的检索能够捕获实体之间更丰富的关系和更全面的背景知识。

最终，通过向大型语言模型（LLM）提供这种结构化、上下文更丰富的知识，GraphRAG旨在显著提升生成结果的质量，使其在准确性、连贯性和深度上优于传统的RAG方法。这项工作由来自密歇根州立大学、俄勒冈大学等顶尖学术机构与Meta、Amazon、Adobe Research等多个行业研究实验室的学者共同完成，显示了该技术在学术界与工业界均具有重要的应用前景。

## Abstract

`Retrieval-augmented generation (RAG)` 是一种通过从外部来源检索知识、技能和工具等额外信息来增强下游任务执行的强大技术。`Graph` 以其固有的“节点由边连接”的特性，编码了海量的异构和关系信息，使其成为众多现实世界应用中 `RAG` 的宝贵资源。因此，近期将 `RAG` 与 `Graph` 结合，即 `GraphRAG`，受到了越来越多的关注。然而，与传统的 `RAG` 不同（其 `retriever`、`generator` 和外部数据源可以在神经嵌入空间中统一设计），图结构数据的独特性，如格式多样和领域特定的关系知识，在为不同领域设计 `GraphRAG` 时带来了独特且重大的挑战。鉴于 `GraphRAG` 的广泛适用性、相关的设计挑战以及近期的快速发展，迫切需要对其关键概念和技术进行系统和及时的综述。

基于此动机，本研究对 `GraphRAG` 进行了全面且最新的综述。我们的综述首先提出了一个整体的 `GraphRAG` 框架，定义了其关键组件，包括 `query processor`、`retriever`、`organizer`、`generator` 和 `data source`。此外，我们认识到不同领域的图展现出不同的关系模式并需要专门的设计，因此回顾了为每个领域独特定制的 `GraphRAG` 技术。最后，我们讨论了研究挑战并展望了未来方向，以激发跨学科的合作机会。本综述的资源库公开维护于 https://github.com/Graph-RAG/GraphRAG/。

## 1 Introduction

`RAG` (Retrieval-Augmented Generation) 是一种通过从外部数据源检索附加信息来增强下游任务的强大技术，已成功应用于多种现实场景。在 `RAG` 框架中，检索器根据用户查询或任务指令搜索知识、技能和工具，检索到的内容由组织器提炼并与原始查询无缝集成，最终送入生成器产生答案。例如，在问答任务中，经典的 "Retriever-then-Reader" 框架通过检索外部事实知识来提高答案的忠实度。`LLMs` 的最新进展进一步凸显了 `RAG` 在增强模型社会责任方面的能力，如减轻幻觉、增强可解释性、实现动态适应性、降低隐私风险、确保可靠性及促进公平性。

基于 `RAG` 的成功以及图结构数据在现实世界中的普遍性，近期研究开始探索将 `RAG` 与图结构数据相结合，催生了 `GraphRAG`。与主要依赖语义/词汇相似性搜索的 `RAG` 不同，图结构数据通过其固有的“节点由边连接”的特性编码了异构和关系信息。`GraphRAG` 利用基于图的机器学习（如 `Graph Neural Networks (GNNs)`）和图/网络分析技术（如 Graph Traversal Search 和 Community Detection）来捕获关系知识，从而展现出独特优势。例如，对于查询“哪些药物用于治疗上皮样肉瘤并且影响EZH2基因产物？”，仅依赖语义相似性的搜索会忽略图结构中编码的关系知识。而 `GraphRAG` 方法可以沿着关系路径“疾病(上皮样肉瘤) → [适应症] → 药物 ← [靶点] ← 基因/蛋白质(EZH2基因产物)”进行图遍历，从而精确检索。此外，某些领域的实体具有极其复杂的几何结构，如分子图中的3D结构和产品分类、文档结构、社交网络中常见的层次树结构，这需要精心设计的图编码器来捕捉结构细微差别。简单地将节点文本语言化并输入 `LLMs` 无法表达复杂的几何信息，并且随着邻域扩展，文本描述会呈指数级增长，变得不可行。

尽管 `GraphRAG` 优势明显，但由于图结构数据存在以下差异，其设计面临着前所未有的挑战：

*   **统一与多样化格式信息的差异**：传统 `RAG` 处理的信息（如图像块或文本序列）可以统一表示，而图结构数据格式多样，存储在异构来源中。例如，文档图将实体嵌入为句子块，知识图以三元组或路径存储信息，分子图包含高阶结构。![](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/4b4ef89fcdd80b7fa9755c6b4ec559b92a5bd7539131eae139911bc0b3d2cf7d_b2ef8b56.jpg) 如图1所示，这种多样性要求 `RAG` 进行差异化设计。对于检索器，传统 `RAG` 的“一刀切”嵌入式检索方法不再适用，`GraphRAG` 的检索器必须考虑信息的具体格式和来源。例如，在知识图问答中，通常需要通过实体链接、关系匹配和图搜索算法（如 `Breadth-First Search`, `A* search`）来获取节点/边/子图，然后才能进行嵌入匹配。此外，检索器需要具备足够的几何表达能力以捕捉结构细微差别，例如在规划图中检索API时需具备方向感知能力，在药物设计中需能区分不同的子图结构。对于生成器，当检索内容包含复杂的图结构和文本属性时，简单地将子图文本串联成提示会丢失关键结构信息，此时需要使用 `GNNs` 等图编码器对图进行编码，以保留结构细节。

*   **独立与相互依赖信息的差异**：在传统 `RAG` 中，信息（如文档块）被独立存储和使用，这阻碍了需要多跳推理的任务。而 `GraphRAG` 将信息块存储为相互连接的节点，边表示它们的关系。这种相互依赖性在检索、组织和生成阶段均有助益。在检索时，边可以实现多跳遍历；在组织时，内容不仅可以按语义排序，还可以按结构关系进行剪枝（`graph pruning`）；在生成时，将相互依赖性（如 `positional encoding`）传递给生成器，可以使生成内容包含更丰富的结构信号。

*   **领域不变性与领域特定信息的差异**：图结构数据中的关系是高度领域特定的。与图像和文本（在不同领域间常有可迁移的语义，如纹理或词汇）不同，图结构数据缺乏明确的可迁移单元。图像和文本的共享基础使其编码器可以设计成具有几何不变性，并遵循数据规模定律。然而，不同领域图数据的底层生成过程差异巨大，导致关系信息高度领域化，几乎不可能设计出适用于所有领域的统一 `GraphRAG`。例如，预测学术论文主题时，可以利用同质性（homophily）假设检索其参考文献；但在分类航线网络中机场的角色时，枢纽机场通常分布稀疏且无直接连接，同质性假设不再适用。即使在同一领域同一张图中，不同任务也可能需要不同的 `GraphRAG` 设计。例如，在设计自动邮件补全系统时，为保证内容相关性，可检索同一对话线程的邮件；而为保持语气一致性，则可能需要检索公司内担任相似结构角色的员工邮件。

尽管上述差异推动了 `GraphRAG` 的广泛研究，但该领域目前的研究格局仍然分散，概念、技术和数据集差异巨大。此外，当前研究主要集中在知识图和文档图（如图2所示），忽视了在基础设施图等其他领域的应用，这可能导致“泡沫效应”。![](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/22ce1051b1d5190a0f1df57271978afd9b5eaaecf183f4b7ae36a266d01c76fb_59bf12bb.jpg) 为应对这些挑战，本综述旨在对 `GraphRAG` 进行全面回顾，从全局视角统一其框架，并从局部视角针对各领域进行专门化设计。本综述的主要贡献如下：

*   **一个 `GraphRAG` 的整体框架**：我们提出了一个包含五个关键组件的 `GraphRAG` 整体框架：查询处理器、检索器、组织器、生成器和图数据源，并回顾了每个组件的代表性技术。
*   **`GraphRAG` 在不同领域的专门化**：我们将 `GraphRAG` 的设计根据其具体应用分为10个不同领域，包括知识图、文档图、科学图、社交图、规划与推理图、表格图、基础设施图、生物图、场景图和随机图。我们回顾了每个领域的独特应用和图构建方法，并总结了我们提出的整体框架中各组件的独特设计，同时收集了丰富的基准数据集和工具资源。
*   **挑战与未来方向**：我们指出了当前 `GraphRAG` 研究面临的挑战，并为推动该领域进入新前沿指明了未来机遇。

本综述不同于现有综述。多数现有综述关注的是基于i.i.d.数据的通用 `RAG`。尽管近期有综述探讨了由基础模型驱动的多模态 `RAG`，但均未专门关注图结构数据。据我们所知，仅有一篇近期研究[319]专门探讨了图结构数据背景下的 `RAG`，但其主要在传统 `RAG` 架构下回顾图引入的技术，未针对不同领域图的多样化关系和技术设计进行专门化审视。与这种整体性回顾理念相反，我们认识到图结构数据的内在异构性，并跨不同领域对 `GraphRAG` 进行了专门化回顾，揭示了每个领域的基本任务应用、图构建方法和关系原理，以及具体的 `GraphRAG` 技术。

本综述的结构如下：第二节介绍 `GraphRAG` 的整体框架及其五个关键组件的代表性技术。![](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/3ea38d6e1639308a00bcdccc4d6583a253cc3cad7b4a69fca85891faddf106c4_adda05af.jpg) 第三至九节深入探讨特定领域，回顾其独特的任务应用、图构建方法、领域特定的技术设计，并介绍相关资源。最后，第十节讨论研究挑战与机遇，第十一节进行总结。

## 2 A Holistic Framework of GraphRAG

本章基于现有关于GraphRAG的文献，提出了一个GraphRAG的整体性框架。接下来，将介绍贯穿整个框架所使用的基本问题设定与符号表示。

## 2.1 Problem Setting and Notations

该章节定义了GraphRAG的问题设定与符号体系。其核心框架遵循通用的RAG流程，包含五个关键组件：

1.  **Query Processor** `Ω^Processor`：对用户给定的查询`Q`进行预处理，生成`hat(Q) = Ω^Processor(Q)`。
2.  **Graph Data Source** `G`：以图结构格式组织的信息源。
3.  **Retriever** `Ω^Retriever`：根据预处理后的查询`hat(Q)`，从图数据源`G`中检索相关内容`C = Ω^Retriever(hat(Q),G)`。
4.  **Organizer** `Ω^Organizer`：对检索到的内容`C`进行整理和精炼，以形成精炼后的内容`hat(C) = Ω^Organizer(hat(Q),C)`。
5.  **Generator** `Ω^General`：结合查询`hat(Q)`与精炼内容`hat(C)`，生成最终答案`A = Ω^General(hat(Q),hat(C))`。

与基于序列的文本数据和基于网格的图像数据不同，图结构数据封装了丰富的关系信息。为了有效利用这些信息，GraphRAG的上述五个核心组件需要经过专门设计，以处理图结构的输入/输出并支持基于图的操作。例如，在`Retriever`组件中，自然语言处理（NLP）领域的传统RAG通常利用稀疏/密集编码器进行索引搜索。相比之下，GraphRAG则采用图遍历方法（如entity linking和BFS/DFS）以及基于图的编码器（如`Graph Neural Networks (GNNs)`）来生成用于检索的`embeddings`。这促使本文在GraphRAG的整体框架下，对这五个组件各自的关键创新和代表性设计进行总结。

## 2.2 Task Applications and Example Query  $Q$

在GraphRAG框架中，查询`Q`与通用RAG框架类似，用于指定问题背景或任务指令。`Q`可以是文本格式，例如在基于Knowledge Graph的问答任务中，查询可以是“中国的首都是哪里？”。此外，查询`Q`也可以是其他格式，例如用于分子图的SMILES字符串，甚至可以是多模态格式的组合，如场景图与文本指令的结合。表1总结了GraphRAG在各个领域中的常见任务应用、示例查询及其代表性参考文献。

![](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/cd7cf8ad709257c8a549944e2f17374b61a01b7f9eefbf37b4bb9d25d7c83b0c_3498b220.jpg)

上图（图4）展示了GraphRAG中查询处理器$\Omega^{\mathrm{Processor}}$的现有技术。表2则详细对比了RAG和GraphRAG在查询处理器$\Omega^{\mathrm{Processor}}$上的关键差异，这些差异凸显了GraphRAG为适应图结构数据而进行的专门设计：

*   **Entity Recognition**：RAG从知识库中提取实体提及（mentions），而GraphRAG则专注于从图中提取被提及的节点。
*   **Relational Extraction**：RAG从文本中提取关系，而GraphRAG则从图中提取由边（edge）表示的关系。
*   **Query Structuration**：RAG通常将文本查询结构化为SQL或SPARQL，而GraphRAG则倾向于将查询结构化为GQL（Graph Query Language）。
*   **Query Decomposition**：在RAG中，分解后的子查询通常是相互独立的；而在GraphRAG中，由于图的内在连通性，分解后的子查询在逻辑上是相互关联的。
*   **Query Expansion**：RAG主要基于语义知识进行查询扩展，而GraphRAG则利用图结构所提供的关系知识（relational knowledge）进行扩展。

## 2.3 Query Processor  $\Omega^{\mathrm{Processor}}$

查询处理器 $\Omega^{\mathrm{Processor}}$ 的核心挑战在于处理GraphRAG中的格式不匹配问题。与查询和数据源均为纯文本格式的RAG不同，GraphRAG的数据源是图结构的，这给连接文本格式的查询与图结构的数据源带来了困难。例如，对于查询“Who is Justin Bieber's brother?”，连接知识图谱与该查询的关键信息并非某个特定文本段落，而是实体“Justin Bieber”和关系“brother of”。为了从查询中准确提取此类结构化信息，学界提出了多种技术，主要包括entity recognition、relational extraction、query structuration、query decomposition和query expansion。本节将首先在更广泛的NLP领域回顾这五种查询处理技术，随后重点探讨它们在GraphRAG中的独特应用与调整。

## 2.3.1 Name Entity Recognition

Named Entity Recognition (NER) 旨在从文本中识别隶属于预定义类别的实体（如人名、地名、组织机构），是众多自然语言应用的基础组件。NER技术大致可分为四类：基于规则的方法、无监督学习方法、基于特征的监督学习方法以及深度学习方法。近期的LLMs属于深度学习方法，并在NER任务上取得了前所未有的成功。

在GraphRAG的背景下，实体识别主要采用深度学习技术（如EntityLinker和基于LLM的抽取方法）来识别查询中的实体，并将其与给定图数据源中的节点进行关联。这一步骤对于基于知识图谱的问答等应用至关重要。例如，对于问题“预测婴儿眼睛颜色的最佳方法是什么？”，NER会抽取出“婴儿”、“眼睛”和“颜色”等实体，这些实体对应知识图谱中的节点，并作为种子节点来初始化后续的检索过程。

在更近期的GraphRAG研究中，NER的功能已从单纯识别实体名称扩展到识别其结构。例如，Jin等人[186]利用LLMs来识别图中的节点类型，从而进一步指导检索器识别匹配该类型的节点以进行下一轮探索。例如，对于问题“‘Language Models are Unsupervised Multi-task Learners’的作者是谁？”，初始识别的实体不仅应基于其语义名称“Language Models are Unsupervised Multi-task Learners”，还应基于该实体的类型，即本例中的“论文”节点。在GraphRAG中准确识别实体的名称和结构，能够减少级联错误，并为后续的检索和生成步骤提供坚实的基础。

## 2.3.2 Relational Extraction

关系抽取（Relational Extraction, RE）是NLP领域的一项成熟技术，旨在识别实体间的关系，并广泛应用于结构化搜索、情感分析、问答、摘要生成及knowledge graph构建。近年来，RE的发展主要由深度学习技术推动，其研究可概括为文本表示、上下文编码和triplet预测三个方面。

在GraphRAG框架中，RE主要服务于两个目的：其一，通过提取triplets来构建图结构化数据源（例如knowledge graphs）；其二，匹配用户查询中提及的关系与图数据源中的关系，以指导图搜索过程。例如，对于“中国的首都是什么？”这样的查询，RE会识别出“capital of”这一关系，并通过vector similarity在knowledge graph中搜索相应的边，从而为neighborhood selection和graph traversal指明方向。

## 2.3.3 Query Structuration

`Query Structuration`旨在将查询转换为适配特定数据源和任务的格式。它通常将自然语言查询转化为如`SQL`或`SPARQL`等结构化格式，以便与关系数据库进行交互。近期的研究进展利用经过预训练和`fine-tuning`的`LLMs`，从自然语言输入生成结构化查询以操作数据库。针对图结构化数据，已出现`Graph Query Language (GQL)`，例如`Cypher`、`GraphQL`和`SPARQL`，这些语言能够实现与属性图数据库的复杂交互。此外，Jin等人[186]引入了一种技术，该技术将复杂查询分解为多个结构化操作，包括节点检索、特征获取、邻居检查和度评估，从而增强了查询的精确性和适应性。

## 2.3.4 Query Decomposition

`Query decomposition` [447] 旨在将输入查询分解为多个不同的子查询，这些子查询首先用于检索子结果，然后将这些子结果聚合以形成最终答案。在多数现有的 `RAG` 和 `GraphRAG` 中，分解后的查询通常具有明确的逻辑联系，能够处理需要多步推理和规划的复杂任务 [248, 316, 355, 372, 477]。例如，一个查询“请生成一张女孩读书的图片，其姿势与‘example.jpg’中的男孩相同，然后用语音描述这张新图片”涉及多个子任务 [477]，每个子任务都由一个特定的子查询完成。此外，Park等人 [316] 通过构建一个“问题图”（question graph）来增强查询分解，其中每个子查询在图中被表示为一个三元组。这种图结构的子查询能通过多步提示（multi-step promptings）有效引导检索器或生成器。

## 2.3.5 Query Expansion

`Query Expansion`通过添加具有相似意义的术语来丰富查询，主要旨在解决三个挑战：(1) 用户提交的查询可能模棱两可，涉及多个主题；(2) 查询可能过于简短，无法完全捕捉用户意图；(3) 用户通常不确定他们正在寻找什么。`Query Expansion`通常可分为手动、自动和交互式三类。近期，由于生成内容的创造性，基于`LLM`的`Query Expansion`已成为一个重要领域。

与现有方法大多关注文本相似性而忽略关系不同，`GraphRAG`中的`Query Expansion`利用结构化关系来增强`LLM`的扩展能力。例如，Xia等人[459]通过利用查询中提及实体的邻近节点来扩展查询。另外，Wang等人[406]使用预定义的模板将查询转换为多个子查询。

![](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/23a20f8c454fce38d5b75192224a1b52113bba7a200bb8c64ed0f2e5d7aa67b3_dd422c92.jpg)
图5：可视化了`GraphRAG`中使用的代表性检索器。
表3：对`GraphRAG`中使用的代表性检索器进行了分类。
<table><tr><td>方法/策略</td><td>输入</td><td>输出</td><td>描述</td></tr><tr><td>Entity Linking</td><td>实体提及</td><td>节点</td><td>匹配查询实体和图节点</td></tr><tr><td>Relational Matching</td><td>关系提及</td><td>边</td><td>匹配查询关系和图的边</td></tr><tr><td>Graph Traversal</td><td>节点/边</td><td>图</td><td>将种子节点/边扩展为子图</td></tr><tr><td>Graph Kernel</td><td>（子）图</td><td>（子）图</td><td>匹配查询图和候选图</td></tr><tr><td>Shallow Embedding</td><td>任意</td><td>任意</td><td>通过嵌入相似性匹配查询和候选者</td></tr><tr><td>Deep Embedding</td><td>任意</td><td>任意</td><td>通过嵌入相似性匹配查询和候选者</td></tr><tr><td>Domain Expertise</td><td>专业规则</td><td>任意</td><td>将领域专业知识与节点/边/图进行匹配</td></tr></table>

## 2.4 Retriever  $\Omega^{\mathrm{Retriever}}$

在获得处理后的查询 $\hat{Q}$ 后，检索器 $\Omega^{\mathrm{Retriever}}$ 从外部图数据源 $G$ 中识别并检索相关内容 $C$，以增强下游任务的执行：$C = \Omega^{\mathrm{Retriever}}(\hat{Q},G)$。

近年来，检索器越来越多地与 `LLMs` 集成，以缓解幻觉、解决隐私问题并增强可解释性和动态适应性。然而，这些主要为文本和图像设计的检索器由于两个核心原因，不能直接应用于 `GraphRAG` 的图结构数据。

首先，`GraphRAG` 的输入/输出格式与传统 `RAG` 存在显著差异。传统 `RAG` 的检索器大多遵循“文本输入，文本输出”的工作流，而 `GraphRAG` 的工作流更为多样，涵盖“文本输入，文本输出”、“文本输入，图输出”、“图输入，文本输出”以及“图输入，图输出”等多种模式。

其次，传统 `RAG` 中的检索器无法捕捉图结构信号。例如，`BM25` 和 `TF-IDF` 等方法主要关注词汇信号，而基于深度学习的检索器通常捕捉语义信号，这两种方法都忽略了关键的图结构信息。因此，本节旨在回顾现有的 `GraphRAG` 检索器，包括基于启发式、基于学习和特定领域的检索器，并重点分析其为适应图结构数据所做的独特技术设计。

## 2.4.1 Heuristic-based Retriever

基于启发式的检索器 (Heuristic-based Retriever) 主要利用预定义规则、领域特定知识和硬编码算法从图数据源中提取相关信息。与深度学习模型相比，它们对固定启发式规则的依赖使其通常在时间与资源上更高效，例如，简单的图遍历方法如 BFS 或 DFS 可以在线性时间内执行，且无需训练数据。然而，这也限制了它们对未知场景的泛化适应能力。以下回顾了在 GraphRAG 中常用的几种基于启发式的检索器。

**Entity Linking**: 在基于启发式的检索器中，`Entity Linking` 负责将查询中识别的实体映射到图数据源中的相应节点。这种映射在查询和图之间建立了初步联系，既可以作为独立的检索器，也可以作为后续图遍历的基础。该方法的有效性依赖于查询处理器准确的实体识别能力以及图节点上实体标签的质量。此技术常用于知识图中，根据与查询的文本相似度（可使用向量嵌入或词汇特征计算）选择 Top-K 节点作为起点。近期，LLMs 也被用作知识增强器，为那些因训练数据有限而导致 `Entity Linking` 模型难以消歧的长尾实体生成以提及为中心的描述，作为额外输入。

**Relational Matching**: `Relational Matching` 与 `Entity Linking` 类似，是一种旨在识别图数据源中与查询指定关系相匹配的边的启发式检索方法。该方法对于识别图中实体间关系的任务至关重要。匹配到的边可以根据图中遇到的实体和关系，指示下一步应探索哪些边，从而指导遍历过程。与 `Entity Linking` 相似，它根据与图中每条边的相似度来选择 Top-K 边。

上述两种启发式方法除了高效和简单外，另一个关键优势是能够克服模糊性。例如，对于机器学习或深度学习模型难以区分的语义或词汇上相似的实体/关系（如 Byte vs. Bit，President of vs. Resident of），这些启发式方法可以基于预定义规则轻松区分它们，即使语义/词汇差异非常细微。

**Graph Traversal**: 在通过 `Entity Linking` 和 `Relational Matching` 识别出图数据源中的初始节点和关系后，`Graph Traversal` 算法（如 BFS、DFS）可以扩展这个集合，以发现更多与查询相关的信息。然而，基于遍历的检索面临的核心挑战是信息过载的风险，因为邻域的指数级扩展通常包含大量不相关内容。为解决此问题，当前的遍历技术集成了自适应检索和过滤过程，有选择地探索最相关的邻近节点，并逐步优化检索内容以减少噪声。这种图遍历主要用于知识图和文档图的 GraphRAG 中。在遍历这两类图时，许多方法提取由 `Entity Linking` 识别的节点之间所有长度小于 $l$ 的路径，而其他方法则考虑初始实体周围的 $l$-hop 子图。为了更高效地遍历知识图 (KG)，一些方法利用 LLM 来剪除不相关的路径，另一些则使用预定义的规则或模板来遍历图。

**Graph Kernel**: 与上述检索节点、边及其组合子图的启发式方法相比，一些早期工作（如在图提取和图像检索中）将文本和图像视为一个完整的图，并使用图级别的启发式方法（如 `Graph Kernel`）来衡量相似性并进行检索。`Graph Kernel` 通过计算图之间的内积来衡量成对相似性，能够同时对齐查询图和被检索图的结构与语义。著名的例子包括 `random-walk kernel` 和 `Weisfeiler Leman kernel`。`random-walk kernel` 通过在两个图上同时进行随机游走并计算匹配路径的数量来衡量相似性。`Weisfeiler Leman kernel` 则通过迭代应用 Weisfeiler Leman 算法，在每次迭代中生成节点标签的颜色分布，然后基于这些直方图向量的内积计算相似性。例如，Wu 等人 [448] 构建了文档和查询的事件图，并使用一种 `product graph kernel` 来衡量查询-文档的相似性并对文档进行排序。

**Domain Expertise**: 传统启发式方法的领域无关性限制了其在需要专业知识领域的有效性。例如，在药物发现中，化学家通常通过参考具有理想特性的现有分子来设计新药，而不是从头构建分子结构。这些分子是基于指导检索具有相似特征结构的领域知识来选择的。遵循这一思路，许多 GraphRAG 系统将领域专业知识融入检索器设计中。例如，Wang 等人 [434] 开发了一个混合检索系统，该系统集成了基于启发式和基于学习的检索方法，以检索部分满足目标设计标准的 exemplar 分子。

## 2.4.2 Learning-based Retriever

基于学习的检索器（Learning-based Retriever）旨在克服基于启发式规则检索器的局限性。启发式方法过度依赖预定义规则，导致其在处理不严格遵守这些规则的数据时泛化能力有限，例如，它们可能因词汇表示不同而无法识别“doctor”和“physician”等实体的深层语义关联。为解决此问题，基于学习的检索器通过机器学习编码器，将查询和数据源中的信息统一压缩成嵌入（embeddings），然后在嵌入空间中进行相似性搜索以获取相关信息，从而捕捉查询与数据对象之间更深层、更抽象且与任务相关的关系。

在传统的RAG中，查询 $q$ 和数据源 $S$ 分别由编码器 $\mathcal{F}_q$ 和 $\mathcal{F}_S$ 映射为嵌入向量 $\mathbf{q}$ 和 $\mathbf{S}$。随后，通过预定义的相似度函数 $\phi$ 在嵌入空间中检索top-k个最相关的实例：
$$
S^{*} = \underset {k}{\arg \max}\phi (\mathbf{q},\mathbf{S}), \tag{2}
$$
与使用语言和视觉编码器的RAG不同，GraphRAG中的编码器能够处理图结构数据，如节点、边和（子）图。这些编码器可分为文本编码器、图编码器以及集成了文本和图的编码器。本文重点关注图编码器，主要分为浅层嵌入方法和深层嵌入方法。

**浅层嵌入方法 (Shallow Embedding Methods)**：
这类方法如Node2Vec和Role2Vec，旨在学习保留图原始结构信息的节点、边或图的嵌入。它们主要分为两类：
1.  **基于邻近度的嵌入 (Proximity-based embeddings)**：如DeepWalk和Node2Vec，确保在图中邻近的节点在嵌入空间中也保持相近。
2.  **基于角色的嵌入 (Role-based embeddings)**：如Role2Vec和GraphWave，根据节点的结构角色而非邻近关系生成嵌入。
在GraphRAG中，基于邻近度的嵌入可用于检索位置相近的实体（如引用相似主题的论文），而基于角色的嵌入则能捕捉功能相似的实体（如根据共享角色或语气检索公司邮件）。

**深层嵌入方法 (Deep Embedding Methods)**：
浅层方法难以利用节点的语义特征（如论文的词袋表示），且缺乏归纳能力（inductivity），每当图中新增节点或边时都需要重新训练，这限制了其在知识图谱等动态演化图谱中的应用。深层嵌入方法通过联合融合特征和图结构来解决这些问题，并具备归纳性。

其中，最具代表性的是Graph Neural Networks (GNNs)，它结合了用于编码结构信号的message-passing机制和用于提取任务相关信息的特征转换。其核心思想如下：
- **节点级图卷积 (Node-level graph convolution)**：如公式(3)所示，每个节点通过加权函数 $\phi_{\Theta_{\phi}}$ 聚合其邻居节点 $\mathcal{N}_i$ 的嵌入，并与自身上一层的嵌入 $\mathbf{x}_i^{l - 1}$ 结合。
- **边级图卷积 (Edge-level graph convolution)**：如公式(4)所示，边的嵌入更新也遵循类似的聚合原则。
- **图级嵌入 (Graph-level embeddings)**：如公式(5)所示，通过对节点和边嵌入进行pooling操作 $\rho \Theta_{\rho}$ 获得。

通过这种基于GNN的嵌入范式，来自不同来源的图知识（节点、边、子图）可以被统一编码为向量表示，如Figure 5(c)所示，我们能为节点 $(\mathbf{X})$、边 $(\mathbf{E})$ 和图 $(\mathbf{G})$ 推导出嵌入。这些子结构嵌入可以进一步组合，以生成更复杂结构的嵌入（例如，知识图谱中一条路径的嵌入）。

最终，这些嵌入可用于训练阶段优化查询对齐，或在测试阶段进行基于相似度的神经搜索。具体应用案例如下：
- **GNN-RAG**：使用GNN为每个查询执行一轮特定的message passing，并将查询嵌入融入消息计算中，最终检索从查询节点到候选节点的最短路径作为上下文。
- **Liu et al. [251]**：采用conditional GNN，仅初始化与查询相关的实体，然后通过回溯从候选节点中提取单条路径。
- **REANO**：将查询信息编码到边特定的注意力权重中，以查询为条件进行聚合，并选择与查询最相似的top-k个三元组作为上下文。

## 2.4.3 Advanced Retrieval Strategies

现实世界中的查询通常很复杂，包含多方面意图和结构化模式，并需要多跳推理能力，而基本的检索器难以应对。例如，回答关于特定大学校歌的问题需要多跳推理来首先定位大学；理解数据集的主题则需要理解其社区结构并聚合各社区的主题。为了处理这些高度复杂的查询，研究者提出了高级检索策略。

**Integrated Retrieval (集成检索)**
该策略通过结合不同类型的检索器来平衡各自的优缺点，以捕获全面的相关信息。集成检索方法通常根据其组合的检索器类型进行分类，其中最著名的例子是 neural-symbolic retrieval 和 multimodal retrieval。

由于图结构数据中存储的知识大多是符号格式，neural-symbolic retrieval 成为 GraphRAG 中集成检索的自然选择。该策略将用于检索符号知识的基于规则的模式与用于检索更抽象和深层知识的基于神经网络的信号相结合。例如，一些研究首先基于符号知识图谱扩展邻居，然后使用神经匹配进行路径检索。相反，另一些研究则先利用 GNNs 检索种子实体（神经检索），然后提取从这些实体出发的最短路径（符号检索）。类似地，还有方法先获取问题中提及实体的 k-hop 邻域作为候选答案（符号检索），然后计算查询与提取出的子图之间的 attention，以区分候选答案的相关性（神经检索）。

**Iterative Retrieval (迭代检索)**
这是一个多步骤过程，其中连续的检索操作之间存在依赖关系，如因果、资源和时间依赖。这些依赖关系在 RAG 中可以通过检索顺序隐式表征，而在 GraphRAG 中则被显式地建模为图结构。因此，迭代检索主要在 GraphRAG 中用于捕获这些依赖。例如，KGP 模型在为问题生成下一个证据和选择最有可能的邻居之间交替进行。ToG 从识别初始实体开始，然后迭代地扩展推理路径，直到收集到足够的信息来回答问题。StructGPT 则预定义了图接口，并提示 LLMs 迭代调用这些接口，直至收集到足够信息。

**Adaptive Retrieval (自适应检索)**
虽然检索到的外部知识有益，但也可能引入风险。如果生成器本身已具备足够的内部知识，外部信息可能变得多余甚至产生冲突。为缓解此问题，RAG 系统中提出了知识检查（knowledge checking）机制，允许系统自适应地评估何时以及需要多少外部信息，从而使 RAG 能够提供更智能、灵活且与上下文感知的响应。

在 GraphRAG 中，一种自适应检索的设计是为不同查询考虑不同的推理深度。过少的图遍历跳数可能会忽略关键的推理关系，而过多的跳数则可能引入不必要的噪声。为解决此问题，有研究通过训练模型来预测给定查询所需的跳数，并据此检索相关的图内容。目前尚无工作专注于解决 GraphRAG 中的知识冲突问题，因此这被视为未来的研究方向。

## 2.5 Organizer

在从外部图数据源检索到相关内容 $C$（其格式可能为实体、关系、三元组、路径或子图）后，Organizer $\Omega^{\mathrm{Organizer}}$ 会结合处理后的查询 $\hat{Q}$ 对这些内容进行处理。其目标是对检索到的内容进行后处理和精炼，使其能更好地被生成器（generator）使用，从而进一步提升下游内容生成的质量。该过程可形式化表示为：
$$
\hat{C} = \Omega^{\mathrm{Organizer}}(\hat{Q},C) \tag{6}
$$
在 GraphRAG 中，对检索内容进行精细化组织和优化的需求主要源于以下几个关键原因。

首先，当检索到的内容是子图时，其节点/边特征和图结构方面知识的异构性，很可能使其包含不相关和嘈杂的信息，这给 LLM 的消化带来了巨大困难，进而损害生成质量。因此，需要采用图剪枝（graph pruning）技术来优化检索到的子图，移除与任务无关的知识。

其次，大量研究表明，LLM 对检索上下文中相关信息的位置存在注意力偏差。在检索的子图中，随着感受野（即跳数）的扩大，邻居节点数量会呈指数级增长，这会急剧增加 prompt 的上下文长度，并稀释 LLM 对任务相关知识的关注。这催生了对基于图的重排序（graph-based reranking）机制的新需求，以优先处理检索图中的最重要内容。

第三，检索到的内容在语义和结构层面可能是不完整的，这使得图增强（graph augmentation）成为必要的强化手段。

最后，检索到的内容通常是图，它不仅拥有语义信息，还具备独特的结构。这种复杂的结构性内容不易被依赖 next-token prediction 和线性化 prompting 训练的 LLM 所消化，因此需要采用感知结构的文本化（structure-aware verbalization）技术对其进行重组。

后续章节将对上述每一种 Organizer 技术进行正式的回顾。

## 2.5.1 Graph Pruning

在 `GraphRAG` 中，检索到的图可能规模庞大，并包含大量噪声和冗余信息。例如，当应用图遍历方法进行检索时，检索子图的大小会随着跳数的增加呈指数级增长。庞大的子图不仅会增加计算成本，还可能因包含噪声信息而降低生成质量。相反，如果跳数过少，检索到的子图可能无法包含任务所需的关键知识。为了在检索子图的大小与其编码的任务相关信息量之间实现更好的权衡，研究者提出了多种 `Graph Pruning` 方法，旨在通过移除不相关的节点和边来缩减子图规模，同时保留核心信息。

- **基于语义的剪枝 (Semantic-based pruning):** 该方法专注于通过移除与查询在语义上不相关的节点和边来缩减图的规模。例如，`QA-GNN` [492] 利用 `LLMs` 对查询上下文和节点标签进行编码，并通过线性投影剪除相关性得分较低的节点。`GraphQA` [389] 则进一步移除与查询相关性最低的节点簇。`KnowledgeNavigator` [133] 根据查询对检索图中的关系进行评分，并剪除不相关的关系以减小图的规模。此外，Gao等人 [118] 将检索到的子图划分为更小的子图，对其进行排序，并仅保留排名最高的 $k$ 个子图用于生成。`G-Retriever` [147] 为每个检索到的节点和边定义一个语义分数，然后通过解决prize-collecting Steiner tree问题来优化图，从而构建一个更紧凑、更相关的子图。

- **基于句法的剪枝 (Syntactic-based pruning):** 该方法从句法角度移除不相关的节点。例如，Su等人 [377] 利用依赖性分析生成上下文的解析树，然后根据检索节点与该解析树的跨度距离（span distance）来过滤节点。

- **基于结构的剪枝 (Structure-based pruning):** 该方法依据图的结构属性对检索到的图进行剪枝。例如，`RoK` [431] 通过计算每条路径的平均 `PageRank` 分数来过滤子图中的推理路径。其他工作，如Jiang等人 [181] 和He等人 [144]，也利用 `PageRank` 来提取最相关的实体。

- **动态剪枝 (Dynamic pruning):** 与上述通常只进行一次剪枝的方法不同，动态剪枝在训练过程中动态地移除噪声节点。例如，`JointLK` [382] 在每一层利用注意力权重递归地移除不相关的节点，仅保留固定比例的节点。类似地，`DHLK` [430] 在学习过程中动态地过滤掉注意力分数低于特定阈值的节点。

## 2.5.2 Reranker

LLMs的性能会受到上下文中相关信息位置（开头、中间或结尾）的影响。此外，LLMs的生成效果也受`in-context`知识提供顺序的影响，后出现的文档通常比先出现的文档贡献更小。尽管在检索过程中，信息通常已按相关性分数排序，但这种排序在大量候选项中往往是粗粒度的（coarse-grained）。因此，在已检索的信息中进行细粒度（fine-grained）的重新排序，即`reranking`过程，对于实现最佳的下游任务性能至关重要。

具体实现上，Li等人[234]使用预训练的`cross-encoder`对检索到的三元组进行重排。Jiang等人[185]和Liu等人[252]则采用预训练的`reranker`模型来重排检索到的路径。Yu等人[498]训练了一个`GNN`来对检索到的段落进行重排。Liao等人[246]根据路径发生的时间顺序进行排序，更加强调近期的路径。

## 2.5.3 Graph Augmentation

Graph augmentation旨在丰富检索到的图，以增强其内容或提高生成器的鲁棒性。该过程通过添加补充信息来扩充检索图，这些信息可源于外部数据或嵌入在LLM中的知识。主要有两类方法：

**Graph Structure Augmentation**：此类方法通过向检索图中添加新的节点和边来增强结构。例如，GraphQA [389]通过整合从上下文中提取的名词短语块节点来增强检索到的子图。Yasunaga等人[492]和Taunk等人[389]将查询本身作为一个节点整合到检索图中，以创建查询与相关信息之间的直接联系。Tang等人[388]则利用预训练的diffusion models来增强图结构。

**Graph Feature Augmentation**：此类方法专注于丰富图中节点和边的特征。由于原始特征可能过长或稀疏，可使用数据增强器来总结特征或为其提供更多细节。例如，Once [258]在推荐系统中使用LLM作为内容摘要器（Content Summarizers）、用户画像器（User Profilers）和个性化内容生成器（Personalized Content Generators）。同样，LLM-Rec [276]和KAR [458]应用各种prompting技术来丰富节点特征，使其对下游任务更具信息量。

此外，一些graph augmentation技术仅关注检索图本身，例如通过随机丢弃节点、边或特征来提升模型的鲁棒性。Ding等人[86]对这些数据增强方法进行了系统性的综述。

## 2.5.4 Verbalizing

Verbalizing是指将检索到的三元组、路径或图谱转换为LLMs能够理解的自然语言。主要存在两种方法：线性Verbalizing和基于模型的Verbalizing。

线性Verbalizing方法通常使用预定义规则将图谱转换为文本，其主要技术包括：
*   **Tuple-based**：这类方法将检索到的不同信息片段放入一个元组中并进行排序 [14, 309]。例如，在对KG进行检索时，许多方法会检索一组事实，其中单个事实在生成提示中被表述为元组 (entity 1, relation 1, entity 2) [308, 395]。对于事实集合，会先按特定顺序排序，然后逐一表述为单个元组，信息之间通常用换行符分隔。此逻辑同样适用于路径和节点等。
*   **Template-based**：这类方法使用预定义模板将路径或图谱转换为更自然的文本。例如，LLaGA [49] 提出了如Hop-Field Overview Template等模板将图谱转换为序列。对于KG，一些方法 [134, 244] 将单个事实转换为自然文本，如Guo等人 [134] 使用模板 "The {relation} of {entity 1} is/are: {entity 2}" 来转换事实 (entity 1, relation, entity 2)。

基于模型的Verbalizing方法通常使用经过`fine-tuning`的模型或LLMs将输入的事实转换为连贯自然的语言，主要分为两类：
*   **Graph-to-text verbalization**：这类方法专注于将检索到的图谱转换为自然语言，同时保留所有信息。例如，Koncel-Kedziorski等人 [211] 和Wang等人 [421] 利用`graph transformers`从`Knowledge Graph`生成文本。Ribeiro等人 [336] 评估了多种预训练语言模型用于图到文本生成任务，而Wu等人 [455] 和Agarwal等人 [3] 则通过`fine-tune` LLMs将图谱转换为句子，确保文本形式能忠实地再现图谱内容。
*   **Graph Summarization**：与保留所有细节的Graph-to-Text Verbalization不同，Graph Summarization旨在根据检索到的图谱和查询生成简洁的摘要。EFSum [208] 提出了两种方法：一种是直接提示LLMs总结检索到的事实和查询，另一种是专门为摘要任务`fine-tune` LLMs。而CoTKR [457] 则在两种操作间交替进行：`Reasoning`（分解问题、生成推理轨迹、识别当前步骤所需知识）和`Summarization`（根据当前推理轨迹从检索到的子图中总结相关知识）。

## 2.6 Generator

`Generator` 的核心目标是根据查询（query）和检索到的信息，为特定任务生成期望的输出。这些任务范围广泛，从判别性任务（如 `node/edge/graph classification`）到生成性任务（如基于 `KG` 的问答），再到图生成（如分子生成）。

由于不同任务具有独特性，通常需要采用不同的 `Generator`。因此，可将 `Generator` 分为三种主要类型：
1.  **基于判别模型的 `Generator` (Discriminative-based Generators)**：利用 `GNNs` 和 `Graph Transformers` 等模型来执行分类等任务。
2.  **基于 `LLM` 的 `Generator` (LLM-based Generators)**：利用 `LLM` 的能力为基于文本的任务生成答案。
3.  **基于图的 `Generator` (Graph-based Generators)**：使用如 `diffusion models` 等生成模型来生成新的图。

## 2.6.1 Discrimination-based Generator

Discrimination-based generator 主要关注判别式任务和回归任务，这些任务通常可以建模为图任务。因此，GNNs 和 Graph Transformers 被广泛用作此类生成器。具体 GNN 的选择取决于图的类型和任务需求。例如，GCN、GraphSAGE 和 GAT 通常应用于 homogeneous graphs；RGCN 和 HAN 等模型用于 heterogeneous graphs；而 HGNN 和 HyperAttention 则适用于超图。此外，Graph Transformers 因其能够捕捉全局依赖关系而受到欢迎。同时，根据任务的具体要求，还会采用不同的训练策略，如（半）监督学习 ((semi-)supervised learning) 和图对比学习 (graph contrastive learning)。

## 2.6.2 LLM-based Generator

LLM在理解和生成自然语言方面表现出卓越能力，但其本质上是为处理序列数据而设计的，而GraphRAG中检索到的信息通常是图结构。尽管像verbalization这样的GraphRAG组织器可以将图信息转换为文本，但这种转换可能导致关键图结构信息的丢失。为了利用LLM的能力，研究者们提出了多种将图信息输入LLM的方法，可分为以下几类：

**Verbalizing**：此方法旨在将GraphRAG中检索到的信息转换为LLM可以处理的序列。

**Embedding-fusion**：该方法在LLM内部融合图嵌入和文本嵌入。图嵌入可由GNNs或Graph Transformers生成。为了对齐图嵌入与文本嵌入，通常需要学习一个`domain projector`，将图嵌入映射到文本嵌入空间。嵌入融合可以发生在LLM的不同层级。例如，He等人[147]将投影后的图嵌入送入LLM的`self-attention`层；Tian等人[395]将投影后的图嵌入前置于文本token之前；而[9]则在LLM的预测层之前融合文本和投影后的图嵌入。此外，在训练策略上，可以采用`LoRA`等方法对LLM和`domain projector`进行`fine-tuning`，也可以保持LLM参数固定，仅训练图嵌入模型和`domain projector`。

**Positional embedding-fusion**：通过Verbalizing直接将图转换为序列可能会丢失图结构信息，而这些信息在某些任务中至关重要。此方法旨在将检索图中节点的位置信息添加到LLM中。例如，统一的图文模型`GIMLET`[549]采用一种广义位置嵌入，将图结构和文本指令编码为统一的token。`LINKGPT`[148]则利用`LPFormer`[361]中的成对编码（pairwise encoding）来编码两个节点间的成对信息。

## 2.6.3 Graph-based Generator

在科学图谱领域，由于需要精确地生成结构，GraphRAG的生成器通常超越了基于LLM的方法。例如，RetMol [433] 是一个通用性很强的框架，它能够兼容多样的encoder和decoder架构，支持包括基于`Transformer`或`Graph VAE`在内的多种生成模型及分子表示方法。Huang等人 [167] 则强调了`diffusion model`的应用，特别是3D分子`diffusion model` `IRDIFF`。在生成过程中，通过采用`Equivariant Graph Neural Networks (EGNNs)` [349] 等架构来实现`SE(3)-equivariance`，这确保了分子结构的几何特性在旋转、平移和反射等空间变换下保持不变。将`SE(3)-equivariance`融入`diffusion model`，保证了所生成分子结构的几何一致性。对于`Knowledge Graph (KG)`，多项研究 [110, 492, 389] 利用`GNN`来生成答案。这些工作中使用的`GNN`以查询为条件，从而确保最终的预测与查询高度相关。

## 2.7 Graph Datasources

对于GraphRAG系统而言，即使其查询处理器、检索器、组织器和生成器等以模型为中心的组件配置最优，若其赖以检索外部知识的底层图数据源未经精心构建，系统性能仍可能无法达到最佳。这也凸显了当前AI研究从以模型为中心（model-centric）向以数据为中心（data-centric）的重大转变，即提升数据质量与相关性对于取得卓越成果同等重要，甚至更为关键。本节从高层次概述了现有GraphRAG研究中图数据源的构建方法。

图的构建方法主要分为两类：
- **显式构建 (Explicit Construction)**：指基于数据中明确、预定义的关系来构建图。此方法应用广泛，例如，根据原子间的连接构建分子图；基于实体间的显式关系形成knowledge graphs；通过引用关系链接论文构建引文图；以及模拟用户与物品交互构建推荐图。
- **隐式构建 (Implicit Construction)**：适用于节点间无明确关系，但可推导出隐式连接的场景。例如，文档中的词语共现可暗示共享的语义信息，表格数据（Tabular data）中的特征交互可表明特征间的相关性。图可以显式地建模这些连接，从而有益于下游任务。

图构建完成后，有多种方式可对其进行形式化表示：
- **邻接矩阵 (Adjacency matrix)**：这是表示图最流行的方式之一。具体而言，邻接矩阵 $\mathbf{A} \in \mathbb{R}^{||\mathcal{V}\times |\mathcal{V}|}$ 表示了节点集合 $\mathcal{V}$ 中节点间的连接关系。
- **边列表 (Edge list)**：该表示法列出图中的每一条边，通常采用元组或三元组形式，如 $(i,j)$ 或 $(i,r,j)$，其中 $i$ 和 $j$ 是节点，$r$ 是它们之间的关系。
- **邻接列表 (Adjacency list)**：这是一种以节点为中心的表示法，每个节点都关联一个其邻居节点的列表，通常表示为字典 $\{i: \mathcal{N}_i\}$，其中 $\mathcal{N}_i$ 是节点 $i$ 的邻居列表。
- **节点序列 (Node Sequence)**：通过可逆或不可逆的方式将图转换为节点序列。大多数序列化方法是不可逆的，无法完全恢复原始图结构。也存在可逆的序列化方法，例如，Zhao等人[552]提出先对图进行欧拉化（Eulerization），再使用欧拉路径（Eulerian paths）序列化图。此外，若图为树结构，通过BFS/DFS也能实现可逆的序列化。
- **自然语言 (Natural language)**：随着LLM在处理文本信息方面日益普及，已发展出多种使用自然语言描述图的方法。

需要注意的是，上述数据结构主要用于表示基础图，对于多关系边或边属性等复杂场景支持不足。例如，使用邻接矩阵表示一个多关系属性图需要一个扩展结构：$\mathbf{A} \in \mathbb{R}^{|\mathcal{V}| \times |\mathcal{V}| \times |\mathcal{R}|}$，其中 $\mathcal{R}$ 表示所有可能的关系集合，$\mathbf{A}_{i,j,r}$ 代表节点 $i$ 和节点 $j$ 在关系 $r$ 下的边权重。

选择合适的图表示方法对特定任务至关重要。例如，Ge等人[122]的研究发现，图描述的顺序会显著影响LLM对图结构的理解及其在不同任务上的表现。

## 3 Knowledge Graph

一个 `Knowledge Graph` 是一个结构化的数据库，通过明确定义的关系连接实体。它既可以涵盖广泛的通用知识，如广为人知的 Google Knowledge Graph [53, 261]，也可以深入特定的专业领域，如用于生物医学推理的 BioASQ 数据集 [400]。`Knowledge Graph` 中包含的实体、关系、路径和子图等多样化信息，可作为宝贵资源，用于增强不同领域的各种下游任务，例如问答 [395, 428, 493]、常识推理 [169]、事实核查 [201]、推荐系统 [131]、药物发现 [28]、医疗保健 [37] 以及欺诈检测 [287]。

## 3.1 Application Tasks

本节回顾了GraphRAG在Knowledge Graphs (KGs)上的代表性应用。

- **问答 (Question-answering):** 问答任务旨在回答特定领域或跨全局知识的用户文本查询。在这些场景中，GraphRAG利用knowledge graphs检索相关信息，为large language model (LLM)生成准确答案（形式可以是句子、文本片段或多项选择）提供必要的上下文或支持性事实。

- **事实核查 (Fact-Checking):** 该任务通过与可靠信息源进行交叉引用来验证陈述的真实性。GraphRAG通过查询knowledge graph来检索支持或反驳给定主张的相关事实和关系结构，从而增强此任务。通过将陈述映射到knowledge graph上，GraphRAG能够识别数据中的差异或确认点，提供一个彻底且基于证据的验证过程。

- **知识图谱补全 (Knowledge Graph Completion):** 此任务旨在预测新事实以增强图谱的完整性并推断缺失信息。GraphRAG通过检索三元组周围的结构化知识来进行推理，为LLM的推理过程提供必要的结构性知识，从而增强其性能。

- **网络安全分析与防御 (Cybersecurity Analysis and Defense):** 该领域旨在分析并应对漏洞、弱点、攻击模式和威胁策略。面对日益复杂和庞大的网络安全数据，研究人员提出使用GraphRAG，以便为网络安全分析提供关于潜在攻击向量和缓解策略的更全面见解。

## 3.2 Knowledge Graph Construction

本节探讨了Knowledge Graph (KG) 的典型构建方法，并指出构建方式会影响其在下游任务中的功用。主要技术如下：

*   **手动构建 (Manual construction):** 此方法依赖人工标注。例如，WikiData [404] 利用众包力量收集知识，每个实体对应一个维基百科页面。Unified Medical Language System (UMLS) [25] 则是一个包含从多源收集的生物医学事实的KG。

*   **基于规则的构建 (Rule-based construction):** 传统方法常使用基于规则的技术，通过定制的解析器和手动定义的规则从原始文本中提取事实，这些解析器可能因文本来源而异。著名案例包括：ConceptNet [373]，通过断言连接不同词语；Freebase [27]，包含广泛的通用事实。REANO [106] 则利用传统的实体识别 (ER) 和关系提取 (RE) 方法（如用于ER的SpCy [151]和用于RE的TAGME [112]）来提取实体与关系，并使用DocuNet [526] 提取连接两个实体的具体事实。

*   **基于LLM的构建 (LLM-based construction):** 近期研究探索了利用LLM从文档中自动构建KG。LLM可以自动提取实体和关系，并将其链接成事实。值得注意的是，这类方法通常没有ground-truth KG作参考，而是将KG作为组织和表示文档集的方式。例如，CuriousLLM [487] 将文本段落视为实体，根据编码后的文本相似度建立连接。Cheng et al. [58] 使用手动定义的prompt将文本转换为KG。Graph-RAG [98] 先将文档分块，用LLM检测每块中的实体及其属性，再用LLM识别实体间的关系，最后再次调用LLM总结实体和关系内容以生成最终标题。AutoKG [40] 则结合LLM embeddings和聚类技术来构建KG。

## 3.3 Retriever

知识图谱（Knowledge Graphs, KGs）中的事实能够为生成模型提供可靠信息，增强其输出的可靠性。鉴于KGs的结构化特性，它们天然适合用于检索。检索的目标是针对给定的问题或查询，检索出有助于回答该问题的相关事实或实体。检索过程需考虑多个因素，包括检索事实的类型、效率以及检索事实的数量。通常，KGs的检索分为两个阶段：识别种子实体和检索事实或实体。

**识别种子实体**
为给定查询检索相关事实的第一步是识别一组“种子实体”（seed entities）。这些是与原始查询高度相关的初始实体，包含这些实体或在图谱中邻近它们的三元组被认为能提供有用的上下文。识别种子实体的方法多样：
*   一些研究[181, 200, 251, 380, 522]假设种子实体是给定的。
*   大多数研究[110, 381, 443, 530, 308, 493]则尝试从查询中提取实体。一种方法是使用专门的实体提取技术。
*   另一种常见方法是提取与原始查询语义相似的实体集[443, 347]。
*   更复杂的方法利用大型语言模型（LLM）。HyKGE[185]首先生成一个假设，然后从原始查询和假设中提取实体。Guo等人[134]利用LLM生成两个相似问题，并从所有问题中提取实体以减少幻觉。Rok[431]则使用思维链（chain of thoughts）推理来扩展原始查询，并从中提取种子实体。

**检索方法**
在获得与查询相关的种子实体集后，利用这些实体来检索有助于回答查询的事实或实体。核心检索方法总结如下：

*   **基于遍历的检索器 (Traversal-based retriever)**: 这类方法通过遍历图谱来提取路径。
*   Yasunaga等人[492, 493]和Zhang等人[530]提取种子实体之间长度最多为2的所有路径，并保留通过相关性评分模型筛选出的top-k个实体。
*   一些方法使用beam-search[381]或提取固定长度（如k≤2）的路径[185, 110]。LARK[62]则检索从种子实体出发、长度≤k的路径上的所有事实。
*   OREQLM[158]从种子实体出发遍历k跳，并使用可学习的嵌入来衡量路径中关系和实体的重要性。
*   可训练的检索器也被提出，例如Zhang等人[522]训练一个模型来为新访问的边评分并进行剪枝。KG-RAG[347]同样对边进行评分，并使用LLM决定下一步探索的路径。RoG[271]通过指令微调（instruction tuning）使LLM生成有用的关系路径。KnowledgeNavigator[134]首先预测所需的遍历跳数，然后使用LLM在遍历过程中对节点进行评分和剪枝。
*   Rok[431]使用Personalized PageRank (PPR)评分来识别有用路径。PullNet[380]假设每个实体关联一组文档，在遍历过程中同时提取事实和文档中包含的实体。KG-R3[312]使用强化学习方法MINERVA[75]来挖掘实体间的重要路径。Wang等人[428]则利用LLM在遍历的每一步中决策下一个要访问的节点。

*   **基于子图的检索器 (Subgraph-based retriever)**: 这类方法围绕每个种子实体提取一个大小为k的子图。
*   多项研究[308, 395, 181, 205]提取每个种子实体周围的一跳或两跳子图，并将它们合并。
*   Gao等人[118]先提取一个包含种子实体和潜在答案的子图，然后将其分区并对小块子图进行排序，保留top-k个。
*   MVP-Tuning[164]针对问答选择题，优先考虑包含最多种子实体和选项实体的三元组，并利用BM25[338]找到相似问题来扩充三元组。

*   **基于规则的检索器 (Rule-based retriever)**: 这类方法使用预定义的规则或模板来提取路径。
*   GenTKG[246]在时序KG上首先提取逻辑规则，然后用top-k规则在给定时间间隔内为种子实体提取路径。
*   一些工作[72, 270]使用SPARQL生成查询来检索路径。
*   KEQING[406]使用经过LoRA[153]微调的LLM将原始查询分解为子查询，为每个子查询匹配预定义的模板和逻辑链，从而从KG中提取路径。

*   **基于GNN的检索器 (GNN-based retriever)**:
*   GNN-RAG[289]为检索任务训练一个GNN。GNN将查询信息融入消息传递（Message Passing）过程，并像节点分类任务一样进行训练，正确答案实体的标签为1。
*   Liu等人[251]使用一个条件GNN（conditional GNN），其中只有种子实体被初始化为非零表示。在多轮消息传递中，每层只保留top-K的新边，最终通过回溯注意力权重最高的边来构建证据链。
*   REANO[106]使用T5编码的文本均值池化表示来初始化实体和关系，然后运行一个GNN，其注意力机制考虑了三元组与原始问题的相关性，最后检索与问题最相关的top-K三元组。

*   **基于相似度的检索器 (Similarity-based retriever)**:
*   STaRK[452]计算查询与每个实体的向量相似度，其中实体嵌入融合了文本和关系信息，并考虑了多向量表示。
*   REALM[567]和EMERGE[566]都提取与查询最相似的实体，但EMERGE会进一步检索这些实体周围的1跳子图。

*   **基于关系的检索器 (Relation-based retriever)**:
*   Kim等人[200]的框架首先使用LLM将查询分割为子句，再为每个子句预测top-k个最相关的关系，然后检索包含这些关系和相关实体的三元组。
*   GenTKGQA[119]专注于时序KG问答，同样先检索top-k关系，再检索满足时间约束的相关事实。

*   **基于融合的检索器 (Fusion-based retriever)**: 这类方法结合了多种检索技术。
*   Mindmap[443]结合了路径提取和种子实体的1跳子图提取。DALK[224]在此基础上使用LLM对检索到的事实进行排序，以去除冗余信息。
*   UniOQA[244]并行使用两个分支：一个生成CQL格式答案的翻译器（fine-tuned LLM）和一个检索1跳子图的搜索器。
*   KG-Rank[483]综合考虑关系与查询的相似度、三元组与LLM输出的相似度以及MMR排序[35]来对种子实体1跳邻域内的三元组进行排序。
*   GrapeQA[389]在路径检索的基础上，增加了路径实体共同邻居的“额外节点”，并引入聚类方法进行剪枝。
*   SubgraphRAG[232]结合了GNN和文本信息，使用MLP综合GNN输出的节点表示和文本表示来为三元组评分。

*   **基于Agent的检索器 (Agent-based retriever)**: 这类方法使用LLM Agent从KG中检索事实。
*   KnowledGPT[425]定义了一套KG搜索工具，并生成代码来执行检索。
*   KG-Agent[182]微调LLM以生成SQL代码进行检索。
*   KnowAgent[568]首先通过规划模块识别相关动作，然后利用这些动作生成用于生成的路径。

*   **其他检索器**:
*   KICGPT[439]专注于知识图谱补全任务，它使用传统的KG嵌入评分函数（如RotatE[383]）对所有可能的实体进行评分，并检索得分最高的top-k个实体，同时辅以包含相同关系或头实体的其他三元组作为补充知识。

## 3.4 Organizer

本小节描述了如何组织检索到的知识以供生成模型使用，即信息如何被格式化并提供给生成器。并非所有方法都包含一个明确的Organizer。以下是常见方法的总结：

*   **Tuple-based organizer (基于元组的组织器)**：这类方法将每条检索到的信息视为一个有序元组。例如，在生成提示中包含一个三元组 `(entity 1, relation 1, entity 2)`。类似地，长度为 $m$ 的路径表示为 `(entity 1, relation 1, entity 2, relation 2, ..., entity m)`。实体和关系通常用其名称或ID表示，每个三元组或路径通常单独成行。许多研究将检索到的路径作为额外上下文附加到原始查询后。其他检索事实（而非路径）的研究也采用类似方式，附加三元组。一些方法仅将检索到的实体作为上下文。KG-R3 [312] 首先列出所有实体，然后列出所有关系。Delile et al. [78] 考虑的KG中，每个实体关联一个文本块，每个文本块都被视为要包含在上下文中的一条信息。一些研究将每个实体和关系表示为一个结合了LLM和GNN的embedding。Liu et al. [231] 进一步包含了由GNN模型给出的每条路径包含正确答案的概率。MVP-Tuning [164] 考虑合并共享相同主语和关系的多个事实以消除冗余信息，表示为 `subject relation {object 1, ..., object k}`。KG-Agent [182] 将当前的KG信息和历史推理程序存储在列表中。

*   **Text organizer (基于文本的组织器)**：这类方法将检索到的结构化知识“文本化”。Wu et al. [456] 将每个三元组传递给LLM，并提示其转换为文本表示，从而文本化检索到的子图。MindMap [443] 对子图采用类似流程。一些方法使用预定义模板来文本化三元组或路径。Wang et al. [406] 的实验发现，基于LLM的文本化对ChatGPT效果更好，而基于模板的文本化对LLaMA效果更佳。KICGPT [439] 结合数据预处理和LLM提示将三元组转换为文本。STaRK [452] 使用LLM综合每个实体的关系和文本信息，并使用依赖于特定任务的预定义模板。CoTKR [457] 通过一个“knowledge rewriter”使用LLM来总结并重写与问题相关的子图事实。该重写器通过preference alignment进行训练，即从生成的 $k$ 个子图表示中，由ChatGPT选出最优和最差的表示作为偏好优化的目标。

*   **Other organizer (其他组织器)**：存在一些不属于上述分类的例外。KnowledgeGPT [425] 以Python类的格式表示信息，并尝试包含实体描述和实体-方面信息等额外内容。

*   **Re-Ranking (重排序)**：一些方法还会对信息进行特定顺序的重排序，因为信息的顺序会对LLM的性能产生细微影响。
*   Delile et al. [78] 根据影响力（父论文引用数）和新近度对实体文本块进行排序。
*   Dai et al. [72] 按三元组与查询的相关性得分排序。
*   Choudhary and Reddy [62] 尝试按逻辑顺序排列路径，使后继路径建立在前一路径之上。
*   Yang et al. [483] 使用一个任务特定的Cross-Encoder [187] 对检索到的三元组进行重排序。
*   STaRK [452] 考虑使用LLM对检索到的实体进行重排序，LLM根据每个实体的关系和文本信息给出一个0到1的分数用于排序。
*   GenTKG [246] 按事件发生的时间顺序排列路径。
*   KICGPT [439] 首先使用KG embedding的分数函数对所有实体进行排序并保留top-k，然后利用`In-context Learning`进行重排序，即向LLM提供示例作为先验知识，以辅助其如何重排实体。

## 3.5 Generator

本节描述了如何利用检索和组织后的数据来生成对查询的最终响应，并根据生成响应所用方法的类型对这些生成器进行分类。

- **基于LLM的生成器**: 绝大多数研究使用LLM来生成响应。LLM的输入是原始查询以及通过特定模板格式化后的检索与组织化上下文。最常用的LLM包括ChatGPT、Gemini、Mistral和Gemma等。对于权重公开的开源模型，有时会采用`fine-tuning`技术来针对特定任务修改模型权重，这一过程常通过`LoRA`以实现高效`fine-tuning`。

- **基于GNN的生成器**: 一些方法使用图神经网络（`GNNs`）来执行生成任务。这些方法会根据查询条件，为每个潜在答案（即实体）提取语言`embedding`和`GNN` `embedding`。然后，基于这两种`embedding`的融合来学习单个实体作为正确答案的概率。

- **其他生成器**: 其他方法也多种多样。一些研究将预测任务构建为一个遮蔽语言模型（`MLM`）问题，其目标是预测出能回答查询的被遮蔽词元（即正确实体），通常通过`fine-tune` `RoBERTa`语言模型来实现。`KG-R3`通过计算查询与每个独立实体表示之间的`cross-attention`来为潜在答案实体评分。`PullNet`使用`GraftNet`来为不同实体打分。另一项工作首先通过计算查询与子图表示之间的余弦相似度来选择正确的子图，然后将相似度最高的子图送入`GraftNet`以选出最可能的实体。`REANO`则将编码后的三元组及其关联的文本段落传递给`T5`解码器，并将任务框架化为一个分类问题，旨在为包含正确答案的三元组分配最高概率。

## 3.6 Resources and Tools

### 3.6 资源与工具

本节主要梳理并列举了在图 RAG (Retrieval-Augmented Generation) 系统中常用的工具与 Knowledge Graphs (KGs)。针对所列的每一项资源，文中均提供了其简要描述和对应的项目链接。

## 3.6.1 Data Resources

本节介绍了三种常用于图学习的数据资源：
- **Freebase [27]**：一个百科全书式的KG (Knowledge Graph)，包含大量通用和基础性事实。
- **ConceptNet [373]**：一个语义图，其图中的链接用于描述不同词语或概念的含义。
- **WikiData [404]**：一个众包知识库，其功能相当于维基百科（Wikipedia）的结构化对应物。

## 3.6.2 Tools

*   **Graph RAG** [98]：作为 `Graph RAG` [98] 框架的官方开源实现，该工具可通过 `graphfrag` python包进行安装。
*   **LangChain**：一个开源框架，旨在将 `LLMs` 与各类组件和应用（包括 `RAG`）结合使用，并为在 `KGs` 上应用 `RAG` 提供支持。

## 4 Document Graph

文档图（Document Graph）通常用于建模不同文档之间或文档内部不同粒度内容之间的连接。这种结构在现实世界中广泛存在，例如连接不同网站的超链接以及关联学术论文的引文。此外，文档图内部的句子和实体关系能够显式地捕捉语义和句法层面的上下文信息。

该章节的核心观点是，文档中蕴含的结构化信息可作为GraphRAG的宝贵资源，能够有效辅助LLMs完成各种任务。其主要方法和应用体现在RAG的检索过程中。例如，在多跳问答（multi-hop question answering）等复杂场景下，包含最终答案的文档可能与原始问题之间缺乏直接或明显的关联。然而，通过利用文档图，我们可以追踪这些文档与其他上下文与问题高度相关的文档之间的连接，从而识别并定位到这些关键的相关文档。本章节将对文档图进行系统性的回顾。

## 4.1 Application Tasks

文档图（Document graphs）在一系列广泛的任务中都具有重要价值。本节回顾了文档图能够发挥关键作用的应用任务。尽管文档图尚未与大语言模型（LLMs）完全集成，但它们在增强LLM于各类应用中的能力方面展现出巨大潜力。

- **多文档摘要（Multi-document Summarization, MDS）**: MDS旨在将多个文档的内容浓缩成一个连贯的摘要。由于语料库通常包含大量文本，常超出LLM的上下文窗口限制，文档图通过提取关键组成部分及其关系来压缩语料库，这对MDS任务极具价值。此外，通过在图上进行层次化聚类（hierarchical clustering），可以实现不同粒度的摘要生成。

- **文本生成（Text generation）**: 该任务专注于生成连贯且有意义的文本。虽然基于文本的RAG模型已广泛用于生成更可靠的文本，但文档图能够利用图拓扑结构来检索相似文档，从而进一步增强这一过程。例如，在撰写论文摘要时，访问其引用的相关文献（这些文献在图中相互连接）可以显著提高写作效率，因为这些参考文献通常包含相关的知识和背景。

- **文档检索（Document Retrieval）**: 作为信息检索（IR）的核心任务，文档检索旨在根据查询找到相关的文档列表。查询词可能不会直接出现在目标文档中，但通过利用文档间的连接，可以检索到与查询强相关的文档所连接的其他相关文档。因此，在检索过程中考虑文档级别的关系至关重要。已有研究利用不同粒度的文档图来改进文档检索和排序。除了检索整个文档，图结构也可用于检索特定的文本片段（chunks）。

- **文档分类（Document Classification）**: 这是自然语言处理中的一项基础任务。传统方法常关注词语的局部性，限制了其捕捉长距离和非连续词语交互的能力，并且通常忽略了文档间的关系。然而，相互连接的文档常表现出同质性（homophily），即它们更可能共享相似的标签。构建文档图可以通过利用单个文档内词语的局部与全局关系，以及利用文档间的关系来增强分类性能。

- **问答（Question Answering）**: 问答是RAG的一项基础任务，旨在根据文档信息回答问题。用于问答的文档可能很长，传统方法常忽略对长距离理解至关重要的全局结构。此外，一些多跳（multi-hop）问题需要跨多个文档进行推理，这必须利用文档级别的关系。依据认知负荷理论（cognitive load theory），人类倾向于将分散信息整合成结构化知识以简化推理过程。基于图的方法非常适合此任务，它们通过构建词级别的文档图、利用文档级别的关系以及借助层次化交互来解决这些挑战。

- **关系抽取（Relation Extraction）**: 该任务旨在从文本中提取实体间的语义关系，这通常需要捕捉局部、全局、句法和语义依赖，尤其是在文档级关系抽取中。事实证明，图结构能够更有效地捕捉这些复杂的依赖关系，因此对文档级关系抽取非常有帮助。

除了上述任务，图结构在其他领域也被证明是有益的，例如虚假新闻检测（fake news detection）、连贯性评估（coherence assessment）和机器翻译（machine translation）。

## 4.2 Document Graph Construction

### 4.2 文档图构建

不同任务可能需要不同类型的文档图，例如文档级、句子级或词语级的图。因此，获取文档图的方法至关重要。构建文档图主要有两种方法：显式构建和隐式构建。

*   **显式构建 (Explicit Construction)**：在现实场景中，许多文档之间存在明确的连接。例如，通过超链接连接的网页、相互引用的学术论文，以及通过转发、评论和互动连接的社交媒体帖子。在这些情况下，利用这些连接来构建文档图是很自然的，因为相互连接的文档通常共享语义关系。例如，有研究基于维基百科文章间的超链接构建了Wikipedia图。其他研究也采用相同方式利用超链接构建图。还有研究利用外部`Knowledge Graph` (KG) 构建图，其中每个节点代表一个映射到KG中实体的检索段落，如果两个段落节点映射的实体在KG中有关联，则它们之间建立连接。这些连接已被用于预训练大语言模型 (LLMs)，以提升其在各种任务上的性能。

*   **隐式构建 (Implicit Construction)**：尽管文档间存在显式连接，但文档内部的不同组成部分也表现出重要的语义和句法关系。这些组件的结构对于自然语言处理中的多种任务非常有益。例如，可以利用`Abstract Meaning Representation` (AMR) 等语义解析图来增强信息提取和文本摘要。此外，句法分析树被用来理解语法结构和解决歧义。

文档图的隐式构建方法高度多样化，以适应不同任务的具体需求。例如，文档图中的节点可以代表不同粒度，如词语、实体、句子、文本段、段落、文档或主题。此外，文档图通常表现出异构性（`heterogeneity`），其中边连接不同类型的节点。接下来，我们将详细介绍不同类型边的构建方法：

*   **词-词边 (Word-word edge)**：连接具有语义或句法关系/依赖的词语。建立这些连接的方法多种多样，包括在滑动窗口内的词语共现、由NLP解析工具生成的依赖解析图、`Abstract Meaning Representation` (AMR) 和基于不同表示的语义图。其他技术包括`coreference resolution`、`word embedding`相似度以及使用大语言模型 (LLMs) 提取词语间关系。对于实体而言，构建过程与词语类似，但通常需要先使用实体提取方法识别实体。

*   **词-句边 (Word-Sentence edge)**：主要基于归属关系连接词语和句子。通过将词语链接到它们所在的句子来构建这些边，边的权重通常使用`term frequency-inverse document frequency` (TF-IDF) 来衡量。此外，有研究通过现成的实体链接器，利用超链接将实体与段落标题连接起来。

*   **句-句边 (Sentence-Sentence edge)**：基于语义相似性或关系连接句子。例如，可以通过句子间的交互、`TF-IDF`表示的相似性、`BM25`、`sentence embeddings`、词性（PoS）特征和N-Gram特征来构建这些边。此外，有研究使用AllenNLP-SRL模型构建`Semantic Role Labeling` (SRL) 图。这使得连接长文档内部或跨不同文档的句子成为可能，对于上下文长度有限的LLMs尤其有用。

*   **句-文档边 (Sentence-document edge)**：通过将句子链接到它们所属的特定文档来构建。

*   **文档-文档边 (Document-document edge)**：基于文档间的相似性连接文档。当一个文档中的实体被另一个文档引用或共享时，或者通过文档聚类、`embedding`相似性、主题相似性或结构相似性，可以构建这些边。

文档图通常表现出`heterogeneity`，由多种类型的边构成。此外，一些研究提出了分层图（hierarchical graphs），用以捕捉不同层次的抽象。图结构也可以是动态的，或在学习过程中进行更新。而且，文档图中的节点也可以是LLMs的响应。例如，GoR模型为进行长文本摘要，将LLMs的历史响应与文档的响应块连接起来。

## 4.3 Retriever

文档图的 retriever 通常遵循通用的 retriever 设计，但也存在一些针对图结构的特殊检索方法，具体如下：

-   **Pre-Retrieval**：在许多场景中，为海量文档构建精细图谱的开销巨大且效率低下。Pre-retrieval 方法旨在解决此问题，其核心思想是先根据查询检索相关的文档或文本片段，然后仅基于这些检索出的信息构建图。例如，Thayaparan等人[392]利用预训练的GloVe向量先提取相关句子，再基于这些句子构建图。Zheng和Kordjamshidi [556]以及Yu等人[498]也采用了类似的方法。

-   **基于图相似性的Retriever (Graph similarity-based retriever)**：当查询本身和检索数据源都是图结构时，此方法通过计算图与图之间的相似性来检索相关信息。例如，研究[544]利用General Maximum Common Subgraph (GMCS)方法来检索相似的图。

-   **Iterative Retriever**：在某些任务中（如multi-step question answering），包含最终答案的节点可能与初始查询并不直接相似。Iterative retriever通过一个多步过程解决该问题：首先检索与查询直接相关的初始节点，然后利用已检索到的信息作为新的上下文，迭代地检索后续节点。例如，Wang等人[428]和Zhang等人[541]将迭代检索用于多步问答任务；Ma等人[278]基于已有的knowledge graph进行迭代式文档检索。Asai等人[172]则训练了一个Recurrent Neural Network (RNN)，并结合Bayesian Personalized Ranking (BRR)损失函数来循环地检索相关信息。

-   **基于拓扑的Retriever (Topology-based Retriever)**：此方法利用图中的各种拓扑关系来衡量不同类型的相似性，并将其用于检索。例如，基于邻近性的拓扑相似性（proximity-based topological similarity）衡量两个节点间的结构距离，而基于角色的拓扑相似性（role-based topological similarity）则评估节点在图中所扮演角色的相似度。这些拓扑相似性均可被整合到检索流程中[429]。

## 4.4 Organizer

本节描述了用于文档图的Organizer。在文档图上的GraphRAG研究尚处于早期阶段，许多工作并未集成显式的Organizer。现有方法总结如下：

-   **Graph Pruning**：该方法通过精简检索到的子图来减少无关信息并提升计算效率。例如，Hemmati和Ghassem-Sani [149] 根据局部聚类系数进行图剪枝；Zhang等人 [539] 采用以路径为中心的剪枝方法（path-centric pruning）来整合路径外的信息；Li等人 [229] 在解码（decoding）过程中动态丢弃不相关的节点；Angelova和Weikum [8] 基于相似度阈值对边进行剪枝。此外，Edge等人 [98] 利用社区发现算法创建不同的社区，再将这些社区输入到生成器中。

-   **Reranking**：Reranking方法旨在对检索到的信息进行重新排序，以辅助生成过程。例如，Yu等人 [498]、Zhang等人 [541] 和Dong等人 [90] 使用GNNs对检索到的段落进行重排序。Li等人 [239] 则对通过图结构扩展的段落执行列表式重排序（listwise reranking）。

## 4.5 Generator

本节总结了用于文档图的常用生成器（Generator）。根据输入格式的不同，文档图中会应用多种方法。一些方法将整个图作为输入，此时通常采用 GNNs 和 Graph Transformers。另一些方法将单个句子作为输入，适用于 RNNs 或（大）语言模型。此外，还有一些工作同时利用图和文本作为输入，需要能够有效处理多模态数据的集成方法。

- **基于 GNN 的生成器**：大量研究将任务建模为图相关问题，并利用 GNNs 作为生成器。传统的 GNNs，如 GCN、GraphSAGE 和 GAT，在多项研究中被广泛采用。当图中包含边关系时，通常使用 Relational Graph Convolutional Networks (R-GCNs) 来有效捕捉这些关系。此外，一些工作还结合了图对比学习（graph contrastive learning）技术以提升性能。

- **基于 Graph Transformer 的生成器**：Graph Transformers 能够捕捉整个图的全局信息，被用于为各种任务编码图结构。这些模型利用 Transformer 的自注意力机制来捕捉超越局部邻域的依赖关系，因此非常适合需要全局上下文的任务。

- **基于 RNN 的生成器**：Recurrent Neural Networks (RNNs)，如 LSTMs，是处理序列的常用模型。因此，当输入为文本形式时，会采用 RNNs。

- **基于 LLM 的生成器**：基于 LLM 的生成器通常先将检索到的子图转换为文本，然后使用大语言模型（LLMs）进行生成。该方法中使用了多种模型，例如，BERT 被应用于支持生成任务；一些研究利用 T5 模型；还有研究使用 RoBERTa。

- **集成生成器 (Integrated Generator)**：一些工作同时利用图和文本数据进行生成，使用集成了图模型和文本生成模型的生成器。例如，有研究采用了 RoBERTa 和 GCN 的组合，也有研究将 GNN 与 T5 相融合，以充分利用图结构和语言模型各自的优势。

除了上述生成器，还有一些方法将图直接嵌入到文本生成模型中。例如，有研究提出用图信息自注意力（graph-informed self-attention）取代 Transformer 中传统的自注意力层，使模型能够将图结构直接整合到生成过程中。

## 4.6 Resources and Tools

本章节介绍了专为文档GraphRAG设计或常用的资源与工具。由于文档GraphRAG的数据源可以是任何类型的文档，本节不提供详尽的数据列表，而是重点介绍用于处理文档图的特定工具。

-   **基础自然语言处理与信息抽取工具**：这类工具对于从文本构建文档图至关重要。
-   **CoreNLP**: Stanford CoreNLP是一个全面的自然语言处理工具包，提供分词、句法分析、命名实体识别、共指消解等功能，这些对于构建文档图非常有价值。
-   **spaCy**: 这是一个以速度和神经网络模型闻名的高级NLP库，为词性标注、依存句法分析、命名实体识别和句子分割等任务进行了优化。
-   **BLINK**: 这是一个`entity linking` Python库，它使用维基百科作为目标知识库。
-   **OpenIE**: Open Information Extraction工具用于从文本中提取结构化信息，尤其擅长从非结构化文本中生成三元组，这些三元组可直接用作文档图中的节点和边。
-   **CogComp NLP**: 由Cognitive Computation Group开发的工具套件，包含命名实体识别、情感分析和共指消解等NLP功能。

-   **核心GraphRAG框架与LLM应用开发工具**：这类工具提供了从图构建到RAG应用的端到端解决方案。
-   **GraphRAG [98]14**: 这是一个核心的数据管道和转换套件，旨在利用LLMs从非结构化文本中提取有意义的结构化数据。其核心流程包括：从原始文本中提取`knowledge graph`，构建社区层级结构，为这些社区生成摘要，并最终在执行基于RAG的任务时利用这些图结构。
-   **LangChain**: 这是一个用于开发LLM驱动应用的框架。其突出特点是支持`Graph Transformers`，能够将文档转换为图结构化格式，因此非常适合处理文档图。
-   **LlamaIndex [253]17**: 这是一个为LLM应用开发设计的数据框架，能将多种数据源与LLM无缝集成。其关键特性是包含一个`Property Graph Index`，该索引有助于图的构建、建模、存储和查询，从而为LLM提供富含上下文的知识增强输出。
-   **Haystack**: 这是一个用于构建由LLMs、`Transformer`模型和向量搜索驱动的应用的端到端框架。它支持RAG等多种用例，并能将`Neo4j`作为`DocumentStore`，使其能够胜任文档图的存储和查询操作。

-   **图数据库平台**：
-   **Neo4j**: 作为一个图数据库平台，`Neo4j`提供图数据的存储、可视化、管理和查询的全面工具。它包含一个`LLM Graph Builder`，可以使用LLMs提取图结构，并提供了`GraphRAG`的演示，展示了如何用`Neo4j`实现LLMs和RAG系统。

## 5 Scientific Graph

Scientific Graph 指的是在药物发现和生物医学等领域中使用的图结构化数据，这些领域也是 GraphRAG 的常见应用场景。本章节中，Scientific Graph 特指分子图和医学图。

近年来，科学人工智能取得了显著进展，机器学习（ML）和深度神经网络技术正越来越多地从实验数据中驱动科学发现。值得注意的是，像 Large Language Models (LLMs) 这样的生成模型在处理 Scientific Graph 数据（包括分子图和生物医学图）方面取得了巨大成功。以分子图为例，原子作为节点，化学键作为边，以此捕捉分子结构。AI 技术能够处理这些图上的预测和生成任务，从而推动药物发现等领域的发展。

尽管 LLMs 等生成模型能力强大，但在科学领域的应用仍面临若干挑战，其中最突出的是缺乏领域专业知识。在药物发现等领域，分子生成至关重要，但传统生成模型常难以生成正确或科学上有效的结构。在医学问答（QA）任务中，则经常遇到答案错误、幻觉和可解释性有限等问题。为应对这些挑战，近期研究提出利用外部知识库，通过 GraphRAG 来增强生成过程。GraphRAG 通过从大型数据库中检索相关的 Scientific Graph 来指导生成或回答过程，从而提高准确性。该方法通过引入已知的有效图结构来确保科学有效性，利用现有知识进行实际应用，并通过缩小搜索空间来加速生成过程。

## 5.1 Application Tasks

科学图谱在一系列广泛的任务中都具有重要价值。本节回顾了科学图谱能够发挥关键作用的几个代表性应用任务。

- **分子生成 (Molecule generation):** 该任务指利用生成模型创建或设计新分子结构的过程，在药物发现等领域至关重要。应用科学图谱，特别是分子图，能够提升所生成分子结构的合理性与准确性。其典型方法是，给定一个查询分子，检索出最相关的分子结构，以指导生成过程。

- **分子属性预测 (Molecule property prediction):** 该任务指利用计算方法，根据分子结构来预测其物理、化学或生物属性。它已被证明能有效加速药物发现过程，同时显著降低相关成本。应用科学图谱，尤其是分子图，可以提高预测的准确性。为实现这一目标，通常会提供一个查询分子，并识别出相似的分子作为示例（demonstrations），从而改进预测效果。

- **问答 (Question answering, QA):** 科学领域的QA指利用计算方法，为科学问题提供准确且与上下文相关的答案。这需要从科学文献、数据库或其他信息源中检索或生成信息，以处理复杂的领域特定查询，例如“饭后我感到有些胃反流，应该吃什么药？”。在`graphRAG`中，通常会将科学文献转化为`Knowledge Graph`，为回答问题提供依据或用以丰富查询内容。

## 5.2 Scientific Graph Construction

在`GraphRAG`中，数据源的选择与构建至关重要，通常包括公共数据集和私有数据集。公共数据集来源于广泛认可的资源，如分子数据库PubChem、ChEMBL和ZINC，以及生物医学文献和数据源PubMed与ClinicalTrials。这些数据集为模型提供了跨领域的广泛信息基础和可靠的权威参考。私有数据集则包含用户特定信息，如医院的医疗记录或保密的临床试验数据，这些数据具有高度机密性和独特性，使`GraphRAG`模型能够提供个性化和专有的知识支持。

对于化学领域，分子主要有四种表示形式：1D `SMILES`（简化分子线性输入规范）、2D分子图、带坐标的3D分子图以及描述分子结构的文本标题。1D `SMILES`是通过在分子图上遵循特定规则进行深度优先搜索（DFS）生成的线性字符串。2D分子图将原子表示为节点，化学键表示为边。3D分子图则包含了每个原子的空间坐标，反映了分子的三维空间结构，这对于分子对接和反应预测等任务至关重要。文本标题则为分子结构提供了自然语言描述。

科学图谱的构建方法通常如下：

*   **基于文本的构建**：这是最常用的方法，可将文本化的科学知识转化为`Knowledge Graph`。Delile等人[78]认为，纯文本标题存在信息冗余和不平衡问题，通过将其构建为`Knowledge Graph`，可以重新平衡可检索信息并减少冗余。构建过程通常包括两个关键步骤：
*   **`Entity Extraction`**：识别并从文本中提取关键实体，如化学化合物、基因等领域特定术语。
*   **`Relationship Extraction`**：在识别实体后，提取这些实体之间的关系（例如，“A与B相关”），从而构建`Knowledge Graph`的结构骨干。

*   **基于`SMILES`的构建**：许多化学数据库以`SMILES`等分析描述符格式存储数据。为了进行图建模，需要将`SMILES`表示法转换为图结构。该方法利用`RDKit`等库读取`SMILES`符号，创建分子对象，并提取原子和键合信息来构建2D图。分子中的每个原子表示为一个节点，每个化学键表示为节点间的边。原子节点带有原子类型、度、电荷和芳香性等特征，而化学键边则可包含键类型（单键、双键等）以及是否属于环等信息。

*   **3D图构建**：Huang等人[167]介绍了`IRDIFF`模型，这是一种基于相互作用的、检索增强的3D分子扩散模型，专为目标特异性分子生成而设计。在`pre-training`阶段，利用`PMINet`和PDBbind v2016数据集来捕捉具有结合亲和力信号的相互作用结构上下文信息。该数据集提供了3D蛋白质结构和大量经过实验验证的蛋白质-配体复合物。这些蛋白质结构主要通过X射线晶体学、核磁共振（`NMR`）或冷冻电镜等技术获得，包含详细的原子坐标、键角和二级结构信息。

## 5.3 Retriever

`Retriever`负责根据输入查询定位相关信息，在`GraphRAG`中，这些信息通常是图结构数据。`Retriever`大致可分为基于启发式（heuristic-based）和基于深度学习（deep learning-based）两类。

- **基于启发式的Retriever**：此类`Retriever`采用预定义规则、算法和启发式方法从图结构数据源中识别和检索相关知识。其可分为以下几种类型：
- **基于相似度的Retriever**：Wang等人[433]基于与输入分子的`cosine similarity`来检索范例分子。`MindMap`[443]使用`BERT`将查询和外部`Knowledge Graph`中的实体编码为密集嵌入，然后检索相似度得分最高的实体集。
- **基于匹配的Retriever**：Wu等人[449]通过一个自上而下的匹配过程识别最相关的图，使`LLM`能够利用全面的私有数据生成基于证据的响应，从而增强结果的透明度和可解释性。
- **基于Knowledge Graph的Retriever**：此类方法能有效识别和检索响应查询所需的信息。Pelletier等人[318]和Li等人[225]使用命名实体识别和关系提取将用户查询与`Knowledge Graph`中的相关实体连接起来，从而从现有生物医学知识中发掘可解释的见解。Delile等人[78]将文本块映射到`Knowledge Graph`，然后利用图距离找到与用户问题最相关的文本块，并引入一种评分指标，通过为最短路径上的每个概念提供平等机会来平衡数据，该指标根据新近度和影响力对文本块进行排序。`HyKGE`[185]首先查询`LLM`生成一个假设性输出，并从中提取实体，然后在现有的`Knowledge Graph`（如`CMKG`[30]）中检索任意两个锚定实体之间的推理链，并将这些推理链与查询一同输入`LLM`。`KG-Rank`[484]则在查询中识别实体，并从`KG`中检索相关的三元组或子图以收集事实信息。
- **基于融合的Retriever**：Soman等人[366]首先根据与查询实体的向量相似性在`Knowledge Graph`中检索相关节点，然后检索与该节点关联的上下文三元组（主语、谓语、宾语）。

- **基于深度学习的Retriever**：此类`Retriever`能够提取相关知识以指导生成过程，例如分子或蛋白质的生成。具体而言，Huang等人[167]使用一个名为`PMINet`的预训练蛋白质-分子相互作用网络，提取目标蛋白与参考池中配体之间的交互结构上下文信息，以指导目标感知配体的生成。Jeong等人[175]利用现成的`MedCPT` retriever，这是一个专为检索生物医学查询文档而设计的工具，能为每个输入检索多达十个相关证据。`DALK`[225]则利用`LLM`的排序能力来过滤噪声并检索最相关的知识。

## 5.4 Organizer

`Organizer`主要分为两种类型：基于`embedding`的`organizer`和基于`query`的`organizer`，其划分依据是利用检索知识的方式。

- **基于`query`的`organizer`**：这是最简单直接的方法，它将检索到的信息与输入`query`整合以生成回应。
- `HyKGE`通过将检索到的推理链与原始`query`一同输入LLM，来增强其推理过程。这使得模型的响应能够基于结构化的、与上下文相关的信息，从而提高生成输出的准确性和深度。
- `Wu et al.`通过将检索到的实体名称及其关系以串联形式提供给LLM，来引导其回答问题。
- `DALK`和`KG-Rank`也采用类似方法，分别将`query`与检索知识、或将重排序后的三元组（triplets）与任务`prompt`结合，然后输入LLM进行推理和答案生成。
- 与上述方法不同，`Soman et al.`首先进行“context pruning”，通过筛选仅与回答`query`最相关的语义元素来优化检索到的上下文。然后，将这种经过剪枝的信息与输入`prompt`结合，形成一个内容更丰富的`prompt`输入LLM。
- `Delile et al.`开发了一种“data rebalancing mechanism”，以确保与问题相关的每个实体都有平等的表示机会，同时突出近期的重要发现。这种经过再平衡的知识随后与`query prompt`结合并输入LLM。

- **基于`embedding`的`organizer`**：此类`organizer`将检索到的信息与输入`embedding`进行融合以生成回应。
- `Wang et al.`使用一个轻量级、可训练的标准`cross-attention`机制，来融合输入分子与检索到的示例分子的`embedding`。
- 类似地，`Huang et al.`也使用一个可训练的`cross-attention`机制，但其融合的是检索到的示例配体（ligands）的增强`embedding`与模型所生成分子的`embedding`。

## 5.5 Generator

Generator是GraphRAG模型的核心组件，其主要职责是整合检索到的证据与输入数据，以生成最终的输出。根据所采用的生成模型类型，Generator可被分为三大类：基于Transformer的Generator、基于diffusion model的Generator以及基于large language models的Generator。

- **基于Transformer的Generator**：以RetMol [433]为例，该模型利用分子生成模型Chemformer的Megatron版本进行药物发现。Chemformer本身是一个基于Transformer的模型，能够高效地应用于化学领域的各项任务。

- **基于diffusion model的Generator**：Huang等人[167]提出了一种新颖的、基于交互的检索增强diffusion model（IRDIFF），专门用于基于结构的药物设计。IRDIFF的核心机制是利用参考蛋白与目标蛋白之间的蛋白质-分子相互作用数据来引导diffusion model，从而生成能够与目标口袋强力结合的分子。

- **基于LLM的Generator**：许多研究方法利用了诸如LLaMA2、LLaMA3、GPT-4和Gemini等large language models [449, 175, 318, 265, 225, 366]。具体应用案例如下：MedGraphRAG [449]通过GraphRAG提升LLaMA2、LLaMA3、Gemini和GPT-4在医学问答任务中的表现；Molecular-GPT [265]利用GraphRAG来增强GPT-3的分子属性预测能力；DALK [225]采用GraphRAG来提升GPT-3.5-turbo在回答阿尔茨海默病相关问题时的性能；HyKGE [185]则利用GraphRAG增强了GPT-3.5和Baichuan13B的医学问答能力。

## 5.6 Resources and Tools

本章节概述了在科学领域内，应用于graph RAG系统的常用数据源与工具，并对每个项目进行了简要描述。

## 5.6.1 Data Resources

### 5.6.1 数据资源

公开数据集通常来源于知名的资源库，例如分子数据库：
- **PubChem [204]**: PubChem 涵盖了广泛的化学数据，包括二维和三维结构、化学与物理性质、生物活性、药理学、毒理学、药物靶点、新陈代谢、安全指南、相关专利及科学文献。其大部分条目与小分子相关，主要侧重于原子数少于100个、化学键少于1000个的分子。
- **ChEMBL [121]**: 这是一个开放获取的数据库，包含有关药物、类药小分子及其生物活性的详细信息。该精选资源以其对药物发现过程的全面覆盖而著称，包含了超过220万种化合物的数据和超过1800万条记录其生物系统效应的文档。ChEMBL 提供了小分子与其蛋白质靶点相互作用的见解，以及这些化合物如何影响细胞和机体功能的数据。它还包括 ADMET（吸收、分布、代谢、排泄和毒性）特征信息。该数据库存储了二维结构、计算出的分子特性（如 logP、分子量和 Lipinski 五规则参数）以及生物活性数据（如结合亲和力和药理效应）。
- **ZINC [170]**: ZINC 数据集是一个为虚拟筛选目的而专门整理的市售化合物集合。它提供了超过2.3亿种可购买的、已准备好用于对接（docking）的3D格式化合物，以及超过7.5亿种可用于类似物搜索的化合物。每个分子都被调整到生物学相关的质子化状态，并标注了分子量、计算出的 LogP 和可旋转键等属性。该库包含供应商和采购细节，使其与多种广泛使用的对接软件兼容。在特定约束下，化合物以多种质子化状态和互变异构体形式提供，某些格式甚至为每个分子提供多种构象。ZINC 数据库可以多种常见文件格式免费下载，包括 SMILES、mol2、3D SDF 和 DOCK flexibase。

此外，还有如下的生物医学数据源：
- **PubMed [269]**: PubMed 是一个免费访问的数据库，主要收录 MEDLINE 集合，包含生命科学和生物医学领域的参考文献和摘要。该数据库由美国国家医学图书馆（NLM）在美国国立卫生研究院（NIH）内部管理，是 Entrez 检索系统的一部分。截至2023年5月23日，PubMed 包含超过3500万条引文和摘要，记录可追溯至1966年，部分精选记录可追溯至1865年，甚至有少数记录至1809年。在过去十年中（截至2019年12月31日），PubMed 平均每年新增近一百万条记录。
- **ClinicalTrials [509]**: ClinicalTrials 是一个全球性的注册库和数据库，提供由私人和公共来源资助的临床研究信息。该资源由美国国家医学图书馆管理，包含每项研究方案的摘要，部分研究还提供表格形式的结果。用户可以按研究状态、病症或疾病、国家及其他关键词进行检索。该数据库持续更新，现已包含在美国所有州和全球200多个国家进行的超过30万项研究。
- **开源医疗 Knowledge Graph (KG)**: CMeKG (中文临床医学知识图谱)、CPubMed-KG (大规模中文开放医学知识图谱) 和 Disease-KG (中文疾病知识图谱) 是开源的医疗 Knowledge Graph，它们整合了海量的医学文本数据，涵盖疾病、药物、症状和诊断治疗等领域。这些知识图谱合计包含1,288,721个实体和3,569,427个关系。

## 5.6.2 Tools

RDKit [217]是一个用于化学信息学的开源工具包。其主要特性包括：通过读取和写入SMILES、InChI和Mol文件等多种格式来处理化学结构；生成多种类型的分子指纹，以支持化学结构比较和相似性搜索。RDKit还提供计算分子相似性的算法，并支持化学反应的表示与处理，包括识别反应物和产物。尽管RDKit自身不具备分子对接功能，但它可以与其他对接工具集成。此外，RDKit支持机器学习算法，能够对化学数据进行模式识别并构建预测模型。

CADRO（Common Alzheimer's and Related Dementias Research Ontology）[23]被用于从医学QA数据集中提取与阿尔茨海默病（AD）相关的样本子集，以供评估。CADRO将术语组织成一个三层分类系统，包含八个主要类别和多个子类别，专注于AD及相关痴呆症，并包含了该领域常用的术语或关键词。用户可以利用CADRO获取与医学QA数据集最相关的AD关键词列表。

## 6 Social Graph

Social Graph通常由通过社会关系连接的实体构成，在现实世界的应用中无处不在。一个主要例子是像Twitter和Facebook这样的社交网络，其中实体代表由社交互动（例如友谊、关注/被关注、点赞和提及）连接的个体。这些Social Graph的应用范围超越了人类互动，并不局限于生物实体，例如在动物社交网络中共同使用同一洞穴的乌龟，在电子商务推荐系统中被同一顾客共同购买的互补产品，甚至包括由LLM模拟的社交代理。这些Social Graph中丰富的社会关系知识是GraphRAG的宝贵资源，本节将对此进行综述。

## 6.1 Application Tasks

### 6.1 应用任务

本节概述了图结构数据在多种任务中的应用。

**实体属性预测 (Entity Property Prediction):** 该任务的核心是预测社交网络中社会实体的属性与类别。具体应用场景包括预测伙伴关系的兼容性、评估道德水平、检测账户封禁、识别有毒行为[183]以及预测产品属性[427]。

**文本生成 (Text Generation):** 此任务旨在生成符合特定社交情境和规范的文本。其实现通常依赖于结构信息与文本信息的相互作用，例如基于邻近性的网络同质性（proximity-based network homophily）和基于角色的相似性（role-based similarity）[5]。例如，Wang等人[429]通过检索邻近或角色相似节点的文本来增强目标节点的文本生成能力。Kim等人[202]和Xie等人[463]则通过检索客户与产品的历史评论，生成个性化的推荐解释。此外，其他研究也利用语义相似性来检索参考、属性或观点，以增强下游的评论生成任务[353, 92, 315]。

**推荐 (Recommendation):** 推荐任务旨在为用户找到最相关的项目。由于客户与项目间的交互数据常存在缺失和稀疏问题（如冷启动 `cold-start issues`），`GraphRAG` 可通过检索额外的元知识（meta-knowledge）来有效增强稀疏的交互数据。根据具体场景，`GraphRAG` 已被应用于基于图的推荐[438, 95]、下一个项目推荐（next-item recommendation）[427, 159, 528, 327, 510, 416]以及对话式推荐[116]。

**问答 (Question-answering):** 问答任务不仅存在于知识图谱和文档图领域，也广泛应用于社交图。例如，用户可能提出“Los Gatos附近最适合家庭聚会的公园是哪些？”这类问题，并期望获得个性化的答案[511, 198]。更进一步，某些问题可能明确要求进行图结构推理。例如，Wu等人[452]构建了一个半结构化知识库，用户可能会查询“你能列出Nike生产的产品吗？”。回答这类问题不仅需要深入理解查询意图，还必须熟悉数据的内在结构信息。

**虚假新闻检测 (Fake News Detection):** 检测虚假新闻需要综合考量语义内容（新闻正文）和结构化交互（新闻间的互动关系）。例如，Ram等人[331]通过评估与目标Reddit帖子有过互动的共同评论者所评论的其他帖子的可信度，来判断目标帖子的可信度。

## 6.2 Social Graph Construction

GraphRAG利用社交图谱来获取额外信息，其所依赖的关系主要可归纳为三种基本原理：基于邻近性（proximity-based）、基于角色（role-based）和基于个性化（personalization-based）。

基于邻近性的原理源于“物以类聚，人以群分”的观念，即社交网络中彼此邻近的节点通常共享相似的属性，例如，亲近的朋友往往有相似的爱好。基于角色的原理关注具有相似局部子图结构（local subgraph structures）的节点，这些节点共享相似的特征或标签分布。例如，公司内同一层级的管理者通常拥有相似的职位和职责，而枢纽机场也表现出相似的运营特征和战略重要性。最后，基于个性化的原理指个体在特征和互动方面的独特性。例如，在推荐系统中，用户与物品的互动方式多种多样（如点击、查看、加购、购买和评论），每种互动都为GraphRAG提供了可用于生成个性化内容的宝贵知识。

基于上述三种关系原理，社交图谱的构建方法可总结如下：

-   **User-User-Interaction**：此类社交图谱表示用户间的互动，常见于Twitter、Reddit和Facebook等社交网络。例如Twitter上的关注关系、Facebook上的好友关系以及Reddit上用户对其他用户帖子的评论。值得注意的是，与文档或知识图谱相比，这种用户间的互动是现实世界中自然存在的，无需人工策划或修改。
-   **User-Item-Interaction**：此类社交图谱表示用户与物品间的互动，常见于Amazon和eBay等电子商务平台。这些互动行为（包括购买、加入购物车和查看）可以被建模为一个二分图（bipartite graph），其中每种互动类型都反映了用户独特的意图。
-   **Item-Item-Interaction**：此类社交图谱捕捉物品之间的互动关系，通常通过来自同一客户或用户的共同互动来识别。例如，两个产品间的“共同浏览”（co-view）互动表示它们被同一客户浏览过；而“浏览-加购”（view-add-to-cart）互动则表示同一客户先浏览了一个产品，接着将另一个产品加入购物车。在电子商务网络中，两个物品间的这些共同互动可大致分为互补关系和替代关系。
-   **Metadata-Interaction**：物品和用户通常拥有元数据（metadata）。例如，Amazon等平台上的产品可能包含品牌、制造商和颜色等属性。这些元数据可以表示为额外的节点类型，并通过相应的边来指示产品与属性之间的关系，如所有权或关联。
-   **Agent-Agent Interaction**：随着LLMs智能水平的提升，近期文献开始探索使用由LLM驱动的智能体（agent）来模拟协作、辩论和反思等社会行为。这些智能体之间的互动也可用于GraphRAG。

需要注意的是，在上述五种互动类型中，user-user、user-item和metadata关系是自然形成的，无需人工策划。相比之下，item-item互动是通过手动提取生成的，而agent-agent互动则需要通过模拟来产生。

## 6.3 Retriever

在`GraphRAG`中，可以利用社交图谱中的关系来检索额外信息，以增强下游任务（如推荐）的效果。本节回顾了`GraphRAG`在社交图谱中使用的代表性`Retriever`方法。

- **ID-based Retriever**：该方法类似于实体链接，通过检索由特定用户/项目生成的内容来工作。例如，检索特定客户的历史项目交互记录、特定产品的用户评论以及特定用户的元数据信息。

- **Filtering-based Retriever**：该方法在`ID-based retriever`的基础上，利用`collaborative filtering`来检索额外内容。在用户过滤方面，通过比较历史项目交互的相似性，识别出与目标推荐用户最相似的Top K个用户，并从这些用户中检索最受欢迎的项目来增强目标用户的上下文。在项目过滤方面，通过比较用户交互历史，识别出与当前项目最相似的Top K个项目，并从中获取最受欢迎的项目来增强当前的推荐。

- **Social Relational Retriever**：与`ID-based Retriever`类似，该方法专注于从与目标实体有特定关系的其他实体中检索知识。例如，有研究分层检索中心节点数跳范围内的邻居文本，以增强目标用户/项目的语义信息。同时，也有方法检索与目标节点具有高邻近性（proximity-based）和角色相似性（role-based）的节点所对应的文本。

- **Integrated Neural-Symbolic Retriever**：这种方法结合了符号化（symbolic）和神经化（neural）两种`Retriever`以提升检索效果。符号化`Retriever`遵循明确定义的规则进行检索（如基于标识符、结构化关系或交互模式），确保检索数据严格符合特定标准。而神经化`Retriever`则通过基于`embedding`的相似性来补充，捕捉规则无法直接编码的细微模式和上下文关系。两者的结合在基于规则的精确性与基于神经网络的适应性和泛化能力之间取得了更好的平衡。例如，有研究首先从产品`knowledge graph`中检索用户会话中产品的K跳邻居（符号化`Retriever`），然后利用基于神经网络的自适应过滤来聚合与当前序列最相关的项目（神经化`Retriever`）。类似地，为解决数据稀疏性和异构性问题，有方法将基于用户ID检索电影的`ID-based retrieval`与支持跨方电影检索的文本`Retriever`相结合。

## 6.4Organizer

为了进一步增强检索到的内容，用于社交图的Organizer采用了超越其他图领域中典型重排序和过滤的专门技术。对于社交图，GraphRAG的Organizer通常使用Keyword Extraction、Profile Summarization和Hierarchical Graph Aggregation来组织检索内容：

*   **Keyword Extraction:** 该技术从检索到的内容中识别最相关、信息量最大的关键词。这些提取出的关键词能够引导下游的生成器优先分配注意力，并降低因上下文过多而给LLM带来负担的风险。例如，Xie等人[463]使用一个embedding estimator来精确定位与个性化潜在查询对齐的关键词，这些关键词随后被用于生成解释。

*   **Profile Summarization:** 该技术创建丰富而详细的用户画像，捕捉从用户过往交互和项目元数据中推断出的属性，如年龄、性别、偏好和不喜欢的类型、喜爱的导演、国家和语言等[438]。这种丰富的用户数据通过使用重写后的画像，在保护隐私的同时，也增加了检索内容的信息量。此外，Wang和Lim[416]在通过用户/项目过滤检索到相关电影后，应用一种三步prompting策略，通过直接指示LLM来提取为用户量身定制的特征并选择代表性电影。这些提取的特征和代表性电影被进一步用作用户画像，以指导最终的推荐生成。Guo等人[137]则利用LLM，根据来自外部数据的关键词或短语为实体画像生成更多细节，以辅助文本生成。

*   **Hierarchical Graph Aggregation and Summarization:** 在检索邻域文本信息时，高阶邻域层中指数级扩展的感受野常常导致聚合内容超出可管理的限制，这可能削弱LLM的效能[236]。这一挑战凸显了进行分层图聚合与总结的必要性。其核心思想是，在将每一层检索到的邻域信息传播到下一层之前，先对其进行总结。这种方法使每个节点接收的文本量保持在一致的范围内。例如，Du等人[95]从更高层的邻居节点递归地聚合信息，并利用LLM在将内容分享给低层相关节点之前对其进行转述和压缩。因此，该策略在扩展感受野的同时，也优化了下游生成任务的计算预算。

## 6.5 Generator

在检索并组织好相关内容后，这些信息会被送入一个下游的`Generator`进行进一步处理，以生成最终内容。根据期望输出的不同，用于社交图谱的现有`Generator`可分为基于`LLM`的文本生成器和基于预测的生成器。这两种类型的选择取决于期望输出的格式以及社交图谱应用的需求。

- **基于LLM的文本生成 (LLM-based Text Generation):** 当下游应用需要文本输出时，通常会使用此类生成器，例如基于名称的物品推荐、推荐解释和评论生成。由于下一词元预测（next token prediction）具有概率性，生成的文本可能不总是与期望输出完全一致。为了解决这种幻觉（hallucination）问题，通常会使用真实数据（ground-truth text）来对生成的文本进行校准，例如将生成的物品与平台上的真实物品进行匹配。

- **基于预测的生成 (Prediction-based Generation):** 此类生成器直接预测输出，主要用于非文本任务，如物品推荐和社交预测。例如，`Graph Neural Networks`已成为基于图的推荐任务的热门选择，而`Transformers`则被用于物品推荐任务。此外，在社交属性预测中，`Generator`可以是一个简单的多层感知机（multilayer perception），用于分类（如党派倾向分类）或回归（如道德观回归）。

## 6.6Resources and Tools

本章节列举了在 social graphs 上应用 GraphRAG 所需的常用资源与工具，并将以逐项列表的形式提供其摘要和链接。

## 6.6.1 Data Resources

### 6.6.1 数据资源

- **STARK-Amazon**: 这是一个大规模、半结构化的检索基准数据集，专为亚马逊平台上的产品搜索而设计，整合了文本和关系知识库。数据集中的节点代表产品、颜色、品牌和类别，而边则捕捉了如`also_bought`、`also_viewed`、`has_brand`等关系。该数据集包含丰富文本信息，如产品描述和顾客评论，为检索任务提供了重要上下文。其查询是通过关系模板采样并与特定实体结合生成，再利用LLM综合相关的文本和关系信息，从而模拟出能捕捉顾客兴趣、理解专业描述并推断多实体关系的复杂查询。

- **Amazon-Review**: 该数据集包含带有评分、文本和有用性投票的评论，以及产品元数据（如描述、类别、价格、品牌和图像特征）。此外，它通过`also viewed`和`also bought`图谱提供了链接信息。此数据集有两个版本：早期版本记录了1996年至2014年的评论数据，而新版本则记录了2014年至今的数据，并增加了新的元数据，如详细产品信息和道德细节表。大量在社交图谱领域的GraphRAG研究已利用此数据集为推荐研究构建RAG框架。

- **MovieLens**: MovieLens数据集描述了用户对电影的偏好，表现为包含用户、电影、评分（0-5星）和时间戳的元组。这些数据来源于MovieLens网站——一个通过用户评分来提供个性化电影推荐的系统。数据集的辅助信息包括电影标题、年份和类型的文本。部分研究进一步爬取了电影海报的视觉内容。其中，Movielen-100k版本被频繁使用，并提供了用户ID、年龄、性别、职业等人口统计信息。

- **Netflix**: 该数据集为Netflix Prize竞赛而构建，包含了从48万匿名Netflix用户中随机抽取的、针对1.7万部电影的超过1亿条评分记录。数据收集于1998年10月至2005年12月，反映了该时期的评分分布。数据还提供了每次评分的日期、电影标题和上映年份。研究人员通过网络爬虫收集了相关的多模态辅助信息。

- **Yelp**: Yelp数据集是用于学术研究的丰富资源，尤其适用于数据科学、自然语言处理（NLP）和机器学习领域。它包含超过690万条评论、15万个商家和20万张照片，覆盖11个都市区。数据集提供了详尽的商家信息（位置、类别、营业时间等）、完整的评论文本和评分、以及包含社交关系和行为的用户画像。此外，它还包括约91万条“贴士”（tips）和120万条商家属性，为研究提供了细粒度的信息。

- **Weibo**: 微博数据集捕捉了新浪微博平台上的用户互动、行为和社交关系。该数据集从100个随机种子用户开始，扩展到170万用户和约4亿个关注关系。每个用户都有详细的个人资料，推文内容则以原始中文和索引格式提供。该数据集为社交网络分析、内容传播和用户互动动力学等研究提供了支持，对于RAG研究也极具价值。

- **Brexit**: 该数据集包含了2016年英国脱欧公投前X (Twitter)网络中关于“留欧-脱欧”讨论的一部分。它构成了一个包含7,589名用户、532,459条有向关注关系和19,963条推文的网络，每条推文都关联一个二元立场（0代表“留欧”，1代表“脱欧”）。数据经过预处理，为每个用户分配了一个0到1之间的标量值（称为opinion），代表该用户转发推文的平均立场。

- **Diginetica**: 该数据集包含来自一个电子商务搜索引擎的用户会话日志。数据跨度为六个月，捕捉了用户的点击、产品浏览和购买等互动行为。每个用户会话（以一小时不活动为界）包含匿名用户ID、哈希处理的查询、产品描述和元数据（价格、哈希处理的产品名、图像标识符和产品类别）。

- **Yoochoose**: Yoochoose数据集包含一家欧洲在线零售商的会话数据。每个会话记录了用户的点击事件，部分会话还包含购买事件。数据收集于2014年，捕捉了用户与零售商网站的互动行为，其产品元数据包括类别信息。

## 6.6.2 Tools

*   **X-Developer Platform**³³: X-Developer Platform为开发者提供了强大的工具与资源，以便将X的实时、历史和全球数据集成到其应用程序中。该平台包含三个主要产品：X API、X Ads API和X for Websites，支持从检索和分析推文到管理广告活动，再到将X内容直接嵌入网站等多种用例。X API提供用于管理对话、探索趋势和与用户互动的端点；X Ads API使企业能够通过自定义定位和分析来管理广告；X for Websites则允许无缝嵌入实时内容以增强网站互动。通过全面的文档、库和社区支持，X-Developer Platform使开发者能够利用X的数据和互动工具创建创新的解决方案。

*   **Reddit-API**³⁴: Reddit是一个新闻聚合与讨论平台，其帖子被组织在由社区管理的、用户创建的板块“subreddits”中。Reddit API为开发者提供了访问该网站海量帖子和评论的权限。这个免费的API促进了审核工具、第三方应用以及用于训练LLMs（如ChatGPT、Google和Gemini）的数据集的开发。通过使用此API，可以查询海量的用户交互（即评论和帖子）及其相应的文本内容（即subreddit帖子串），这些被认为是GraphRAG的宝贵资源。

*   **Rec-Bole**³⁵ [553]: RecBole是一个开源、统一且全面的库，专为开发和基准测试推荐算法而设计。RecBole基于Python和PyTorch构建，为研究人员提供了一个精简高效的框架，用于实验超过100种推荐算法，涵盖四大类别：通用推荐、序列化推荐、上下文感知推荐和基于知识的推荐。该平台通过提供43个基准数据集的预处理副本，简化了数据处理流程，使用户能轻松投入模型测试与开发。其提供的用户-产品交互数据以及文本格式的用户/产品元数据，也可用于GraphRAG。

## 7 Planning and Reasoning Graph

规划或推理图（planning or reasoning graph）用于描述不同实体间的内在逻辑流，其中实体通常代表具体的规划或推理子步骤，而边则表示它们之间的逻辑关系。在规划图（planning graph）中，一个常见的例子是为达成特定目标而使用的一组API工具，其中节点代表行动，边表示它们之间的关系依赖。对于推理图（reasoning graph），一个显著的例子是近期提出的`chain/tree/graph of thoughts`技术，其中每个节点代表一个由推理流连接起来的决策思考步骤。

该章节的核心论点是，规划与推理图中存在的依赖约束和推理流可以被自然地表示为关系型知识（relational knowledge），这为`GraphRAG`模型完成规划与推理任务奠定了基础。本节内容将回顾`GraphRAG`在规划与推理图领域的应用。

## 7.1 Application Tasks

本节总结了在规划与推理图上执行的代表性应用任务，具体如下：

*   **Sequential Plan Retrieval**：作为最常见的任务之一，计划检索旨在以子图的形式检索完成用户查询所需的步骤或工具计划。例如，对于一个复杂指令“请生成一张女孩读书的图片，姿势与‘example.jpg’中的男孩相同，然后用语音描述新图片”，从全局计划图中检索出的最终计划将是 "Post Detection" → "Pose-to-Image" → "Image-to-Text" → "Text-to-Speech"。

*   **Naturalistic Asynchronous Planning**：与仅考虑计划间依赖性约束的计划检索相比，该任务引入了时间约束，带来了更大的挑战。它旨在生成一个既满足依赖性要求又能优化任务完成效率的计划，其方法利用了时间求和、时间比较和约束推理。例如，用户可以提供制作烤馅饼的步骤和所需时间，系统计算出的最优计划会并行执行“预热烤箱”等步骤，以提高效率。

*   **Structured Commonsense Reasoning**：给定一个信念和一个论点，该任务旨在推断出相应的立场，并生成或检索一个常识解释图来解释所推断的立场。

*   **Defeasible Inference**：这是一种特殊的推理模式，即在给定一个前提的情况下，一个假设可能会因为新证据的出现而被削弱或推翻。一种主流方法是通过构建推理图进行论证来支持这种可废止推理。

*   **Tool Usage**：指导 LLMs 使用外部工具解决复杂的现实世界问题变得日益重要。近期研究探索了高级规划策略以增强 LLMs 的工具使用智能。其中，两种著名的方法分别采用了 A* search 和 Monte Carlo Tree Search，两者都利用图结构化推理，根据 LLM 的内部评估和环境反馈来适应性地检索下一个工具。这些方法实现了动态工具检索，提升了模型解决问题的精确性和灵活性。

*   **Embodied Planning**：在 Embodied AI 领域，Embodied Planning 任务涉及引导智能体在模拟或真实环境中，根据自然语言指令和视觉线索执行一系列动作，如整理或清洁。这些任务因指令模糊、特定任务知识有限、反馈稀疏以及复杂多变的动作空间而充满挑战。

## 7.2 Reasoning and Planning Graph Construction

现有的推理与规划图构建方法大多首先分析关系依赖，然后基于这些硬编码规则添加边。因此，本文将重点回顾用于添加边的各种依赖关系类别，而非仅限于基于规则的构建方法。

- **资源依赖 (Resource Dependency) [355, 372, 454]**: 此依赖定义为不同行动/决策之间共享的资源。例如，如果一个工具的输出与另一个工具的输入相匹配，则这两个工具被连接起来，从而实现从一个过程到另一个过程的无缝过渡。现有图构建方法通过检查一个节点的输入是否与另一个节点的输出（例如，计划、工具或其他抽象过程）相匹配来决定是否添加边。

- **时间依赖 (Temporal Dependency) [355]**: 这种关系确保在规划和推理过程中，事件序列遵循特定的顺序。例如，在某些收集的数据集中，连接表示了日常生活中两个API之间的连续调用顺序。

- **包含依赖 (Inclusive Dependency) [277]**: 该依赖描述了两个连接的节点属于同一类别或环境。例如，鹅卵石和鸟屋都属于花园装饰品类别[427]。`Hypergraphs`可以有效捕捉这种一个实体属于多个环境的归属关系[111]。此外，这些依赖常形成层级结构，其中“祖父”实体包含“父”实体，“父”实体又包含其“子”实体。随着层级深度的增加，可能存在的依赖关系空间呈指数级增长，带来了巨大的计算挑战。为解决此问题，许多先前工作提出在`hyperbolic space`中对此类层级结构进行编码[277, 257, 527]。据我们所知，尚无研究在RAG系统中探索包含依赖。

- **因果依赖 (Causal Dependency) [248]**: 此依赖表示图中的因果逻辑，即一个行动/决策导致另一个行动/决策的触发。一个经典的例子是用于编码数据生成过程假设的因果图。

- **类比依赖 (Analogy Dependency) [499, 503]**: 该依赖强调类比推理，其关系形式为“A之于B犹如C之于D”。通过识别和利用此类依赖，人类能够基于现有知识跨领域建立新的见解。一个有力的历史例证是库仑定律的发现，其灵感来源于天体间的引力与带电粒子间的电力之间的类比[322]。

尽管资源依赖和因果关系都涉及顺序结构化的关系（前一步/工具/决策导致后一步/工具/决策），但它们本质上是不同的。例如，如果工具A生成PDF格式的报告，而工具B用于从PDF文件中提取数据，那么工具A和B共享资源依赖，因为A的输出（PDF）与B的输入相匹配。然而，这种连接并不意味着两者之间存在直接的因果关系，即使用工具A不一定会*导致*我们使用工具B。

## 7.3 Retriever

用于处理推理和规划图任务的`Retriever`通常被建模为图遍历器 (`graph traversers`)。该过程由查询或任务指令定位初始种子节点以启动图遍历，随后遍历会扩展图的范围，直至达到预设的预算或满足特定标准。整个过程的核心步骤是从所有候选者中选择最相关的邻居。根据邻居选择标准，`Retriever`可分为两大类：基于`embedding`的方法和基于启发式的方法。

- **基于`Embedding`的方法**：此类方法根据`embedding`相似度来确定邻居的优先级。例如，Wu等人[454]提出分解查询，然后将子查询与当前已检索的任务API拼接，并与所有现有的邻居API进行`embedding`相似度匹配，从而选择最匹配的API。该研究同时探讨了需要训练和无需训练的策略。

- **基于启发式的方法**：与依赖专用训练数据进行映射的基于`embedding`的方法不同，此类方法通过定义规则来有效指导图`Retriever`[555, 569, 142]。例如，Zhuang等人[569]将工具规划建模为树搜索算法，并结合`A* search`，根据累积和预期的成本自适应地检索最有潜力的工具。这些成本函数是基于现有文献和实践经验启发式设计的。

- **`Thought Propagation Retrieval`** [499]：这是一种特殊方法。对于给定的输入问题，它首先提示LLM提出一系列相似问题，然后应用如`Chain-of-Thought (CoT)`等成熟的提示技术来推导这些问题的解决方案。最后，一个聚合模块 (`aggregation module`) 会整合这些方案，以增强对原始问题的解决能力。

## 7.4 Organizer

当前关于规划与推理图（planning and reasoning graphs）的 GraphRAG 文献通常省略了 Organizer 机制，因为其检索过程本身已能达到足够高的精度，从而无需进行重排序（reranking）。

这与文档图或 knowledge graphs 不同，后者通常采用单次（one-shot）基于 embedding 的相似性检索来选择 top-K 相关内容。相比之下，规划与推理图使用一种与推理步骤相结合的多轮（multi-round）embedding 相似性过程，这增强了规划的保真度（fidelity）。此外，基于奖励（reward-based）的检索涉及一个复杂的搜索过程，可进一步提高准确性。

综上所述，这些高质量的检索策略共同作用，降低了对精细化重排序或过滤的需求。

## 7.5 Generator

在处理推理和规划任务时，现有的大多数 GraphRAG 方法中的 Generator 主要采用两种策略。第一种是直接输出检索到的计划，例如，Wu等人[454]将检索到的图结构计划作为最终结果。第二种是将检索到的信息整合到 LLM 中以生成下游解决方案。具体实例包括：Shen等人[356]汇编来自专家工具的执行结果以生成响应；Shen等人[355]在构建工具调用图后，直接提示 LLM 生成参数；Lin等人[248]则利用 LLM 根据任务依赖、时间和图约束来生成异步计划。一个显著的共同点是，这些研究大多侧重于融合文本信息，主要通过将不同的图结构格式（例如，邻接矩阵、邻接列表、边列表、CSR）以文本形式呈现给 LLM 进行处理。

## 7.6 Resources and Tools

### 7.6 资源与工具

本节总结了在 planning graphs 和 reasoning graphs 上应用 GraphRAG 所需的实用资源与工具。

## 7.7 Data Resources

本节介绍了多个用于训练和评估AI模型（尤其是在规划、推理和工具使用方面）的数据资源，其中许多具有图结构。

- **Hugging Face [355]**: 该数据集将Hugging Face上的AI模型视为工具节点，涵盖语言、视觉、音频等多模态任务。如果工具A的输出类型与工具B的输入类型匹配，则它们之间存在连接。因此，Hugging Face规划图中的边代表资源依赖关系。其构建过程首先收集工具库并建立工具依赖图；然后，通过从图中采样三种基本格式（节点、链、有向无环图-DAG）的子图来生成问题，每种格式代表一种特定的工具调用模式；接着，利用LLMs为采样的子图合成用户指令并填充参数；最后，采用基于LLM和规则的自我批判机制进行检查和筛选，以保证生成指令的质量。

- **Multimedia [355]**: 与Hugging Face中专注于AI的工具不同，多媒体工具服务于更广泛的以用户为中心的任务，如文件下载和视频编辑。其图的边与Hugging Face领域保持一致，表示资源依赖关系。Multimedia数据集的构建方法与Hugging Face类似。

- **Daily Life APIs [355]**: 日常生活服务（如网页搜索和购物）也可以被视为特定任务的工具。这些API之间的依赖关系主要是时间上的，即如果一个API在序列上紧随另一个，则它们相连。该数据集的构建过程与Hugging Face基本相似，但由于公开API的稀缺性，其边是手动构建的。

- **RestBench [372, 454]**: 这是一个包含多个API的数据集，用于处理两个场景（TMDB电影数据库和Spotify音乐播放器）中复杂的真实世界用户指令。TMDB提供关于电影、电视、演员和图像的RESTful API，而Spotify提供用于检索内容元数据、获取推荐、管理播放列表和控制播放的API。在构建RestBench时，[372]首先由NLP专家为不同的API组合设计指令，并标注每个指令的正确API解决方案路径，再由另外两名专家验证其可解性和正确性。为了将其适配为图结构数据集，[454]将每个API视为一个任务节点，并通过两个关键维度建模它们的关系：(1) **类别关联**，例如将提供电影相关功能的API（如检索电影详情）归为“电影”类别；(2) **资源依赖**，如果两个API共享一个共同参数（如`movie-id`），则建立链接。此外，还使用GPT-4为每个API分配唯一的名称和详细的功能描述，以增强语义区分度。

- **Asynchow [248]**: 这是一个包含1.6K个数据点的异步规划数据集。每个数据点包含一个用户指令，该指令指定了具有基本执行约束的任务，并由一个有向无环图（DAG）表示。在这些DAG中，节点代表动作，边代表顺序约束。每条边带有一个权重，表示完成前一个动作并转换到下一个动作所需的时间。此外，边还表示因果链接，即一个动作只有在所有前序链接动作完成后才能进行。该数据集的构建首先从WikiHow收集规划任务，然后使用LLMs进行预处理、时间标注和步骤依赖标注。具体而言，GPT-3.5用于估计每个步骤的持续时间，GPT-4使用DOT语言标注步骤依赖关系。为了生成带有执行约束的自然语言问题，使用了十个模板将图结构的DOT语言转述为人类可理解的文本。一个规划的最佳持续时间通过计算工作流DAG表示中的最长路径来确定。

- **EXPLAGRAPHS [342]**: 该数据集通过一个通用的“创建-验证-修正”迭代框架构建常识性解释图。初始数据为包含信念、论点和立场的“三元组”。首先，标注者构建一个常识增强的解释图来明确解释立场。每个图包含3-8个事实，每个事实是一个由两个概念实体及其关系构成的三元组。这种图形表示允许自动进行结构约束检查，保证图的结构正确性。为确保语义正确性，标注者会仅根据信念和解释图进行推理以推断立场。最后，对于不正确的图，由另一位标注者通过添加、删除或替换事实来进行修正。

- **GSM8K [65]**: 这是一个包含8.5K个高质量、语言多样化的数学应用题的数据集，旨在评估问答中的多步推理能力。这些小学水平的问题（聪明的初中生可解）需要2到8个步骤，主要使用基本算术运算（+、-、×、÷）。其解决方案以自然语言形式呈现，以便深入了解大型语言模型的推理过程，并展示模型如何处理结构化的、分步的推理任务。

- **PrOntoQA [348]**: 这是一个问答数据集，提供带有“思维链”（chains-of-thought）的示例，以勾勒出得出正确答案所需的推理过程。其句子句法简单，非常适合进行语义解析，因此对于大型语言模型（如GPT-3）预测的推理链进行形式化分析非常有价值。

## 7.7.1 Tools

当前利用 `LLMs` 进行软件工具操作的研究主要依赖于封闭模型 `APIs`（例如 `OpenAI`），因为这些专有模型与现有开源 `LLMs` 在性能上存在显著差距。为了探究此差异的根本原因并提升开源 `LLMs` 的工具操作能力，研究人员开发了一个名为 `ToolBench` 的基准测试。`ToolBench` 包含一系列为真实世界任务设计的、多样化的软件工具，并提供了一个易于使用的基础设施，可以直接评估每个模型的执行成功率。

## 8 Tabular Graph

表格数据（Tabular data）是现实世界应用中广泛使用的另一种结构化数据，通常存储在关系型数据库中。表格数据可能由包含样本及其属性的单个表，或共享主键和外键的多个表组成。

大型语言模型（LLMs）已被探索用于处理和解决涉及表格数据的任务，主要方法是通过`serialization`将表格数据转换为文本。然而，这种`serialization`方法可能导致一些问题：(1) 对于单表情况，特征列应具有`permutation invariance`（置换不变性），但序列化表格数据可能会破坏这种不变性；(2) 对于多表情况，表之间通过主键/外键连接，利用这些关系对完成各种任务至关重要，而`serialization`可能无法有效捕捉这些关系。

因此，图结构（graph structures）可以成为表格数据的一种合适表示方式。此外，当表格包含的行数过多，超出LLMs的上下文窗口时，图结构可以促进高效的数据检索。

## 8.1 Application Tasks

表格在现实世界中被广泛用于存储特征和数据间的关系，因此理解表格数据结构至关重要。将表格数据转换为图结构后，可以应用于多种任务，以下列举了几个代表性应用：

-   **节点级任务 (Node-level tasks):** 此类任务包括 `node classification` 和 `node regression`，具体应用涵盖细胞类型预测 [188]、欺诈检测 [335, 364]、异常值检测 [124] 以及点击率 (CTR) 预测 [242, 94]。

-   **链接级任务 (Link-level tasks):** 此类任务涉及 `link prediction`、`edge classification` 和 `edge regression`。许多表格数据处理任务可以被建模为链接级任务，例如数据插补 [557, 497] 和推荐系统 [339]。

-   **图级任务 (Graph-level tasks):** 此类任务旨在预测整个图的属性，例如表格类型分类和表格相似度预测 [432, 178, 188]。

-   **表格问答 (Table question answering):** `Table QA` 通过对表格数据进行理解和推理来生成答案。该任务要求同时理解表格内容及其内部关系，因此图结构非常适合用于编码这类信息。例如，Zhang [532] 和 Zhang et al. [531] 利用图结构来增强 `Table QA` 的性能。

-   **表格检索 (Table retrieval):** `Table retrieval` 专注于根据自然语言查询，检索出语义上相关的表格 [411, 61]。

## 8.2 Tabular Graph Construction

为表格数据构建图（Graph）旨在建模高阶的特征交互、高阶的实例关系以及跨多个表格的实例间关系。图中的节点通常分为两类：代表表格中每一行的实例节点（instance nodes）和代表单个特征的特征节点（feature nodes）。主要的图构建方法如下：

- **Instance Graph**：该图连接一个表中的行（实例），用于建模实例之间的关系，尤其适用于在表格数据中检索相关实例。其构建方法主要有两种：
- **基于规则的方法 (Rule-based methods)**：根据预定义规则连接实例。例如，利用专家知识衍生的启发式规则连接共享某些特征的实例，或使用基于相似性的方法，如通过K-Nearest Neighbors (KNN)算法或基于相似度超过阈值来连接实例。
- **可学习的方法 (Learnable methods)**：通常使用规则或启发式方法初始化一个`Instance Graph`，然后在模型学习过程中调整边的权重，从而动态地优化图结构。

- **Feature Graph**：该图连接各个特征，边代表成对特征之间的相关性。特征关系通常以可学习的方式进行建模。一些工作利用特征相似性来构建图，另一些则使用基于专家知识的启发式方法建立连接。此外，也有方法将属于同一个实例的特征连接起来。

- **Instance-Feature Graph**：这是一种`heterogeneous graph`，它将实例节点与其对应的特征节点连接起来。

- **Cell Graph**：这种图将表格中的每个单元格（cell）视为一个节点。例如，Xue等人构建的`Cell Graph`中，每个单元格节点包含空间和逻辑位置属性，而邻接矩阵则表示两个单元格之间的相邻关系或同行同列关系。

- **Tabular Hypergraph**：`Hypergraph`是图的一般化形式，其中的`hyperedge`（超边）可以连接多个节点。由于表格数据通常对行和列的任意排列具有不变性，`Hypergraph`成为一种合适的建模结构。例如，有研究将表中的每一行和每一列建模为一个`hyperedge`用于`pre-training`。此外，`Hypergraph`也被用来有效捕捉实例间的关系。

此外，还有其他方法，如Cvetkov-Iliev等人将表格建模为一个`Knowledge Graph`，其中特征值或行代表节点，列名代表关系。Zhang等人基于多种预定义关系构建了一个`heterogeneous graph`。Wang等人则为非关系型表格构建了基于层级关系的树状结构。

以往的方法主要集中于基于单个表格构建图。然而，在关系型数据库中，数据通常分布在多个表格中。一种常见方法是先将这些表合并为单个大表，再应用上述方法。但这种方式依赖于作为特征工程一部分的手动表格连接，需要大量的精力和领域知识。因此，`Cross-table Graphs`被提出来直接从多个表格构建图，无需手动合并。

- **Cross-table Graphs**：这类图通常连接来自不同表格的实例。节点通常代表每个表中的行，而边则由主键-外键（primary-foreign key）关系定义。例如，Wang等人提出了`Row2N/E`方法：如果一个表有主键（PK），则每行被视为一个节点；但如果该行同时包含两个外键（FK），则它被视为一条边。这类图能够建模跨多表的关系，从而整合不同来源的信息以支持各类任务。此外，Bai等人基于多表构建了一个`hypergraph`，其中主键或外键作为节点，同一表内的节点构成一个`hyperedge`。

## 8.3 Retriever

将表格数据建模为图（Graph）的研究尚处于早期阶段，大多数工作沿用了第2.4节中介绍的流行检索方法。具体而言，Fey等人 [115] 提出一种方法，通过基于时间戳检索`subgraphs`来构建时间一致的计算图。与此同时，Cvitkovic [71] 则采用一种`deterministic heuristic`（确定性启发式方法）来选择`subgraphs`。

## 8.4 Generator

在处理表格图时，大多数现有方法仍依赖 `GNNs` 或 `Graph Transformers` 作为生成器。此外，一些研究开始融合不同模型，例如 Wang 等人 [417] 将 `GNNs` 与 `DeepFM`、`FT-Transformer`、`XGBoost` 和 `AutoGluon` 等基于表格的预测器相结合。Ivanov 和 Prokhorenkova [171] 则联合训练了 `gradient boosted decision tree (GBDT)` 和 `GNN`。

近期的研究进展已将 `LLMs` 应用于表格数据任务，通常做法是将表格数据转换为适合 `LLM` 输入的序列化格式。然而，这种转换可能导致原始表格格式中固有的结构信息丢失。随着 `LLMs` 在图数据应用上的不断进步，未来可以利用表格图来支持和增强 `LLMs`，使其能够更有效地处理各类任务，从而克服序列化带来的结构信息损失问题。

## 8.5 Resources and Tools

### 8.5 资源与工具

本章节旨在系统性地梳理和介绍应用于 `tabular graphs` 的 `GraphRAG` 研究所需的关键数据资源和软件工具。这些资源对于评估、复现和推进 `GraphRAG` 模型在处理结构化表格数据方面的能力至关重要。

本节内容主要分为两个核心部分：

1.  **数据资源 (Data Sources)**：首先介绍了用于构建和评估 `tabular graphs` 的各类数据集。这些数据集通常源自现实世界的表格数据，如金融交易记录、医疗病历或企业客户关系管理系统。章节对这些资源进行了分类，依据包括应用领域、图的规模与复杂性，以及所支持的下游任务（如 `Node Classification`、`Link Prediction`）。通过提供标准化的基准数据集，研究人员可以更公平地比较不同 `GraphRAG` 方法的性能。

2.  **软件工具 (Tools)**：其次，章节详细讨论了支持 `GraphRAG` 在 `tabular graphs` 上实现和部署的开源工具与框架。这些工具链可大致分为几个层面：
*   **图构建工具**：用于将原始 `tabular` 数据高效转换为图结构（例如 `Heterogeneous Graph` 或 `Homogeneous Graph`）的库。
*   **`GNN` 基础框架**：介绍了主流的 `Graph Neural Networks (GNNs)` 库，如 PyTorch Geometric (PyG) 和 Deep Graph Library (DGL)。这些框架为实现如图注意力网络 (`GAT`) 或 `GraphSAGE` 等模型提供了核心算子和 `Message Passing` 机制，是构建 `GraphRAG` 中图编码器的基础。
*   **`GraphRAG` 集成平台**：探讨了专门用于或可轻松集成 `GraphRAG` 流程的工具。这些工具通常整合了图数据库、检索引擎和大型语言模型接口，简化了从数据准备到模型 `Pre-training`、`Fine-tuning` 和 `In-context Learning` 的完整研发流程。

总而言之，本章节的核心贡献在于为研究人员和开发者提供了一份全面的指南，汇集了在 `tabular graphs` 上实践 `GraphRAG` 的关键资源。通过利用这些标准化的数据集和高效的工具，可以显著加速算法的迭代、提高实验的可复现性，并推动 `GraphRAG` 技术在更多实际场景中的应用落地。

## 8.5.1 Data Resources

关系型机器学习的日益普及催生了多种针对表格数据的基准和数据集。

**RelBench** [339, 115] 是一个为关系型数据库上的机器学习任务设计的大规模、多样化的现实基准数据集集合。它包含多种任务类型，如节点级别的预测任务（例如，多类别分类、多标签分类、回归）、`Link prediction` 任务以及时序和静态预测任务。该基准包含多个数据集，如 `rel-amazon`、`rel-stack`、`rel-trial`、`rel-f1`、`rel-hm`、`rel-event` 和 `rel-avito`，为在多种关系数据场景和任务中评估模型提供了一个稳健的平台。

**TabGraphs** [23] 专注于在带有表格化节点特征的图上评估各类模型，包括简单基线模型、表格模型和 `GNNs`。该基准包含多个 `TabGraphs` 数据集，例如 `tolokers-tab`、`questions-tab`、`city-reviews`、`browser-games`、`hm-categories`、`hm-prices`、`city-roads-M`、`city-roads-L`、`avazu-devices`、`web-fraud` 和 `web-traffic`。

**Tabular-benchmark** [126] 是一个涵盖了来自不同领域的45个表格数据集的基准，它比较了多种基于树的模型和深度学习模型的性能。评估的任务包括数值分类、数值回归、类别分类和类别回归。

**Shwartz-Ziv and Armon** [363] 的研究 benchmark 了11个表格数据集，如 `MSLR` [325]、`Forest Cover Type`、`Higgs Boson` 和 `Year Prediction` [96]，评估了多种基于树的模型、深度学习模型和集成模型。

**DBInfer Benchmark** [417] 是一套用于衡量在多表存储数据上运行的机器学习解决方案的基准。它包括多个大规模关系型数据库（RDB）数据集，如 `AVS`、`OB`、`DN`、`RR`、`AB`、`SE`、`MAG` 和 `SE`，涵盖的任务包括留存率、CTR、购买、CVR、流失率、评分、流行度、场馆预测、引文、收费和预付预测。该基准提供了多种基线模型的实现，包括使用和不使用自动特征工程方法的流行表格模型以及 `Graph Neural Networks`，使其成为多表学习评估的强大资源。

**RTDL** (Research on Tabular Deep Learning) 是一个关于表格数据深度学习的论文和软件包集合，提供了多种流行的表格数据深度学习模型。

**OpenML** 是一个用于共享数据集、算法和实验的开放平台。它提供了跨多个领域的大量机器学习数据集，其中包括许多表格数据集。

**Kaggle** 托管了大量用于数据科学竞赛的数据集，使其成为在多样化的真实世界数据上对表格机器学习模型进行基准测试的宝贵资源。

**UC Irvine Machine Learning Repository** [96] 是一个由数据库、领域理论和数据生成器组成的集合，被机器学习社区广泛用于机器学习算法的实证分析。

**HiTab** [61] 是一个用于问答和自然语言生成任务的层次化表格数据集。

## 8.5.2 Tools

本小节列举了几个为数据准备、模型训练和评估提供核心功能的工具，这些工具可被有效应用于表格图（tabular graphs）上的GraphRAG。

*   **PyTorch Tabular [190]**：这是一个基于PyTorch的强大库，旨在简化深度学习技术在表格数据上的应用。它提供多种数据预处理功能，包括归一化、标准化、类别特征编码和数据加载器（data loader）准备。此外，它还集成了多样的表格机器学习模型和评估函数，是一个处理表格数据的综合性工具。
*   **DeepTables [179]**：这是一个易于使用的工具包，利用深度学习处理表格数据。它基于TensorFlow构建，旨在解决表格数据上的分类和回归任务，并提供了多种表格模型及对AutoML的支持。
*   **PyTorch Frame [156]**：这是PyTorch的一个深度学习扩展，专为包含数值、类别、时间、文本和图像等不同列类型的异构表格数据（heterogeneous tabular data）设计。它提供了广泛的表格模型，并支持与包括Large Language Models在内的多种模型架构进行集成。

## 9 Other Domains

# 9 其他领域
尽管 `GraphRAG` 的研究在先前讨论的领域中已得到广泛探讨，但在其他领域，如 infrastructure、biology 和 scene 等，`GraphRAG` 的研究仍显不足。因此，本章将这些领域合并为一个综合性章节，并仅关注这些领域中的关键研究。

## 9.1 Infrastructure Graph

基础设施图 (Infrastructure graphs) 由通过物理链路互连的 Points of Presence (PoPs) 定义，在电力、水、天然气、交通和通信等服务于我们日常活动的关键领域中扮演着至关重要的角色。鉴于针对基础设施图的 GraphRAG 研究尚属稀缺，本节的综述主要聚焦于图的构建方法和相关任务，并仅对该领域近期的 (Graph)RAG 应用进行简要概述。

-   **电力网络 (Power Networks)**：在此类网络中，节点代表发电厂、变电站、变压器和负荷点等关键实体，而边则对应于承载电能流动的输配电线路。节点特征包括发电容量、电压等级、负荷需求、地理位置和运行状态等，以捕捉网络的运营和空间特性。边的特征则包括传输容量、阻抗、长度、电压等级和实时潮流，这些对于分析线路性能和流动效率至关重要。这种基于图的表示方法支持一系列关键任务，如变压器故障诊断、停电预测、潮流近似计算和发电优化。

-   **水力网络 (Water Networks)**：节点是连接点（管道连接或用户）和源头（水库、水箱），边是输水管道。基本任务是在给定水网布局、管道特性、节点需求、水库水位和有限位置的水头测量值的情况下，估算所有节点的压力水头和所有管道的流量。

-   **天然气网络 (Gas Networks)**：节点代表连接点、气源、存储设施、压缩机站和用户，边代表承载用户负荷、分流和输入的天然气管道。

-   **交通网络 (Transportation Networks)**：交通网络建模方式多样。在**道路网络**中，交叉口作为节点，道路连接作为边，常用于为交通流量和速度预测建立空间依赖模型。类似地，**地铁和公交网络**使用站点作为节点，线路作为边，以捕捉站点拓扑。在**区域层面**，城市被划分为规则或不规则的区域作为图节点，其空间依赖性反映了土地利用模式。在**道路层面**，可通过传感器图、路段图、交叉口图和车道图来捕捉不同的道路元素。在**站点层面**，节点代表各种交通枢纽（地铁、公交、自行车或共享汽车站），通过地铁或道路等自然连接形成一个互联的空间依赖图。

-   **通信网络 (Communication Networks)**：计算机网络系统通常包含两个互连的图层：逻辑层和物理层。**逻辑层**代表数据流，节点是路由器，边是数据包遍历的逻辑路径。**物理层**则指底层基础设施，节点是服务提供商（如Comcast和Verizon）的 Points of Presence (PoPs)，边是它们之间的物理光纤链路。专注于逻辑层的研究常将网络建模为图，以捕捉网络的转发行为（流量交互）和连通性（拓扑行为）。例如，感知光纤拓扑的流量工程已被证明能有效缓解光纤中断和网络拥塞等问题。对于物理层，以往的研究多集中于推断完整的物理层结构，并实现物理层与逻辑层的对齐。

总而言之，基础设施网络上的任务可大致归纳为效用预测（如流量和节点性能）、流模拟与生成、脆弱性分析以及网络维护与运营。管理和理解这些图中复杂的物理关系对于在服务交付、功能预测和网络优化等关键领域改进基础设施管理至关重要。例如，在通信网络中，逻辑路由路径的状态直接受到底层物理光纤链路的影响，预测流量延迟等关键指标依赖于对所有相关光纤链路状态的评估。

基础设施图中错综复杂的物理连接为应用 GraphRAG 技术以增强基础设施管理和优化创造了宝贵的机会。尽管目前尚无研究在基础设施领域探索 GraphRAG，但已有少数工作利用了 RAG。Hussien等人 [168] 探索使用 RAG，通过从JAAD和PSI数据集中检索解释性文档，赋予自动驾驶车辆预测行人（如过马路）和驾驶员（如变道）行为的能力。此外，Qian等人 [323]、Wang等人 [418] 等利用生成模型在视觉和语言方面的最新进展，提议在计算机网络中运用 LLMs 的能力，并提出了一种系统性方法来为流量分类和生成等任务开发基础模型，该方法将数据包的十六进制字节视为 token。Kotaru [213] 介绍了一种“操作员副驾驶 (operator's copilot)”，这是一个利用 LLMs 进行高效数据检索的自然语言界面，可帮助管理数千个计数器和指标，从而减少对专家的依赖并通过数据智能加速问题解决。这些在计算机网络领域利用生成式AI的开创性工作，为构建面向基础设施网络的 (Graph)RAG 奠定了良好的基础。

## 9.2 Single-cell Graph

单细胞测序技术能够在单个细胞层面实现对分子特征的精细分析。例如，单细胞RNA测序（scRNA-seq）可以量化RNA转录水平，为细胞身份、发育阶段和功能特征提供宝贵信息；而scATAC-seq则记录每个开放染色质区域的读数，产生包含数十万个基因组区域的高维数据矩阵。随着单细胞数据量的激增，近年来涌现出多种深度学习方法用于单细胞分析，特别是GNN方法已被广泛应用于各类下游任务。

在细胞类型注释任务中，sigGCN利用STRING数据库构建了一个基因维度的加权邻接矩阵，以建立基因互作网络，其中节点特征代表相应的基因表达水平。该图被输入一个基于GCN的自编码器进行处理，最终完成细胞类型注释。scDeepSort则构建了一个加权二部图，其中细胞和基因均作为节点，边的权重代表每个细胞-基因对的基因表达值。基因节点的特征通过主成分分析（PCA）获得，而细胞节点的特征则通过聚合其连接的基因节点的加权特征得到。构建单细胞图最常见的方法是基于单细胞数据构建一个KNN图。具体流程为：首先对数据进行归一化处理；接着，使用PCA等降维方法在保留关键信息的同时降低数据集的高维度；然后，在这个低维空间中计算细胞间的距离（通常使用欧氏距离）；最后，确定每个细胞的K个最近邻居，并构建一个图，其中细胞为节点，边连接每个细胞与其K个最近邻居。

在多组学单细胞图方面，多组学单细胞技术在单细胞分辨率下整合了多个生物信息层面，如基因表达（RNA）、染色质可及性（ATAC）和蛋白质数据。Multiome技术可同时测量来自同个单细胞的多种分子模态（如RNA和ATAC），而CITE-seq则能同时测量单细胞的基因表达和表面蛋白标志物。以Multiome数据集为例，scMoGNN构建了一个包含细胞节点、基因节点和peak节点的`heterogeneous graph`。细胞节点与基因节点间的边表示该基因在细胞中的表达水平，细胞节点与peak节点间的边则反映了该peak在细胞中的表达水平。此外，还可以利用通路和基因活性等先验知识来建立基因节点之间以及peak与基因节点之间的连接。这种图表示方法能够捕捉模态内（intra-modality）和模态间（cross-modality）的关系，从而在单细胞水平上提供对调控动态的全面视图。

在空间转录组学单细胞图方面，与传统转录组学不同，空间转录组学保留了代表单个细胞或一小组细胞的spot在组织内的精确位置信息。空间转录组学主要包含三个关键数据源：基因表达、提供每个spot空间坐标的spot位置，以及提供组织视觉背景和形态的spot图像。在细胞类型反卷积任务中，GNNDeconvolver在构建KNN图时，综合了细胞位置信息和基因表达数据来计算细胞间的相似性。SpaOCN则额外整合了spot的形态学信息来计算相似度。将这三种数据源结合起来构建KNN图，能够提供对组织更丰富、更全面的视角，从而对细胞功能、相互作用和空间组织产生更深入的洞察。

## 9.3 Scene Graph

`Scene Graph`是一种旨在捕捉场景内对象之间空间和语义关系的数据结构，在计算机视觉、图形学和机器人学中被广泛用于组织场景，尤其是在处理多对象交互或复杂交互时。例如，`SceneGraphs` [147] 是一个用于视觉问答的数据集，包含10万个描述图像中对象、属性和关系的`Scene Graph`，它通过要求用户根据从`Scene Graph`派生的文本描述回答开放式问题，来测试模型的空间推理和多步推断能力。

`G-Retriever` [147] 处理`Scene Graph`的方法是：首先解析JSON数据以索引对象和属性，从而根据查询高效检索相关节点和边；接着，它构建一个包含必要场景信息的子图，并过滤掉无关细节；最后，`G-Retriever`利用这个子图和LLM来生成答案，借助图中的空间和语义关系进行精确的推理和响应生成。

`P-RAG` [477] 则通过智能体与环境互动，构建并更新一个指导其行动的历史轨迹数据库。在每次行动前，智能体捕捉反映当前状态的观测图像，并将其转换为`Scene Graph`格式以便于LLM处理。通过创建和检索`Scene Graph`上下文，`P-RAG`增强了LLM准确解释和导航复杂场景的能力，这种方法在规划具体的日常任务中尤其有效。

`Random Graph`是网络理论中的一个基础概念 [304, 174]，它基于概率规则构建，广泛用于计算机科学、物理学、生物学和社会科学等领域对复杂网络进行建模和研究。这些`Random Graph`可用于分析`GraphRAG`内部的检索、组织和生成过程。

生成`Random Graph`的模型有很多，例如`Erdős-Rényi Model (ER Model)` [100]、`Watts-Strogatz model` [436]、`Barabási-Albert model` [7]、`Random geometric graph` [33]、`scale-free networks` [18]和`stochastic block model` [150]。此外，还可以生成如`Path Graphs`、`Complete Graphs`、`Star Graphs`和`Barbell Graphs`等多种图结构以满足特定的分析需求。

`Random Graph`生成模型，如`Contextual stochastic block models (CSBM)` [80]，已被广泛用于`GNNs`分析 [19, 280, 285, 140]。同时，`Random Graph`也越来越多地被应用于检验LLM的行为。例如，Fatemi等人 [109] 利用`Erdős-Rényi`图、`scale-free networks`、`Barabási-Albert`模型、`stochastic block model`等多种生成器来测试LLM在各种图推理任务（如`edge existence`、`node degree`、`node/edge count`、`connected nodes`和`cycle check`）上的性能。`GraphLLM` [36] 通过生成不同输入格式的`Random Graph`来评估LLM在子结构计数、最大三元组求和、最短路径计算和二分图匹配等图推理任务上的表现，该方法使用一个`graph transformer`进行编码，并采用`embedding-fusion`方法进行生成。Bachmann和Nagarajan [13] 使用`star graphs`来研究`next-token prediction`范式内的局限性。其他研究，如Dai等人 [73]、Wang等人 [413]、Guo等人 [130]和Luo等人 [275]，也在各种任务中探索了LLM的图推理能力。

## 10 Challenges and Future Work

在提出了 `GraphRAG` 的整体框架并回顾其在各领域的应用之后，本章节旨在概述与 `GraphRAG` 各个关键组件相关的挑战与机遇，这些组件包括图构建 (`graph construction`)、检索器 (`retriever`)、组织器 (`organizer`) 和生成器 (`generator`)。随后，本章将进一步探讨 `GraphRAG` 作为一个整体系统，在评估与应用方面所面临的挑战和机遇。

## 10.1 Graph Construction

图的构建方法多种多样，不同的任务或领域需要不同的图结构。关键决策包括确定节点和边的粒度，以及选择提取哪些实体或关系。此过程还需解决实体消歧（entity disambiguation）、实体对齐（entity alignment）和共指消解（coreference resolution）等挑战。因此，理解何时需要图结构、是使用单个还是多个图，以及如何为特定应用以最合适的方式构建图，是至关重要且复杂的问题。

图的格式也是一个关键因素。图可以用多种形式表示，这些表示法是否等效，或者是否各自具有独特的优势，是一个需要考量的问题。为特定任务选择最有效的表示方法能显著影响最终性能。

对于`Multi-modal Graphs`，尽管许多图是基于文本构建的，但检索到的资源（如图像、音频或视频）可能是多模态的。从`multi-modal`数据中构建一个连贯的图是一项重大挑战，因为它要求在整合不同数据类型的同时，保留数据间有意义的关系。

此外，许多现实世界场景涉及随时间演变的动态数据，这对下游任务至关重要，因此需要构建`Dynamic graphs`。开发能够动态地构建、更新和存储图，同时保持高效率和有效性的策略，是另一个值得探索的挑战。

## 10.2 Retriever

### 10.2 Retriever

- **区分神经与符号知识**：图结构化数据通常涉及两种截然不同的知识类型：符号格式知识（symbolic-formatted knowledge），如知识图谱中的关系；以及神经格式知识（neural-formatted knowledge），如实体名称。开发能够区分这两种知识类型的技术，并为它们设计相应的`Retriever`策略，是值得进一步研究的方向。

- **内部与外部知识的协调**：由于`GraphRAG`通常在仅靠内部知识不足以解决任务时应用，因此使用稳健的校准方法评估内部与外部知识的重叠至关重要。此外，外部知识有时可能与内部知识相冲突。为应对此问题，必须设计一个有效的知识验证与和解机制，允许根据需要选择性地检索和更新外部内容。

- **准确性、多样性与新颖性之间的权衡**：现实世界中的用户检索通常涉及复杂的意图。除了提供准确内容以确保高效用（如实现高问答准确率）外，用户可能还对检索信息的多样性（diversity）和新颖性（novelty）有需求。如何在检索内容的准确性（accuracy）、多样性（diversity）和新颖性（novelty）之间取得平衡，仍然是一个开放性挑战。

- **过程中的推理、规划与思考**：一个现实世界中的`Retriever`可能需要根据初始查询和在检索过程中获取的内容，动态地、自适应地更新其检索过程。如何赋予`Retriever`这种自适应的思考、推理（reasoning）和规划（planning）能力，仍然是一个重大难题。

## 10.3Organizer

Organizer模块面临以下核心挑战：

*   **平衡完整性与简洁性**：检索到的图可能规模庞大，并包含大量与查询无关的信息。Organizer需要在信息的完整性与避免模型过载之间取得平衡。这要求采用技术修剪不相关的节点和边，同时保留必要的上下文，这在大型或嘈杂的图中尤其具有挑战性。此外，部分知识可能已被LLMs掌握，因此如何识别并移除这些冗余信息以提升效率，也是一个关键问题。

*   **最优数据结构化**：确定如何最有效地组织检索到的内容是一个挑战。例如，如何将结构化的图转换为生成器可以利用的格式，如何排列检索内容的顺序，以及如何为结构敏感型任务保留原始数据结构，这些都是重要的考虑因素。不同的任务可能需要不同的结构化方法。

*   **对齐不同来源的资源**：检索到的内容可能来自多种来源，并呈现为文本、图和图像等不同格式。如何有效地对齐这些不同来源和格式的组件以辅助生成器，是一个重大挑战，尤其是在整合多种数据模态时。

*   **数据增强**：在Organizer中整合数据增强技术，通过为检索到的图内容增加节点、边或特征，来提升模型的鲁棒性并改善下游任务的性能。然而，这一过程需要在真实数据与增强数据之间进行权衡，以避免引入不相关或冗余的信息。

## 10.4Generator

### 10.4 Generator

- **正确的提示格式 (Correct Format for Prompting)**：经过组织后检索到的内容格式差异巨大，例如文本、三元组或图，而当前的大语言模型（LLM）仅能处理文本输入。因此，探索针对特定任务能使LLM性能最优化的最有效格式，以及设计能够超越文本输入的更灵活的生成器，是值得研究的方向。

- **结构化编码 (Structural Encoding)**：当检索到的内容是子图（subgraph）且下游生成器是LLM时，确保LLM能够理解图的结构信息至关重要。设计有效的结构化编码并将其整合到token embeddings中是一项关键挑战。尽管已有研究将多种图编码（graph encodings）融入文本解码过程，但目前尚无系统性研究证明LLM是否能有效区分这些编码，并准确识别其对应的几何结构。

## 10.5 GraphRAG as a System

GraphRAG 并非各独立组件的集合，而是一个完整的系统。设计一个高效且内聚的 GraphRAG 系统带来了额外的挑战，主要体现在以下几个方面：

**系统级挑战**

*   **组件集成 (Integration Across Components):** 确保 Graph Construction、Retriever、Organizer 和 Generator 组件之间的无缝交互至关重要。各个部分必须协同工作以保持效率和准确性，而实现系统全局优化具有挑战性。
*   **可扩展性 (Scalability):** 随着数据量和查询需求的增长，GraphRAG 的每个组件都必须能高效处理更大、更复杂的图。这要求高效的图存储、优化的查询（如子图采样和路径查找）、对检索内容的流线化组织和快速响应的生成。此外，GraphRAG 的训练、服务、Fine-tuning 和评估需要基于现代硬件和软件栈的复杂工程支持，包括高效训练、数据高效的 Fine-tuning、通信高效算法、基于人类反馈的强化学习实现、GPU 加速、模型压缩和在线维护。
*   **可信赖性 (Trustworthiness):** GraphRAG 系统常用于教育、医疗和法律等高风险领域，因此除了优化效用外，还必须关注可靠性、鲁棒性、公平性和隐私等更广泛的目标。虽然已有工作开始探索 RAG 的多目标优化，但大多未专门研究 GraphRAG 捕获的关系信息可能引发的额外可信赖性与安全问题。

**可信赖性的关键维度**

1.  **可靠性 (Reliability):**
可靠性要求系统在不同场景下都能提供持续稳定的低错误率。在 RAG 中，不确定性量化面临两大挑战：一是 LLMs 生成阶段固有的概率性，可通过 Conformal Prediction 等技术进行校准；二是 Retriever 及其与 LLMs 交互过程中的不确定性。
与传统 RAG 不同，GraphRAG 的多跳 (multi-hop) 特性对多阶段不确定性量化提出了新要求。单步生成的错误率可能在多步推理后累积，如何从全局层面校准这种累积误差是关键挑战。已有工作 [305] 提出了 learn-then-test 框架来保证全局错误率，但这可能未考虑人机交互的不确定性，并增加了额外的计算开销。未来研究旨在开发能够整体量化和校准 (Graph)RAG 系统不确定性的方法。

2.  **鲁棒性 (Robustness):**
鲁棒性指系统在极端场景（如存在噪声和不相关内容）下保持同等质量响应的能力。现有研究表明，当检索内容包含噪声时，LLMs 的性能会显著下降。虽然一些研究通过对抗性训练来应对，但从结构角度对 LLMs 鲁棒性的探索有限。例如，当底层的推理图受到扰动时，LLM 的推理性能是否会改变？解决这些问题需要更深入地关注结构完整性与 GraphRAG 系统鲁棒性之间的相互作用，为需要复杂推理和规划的任务实现鲁棒性能铺平道路。

3.  **安全性 (Safety):**
LLMs 易受 prompt manipulation、hint injection 等多种对抗性攻击。结合了 LLMs 和外部数据库的 RAG 系统引入了独特的安全挑战。尽管已有工作针对 RAG 开发了威胁模型（如 adversarial passage injection）和防御策略，但它们都忽略了图结构数据固有的结构性漏洞。攻击者可以利用网络科学原理，通过策略性地攻击具有高 度数 或 中心性 等特定结构属性的节点，来最大化对系统行为的影响。这凸显了开发能够同时应对基于内容和基于结构的威胁的强大防御机制的必要性。

4.  **隐私 (Privacy):**
隐私在 RAG 系统中至关重要，尤其是在处理医疗、金融等敏感数据时。与传统 RAG 不同，GraphRAG 因图的关系性质引入了额外的隐私风险。例如，即使敏感节点受保护，也可能通过其邻居被间接检索。在表现出 homophily（连接的节点倾向于共享相似属性）的图中，敏感信息可从邻近节点推断出来。用于图编码的 GNNs 会加剧这些风险，其 message-passing 机制可能在特征传播过程中导致敏感信息泄露。应对这些挑战需要先进的、能考虑图互联特性的隐私保护技术，并将其贯穿从图构建到生成的整个 GraphRAG 流程。

5.  **可解释性 (Explainability):**
可解释性对于在高风险领域建立信任至关重要。与传统 RAG 相比，GraphRAG 通过图中节点之间编码的显式关系提供了更强的可解释性。例如，在 multi-hop question answering 任务中，GraphRAG 可以生成推理路径作为分步解释，让用户验证系统逻辑的正确性。在分子属性预测中，特定的子图可用于解释预测结果。然而，实现这种可解释性需要 GraphRAG 能够检索到合理且与上下文相关的子图，这仍然是一个挑战。确保解释忠实于底层模型逻辑，同时平衡全面性与简洁性，将是未来研究的关键。

## 10.6 Evaluation of GraphRAG.

评估GraphRAG系统的性能因其复杂的多组件性质而充满挑战。标准的基准测试无法完全捕捉基于图的构建、检索、组织和生成过程中的细微差别，因此，必须采用定制化的基准来评估每个组件及其对系统的整体影响。

*   **组件级最优性 (Component-Level Optimality)**：每个组件（如Graph Construction、Retriever、Organizer和Generator）的性能都直接影响GraphRAG系统的整体表现。评估这些组件需要根据其独特功能进行专门设计，可能涉及构建与其预期功能相符的不同数据集和评估指标。

*   **端到端基准 (End-to-End Benchmarks)**：为评估系统的整体有效性，全面的端到端基准至关重要。这些基准应评估生成输出的质量、系统响应时间、效率和资源利用率，从而提供GraphRAG在实际应用中性能的整体视图。

*   **特定任务与领域的评估 (Task and Domain-Specific Evaluation)**：不同的任务和领域对GraphRAG系统有独特要求，需要对各组件进行专门设计。在某一领域表现良好的方法可能无法有效泛化到其他领域，这凸显了多样化基准的必要性。此外，多任务和多领域评估有助于确定系统的适应性及其在不同情境下的有效性。

*   **可信度基准 (Trustworthiness benchmark)**：确保GraphRAG系统的可信度至关重要，尤其是在决策高度依赖准确、无偏信息的应用中。可信度基准应评估系统在对抗性输入下的鲁棒性、数据隐私保护以及答案推导过程的透明度，以确保输出是可解释且可靠的。

## 10.7 New Applications

尽管GraphRAG已在多个领域和任务中展现其应用价值，但仍有许多领域可以利用该技术，例如代码生成和强大的网络防御。将GraphRAG的应用扩展到其他领域前景广阔，但也带来了独特的挑战。为了有效地将GraphRAG适配于新领域，关键在于理解每个应用领域特有的需求、数据结构和图配置。因此，为不同领域制定量身定制的数据构建、检索、组织和生成策略，对于最大化GraphRAG的适应性和有效性至关重要。

## 11 Conclusion

本综述首先介绍了`GraphRAG`的需求与基本原理，强调了其通过整合图结构化信息来增强检索增强生成（retrieval-augmented generation）的能力。随后，我们将现有的`GraphRAG`方法架构统一为一个整体框架，该框架包含五个关键组件：graph construction、retriever、organizer、generator 和 data source，并对每个组件的代表性技术进行了回顾。考虑到图结构的多样性及其在不同领域的应用，我们还探讨了针对特定领域定制的`GraphRAG`设计。通过回顾`GraphRAG`在从`knowledge graphs`、文档图到科学图和社交图等不同领域的应用，本综述展示了其灵活性如何满足独特需求并解决广泛的任务。最后，我们讨论了有望推动`GraphRAG`发展的挑战与机遇。

---

## 统计信息

- **总处理块数**: 90
- **原始总token数**: 34,378
- **总结总token数**: 2,942
- **整体压缩比**: 8.56%
- **平均压缩比**: 47.88%
- **处理章节数**: 90


*此文档由MinerU内容总结器V2自动生成，基于Langchain Markdown分割技术。*