# A Survey of Large Language Models for Graphs (标准版) - 中文总结 (70%)

## 生成信息
- **压缩级别**: 70%
- **生成时间**: 2025-08-10 09:42:53
- **工具**: MinerU内容总结器 V2
- **原始块数**: 20
- **处理章节数**: 20
- **压缩比**: 12.76%

## 目录
- [A Survey of Large Language Models for Graphs](#a-survey-of-large-language-models-for-graphs)
- [ABSTRACT](#abstract)
- [CCS CONCEPTS](#ccs-concepts)
- [KEYWORDS](#keywords)
- [ACM Reference Format:](#acm-reference-format)
- [1 INTRODUCTION](#1-introduction)
- [2 PRELIMINARIES AND TAXONOMY](#2-preliminaries-and-taxonomy)
- [2.1 Definitions](#21-definitions)
- [2.2 Taxonomy](#22-taxonomy)
- [3 LARGE LANGUAGE MODELS FOR GRAPHS](#3-large-language-models-for-graphs)
- [3.1 GNNs as Prefix](#31-gnns-as-prefix)
- [3.2 LLMs as Prefix](#32-llms-as-prefix)
- [3.3 LLMs-Graphs Integration](#33-llms-graphs-integration)
- [3.4 LLMs-Only](#34-llms-only)
- [4 FUTURE DIRECTIONS](#4-future-directions)
- [4.1 LLMs for Multi-modal Graphs](#41-llms-for-multi-modal-graphs)
- [4.2 Efficiency and Less Computational Cost](#42-efficiency-and-less-computational-cost)
- [4.3 Tackling Different Graph Tasks](#43-tackling-different-graph-tasks)
- [4.4 User-Centric Agents on Graphs](#44-user-centric-agents-on-graphs)
- [5 CONCLUSION](#5-conclusion)

## A Survey of Large Language Models for Graphs

这篇综述系统性地探讨了大型语言模型（Large Language Models, LLMs）在图（Graph）数据分析领域的应用。文章旨在全面梳理将LLMs的强大能力与图结构数据相结合的前沿研究，为该交叉领域提供一个清晰的分类框架、方法论总结和未来方向展望。

**核心论点与贡献：**

该综述的核心贡献在于构建了一个分类体系，将现有“LLMs for Graphs”的研究范式分为两大类：
1.  **将LLM作为增强模块赋能图学习：** 这种范式主要利用LLM强大的文本理解和表征能力来提升传统的图学习模型，特别是`Graph Neural Networks (GNNs)`。具体方法包括使用LLM为图中的节点或边生成高质量的初始`Node Embedding`，尤其是在富文本图（text-rich graphs）中，LLM可以捕捉到传统方法难以获取的深层语义信息。这增强了`GNNs`（如`GCN`, `GAT`, `GraphSAGE`）在`Node Classification`和`Link Prediction`等任务上的表现。
2.  **将LLM作为核心处理单元直接处理图数据：** 这种范式探索将图结构本身转化为LLM能够理解的序列格式，从而直接利用`Transformer`架构进行端到端的图任务处理。这通常涉及“图序列化”（graph serialization）技术，将图的拓扑结构和节点/边特征编码为文本序列。通过这种方式，LLM可以直接执行`Graph Classification`、`Graph Generation`等复杂任务，并展现出强大的`Zero-shot Learning`和`Few-shot Learning`能力。这种方法有望催生通用的`Graph Foundation Models (GFMs)`。

**主要方法与技术：**

文章详细阐述了实现上述两种范式的具体技术路径：
*   **在增强GNN方面：** 重点讨论了如何通过`Pre-training`和`Fine-tuning`策略将LLM与`GNN`的`Message Passing`机制相结合。例如，通过`Contrastive Learning`对齐LLM生成的语义空间和`GNN`学习到的结构空间，实现多模态信息的有效融合。
*   **在LLM直接处理图方面：** 综述了多种图序列化方案，以及如何设计`prompt`和利用`In-context Learning`来引导LLM理解图任务。文章还探讨了如何将`Knowledge Graph`中的结构化知识注入LLM，以缓解模型幻觉并增强其推理能力。
*   **模型架构：** 讨论了从经典的`GNN`架构到以`Transformer`为核心的新型图模型架构的演变，并分析了它们在处理不同类型图（如`Homogeneous Graph`, `Heterogeneous Graph`）时的优缺点。

**关键结果与未来展望：**

该综述总结了现有研究在多个基准测试上的表现，指出LLM的引入显著提升了图学习任务的性能，尤其是在需要深度语义理解和跨领域知识迁移的场景中。

最后，文章指出了该领域面临的主要挑战和未来研究方向：
*   **可扩展性：** 如何将LLM应用于拥有数十亿节点和边的超大规模图。
*   **效率：** `Transformer`模型在处理长序列（序列化的图）时面临的计算瓶颈。
*   **鲁棒性：** 模型对图结构噪声和对抗性攻击的敏感性。
*   **前沿方向：** 探索`Multi-modal Learning`（结合图像、文本和图结构）、`Cross-domain Transfer`以及更有效的`Graph Pooling`和`Graph Generation`策略，是推动`Graph Foundation Models (GFMs)`发展的关键。

## ABSTRACT

图（Graphs）是表示现实世界关系的重要数据结构。以往研究表明，`Graph Neural Networks` (`GNNs`) 在如图`link prediction`和`node classification`等以图为中心的任务中取得了显著成果。然而，数据稀疏性和泛化能力有限等挑战依然存在。近年来，`Large Language Models` (`LLMs`) 因其卓越的语言理解和总结能力在自然语言处理领域备受关注。将`LLMs`与图学习技术相结合以提升图学习任务性能的方法已引起广泛兴趣。

本综述深入回顾了应用于图学习领域的最新`LLMs`技术，并提出了一种基于框架设计的新颖分类法来归纳现有方法。我们详细阐述了四种独特的设计：i) `GNNs as Prefix`，ii) `LLMs as Prefix`，iii) `LLMs-Graphs Integration`，以及 iv) `LLMs-Only`，并重点介绍了每个类别下的关键方法论。我们探讨了每种框架的优势与局限，并强调了未来的潜在研究方向，包括克服当前`LLMs`与图学习技术集成的挑战以及开拓新的应用领域。本综述旨在为希望在图学习中利用`LLMs`的研究人员和从业者提供宝贵资源，并激励该领域的持续进步。我们通过以下链接持续维护相关的开源资料：https://github.com/HKUDS/Awesome-LLM4Graph-Papers。

## CCS CONCEPTS

根据CCS概念分类，本文属于一篇综述与概述（Surveys and overviews）类型的研究。其内容横跨多个领域，主要涉及信息系统（Information systems）学科下的数据挖掘（Data mining）与语言模型（Language models），并深入探讨了计算数学（Mathematics of computing）范畴内的图算法（Graph algorithms）。

## KEYWORDS

该学术文本的核心关键词为`Large Language Models`与`Graph Learning`。这表明研究的核心聚焦于这两个前沿领域的交叉与融合。其主要内容可能探讨如何利用`Large Language Models`的强大语义理解和生成能力来增强`Graph Learning`任务，例如通过`Large Language Models`生成更丰富的节点特征或辅助理解图结构。同时，研究也可能反向探索如何运用`Graph Learning`技术，如图结构数据和`Graph Neural Networks (GNNs)`，来提升`Large Language Models`的性能，特别是在处理和推理包含复杂关系和结构化知识的任务中。

## ACM Reference Format:

该文献是 Xubin Ren、Jiabin Tang、Dawei Yin、Nitesh Chawla 和 Chao Huang 于2024年发表的一篇题为《A Survey of Large Language Models for Graphs》的综述文章。该文发表于《第30届 ACM SIGKDD 知识发现与数据挖掘会议论文集》（KDD '24），会议于2024年8月25日至29日在西班牙巴塞罗那举行。文章由 ACM 在西班牙巴塞罗那出版，共11页，其数字对象标识符（DOI）为 https://doi.org/10.1145/3637528.3671460。

## 1 INTRODUCTION

图（Graphs）由表示关系的节点和边组成，对于描绘社会网络、分子图、推荐系统和学术网络等不同领域的现实世界连接至关重要。这种结构化数据形式在映射各种应用中的复杂相互关系方面不可或缺。

近年来，Graph Neural Networks (GNNs) 已成为处理节点分类和链接预测等多种任务的强大工具。通过在节点间传递和聚合信息，并利用监督学习迭代地优化节点特征，GNNs 在捕捉结构细微差别和提升模型准确性方面取得了显著成果。为实现这一目标，GNNs 利用图标签来指导学习过程。文献中提出了多种著名模型，例如，Graph Convolutional Networks (GCNs) 能有效地在节点间传播嵌入；Graph Attention Networks (GATs) 利用注意力机制对节点特征进行精确聚合；而 Graph Transformers 则使用 self-attention 和位置编码来捕捉图中的全局信号，进一步增强了 GNNs 的表达能力。为应对大图的可扩展性挑战，研究者提出了 Nodeformer 和 DIFFormer 等方法，它们采用高效的注意力机制和可微分池化技术，在保持高精度的同时降低了计算复杂性。尽管取得了这些进展，但现有的 GNNs 方法仍面临若干挑战，例如数据稀疏性问题依然严峻，尤其是在图结构不完整或存在噪声的情况下。此外，GNNs 对新图或未见节点的泛化能力仍是一个悬而未决的研究问题。

与此同时，在自然语言处理、计算机视觉和信息检索等多个研究领域，展现出强大泛化能力的 Large Language Models (LLMs) 已成为强大的工具。LLMs 的出现激发了图学习社区的浓厚兴趣，推动了关于利用 LLMs 提升图相关任务性能的探索。研究人员探索了多种方法来结合 LLMs 的优势进行图学习，催生了一批结合 LLMs 和 GNNs 的新方法。一个有前景的方向是开发能让 LLMs 理解图结构并有效响应查询的提示（prompts）。例如，InstructGLM 和 NLGraph 等方法设计了专门的提示，使 LLMs 能够对图数据进行推理并生成准确的响应。另一种方法是集成 GNNs，将图结构信息作为 tokens 输入给 LLMs，使其能更直接地理解图结构。例如，GraphGPT 和 GraphLLM 使用 GNNs 将图数据编码为 tokens，再送入 LLMs 进行处理。LLMs 和 GNNs 的这种协同作用不仅提升了任务性能，还展示了令人印象深刻的 zero-shot 泛化能力，使模型能够准确回答关于未见图或节点的问题。

本综述旨在系统性地回顾 Large Language Models (LLMs) 在图应用领域的进展，并探讨未来的研究方向。与以往根据 LLMs 角色进行分类或主要关注 LLMs 与 knowledge graphs 集成的综述不同，本文的工作重点在于模型框架设计，特别是推理和训练过程，以此来区分现有分类法。这一视角能让读者更深入地理解 LLMs 如何有效应对图相关的挑战。我们识别并讨论了四种不同的架构方法：i) GNNs as Prefix, ii) LLMs as Prefix, iii) LLMs-Graphs Integration, 和 iv) LLMs-Only，并为每种方法提供了代表性示例。

本工作的贡献可总结如下：
*   **对用于图学习的 LLMs 进行全面综述**：我们全面回顾了当前最先进的用于图学习的 Large Language Models (LLMs)，阐明了它们的优势并指出了其局限性。
*   **提出新颖的研究分类法**：我们引入了一种基于框架设计的新颖分类法来归类现有研究，这为如何将 LLMs 与图学习无缝集成提供了更深刻的见解。
*   **探索未来研究方向**：我们还探讨了未来的潜在研究途径，包括解决在融合 LLMs 与图学习方法中普遍存在的挑战，以及开拓新的应用领域。

## 2 PRELIMINARIES AND TAXONOMY

本章节首先提供了关于large language models和图学习（graph learning）的基础背景知识。随后，在此基础上，提出了一个针对应用于图的large language models的分类体系（taxonomy）。

## 2.1 Definitions

**图结构化数据 (Graph-Structured Data)**。图 $\mathcal{G} = (\mathcal{V},\mathcal{E})$ 是一种非线性数据结构，由节点集 $\mathcal{V}$ 和连接这些节点的边集 $\mathcal{E}$ 组成。每条边 $e\in \mathcal{E}$ 关联一对节点 $(u,v)$。边可以是表示从 $u$ 到 $v$ 方向的“有向边”，也可以是无方向的“无向边”。此外，文本属性图 (Text-Attributed Graph, TAG) 是一种为每个节点分配序列化文本特征（如句子）的图，该特征记为 $\mathbf{t}_0$。在大型语言模型时代，TAG 被广泛使用，其形式化表示为 $\mathcal{G}_S = (\mathcal{V},\mathcal{E},\mathcal{T})$，其中 $\mathcal{T}$ 是文本特征集。

**图神经网络 (Graph Neural Networks, GNNs)** 是针对图结构化数据的深度学习架构，它通过聚合邻居节点的信息来更新节点嵌入 (node embeddings)。在形式上，每个 GNN 层中节点嵌入 $\mathbf{h}_v\in \mathbb{R}^d$ 的更新过程可表示为：
$$
\mathbf{h}_v^{(l + 1)} = \psi (\phi (\{\mathbf{h}_v^{(l)}:v'\in \mathcal{N}(v)\}),\mathbf{h}_v^{(l)}), \tag{1}
$$
其中 $v'\in \mathcal{N}(v)$ 表示节点 $v$ 的一个邻居节点，$\phi(\cdot)$ 和 $\psi(\cdot)$ 分别是聚合函数和更新函数。通过堆叠 $L$ 个 GNN 层，最终的 node embeddings 可用于如图分类 (node classification) 和链接预测 (link prediction) 等下游图相关任务。

**大型语言模型 (Large Language Models, LLMs)**。Language Models (LMs) 是一种估计给定句子中词汇概率分布的统计模型。当 LMs 拥有数十亿参数并在多种自然语言任务（如翻译、摘要和指令遵循）中展现出卓越性能时，它们被称为 LLMs。通常，最新的 LLMs 大多基于 Transformer blocks 构建，使用一种基于 query-key-value (QKV) 的注意力机制来聚合序列中 tokens 的信息。根据注意力方向的不同，LLMs 可分为两类：

**掩码语言建模 (Masked Language Modeling, MLM)**。这是一种流行的 LLMs pre-training 目标，其过程是掩盖序列中的某些 tokens，并训练模型根据周围的上下文来预测这些被掩盖的 tokens。具体来说，模型会同时考虑被掩盖 token 的左右两侧上下文进行预测：
$$
p(x_i|x_0,x_1,\dots,x_n). \tag{2}
$$
代表性模型包括 BERT 和 RoBERTa。

**因果语言建模 (Causal Language Modeling, CLM)**。这是另一种流行的 LLMs 训练目标，其过程是根据前面的 tokens 来预测序列中的下一个 token。具体来说，模型只考虑当前 token 的左侧上下文进行预测：
$$
p(x_i|x_0,x_1,\dots,x_{i - 1}) \tag{3}
$$
著名示例包括 GPT 系列（如 ChatGPT）和 Llama。

## 2.2 Taxonomy

本综述提出了一个分类法，其核心是处理图数据与文本的LLM模型推理流程。该分类法总结了四种主要的、面向图数据的大语言模型（LLM）架构设计，具体如下：

![](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/6e336fc9fe033b1c2cd2ac487249eccc7cbc7634d69828114326fd4e92cb36a8_5762487d.jpg)
图1：所提出的面向图数据的LLM分类法，并列举了代表性工作。

- **GNNs as Prefix**：在此架构中，Graph Neural Networks (GNNs) 作为首要组件，负责处理图数据，并为LLM的后续推理提供具备结构感知能力的tokens（如节点级、边级或图级tokens）。

- **LLMs as Prefix**：此架构由LLM率先处理包含文本信息的图数据，进而生成node embeddings或标签，用以优化Graph Neural Networks的训练效果。

- **LLMs-Graphs Integration**：这类方法旨在实现LLM与图数据更高层次的集成。具体方式包括与GNNs进行融合训练或对齐，以及构建基于LLM的智能体（agent）来与图信息进行交互。

- **LLMs-Only**：该路线专注于设计实用的prompting方法，将图结构数据转化为词语序列，以便LLM直接进行推理。部分研究也在此基础上融合了multi-modal tokens。

## 3 LARGE LANGUAGE MODELS FOR GRAPHS

### 第3章：面向图数据的大语言模型 (LARGE LANGUAGE MODELS FOR GRAPHS)

本章系统性地探讨了将大语言模型 (Large Language Models, LLMs) 应用于图结构化数据的研究前沿。随着LLMs在自然语言处理领域取得巨大成功，研究者们开始探索其在图学习领域的潜力，旨在克服传统`Graph Neural Networks (GNNs)`在语义理解、跨领域泛化和零样本学习等方面的局限性。本章的核心贡献在于梳理并总结了LLMs与图学习结合的三种主要范式，分析了其在各类图任务上的应用，并指出了当前面临的挑战与未来发展方向。

#### **核心方法论：LLMs与图的集成范式**

LLMs与图的结合主要遵循三种技术路径，它们在模型架构和任务处理方式上存在显著差异。

1.  **LLM作为图学习的增强器 (LLM as an Enhancer for Graph Learning)**：
此范式主要利用LLMs强大的文本编码能力来处理图中的文本信息。在许多现实世界的图中，如社交网络、引文网络或`Knowledge Graph`，节点和边通常包含丰富的文本属性。传统方法通常使用简单的词袋模型或预训练词向量，难以捕捉深层语义。该方法通过以下步骤增强`GNNs`：
*   **特征工程**: 使用预训练的LLM（如BERT）对每个节点或边的文本描述进行编码，生成高质量的语义`Node Embedding`。
*   **GNNs集成**: 将LLM生成的语义向量作为`GNNs`（如`GCN`, `GAT`, `GraphSAGE`）的初始节点特征输入。随后，`GNNs`通过`Message Passing`机制聚合邻域的结构信息和增强后的语义信息。
*   **优势**: 这种方法显著提升了在富文本图上执行`Node Classification`和`Link Prediction`等任务的性能，因为它结合了LLMs的语义理解能力和`GNNs`的结构推理能力。

2.  **GNN作为LLM的增强器 (GNN as an Enhancer for LLM)**：
该范式反其道而行之，利用图的结构化信息来增强LLMs的性能，尤其是在需要结构化知识和逻辑推理的任务中。
*   **知识注入**: `GNNs`首先在大型`Knowledge Graph`上进行学习，捕捉实体间的复杂关系。
*   **LLM增强**: GNN学习到的图结构知识以多种方式注入LLM，例如作为额外的上下文、指导LLM的注意力机制，或在生成文本时约束其输出空间。这有助于缓解LLM的“幻觉”问题，提高其在知识问答、事实核查等任务中的准确性。

3.  **统一的图语言模型框架 (Unified Graph-Language Frameworks)**：
这是当前最具前瞻性的研究方向，旨在构建能够直接处理和理解图数据的`Graph Foundation Models (GFMs)`。其核心思想是将图结构“翻译”成LLM能够理解的序列格式。
*   **图的序列化 (Graph Serialization)**: 这是关键步骤，通过特定算法（如基于广度/深度优先搜索的节点遍历、邻接表线性化等）将图的拓扑结构和节点特征转换为文本序列。这个过程需要尽可能保留图的关键信息，以避免`Graph Isomorphism`问题带来的信息损失。
*   **模型架构**: 通常采用`Transformer`架构。序列化后的图数据被视为一种特殊的“语言”，模型在此基础上进行`Pre-training`。
*   **训练与应用**: 模型通常在海量无标签图数据上进行`Self-supervised Learning`，学习目标包括掩码节点/边预测、`Contrastive Learning`等。完成`Pre-training`后，模型可以通过`Fine-tuning`适应下游任务，或直接通过`In-context Learning`进行`Zero-shot`或`Few-shot`推理。下图展示了这种统一框架的典型架构。
![](./images/llm_graph_framework.jpg)

#### **主要应用与任务**

LLMs for Graphs在多种传统和新兴的图任务上展现了巨大潜力：

*   **传统图任务**:
*   `Node Classification`: 通过更丰富的语义特征或直接对序列化的图进行端到端分类，模型表现出色。
*   `Link Prediction`: 模型能够基于节点的深层语义和全局图结构来预测边的存在。
*   `Graph Classification`: 将整个图序列化后输入`Transformer`，利用其全局感受野进行分类，尤其适用于分子属性预测等场景。

*   **新兴的生成式与跨模态任务**:
*   `Graph Generation`: LLM可以根据文本描述生成符合特定结构和属性的图，例如根据化学分子名称生成其分子图。
*   **图文转换**: 包括`Graph-to-Text`（为图生成自然语言描述，即图描述）和`Text-to-Graph`（从文本中解析并构建图结构）。

#### **挑战与未来展望**

尽管LLMs for Graphs取得了显著进展，但仍面临诸多挑战：

1.  **结构信息损失**: 图的序列化过程不可避免地会损失部分高维拓扑信息，如何设计保真度更高的序列化方案是核心难题。
2.  **可扩展性与计算成本**: LLMs的`Transformer`架构对输入序列长度敏感，处理大规模图（百万级节点）时面临巨大的计算和内存瓶颈。
3.  **处理复杂图结构**: 当前方法主要集中在`Homogeneous Graph`，对于`Heterogeneous Graph`和动态图的处理仍不成熟。

未来的研究方向将聚焦于：
*   开发更高效的图序列化和`Graph Pooling`技术，以应对大规模图。
*   探索`Multi-modal Learning`，将图、文本、图像等多种信息源融合到统一模型中。
*   推动`Cross-domain Transfer`和`Domain Adaptation`，构建能够泛化到不同领域图数据的通用`Graph Foundation Models (GFMs)`。
*   研究专门为图结构设计的`Transformer`变体，使其能更原生、更高效地处理图数据，而非仅仅依赖文本序列化。

## 3.1 GNNs as Prefix

本节探讨了将Graph Neural Networks (GNNs)作为结构编码器（即GNNs as Prefix）的应用，旨在增强大型语言模型（LLMs）对图结构的理解，以支持各类下游任务。在此类方法中，GNNs通常扮演tokenizer的角色，将图数据编码为富含结构信息的graph token序列，再输入LLMs与自然语言进行对齐。这些方法主要分为两类：i) Node-level Tokenization，将图的每个节点作为输入，使LLM能理解细粒度的节点级结构信息；ii) Graph-level Tokenization，通过pooling方法将整个图压缩为固定长度的token序列，以捕获图结构的高层全局语义。

### 3.1.1 Node-level Tokenization
对于node classification和link prediction等需要模型建模细粒度节点级结构信息并区分不同节点语义的下游任务，Node-level Tokenization方法能够最大程度地保留每个节点的独有结构表示。

该领域的研究包括：
*   **GraphGPT [63]** 提出通过文本-图对齐来初步校准图编码器与自然语言语义，然后利用一个projector将训练好的图编码器与LLM结合。通过两阶段指令调优范式，模型能直接用自然语言完成多种图学习任务，展现出强大的zero-shot迁移能力和多任务兼容性。其提出的Chain-of-Thought蒸馏方法使GraphGPT能以较小的参数规模迁移至复杂任务。
*   **HiGPT [64]** 提出将语言增强的in-context heterogeneous graph tokenizer与LLMs结合，解决了不同heterogeneous graph之间关系类型异构性转变的挑战。同时，两阶段的heterogeneous graph指令调优向LLM注入了同构性和异构性感知。结合多种prompt engineering的Mixture-of-Thought (MoT)方法进一步解决了heterogeneous graph学习中常见的数据稀缺问题。
*   **GIMLET [92]** 作为一个统一的图-文模型，利用自然语言指令来应对分子相关任务中标签不足的挑战，有效缓解了对昂贵实验数据标注的依赖。它采用广义位置嵌入和注意力机制，将图结构和文本指令编码为统一的token组合，并输入到一个transformer decoder中。
*   **GraphTranslator [88]** 提出使用带有共享self-attention的translator来对齐目标节点和指令，并采用cross-attention将图模型编码的节点表示映射到定长的语义token。其双阶段训练范式使LLM能基于语言指令进行预测，为预定义和开放式图任务提供了统一的解决方案。
*   **UniGraph [25]** 并未使用维度各异的预计算节点特征，而是利用Text-Attributed Graphs来统一节点表示，其核心是一个由语言模型和GNNs组成的级联骨干网络。
![](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/8c95e2c7069981ee9f7171f8c1fcc4642fade863c373d295556f0c90cc7ab877_392ff0f6.jpg)
图2: GNNs as Prefix.
*   在推荐系统研究中，**XRec [51]** 将GNN编码的用户/项目嵌入作为协作信号，并将其整合到LLM的每一层中，从而使模型即使在zero-shot场景下也能为推荐生成解释。

### 3.1.2 Graph-level Tokenization
另一方面，为适应graph-level任务，模型需要能够从节点表示中提取全局信息，以获得高层的图语义token。在GNN as Prefix方法中，Graph-level tokenization通过各种“pooling”操作将节点表示抽象为统一的图表示，从而增强各类下游任务。

该领域的研究包括：
*   **GraphLLM [5]** 利用一个包含可学习query和位置编码的graph transformer来编码图结构，并通过pooling获得图表示。这些表示直接作为graph-enhanced prefix用于LLM的prefix tuning，在基础图推理任务中表现出显著效果。
*   **MolCA [48]** 通过提出的Cross-Modal Projector和Uni-Modal Adapter，以及双阶段预训练和微调，使语言模型能够理解基于文本和图的分子内容。它采用一个实现为Q-Former的cross-modal projector来连接图编码器的表示空间和语言模型的文本空间，并使用一个uni-modal adapter进行高效的下游任务适配。
*   **InstructMol [4]** 引入一个projector，将GNN编码的分子图与分子的序列信息及自然语言指令对齐，通过第一阶段的Alignment Pretraining和第二阶段的Task-specific Instruction Tuning，使模型在多种药物发现相关的分子任务中取得优异性能。
*   **GIT-Mol [45]** 通过不同模态编码器之间的interaction cross-attention进一步统一了图、文本和图像三种模态，并对这三种模态进行对齐，使模型能同时执行captioning、generation、recognition和prediction四种下游任务。
*   **GNP [65]** 采用cross-modality pooling来整合GNN编码的节点表示与自然语言token，形成一个统一的图表示。该表示通过LLM与指令对齐，在常识和生物医学推理任务中展现出优越性。
*   近期，**G-Retriever [24]** 利用retrieval-augmented技术获取子图结构，通过图编码器和LLMs的协作完成GraphQA（图问答）中的各种下游任务。

### 3.1.3 讨论
GNN as Prefix方法将GNNs的建模能力与LLMs的语义建模能力对齐，在多种图学习下游任务和实际应用中展现了前所未有的泛化能力，即zero-shot能力。然而，尽管上述方法取得了成效，但挑战在于GNN as Prefix方法对于新的text-attributed graphs是否依然有效。此外，如何最优化地协调GNNs和LLMs的架构与训练，仍然是一个有待解决的问题。

## 3.2 LLMs as Prefix

本节介绍的方法利用大型语言模型（LLM）生成的信息来改进图神经网络（GNN）的训练。这些信息包括文本内容、标签或由LLM派生的嵌入。这些技术可分为两类：i) 将LLM生成的嵌入用于GNN，ii) 将LLM生成的标签用于GNN。

### 3.2.1 来自LLM的嵌入用于GNN
GNN的推理过程涉及通过边传递节点嵌入，然后聚合它们以获得下一层的节点嵌入。在此过程中，初始节点嵌入在不同领域中差异很大，例如推荐系统中的ID-based嵌入或引文网络中的词袋嵌入可能不清晰且缺乏多样性，导致GNN性能不佳。此外，由于缺乏通用的节点嵌入器设计，GNN在面对具有不同节点集的未见任务时其泛化能力受到挑战。为此，该领域的研究工作利用LLM强大的语言总结和建模能力，为GNN的训练生成有意义且有效的嵌入。

具体方法包括：
- **G-Prompt**：在预训练语言模型（PLM）的末端添加一个GNN层，以实现图感知的填充掩码（fill-masking）自监督学习。通过这种方式，G-Prompt能够利用prompt tuning为下游任务生成任务特定的、可解释的node embeddings。
- **SimTeG**：首先对LLM获得的文本嵌入进行参数高效的fine-tuning，以适应下游任务（如节点分类），然后将这些node embeddings输入GNN进行推理。
- **GALM**：利用BERT作为预语言模型来编码每个节点的文本嵌入。然后，通过link prediction等无监督学习任务对模型进行预训练，以最小化经验损失并找到最优模型参数，使GALM能够应用于各种下游任务。
- **OFA**：利用LLM将来自不同领域的图数据统一到一个共同的嵌入空间中，以进行cross-domain learning。它还使用LLM编码与任务相关的文本描述来构建提示图（prompt graphs），使模型能根据上下文执行特定任务。
- **TAPE**：使用定制的prompts查询LLM，为每个节点生成预测和文本解释。然后，fine-tune DeBERTa模型将文本解释转换为node embeddings供GNN使用。最终，GNN可以结合原始文本特征、解释特征和预测特征来预测节点标签。

![](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/eac4d994dcf3df02a468513c81e679d17ce565d8c51d49bbcaf3b90634119a64_fe829c4e.jpg)
图3展示了将LLM用作前缀（Prefix）的模式。

在推荐系统领域，**LLMRec**利用GPT-3.5对用户-物品交互数据进行图增强，不仅过滤了噪声交互并增加了有意义的训练数据，还通过生成的丰富文本简介充实了用户和物品的初始node embeddings，最终提升了推荐器的性能。

### 3.2.2 来自LLM的标签用于GNN
另一种方法利用LLM生成的标签作为监督信号来改进GNN的训练。这里的监督标签不仅限于分类任务中的类别标签，还可以是嵌入、图等多种形式。LLM生成的信息不作为GNN的输入，而是构成用于更好优化的监督信号，使GNN能够在各种图相关任务上实现更高性能。

具体方法包括：
- **OpenGraph**：利用LLM生成节点和边，以缓解训练数据稀疏的问题。节点和边的生成过程通过Gibbs采样算法和一种“提示树”（tree-of-prompt）策略进行优化，生成的数据随后被用于训练graph foundation model。
- **LLM-GNN**：利用LLM作为标注器，生成带有置信度分数的节点类别预测，并将其作为标签。然后通过后置过滤筛选掉低质量的标注，同时保持标签的多样性。最后，使用这些生成的标签来训练GNN。
- **GraphEdit**：利用LLM构建一个边预测器，用于评估和修正候选边与原始图边的关系。
- **RLMRec**：在推荐系统中，利用LLM生成用户/物品偏好的文本描述。这些描述被编码为语义嵌入，通过contrastive learning和generative learning技术来指导ID-based推荐模型的表示学习。

### 3.2.3 讨论
尽管上述方法在提升图学习性能方面取得了进展，但它们普遍存在一个局限性，即其解耦（decoupled）的特性——LLM不与GNN共同训练，导致这是一个两阶段的学习过程。这种解耦通常是由于图的规模过大或LLM参数过多所带来的计算资源限制。因此，GNN的性能在很大程度上依赖于LLM预先生成的嵌入/标签的质量，甚至依赖于任务特定prompt的设计。

## 3.3 LLMs-Graphs Integration

本节旨在进一步整合大型语言模型（LLM）与图数据，涵盖了多种旨在增强LLM处理图任务能力以及优化GNN参数学习的方法。这些工作可分为三类：i) GNN与LLM的融合训练，旨在实现两种模型参数的融合协同训练；ii) GNN与LLM的对齐，专注于实现两种模型在表示或任务层面的对齐；iii) 面向图的LLM智能体（LLMs Agent for Graphs），即基于LLM构建自主智能体来规划和解决图任务。

### 3.3.1 GNN与LLM的对齐
GNN和LLM分别设计用于处理结构化数据和文本数据，导致它们的特征空间不同。为解决此问题，并使两种模态的数据能更好地促进GNN和LLM的学习，研究者采用`contrastive learning`或期望最大化（EM）迭代训练等技术来对齐两种模型的特征空间，从而更好地建模图与文本信息，提升多项任务的性能。

![](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/80bb9e9ac5b115eba23da952ecd1d4afd62bd30a7ee32d8d39c40fa9f22d5e86_b2a867d6.jpg)
图4: LLMs-Graphs Integration.

在此方向上，`MoMu`是一个多模态分子基础模型，它包含两个独立的编码器（一个用于分子图的GIN，一个用于文本的BERT），并使用`contrastive learning`在分子图-文本对数据集上进行预训练，使其能直接从文本描述中生成新分子。同样在生物信息领域，`Molecules IM`结合分子的化学结构（分子图）和文本描述（SMILES字符串），通过`contrastive learning`联合学习分子结构和文本表示，在结构-文本检索、基于文本的编辑和分子属性预测等多个基准测试中表现出色。`ConGraT`提出了一种对比式图文预训练技术，旨在同时对齐由LM和GNN编码的节点嵌入，在社交网络、引文网络和链接网络上的实验表明，其在节点与文本分类及链接预测任务上效果显著。`G2P2`通过提出三种不同类型的对齐（文本-节点、文本-摘要、节点-摘要）来增强基于图的对比预训练，从而在低资源环境下利用图结构中丰富的语义关系提升文本分类性能。`GRENADE`是一个以图为中心的语言模型，它提出图中心`contrastive learning`和知识对齐，以实现基于GNN和LM编码的节点嵌入在节点级别和邻域级别的对齐，使模型即使在没有人工标注的情况下也能通过`self-supervised learning`捕获文本语义和图结构信息。除了对比学习，`THLM`利用BERT和HGNNs编码节点嵌入，并通过带负采样的正负分类任务来改善两种不同模态嵌入的对齐效果。近期，`GLEM`采用了一个高效的变分期望最大化（variational expectation-maximization, EM）框架，通过让LM和GNN在节点分类任务中迭代地为对方提供标签，从而对齐它们在图任务上的能力。

### 3.3.2 GNN与LLM的融合训练
尽管GNN与LLM的表示对齐实现了两种模型的协同优化和嵌入层面对齐，但它们在推理时仍是分离的。为了实现LLM与GNN更深层次的集成，一些工作专注于设计更深度的模块架构融合，例如LLM中的`Transformer`层和GNN中的图神经层。协同训练GNN和LLM可以在图任务中为两个模块带来双赢的双向增益。

`GreaseLM`通过设计一个特定的前向传播层来整合`Transformer`层和GNN层，该层通过特殊的交互标记和交互节点实现LM和GNN之间的双向信息传递。这种方法使得语言上下文表示能够基于结构化的世界知识，同时细微的语言差异（如否定或修饰词）也能影响知识图谱的表示，使`GreaseLM`在问答任务上取得了高性能。`DGTL`提出`disentangled graph learning`，利用GNN编码解耦表示，然后将其注入到LLM的每个`Transformer`层中。这使得LLM能够感知图结构，并利用来自LLM的梯度来`fine-tune` GNN，从而在引文网络和电商图任务上取得优异表现。`ENGINE`在LLM的每一层增加了一个轻量级且可调的`G-Ladder`模块，该模块使用`message-passing`机制来整合结构信息。这使得每个LLM层的输出（即`token`级表示）能够传递给相应的`G-Ladder`，增强后的节点表示可用于节点分类等下游任务。更直接地，`GraphAdapter`使用一个融合模块（通常是多层感知机）将从GNN获得的结构表示与LLM的上下文隐藏状态（如编码后的节点文本）相结合。这使得来自GNN适配器的结构信息能够补充LLM的文本信息，生成一个可用于监督训练和下游任务`prompting`的融合表示。

### 3.3.3 面向图的LLM智能体
随着LLM在理解指令和自我规划以解决任务方面展现出强大能力，一个新兴的研究方向是构建基于LLM的自主智能体来处理人类赋予或与研究相关的任务。通常，一个智能体由记忆模块、感知模块和行动模块组成，以实现观察、记忆回忆和行动的循环来解决给定任务。在图领域，基于LLM的智能体可以直接与图数据交互，执行节点分类和链接预测等任务。

在该领域，`Pangu`开创性地使用LM来导航`Knowledge Graph`（KG）。其方法将智能体设计为一种符号图搜索算法，为语言模型提供一组潜在的搜索路径以评估给定查询，然后利用剩余路径检索答案。`Graph Agent (GA)`将图数据转换为文本描述并生成嵌入向量存入长期记忆。在推理时，`GA`从长期记忆中检索相似样本，并将其整合到一个结构化`prompt`中，供LLM解释节点分类或边连接的潜在原因。`FUXI`框架集成了定制工具和`ReAct`算法，使LLM能作为智能体主动与KG交互。通过利用基于工具的数据导航和探索，这些智能体执行链式推理，逐步构建答案，最终高效准确地解决复杂查询。`Readi`是另一种方法，它首先使用`in-context learning`和`chain-of-thought` `prompt`生成带有多重约束的推理路径，然后基于图数据进行实例化。实例化的推理路径被合并后作为LLM的输入以生成答案，该方法在KGQA和TableQA任务上取得了显著的性能提升。近期提出的`RoG`通过三步（规划、检索、推理）来回答图相关问题：首先根据问题的知识图谱结构信息生成一组关联路径；然后利用这些路径从KG中检索相应的推理路径；最后，利用检索到的推理路径，通过LLM生成问题的答案和解释。

### 3.3.4 讨论
LLM与图的整合在弥合结构化数据与文本数据之间的模态鸿沟以解决图相关任务方面取得了可喜的进展。通过结合LLM在语言理解上的优势和图捕捉实体间复杂关系的能力，我们可以在图数据上实现更准确、更灵活的推理。然而，尽管进展显著，该领域仍有提升空间。

![](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/806217f0e7cd5b0c681c7abb9d2c4af5d2bc138dbf416a32e2c36955e21b4580_1b9b9ab8.jpg)
图5: LLMs-Only.

主要挑战之一是**可扩展性**。在对齐和融合训练中，当前方法通常使用小型语言模型或固定LLM的参数，这限制了它们扩展到更大数据集的能力。因此，探索在`web-scale`图数据上用更大模型进行训练的方法至关重要，这将有助于在超大规模图上实现更精确高效的推理。

另一挑战是**图智能体与图数据交互的局限性**。当前图智能体的方法通常只进行一次规划和执行，这对于需要多次运行的复杂任务可能不是最优的。因此，有必要研究智能体与图数据进行多次交互的方法，根据图的反馈来优化其规划并提升性能。这将支持在图数据上进行更复杂的推理，并提高下游任务的准确性。

总而言之，LLM与图的整合是一个充满潜力的研究方向，对推动`graph learning`的发展具有重要意义。通过解决上述挑战并开发更先进的整合方法，我们可以在图数据上实现更精确、灵活的推理，并解锁在`knowledge graph reasoning`、分子建模和社交网络分析等领域的新应用。

## 3.4 LLMs-Only

`LLMs-Only`方法旨在让大型语言模型（LLMs）直接接收并理解图结构信息，并结合这些信息执行下游任务。该方法主要分为两大类：`Tuning-free`方法通过设计专门的prompt，使预训练LLMs能够直接处理图任务；`Tuning-required`方法则将图转换为特定序列，并通过fine-tuning对齐图token序列与自然语言token序列。

### 3.4.1 Tuning-free
`Tuning-free`方法的核心挑战在于如何用自然语言有效构建图，并确保LLMs能准确理解其语言学表示的结构。这类方法在纯文本空间中对图进行建模和推理，以探索预训练LLM的结构理解潜力。

多个研究项目共同探索了LLMs在理解和推理图数据方面的能力。`NLGraph`提出了一个用于图问题求解的基准测试，并引入了基于指令的方法。`GPT4Graph`和`Beyond Text`则深入研究了LLM对图结构的理解能力，并强调了提升其图处理能力的必要性。`Graph-LLM`聚焦于node classification任务，通过`LLMs-as-Enhancers`和`LLMs-as-Predictors`两种流程，利用LLM的常识知识和语义理解能力。同时，`GraphText`通过生成图语法树，将图翻译为自然语言，实现了无需训练的交互式图推理。`Talk like a Graph`深入研究了用于LLMs的文本图编码器功能，并提出`GraphQA`基准来系统评估编码策略对模型性能的影响。针对动态图，`LLM4DyG`引入了评估时空理解的任务，并提出了`Disentangled Spatial/Temporal Thoughts (DST2)`提示技术以提升性能。

为了融合多模态信息，`GraphTMI`提出了一种创新方法，将文本、图像和motif等多种模态与图数据结合，并推出了`GraphTMI`基准。研究发现，图像模态在平衡token限制和保留关键信息方面优于文本和传统的GNNs。`Ai et al.` [2] 则利用图像编码和`GPT-4V`的先进能力，构建了一个多模态图理解与推理框架，同时也指出了在中文OCR和复杂图类型方面存在的挑战。

### 3.4.2 Tuning-required
由于纯文本表达图结构信息的局限性，近期的主流方法是在将图输入LLMs时，将其作为节点token序列与自然语言token序列进行对齐。与`GNN as Prefix`方法不同，`Tuning-required LLM-only`方法放弃了图编码器，转而采用特定的图token序列排列方式和精心设计的token嵌入，在多种图相关任务中取得了良好效果。

`InstructGLM`框架将自然语言指令与图嵌入相结合对LLMs进行fine-tuning，使其无需依赖专门的GNN架构即可处理图结构。`WalkLM`将random walks与语言模型结合，通过将图实体转化为文本序列并利用graph-aware fine-tuning，创建了能够捕捉属性语义和图结构的无监督图嵌入。近期，`LLaGA`利用node-level模板将图数据重组为有序序列，并映射到token嵌入空间，增强了LLM处理图结构数据的通用性和可解释性。`InstructGraph`通过结构化格式表达、图指令微调和偏好对齐，旨在弥合图数据与文本模型间的语义鸿沟，并缓解LLM输出中的幻觉问题。

此外，`ZeroG`利用语言模型编码节点属性和类别语义，通过基于prompt的子图采样和轻量级fine-tuning策略，解决了图学习中的跨数据集zero-shot transferability难题。`GraphWiz`利用`GraphInstruct`这一指令微调数据集和`Direct Preference Optimization (DPO)`来增强模型推理过程的清晰度和准确性。`GraphInstruct`本身是一个包含21个图推理任务的综合基准，旨在提升LLMs的图理解与推理能力。`MuseGraph`通过紧凑的图描述机制、多样化的指令生成和graph-aware instruction tuning，将LLMs的能力与图挖掘任务相融合。

### 3.4.3 讨论
`LLMs-Only`是一个新兴的研究方向，旨在探索专门为解释图数据和融合图与自然语言指令而预训练LLMs的潜力。其核心思想是利用LLM强大的语言理解能力对图数据进行推理。然而，当前仍面临重大挑战：如何在没有图编码器的情况下，有效地将大规模图转化为文本prompt，并通过重新排序图token序列来保持其结构完整性。这些挑战源于图数据的复杂性以及LLMs在没有明确指导下捕捉复杂关系的能力有限。因此，需要进一步的研究来开发更先进的方法，以克服上述挑战并更好地整合LLMs与图数据。

## 4 FUTURE DIRECTIONS

### 4. 未来方向

本章节探讨了图领域大语言模型（Large Language Models for Graphs）所面临的若干开放性问题和潜在的未来研究方向。

首先，一个核心方向是构建和扩展通用的**图基础模型（Graph Foundation Models, GFMs）**。当前研究表明，通过在海量图数据上进行**Pre-training**，模型能够学习到可迁移的图结构与语义知识。未来的工作需要探索如何进一步扩大**GFMs**的规模，以处理数十亿级别节点和边的超大规模图。这不仅对模型架构（如**Transformer**的变体）提出了挑战，也对**Self-supervised Learning**的效率和有效性提出了更高要求，例如开发比现有**Contrastive Learning**更优化的预训练目标。

其次，提升模型在复杂图任务上的**推理能力**是另一个关键研究领域。现有模型在**Node Classification**、**Link Prediction**等任务上表现出色，但在需要多步逻辑推理或理解深层结构关系的场景（如**Knowledge Graph**推理、**Graph Isomorphism**判断）中仍有局限。未来的研究可以探索如何将符号推理与**Graph Neural Networks (GNNs)**的表示学习能力更紧密地结合。此外，增强模型的**Few-shot Learning**和**Zero-shot Learning**能力，特别是通过**In-context Learning**使其能够快速适应未见过的图或任务，将是推动模型泛化性的重要突破口。

第三，对**多模态与异构图（Multi-modal and Heterogeneous Graph）**的处理能力亟待加强。现实世界的图数据往往是多模态的，例如社交网络中的图结构与用户发布的文本、图片相结合。未来的模型需要能够有效融合来自不同模态的信息，实现真正的**Multi-modal Learning**。同时，对于包含多种节点和关系类型的**Heterogeneous Graph**，如何设计统一且高效的**Message Passing**机制，以取代或改进现有的**GraphSAGE**和**Graph Attention Networks (GAT)**等方法，仍然是一个开放性问题。

第四，**跨领域迁移与领域自适应（Cross-domain Transfer and Domain Adaptation）**是提升模型实用价值的重要途径。目前，在一个领域（如生物信息学）**Pre-training**的模型直接**Fine-tuning**到另一个差异巨大的领域（如金融风控）时，效果往往不理想。未来的研究需要关注如何学习更具通用性的图表示，并开发高效的**Domain Adaptation**技术，以最小化目标域的标注需求，实现知识的有效迁移。

最后，模型的可解释性、鲁棒性和公平性是其在关键应用中落地前必须解决的问题。未来的研究需要超越传统的性能指标，关注模型的决策过程，并为**Graph Classification**或**Graph Anomaly Detection**等任务提供可靠的解释。同时，评估和提升模型在面对数据噪声或恶意攻击时的鲁棒性，也是一个至关重要的研究方向。

## 4.1 LLMs for Multi-modal Graphs

近期研究已证明，大型语言模型（LLMs）在处理和理解如图像、视频等多模态数据方面展现出卓越能力。这一能力为将LLMs与多模态图数据集成开辟了新途径，在此类图中，节点可能包含来自多种模态的特征。通过开发能够处理此类图数据的多模态LLMs，可以实现对图结构更精确、更全面的推理，这种推理不仅考虑了文本信息，还融合了视觉、听觉及其他类型的数据。

## 4.2 Efficiency and Less Computational Cost

当前，LLMs在训练和推理阶段的巨大计算开销构成了一个显著限制，阻碍了其处理包含数百万节点的大规模图的能力。当尝试将LLMs与GNNs进行融合时，由于前述的计算约束，这一挑战变得更加严峻。因此，寻找并实施能够以更低计算成本有效训练LLMs和GNNs的策略变得至关重要。这不仅是为了缓解当前的局限性，也是为了推动LLMs在图相关任务中的应用，从而扩大其在数据科学领域的作用和影响力。

## 4.3 Tackling Different Graph Tasks

目前，LLM 的主流方法主要集中于传统的图相关任务，如 `link prediction` 和 `node classification`。然而，考虑到 LLM 的卓越能力，探索其在处理更复杂和生成式任务方面的潜力是合理且充满前景的，这些任务包括但不限于 `graph generation` [97]、图理解以及基于图的问答 [32]。

将基于 LLM 的方法扩展至这些复杂任务，将为其在不同领域的应用开启众多新机遇。例如，在药物发现领域，LLM 可以促进新分子结构的生成；在社交网络分析中，它们能为复杂的关系模式提供更深刻的洞察；在 `knowledge graph` 构建方面，LLM 则有助于创建更全面、上下文更准确的知识库。

## 4.4 User-Centric Agents on Graphs

当前大多数为图相关任务设计的基于LLM的agent主要面向单一图任务。这些agent通常遵循一次性运行流程，旨在单次尝试中解决给定问题。因此，它们既不具备作为多轮交互式agent的功能，无法根据反馈或额外信息调整其生成的计划，也不是能有效处理用户各类问题的用户友好型agent。

一个理想的LLM-based agent [70] 不仅应是用户友好的，还必须能够响应用户提出的各种开放性问题，在图数据中动态搜索答案。这要求开发一种兼具适应性和鲁棒性的agent，它能够与用户进行迭代式交互，并能熟练地在复杂的图数据中导航，以提供准确且相关的答案。

## 5 CONCLUSION

本综述深入探讨了面向图数据的大型语言模型 (LLMs) 的研究现状，并基于模型推理框架的独特设计，提出了一种创新的分类法。我们将现有模型细分为四个独特的框架设计，并对每个类别的优缺点进行了详细讨论，同时分析了该领域内的潜在挑战与机遇。本研究旨在为探索和应用LLMs于图相关任务的研究者提供一份关键资源，并期望能启发和指引这一新兴领域的未来研究工作，从而促进对LLMs与图集成更深层次的理解并激发进一步的创新。

---

## 统计信息

- **总处理块数**: 20
- **原始总token数**: 7,110
- **总结总token数**: 907
- **整体压缩比**: 12.76%
- **平均压缩比**: 518.13%
- **处理章节数**: 20


*此文档由MinerU内容总结器V2自动生成，基于Langchain Markdown分割技术。*