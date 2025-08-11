# GRAPH FOUNDATION MODELS: A COMPREHENSIVE SURVEY (标准版) - 中文总结 (70%)

## 生成信息
- **压缩级别**: 70%
- **生成时间**: 2025-08-10 17:35:32
- **工具**: MinerU内容总结器 V2
- **原始块数**: 120
- **处理章节数**: 120
- **压缩比**: 20.35%

## 目录
- [GRAPH FOUNDATION MODELS: A COMPREHENSIVE SURVEY](#graph-foundation-models-a-comprehensive-survey)
- [ABSTRACT](#abstract)
- [3 Challenges in Designing Graph Foundation Models 12](#3-challenges-in-designing-graph-foundation-models-12)
- [4 A Unified Framework of Graph Foundation Models 14](#4-a-unified-framework-of-graph-foundation-models-14)
- [5 Universal Graph Foundation Models 29](#5-universal-graph-foundation-models-29)
- [6 Task-Specific Graph Foundation Models 41](#6-task-specific-graph-foundation-models-41)
- [7 Domain-Specific Graph Foundation Models 52](#7-domain-specific-graph-foundation-models-52)
- [7.2 Biology & Molecule Graph 52](#72-biology-molecule-graph-52)
- [7.3 Algorithmic Graphs 55](#73-algorithmic-graphs-55)
- [8 Theoretical Understandings 62](#8-theoretical-understandings-62)
- [9 Dataset Resources 65](#9-dataset-resources-65)
- [10 Open Questions 68](#10-open-questions-68)
- [1 Introduction](#1-introduction)
- [2 Background](#2-background)
- [2.1 A Brief History of Graph Learning](#21-a-brief-history-of-graph-learning)
- [2.2 Background of Foundation Models](#22-background-of-foundation-models)
- [2.3 Definitions & Notations](#23-definitions-notations)
- [3 Challenges in Designing Graph Foundation Models](#3-challenges-in-designing-graph-foundation-models)
- [3.1 Feature Heterogeneity](#31-feature-heterogeneity)
- [3.2 Structure Heterogeneity](#32-structure-heterogeneity)
- [3.3 Task Heterogeneity](#33-task-heterogeneity)
- [4 A Unified Framework of Graph Foundation Models](#4-a-unified-framework-of-graph-foundation-models)
- [4.1 Unified Framework](#41-unified-framework)
- [4.2 Backbone Architectures](#42-backbone-architectures)
- [4.2.1 Graph Model as Predictor](#421-graph-model-as-predictor)
- [4.2.2 Language Model as Predictor](#422-language-model-as-predictor)
- [4.2.3 Graph-Language Co-Training](#423-graph-language-co-training)
- [4.2.4 Discussion](#424-discussion)
- [4.3 Pretraining Strategies](#43-pretraining-strategies)
- [4.3.1 Supervised Pretraining](#431-supervised-pretraining)
- [4.3.2 Generative Pretraining](#432-generative-pretraining)
- [4.3.3 Contrastive Pretraining](#433-contrastive-pretraining)
- [4.3.4 Discussion](#434-discussion)
- [4.4 Adaptation](#44-adaptation)
- [4.4.1 Transfer Learning](#441-transfer-learning)
- [4.4.2 Distillation](#442-distillation)
- [4.4.3 Test-Time Adaptation](#443-test-time-adaptation)
- [4.4.4 Graph Prompting](#444-graph-prompting)
- [4.4.5 In-Context Learning](#445-in-context-learning)
- [4.4.6 Prototype Learning](#446-prototype-learning)
- [4.4.7 Discussion](#447-discussion)
- [5 Universal Graph Foundation Models](#5-universal-graph-foundation-models)
- [5.1 Design Principle](#51-design-principle)
- [5.2 Graph Model-Based Universal GFM](#52-graph-model-based-universal-gfm)
- [5.2.1 Model Unification](#521-model-unification)
- [5.2.2 Domain Alignment in Pretraining](#522-domain-alignment-in-pretraining)
- [5.2.3 Downstream Task Adaptation](#523-downstream-task-adaptation)
- [5.3 Language Model-Based Universal GFM](#53-language-model-based-universal-gfm)
- [5.3.1 Model Unification](#531-model-unification)
- [5.3.2 Domain Alignment in Model Training](#532-domain-alignment-in-model-training)
- [5.3.3 Downstream Task Adaptation](#533-downstream-task-adaptation)
- [5.4 Graph-Language Co-Training Universal GFMI](#54-graph-language-co-training-universal-gfmi)
- [5.4.1 Model Unification](#541-model-unification)
- [5.4.2 Domain Alignment in Model Training](#542-domain-alignment-in-model-training)
- [5.4.3 Downstream Task Adaptation](#543-downstream-task-adaptation)
- [5.5 Discussion](#55-discussion)
- [6 Task-Specific Graph Foundation Models](#6-task-specific-graph-foundation-models)
- [6.1 Design Principle](#61-design-principle)
- [6.2 Node-level Task](#62-node-level-task)
- [6.2.1 Handling Graph Heterogeneity](#621-handling-graph-heterogeneity)
- [6.2.2 Cross-domain Alignment](#622-cross-domain-alignment)
- [6.2.3 Domain Generalization v.s. Task-specific Adaptation](#623-domain-generalization-vs-task-specific-adaptation)
- [6.2.4 Future Direction](#624-future-direction)
- [6.3 Link-Level Task](#63-link-level-task)
- [6.3.1 Inductive Reasoning Approaches](#631-inductive-reasoning-approaches)
- [6.3.2 In-Context Learning Approaches](#632-in-context-learning-approaches)
- [6.3.3 Transformer-based Approaches](#633-transformer-based-approaches)
- [6.3.4 Hybrid Methods](#634-hybrid-methods)
- [6.3.5 Future Directions](#635-future-directions)
- [6.4Graph-Level Task](#64graph-level-task)
- [6.4.1 Pre-Training Stages](#641-pre-training-stages)
- [6.4.2 Fine-Tuning Stages](#642-fine-tuning-stages)
- [6.4.3 LLM-incorporated Approaches](#643-llm-incorporated-approaches)
- [6.4.4 Graph Generation](#644-graph-generation)
- [6.4.5 Hybrid Approaches](#645-hybrid-approaches)
- [6.4.6 Future Directions](#646-future-directions)
- [6.5 Question Answering](#65-question-answering)
- [6.6 Graph Anomaly Detection](#66-graph-anomaly-detection)
- [6.7 Recommendation](#67-recommendation)
- [7 Domain-Specific Graph Foundation Models](#7-domain-specific-graph-foundation-models)
- [7.1 Design Principle](#71-design-principle)
- [7.2 Biology & Molecule Graph](#72-biology-molecule-graph)
- [7.2.1 Graph Model-based Approaches](#721-graph-model-based-approaches)
- [7.2.2 Language Model-based Approaches](#722-language-model-based-approaches)
- [7.2.3 Hybrid Approaches](#723-hybrid-approaches)
- [7.2.4 Future Directions](#724-future-directions)
- [7.3 Algorithmic Graphs](#73-algorithmic-graphs)
- [7.3.1 Structured Graph Reasoning](#731-structured-graph-reasoning)
- [7.3.2 Benchmarking and Multi-Agent Collaboration](#732-benchmarking-and-multi-agent-collaboration)
- [7.3.3 Encoding Strategies and Algorithmic Refinement](#733-encoding-strategies-and-algorithmic-refinement)
- [7.3.4 Future Directions](#734-future-directions)
- [7.4 Document Network](#74-document-network)
- [7.5 Heterogeneous Graph](#75-heterogeneous-graph)
- [7.6 Knowledge Graph](#76-knowledge-graph)
- [7.7 Temporal Graph](#77-temporal-graph)
- [7.8 Academic Network](#78-academic-network)
- [7.9 Causal Graph](#79-causal-graph)
- [8 Theoretical Understandings](#8-theoretical-understandings)
- [8.1 Emergence and Scaling Law](#81-emergence-and-scaling-law)
- [8.1.1 Well-Structured Graphs](#811-well-structured-graphs)
- [8.1.2 General Graphs](#812-general-graphs)
- [8.2 Transferability](#82-transferability)
- [8.2.1 Single-Task Transferability](#821-single-task-transferability)
- [8.2.2 Cross-Task Transferability](#822-cross-task-transferability)
- [9 Dataset Resources](#9-dataset-resources)
- [9.1 Tasks and Domains Overview](#91-tasks-and-domains-overview)
- [9.1.1 Tasks](#911-tasks)
- [9.1.2 Domains](#912-domains)
- [9.2 Benchmark Descriptions](#92-benchmark-descriptions)
- [10 Open Questions](#10-open-questions)
- [10.1 How to Enhance Scalability?](#101-how-to-enhance-scalability)
- [10.2 How to Mitigating Data Scarcity?](#102-how-to-mitigating-data-scarcity)
- [10.3 How to Better Evaluate GFMs?](#103-how-to-better-evaluate-gfms)
- [10.4 How to Better Utilize GFMs?](#104-how-to-better-utilize-gfms)
- [10.5 Advanced Theoretical Understandings](#105-advanced-theoretical-understandings)
- [11 Conclusion](#11-conclusion)

## GRAPH FOUNDATION MODELS: A COMPREHENSIVE SURVEY

本综述全面探讨了Graph Foundation Models (GFMs)，旨在为图学习领域提供一个统一的视角。文章首先回顾了Graph Neural Networks (GNNs) 的发展历程，重点介绍了Message Passing机制、Node Embedding技术以及各种GNN架构，如Graph Convolutional Networks (GCN) 和 Graph Attention Networks (GAT)。接着，文章深入分析了GFMs的核心概念，包括Pre-training、Self-supervised Learning、Contrastive Learning等训练范式，以及Fine-tuning、In-context Learning、Few-shot Learning和Zero-shot Learning等下游任务的适应策略。

GFMs在处理不同类型的图结构，如Homogeneous Graph、Heterogeneous Graph和Knowledge Graph方面展现出强大的能力。文章详细阐述了GFMs在多种图学习任务中的应用，包括Graph Classification、Node Classification、Link Prediction、Graph Generation和Graph Anomaly Detection。此外，GFMs还被应用于Multi-modal Learning和Cross-domain Transfer，以实现Domain Adaptation。

本综述还讨论了GFMs面临的挑战，例如Graph Isomorphism问题、计算效率和模型可解释性。最后，文章展望了GFMs的未来发展方向，包括更强大的预训练模型、更高效的微调技术以及在更广泛领域的应用潜力。

本综述深入探讨了Graph Foundation Models (GFMs)，重点关注了预训练中的Domain Alignment和下游任务的Adaptation。文章详细介绍了基于Language Model的Universal GFM，强调了Model Unification、Domain Alignment in Model Training以及Downstream Task Adaptation。此外，还讨论了Graph-Language Co-Training Universal GFM，同样涵盖了Model Unification、Domain Alignment in Model Training和Downstream Task Adaptation。最后，对这些方法进行了综合性讨论。

本章节全面 survey 了 Graph Foundation Models (GFMs)，重点关注了结合 Graph Neural Networks (GNNs) 和 Large Language Models (LLMs) 的混合架构，旨在弥合图结构和语言之间的模态鸿沟，实现更强大的图推理能力。

**核心挑战与动机：**
将图结构线性化以供 LLMs 处理时，图的拓扑结构、连接模式和图不变性等信息常常丢失或被模糊化，导致推理性能不佳。因此，需要能够保留图的归纳偏置（inductive biases）并利用 LLMs 实现语义泛化的混合架构。

**混合架构的设计思路：**
借鉴 Vision-Language Models (VLMs) 将视觉信息融入 LLMs 的思路，研究者们提出了结合 GNNs 的表示能力和 LLMs 的推理能力的混合 Graph-Language Models。这些模型通常包含三个关键步骤：
1.  **Graph Encoding：** 使用 GNN 提取节点或图级别的 embedding，捕捉局部和全局的结构依赖。公式表示为 $\mathbf{H} = \mathrm{GNN}(\mathbf{X},\mathbf{A})$，其中 $\mathbf{X}$ 是节点特征，$\mathbf{A}$ 是邻接矩阵，$\mathbf{H}$ 是学习到的节点 embedding。
2.  **Cross-Modality Projection：** 通过一个投影函数 $\rho$ 将图 embedding 映射到 LLM 的 token 空间，实现结构信息与语言模型的对齐。公式表示为 $\mathbf{Z} = \rho (\mathbf{H})$，其中 $\mathbf{Z}$ 是 token 对齐的图表示。
3.  **Language-Based Inference：** LLM $f_{\mathrm{LLM}}$ 接收一个包含投影后的图 embedding $\mathbf{Z}$、任务指令和示例的 prompt $\mathcal{P}$ 进行推理。公式表示为 $\hat{y} = f_{\mathrm{LLM}}([\mathcal{P}\parallel \mathbf{Z}])$。

**关键技术和方法：**
*   **GNNs：** 用于捕获图的结构信息，例如 Graph Convolutional Networks (GCN) 和 Graph Attention Networks (GAT)。
*   **LLMs：** 用于执行下游推理任务，利用其强大的语言理解和生成能力。
*   **Pre-training：** 通常采用 Self-supervised Learning 或 Contrastive Learning 等方法对 GNN 和 LLM 进行预训练，以学习通用的图表示和语言表示。
*   **Adaptation：** 预训练后的模型可以通过 Fine-tuning、In-context Learning、Few-shot Learning 或 Zero-shot Learning 等方式适应下游任务。
*   **Feature Align：** 通过将图的节点特征或文本属性与语言模型对齐。
*   **Structure Align：** 通过数据增强或模型设计来对齐图的结构信息。
*   **Task Align：** 通过显式的任务定义（如 Question Answering, QA）或子图匹配来对齐任务目标。

**代表性模型（Table 4 总结）：**
表格展示了多种 Graph-Language Co-training Universal GFMs，它们大多采用 GNN + LLM 的 Backbone，并结合了不同的 Pretrain、Adaptation、Feature Align、Structure Align 和 Task Align 策略。例如，GOFA、GraphGPT、GALLM、LLaGA、GraphCLIP、GraphTranslator、PromptGFM、GraphPrompter、TEA-GLM、NT-LLM、AskGNN 和 GraphAgent 等模型在这些方面各有侧重。其中，许多模型通过将图的节点特征与文本属性对齐，并利用数据增强来对齐结构，同时通过显式的 QA 任务来对齐任务。Adaptation 策略则包括 Finetune 和 In-context Learning。

本章节对Graph Foundation Models (GFMs)进行了全面的调查，重点关注其在计算图领域的应用。调查结果总结在表10中，该表列出了在计算图领域应用的各种GFMs。这些模型主要基于GNN或LLM架构，并采用不同的预训练（Pretrain）策略，如Supervised或Generative。在模型适应（Adaptation）方面，研究涵盖了Finetune、In-context Learning等多种方法。

调查显示，大多数模型通过对Node Property进行数据对齐（Feature Align）来处理计算图数据。结构对齐（Structure Align）方面，模型采用了Data - Augment、Model - Retriever等技术。任务对齐（Task Align）主要集中在Explicit - QA任务上。

具体而言，一些模型如Triplet-GMPNN使用GNN作为Backbone，并采用Supervised预训练和Finetune适应。而GraphForge、HLM-G、PathCompare、Hyper-BAG and Hyper-COT、Graph Linearization、TP、GPT4Graph、Graph-Agent-Reasoner、GraphTeam、GUNDAM、PIE、GraphInstruct、GCoder、GraphML等模型则利用LLM作为Backbone，并主要采用Generative预训练和In-context Learning适应。其中，GraphTeam模型在Adaptation上同时使用了Generative和Finetune。

此外，GraphLLM和GraphToken模型结合了GNN和LLM，并采用Generative预训练和Finetune、In-context Learning适应。这些模型在处理计算图数据时，普遍关注Node Property的对齐，并利用Model - Retriever或Model - Augment等技术进行结构对齐。在任务对齐上，Explicit - QA是计算图领域GFMs的主要应用方向。

本章节对Graph Foundation Models (GFMs)进行了全面的调研，重点关注其在文档图上的应用。调研结果总结于Table 11，展示了METAG、TAPE、LLM4GraphTopology、G-Prompt、ConGraT、GLEM和PATTON等方法。这些方法通常采用GNN + LLM的backbone，并在预训练（Pretrain）阶段采用Supervised或Hybrid策略。在模型适应（Adaptation）方面，In-context Learning、Fine-tuning和Distillation是常用技术。特征对齐（Feature Align）主要依赖Data - Text Attribute，结构对齐（Structure Align）则涉及Data - Augment和Loss - Pretrain等。任务对齐（Task Align）则通过Model - Retriever或Explicit - QA等方式实现。

展望未来，GFMs有望通过递归分解图问题为子问题来解决更复杂的任务。结合结构化检索、多智能体协作和外部工具使用将提升模型在真实世界任务中的适应性和鲁棒性。GraphPatternBench、NLGraph和GraphArena等基准测试强调了跨科学、社会和生物领域对真实数据集的需求。Tool-augmented reasoning框架，如GraphTool-Instruction和PIE，预示着混合GFMs的发展方向，即融合学习推理与结构化算法调用，为下一代图数学推理模型奠定基础。

## ABSTRACT

本综述全面概述了Graph Foundation Models (GFMs)，旨在为结构化数据带来可扩展、通用型智能，并实现跨图任务和领域的广泛迁移。图结构数据广泛存在于社交网络、生物系统、Knowledge Graph和推荐系统等领域。尽管Foundation Models通过大规模预训练和泛化能力改变了自然语言处理、视觉和Multi-modal Learning，但将其能力扩展到图数据——其特点是非欧几里得结构和复杂的关联语义——带来了独特的挑战和新的机遇。GFMs将各种努力统一在一个包含三个关键组件的模块化框架下：backbone architectures、pretraining strategies和adaptation mechanisms。我们根据GFMs的泛化范围将其分类：universal、task-specific和domain-specific，并回顾每个类别中的代表性方法、关键创新和理论见解。除了方法论，我们还考察了包括transferability和emergent capabilities在内的理论基础，并强调了结构对齐、异质性、可扩展性和评估等关键挑战。GFMs处于Graph Learning和General-purpose AI的交叉点，有望成为开放式结构化数据推理的基础设施。本综述整合了当前进展，并概述了未来方向，以指导这一快速发展领域的研究。相关资源可在https://github.com/Zehong-Wang/Awesome-Foundation-Models-on-Graphs获取。

## 3 Challenges in Designing Graph Foundation Models 12

本章节探讨了设计Graph Foundation Models (GFMs)所面临的三大核心挑战：Feature Heterogeneity、Structure Heterogeneity和Task Heterogeneity。

**3.1 Feature Heterogeneity** 指的是图中节点和边的特征可能具有截然不同的类型和分布。例如，某些节点可能拥有数值型特征，而另一些则可能包含文本或图像信息。这种多样的特征表示形式给GFMs的统一处理带来了困难，需要模型能够有效地整合和学习来自不同模态的特征。

**3.2 Structure Heterogeneity** 关注的是图中结构的多样性。这包括了节点连接模式的差异、图的规模变化以及图的类型（如Homogeneous Graph vs. Heterogeneous Graph）。GFMs需要具备处理不同连接密度、不同节点度分布以及能够泛化到不同拓扑结构的图的能力。例如，Message Passing机制在处理高度稀疏或高度稠密的图时可能面临挑战。

**3.3 Task Heterogeneity** 强调了GFMs需要适应多种下游图学习任务。这些任务可能包括Node Classification、Link Prediction、Graph Classification、Graph Generation以及Graph Anomaly Detection等。一个成功的GFM应该能够通过Pre-training和Fine-tuning，或者通过In-context Learning和Few-shot Learning/Zero-shot Learning等方式，有效地迁移到各种不同的图任务上，而无需从头开始训练。这要求GFMs具备强大的泛化能力和任务适应性。

## 4 A Unified Framework of Graph Foundation Models 14

本章提出了一个统一的Graph Foundation Models (GFMs) 框架，旨在整合现有GFMs的研究进展。框架的核心在于其灵活的“Backbone Architectures”，包括将Graph Model作为Predictor、将Language Model作为Predictor，以及Graph-Language Co-Training。这些架构为GFMs提供了多样化的建模能力。

在“Pretraining Strategies”部分，本章探讨了多种预训练方法，以提升GFMs的泛化能力和下游任务性能。主要包括Supervised Pretraining、Generative Pretraining和Contrastive Pretraining。这些策略通过不同的目标函数和数据增强方式，使GFMs能够学习到丰富的图结构和节点/边表示。

最后，“Adaptation”部分聚焦于如何将预训练好的GFMs有效地应用于各种下游任务。本章介绍了多种适应技术，如Transfer Learning、Distillation、Test-Time Adaptation、Graph Prompting、In-Context Learning和Prototype Learning。这些方法使得GFMs能够在不同领域和任务上实现高效的Few-shot Learning和Zero-shot Learning，并促进Cross-domain Transfer。

## 5 Universal Graph Foundation Models 29

本章探讨了通用Graph Foundation Models (GFMs) 的设计原则和基于图模型的通用GFM。核心观点在于，GFMs应具备跨多种图任务和数据类型的通用性。

**5.1 设计原则 (Design Principle)**

通用GFMs的设计应遵循以下原则：

*   **模型统一 (Model Unification)**：旨在开发能够处理不同图结构（如Homogeneous Graph, Heterogeneous Graph）和不同任务（如Node Classification, Link Prediction, Graph Classification, Graph Anomaly Detection）的单一模型架构。这与以往针对特定任务或图类型设计的模型形成对比。
*   **可扩展性 (Scalability)**：模型应能够处理大规模图数据，这通常需要高效的Message Passing机制和优化的计算策略。
*   **泛化能力 (Generalization)**：GFMs应具备强大的泛化能力，能够将从大规模预训练中学到的知识迁移到下游任务和不同领域（Cross-domain Transfer），即使在Few-shot Learning或Zero-shot Learning场景下也能表现良好。
*   **预训练与微调 (Pre-training and Fine-tuning)**：借鉴自然语言处理领域的成功经验，GFMs也应采用大规模预训练（通常结合Self-supervised Learning）和下游任务的Fine-tuning范式。

**5.2 基于图模型的通用GFM (Graph Model-Based Universal GFM)**

本节重点介绍了如何构建能够实现上述原则的通用GFMs。

**5.2.1 模型统一 (Model Unification)**

实现模型统一的关键在于设计能够灵活适应不同图属性和任务的架构。这通常涉及：

*   **统一的图表示学习 (Unified Graph Representation Learning)**：开发能够学习到通用、丰富的Node Embedding的机制，这些Embedding能够捕捉节点在不同图结构中的语义和结构信息。
*   **灵活的Message Passing机制 (Flexible Message Passing Mechanisms)**：虽然Message Passing是GNNs的核心，但通用GFMs需要更灵活的Message Passing，例如能够处理异构图中的不同边类型和节点属性，或者集成Transformer的自注意力机制（如Graph Attention Networks - GAT）。
*   **多任务学习框架 (Multi-task Learning Framework)**：通过在预训练阶段同时学习多种图任务（如Node Classification, Link Prediction），可以使模型获得更全面的图结构和属性理解能力。
*   **适应性架构设计 (Adaptive Architecture Design)**：可能需要引入能够根据输入图的特性（如节点数量、边密度、异构性程度）动态调整模型参数或结构的机制。

通过这些设计原则和模型统一的策略，通用GFMs有望成为处理各种图数据和任务的强大基础模型，极大地推动图学习领域的发展。

## 6 Task-Specific Graph Foundation Models 41

本章探讨了Task-Specific Graph Foundation Models (GFMs)，重点关注其设计原则以及在不同图任务中的应用。

**6.1 设计原则**
GFMs的设计原则旨在构建能够适应多种下游图任务的通用模型。

**6.2 节点级任务 (Node-level Task)**
该部分讨论了在节点级任务中处理图异质性（Graph Heterogeneity）、跨领域对齐（Cross-domain Alignment）以及领域泛化（Domain Generalization）与任务特定适应（Task-specific Adaptation）之间的权衡。未来的研究方向包括更有效的异质图表示学习和跨领域迁移。

**6.3 链接级任务 (Link-Level Task)**
链接级任务，如Link Prediction，涵盖了多种方法。包括归纳推理方法（Inductive Reasoning Approaches）、In-Context Learning Approaches以及基于Transformer的方法（Transformer-based Approaches）。混合方法（Hybrid Methods）结合了不同技术的优势。未来的研究将侧重于提升模型的归纳能力和上下文学习能力。

**6.4 图级任务 (Graph-Level Task)**
图级任务，如Graph Classification，通常涉及预训练阶段（Pre-Training Stages）和Fine-tuning阶段（Fine-Tuning Stages）。此外，还介绍了结合大型语言模型（LLM-incorporated Approaches）的方法、Graph Generation技术以及混合方法。未来的研究方向包括更强大的预训练策略、LLM在图生成和理解中的作用以及跨领域迁移能力。

**6.5 问答 (Question Answering)**
在图问答任务中，GFMs被用于理解和回答关于图结构和节点/边属性的问题。

**6.6 图异常检测 (Graph Anomaly Detection)**
GFMs在图异常检测任务中，能够学习正常图的模式并识别偏离这些模式的异常节点或子图。

**6.7 推荐 (Recommendation)**
在推荐系统中，GFMs利用用户-物品交互图来学习用户和物品的Node Embedding，从而进行个性化推荐。

## 7 Domain-Specific Graph Foundation Models 52

本章探讨了领域特定的Graph Foundation Models (GFMs)，重点关注其设计原则。

**7.1 设计原则**

领域特定的GFMs在设计时需要考虑如何有效地捕捉和利用特定领域的图结构和语义信息。这通常涉及以下几个关键原则：

*   **领域知识的整合 (Integration of Domain Knowledge):** 将领域内的先验知识（如实体类型、关系类型、属性等）融入到模型架构或训练过程中，以增强模型对特定领域图数据的理解能力。这可以通过定制化的图表示学习方法、知识图谱的利用或领域特定的预训练任务来实现。
*   **异构图处理 (Handling Heterogeneous Graphs):** 许多领域图是异构的，包含不同类型的节点和边。设计原则需要关注如何有效地处理这种异构性，例如通过使用能够区分不同节点和边类型的Message Passing机制，或者采用能够学习不同类型实体和关系表示的Node Embedding技术。
*   **多模态信息融合 (Multi-modal Information Fusion):** 在某些领域，图数据可能伴随着其他模态的信息，如文本、图像或数值属性。领域特定的GFMs应能够有效地融合这些多模态信息，以获得更全面的图表示。这可能涉及到多模态学习技术，将不同模态的信息映射到统一的表示空间。
*   **可解释性与可控性 (Interpretability and Controllability):** 领域专家通常需要理解模型的决策过程，并能够对其行为进行一定程度的控制。因此，设计原则应考虑如何提高GFMs的可解释性，例如通过注意力机制的分析或引入可解释的图表示学习方法。
*   **跨领域迁移与适应 (Cross-domain Transfer and Adaptation):** 尽管是领域特定的，但GFMs也应具备一定的跨领域迁移能力，或者能够通过Domain Adaptation技术快速适应新的、但与预训练领域相关的下游任务。这通常依赖于强大的预训练表示和有效的Fine-tuning策略。

总而言之，领域特定的GFMs的设计原则在于平衡通用图学习能力与特定领域知识的深度融合，以在各种下游任务中实现卓越的性能。

## 7.2 Biology & Molecule Graph 52

本章探讨了在生物学和分子图谱领域应用图模型、语言模型及混合方法的研究进展。

**7.2.1 图模型基础方法** 重点介绍了基于Graph Neural Networks (GNNs) 的方法，包括Graph Convolutional Networks (GCN) 和Graph Attention Networks (GAT) 等，它们通过Message Passing机制学习Node Embedding，并应用于Graph Classification、Node Classification和Link Prediction等任务。此外，还提及了GraphSAGE等归纳式学习方法。

**7.2.2 语言模型基础方法** 关注了将Transformer等语言模型应用于生物分子序列和图谱数据的方法，例如通过Self-supervised Learning进行Pre-training，并利用In-context Learning、Few-shot Learning或Zero-shot Learning进行下游任务的Fine-tuning。

**7.2.3 混合方法** 结合了图模型和语言模型的优势，例如将多模态信息整合到图结构中，或利用语言模型理解图谱数据的上下文信息，以实现Cross-domain Transfer和Domain Adaptation。

**7.2.4 未来方向** 指出该领域未来的研究方向可能包括开发更强大的Graph Foundation Models (GFMs)，探索更有效的Contrastive Learning策略，以及在生物信息学和药物发现等实际应用中进一步拓展这些模型的潜力。

## 7.3 Algorithmic Graphs 55

本章节“Algorithmic Graphs”探讨了图算法在人工智能领域的应用，重点关注了结构化图推理、基准测试与多智能体协作、编码策略与算法优化，并展望了未来的发展方向。

在结构化图推理方面，章节讨论了如何利用图结构进行复杂的推理任务。基准测试与多智能体协作部分则关注如何评估图算法的性能，并探索了多智能体系统在图相关任务中的协同作用。编码策略与算法优化部分深入研究了有效的图信息编码方法以及如何改进图算法的效率和性能。最后，章节对“Algorithmic Graphs”的未来研究方向进行了展望，预示着该领域在 Graph Neural Networks (GNNs) 和 Graph Foundation Models (GFMs) 等前沿技术中的潜力。

本章节的讨论为理解和应用图算法提供了理论基础和实践指导，尤其是在处理复杂关系数据方面。

## 8 Theoretical Understandings 62

本章深入探讨了Graph Neural Networks (GNNs) 和 Graph Foundation Models (GFMs) 的理论基础，重点关注其在不同规模和结构图上的表现以及跨任务和跨领域的迁移能力。

**8.1 Emergence and Scaling Law** 探讨了GNNs和GFMs在图数据上的涌现能力和Scaling Law。

*   **8.1.1 Well-Structured Graphs**: 在结构良好的图（如规则图、同质图）上，GNNs和GFMs展现出良好的涌现现象，即随着模型规模（如层数、隐藏维度）和数据规模的增加，模型性能会遵循特定的Scaling Law，表现出更强的学习和表示能力。这通常与Message Passing机制在结构化信息上的有效聚合有关。
*   **8.1.2 General Graphs**: 在更一般的、异质的、包含噪声或不规则结构的图上，Scaling Law的体现可能更为复杂。本节可能讨论了在这些情况下，模型如何通过更复杂的架构（如Transformer-based GNNs）或更有效的图表示学习（如Node Embedding）来克服结构挑战，并探索其涌现能力的边界。

**8.2 Transferability** 关注GNNs和GFMs的迁移能力，即模型在不同任务或领域之间传递知识的能力。

*   **8.2.1 Single-Task Transferability**: 讨论了在同一任务下，模型从一个图数据集迁移到另一个图数据集的能力。这通常通过Pre-training和Fine-tuning策略实现，例如在大型图上进行Self-supervised Learning的Pre-training，然后在特定下游任务（如Node Classification, Link Prediction）上进行Fine-tuning。In-context Learning和Few-shot Learning也可能被提及，作为在少量目标数据上快速适应的方法。
*   **8.2.2 Cross-Task Transferability**: 探讨了模型在不同任务之间迁移的能力，例如在一个任务（如Graph Classification）上学习到的知识能否有效应用于另一个任务（如Graph Anomaly Detection）。这可能涉及到更通用的图表示学习，以及如何设计能够捕捉不同任务共性特征的GFMs。Cross-domain Transfer和Domain Adaptation是实现跨任务迁移的关键技术。

## 9 Dataset Resources 65

本章节详细介绍了用于评估 Graph Foundation Models (GFMs) 的数据集资源。

**9.1 任务和领域概述**

本节首先对 GFMs 的应用任务和涉及的领域进行了概览。

*   **9.1.1 任务 (Tasks)**：本节将 GFMs 的应用任务归类，涵盖了图学习中的核心任务，例如 Node Classification, Link Prediction, Graph Classification 等。这些任务旨在评估模型在理解图结构和节点/边属性方面的能力。
*   **9.1.2 领域 (Domains)**：本节进一步梳理了 GFMs 所应用的具体领域，包括但不限于社交网络、生物信息学、推荐系统、知识图谱 (Knowledge Graph) 等。不同领域的数据具有不同的特性，例如异构性 (Heterogeneous Graph) 或同质性 (Homogeneous Graph)，这为模型提出了不同的挑战。

**9.2 基准数据集描述 (Benchmark Descriptions)**

本节详细介绍了用于评估 GFMs 的一系列基准数据集。这些数据集被精心选择，以覆盖广泛的任务和领域，并为模型性能的公平比较提供基础。描述中可能包含数据集的规模、节点和边的特征、以及其在特定任务上的应用情况。这些基准数据集对于衡量 Graph Neural Networks (GNNs) 和 GFMs 在各种图学习任务上的有效性至关重要，并为研究人员提供了进行模型比较和分析的标准化平台。

## 10 Open Questions 68

本章探讨了Graph Foundation Models (GFMs)领域的十个开放性问题，旨在推动该领域的发展。主要问题包括：

1.  **可扩展性增强 (Scalability Enhancement)**：如何设计更具可扩展性的GFMs，以处理大规模图数据。
2.  **数据稀疏性缓解 (Mitigating Data Scarcity)**：如何有效解决GFMs在数据稀疏场景下的性能问题，例如通过Self-supervised Learning和Pre-training技术。
3.  **评估方法改进 (Better Evaluation)**：如何开发更全面、更准确的评估指标和基准，以衡量GFMs在不同任务（如Graph Classification, Node Classification, Link Prediction）上的表现。
4.  **GFMs的有效利用 (Better Utilization)**：如何更好地将GFMs应用于下游任务，包括Fine-tuning、In-context Learning和Few-shot Learning等场景。
5.  **理论理解深化 (Advanced Theoretical Understandings)**：深入理解GFMs（如基于Transformer和Message Passing的架构）的工作原理，包括其表达能力、泛化性和局限性。

此外，还涉及了如处理异构图 (Heterogeneous Graph) 和同构图 (Homogeneous Graph) 的挑战、GFMs在多模态学习 (Multi-modal Learning) 和跨领域迁移 (Cross-domain Transfer) 中的应用潜力，以及如何利用GFMs进行图生成 (Graph Generation) 和图异常检测 (Graph Anomaly Detection)。这些问题共同指明了GFMs未来研究的方向。

## 1 Introduction

本章节介绍了Graph Foundation Models (GFMs) 的概念、发展背景、现有研究的不足以及本文的贡献。

**核心论点：**
文章指出，机器学习领域正朝着“一个模型适应所有任务”（one-model-fits-all）的范式转变，旨在开发高度通用、可迁移的模型。继自然语言处理（NLP）和计算机视觉（CV）领域出现Foundation Models（如LLMs和LVMs）后，GFMs的出现旨在将这种能力扩展到图结构数据。图结构数据因其关系依赖性、置换不变性和非欧几里得几何特性而具有独特性。GFMs的目标是提供一个统一、可预训练、可适应的解决方案，以应对各种图基应用，包括分子属性预测、知识图谱推理、社交网络分析和推荐系统等。

**方法与内容组织：**

1.  **发展背景与挑战：**
*   机器学习从早期的规则系统、线性分类器发展到深度学习，在表示学习、可扩展性和任务性能方面取得了进步。
*   传统模型（如决策树、SVM、KNN）在低维结构化数据上表现良好，但在高维、非结构化或多模态数据上遇到挑战。
*   深度学习模型（CNNs, RNNs）在感知任务上表现出色，但仍需要任务特定的调整、架构设计和大量标注数据。
*   迁移学习和Self-supervised Learning的出现使得模型能够从大规模无标签数据中学习可迁移的表示，为Foundation Models奠定了基础。
*   Foundation Models的特点是规模大、通用性强、在异构数据源上进行Pre-training，能够捕获可迁移的归纳偏置（inductive biases），从而在少量任务特定监督下实现高性能。
*   LLMs和LVMs通过将输入视为token序列并使用Transformer架构，在NLP和CV领域展示了强大的Zero-shot Learning和Few-shot Learning能力。

2.  **GFMs的提出与现有工作：**
*   GFMs旨在将Foundation Models的能力扩展到图结构数据，以解决图基应用的广泛需求。
*   文中提到了OFA和GFT等GFM的例子，它们通过跨领域图的节点表示对齐和结构模式捕获来实现通用性。
*   此外，也存在针对特定任务（如Node Classification, Anomaly Detection, Recommendation Systems）或特定领域（如Knowledge Graphs, Molecular Graphs）的GFMs。

3.  **现有研究的不足：**
*   现有关于GFMs的综述存在碎片化问题，未能系统性地覆盖该领域的全貌，包括基础技术、设计挑战和研究方向。
*   部分综述侧重于特定方面，如骨干架构（GNN-based, LLM-based, hybrid GNN+LLM）、Pre-training目标、可迁移性理论或跨领域图学习，但缺乏整体性。

4.  **本文的贡献：**
*   **GFM设计挑战：** 识别并分类了构建GFM的核心挑战，包括特征异质性（feature heterogeneity）、结构异质性（structural heterogeneity）和任务异质性（task heterogeneity）。
*   **统一框架：** 提出了一个模块化的统一框架，将GFMs分解为三个核心组件：骨干架构（backbone architectures）、Pre-training策略（pretraining strategies）和适应机制（adaptation mechanisms）。
*   **分类与全面综述：** 建立了一个分类体系，将GFMs分为通用GFMs（universal GFMs）、领域特定GFMs（domain-specific GFMs）和任务特定GFMs（task-specific GFMs），并对每个类别进行了广泛的文献回顾。
*   **理论基础：** 探讨了GFMs的理论基础，包括Scaling Laws、可迁移性理论（transferability theory）以及图基Pre-training中的泛化能力。
*   **资源与代码库：** 整理并发布了一个资源库，包含基准数据集、开源实现、预训练模型和GitHub链接（https://github.com/Zehong-Wang/Awesome-Foundation-Models-on-Graphs），以促进可复现性和研究。
*   **开放性问题：** 总结了GFM领域的关键开放性问题，如异构图对齐、高效适应机制、鲁棒评估和深入的理论洞察。

5.  **未来方向总结：**
*   GFM的发展仍处于早期阶段，面临可扩展性、数据可用性、评估、利用和理论理解等方面的挑战。
*   需要更具可扩展性的架构、高级生成目标和统一的学习实例来解锁类似LLMs和LVMs的性能。
*   解决图数据的稀疏性问题需要自动化数据收集、高保真合成生成和质量中心的数据集策展策略。
*   GFM的评估需要反映真实世界任务的基准和衡量泛化、鲁棒性和可信度的指标。
*   有效利用GFMs需要改进适应机制（如Zero-shot Learning和Prompt-based Learning），探索传统图任务之外的高影响力应用，并整合多模态知识表示。
*   理论基础仍需深入研究，包括理解可迁移性的极限、解决跨领域模式冲突、确保分布偏移下的鲁棒性以及推导泛化保证。

![](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/802bbe62f885717b58b83579ddfa52c3c1d73c480c874582ae32b29b14207c6a_0596be7e.jpg)
（图1展示了从传统的任务特定图模型到通用图Foundation Models的范式转变。图(a)描述了GFMs如何通过在跨多个领域的图语料库上进行Pre-training来获取可迁移表示，并通过微调、蒸馏、提示或零样本推理等方式适应下游任务。图(b)对比了传统GNNs通常在单领域数据集上为特定任务进行端到端训练，缺乏开放世界的泛化能力。）

## 2 Background

本章节“2 Background”为后续研究奠定了基础，主要介绍了与图神经网络（GNNs）和图基础模型（GFMs）相关的背景知识。

**核心观点与贡献：**

本章节旨在为读者提供理解图数据处理和分析领域最新进展所需的关键概念和技术。它强调了GNNs在处理非结构化图数据方面的强大能力，并引出了GFMs作为更通用、更强大的图数据建模范式。

**主要内容概述：**

*   **图神经网络（GNNs）的兴起与发展：** 章节可能回顾了GNNs的起源，解释了其核心思想，即通过Message Passing机制在图结构上传播和聚合节点信息，从而学习Node Embedding。可能会提及一些经典的GNNs模型，如Graph Convolutional Networks (GCN) 和 Graph Attention Networks (GAT)，以及GraphSAGE等，并阐述它们在Node Classification、Link Prediction等下游任务上的应用。
*   **图基础模型（GFMs）的概念与潜力：** 章节将GFMs定义为在大规模、多样化的图数据集上进行Pre-training的模型，旨在学习通用的图表示能力。这使得GFMs能够通过Fine-tuning、In-context Learning、Few-shot Learning甚至Zero-shot Learning等方式，快速适应各种下游图任务，而无需从头开始训练。GFMs的出现标志着图学习领域正朝着更高效、更通用的方向发展。
*   **相关技术与挑战：** 章节可能还会涉及与图数据处理相关的其他重要技术，例如Self-supervised Learning在图数据上的应用，以及处理Heterogeneous Graph和Homogeneous Graph的挑战。此外，Graph Pooling、Graph Classification、Graph Generation、Graph Anomaly Detection等任务也可能被提及，作为GFMs潜在的应用场景。

总而言之，本章节为理解和研究GFMs提供了必要的理论和技术背景，强调了GNNs作为基础，以及GFMs在提升图学习通用性和效率方面的关键作用。

## 2.1 A Brief History of Graph Learning

图学习正经历一场范式转变，从高度专业化、任务特定的模型转向更统一、通用的框架，这与自然语言处理（NLP）和计算机视觉（CV）的轨迹类似。这一演进经历了几个关键里程碑：

1.  **传统图学习方法**：早期方法根植于经典图论和组合优化，如最短路径计算、谱聚类和图核。这些算法在网络分析、社区检测和图匹配等领域取得了重要应用。然而，它们通常依赖手工特征，难以扩展，且缺乏学习丰富、可迁移表示的能力。

2.  **图嵌入（Graph Embedding）**：表示学习与图的结合催生了图嵌入技术。DeepWalk、node2vec和LINE等方法通过随机游走或邻域采样，将节点映射到低维连续向量空间。这些嵌入在节点分类、聚类和链接预测等下游任务中表现有效。但它们主要是transductive的，缺乏归纳泛化能力，且仅捕捉结构模式，未能考虑节点或边的属性。

3.  **图神经网络（Graph Neural Networks, GNNs）**：GNNs的引入是变革性的一步，将深度学习原理应用于非欧几里得图结构。GNNs利用message-passing机制，基于邻居节点迭代地聚合和更新节点表示。关键模型包括Graph Convolutional Networks (GCNs)、Graph Attention Networks (GATs)和GraphSAGE。尽管GNNs显著推动了该领域发展，但仍受限于过平滑（oversmoothing）、有限的感受野以及大量的任务特定架构调整需求。图2展示了图学习范式的演进，从统计方法到图嵌入，再到GNNs，显示了任务解决能力的提升。

4.  **图基础模型（Graph Foundation Models, GFMs）**：受NLP和视觉领域基础模型成功的启发，图学习近期进入了GFMs时代。这些模型在大规模图上使用self-supervised learning目标进行预训练，学习通用的、可跨任务和跨领域迁移的表示。GFMs整合了结构依赖和语义内容，展现出强大的zero-shot和few-shot泛化能力。应用领域广泛，包括分子性质预测、社交网络分析、推荐系统和知识图谱。通过将模型训练与特定任务解耦，GFMs减少了对标记数据和领域特定启发式方法的依赖，使图学习更接近通用图智能。

## 2.2 Background of Foundation Models

Foundation Models 是现代人工智能的核心，代表了从特定任务模型向高度通用系统的范式转变。它们通过在多样化、异构数据集（包括文本、图像、代码和多模态内容）上进行大规模 pre-training 来实现跨领域的可迁移能力。Foundation Models 通常基于 transformer 框架构建，利用 self-attention 机制捕捉长距离依赖并扩展至数十亿参数。例如，语言领域的 GPT、BERT、PaLM、LLaMA，以及视觉-语言任务的 CLIP、DALL-E。

Foundation Models 的核心优势在于学习通用的表示，这些表示可以通过 fine-tuning、prompting 或 instruction tuning 以最小的额外监督适应新任务。它们通过预训练获得丰富的语义、句法和结构知识，并能处理复杂和结构化数据，适用于推理、生成和分类任务。此外，Foundation Models 能够通过 in-context learning 实现强大的 few-shot 和 zero-shot learning 能力，仅凭输入 prompt 即可执行新任务，无需梯度更新。

随着模型规模和训练数据的增长，Foundation Models 开始展现 emergent behaviors，如逻辑推理、chain-of-thought generation 和 tool use。这些能力虽然展示了其作为通用 AI 系统的潜力，但也带来了数据偏见、可解释性、安全性和环境成本等挑战。

Graph Foundation Models (GFMs) 是受 Foundation Models 启发而提出的，专门用于理解和推理图结构数据。图由节点（实体）和边（关系）组成，广泛用于表示复杂系统，如社交网络、分子结构和 Knowledge Graph。GFMs 同样在大型、多样化的图数据集上进行 pre-training，以学习可迁移的通用表示，并能通过 fine-tuning 或 adaptation 应用于 node classification、link prediction 和 graph generation 等下游任务。GFMs 通过捕捉图的结构和关系属性，实现对互联数据的有效和可扩展分析。

GFMs 的关键特性包括：
*   **Pretraining on Large-Scale Graph Data**: 在广泛的图数据集上训练，学习跨领域的通用模式和结构语义。
*   **General-Purpose Representations**: 学习通用的 node、edge 和 graph 级 embeddings，可适应多种任务。
*   **Structural Awareness**: 内在地捕捉图的拓扑特征，如连通性、邻域结构和全局属性。
*   **Transferability**: 知识可跨任务和领域迁移，即使在任务特定数据有限的情况下也能表现良好。
*   **Few-shot and Zero-shot Capabilities**: 预训练后，可利用其丰富的内部表示，以极少或零标记样本执行新任务。

## 2.3 Definitions & Notations

本章节详细介绍了论文中使用的关键符号和概念。

**核心定义：**

*   **图 (Graph):** 定义为 $\mathcal{G} = (\mathcal{V},\mathcal{E})$，其中 $\mathcal{V}$ 是节点集合，$\mathcal{E}$ 是边集合， $|\mathcal{V}| = N$ 是节点数量，$|\mathcal{E}| = M$ 是边数量。邻接矩阵 $\mathbf{A}$ 用于表示节点间的连接关系，若 $(i,j)\in \mathcal{E}$，则 $\mathbf{A}_{ij} = 1$，否则为 0。节点的邻域定义为 $\mathcal{N}_v = \{u\in \mathcal{V}|(u,v)\in \mathcal{E}\}$。
*   **带属性图 (Attributed Graph):** 在图的基础上，为节点或边关联了特征信息。表示为 $\mathcal{G} = (\mathbf{X},\mathbf{A})$，其中 $\mathbf{X}\in \mathbb{R}^{N\times D}$ 是节点属性矩阵，$\mathbf{A}\in \{0,1\}^{N\times N}$ 是邻接矩阵。节点 $v_{i}$ 的原始属性向量为 $\mathbf{x}_i\in \mathbb{R}^D$。
*   **文本属性图 (Text- Attributed Graph, TAG):** 在带属性图的基础上，进一步引入了文本信息。表示为 $\mathcal{G} = (\mathbf{X},\mathbf{A},\mathbf{D})$，其中 $\mathbf{D}$ 包含了与节点、边或整个图相关的文本描述。节点 $v_{i}$ 的文本描述为 $\mathbf{d}_{v_{i}}$，边 $e_{ij}$ 的文本描述为 $\mathbf{d}_{e_{ij}}$，整个图的文本描述为 $\mathbf{d}_{G}$。

**关键技术模型：**

*   **Graph Neural Network (GNN):** 一类专门用于处理图结构数据的神经网络。GNNs 通过递归地聚合和转换局部邻域信息来学习节点、边或图级别的表示。它们能够捕捉图的结构和拓扑信息，广泛应用于 node classification, link prediction, 和 graph classification 等任务。
*   **Large Language Model (LLM):** 基于 Transformer 框架的深度神经网络，在大规模文本语料上进行预训练，以学习通用的语言表示。LLMs 能够处理文本序列或查询，并产生上下文相关的输出。它们在文本理解、生成和推理方面表现出色，并支持无需显式 fine-tuning 的下游应用。在图数据上，LLMs 可以利用文本属性进行结构感知推理。
*   **Graph Foundation Model (GFM):** 在大规模跨领域和跨任务图数据集上进行预训练的大规模模型。GFMs 通过预训练获得可迁移的知识和通用能力，展现出涌现属性和跨领域适应性，可应用于分子属性预测、推荐系统、社交网络分析和异常检测等多种图应用。

**符号约定：**

论文中，粗体大写字母表示矩阵，粗体小写字母表示向量。表格 1 详细列出了所有使用的符号及其含义，包括节点、边、属性矩阵、文本信息、学习到的节点表示、邻域集合、模型参数以及一些操作符（如集合基数 $| \cdot |$ 和拼接 $\Vert$）。此外，还定义了 GNN 和 LLM 的通用函数表示。

## 3 Challenges in Designing Graph Foundation Models

设计Graph Foundation Models (GFMs)面临三大核心挑战：特征异质性（feature heterogeneity）、结构异质性（structure heterogeneity）和任务异质性（task heterogeneity）。这些挑战共同构成了构建通用模型以适应不同图数据集和学习场景的难度。

特征异质性体现在不同图数据集中节点和边的特征类型、维度和分布差异巨大。结构异质性则源于图的拓扑结构、连通性、节点度分布以及是否存在同构或异构关系等方面的多样性。任务异质性则指GFMs需要能够处理多种下游图学习任务，如Node Classification, Link Prediction, Graph Classification, Graph Generation, Graph Anomaly Detection等。

GFMs旨在通过学习可迁移和适应性强的表示来克服这些障碍，从而在各种图设置下实现良好的泛化能力。解决这些异质性问题是GFM发展的关键。

## 3.1 Feature Heterogeneity

Feature Heterogeneity 指的是不同数据集中的节点、边或图级别的特征存在差异。这种挑战主要源于两个方面：领域特定差异和预处理不一致。

领域特定差异体现在不同领域的图数据编码了不同的语义。例如，引用网络（citation networks）代表学术关系，其特征属性包括论文标题、作者和摘要；而分子图（molecular graphs）代表化学化合物，其特征描述原子类型、键序和空间构型。

预处理不一致则源于即使在同一领域内，也可能使用不同的特征提取流程。例如，Cora 和 Pubmed 都是引用网络，但 Cora 使用 1433 维的关键词 one-hot 表示，而 Pubmed 使用 500 维的 TF-IDF 向量，这导致了不同的输入特征空间。

传统 GNNs 假设输入特征空间一致，因此不适用于处理 Feature Heterogeneity。为解决此问题，已提出多种方法，包括使用奇异值分解（SVD）将特征投影到共享的潜在空间，利用大型语言模型进行文本编码，或应用图特定的特征投影层。此外，GraphAny 提出了一种有前景的方向，即基于图上的相对信息（而非绝对信息）获取归纳式特征（inductive features）。然而，这些方法通常依赖于领域知识、手工映射或引入了可扩展性瓶颈。开发一种更通用、更自适应的异构特征对齐（heterogeneous feature alignment）解决方案仍然是一个开放的研究方向。

## 3.2 Structure Heterogeneity

结构异质性（Structure Heterogeneity）指的是图数据集之间拓扑模式的差异。这些差异对模型性能有显著影响，因为图结构在下游推理任务中起着至关重要的作用。例如，社交网络和引用网络通常表现出局部依赖性和基序（motifs），如星形中心节点（star-shaped hubs）和三角形（triangles），它们捕捉了流行度和社区结构。相比之下，分子图（molecular graphs）表现出长程依赖性，其特点是环状结构（ring structures）和 $k$-cliques，这些结构编码了化学亚结构和相互作用。这些结构模式在不同领域差异很大，这使得开发一种能够跨图类型有效泛化的 GNN 模型变得复杂。增加模型深度或容量并非充分的解决方案，因为它会引入过平滑（over-smoothing）和过压缩（over-squashing）等问题，两者都会阻碍判别性信号的传播。此外，传统 message-passing GNNs 中固有的局部性偏差限制了它们捕捉全局结构的能力。

为改善结构适应性，已提出多种技术，包括结构感知数据增强（structure-aware data augmentation）、图提示调优（graph prompt tuning）和离散结构码本（discrete structural codebooks）。然而，当前方法在适应真实世界数据中发现的全部图结构方面仍面临挑战。

## 3.3 Task Heterogeneity

本章节探讨了图学习任务的多样性（Task Heterogeneity），即不同图任务需要不同的建模策略和归纳偏置（inductive biases）。与自然语言处理（NLP）中许多任务可重构为问答不同，图任务的表述和基本假设差异很大。

*   **节点级任务 (Node-level tasks)**：旨在利用节点局部邻域信息对单个节点进行分类，成功关键在于建模节点交互中的同质性（homophily）或异质性（heterophily）。
*   **链接级任务 (Link-level tasks)**：关注预测节点对之间的边是否存在或其类型，通常依赖于邻近性度量（如共同邻居或最短路径）来推断关系模式。
*   **图级任务 (Graph-level tasks)**：要求对整个图进行整体理解，需要提取子图模式（subgraph motifs）和全局依赖关系。
*   **领域特定任务 (Domain-specific tasks)**：如知识图谱（Knowledge Graph）推理或分子生成（molecule generation），引入了独特的建模需求，进一步增加了跨任务类型的泛化难度。

为解决任务异质性问题，研究者提出了两种策略：

1.  **显式对齐 (Explicit alignment)**：将不同任务重构为统一的目标，例如链接预测（link prediction）、子图分类（subgraph classification）或树分类（tree classification）。
2.  **隐式对齐 (Implicit alignment)**：在不依赖任务特定重构的情况下，学习跨任务的通用化表示（generalizable representations）。

尽管已取得一定进展，但一个能够无缝适应各种图任务的通用 Graph Foundation Model (GFM) 仍然是一个充满挑战且尚未完全解决的目标。

## 4 A Unified Framework of Graph Foundation Models

本章提出了一个统一的Graph Foundation Models (GFMs)框架，旨在整合和发展现有的图学习方法。核心论点是，GFMs应具备强大的预训练能力、灵活的下游任务适应性以及跨领域迁移能力。

**主要内容和贡献：**

*   **GFMs的统一视角：** 章节首先回顾了图学习领域的发展，特别是Graph Neural Networks (GNNs)的演进，并指出现有方法在处理不同类型的图（如Homogeneous Graph, Heterogeneous Graph）和任务时存在碎片化的问题。本框架旨在提供一个更普适的解决方案。
*   **核心组件与设计原则：**
*   **强大的预训练（Pre-training）：** 强调了通过Self-supervised Learning（如Contrastive Learning）在海量无标签图数据上进行预训练的重要性，以学习通用的图表示（Node Embedding）。这使得模型能够捕捉图的结构和语义信息。
*   **灵活的下游任务适应性：** 提出了多种适应下游任务的方式，包括Fine-tuning、In-context Learning和Few-shot Learning/Zero-shot Learning。这使得GFMs能够高效地应用于各种图任务，如Node Classification, Link Prediction, Graph Classification, Graph Generation, Graph Anomaly Detection等，而无需从头训练。
*   **跨领域迁移能力：** 探讨了GFMs如何实现Cross-domain Transfer和Domain Adaptation，即在不同领域或不同类型图数据之间迁移学习到的知识，克服数据稀疏性或领域差异带来的挑战。
*   **模型架构与技术：** 虽然未详细展开具体模型架构，但暗示了Transformer等先进的神经网络结构在GFMs中的应用潜力，以及Message Passing机制的演变。
*   **潜在应用与未来方向：** 章节展望了GFMs在Knowledge Graph、Multi-modal Learning等领域的应用前景，并指出了未来研究方向，如处理大规模图、提升模型的可解释性以及解决Graph Isomorphism等挑战。

总而言之，本章提出的统一框架为构建更通用、更强大的Graph Foundation Models提供了理论指导和实践蓝图，强调了预训练、灵活适应和跨领域迁移是GFMs的关键特征。

## 4.1 Unified Framework

本章节介绍了Graph Foundation Models (GFMs) 的统一框架，与传统的task-specific, end-to-end的Graph Neural Networks (GNNs) 范式形成对比。GFMs的核心理念是“pretrain then adapt”，即首先在一个多样化的图数据集集合 $\mathcal{D}_{pt}$ 上对模型主干 $\theta$ 进行预训练，学习通用的图表示，然后将此预训练模型适配到各种下游任务。

预训练阶段的目标是最小化预训练目标函数 $\mathcal{L}_{pt}(\mathcal{D}_{pt};\theta)$，得到参数 $\theta^{*}$。这些参数 $\theta^{*}$ 封装了关于图结构、语义和动态的迁移知识。

预训练完成后，模型可以被直接应用于下游任务，或者通过一个额外的适配阶段来进一步提升性能。适配阶段利用与目标任务或领域相关的下游数据 $\mathcal{D}_{adapt}$，通过最小化适配损失函数 $\mathcal{L}_{adapt}(\mathcal{D}_{adapt};\theta^{*})$ 来微调预训练模型的参数，得到 $\hat{\theta}$。

该统一框架包含三个核心组件：

*   **Backbone**: 指负责处理图结构数据并学习有意义表示的基础架构。它定义了节点、边和全局上下文的编码方式，整合了结构依赖性和属性信息。有效的Backbone可以是GNNs、Transformer、LLMs甚至混合架构，对于GFMs的可扩展性、多模态集成和跨域泛化至关重要。

*   **Pretraining**: 模型从大规模、通常是无标签的图语料库中学习通用图表示的阶段。这通常通过self-supervised learning目标实现，如contrastive learning、graph masking或结构/语义属性的预测建模。目标是使模型具备对普遍图模式的丰富理解，从而促进迁移性、鲁棒性和数据效率。强大的pretraining方案为zero-shot learning和few-shot learning在多种图任务和领域中的泛化奠定基础。

*   **Adaptation**: 将预训练模型与特定下游任务或领域对齐的过程。这可以包括微调模型的所有或部分参数、使用轻量级调优方法，或添加特定任务的预测头。Adaptation阶段确保预训练的通用知识被有效利用于专业应用，从而提升任务性能、降低数据需求并促进跨不同图场景的快速部署。

![](./images/unified_framework.jpg) 图1展示了传统GNNs和GFMs之间的基本区别。

## 4.2 Backbone Architectures

GFMs 的 Backbone Architectures 旨在整合结构和语义信息，通过利用 Graph Neural Networks (GNNs) 和 large language models 的表示能力。GNNs，如 Graph Convolutional Networks (GCN) 和 Graph Attention Networks (GAT)，擅长通过 Message Passing 机制捕捉关系依赖。然而，它们在建模长距离依赖和整合多模态数据方面存在挑战。相反，LLMs 将图结构数据编码为序列，实现了泛化和可扩展性的增强，但通常缺乏显式的图归纳偏置 (graph inductive biases)，限制了其忠实表示拓扑结构的能力。为解决这些局限性，结合 GNNs 和 LMs 优势的混合方法应运而生，旨在融合结构归纳偏置和语义泛化，从而提供对图结构数据的更全面理解。

本节将系统概述 GFMs 中使用的核心骨干网络，并将其分为三个主要范式：(i) Graph Model as Predictor，(ii) Language Model as Predictor，以及 (iii) Graph-Language Co-Training。

*   **Graph Model as Predictor**: GNNs 作为主要推理引擎，可能包含可选的辅助模块。
*   **Language Model as Predictor**: LLMs 将图结构输入转换为文本或结构化提示进行解释。
*   **Graph-Language Co-Training**: 通过对齐联合优化 GNNs 和 LLMs，以增强跨任务和模态的泛化能力。

图 4 提供了这些骨干策略的分类图示。

## 4.2.1 Graph Model as Predictor

本章节探讨了Graph Model作为预测器在处理图结构数据中的作用。图模型能够学习节点间的关系依赖，将深度学习范式扩展到非欧几里得空间，在推荐系统、社交网络、分子性质预测、知识图谱和医疗分析等领域展现出强大能力。

图模型的核心是message-passing范式，通过聚合邻域信息迭代更新节点表示。其通用更新规则为：$\mathbf{h}_v^{(k)} = \mathbf{UPDATE}\left(\mathbf{h}_v^{(k - 1)},\mathbf{AGREGATE}\left(\{\mathbf{h}_u^{(k - 1)}:u\in \mathcal{N}(v)\}\right)\right)$，其中$\mathbf{h}_v^{(k)}$是节点$v$在第$k$层的特征嵌入，$\mathcal{N}(v)$是其邻居集合。不同的图模型通过不同的AGGREGATE和UPDATE函数实现信息传播和转换。例如，Graph Convolutional Networks (GCNs)采用归一化求和进行聚合，而Graph Attention Networks (GATs)则利用attention机制为邻居节点分配重要性得分$\alpha_{vu}$。

近期研究通过引入Transformer的全局attention机制，增强了GNNs的表达能力。Graph Transformers用图中所有节点的attention来替代局部聚合，从而捕捉长距离依赖：$\mathbf{h}_v^{(k)} = \sum_{u\in \mathcal{V}}\alpha_{vu}\cdot \mathbf{W}\mathbf{h}_u^{(k - 1)}$，其中$\alpha_{vu}$是节点$v$对节点$u$的attention权重。

一些Graph Foundation Models (GFMs)采用纯图模型作为骨干，仅依赖结构信号。例如，MINIMOL为分子性质预测设计了参数高效的GNN，JMP提出了一种分层表示方案，使用度归一化公式更新节点嵌入。这些方法在具有丰富关系信号的领域表现出色，但在需要多模态推理或外部上下文知识的场景下可能面临挑战。

为克服纯GNN的局限性，一些方法引入了辅助语言模型。这些混合方法能够将非结构化文本知识整合到图表示学习中。主要策略包括：(i) 在图编码前使用LLMs增强节点特征，例如TAPE通过LLM-to-LM解释器提取任务相关的文本解释，并将其转换为结构化节点特征$\mathbf{h}_v = f_{\mathrm{LM}}(\mathbf{e}_v)$；(ii) 使用LLMs直接编码纯图结构，例如OFA提出统一的文本模板来对齐不同的图节点描述，并使用预训练LM将其编码到共享嵌入空间，从而实现跨域的zero-shot generalization。这些辅助增强的图模型展示了混合架构的灵活性和有效性，能够在一个统一的学习框架中整合结构和语义信号。

## 4.2.2 Language Model as Predictor

本章节探讨了语言模型（Language Models）作为图学习任务的预测器。语言模型，最初用于自然语言处理任务，现已广泛应用于图学习领域，通过大型预训练模型实现结构化数据的编码、推理和泛化。

**核心论点：** 语言模型能够通过将图结构转化为序列表示，实现图推理，无需依赖Graph Neural Networks (GNNs)。同时，通过引入辅助模块，可以增强语言模型对图结构的理解能力。

**方法与结果：**

1.  **独立语言模型作为图预测器：**
*   **方法：** 将图结构序列化为文本输入，使大型语言模型（LLMs）能够解析节点信息、特征和关系。转换过程包括将每个节点、其特征及其邻域编码为结构化序列（如公式7所示）。
*   **示例：** LangGFM将图转换为自然语言模板，证明LLMs可在无显式图操作的情况下进行结构模式推理。BeyondText验证了LLMs通过文本提示恢复图拓扑和关系依赖的能力。GLM利用强化学习优化prompt engineering，以适应图推理。
*   **挑战：** 纯LLM方法可能难以内化结构归纳偏差，尤其对于拓扑丰富的图或文本信号较弱的情况。

2.  **带辅助模块的语言模型：**
*   **方法：** VLM-style架构通过跨模态对齐、图感知tokenization和辅助编码器来增强语言模型，显式地整合图结构。这些混合架构使用图模型来指导或条件化LLMs，促进结构感知的语言理解。常见流程是通过GNN编码图，并将节点embedding投影到LLM的token空间（如公式8所示）。
*   **示例：** GraphGPT通过instruction tuning和contrastive learning来对齐图和语言表示。GraphTranslator引入了结构感知正则化，以减少模态间的语义漂移。LLaGA通过检索模块提取与任务相关的子图，增强推理能力，确保LLM关注重要的关系模式。
*   **归类：** 这些方法虽然以LLM为中心，但依赖于GNN组件，因此被归类为GNN+LLM混合范式。

**总结：** 语言模型在图学习中展现出巨大潜力，无论是独立作为预测器，还是通过辅助模块增强其图感知能力。未来的研究方向可能包括结构化tokenization、检索机制和任务特定fine-tuning，以构建更强大的混合VLM-style框架。

## 4.2.3 Graph-Language Co-Training

Graph-Language Co-Training 是一种双向学习框架，整合了图结构建模和语言语义推理。与单模态主导的辅助方法不同，co-training 将图模型和语言模型视为同等重要的组成部分，促进互表征学习。该领域主要有两种范式：（i）Graph-Language Alignment，通过 contrastive learning 强制建立共享的潜在空间；（ii）Graph-Language Iterative Update，通过多阶段或变分目标联合优化图和语言表征。

Graph-Language Alignment 方法将结构化和非结构化表征映射到共享的 embedding space。受 vision-language modeling 中 CLIP 式训练的启发，GraphCLIP [104] 提出了一种双编码器框架，包含一个 GNN encoder $f^{\mathrm{GNN}}$ 和一个语言 encoder $f^{\mathrm{LLM}}$。给定一个图 $\mathcal{G} = (\mathcal{V},\mathcal{E},\mathbf{X})$ 和相应的节点描述，通过 contrastive loss 学习表征：
$$
\mathcal{L}_{\mathrm{clip}} = -\sum_{(v_i,v_j)\in \mathcal{P}}\log \frac{\exp(\sin(\mathbf{h}_{v_i}^{\mathrm{GNN}},\mathbf{h}_{v_j}^{\mathrm{LLM}}) / \tau)}{\sum_{w\in\mathcal{V}}\exp(\sin(\mathbf{h}_{v_i}^{\mathrm{GNN}},\mathbf{h}_w^{\mathrm{LLM}}) / \tau)}, \tag{9}
$$
其中 $\sin (\cdot ,\cdot)$ 表示相似度（如 cosine），$\mathcal{P}$ 是对齐的节点-文本对集合，$\tau$ 是温度参数。ConGraT [105] 通过跨模态监督扩展了这一思想，其中 GNN 增强了文本衍生的特征。这些方法通过统一它们的表征空间来提高图-文本对的泛化能力。

Graph-Language Iterative Update 超越了 contrastive alignment，通过连续细化实现图模型和语言模型之间的动态交互。GLEM [106] 通过引入一个潜在变量 $\mathbf{z}_v$ 来表示文本和结构输入的共享语义，展示了这种方法。生成过程建模为：
$$
p(\mathbf{h}_v|\mathcal{G}) = \int p(\mathbf{h}_v|\mathbf{z}_v,\mathcal{G})\cdot p(\mathbf{z}_v|\mathcal{G})d\mathbf{z}_v, \tag{10}
$$
其中 $\mathbf{z}_v$ 作为整合模态的桥梁。该模型遵循 EM-style 优化，通过文本伪标签更新语义特征，并通过图传播细化拓扑 embedding，进行交替更新。这种迭代机制提供了更具表现力的模态融合，实现了图和语言表征的协同演进，并提高了在文本属性图上的性能。

## 4.2.4 Discussion

Graph Foundation Models (GFMs) 的骨干架构可分为三类：Graph Models、Language Models 和 Hybrid Models。Graph-based backbones 提供结构保真度和效率；Language-based backbones 提供泛化能力和多模态灵活性；Hybrid models 实现全面的推理，但需要更复杂的训练流程。

Graph-based backbones（如 GNNs, Graph Transformers）与图数据的结构天然契合。通过 message-passing 或 attention-based aggregation 显式建模节点邻域，这些架构保留了局部连通性和关系信息，在 node classification, link prediction, graph classification 等任务中表现出色。与 language-based 骨干相比，它们通常更具参数效率。然而，它们也存在局限性：局部性诱导偏差难以捕捉长距离依赖；整合文本或多模态信息仍具挑战性，常需辅助编码器或临时融合机制。

Language-based backbones 通过将图组件（如节点属性、边描述或子图模式）编码为自然语言来利用 LLMs。这种 graph-to-text 的表述使强大的语言理解能力迁移到图学习任务中。当图数据富含文本元数据时（如 knowledge graphs, social networks, biomedical corpora），Language-based models 特别有用，其泛化能力也使其适用于 zero-shot 和 few-shot learning。尽管如此，这些模型缺乏显式的结构诱导偏差，依赖于顺序表示，可能模糊拓扑细节，并在需要精确关系推理的任务中表现不佳。

Hybrid backbones 集成了 graph-based 和 language-based 架构，旨在结合两者的优势。这些模型通常包含通过 co-training、cross-modal attention 或 alignment objectives 交互的双编码器（如 GNNs 和 LLMs）。Hybrid approaches 通过联合建模结构和语义，在多样化任务中展现出令人印象深刻的性能。例如，graph encoders 可捕捉连通性骨架，而 LLMs 则编码描述性上下文或领域特定知识。然而，这种协同效应是有代价的：Hybrid models 通常需要复杂的架构设计、增加的内存和计算开销，以及仔细的 pretraining 或 alignment 策略，以避免 modality collapse 或 overfitting。

## 4.3 Pretraining Strategies

本节概述了Graph Foundation Models (GFMs) 的关键预训练范式，旨在从大规模无标签或弱标签数据中获取可迁移知识。主要策略包括：

1.  **Supervised Pretraining**: 利用从大规模图中提取的带标签子图进行预训练，通过监督目标引导学习过程。
2.  **Generative Pretraining**: 模型学习重构图中被掩盖或损坏的部分（如节点特征或邻接信息），通常采用自回归或自编码范式来捕捉高阶依赖。
3.  **Contrastive Pretraining**: 模型通过区分图的不同视图或增强下的相似（正例）和不相似（负例）节点或子图对进行训练，从而学习不变性和可迁移的表示。

这些策略如图5所示。

## 4.3.1 Supervised Pretraining

监督式预训练是一种利用带标签图数据指导模型预训练的策略。与仅依赖内在图信号的self-supervised methods不同，监督式预训练直接优化模型以预测已知标签，从而从一开始就学习与任务相关的表示。具体而言，令$\mathcal{G}_{\mathrm{pt}}$表示一个具有相关监督$\mathcal{V}$的大规模预训练图，其中$\mathcal{V}$可能对应于node-level、edge-level或graph-level标签。模型通过最小化这些带标签图实例上的监督损失函数进行训练：$\theta^{*} = \arg \min_{\theta}\mathcal{L}_{\mathrm{pt}}(f(\mathcal{G}_{\mathrm{pt}};\theta),\mathcal{Y})$，其中$\mathcal{L}_{\mathrm{pt}}$通常是任务特定的损失，如分类的cross-entropy和回归的mean-average error。

监督式预训练的核心优势在于其与下游目标的直接对齐，这通常能带来更快的收敛速度和在相似任务上更优的性能。遵循此范式的代表性方法包括OFA [22]，它引入了一种使用nodes-of-interest的统一任务表述来标准化各种graph prediction tasks；以及Prodigy [108]，它通过结构和语义分解生成subgraph tasks。这些方法展示了监督式预训练在捕捉不同图域的局部和全局信号方面的灵活性。

尽管有效，监督式预训练常受限于大规模、高质量标签的可用性和获取成本[107]。因此，它常与self-supervised learning结合，以增强泛化能力并减少对带标签数据的依赖。

## 4.3.2 Generative Pretraining

Generative pretraining 是一种基础的 foundation model 学习范式，其核心思想是通过训练模型预测或生成原始数据来学习通用的表示，而无需任务特定的标签。这种方法假设通过建模数据分布本身，模型可以获得广泛、可迁移的知识，并通过 fine-tuning 或 prompting 适应各种下游任务。

**核心目标**:
Generative pretraining 的目标是最大化参数化模型 $f_{\theta}$ 下观测数据 $\mathcal{D} = \{x_1,x_2,\ldots ,x_N\}$ 的似然性：
$$
\theta^{*} = \arg \max_{\theta}\sum_{i = 1}^{N}\log p(x_{i};\theta), \tag{12}
$$
其中 $x_i$ 是单个数据样本，$p(x_i;\theta)$ 是生成 $x_i$ 的估计概率。

**主要方法**:

1.  **Auto-Regressive Generation**:
*   **原理**: Autoregressive modeling 将联合概率分布分解为一系列条件概率的乘积，即 $p_{\theta}(\mathbf{x}) = \prod_{t = 1}^{T}p_{\theta}(x_t\mid \mathbf{x}_{< t})$，其中 $\mathbf{x}_{< t}$ 是序列中所有前置元素。这种方法在自然语言处理（如 GPT）和计算机视觉中广泛应用。
*   **在图领域的应用**: 将图映射为序列，通过节点排序方案实现。给定一个图 $\mathcal{G} = (\mathbf{X},\mathbf{A})$ 和一个节点排列 $\pi$，图被转化为序列 $\mathbf{S}^{\pi} = (\mathbf{S}_{1}^{\pi},\ldots ,\mathbf{S}_{n}^{\pi})$，其中 $\mathbf{S}_i^{\pi}$ 编码了节点 $\pi (v_{i})$ 与其前置节点 $\pi (v_{j}),j< i$ 的连接。生成过程遵循自回归分解：$p(\mathbf{S}^\pi) = \prod_{i = 1}^{n}p(\mathbf{S}_i\mid \mathbf{S}_{< i})$。每一步生成一个新节点及其连接，模型通过隐藏状态 $h_i$ 总结生成历史，并用 $f_{\mathrm{trans}}$（如 RNNs 或 Transformer）和 $f_{\mathrm{out}}$ 来参数化输出。
*   **代表性工作**: GraphRNN, MolecularRNN, GraphGPT。一些工作也扩展到边级别的自回归。

2.  **Auto-Encoding Generation**:
*   **原理**: 借鉴 BERT 等模型的 masked modeling 策略，目标是根据可见上下文重构输入中被 mask 或损坏的部分。形式化表示为：$p_{\theta}(\mathbf{x}) = \prod_{t\in \mathcal{M}}p_{\theta}(x_t\mid \mathbf{x}_{\setminus \mathcal{M}})$，其中 $\mathcal{M}$ 是被 mask 的索引集合，$\mathbf{x}_{\setminus \mathcal{M}}$ 是可见的 token。
*   **在图领域的应用**: Graph Auto-Encoders (GAEs) 采用类似的 masked modeling 策略，通过预测被 mask 的图组件（如节点特征、边特征或结构）来训练模型，条件是可见的图上下文。给定一个属性图 $\mathcal{G} = (\mathbf{X},\mathbf{A})$，通过 masking 或 augmentation 函数 $\mathcal{T}$ 得到损坏版本 $\widetilde{\mathcal{G}} = (\widetilde{\mathbf{X}},\widetilde{\mathbf{A}})$。使用 GNN-based encoder 得到潜在表示 $\widetilde{\mathbf{Z}} = f_{\mathrm{GNN}}(\widetilde{\mathcal{G}};\theta)$，然后通过预测头重构被 mask 的组件。
*   **Masked Feature Modeling**: 重构被 mask 的节点或边属性：$\theta^{*} = \arg \min_{\theta}\mathcal{L}_{\mathrm{opt}}\left(p(\widetilde{\mathbf{Z}}),\mathbf{X}_{\mathcal{M}}\right)$。
*   **Masked Structure Modeling**: 恢复被 mask 的链接或邻接项：$\theta^{*} = \arg \min_{\theta}\mathcal{L}_{\mathrm{opt}}\left(p(\widetilde{\mathbf{Z}}),\mathbf{A}_{\mathcal{M}}\right)$。

Generative pretraining 通过这两种方法，旨在学习能够捕捉数据内在分布和结构的通用表示，为后续的 fine-tuning、in-context learning 或 few-shot learning 任务奠定基础。

## 4.3.3 Contrastive Pretraining

Contrastive pretraining 是一种 self-supervised learning 范式，旨在通过对比 positive pairs 和 negative pairs 来学习 discriminative representations。其核心思想是将语义相似的表示在 embedding space 中拉近，将不相似的表示推远，从而使模型能够捕捉有意义且可泛化的特征，而无需人工标注。对于一个数据集 $\mathcal{D} = \{x_i\}_{i = 1}^N$，$(x_i,x_i^+)$ 表示一个 positive pair（例如同一实例的不同视图或增强），而 $(x_i,x_j^- )$ 表示一个 negative pair，其中 $x_j^-\neq x_i$。常用的目标函数是 InfoNCE loss [128]，其公式为：
$$
\mathcal{L}_{\mathrm{Inf o N C E}} = -\sum_{i = 1}^{N}\log \frac{\exp(\sin(f(x_{i}),f(x_{i}^{+})) / \tau)}{\sum_{j = 1}^{N}\exp(\sin(f(x_{i}),f(x_{j}^{-})) / \tau)}, \tag{19}
$$
其中 $f(\cdot)$ 是 encoder network，$\sin (\cdot ,\cdot)$ 是相似度函数（如 cosine similarity），$\tau$ 是 temperature parameter。通过优化此目标，模型能够区分语义相关和不相关的样本，从而学习到能够很好地迁移到各种 downstream tasks 的表示。

根据对比的层级，我们将现有的 contrastive pretraining 方法分为 instance-instance 和 instance-context 对比方法。

**Instance-Instance Contrastive Learning**

Instance-instance contrastive learning 侧重于比较单个实例。其关键思想是使同一实例在不同视图下的表示在 embedding space 中靠近（positive pairs），同时将不同实例的表示推开（negative pairs）。这与 instance-to-context learning 不同，后者旨在将一个实例与更广泛的语义上下文（如 prototypes、clusters 或 class-level embeddings）对齐 [137, 130]。Instance-instance 范式将每个实例视为其自身的类别，从而产生 instance-discriminative embeddings，这些 embeddings 在 downstream tasks 中具有高度的可泛化性。

在 graph 领域，许多工作 [138, 139, 140, 23, 141, 142, 143, 144] 展示了在 graph-structured data 上进行 instance-instance contrastive learning 的标准流程。典型流程是首先对给定的 graph $\mathcal{G} = (\mathbf{X},\mathbf{A})$ 应用两个随机增强 $t_1,t_2\sim \mathcal{T}$，生成两个视图 $\widetilde{\mathcal{G}}_1$ 和 $\widetilde{\mathcal{G}}_2$。
$$
\widetilde{\mathcal{G}}_{*} = (\widetilde{\mathbf{X}}_{*},\widetilde{\mathbf{A}}_{*}) = t_{*}(\mathbf{X},\mathbf{A}),\quad \mathbf{Z}_{*} = f(\widetilde{\mathcal{G}}_{*};\theta), \tag{20}
$$
其中 $*$ 表示视图索引（1 或 2），$\mathbf{Z}_{*}$ 包含对应增强图的 node-level embeddings。

对于 graph $\mathcal{G}$ 中的每个节点 $v_{i}\in \mathcal{G}$，选择一组 positive counterparts $\mathbb{P}(v_i)$，通常是同一节点在不同视图下的表示。训练目标是使用 InfoNCE loss [128]（Equation 19）来最大化 positive pairs 之间的一致性，同时最小化与其他所有样本的一致性。

当不显式使用 negative samples 时（如 BGRL [145]），会采用一种 bootstrapped 替代方法，避免了与 negative instances 的直接对比。这种 bootstrapping loss 定义为：
$$
\mathcal{L}_{\mathrm{Bootstrap}} = -\sum_{i = 1}^{N}\operatorname {sim}(f(x_i),\operatorname {sg}g([f(x_i^+)])), \tag{21}
$$
其中 $g(\cdot)$ 是一个 projector，$\operatorname {sg}[\cdot ]$ 表示 stop-gradient 操作。

尽管 instance-instance contrastive learning 在 graph representation learning 中取得了显著成果，但一个值得注意的局限性在于其假设 positive sample 仅仅是不同增强下的同一节点。这种假设可能引入 sampling bias，尤其是在具有噪声结构或弱 homophily 的图中。解决 positive sample 选择的挑战以及探索更语义对齐的对比对，仍然是提高 graph contrastive learning 方法鲁棒性和泛化性的重要方向 [146]。

**Instance-Context Contrastive Learning**

除了 instance-instance contrastive learning，另一种互补的范式是 instance-context contrastive learning，它旨在最大化局部（instance-level）和全局（context-level）表示之间的 mutual information [130, 143, 147, 148]。与 instance-instance 方法不同（该方法区分节点或子图的个体视图），instance-context contrastive learning 鼓励节点（或子结构）与图的全局摘要对齐，从而有助于捕捉整体的 graph-level semantics。

在 graph 领域，这一思想首次由 Deep Graph Infomax (DGI) [137] 提出，它将 Deep InfoMax 框架 [149] 应用于 graph-structured data。DGI 提出最大化节点表示与全局 summary vector 之间的 local-global mutual information，从而使 encoder 能够学习到在整个图的结构和语义中具有上下文基础的 node embeddings。形式上，给定一个 graph $\mathcal{G} = (\mathbf{X},\mathbf{A})$ 和一个随机增强 $t\sim \mathcal{T}$ 生成一个 corrupted graph $\widetilde{\mathcal{G}} = (\widetilde{\mathbf{X}},\widetilde{\mathbf{A}})$，使用 encoder $f(\cdot)$ 将原始图和 corrupted graph 映射到 latent space：
$$
\mathbf{Z} = f(\mathcal{G};\theta),\quad \widetilde{\mathbf{Z}} = f(\widetilde{\mathcal{G}};\theta), \tag{22}
$$
其中 $\mathbf{Z} = [\mathbf{z}_1,\ldots ,\mathbf{z}_N]$ 和 $\widetilde{\mathbf{Z}} = [\widetilde{\mathbf{z}}_1,\ldots ,\widetilde{\mathbf{z}}_M]$ 分别表示原始图和 corrupted graph 的 node embeddings。为了计算一个 graph-level summary vector，将一个 permutation-invariant readout function $\mathcal{R}(\cdot)$ 应用于原始 node embeddings $\mathbf{s} = \mathcal{R}(\widetilde{\mathbf{Z}})$，其中 $\mathbf{s}$ 作为图的全局上下文 embedding。

对比目标被定义为区分来自原始图的 positive pairs $(\mathbf{z}_i,\mathbf{s})$ 和来自 corrupted graph 的 negative pairs $(\widetilde{\mathbf{z}}_j,\mathbf{s})$。训练一个 discriminator $\mathcal{D}(\cdot ,\cdot)$ 来为 positive pairs 分配高分，为 negative pairs 分配低分。训练目标为：
$$
\mathcal{L}_{\mathrm{DGI}} = -\frac{1}{N + M}\left(\sum_{i = 1}^{N}\log \mathcal{D}(\mathbf{z}_i,\mathbf{s}) + \sum_{j = 1}^{M}\log \left(1 - \mathcal{D}(\widetilde{\mathbf{z}}_j,\mathbf{s})\right)\right), \tag{23}
$$
其中 $N$ 和 $M$ 分别是原始图和 corrupted graph 中的节点数量。这个 local-global 目标鼓励模型学习不仅局部表达性强，而且全局意识强的表示。近期的扩展通过整合额外的结构先验（如从 information bottleneck 角度的 structural mutual information [150]）或针对 low-resource settings（如 few-shot node classification [151]）调整方法，对 DGI 进行了改进。

## 4.3.4 Discussion

Graph Foundation Models (GFMs) 的 pretraining 是提升 generalization 和 transferability 的关键，尤其是在多样化的 graph learning tasks 中。不同的 pretraining paradigm 各有优劣，取决于 underlying assumptions, supervision signals, 和 application scenarios。

- **Supervised Pretraining** 直接利用 labeled graph data 进行模型优化，能够产生 task-aligned 和 semantically rich 的 representations。当 pretraining task 与 downstream objectives 高度匹配时，此方法效果显著，能加速 convergence 并提升 performance。然而，其主要限制在于对 large-scale, high-quality labeled datasets 的依赖，获取这些数据成本高昂且耗时，限制了其 scalability 和 generality。

- **Generative Pretraining**（包括 auto-regressive modeling 和 auto-encoding modeling）通过 reconstruction objectives 来学习 graph data 的 underlying structure。这类方法仅依赖输入数据本身，实现了 label-free pretraining at scale。其核心优势在于灵活且可扩展的框架，比 contrastive learning 更高效。但 generative models 可能缺乏 strong task specificity，且其 reconstruction-based objectives 与 downstream performance 的关联性并非总是直接。

- **Contrastive Pretraining** 因其简洁性和学习 discriminative graph representations 的有效性而广受欢迎。Instance-instance contrastive learning 通过区分 positive 和 negative pairs 来生成 fine-grained embeddings，而 instance-context contrastive learning 则侧重于将 local representations 与 global summaries 对齐。在 graphs 上，这些方法通常优于 generative models [121]。尽管如此，contrastive methods 对 augmentations 的选择、sampling strategies 以及 informative negatives 的可用性非常敏感。此外，计算 contrastive loss 可能计算量巨大，尤其是在 modeling large 或 densely connected graphs 时。

## 4.4 Adaptation

本节全面概述了Graph Foundation Models (GFMs) 的Adaptation策略，重点介绍了预训练模型如何有效地应用于各种下游任务。这些策略被归纳为六种主要范式：transfer learning、distillation、test-time adaptation、graph prompting、in-context learning 和 prototype learning。每种范式都根据特定的数据条件、监督水平和部署约束进行了定制。

## 4.4.1 Transfer Learning

Transfer learning 是现代机器学习中的一个基础范式，它将一个在大型源数据集上预训练的模型适配到一个具有有限标记数据的新目标领域。在 Graph Foundation Models (GFMs) 的背景下，transfer learning 能够重用在大规模预训练过程中获得的结构和语义知识，从而提高在下游图相关任务上的性能和泛化能力。其核心思想是使用预训练参数初始化模型，从而利用学习到的表示并降低过拟合的风险，这在数据有限的情况下尤其有益。根据适配策略，预训练的 GFM 可以直接应用于下游任务，也可以使用特定任务的监督进行进一步的 fine-tuning。

**直接适配 (Direct Adaptation)**：在直接适配中，预训练的 GFM 在没有任何参数更新的情况下应用于下游任务。这种 zero-shot 设置以即插即用的方式评估了预训练模型的泛化能力。例如，OFA [22] 引入了一个统一的框架，将图数据转换为文本提示 (textual prompts)，并利用预训练的 LLMs 进行图推理。它通过附加一个虚拟提示节点及其关系到原始图来构建一个 prompt graph $\mathcal{P} = (\mathcal{V}_p,\mathcal{E}_p,\mathcal{R}_p)$，从而实现无需任务特定 fine-tuning 的 in-context learning。

**全量微调 (Full Fine-Tuning)**：全量微调涉及在目标任务上更新预训练模型的所有参数。这种方法提供了最大的灵活性和适配能力，但在目标数据集较小或存在噪声时可能导致过拟合。通常在下游任务与预训练目标有显著差异，或者对任务特定精度要求极高时采用 [9]。

![](https://picsheep.oss-cn-beijing.aliyuncs.com/pic/c90c57a106ec977f8197bc4611f59e9923b7c21fd21dacb533d68bc3d13bfd20_b3e6c4d1.jpg)
Figure 6：图基础模型的适配策略。我们展示了将预训练 GFM 适配到下游任务的六种代表性范式：(a) 通过 fine-tuning 进行 Transfer Learning；(b) 蒸馏到更小的 student model；(c) 无需标记数据的 Test-Time Adaptation；(d) 通过可学习的 prompt 向量进行 Graph Prompting；(e) 使用 demonstration sets 进行 In-Context Learning；以及 (f) 通过 class prototype 对齐进行 Prototype Learning。这些策略支持不同级别的监督、泛化和计算效率。

**自适应微调 (Adaptive Fine-Tuning)**：自适应微调旨在根据目标任务的特性，选择性地更新模型中的特定层、模块或参数。这种选择性调整可以降低计算成本并缓解过拟合。AUX-TS [152] 通过动态选择与目标任务语义相似的辅助任务来例证这一范式。相似度分数被学习并用于在 fine-tuning 过程中对每个辅助信号进行加权，从而实现任务感知的适配。

**参数高效微调 (Parameter-Efficient Fine-Tuning, PEFT)**：PEFT 技术旨在保留预训练模型的泛化能力，同时显著减少可训练参数的数量。这些方法通常冻结 backbone 模型，并引入轻量级模块，如 adapters 或 low-rank transformations。例如，AdapterGNN [153] 将一个 adapter 模块集成到 GNN 层中，其变换定义为 $\mathbf{A}(\mathbf{x}) = \mathrm{BN}(\mathbf{W}_{\mathrm{up}}\cdot \mathrm{ReLU}(\mathbf{W}_{\mathrm{down}}\cdot \mathbf{x}))$，其中 $\mathbf{W}_{\mathrm{down}}$ 和 $\mathbf{W}_{\mathrm{up}}$ 是可训练的低维投影，BN 表示 batch normalization。类似地，GraphLoRA [154] 应用 low-rank adaptation 来降低参数复杂度，而 GPF [155] 引入一个可学习的任务特定向量 $\mathbf{p}$，该向量被连接到节点特征 $\mathbf{x}_i$，同时冻结 backbone GNN。

## 4.4.2 Distillation

知识蒸馏是一种模型压缩技术，旨在将大型、强大的模型（teacher）所编码的知识转移到更小、更高效的模型（student）中。在Graph Foundation Models (GFMs) 的背景下，知识蒸馏可以部署紧凑的模型，这些模型在保持竞争力的性能的同时，还能减少推理时间和资源消耗。

蒸馏的目标通常结合了来自真实标签的监督和来自teacher模型输出的指导。其损失函数可以表示为：
$$
\mathcal{L}_{\mathrm{distilion}} = \lambda \mathcal{L}_{\mathrm{true}}(f_{\mathrm{student}}(\mathbf{A},\mathbf{X}),D_{\mathrm{target}}) + (1 - \lambda)\mathcal{L}_{\mathrm{match}}(f_{\mathrm{student}}(\mathbf{A},\mathbf{X}),f_{\mathrm{teacher}}(\mathbf{A},\mathbf{X})), \tag{26}
$$
其中 $\mathcal{L}_{\mathrm{true}}$ 是关于真实标签的监督损失，$\mathcal{L}_{\mathrm{match}}$ 衡量student和teacher输出之间的差异（例如，通常使用Kullback-Leibler divergence），而 $\lambda \in [0,1]$ 平衡两项的贡献。

蒸馏的原理在于，teacher模型的输出（通常称为“soft targets”）比one-hot标签包含更丰富的监督信号，这些信号包括类间相似性和决策边界信息，而这些信息对于student模型直接从数据中推断是困难的。此外，teacher模型中的中间表示（例如，node embedding或attention maps）可以通过特征层面的对齐来进一步增强student模型的学习。

在图领域，蒸馏技术已被扩展以整合结构和关系知识。例如，G-CRD [159] 提出了一种对比表示蒸馏框架，该框架可以保留全局图拓扑。G-CRD不局限于匹配最终预测，而是通过最大化共享表示空间中的一致性来对齐student和teacher的node embedding，从而有效地传递拓扑线索。除了预测层级和embedding层级的监督外，其他蒸馏策略包括：

*   **Graph Structure Distillation**: 在student模型中保留邻接关系、边重要性或motif分布等关系模式 [160, 161, 158]。
*   **Attention-Based Distillation**: 模仿图注意力模型（如GAT）学习到的attention maps，以保留邻居的重要性 [162, 163]。
*   **Multi-View or Multi-Task Distillation**: 从辅助任务或图的不同视图转移知识，以提高鲁棒性 [164, 165, 166]。

## 4.4.3 Test-Time Adaptation

Test-Time Adaptation (TTA) 是一种在推理阶段利用测试数据实时更新预训练 Graph Foundation Models (GFMs) 的过程。与在部署前进行的 fine-tuning 和 distillation 不同，TTA 完全在推理时进行。这种范式特别适用于训练和测试数据存在 distributional shifts 或目标域样本有限/不可用的场景。TTA 通常通过在线方式调整模型参数，即在处理每个新的测试样本或批次时进行。

TTA 的核心思想是，传入的测试数据本身包含有助于将模型适配到目标分布的有用信号。通过利用这些数据进行实时适配，模型可以动态地适应 distributional shifts，增强鲁棒性，并提高预测准确性，而无需重新训练或访问源域数据。

一种 TTA 方法是 Graph Transformation-Based Adaptation，例如 GTRANS [171]。GTRANS 是一种数据中心的方法，它在测试时进行图的精炼。它不直接更新模型参数，而是修改输入图以更好地适应固定的、预训练的 GNN。GTRANS 通过学习对节点特征和图拓扑的扰动来最小化一个 surrogate loss，从而生成一个更兼容预训练模型的适配图 $\mathcal{G}^{\prime}$。这种方法通过精炼输入数据而非模型来提高性能。

另一种 TTA 方法是 Test-Time Supervision，例如 LLM-TTT [172]。该方法利用 LLMs 的生成和标注能力来辅助文本属性图的推理。在该框架中，LLMs 用于为未标记的测试节点生成 pseudo-labels，然后这些 pseudo-labels 被用来在测试时适配 GNN。这个两阶段的流程包括：(i) LLM 利用节点描述和图上下文进行标注，(ii) 使用生成的 pseudo-labels 对 GNN 进行精炼。这种策略展示了基于语言的监督与基于图的推理之间的协同作用，在测试时约束下提高了性能，且无需手动标注。

## 4.4.4 Graph Prompting

Graph prompting 是一种新兴范式，它从数据中心视角调整 Graph Foundation Models (GFMs) 以适应下游任务。与更新模型参数的传统 fine-tuning 不同，graph prompting 保持模型冻结，而是学习额外的 prompt vectors $\mathcal{P}$ 来指导模型行为。这种方法借鉴了 NLP 中的 prompting 策略，即精心设计的输入可以引发大型语言模型的期望行为。Graph prompting 方法可分为两大类：数据级 prompting (data-level prompting)，它修改输入图数据；以及表示级 prompting (representation-level prompting)，它调整模型内部的表示。

数据级 prompting 通过将可学习信号注入特征空间或结构来调整输入图。给定一个图 $\mathcal{G} = (\mathbf{X},\mathbf{A})$，其中 $\mathbf{X}$ 是节点特征矩阵，$\mathbf{A}$ 是邻接矩阵，数据级 prompting 定义一个变换函数 $t_D$，使用 prompt vectors $\mathcal{P}$ 生成一个 prompted graph $\widetilde{\mathcal{G}} = (\widetilde{\mathbf{X}},\widetilde{\mathbf{A}})$。一种简单有效的策略是仅修改节点特征，为每个节点 $v \in V$ 学习一个 prompt vector $\mathbf{p}_v$ 并将其加到原始特征向量上：$\widetilde{\mathbf{x}}_v = \mathbf{x}_v + \mathbf{p}_v$。为降低复杂度，一些方法对所有节点使用共享的 prompt vector，即 $\mathbf{p}_1 = \mathbf{p}_2 = \dots = \mathbf{p}_N = \mathbf{p}$。然而，共享 prompts 可能缺乏表达能力。为解决此问题，近期研究引入了基于注意力机制的方法，该机制作用于一组基向量 $\{\mathbf{b}_1,\ldots ,\mathbf{b}_J\}$。每个节点特定的 prompt 计算为加权组合 $\widetilde{\mathbf{x}}_v = \mathbf{x}_v + \mathbf{p}_v = \mathbf{x}_v + \sum_{j = 1}^{J}w_{v,j}\cdot \mathbf{b}_j$，其中 $w_{v,j}$ 表示节点 $v$ 对基向量 $J$ 的学习注意力权重。另一种策略是插入式 prompting (insertion-based prompting)，它将可学习的 prompt nodes 引入图。这些 prompt nodes 与现有图节点统一连接或基于相似性度量连接，从而生成一个增强的结构，鼓励模型关注与任务相关的子图。

表示级 prompting 修改节点本身的潜在表示，而非输入图。给定节点 $v$ 的隐藏表示 $\mathbf{h}_v$，一个变换函数 $t_R$ 应用学习到的 prompts 来获得一个 prompted embedding：$\widetilde{\mathbf{h}}_v = t_F(\mathbf{h}_v;\mathcal{P})$。一种常见方法是在表示和 prompt vector 之间应用逐元素（Hadamard）乘积 $\widetilde{\mathbf{h}}_v = \mathbf{p}_v\odot \mathbf{h}_v$，其中 $\mathbf{p}_v$ 充当门控向量，突出 $\mathbf{h}_v$ 中与任务相关的维度。与数据级 prompting 类似，$\mathbf{p}_v$ 可以跨节点共享，或以节点特定的方式生成。例如，ProNoG [182] 根据每个节点的 multi-hop ego-networks 计算 prompt vectors，实现局部和个性化的调整。

## 4.4.5 In-Context Learning

In-Context Learning (ICL) 是一种 few-shot learning 方法，允许 LLMs 在不更新参数的情况下适应新任务。它通过在输入序列中提供少量输入-标签对（称为 demonstrations）来 conditioning 模型，而不是进行 fine-tuning。ICL 利用了预训练语言模型（如 GPT-3）强大的 in-context generalization 能力。形式上，给定一个 demonstration set $\mathcal{C}_K = \{(q_k,y_k)\}_{k = 1}^K$，其中 $(q_{k},y_{k})$ 是一个 query 及其对应的 label，对于新 query $q_{v}$，foundation model $f$ 使用 $\mathcal{C}_K$ 生成预测标签 $\hat{y}_v = f(\mathcal{C}_K,q_v)$。模型通过 conditioning 在 $\mathcal{C}_K$ 中的示例作为 contextual guidance 来进行 inference，而不改变其内部参数。

在 GFMs 的背景下，ICL 已成为处理 text-attributed graphs (TAGs) 的一种有前景的策略。TAGs 中，每个图组件（如 node, edge, subgraph）都关联有描述性文本信息。LLMs 可以直接处理这些文本属性，从而将图任务重塑为可以通过 prompting 解决的自然语言问题。然而，将 ICL 应用于 TAGs 会带来挑战，特别是构建高质量的 demonstration sets。与典型的 NLP 设置中的 i.i.d. samples 不同，图数据表现出丰富的结构依赖性，如 homophily, transitivity, 和 higher-order relations。因此，选择代表性和信息量大的 demonstrations 需要仔细考虑底层的 graph structure。为了解决这个问题，AskGNN [183] 引入了一个 GNN-based retriever，该 retriever 根据结构和语义相似性从图中选择相关的 node-label pairs。然后，这些选定的实例被格式化为自然语言 demonstrations 并输入到 LLM 进行预测。类似地，retrieval-augmented generation (RAG) 技术 [184] 也被用于通过从外部 memory 或 training set 动态检索最相关的图样本来提高 demonstration 的质量。除了 node classification，ICL 也被探索用于更复杂的图任务，例如 knowledge graph completion。在这种情况下，每个 sample 对应一个 triple (subject, relation, object)，ICL 可用于推断缺失的 entities 或 relations [185, 186]。

## 4.4.6 Prototype Learning

Prototype learning 是一种分类范式，它在 embedding space 中用一个 prototype vector 来表示每个类别，并根据实例与这些 prototypes 的接近程度进行分类。与依赖于专用分类器（如全连接层或 softmax heads）的传统方法不同，prototype learning 通过比较实例表示与类 prototypes 来执行分类，提供了一种更具可解释性且通常参数效率更高的方法。

在 Graph Foundation Models (GFMs) 的背景下，prototype learning 因其与 node-level 和 graph-level 任务的兼容性而受到关注。给定一个节点或子图的学习表示，模型将分配一个与 embedding space 中最近的 prototype 相对应的类标签。形式化地，实例 $v$ 的预测标签 $\hat{y}_v$ 由其表示 $\mathbf{h}_v$ 计算得出：

$$
\hat{y}_v = \arg \min_{c}\mathrm{dist}(\mathbf{h}_v,\mathbf{h}_c), \tag{33}
$$

其中 $\mathbf{h}_c$ 表示类别 $c$ 的 prototype，$\mathrm{dist}(- )$ 是一个距离度量，通常是 Euclidean 或 cosine distance。Prototype learning 方法可以根据 prototypes 的生成方式分为两类：(i) 源自 node representations 的 prototypes，(ii) 通过外部资源的额外 class nodes 学习的 prototypes。

**Prototypes from Node Representations**：一种常见且直观的策略是通过对训练集中标记节点的表示进行平均来计算类 prototypes。这些 prototypes 作为质心，捕捉了 embedding space 中每个类别的语义分布。具体来说，对于类别 $c$，prototype $\hat{\mathbf{h}}_c$ 计算为：$\hat{\mathbf{h}}_c = \mathrm{Mean}(\{\mathbf{h}_v\mid y_v = c, v\in \mathcal{V}\})$，其中 $\mathcal{V}_l$ 表示标记节点的集合，$\mathbf{h}_v$ 是从 GFM encoder 获得的节点 $v$ 的表示。此方法完全不依赖参数，并利用了 Graph Neural Networks (GNNs) 中邻域聚合的归纳偏置。它已被用于近期的 few-shot 或 prompt-based graph learning 工作中。尽管其简单，但通常能获得强大的性能，尤其是在 embeddings 在 latent space 中分离良好的情况下。

**Prototypes from Extra Class Nodes**：一种替代方法将类 prototypes 显式地建模为辅助图中的可学习节点。此方法构建一个二分图 $\mathcal{G}_g = (\mathcal{V}_g,\mathcal{E}_g)$，其中节点集 $\mathcal{V}_g$ 由数据节点 $\mathcal{V}_d$ 和类节点 $\mathcal{V}_c = \{c_1,c_2,\ldots ,c_C\}$ 组成。$\mathcal{V}_d$ 中的每个数据节点对应一个标记实例（例如，一个节点或图），而每个类节点代表一个不同的类标签。通常在每个数据节点和每个类节点之间构建边以促进跨节点交互。类 prototype $\hat{\mathbf{h}}_c$ 然后定义为在图上进行 message passing 后类节点的学习 embedding。这种 prototype 构建已被近期的工作中采用，其中 LLMs 被集成到带有类节点的 graph prompt 框架中。

## 4.4.7 Discussion

本章节讨论了Graph Foundation Models (GFMs) 的多种适应策略，这些策略针对不同的下游场景、数据特性和计算限制进行了优化，每种方法在适应性、可扩展性和任务性能方面都有其独特的优势和权衡。

**主要适应策略及其特点：**

*   **Transfer Learning:** 这是最传统且有效的策略，通过使用预训练模型初始化，显著减少了对大型标注数据集的需求并加速了收敛。
*   **Full fine-tuning:** 提供最大的灵活性，允许模型高度专业化，但计算资源需求大，且在小数据集上可能过拟合。
*   **Adaptive fine-tuning 和 parameter-efficient fine-tuning:** 通过限制可训练参数数量来缓解上述问题，但当任务分布与预训练分布差异较大时，性能可能受限。

*   **Distillation:** 适用于资源受限环境，通过将大型教师模型的知识转移到小型学生模型，平衡了性能和效率，特别适合延迟敏感的应用（如边缘设备）。主要限制在于学生模型可能无法完全捕捉教师模型中复杂的结构化信息。

*   **Test-Time Adaptation (TTA):** 旨在解决领域偏移问题，无需访问源数据或重新训练，允许模型动态适应新分布，适用于持续学习和在线学习场景。其局限性在于推理过程中缺乏真实标签监督，且可能因自监督信号的噪声或信息不足导致更新不稳定。此外，TTA通常假设测试数据是顺序或批量到达的，这可能不适用于所有实际场景。

*   **Graph Prompting:** 作为一种参数调优的替代方案，通过学习到的prompt vectors引导冻结的GFMs完成特定任务。其主要优势在于模块化，prompt可以重用、替换或组合，而无需修改基础模型。然而，prompting通常需要仔细的prompt engineering或调优，且性能可能受限于模型与任务的对齐程度。prompt可能无法跨任务或跨领域泛化，除非进行重新优化。

*   **In-Context Learning (ICL):** 允许在无需梯度更新的情况下进行zero-shot或few-shot适应，非常适合低资源或动态环境的快速部署。当应用于文本属性图时，ICL允许LLMs通过任务示例进行条件化推理。此方法消除了fine-tuning的需要，并受益于LLMs的生成能力。ICL的有效性取决于示例的质量和相关性，而为图数据构建示例集因实例间的依赖性而尤为困难，不当的示例选择可能导致性能显著下降。

*   **Prototype Learning:** 提供了一种参数高效且可解释的分类框架，特别适用于few-shot learning。通过从有限标注数据中派生的类原型（class prototypes）实现强大的泛化能力。基于平均节点表示的方法简单有效，而基于图的类节点构建则能捕获更丰富的语义。然而，prototype learning假设类簇在嵌入空间中形成良好，这在噪声或异质图（heterophilic graphs）中可能不成立。此外，其对距离度量的依赖可能忽略由判别性分类器（discriminative classifiers）能更好地捕捉的复杂决策边界。

## 5 Universal Graph Foundation Models

## 5 Universal Graph Foundation Models

本章节探讨了Universal Graph Foundation Models (GFMs) 的概念和发展，旨在构建能够处理广泛图任务的通用图模型。GFMs 的核心思想是借鉴大型语言模型 (LLMs) 的成功经验，通过大规模数据进行 **pre-training**，然后通过 **fine-tuning** 或 **in-context learning** 等方式适应下游的图任务。

**主要论点**

*   **通用性是关键：** 传统的 Graph Neural Networks (GNNs) 通常针对特定任务或特定类型的图进行设计。GFMs 的目标是打破这种局限，实现跨任务、跨领域、跨图类型的通用性。
*   **预训练-微调范式：** 借鉴 LLMs 的成功，GFMs 强调通过大规模、多样化的图数据进行 **pre-training**，学习通用的图表示和图结构理解能力。
*   **多模态与跨领域能力：** GFMs 不仅限于处理纯图数据，还能够整合文本、图像等其他模态信息，实现 **multi-modal learning**，并具备 **cross-domain transfer** 和 **domain adaptation** 的能力。

**方法**

GFMs 的构建通常涉及以下关键方法：

*   **大规模图数据预训练：** 利用海量的异构和同构图数据进行 **pre-training**。常用的 **pre-training** 任务包括：
*   **Self-supervised Learning** 任务，例如掩码节点预测、边预测、图结构预测等，旨在让模型学习图的内在结构和节点之间的关系。
*   **Contrastive Learning**，通过最大化相似图样本的表示，最小化不相似图样本的表示，来学习鲁棒的图表示。
*   **先进的 GNN 架构：** GFMs 通常会采用更强大、更具表达力的 GNN 架构，例如基于 **Transformer** 的 GNNs，或者结合 **Message Passing** 机制的先进模型，如 **Graph Attention Networks (GAT)** 和 **GraphSAGE** 的变体。
*   **多模态融合：** 将图结构信息与节点属性、边属性以及其他模态的数据（如文本描述、图像特征）进行有效融合，以增强模型的理解能力。
*   **适应下游任务：** **pre-training** 后的模型可以通过以下方式适应下游图任务：
*   **Fine-tuning：** 在特定下游任务的数据集上对模型进行微调。
*   **In-context Learning / Few-shot Learning / Zero-shot Learning：** 利用模型的通用知识，通过少量示例或直接指令来完成新任务，而无需或只需少量参数更新。

**结果与贡献**

GFMs 的出现标志着图学习领域向通用化迈出了重要一步。它们能够显著提升在各种下游图任务上的性能，包括但不限于：

*   **Node Embedding**
*   **Node Classification**
*   **Link Prediction**
*   **Graph Classification**
*   **Graph Generation**
*   **Graph Anomaly Detection**

GFMs 的通用性和强大的迁移学习能力，使得在数据稀疏或特定领域数据不足的情况下，也能取得优异的表现。它们为构建更强大、更灵活的图智能系统奠定了基础。

## 5.1 Design Principle

Graph Foundation Models (GFMs) 的设计目标是跨越不同领域和任务，适应各种图结构和分布，其愿景类似于 LLMs 在自然语言处理和 VLMs 在计算机视觉中的作用。通过借鉴现有 foundation models 的经验，可以制定 GFMs 的设计原则，以应对跨领域和跨任务的挑战。

**核心设计原则**

1.  **处理异构图分布 (Handling Heterogeneous Graph Distributions)**：来自不同领域的图（如分子结构、社交网络、金融交易系统）在大小、连通性、节点属性、密度和相关任务上存在显著差异。GFM 必须能够以最小的领域特定再训练来泛化于这些异构分布。类似于 LLMs 通过 next-token prediction 从大量文本语料库中提取语义表示，GFMs 需要专门设计的 self-supervised pretraining objectives 来促进从大规模、多领域图数据集的学习。目标是将多样化的图结构嵌入到一个统一的潜在空间中，从而实现有意义的跨领域知识迁移。

2.  **解决任务冲突 (Addressing Task Conflicts)**：基于图的任务通常涉及相互竞争的目标。例如，node classification 需要理解局部邻域结构（如 homophily 和 heterophily），而 graph classification 则侧重于高阶 motifs 和结构模式。LLMs 通过将所有语言相关任务框架化为统一的 objective，即 question-answering 来协调此类冲突。同样，GFMs 必须建立一个共享的 inductive bias，以协调图之间的任务表示。Multi-task learning 技术可以进一步帮助平衡不同的学习目标，确保模型在广泛的图任务中保持有效性。

3.  **促进正向迁移 (Facilitating Positive Transfer)**：尽管存在领域转移，但某些高级图属性（如拓扑模式和 homophily）在不同数据集之间表现出一致性。设计良好的 GFM 应学习一个共享的潜在空间，该空间能够对齐不同领域的图，同时保留任务特定的细微差别。挑战在于缓解具有不同 inductive biases 的任务之间的差异，同时促进知识迁移。实现这一点需要仔细平衡 pretraining objectives 和 downstream adaptations，并采用 task-aware mechanisms 来对齐模型表示。有效的 pretraining 策略不仅应捕获全面的图语义，还应保持适应性，确保 pretraining 和 downstream 任务之间的无缝对齐。

接下来的章节将通过分析现有 universal GFMs 如何解决上述三个核心挑战来审视它们。具体而言，这些方法被归类为三个基本层面：(1) model-level，侧重于模型统一策略以增强跨任务和跨领域的 transferability；(2) pretrain-level，探索 pretraining 期间的领域对齐技术以实现跨领域泛化；(3) adaptation-level，研究 downstream task adaptation 机制以促进高效的 fine-tuning 和 transfer learning。

## 5.2 Graph Model-Based Universal GFM

本章节介绍了基于Graph Model的通用Graph Foundation Models (GFMs)。这类GFMs主要遵循“预训练-再适配”的范式。其核心目标是利用大规模、跨领域、多样化的图数据库进行预训练，以学习能够迁移的结构和语义模式的图编码器。随后，该编码器可被适配到未见的图数据上，以完成下游任务。现有研究成果根据GFMs的骨干网络（backbones）、预训练方法、适配策略，以及处理特征、结构和任务异质性的技术进行了总结，具体体现在Table 2中。

## 5.2.1 Model Unification

构建通用 Graph Foundation Models (GFMs) 的核心挑战在于设计能够跨任务、跨领域和跨图拓扑泛化的 GNN encoder。模型统一的方法主要分为两类：(1) 通过任务和输入重构实现的显式统一 (explicit unification)，以及 (2) 通过架构泛化和不变性强制实现的隐式统一 (implicit unification)。

**显式统一 (Explicit Unification)**

显式统一方法旨在将各种基于图的任务转化为统一的预测格式，从而支持共享的预训练和推理流程。根据任务粒度，可分为三种主要类别：

*   **Link-Level Unification**: 一种策略是将所有基于图的任务都构建为 link prediction 问题。这通过引入 class nodes 到图中，并预测这些节点与任务相关节点之间的 links 来实现。这种方法将分类任务视为 link prediction，例如公式 (34) 所示，其中 $\hat{v}_{v_i}$ 是目标节点 $v_i$ 的预测，通过计算其 embedding $\mathbf{h}_{v_i}$ 与 class node $c_k$ 的 embedding $\mathbf{h}_{c_k}$ 之间的相似度并应用评分函数 $\sigma$ 得到。GPPT [74] 是该方法的开创者，结合了 masked edge prediction 和 prompting 技术。后续方法 [71, 182] 通过 prompt tokens 扩展了这一框架以增强任务对齐。尽管这种方法简洁且通用，但可能忽略某些预测任务所需的精细子结构。

*   **Subgraph-Level Unification**: 为了整合局部结构上下文，第二类方法将图任务构建在 subgraph 层面 [199, 181, 173, 108, 22, 75]。这是一个两阶段过程：首先提取以目标节点为中心的 ego-graphs，然后对每个 subgraph 应用 GNN encoder。例如，在 node classification 中，为每个节点构建一个 ego-graph，其标签对应于中心节点的标签。此原理可推广到 edge 和 graph 级别的任务，从而在 subgraph 层面统一各种图任务。这通过公式 (35) 表示，其中 $\mathcal{G}_{v_i}$ 是节点 $v_i$ 周围半径为 $r$ 的 ego-subgraph，其 embedding 经过 GNN $f_{\mathrm{GNN}}$ 编码后传递给分类器 $f_{\mathrm{Classifier}}$。GCC [199] 等早期工作采用 contrastive pretraining 来捕捉多领域图的结构模式。GraphPrompt [181]、Prodigy [108] 和 All in One [173] 等方法通过引入 prompt learning 技术增强了预训练与下游任务的对齐。OFA [22] 和 UniGraph [75] 将此方法推广到 cross-domain 场景。该范式支持统一的 node、edge 和 graph 级别任务框架，并在 domain adaptation 和 transfer learning 中表现出强大的经验性能。然而，subgraph-level unification 存在两个主要限制：(1) subgraph 提取引入显著的计算开销；(2) message-passing GNNs 可能难以捕捉关键子结构，导致表示学习次优 [207, 208, 209, 210]。

*   **Tree-Level Unification**: 一种更近期且高效的替代方法引入了虚拟节点 (virtual nodes)，这些节点连接到任务相关节点，无需进行 subgraph 提取。这些虚拟节点充当树结构表示的代理，其 embeddings 用于下游预测。例如，在 node classification 中，虚拟节点连接到所有原始节点，并通过 message passing 学习到的其 embeddings 作为最终表示，如公式 (36) 所示。$\mathcal{G}^{+}$ 是在原始图 $\mathcal{G}$ 中添加了一个虚拟节点 $v$ 并连接到所有任务相关节点 $\mathcal{V}_{\mathrm{task}}$。GNN encoder 计算 $v$ 的 embedding，该 embedding 反映了来自图的聚合信息。此设计显著提高了效率，同时保留了表示能力。GFT [23] 是该方法的先驱，展示了树相似性与任务可迁移性提升之间的经验和理论联系。GIT [76] 从理论角度进一步形式化了基于树的表示的稳定性、可迁移性和泛化性。

**隐式统一 (Implicit Unification)**

虽然显式任务重构为统一图任务提供了一种原则性的方法，但另一类研究则侧重于隐式架构统一，即修改底层模型设计，使其能够在不改变任务定义本身的情况下泛化到各种任务和领域。

*   HoloGNN [77] 解决了传统 GNN 架构通常为特定任务类型（如 node-level 或 link-level classification）硬编码的局限性。为了克服这一点，HoloGNN 引入了 expansion 和 reduction maps，显式地建模 node-permutation symmetries。通过将输入图分解为 permutation-invariant 组件，然后重构任务特定的视图，HoloGNN 使单个架构能够灵活地适应各种学习任务。
*   SCORE [192] 提出了 relation graph 框架：SCORE 构建了一个编码跨领域实体关系的语义交互图，而不是直接操作输入图。通过集成语义条件 message passing，模型在保留共享结构和语义不变性的同时，动态地适应领域特定的模式。
*   AnyGraph [64] 通过结合 mixture-of-experts 架构和高阶结构注入来增强模型表达能力。通过引入高阶连接模式和门控机制，AnyGraph 在保持模块化和可扩展性的同时，捕捉了局部和非局部交互。
*   OpenGraph [63] 从数据表示的角度解决了图异构性问题。它引入了一个拓扑感知 tokenizer，将可变大小的图结构（如邻接矩阵）转换为适合 Transformer-based encoder 的固定长度序列。该 tokenizer 保留了关键的拓扑属性，同时允许 foundation models 在不同大小和形状的图上统一运行。

总而言之，这些隐式统一策略表明，独立于任务重构的架构设计在构建可迁移和鲁棒的 GFMs 中起着关键作用。随着图数据的复杂性和多样性不断增长，显式和隐式统一机制之间的相互作用对于开发可扩展、通用图模型至关重要。

## 5.2.2 Domain Alignment in Pretraining

本章节探讨了在Graph Foundation Models (GFMs) 的预训练阶段如何实现Domain Alignment，以解决不同图结构和特征之间的异质性问题。主要分为特征对齐（Feature Alignment）和结构对齐（Structure Alignment）两个方面。

**特征对齐（Feature Alignment）**

特征对齐旨在确保不同图的节点特征在共享的表示空间中保持一致性。主要有两种范式：

1.  **文本和多模态特征对齐**：
*   该方法通过将文本或多模态属性映射到共享表示空间来统一异质图信号。通常使用预训练的编码器（如SentenceBERT, CLIP）将节点描述（文本、图像等）转换为低维嵌入向量 $\mathbf{h}_i$。
*   一些模型（如OFA, UniGraph, UniGLM）通过固定模板、微调编码器或对比学习来增强对齐效果。UniGraph2使用CLIP统一处理文本和图像模态。GraphAlign则采用mixture-of-experts模型动态选择编码器。
*   为解决标注数据不足的问题，TANS利用LLMs生成合成文本描述，扩展了基于对齐的GFMs的应用范围。

2.  **基于模型（Model-Based）的特征对齐**：
*   该方法通过模型架构设计直接对齐异质节点特征，无需外部编码器。
*   一种策略是引入领域特定的投影函数 $f_{\mathrm{proj}}$，将原始节点特征 $\mathbf{x}_i$ 映射到统一的潜在空间 $\mathbf{h}_i$。DARE使用模型重编程（model reprogramming），通过轻量级适配器处理冻结的预训练GNN，降低训练成本并提高参数复用。
*   另一种技术是使用奇异值分解（SVD）来正交化特征空间，然后通过 $f_{\mathrm{align}}$（可包含learnable tokens, LLM模块, MoE routers）进一步对齐。
*   PatchNet提出了一种组合式方法，通过提取和编码图块（graph patches）来形成节点表示。
*   然而，基于模型的方法在泛化到未见图方面存在局限性，其对齐机制可能与预训练图的特征分布和结构模式紧密耦合。

**结构对齐（Structure Alignment）**

结构对齐旨在解决不同领域图在结构模式上的显著差异。主要策略包括：

1.  **领域不变的预训练目标（Domain-Invariant Pretraining Objectives）**：
*   通过优化能够泛化到不同图拓扑的预训练目标来学习领域不变的结构表示。FoToM采用对抗性对比学习来解耦领域特定特征并保留任务相关的结构。

2.  **结构词汇构建（Structural Vocabulary Construction）**：
*   定义一个共享的结构词汇表，捕捉图中的重复模式。GFT构建一个树状码本来编码规范的结构特征。RiemannGFM则在黎曼空间建模树和环状结构。这些方法通过离散、可重用的结构基元来促进结构对齐。

3.  **图提示（Graph Prompting）用于结构自适应**：
*   图提示学习被用于结构对齐。IGAP分析图的谱差异并使用可学习的提示（prompt tokens）在谱域对齐表示。BooG在预训练时引入虚拟节点来协调不同领域的结构上下文。ProNoG使用控制网络生成节点特定的提示，实现细粒度的结构校准。

4.  **Mixture-of-Experts（MoE）用于结构多样性**：
*   OMOG提出一种MoE框架，训练多个专门化的GNNs（每个针对不同结构领域），并在推理时通过门控函数动态选择最相关的专家，以减少负迁移并适应新结构。

**多目标学习（Multi-Objective Learning）**

为平衡不同下游任务的归纳偏置，采用多样化的预训练目标至关重要。

*   **多任务学习框架**：模型联合优化多个目标。GFT整合了节点、链接和语义级别的重构目标。UniGraph联合训练GNN和LLM，结合对比学习和掩码 token 预测。GFS在图Transformer框架下优化特征和局部结构重构。
*   **高级优化技术**：为优化竞争性目标，研究者探索了Pareto优化、可学习任务token和元学习。MultiGPrompt使用多个可学习的前置token连接不同的任务目标。ParetoGNN使用Pareto优化来平衡多个预训练任务。All in One应用元学习优化多任务提示初始化，提升泛化能力。

## 5.2.3 Downstream Task Adaptation

本节详细阐述了Graph Foundation Models (GFMs) 在下游任务适应（Downstream Task Adaptation）方面的多种策略。

**Fine-Tuning** 是最常用的方法，包括全模型微调（full fine-tuning）和线性探测（linear probing），后者仅更新最后一层。GFMs旨在实现归纳式学习（inductive setting），泛化到未见过的图，但跨域迁移仍具挑战。为克服此问题，研究者提出了多种快速适应策略。

**Transfer Learning** 是核心策略，通过在新图上微调预训练模型来提升特定任务性能。为解决计算成本问题，研究者开发了更快的迁移学习技术。EGI [195] 通过自图（ego-graph）分布建模来增强迁移性，将迁移性与源域和目标域的局部图拉普拉斯（local graph Laplacians）联系起来。AUX-TS [152] 则通过引入具有自适应权重的辅助任务，弥合了自监督预训练和下游任务优化目标之间的差距，提高了适应效率。

**Prompt Learning** 受LLMs启发，作为一种高效的替代微调方法。它不修改预训练模型，而是微调可学习的图提示（graph prompt）token，实现快速适应。GPT [74] 引入了提示添加（prompt addition）、提示回答（prompt answering）和提示调优（prompt tuning）三个关键组件，实现了在不修改骨干模型的情况下进行适应。后续研究通过在子图层面统一预训练和下游任务、利用多尺度图提示token、设计高级提示模板以及整合外部知识源等方式进一步改进了这一范式。

**Prototype Learning** 提供了一种无需额外调优的替代方案，通过构建类原型（class-specific prototype embeddings）进行下游任务预测，该技术在few-shot learning中广泛应用。通过对样本进行平均来形成类原型，新实例被分配给最近的原型。OFA [22]、UniGraph [75] 和 UniGraph2 [203] 引入了查询-支持（query-support）框架，利用支持图构建类原型，并可通过外部资源（如文本类嵌入）扩展至zero-shot learning。GFT [23] 采用类似范式，并结合少量样本的有限微调，证明了少量标记样本对下游性能的显著提升作用。

**Structural Augmentation** 作为一种补充策略，通过增强图结构来提升下游任务性能。UniAug [70] 基于离散扩散模型（discrete diffusion model）构建了一个通用结构增强器，该增强器仅在超过1000个数据集的图结构上进行预训练，能够通过引导生成来增强下游图的结构，从而使节点、链接和图级别的任务受益。实验表明，增加预训练数据的量可以提高下游泛化能力，因为它丰富了模型对图之间多样化结构模式的理解。

## 5.3 Language Model-Based Universal GFM

本节探讨了利用大型语言模型（LLMs）作为图（graph）相关任务的预测器。LLM-based GFMs 的设计目标围绕三个关键组件：(1) 开发有效的 tokenization 策略将图数据转化为文本表示；(2) 对 LLMs 进行后训练（post-training），以整合图特有的知识；(3) 设计高级的 adaptation 技术以增强与下游任务的对齐。

LLM-based universal GFMs 的核心组成部分包括：

1.  **Graph Tokenization**: 定义一个 tokenization 函数 $\mathcal{T}$，将图 $\mathcal{G}$ 映射为文本序列 $\mathbf{s} = [s_1,s_2,\ldots ,s_L]$，该序列包含代表输入图的节点、边和属性的 $L$ 个 tokens。

2.  **Post-Training on Graph Data**: 使用 tokenized 输入 $\mathbf{s}$，通过图相关的目标（如 masked token prediction, topology autoencoding）对预训练的 LLM 进行 Fine-tuning，得到 $\theta^{*} = \arg \min_{\theta}\mathcal{L}_{\mathrm{graph}}(\mathrm{LLM}(\mathbf{s};\theta),y)$，其中 $\mathcal{L}_{\mathrm{graph}}$ 是图感知训练损失，$y$ 是监督信号。

3.  **Downstream Adaptation**: 对于下游任务推理，应用一个 adaptation 函数 $\mathcal{A}$（如 in-context learning, prompting, instruction tuning）来构建输入 prompt 并解码预测，得到 $\hat{y} = \mathcal{A}(\mathrm{LLM}(\mathbf{s}))$，其中 $\hat{y}$ 是适配到下游任务格式的模型预测。

Table 3 总结了多种 LLM-based universal GFMs，如 LangGFM, Meta-Transformer, QueryRAG, GraphAgent, Graph-ToolFormer, InstructGraph, Beyond Text, Graph Agent, InstructGLM, 和 GraphICL。这些方法在 backbone、pretrain 策略、adaptation 方式、feature align、structure align 和 task align 等方面有所不同。大多数方法使用 LLM 作为 backbone，并采用 generative pretrain 策略。在 adaptation 方面，finetune 和 in-context learning 均有使用。Feature align 和 structure align 通常通过将数据（如文本属性）和数据增强（data augmentation）与图结构对齐来实现。Task align 方面，许多方法明确地针对 QA 等任务进行优化。

## 5.3.1 Model Unification

本章节探讨了将大型语言模型（LLMs）的能力扩展到图结构数据领域，实现“Model Unification”的关键挑战和方法。核心目标是将图的归纳偏置（inductive biases）与LLMs的序列和语义处理能力对齐。现有方法主要分为两大类：自然语言转换和结构化格式转换。

**自然语言转换**方法将图元素（节点、边、属性）用人类可读的描述表示，利用LLMs的语言能力进行图推理。其具体策略包括：
*   **Template Construction**: 使用手工或自动生成的模板，将节点标签、边类型、度数或图统计信息等图组件嵌入到文本描述中。例如，QueryRAG [184] 包含邻接属性和图大小等详细结构摘要。
*   **Hierarchical Context Inclusion**: 通过包含多跳邻域信息 [101, 223]，使LLMs能够理解更广泛的结构上下文。这些描述通常分层组织以反映结构深度。
*   **Task-Specific Reasoning and Prompting**: 引入动态推理机制，如多步提示、记忆更新和agent式决策 [219, 223]，以迭代优化LLMs对图任务的理解和决策过程，提升 traversal、path-finding 或 subgraph reasoning 等任务的性能。

**结构化格式转换**方法则将图编码为JSON、代码块或嵌套列表等结构化数据，以保留图拓扑并实现LLMs的结构化解析和分析。其关键特征包括：
*   **Predefined Templates and Tokenization**: 使用领域特定的模板定义图元素，例如将节点表示为带有属性和邻居字段的对象，边编码为嵌套数组中的关系 [220]。
*   **API-Augmented Inference**: 通过集成API来增强推理流程，允许在推理过程中动态进行图遍历或数据检索，支持 knowledge graph completion 或 personalized recommendation 等任务 [220]。
*   **Hierarchical Context Encoding**: 类似自然语言方法，结构化格式也可能包含节点邻域的层次化表示。GraphAgent [222] 通过递归上下文树来增强LLMs对嵌套关系依赖的建模能力。

总而言之，自然语言转换和结构化格式转换都为在LLM框架下实现图推理提供了可行途径。自然语言转换更侧重可解释性和人类理解，而结构化格式则在复杂或大规模图任务中提供清晰性和一致性。选择哪种方法取决于泛化能力、计算效率和下游应用兼容性等方面的权衡。

## 5.3.2 Domain Alignment in Model Training

本章节探讨了在模型训练过程中实现Domain Alignment的方法，以使大型语言模型（LLMs）能够有效理解和推理图数据。

一种直接的方法是利用预训练的LLMs作为zero-shot或few-shot预测器。在这种模式下，将图格式的prompts输入模型，实现in-context learning，无需额外的参数更新。这种范式利用了LLMs强大的泛化能力和组合推理能力，仅通过基于prompt的监督来执行任务。

尽管zero-shot性能具有竞争力，但研究表明，后训练适应（post-training adaptation），特别是supervised fine-tuning (SFT) 和 preference alignment（如PPO, DPO）等技术，可以显著提升LLMs与图结构任务的对齐度。因此，近期研究探索了多种策略，通过领域特定的训练目标和multi-task instruction tuning来更好地使LLMs适应图推理。

**Instruction-Tuned Fine-Tuning**：InstructGraph [221]提出了一种监督微调方法，将结构化的图推理任务纳入LLM训练过程。通过将图编码的输入与精心设计的指令和目标输出配对，模型学习遵循图特定的推理模式。诸如reinforcement learning with human feedback (RLHF) 或 direct preference optimization (DPO) 等preference alignment技术被进一步用于增强输出的忠实度和任务依从性。InstructGLM [101]通过multi-prompt training将此概念推广，将多种图任务（包括classification、generation和summarization）转化为基于指令的prompts。LLM在这一multi-task语料库上进行训练，以促进泛化和cross-task transfer。这种统一的训练范式使LLMs能够处理具有不同输入-输出格式和结构复杂性的图问题。

**Self-Supervised Graph Alignment**：LangGFM [99]提出了一种基于self-supervised learning (SSL) 的替代微调策略。受传统graph pretraining技术的启发，LangGFM引入了两个针对基于LLM的图理解的新型SSL目标：Topology Autoencoding和Feature Masked Autoencoding。Topology autoencoder促使模型从文本化的图描述中重建结构信息（如edge connections、adjacency statistics），而feature masked autoencoder则掩盖node attributes并从上下文中预测它们——这类似于masked language modeling，但应用于图编码的文本。这些self-supervised目标在无需手动标注数据的情况下，促进了LLM表示与图拓扑的对齐。因此，LangGFM在下游任务上取得了强大的性能，同时保持了label efficiency和对domain shifts的鲁棒性。

## 5.3.3 Downstream Task Adaptation

本章节探讨了LLM-based Graph Foundation Models (GFMs) 在下游任务适应方面的技术。

**Zero-Shot Reasoning**
LLMs 展现出强大的零样本（Zero-Shot）泛化能力，无需显式 fine-tuning 即可执行多种任务。这种能力自然地延伸到 LLM-based GFMs，使其能够直接处理图数据的文本表示来解决图相关任务。通过设计与 LLMs 预训练分布对齐的提示（prompts），研究表明 LLMs 可以在不更新模型参数的情况下执行 node classification、link prediction 和推理任务。Zero-shot 适应的有效性依赖于高质量的 template engineering，即将图序列化为 LLMs 能语义理解的描述性格式。

**In-Context Learning**
除了零样本推理，LLMs 还可以利用 in-context learning，通过在输入提示中包含示例来提升任务性能。这种方法通过在查询前添加带有标签的图实例或结构化解释，在不更新模型参数的情况下注入任务特定知识。一些研究通过使用带有标签的图实例来探索这种范式，有效地指导 LLMs 完成下游任务。

为了增强 in-context learning，研究人员开发了先进的 prompting 技术，整合了图数据的结构化表示。GraphICL [223] 提出了一种结构化 prompting 框架，使通用 LLMs 在资源受限和 out-of-domain 任务中表现优于专用图模型。其设计的 prompts 包含四个关键组件：(1) 任务描述，定义目标；(2) anchor node text，为相关实体提供上下文；(3) structure-aware information，提供拓扑洞察；(4) 带有标签的示例，支持 few-shot learning。这些元素共同实现了对 node classification 和 link prediction 任务的适应。GraphAgent [219] 将下游图任务重新构建为 agent planning 问题，LLMs 基于图拓扑和节点内容采取结构化行动。该框架包含一个分层记忆机制，整合了长期和短期记忆模块，能够高效处理大规模图数据。通过动态存储高质量示例，GraphAgent 显著提高了 LLMs 在不同图域间的泛化能力。QueryRAG [184] 通过显式地将查询节点、图邻居的上下文信息和相应的标签整合到结构化 prompts 中，增强了 in-context learning。这种设计确保了图结构作为固有的上下文特征，使 LLMs 能够更好地捕捉关系依赖性并提升图数据的推理能力。

## 5.4 Graph-Language Co-Training Universal GFMI

本章节介绍了Graph-Language Co-Training Universal GFMI，旨在解决大型语言模型（LLMs）在处理结构化数据（如图）方面的局限性。LLMs在自然语言处理方面表现出色，具有强大的泛化能力，但在处理图数据时，由于其顺序token表示无法有效捕捉高阶依赖、长程交互和复杂关系结构，存在固有不足。将图数据token化为文本序列以直接利用LLMs的方法，会引入显著的归纳偏置不匹配，丢失关键的结构信息，例如邻域信息。本章节的核心贡献在于提出一种协同训练框架，以弥合LLMs在处理文本和图数据之间的差距，实现通用Graph Foundation Models (GFMs)。

## 5.4.1 Model Unification

本章节探讨了将Graph Neural Networks (GNNs) 与大型语言模型 (LLMs) 整合的统一模型方法。当前主流框架借鉴了视觉-语言模型，通过图编码器提取结构化特征，然后由LLM对这些表示进行推理。为了弥合图嵌入与基于token的语言模型之间的差距，研究人员提出了多种技术，以提升图结构数据的对齐性、可解释性和推理能力。

一些方法专注于将图结构编码为与LLM处理兼容的token化表示。LLaGA [78] 通过两种模板重构节点为序列表示：Neighborhood Detail 捕捉局部连通性，Hop-Field Overview 编码更广泛的结构上下文。一个学习到的投影模块将这些结构化表示与LLM的token embedding对齐。GraphAgent [230] 引入了Graph-Token Grounding，将节点和边映射到结构化的Python对象，而Graph Tokenization则为生成和预测任务嵌入离散的图实体。该模型使用一个意图识别模块，根据用户查询动态调整系统prompt。GraphTranslator [103] 通过一个翻译模块促进GNNs和LLMs之间的交互，该模块将图嵌入转换为文本表示，并使用一个producer模块生成对齐数据，以确保图结构与自然语言描述之间的一致性。NT-LLM [229] 采用Node Tokenization，选择锚点节点来高效编码图结构，同时保持拓扑完整性，从而增强了LLMs中的关系表示和推理能力。TEA-GLM [228] 精炼了prompt构建，以泛化到不同的图任务，将prompt结构化为三个部分：(1) 图信息，(2) 任务描述，以及 (3) 用于跨数据集推理的多项选择题。一个专门的投影模块将图token映射到instruction-tuned LLMs，确保不同任务之间的对齐。

## 5.4.2 Domain Alignment in Model Training

在获得统一的图-文本表示后，模型训练中的Domain Alignment对于提升推理能力和跨不同图任务的泛化能力至关重要。

**监督式对齐 (Supervised Alignment)** 是对齐GNN和LLM组件最常用的策略。通常，图编码器被附加到LLM上，然后将组合后的架构在标注数据集上进行端到端训练。这使得模型能够学习到结构特征和文本推理之间的紧密耦合，并适应特定的下游应用。

**自监督式对齐 (Self-Supervised Alignment)** 旨在减少对标注数据的依赖。GALLM [225] 引入了一个文本匹配目标，使用手动和可学习的软类别prompt，并通过反向传播进行优化。该模型遵循一个两阶段流程，包括基于SSL的预训练和监督式微调。GOFA [53] 将图理解表述为句子补全和推理，在一个共享的prompt空间下统一了结构分析和问答等多种任务。LangGFM [99] 将传统的GNN预训练思想适配到LLM友好的格式，提出了Topology Autoencoding和Feature Masked Autoencoding，通过文本化输入来增强结构推理。

**CLIP-like 对齐** 受CLIP [60] 的启发，GraphCLIP [104] 应用对比学习将图表示与文本摘要进行对齐。借助LLMs生成大规模的图-摘要对，并用于训练一个对比编码器-解码器系统。这种预训练策略促进了Zero-shot和Few-shot迁移，实现了跨领域和图类型的鲁棒泛化。

## 5.4.3 Downstream Task Adaptation

本章节探讨了将LLMs应用于图任务的下游任务适应性。

**Zero-Shot Reasoning**：LLMs通过利用其预训练知识和prompt-based adaptation，天然支持zero-shot reasoning。当与图表示结合时，即使没有额外的fine-tuning，也能在node classification和link prediction等图任务上进行有效推理。Zero-shot adaptation在低资源场景下尤为重要，因为这些场景下标记的图数据稀缺或不可用。

**In-Context Learning (ICL)**：多种方法利用ICL通过将任务演示直接嵌入prompt来增强图推理能力。AskGNN [183]通过ICL Example Purification提高了分类准确性，这是一种两阶段方法，通过LLM评分选择信息性支持示例，并过滤类别不平衡的样本，从而提高了in-context示例的代表性和平衡性。RAG-based方法，如RAGraph [206]，在推理过程中检索与图相关的上下文，动态丰富prompt，并提高对先前未见图结构的泛化能力。

**Interpretability**：使用LLMs进行图推理的一个主要优势是它们能够生成人类可读的解释。GraphTranslator [103]通过用户活动图上的多轮对话推理展示了这一点，支持在行为分析、社交网络动态和推荐场景中的可解释性。通过将自然语言输出与结构化表示相结合，这类模型增强了基于图的AI系统的透明度和可信度。

## 5.5 Discussion

通用 Graph Foundation Models (GFMs) 通过大规模预训练和可适应的架构，旨在实现跨图域和任务的泛化。不同类型的 GFMs 各有优劣，反映了模型表达能力、可扩展性、泛化性和可解释性之间的固有权衡。总而言之，GNN-based models 高效且结构感知，但语义能力有限；LLM-based models 灵活且由语言驱动，但难以处理图拓扑；混合模型旨在融合两者的优势，但引入了显著的系统复杂性。

**Graph Model-Based GFMs**：GNN-based universal models 在结构上与图数据对齐，通过 message passing 和局部邻域聚合，在捕捉拓扑信息方面表现出色，尤其适用于结构至关重要的任务。其优势在于：1) 强大的图专属归纳偏置 (inductive biases)，支持跨图域泛化；2) 由于局部计算，对大规模图计算效率高；3) 非常适合涉及图模式 (graph motifs) 的结构性任务。局限性包括：1) 编码丰富语义信息（如文本或多模态节点属性）的能力有限；2) 在不进行显著架构或 prompt 设计的情况下，难以扩展到域外任务；3) 由于局部 message passing 的限制，难以处理长程依赖。

**Language Model-Based GFMs**：LLM-based approaches 利用预训练的语言模型，通过文本或结构化 prompt 对图结构化数据进行推理。这些方法将图转换为序列，从而实现跨异构任务的 zero-shot 或 in-context 推理。优势包括：1) 通过指令遵循和 prompt 驱动的适应，实现跨任务和域的卓越泛化；2) 支持多模态数据（如文本和图像）的灵活性；3) 由于自然语言输出和推理链，可解释性高。局限性在于：1) 将图拓扑线性化为 token 序列时会损失结构保真度；2) 由于模型规模大和输入序列化开销，计算成本高；3) 缺乏内置的图归纳偏置，需要大量的 template engineering 来处理结构性任务。

**Graph-Language Co-Training GFMs**：混合模型集成了 GNNs 和 LLMs，将 GNNs 的结构推理与 LLMs 的语义和通用推理能力相结合。例如 LLaGA, GraphTranslator, 和 GraphCLIP。这些模型将图 embedding 映射到 LLM token 空间，实现多模态和跨域推理。优势包括：1) 结合了结构感知和语义丰富性，提高了任务迁移能力和表达能力；2) 支持结构化和非结构化输入，非常适合实际应用（如推荐、knowledge graph）；3) 通过 prompting、fine-tuning 或 contrastive alignment 技术实现灵活适应。局限性在于：1) 模型架构复杂，计算和内存需求高；2) 需要仔细对齐图 embedding 和 token 表示；3) 跨模态的监督信号集成仍然是一个具有挑战性的研究问题。

## 6 Task-Specific Graph Foundation Models

本章探讨了**Task-Specific Graph Foundation Models (GFMs)**，即针对特定下游任务进行优化的Graph Foundation Models。与通用的GFMs不同，Task-Specific GFMs旨在通过更精细的调整和设计，在特定应用场景下实现更优越的性能。

本章的核心论点在于，通过**Task-Specific Pre-training**和**Fine-tuning**策略，可以显著提升GFMs在各种图学习任务上的表现。这包括但不限于：

*   **Graph Neural Networks (GNNs)** 的架构优化：针对特定任务，可以调整GNNs的层数、聚合函数（如Message Passing机制）以及注意力机制（如Graph Attention Networks (GAT)）。
*   **Pre-training** 策略的定制：根据下游任务的特点，设计更有效的Self-supervised Learning目标函数，例如Contrastive Learning或Masked Graph Modeling。
*   **Fine-tuning** 方法的改进：探索更高效的Fine-tuning策略，如Parameter-Efficient Fine-tuning (PEFT)，以减少计算资源消耗并防止过拟合。
*   **In-context Learning** 和 **Few-shot Learning** 的应用：研究如何利用Task-Specific GFMs在少量标注数据的情况下，快速适应新的图学习任务，甚至实现Zero-shot Learning。

本章还讨论了Task-Specific GFMs在不同图学习任务中的应用，包括：

*   **Node Classification** 和 **Graph Classification**：通过Task-Specific Pre-training，模型能够学习到更具判别力的Node Embedding，从而提高分类精度。
*   **Link Prediction**：针对特定类型的链接，可以设计相应的GNN架构和Pre-training任务来提升预测能力。
*   **Graph Generation** 和 **Graph Anomaly Detection**：Task-Specific GFMs可以学习到特定图结构的生成模式或异常模式，从而在这些任务上取得突破。

此外，本章也触及了Task-Specific GFMs在处理**Heterogeneous Graph**和**Knowledge Graph**等复杂图结构时的挑战与机遇，以及如何实现**Cross-domain Transfer**和**Domain Adaptation**。

总而言之，本章强调了为特定任务定制Graph Foundation Models的重要性，并介绍了实现这一目标的关键技术和方法，为在实际应用中最大化GFMs的效用提供了指导。

## 6.1 Design Principle

任务特定的 Graph Foundation Models (GFMs) 被设计用于跨多个领域操作，同时专注于解决单一任务，例如 node classification, link prediction, 或 graph generation。尽管来自不同领域的图可能共享与特定下游任务相关的 inductive biases，但它们的 structural properties 可能存在显著差异。因此，一个有效的任务特定 GFM 不仅必须捕捉跨领域的 task-aware invariances，还必须对不同的 graph distributions 进行对齐，以确保 robust generalization。

**Task- Specific Inductive Bias**: 不同的图任务对学习过程施加不同的 inductive biases。例如，node classification 通常依赖于 homophily 和 heterophily 原则，link prediction 强调 local 和 global connectivity patterns，而 graph classification 则侧重于识别有意义的 substructures。尽管图之间存在 structural variations，但与任务相关的表示往往会呈现共享的模式。通过利用这一观察，一个设计良好的 GFM 可以学习 domain-invariant representations，同时保留至关重要的 task-specific knowledge，从而确保在不同数据集上的 adaptability。

**Cross-Domain Alignment**: 来自不同领域的图在 structural properties, node types, feature distributions 和 connectivity patterns 上存在差异。为了在最少的重新训练下实现对未知 graph distributions 的泛化，模型必须学习在跨领域保持 robust 的表示。实现这一点需要诸如 domain-adaptive architectures 等技术，其中 GNN layers 会根据输入域的特性动态调整，或者通过 attention mechanisms 和 parameter-efficient adaptation 进行 domain-specific feature modulation。这些策略有助于减轻在领域之间切换时性能下降的问题。

**Balancing Domain Generalization and Task-Specific Adaptation**: 任务特定 GFMs 的一个基本挑战在于平衡 domain invariance 和 task-specific adaptation。过度强调领域理解可能会引入有利于特定领域的 inductive biases，从而牺牲 task-specific generalizations；而完全泛化的模型则可能忽略关键的 domain-specific patterns，从而降低性能。为了实现这种平衡，可以采用 domain regularization, normalization 和 adversarial training 等 domain generalization 技术。这些方法有助于防止 domain overfitting 和 catastrophic forgetting，使模型能够同时保持 cross-domain adaptability 和高 task-specific performance。

后续章节将系统地探讨 GFMs 在六个基本图相关任务中的 design principles：node classification, link prediction, graph classification, question answering, anomaly detection 和 recommendation。对于每个任务，将考察其基础 design philosophies, 关键挑战, state-of-the-art methodologies 和未来研究的有前景的方向。

## 6.2 Node-level Task

Node-level tasks专注于预测图中节点的属性或角色。Node classification是图学习中基础的node-level下游任务，旨在预测图中单个节点，并已在GFMs中获得显著关注。该任务通过学习一个函数，将每个节点映射到其标签，以最小化预测标签与真实标签之间的差异。传统的GNNs采用message-passing框架，聚合邻居节点的信息到中心节点，并使用MLP等分类器基于学习到的表示来预测节点标签。

然而，GFMs在node-level任务上面临挑战，包括：(i) graph heterogeneity，(ii) cross-domain alignment，以及 (iii) domain generalization与task-specific adaptation之间的平衡。

Table 5总结了针对node-level任务的task-specific GFMs。这些方法在Backbone、Pretrain、Adaptation、Feature Align、Structure Align和Task Align等方面有所不同。例如，ENGINE、LLM-GNN、GCNMF、PCFI、GRAFENNE、E-LLaGNN、GraphFM、TPP、SimMLP、MLP、GraphControl、ZeroG、GraphLoRA、MDGFM、GPT-GNN、GSPT、GPPT、GCOPE、GDLALLM、GraphText、LOGIN、LangGSL、Cella、G2P2、LangTopo和Dr.E等方法都采用了GNN或LLM作为Backbone，并结合了不同的Pretrain策略（如Supervised、Contrastive、Generative、Hybrid）和Adaptation方法（如Finetune、Test-time Adaptation、Graph Prompting、Prototype）。在Feature Align方面，一些方法利用Data-Text Attribute、Data-Others、Model-Projection等；在Structure Align方面，则使用了Data-Augment、Model-Retriever、Model-Structure Learning、Model-Prompt Learning、Model-Pretrain、Model-MoE、Model-Codebook等；Task Align则包括N/A、Implicit-Regularizer、Explicit-Subgraph、Explicit-Link、Explicit-QA等。

## 6.2.1 Handling Graph Heterogeneity

本章节探讨了处理Graph Heterogeneity的两种主要挑战：异构特征空间（Heterogeneous Feature Space）和结构异质性（Structure Heterogeneity）。

**异构特征空间（Heterogeneous Feature Space）**

为解决异构特征空间问题，现有方法常使用MLPs将特征映射到共享的潜在空间，但这在特征缺失或动态变化时可能失效。早期研究聚焦于图表示学习中的缺失特征填补问题。GCNmf [234] 利用Gaussian Mixture Model (GMM) [256] 来建模缺失特征，通过计算GNN第一层神经元的期望激活来处理缺失特征并学习图表示。PCPI [235] 在更高缺失率的场景下进一步改进了GCNmf，引入了伪置信度（pseudo-confidence），即缺失特征节点与最近已知特征节点之间的通道（channel）最短路径距离。PCPI提出了一种特征填补方案，通过通道间的节点间扩散（inter-node diffusion）恢复缺失特征，并通过节点间的通道间传播（inter-channel propagation）优化节点特征。

除了缺失特征填补，一些研究也探索了图中的动态特征集问题。GRAFENNE [236] 通过二分图编码（bipartite encoding）实现图的同质性变换（allotropic transformation），将节点与属性特征解耦。GraphAny [66] 基于图核（graph kernels）之间的交互计算全归纳式（fully-inductive）特征，实现了跨异构特征空间的归纳泛化。GRAFENNE还引入了一个二分图消息传递（bipartite message-passing）框架，使得模型参数大小与特征维度无关，从而缓解了图的异构和多样化特征维度问题，并使模型能适应未见过的节点和特征。此外，FUG [257] 提出了一种特征无关（feature-universal）的对比学习（contrastive learning）预训练策略，无需模型重构或数据重塑即可处理特征异质性。它设计了一个带有对比约束的编码器，以模拟Principle Component Analysis [258] 生成基变换矩阵，用于适应不同空间的特征。

**结构异质性（Structure Heterogeneity）**

除了异构特征空间，结构异质性也是构建Graph Foundation Models (GFMs) 进行下游节点分类任务的另一个挑战。GPT-GNN [114] 提出了一种生成式预训练GNNs的策略，该策略可分解为节点属性和边生成步骤，以捕捉无标签图数据中节点属性与图结构之间的内在依赖性。GPPT [74] 在微调（fine-tuning）阶段引入了prompt机制，将输入节点修改为直接应用于预训练GNNs的token对。考虑到GNNs在延迟敏感应用中的部署，simMLP [158] 提出了一种简单高效的自监督学习（self-supervised learning）框架，在图上学习Multiple-Layer Perceptrons (MLPs)，使图上下文感知GNNs编码的表示与邻域无关MLPs对齐，从而将结构信息完全整合到MLPs中。

## 6.2.2 Cross-domain Alignment

本章节探讨了跨领域对齐（Cross-domain Alignment）在Graph Foundation Models (GFMs) 中的应用，旨在解决不同领域图数据在节点特征和结构类型上的差异性。主要方法可以分为三类：基于GNN的模型、基于Transformer的模型以及混合方法。

**基于GNN的模型**

这类方法致力于开发纯GNN的GFMs，以适应跨领域场景。GCOPE [25] 提出了一个“All in One and One for All”框架，在一个模型上训练多样化的数据集，以处理跨领域的下游任务。TPP [239] 引入了Graph Class- Incremental Learning (GCIL)，利用Laplacian smoothing生成任务特定的prototypical embeddings，并采用graph prompting方法，为每个任务学习一个小的判别性graph prompt，实现免回复和免遗忘。GraphControl [240] 利用通用的结构预训练模型对齐输入空间，并将目标数据的独特特征作为条件输入，通过ControlNet [260] 集成到模型中进行微调或prompt tuning，以支持下游节点分类。GraphLoRA [154] 采用Structure-aware Maximum Mean Discrepancy [261] 对齐源域和目标域的节点特征分布，并在微调阶段引入一个小的GNN来弥合结构分布差距并缓解灾难性遗忘。MDGFM [241] 应用token operators进行图间的语义对齐，并通过graph structure learning (GSL) 优化每个源域，整合特征和拓扑信息。GraphAny [66] 采用全归纳设置，包含LinearGNNs以实现对未见图的有效归纳推理，以及一个归纳注意力模块来聚合多个LinearGNNs的预测。

**基于Transformer的模型**

另一类方法直接使用Transformer进行跨领域节点表示学习。GSPT [242] 是一个面向文本属性图（TAGs）的以特征为中心的预训练框架，利用标准Transformer [55] 学习统一的节点表示模型。GraphFM [238] 通过Perceiver-based encoder [262] 将领域特定的特征压缩到公共潜在空间，将GSPT扩展到多领域场景。GDL4LLM [243] 将图视为一种新语言，将其翻译成图语言语料库，并在该语料库上预训练基于Transformer的LLMs，以理解图结构。LLM随后被微调为下游节点分类任务的下一个token预测。

**混合方法**

利用LLMs强大的自然语言理解能力，一些混合方法结合了GNNs和LLMs来开发GFMs，通常针对Text-Attributed Graphs (TAGs) 数据集。G2P2 [247] 使用GNN作为文本分类的预测器，通过文本-节点、文本-摘要和节点-摘要交互的对比策略联合预训练文本和图编码器。ENGINE [232] 提出了一种参数和内存高效的文本图微调方法，通过侧结构将GNN与LLM结合。LLM-GNN [233] 引入了一个无标签的节点分类流程，即“LLMs-as-annotator”，仅在LLMs标注的一小部分节点上训练GNN，以对剩余节点进行节点分类。在此基础上，LOGIN [244] 提出了“LLMs-as-Consultants”范式，仅在低置信度预测节点上咨询LLMs，并根据LLM反馈增强图。Cella [246] 采用主动节点选择过程，根据标签不协调性和熵筛选代表性节点，并通过LLMs标注，然后应用基于Dirichlet Energy的图重构策略来最小化噪声或缺失链接的不利影响。EhLLaGNN [237] 通过LLMs采样高质量邻域，并利用其prompt catalog中的多样化prompt进行按需邻域特征增强，然后将增强的邻域特征与中心节点聚合，生成代表性节点embedding。

另一类混合方法直接使用LLMs作为下游节点级任务的分类器。GraphText [231] 通过将图翻译成自然语言来实现无训练的图推理，通过构建图-语法树并处理其遍历产生的自然语言序列，利用LLMs进行节点预测和推理。zeroG [241] 提出了一种zero-shot learning框架，首先利用LLMs将文本图编码到统一特征空间，然后使用LoRA策略在基于prompt采样的子图数据上训练一个小的语言模型。

表格6总结了在链接级任务上的特定任务GFMs，展示了不同方法的backbone、预训练方式、适应策略、特征对齐、结构对齐和任务对齐方式。

## 6.2.3 Domain Generalization v.s. Task-specific Adaptation

本节探讨了Domain Generalization与Task-specific Adaptation在Graph Foundation Models (GFMs) 中的作用，并对比了LLMs和GNNs的优势。研究表明，LLMs在Domain Generalization方面表现出色，而GNNs则通过建模结构信息在Task-specific Adaptation上更具优势。

为了融合LLMs和GNNs的优势，多项研究致力于在Node Embedding层面实现两者对齐。LangTropo [248]受vector quantization启发，提出了一种框架，将图的语言描述与tokenized topological modeling对齐，使LLMs能够学习图结构。Dr.E [249]则引入了一个dual-residual vector quantized-variational autoEncoder，通过自然语言将LLMs与图数据对齐。GSLM [245]设计了一个co-training pipeline，迭代训练语言模型和GNN。该方法首先利用LLMs过滤原始节点文本中的噪声信息，然后迭代优化LLM和GNN。LLM根据清理后的文本属性生成图结构、embeddings和pseudo labels，而GNN则反过来优化图结构并向LLM提供更新的pseudo labels。

## 6.2.4 Future Direction

尽管节点级任务已引起学术界的广泛关注，并涌现了大量相关研究，但仍有几个方向有待深入探索。未来的关键研究方向包括：超越 message-passing 框架的图模式建模 [86]；GNNs 的鲁棒性 [268]；以及 GNNs 的可解释性 [269, 270]。

## 6.3 Link-Level Task

在图学习中，link-level tasks 专注于理解和预测图中节点之间的关系（或链接）。这些任务对于分析网络结构和动态至关重要，例如社交网络、生物网络或推荐系统。主要任务包括 link prediction、edge classification 和 network completion 等。

专注于 link-level tasks 的 GFMs 需要具备跨不同领域和数据集泛化和迁移知识的能力，这带来了挑战。例如，异构关系是一个重要问题，因为链接可以代表多种语义，如社交网络中的“友谊”与“交易”。在推理过程中，GFMs 必须学习可迁移的表示，以便在具有任意实体和关系词汇的图上进行推理。此外，还必须考虑时间动态，因为动态图（如金融网络）中的链接需要对时间敏感的模式进行建模。

## 6.3.1 Inductive Reasoning Approaches

本章节探讨了用于归纳推理（Inductive Reasoning）的Graph Foundation Models (GFMs)。这类模型主要关注在测试时出现新节点（novel nodes）和新关系类型（relation types）的问题。

**知识图谱（Knowledge Graph）为基础的方法**：
*   **Ultra** [28] 旨在学习通用且可迁移的图表示。它通过一个变换将原始图 $\mathcal{G} = (\mathcal{V},\mathcal{R},\mathcal{E})$ 转换为关系图 $\mathcal{G}_r = \mathrm{LIFT}(\mathcal{G}) = (\mathcal{V}_l,\mathcal{R}_l,\mathcal{E}_l)$。给定一个查询 $(h,q,?)$，可以获得关系图的 $d$ 维节点表示 $\mathbf{X}\in \mathbb{R}^{|\mathcal{R}|\times d}$。Ultra利用关系结构的不变性，并采用相对关系表示（relative relation representations）来参数化任何未见过的关系，而非相对实体表示（relative entity representations）。
*   **UltraQuery** [29] 是另一个GFM，专注于归纳式零样本复杂逻辑查询回答（inductive zero-shot complex logical query answering, CLQA）问题。它引入了新颖的归纳式关系投影（inductive relation projection）设计和一个可微分但非参数化的模糊逻辑算子（fuzzy logical operator），使其能够独立于词汇表（vocabulary-independent），并泛化到新的实体和关系。

**基于双等变性（Double Equivariance）的方法**：
*   从节点和关系类型的双等变性视角出发，研究者们尝试解决在测试时出现新节点和新关系类型的问题。给定一个训练图 $\mathbf{A}^{tr}$（包含节点集 $\mathcal{V}^{tr}$ 和关系集 $\mathcal{R}^{tr}$），目标是学习一个模型，能够准确预测测试图 $\mathbf{A}^{te}$（包含节点集 $\mathcal{V}^{te}$ 和关系集 $\mathcal{R}^{te}$）中缺失的三元组，其中 $\mathcal{V}^{tr}\subsetneq \mathcal{V}^{te}$ 且 $\mathcal{R}^{tr}\subsetneq \mathcal{R}^{te}$。
*   **MTDEA** [279] 将关系集划分为不同的簇，每个簇仅包含可交换的关系类型，将其视为一个多任务设置。因此，它为每个簇（关系类型）训练多个图模型。在测试时，通过一个适应过程（adaptation procedure）将新的关系类型分配到最合适的簇，从而确保对先前未见过关系类型的泛化能力。

**理论分析**：
*   近期研究在理论框架下证明了双等变结构表示的通用性 [278]。研究发现，Ultra [28] 和 InGram [281] 尽管架构设计不同，但都符合该框架。此外，研究者提出了InGram的更鲁棒和稳定的变体，名为DEq-InGram，以及一个名为ISDEA+的建模框架，该框架可以将任何为同质图设计的GNN转换为适用于知识图的双等变模型。
*   同时，[271] 对知识图GFM的表达能力进行了严格研究，发现其表达能力取决于用于学习关系表示的模体（motifs）。对于一个知识图 $\mathcal{G} = (\mathcal{V},\mathcal{R},\mathcal{E})$，该研究将框架总结为三个步骤：使用一组模体 $\mathcal{F}$ 计算关系超图 $\mathrm{LIFT}_{\mathcal{F}}(G)$；在关系超图上应用关系编码器（relation encoder）获得关系表示；利用关系表示和知识图 $\mathcal{G}$ 应用实体编码器（entity encoder）获得最终的链接编码（link encodings）。此外，他们设计了比现有工作中使用的二元模体更丰富的模体，以提高GFM的性能。

## 6.3.2 In-Context Learning Approaches

本节探讨了In-Context Learning（ICL）在图模型中的应用。KG-ICL [272] 提出了一种图提示学习（graph prompt learning）方法，通过提取与查询事实相关的提示图（prompt graph），并使用unifier tokenizer将实体和关系映射为预定义token，以训练foundation knowledge graph model。UniLP [274] 则利用ICL结合了启发式方法（heuristic approaches）的泛化能力和参数化模型（parametric models）的模式学习能力，构建了一个通用的link predictor，能够直接应用于未见过的图数据集，无需针对性训练。

表格7总结了在图级别任务（graph-level tasks）上特定于任务的Graph Foundation Models（GFMs）。这些方法主要基于Graph Neural Networks（GNNs）或大型语言模型（LLMs），并采用了不同的预训练（Pretrain）和适应（Adaptation）策略。预训练方法包括Supervised、Contrastive、Generative和Hybrid。适应策略则涵盖了Fine-tuning、Prototype、Graph Prompting、In-context Learning和Distillation等。为了提升模型性能，研究者们还探索了多种对齐（Alignment）技术，包括特征对齐（Feature Align）和结构对齐（Structure Align），例如Data-Augment、Loss-Auxiliary、Model-Meta Learning、Model-Structure、Code-Book、Data-Node Property、Data-Text Attribute等。部分方法还引入了显式（Explicit）或隐式（Implicit）的任务对齐（Task Align）机制，如Explicit-QA和Implicit-Codebook Learning。

此外，表格还列出了针对图生成（Graph Generation）任务的方法，这些方法同样依赖GNNs或LLMs，并采用了Test-time Adaptation等适应策略，结合了数据增强（Data-Augment）和结构对齐（Structure Align）等技术。

## 6.3.3 Transformer-based Approaches

Transformer-based Approaches 结合了 GNNs 和 Transformers，利用语言模型的泛化能力。GraphFormers 将文本编码和图聚合整合到迭代流程中，将 GNN 组件与 Transformer 块嵌套。Edgeformers 进一步将文本语义融入边，在具有文档的文本-边网络 $\mathcal{G} = (\mathcal{V},\mathcal{E},\mathcal{D})$ 上进行情境化处理，其中每条边 $e_{ij}\in \mathcal{E}$ 都关联一个文档 $d_{ij}\in \mathcal{D}$。语言模型的内在泛化能力赋予这些模型迁移学习的潜力，并作为 link prediction 的 foundation models。

## 6.3.4 Hybrid Methods

本节探讨了混合方法在图学习中的应用。DGASN [276] 提出了一种跨网络同质性和异质性边分类方法，通过对抗性域适应来解决源域到目标域知识迁移中的域发散问题。该方法处理两个图 $\mathcal{G}^A$ 和 $\mathcal{G}^B$ 以及对齐的邻接矩阵 $\mathbf{A}^{A,B}\in \{0,1\}^{n_A\times n_B}$。另一项工作 [275] 提出了图交集诱导迁移学习（GITL）的新设置，即一个更稠密的图可能与稀疏的原始图共享节点，从而为迁移选择性、有意义的知识提供了天然桥梁。该研究还提出了一个从训练实例优化和预测广播两个角度解决此设置的框架。

## 6.3.5 Future Directions

未来Graph Foundation Models (GFMs) 在链接级任务方面，可探索在动态和异构图等更具挑战性的场景中应用in-context learning。另一有前景的研究方向是提升GFMs的计算效率，以实现对真实世界大规模图的可扩展性。这是必要的，因为当前算法通常需要高昂的预处理成本和冗长的训练时间。

## 6.4Graph-Level Task

本章节探讨了Graph-Level Task在Graph Foundation Models (GFMs) 中的应用，主要包括graph classification, graph regression, 和graph generation等任务。当前研究的重点在于pre-training和fine-tuning，旨在构建一个能够适应跨领域数据集和任务的foundation model。然而，由于不同领域图数据的显著差异，例如分子图遵循化学规则，而社交网络具有scale-free或community结构，设计通用算法面临挑战。图的规模也存在巨大差异，从数十个节点的蛋白质图到数百万个节点的引用网络，这要求模型具备灵活的架构。从任务角度来看，不同的Graph-Level Task（如预测药物疗效与分类社交网络）需要不同的inductive biases，这使得multi-task learning变得复杂。

## 6.4.1 Pre-Training Stages

早期研究主要关注图模型的 pre-training 策略，旨在构建可用于各种 downstream tasks 的强大基础模型。L2P-GNN [286] 通过模拟 downstream tasks 上的 fine-tuning 过程来 pre-train GNN 模型，以直接优化 pre-trained 模型对 downstream tasks 的快速适应性。在 pre-training 阶段，L2P-GNN 为图 $\mathcal{G}$ 构建了一个包含 $k$ 个子任务 $\{\mathcal{T}_G^1,\dots,\mathcal{T}_G^k\}$ 的父任务 $\mathcal{T}_G$。它还设计了节点和图级别的双重适应机制，利用无标签图数据的内在结构作为 self-supervision，同时学习局部和全局表示。Mole-BERT [73] 提出了使用三元组 $(\mathcal{G},\mathcal{G}^{M1},\mathcal{G}^{M2})$ 进行图级别 pre-training 的 triplet masked contrastive learning (TMCL)，以模拟分子之间的异构语义相似性，从而实现有效的分子检索。结合 Masked Atoms Modeling (MAM)，其 pre-training 方法在不要求任何 domain knowledge 的情况下取得了优越的性能。GROVER [287] 在其 GNN-Transformer 风格的框架中结合了节点、边和图级别的 self-supervised 任务。在海量无标签分子数据集上进行 pre-training 后，GROVER 可以学习丰富的隐式知识并轻松地将其迁移到 downstream 图级别任务。GraphsGPT [291] 设计了一个端到端的纯 transformer 编码器来学习图词 $\mathcal{W} = \mathrm{Graph2Seq}([\mathcal{G}P]_1,[\mathcal{G}P]_2,\dots,[\mathcal{G}P]_k,\mathcal{FTSeq})$ 和解码器 (GraphGPT) 来恢复图结构 $h,p = \mathrm{GraphGPT}(|\mathcal{W},[BOS])$。在 1 亿个分子上进行预训练后，Graph2Seq 在包括图分类和回归在内的图级别任务中表现出色。同时，GraphGPT 还可以作为一个强大的图生成器。最近的一项研究 [289] 通过衡量 pre-training 数据集对 downstream generalization 的影响以及通过结构化纳入特征信息，分析了 pre-trained GNNs 在不同数据集之间的迁移程度。

## 6.4.2 Fine-Tuning Stages

本节探讨了图模型（Graph Foundation Models, GFMs）的 Fine-tuning 阶段。

**Full Fine-tuning** 方法包括：
*   **G-Tuning**：该方法识别预训练和下游图之间的结构差异，并提出保留下游任务的生成模式，即 graphon。Graphon 是一个连续且对称的函数 $W:[0,1]^2\to [0,1]$，表示两个点 $u_i, u_j \in [0,1]$ 形成边的概率。这种设计使得 G-Tuning 适用于 Cross-domain Transfer 任务。
*   **GOT-Tuning**：该方法将图局部知识迁移（graph local knowledge transfer）表述为带有结构先验（structural prior）的最优传输（Optimal Transport, OT）问题，并构建 GTOT regularizer 来约束 Fine-tuning 模型的行为。通过保留 Fine-tuning 和预训练模型之间的局部特征不变性（local feature invariances），GTOT-Tuning 展现出强大的 generalization ability。

**Parameter-Efficient Fine-tuning (PEFT)** 方法包括：
*   **AdapterGNN 和 G-adapter**：这些方法在 GNN 领域引入了 adapter 模块，其结构为 $(\mathbf{A}(x) = \mathrm{BN}(\mathbf{W}_{up}(\mathrm{ReLU}(\mathbf{W}_{down}(\mathbf{x})))))$。通过引入少量可调参数，它们在提高基础模型泛化能力的同时，性能优于传统的 Full Fine-tuning 方法。
*   **GPF**：作为一种 Prompt Learning 技术，GPF 将可学习的 prompt 向量注入原始数据集的特征空间。具体而言，对于一个可学习的 prompt 向量 $\pmb{p}_i$，节点 $v_i$ 将拥有一个被提示的特征向量 $\hat{\pmb{x}}_i = \pmb{x}_i + \pmb{p}_i$。GPF 进一步简化为所有节点共享一个 prompt 向量，即 $\pmb{p}_1 = \pmb{p}_2 = \dots = \pmb{p}_n = \pmb{p}$。研究者提供了严格的推导来证明 GPF 的通用性并保证其有效性。GPF 的有效性和效率使其成为分子图分类（molecular graph classification）和回归（regression）等下游任务适配的有力替代方案。

## 6.4.3 LLM-incorporated Approaches

本节探讨了将大型语言模型（LLMs）融入图学习的方法，以解决图级别的问题。

**LLM for Understanding**

早期工作将图转换为纯文本，然后使用自然语言对GPT-2和GPT-3进行fine-tuning，在分子分类任务上取得了有希望的结果。GALLON利用多模态分子数据和LLMs（如GPT-4V）的强大预训练知识，通过prompt提取先验知识，其公式为 $\mathcal{R}_{\lambda} = \mathrm{LLM}(\mathcal{P}_{\lambda},\mathcal{E}_{\lambda},\mathcal{S}_{\lambda},\mathcal{I}_{\lambda})$，旨在将GNN和LLM的优势提炼到MLP中，以捕捉分子结构的最有效表示。GIMLET通过应用具有广义位置嵌入和解耦注意力的Transformer机制，扩展了语言模型以处理图和文本数据。它将分子图 $\mathcal{G}$ 和任务指令 $T$ 整合到图-文本语言模型GIMLET中，并统一解码不同任务的输出为文本，即 $\hat{y}_{str} = \mathrm{GIMLET}(\mathcal{G},T)$，其中 $\hat{y}_{str}$ 是标签字符串。GIMLET的指令式预训练使其能够迁移到广泛的zero-shot图级别任务。UniMoT引入了一个专门为LLMs设计的分子tokenizer，能够将分子token化为因果依赖的短序列。它通过共享的token表示和自回归训练范式，统一了分子 $\{s_i\}_{i = 1}^M$ 和文本 $\{t_i\}_{i = 1}^M$ 的模态。借助LLMs和多阶段训练策略，UniMoT在图理解和生成任务上均表现出色。

**LLM for Generation**

LLM4GraphGen则探索了LLMs在图生成方面的能力，通过系统化的任务设计和广泛的实验。研究人员设计了全面的实验来评估LLMs的图生成能力，提出了不同难度的任务，包括基于规则的图生成、基于分布的图生成和基于属性的图生成。对不同LLMs和prompt的测试揭示了深刻的见解。

## 6.4.4 Graph Generation

本章节探讨了Graph Generation，这是Graph-level tasks的一个重要子领域，目标是生成符合特定规则、分布或领域属性的图。为Graph Generation设计GFMs需要处理跨领域的广泛结构和语义复杂性。传统的图生成模型（如GraphVAE, GDSS, DiGress）通常局限于单一领域且泛化能力较弱。近期工作如UniAug通过引入跨越不同图分布的diffusion models来解决这一问题，追求通用性。UniAug采用了一个仅结构的离散diffusion model，在数千个图上进行pre-training，并通过引导式结构合成来增强下游数据集，从而在不依赖特征相似性的情况下提高泛化能力。这些方法标志着Graph Generation向跨领域可扩展性的转变，使GFMs具备了与语言和视觉foundation models相似的多任务和多领域能力。

受Stable Diffusion和GPT等大型生成模型的成功启发，近期的Graph Foundation Models（GFMs）采用大规模pre-training和cross-modal prompting来增强Graph Generation。LGGM在13个领域的5000多个图上进行pre-training，编码了多样化的结构模式，实现了卓越的zero-shot和fine-tuned generation。LGGM还引入了Text-to-Graph generation，用户可以通过文本提示（如图领域或结构统计信息，例如clustering coefficient）来指导生成，利用了语言模型中嵌入的世界知识。与此同时，InstructG2I提出了一种multi-modal方法，通过图像和文本属性丰富图结构数据，以指导基于diffusion的图像生成。其图条件生成（graph-conditioned generation）既富有表现力又可控，能够在风格或领域之间实现平滑插值。这些pre-training和prompting策略体现了LLMs和GNNs之间日益增长的协同作用，将GFMs的边界扩展到开放式、用户可控的图合成领域。

## 6.4.5 Hybrid Approaches

本节探讨了图模型领域的其他相关工作，重点关注混合方法。

**少样本图分类 (Few-shot Graph Classification)**

*   **CDFSGC [285]** 和 **CDTC [300]** 解决了跨域少样本图分类问题。在这种设置下，目标是学习一个具有良好泛化能力的模型，该模型能够根据目标域的少量标注样本和源域数据来预测目标域图的标签，其中目标域 $\mathcal{D}^T$ 和源域 $\mathcal{D}^S$ 具有不同的边际分布 $\mathcal{P}_{\mathcal{D}^T}$ 和 $\mathcal{P}_{\mathcal{D}^S}$，并且标签空间 $\mathcal{Y}^S$ 和 $\mathcal{Y}^T$ 是不相交的。
*   **CDFSGC [285]** 提出了一种图编码器，该编码器学习关注图的三个同等视图：一个上下文视图和两个拓扑视图，以学习任务特定信息的表示，用于快速适应，以及任务无关信息的表示，用于知识迁移。结合基于度量的元学习框架，该方法在不同域的三个图分类任务上取得了优异的性能。
*   **CDTC [300]** 为了解决域偏移问题，设计了一个新颖的跨域任务协调器 (Cross-domain Task Coordinator, CDTC)，利用一小组标注的目标域数据作为提示任务 $\{\mathbf{p}^t\}_{t = 1}^T$，然后建模元任务与提示任务之间的关联并发现相关性。在与基于优化的元学习过程集成并通过强化学习端到端训练后，CDTC 在多个跨域少样本图分类任务上表现出色。

**分布外检测 (Out-of-Distribution Detection)**

*   **AAGOD [282]** 为一个经过良好训练的 GNN 赋予了跨域 ODD 检测能力，其中我们有图空间中定义的两个不同分布 $\mathcal{P}_{in}$ 和 $\mathcal{P}_{out}$。在训练阶段，可获得从分布内 $\mathcal{P}_{in}$ 采样的图数据集 $\mathcal{D}_{id} = \{G^1,\dots,G^n\}$，模型学习的目标是在测试阶段区分一个图是否属于分布内 $\mathcal{P}_{in}$。AAGOD 通过设计一个包含可学习放大器生成器 (Learnable Amplifier Generator, LAG) 和正则化学习策略 (Regularize Learning Strategy, RLS) 的有效框架，无需修改其参数。

**表 8 总结了在问答、推荐和异常检测任务上的特定任务 GFM。**

*   **问答 (Question Answering)**：包括 MCDGRAPH [301] (GNN, Generative pretrain, In-context adaptation)，GT2Vec [302] (LLM, Contrastive pretrain, Finetune adaptation)，GPT-4V-GSR [303] (LLM, Generative pretrain, In-context adaptation)，G-Researcher [304] (GNN + LLM, Supervised pretrain, In-context adaptation)，GITA [305] (GNN + LLM, Generative pretrain, In-context adaptation)，GFM-RAG [306] (GNN + LLM, Hybrid pretrain, In-context adaptation)。这些方法主要通过数据-文本属性进行特征对齐，并显式地对问答任务进行对齐。
*   **推荐 (Recommendation)**：包括 SR-MDFM [27] (GNN, Supervised pretrain, Test-time Adaptation)，PCRec [307] (GNN, Contrastive pretrain, In-context adaptation)，LLMRec [308] (GNN, Hybrid pretrain, In-context adaptation)，VIPS [309] (LLM, Generative pretrain, In-context adaptation)，2T [310] (GNN + LLM, Supervised pretrain, In-context adaptation)，RLMRec [311] (GNN + LLM, Hybrid pretrain, In-context adaptation)。这些方法在特征对齐、结构对齐和任务对齐方面采用了多种策略，如数据-文本属性、数据增强和预训练损失。
*   **异常检测 (Anomaly Detection)**：包括 AnomalyGFM [26] (GNN, Supervised pretrain, Prototype adaptation)，CDFS-GAD [312] (GNN, Contrastive pretrain, Graph Prompting adaptation)，ACT [313] (GNN, Contrastive pretrain, Prototype adaptation)，UNPrompt [314] (GNN, Contrastive pretrain, Test-time Adaptation)，ARC [315] (GNN, Generative pretrain, Prototype adaptation)，Commander [316] (GNN, Hybrid pretrain, Test-time Adaptation)。这些方法主要利用模型投影、模型提示学习、预训练损失和数据增强等技术进行适应。

## 6.4.6 Future Directions

未来Graph Foundation Models (GFMs)在图级别任务上的发展方向在于构建统一且灵活的架构，例如结合结构编码的Graph Transformers，以捕捉领域无关的属性，并实现多尺度表示的层级化Pooling。通过子图采样、线性化Attention和分布式训练可以缓解可扩展性挑战，而Meta-learning和Prompt-based fine-tuning将支持快速适应新领域。通过图去噪自编码器和数据增强可提升对噪声和稀疏性的鲁棒性。整合多模态数据（如文本、图像）以及创建具有统一指标的跨领域基准将进一步推动评估和标准化。最后，通过可解释Pooling优先考虑可解释性，通过对抗性去偏（adversarial debiasing）确保公平性，将保障可信赖和合乎道德的AI应用，从而推动GFMs在药物发现、欺诈检测和气候建模等领域实现革新。

## 6.5 Question Answering

本章节探讨了Question Answering (QA) 任务在Graph Foundation Models (GFMs) 中的应用。现有研究通常结合Graph Neural Networks (GNNs) 和Large Language Models (LLMs) 来生成答案。

GFM-RAG [306] 提出了一种用于QA任务的retrieval augmented generation的graph foundation model。它首先从文档中构建知识图谱索引 (KG-index) 来捕捉实体间的关系。然后，将查询和构建的KG-index输入到预训练的GFM retriever中，以获取与LLM生成相关的文档。该GFM retriever经过大规模训练，可直接应用于未见过的数据集，无需fine-tuning。

类似地，G-Retriever [304] 在LLM生成QA任务答案之前，引入了额外的子图构建步骤。此外，G-Retriever还提供了一个GraphQA benchmark，包含ExplaGraphs [317]、SceneGraphs [318]和WebQSP [319, 320]三个数据集。

GITA [305] 引入了一个graph visualizer组件来生成图可视化。这些可视化的图与图结构的文本描述一起输入到visual language models (VLMs) 中，以完成QA任务。另一项工作 [303] 通过整合图像编码和OCR等multimodal technologies，提出了一种理解和推理graph image data的范式。VGCURE [301] 提供了一个全面的benchmark，包含22个任务，用于评估VLMs的基本理解和推理能力。GT2VEC [302] 是一个框架，通过将graph embeddings投影到text embedding space并使用contrastive learning进行对齐，利用LLMs学习文本和图数据的联合embedding。这种方法增强了QA任务中模态间的语义一致性。

未来的研究方向集中在提升GFMs在QA任务中的适应性、可扩展性和推理能力。一个有前景的方向是在检索过程中从非结构化数据动态构建图，使模型能够即时创建上下文相关的图 [321, 322]。Multimodal integration是另一个关键方向，它允许GFMs处理文本、视觉和其他模态，以实现更丰富的推理能力 [323, 294]。此外，提高GFMs的可解释性和透明度对于需要信任和问责的应用（如医疗或法律QA系统）至关重要 [323, 324]。

## 6.6 Graph Anomaly Detection

本章节探讨了Graph Anomaly Detection (GAD) 的相关研究，其目标是识别偏离大多数样本的节点和结构层面的异常样本。

早期研究主要集中在 Cross-Domain Graph Anomaly Detection (CD-GAD)，即在目标图缺乏标签的情况下，利用辅助的、相关的源图（包含标记的异常和正常节点）来训练模型以检测异常节点。这些研究通常采用domain adaptation方法。Commander [316] 提出了三个组件：用于domain alignment的domain discriminator、用于检测异常的anomaly classifier，以及提供额外信号评估节点异常的attribute decoder。ACT [313] 也提出了一种domain adaptation方法，该方法联合优化了两个目标：（i）在目标图中对正常节点表示进行unsupervised contrastive learning；（ii）一种anomaly-aware one-class alignment，将对比学习得到的节点表示与源图中标记的正常节点表示对齐。在contrastive learning阶段，CD-GAD还强制使正常节点表示偏离源图中的异常节点表示。

除了CD-GAD，CDFS-GAD [312] 提出了一个更普遍且复杂的情景：Cross-Domain Few-Shot Graph Anomaly Detection。其目标是利用来自相关但不同域的辅助图，在标签稀疏的目标图中识别异常。为了解决这个问题，CDFS-GAD引入了一个prompt tuning模块来提取特定于每个域的特征，并设计了一个自适应超球分类损失（adaptive hypersphere classification loss），通过域敏感范数（domain-sensitive norms）增强正常和异常实例之间的区分度。

近期，一些研究开始关注Graph Foundation Models (GFMs) 在GAD中的应用。ARC [315] 设计了一个“one-for-all” GAD模型，能够即时（on-the-fly）检测各种图数据集中的异常。该模型利用in-context learning，在推理阶段通过少量正常样本提取目标数据集的特定模式，而无需在目标数据集上进行fine-tune。其他研究则侧重于zero-shot GAD任务，即目标图中不提供任何标签信息。UNPrompt [314] 引入了一个简单的prompt tuning模块，该模块在最小化异常节点表示的同时，捕捉正常节点潜在属性中的通用模式。AnomalyGFM [26] 提出了一个用于图异常检测的GFM，它利用图无关表示（graph-agnostic representations）来实现强大的zero-shot泛化能力。此外，如果样本标签可用，AnomalyGFM支持跨不同图数据集的few-shot prompt tuning。通过将可学习的正常和异常类别原型（class prototypes）与节点表示残差（node representation residuals）对齐，AnomalyGFM提炼出区分性特征，从而在统一的特征空间中实现有效的异常度量。

未来的研究方向包括：针对动态图和异构图的GAD方法，因为现实世界的图通常是动态演变的，并且在节点属性和结构上都是异构的（例如社交网络和金融交易网络）[325, 326]。提高GNNs对对抗性攻击和噪声数据的鲁棒性是另一个关键研究焦点[327]。此外，提高基于GNN的异常检测模型的解释性对于建立信任至关重要，尤其是在高风险应用中，如网络安全和欺诈检测等[325]。

## 6.7 Recommendation

推荐系统作为人工智能的重要分支，旨在通过用户交互数据理解用户偏好、历史行为和产品特征。基于图的推荐方法在捕捉复杂用户-物品关系方面表现出色，已成为最先进的技术。随着Graph Foundation Models (GFMs)和Large Language Models (LLMs)的发展，它们为现代推荐系统提供了新视角。然而，推荐系统面临着可扩展性、实时性要求、领域特定语义以及动态用户行为等挑战。例如，大型电商平台涉及数十亿节点和边的图，对计算资源构成压力；不同领域存在不同的交互语义（如电商的“购买”与社交网络的“关注”），用户兴趣也会随时间变化，要求模型适应时间模式。

**GNN-based Approaches:** PCRec [307] 提出了一种用于跨域推荐的预训练Graph Neural Network (GNN)模型，采用对比自监督预训练策略。预训练的GNN encoder可用于目标域生成Node Embedding，并通过BPR loss在二部推荐系统中进行Fine-tuning。

**LLM-based Approaches:** LLMRec [308] 旨在解决推荐系统中隐式反馈信号稀疏的问题，通过整合LLMs来增强用户-物品交互边、物品节点属性和用户节点属性，其表示形式为 $\mathcal{P}_u = \mathrm{LLM}(S_u,Q_u)$ 和 $\mathcal{P}_v = \mathrm{LLM}(S_v,Q_v)$。通过使用去噪数据鲁棒化机制训练GNN backbone，LLMRec在多个基准测试中取得了优异性能。RLMRec [311] 是一个模型无关的框架，旨在通过LLM赋能的表示学习来增强现有的GNN-based推荐器。RLMRec还利用对比和生成对齐技术，将Collaborative Filtering (CF)侧的关系嵌入与LLM侧的语义表示对齐，有效降低了特征噪声。在 [310] 中，研究者首次提出了一种针对个性化的基于图的Foundation Modeling方法。他们结合了LLMs和Heterogeneous Graph Neural Networks (HGNNs)的优势，设计了一种Two-Tower (2T)架构，其中HGNN生成通用表示，而2T组件在连续空间中建模海量的用户-物品交互数据。这种方法的好处在于统一了跨任务的表示学习并促进了信息共享。

**Future Directions:** Graph Foundation Models在推荐系统领域的未来发展方向包括：设计轻量级GFM架构和分布式训练框架以提高可扩展性并有效管理大规模图；探索将图结构与文本、图像等多模态数据进行整合；采用Prompt-based Learning实现任务特定的推荐；以及引入动态GFMs以捕捉实时交互和用户兴趣变化。

## 7 Domain-Specific Graph Foundation Models

本章探讨了**Domain-Specific Graph Foundation Models (GFMs)**，即针对特定领域的图基础模型。与通用GFMs不同，领域特定GFMs旨在通过在特定领域数据上进行**pre-training**和**fine-tuning**，以更好地适应和解决特定领域的图学习任务。

**核心论点**在于，虽然通用GFMs展现了强大的跨领域迁移能力，但在许多专业领域，如生物信息学、化学、金融和社交网络分析等，数据特性和任务需求差异巨大。直接应用通用GFMs可能无法达到最优性能，甚至可能存在偏差。因此，开发和应用领域特定GFMs是提升图学习在这些专业领域应用效果的关键。

**方法论**上，领域特定GFMs的构建通常涉及以下几个关键步骤：

*   **领域数据收集与预处理**: 针对特定领域（如蛋白质-蛋白质相互作用网络、分子图、金融交易图等）收集大规模图数据，并进行必要的清洗和格式化。
*   **领域特定的pre-training**: 在收集到的领域数据上，利用**self-supervised learning**技术对模型进行预训练。常用的预训练任务包括：
*   **Node Embedding**: 学习节点的低维表示，捕捉节点间的结构和语义信息。
*   **Link Prediction**: 预测图中节点之间是否存在连接。
*   **Graph Classification/Regression**: 预测整个图的属性。
*   **Contrastive Learning**: 通过对比正负样本来学习区分性的表示。
*   **Masked Graph Modeling**: 类似于Transformer中的masked language modeling，随机遮蔽图的某些部分（节点、边或属性），然后让模型预测被遮蔽的内容。
*   **模型架构**: 领域特定GFMs通常基于强大的图神经网络（GNNs）架构，如**Graph Neural Networks (GNNs)**的变体，包括**Graph Convolutional Networks (GCN)**, **Graph Attention Networks (GAT)**, **GraphSAGE**等，以及结合**Transformer**的架构。这些模型能够有效地处理图的结构信息和节点特征。
*   **Fine-tuning**: 将预训练好的领域特定GFMs在下游的特定领域任务上进行微调。这些任务可能包括：
*   **Node Classification**: 预测节点的类别（例如，在生物网络中预测蛋白质的功能）。
*   **Link Prediction**: 预测新的连接（例如，在社交网络中推荐好友）。
*   **Graph Classification**: 对整个图进行分类（例如，在化学中预测分子的性质）。
*   **Graph Generation**: 生成新的图结构（例如，设计新的分子）。
*   **Graph Anomaly Detection**: 检测图中的异常模式。
*   **In-context Learning / Few-shot Learning / Zero-shot Learning**: 领域特定GFMs也支持在少量样本（**few-shot learning**）或无样本（**zero-shot learning**）的情况下，通过**in-context learning**的方式快速适应新任务，而无需进行完整的**fine-tuning**。

**结果**方面，研究表明，与通用GFMs相比，领域特定GFMs在各自的领域内通常能取得显著的性能提升。它们能够更好地捕捉领域特有的图结构、节点属性和关系模式，从而在各种下游任务上表现出更强的泛化能力和更高的准确性。例如，在药物发现领域，针对分子图训练的领域特定GFMs在预测分子活性方面优于通用模型。在金融领域，针对交易网络训练的模型在欺诈检测任务上表现更佳。

本章还讨论了领域特定GFMs在处理**Heterogeneous Graph**和**Homogeneous Graph**时的不同策略，以及如何通过**Cross-domain Transfer**和**Domain Adaptation**技术来进一步增强模型的鲁棒性和适用性。此外，**Knowledge Graph**作为一种重要的领域特定图结构，也得到了重点关注，领域特定GFMs在知识图谱补全、问答等任务上展现出巨大潜力。

总而言之，本章强调了领域特定GFMs在推动图学习技术在各个专业领域落地应用中的重要性，并概述了其构建、训练和应用的通用方法论。

## 7.1 Design Principle

本章节阐述了设计领域特定 Graph Foundation Models (GFMs) 的核心原则。尽管 foundation models 具有通用性，但设计能够跨相关任务泛化的领域特定 GFMs 越来越受关注。这类模型需有效捕捉目标领域的内在原理和关键属性，例如在分子图（molecular graphs）中识别和保留关键 motifs 和 functional groups，在知识图（knowledge graphs）中推断 triplets 间的关系和相关性。

设计领域特定 GFMs 的关键原则包括：

*   **Domain-Specific Expertise**: 不同领域具有独特的结构属性和知识形式，不存在普适的 inductive bias。因此，领域特定 GFMs 需要定制化的模型架构、pre-training paradigms 和 adaptation strategies。例如，分子图需要 subgraph-level augmentation 来保留语义组件，而知识图则常需要 node-level 或 edge-level augmentation 来生成 triplets 和增强 relational reasoning。

*   **Learning Task-Agnostic Representations**: 同一领域内的任务和图通常高度相关，可以学习一种通用的 graph representation 来服务于多个 downstream tasks。可采用 multi-task learning、adversarial learning、augmentation strategies 和 domain regularization 等技术。然而，task interference 仍是挑战，可能导致 negative transfer effects。为缓解此问题，可引入 task-aware output heads 或 advanced task alignment strategies 来改进 task-specific adaptation，同时保持共享的领域知识。

*   **Enhancing Interpretability and Trustworthiness**: 在药物发现、数学推理、学术研究等领域，GFMs 不仅需要高性能，还需要生成可解释的洞察以推动领域发展。例如，在大型分子数据集上 pre-trained 的 GFM 可助力发现新的 functional groups、reaction mechanisms 或 physicochemical properties。因此，领域特定 GFMs 必须优先考虑 interpretability 和 trustworthiness，可能涉及 explainable AI techniques、uncertainty quantification 和 domain-specific validation mechanisms。

后续章节将系统探讨八个不同领域的 GFMs 设计原则：分子图、heterogeneous graphs、知识图、temporal graphs、学术领域、graph-based mathematical reasoning、causal graphs 和 semantic document graphs。每个领域将讨论其设计理念、关键挑战、state-of-the-art methodologies 和未来研究方向。

## 7.2 Biology & Molecule Graph

分子图在原子和键级别具有丰富的结构复杂性和化学特征多样性，这与其它图领域不同，带来了独特的挑战。与 homogeneous graph 不同，分子表示必须捕捉化学对称性，例如对旋转、平移和原子置换的不变性。此外，分子性质源于多尺度的复杂相互作用，从局部官能团到全局分子拓扑，并受到量子效应和灵活的3D构象的影响，这些都无法仅通过2D连接性来捕捉。其他挑战包括在天文数字般庞大的分子空间中的可扩展性，以及由于实验成本高昂而导致的标记数据有限。这些问题需要专门的 Graph Foundation Models (GFMs)，整合对称感知、self-supervised learning 和 physics-informed 方法，以实现可靠的分子预测和泛化。

Table 9 总结了在生物和分子图领域应用的领域特定 GFMs。这些方法主要基于 GNNs 或 LLMs，或两者的结合。

**GNN-based GFMs**：
*   **MiniMol [88]** 使用 GNN 作为 backbone，通过 supervised pre-training 进行训练，并通过 finetuning 进行 adaptation。
*   **DPA-2 [328]** 和 **JMP [30]** 也采用 GNN backbone，使用 supervised pre-training，并通过 finetuning 或 distillation 进行 adaptation。JMP 通过多任务 loss 来 align structure。
*   **MACE [329]** 和 **MolGPS [331]** 使用 GNN backbone，进行 supervised pre-training。MACE 通过 node property 来 align feature，MolGPS 通过 node property 来 align structure，并在 test-time 进行 adaptation。
*   **DIG [332]** 使用 GNN backbone，进行 supervised pre-training，通过 finetuning 进行 adaptation，并使用 text attribute 来 align feature 和 data augmentation 来 align structure。
*   **GROVER [287]** 和 **GTFM [333]** 使用 GNN backbone，进行 generative pre-training，并通过 finetuning 进行 adaptation。GTFM 通过多任务 loss 来 align structure。
*   **Mole-BERT [73]** 使用 GNN backbone，进行 hybrid pre-training，并通过 finetuning 进行 adaptation，同时使用 pre-training loss 和 codebook model 来 align structure。

**LLM-based GFMs**：
*   **MolecularGPT [334]** 和 **GP-GPT [335]** 使用 LLM 作为 backbone，进行 supervised pre-training，并通过 finetuning 和 in-context learning 进行 adaptation。它们使用 text attribute 来 align feature，GP-GPT 还使用 data augmentation 来 align structure。两者都通过 explicit QA 来 align task。
*   **BioBRIDGE [336]** 使用 LLM backbone，进行 contrastive pre-training，并通过 in-context learning 进行 adaptation。它使用 text attribute 来 align feature，并使用 pre-training loss 来 align structure。
*   **GraphsGPT [291]** 和 **CaM-Mo [337]** 使用 LLM backbone，进行 generative pre-training，并通过 finetuning 进行 adaptation。GraphsGPT 使用 data augmentation 来 align structure，CaM-Mo 使用 pre-training loss 来 align structure。两者都通过 explicit QA 来 align task。
*   **CaR [338]** 使用 LLM backbone，进行 generative pre-training，并通过 finetuning 和 in-context learning 进行 adaptation。它使用 text attribute 来 align feature，并使用 data augmentation 来 align structure。
*   **UniMot [31]** 和 **MolCA [347]** 使用 LLM backbone，进行 generative pre-training，并通过 finetuning 进行 adaptation。它们使用 text attribute 来 align feature，并使用 pre-training model 来 align structure。两者都通过 explicit QA 来 align task。
*   **ReLM [348]** 使用 LLM backbone，进行 generative pre-training，并通过 in-context learning 进行 adaptation。它使用 node property 来 align feature，并使用 pre-training model 来 align structure。

**GNN + LLM GFMs**：
*   **InstructMol [339]** 和 **ALIGNM [340]** 使用 GNN + LLM 混合 backbone，进行 supervised pre-training，并通过 finetuning 进行 adaptation。它们使用 text attribute 来 align feature。InstructMol 使用 auxiliary loss 和 retriever model 来 align structure，并进行 explicit QA。
*   **GIMLET [293]** 和 **MoleculeSTM [342]** 使用 GNN + LLM 混合 backbone，进行 supervised 或 contrastive pre-training，并通过 in-context learning 或 finetuning 进行 adaptation。它们使用 text attribute 来 align feature。GIMLET 进行 explicit QA。MoleculeSTM 使用 pre-training loss 来 align structure 并进行 explicit QA。
*   **GALLON [294]** 使用 GNN + LLM 混合 backbone，进行 supervised pre-training，并通过 distillation 进行 adaptation。它使用 node property 来 align feature，并使用 auxiliary loss 来 align structure。
*   **Text2Mol [341]** 和 **GIT-Mol [344]** 使用 GNN + LLM 混合 backbone，进行 contrastive pre-training，并通过 finetuning 进行 adaptation。它们使用 text attribute 来 align feature，并使用 multi-task loss 来 align structure。GIT-Mol 进行 explicit QA。
*   **CLAMP [343]** 和 **MolCA [347]** 使用 GNN + LLM 混合 backbone，进行 contrastive 或 generative pre-training，并通过 finetuning 进行 adaptation。它们使用 text attribute 来 align feature，并使用 pre-training loss 来 align structure。两者都进行 explicit QA。
*   **MolMu [346]** 使用 GNN + LLM 混合 backbone，进行 contrastive pre-training，并通过 finetuning 和 in-context learning 进行 adaptation。它使用 text attribute 来 align feature，并使用 codebook model 来 align structure。

## 7.2.1 Graph Model-based Approaches

图模型方法在分子科学中扮演重要角色，因为分子天然可表示为原子和键的图。Graph Neural Networks (GNNs) 中的 message-passing 算子能够显式建模图内的局部和长程相互作用，生成结构感知的表示，这对于准确的 property predictions 至关重要。

**3D Graph 方法** 专注于开发整合三维 (3D) 坐标和对称性的 equivariant graph models。Equivariant Foundation Model for Atomistic Materials Chemistry [329] 能够保持旋转和翻译对称性，从而在材料化学中实现准确的 classification 和 link prediction。Joint Multi-domain Pre-training (JMP) [30] 使用 GemNetOC 来连接小分子、催化剂和块状材料，进行 atomic property prediction，并证明了 equivariant 3D message-passing 策略可以泛化到不同的化学领域。

**2D Graph 方法** 则侧重于纯粹的 2D 连接性和 multi-task learning。Mole-BERT [73] 结合了 Graph Isomorphism Network (GIN) 与 masked-atom modeling 和 contrastive tasks，通过利用学习到的 atom-level representations 提升了 property prediction。Graphium [352] 类似地支持跨量子力学和 bioassay 数据集的 multi-task learning，使用了 GCNs 或 GINE 变体。这些框架表明，在 2D 分子图上进行大规模或 multi-task pre-training 可以为 toxicity classification 或 ADMET endpoints 等任务带来强大的预测性能。

**Efficiency-Focused Methods** 方面，一些近期研究优先考虑参数效率。MiniMol [88] 采用紧凑的 GNN-based 设计和 multi-task pre-training 来同时处理量子和生物 assays。MiniMol 通过使用更少的参数同时保持强大的预测能力，体现了向更易于部署的 foundation-like GNN 架构发展的趋势。总而言之，这些方法表明，精心设计的 message passing（无论是 2D 还是带有显式 3D 坐标）仍然是分子 property prediction 的可靠基础，并为后续的 multi-modal 或 language-driven models 提供了跳板。

## 7.2.2 Language Model-based Approaches

本节探讨了基于语言模型（LM）的方法，其灵感来源于Transformer在序列数据（包括自然语言）中捕捉复杂依赖关系的卓越成功。由于分子可以被线性化（例如通过SMILES）或进行其他标记化处理，研究人员探索了纯粹的Transformer架构来模拟化学或生物序列，将其视为语言数据。

**Transformer-based Models**

一类重要的LM方法将Transformer直接应用于分子图。GROVER结合了GNN式的message passing和全局self-attention，用于大规模属性预测。DiG（基于Graphormer风格设计）模拟了分子构象的整个平衡分布，提供了超越简单终点预测的热力学洞察。GraphGPT将每个节点和边视为“token”，以纯粹的Transformer方式在1亿个分子上进行训练，而Graph Transformer Foundation Model (GTFM) 则专注于ADMET任务。BioBridge则利用Transformer跨多个生物医学模态对知识图谱三元组 $(v_{1},e_{ij},v_{j})$ 进行对齐，而不依赖于GNN。

**Large Language Models**

另一方向完全绕过了图编码，将化学或生物字符串作为大型语言模型（LLM）的输入。例如，有研究探索了LLM本身是否能在zero-shot或few-shot设置下处理分子属性预测。MolecularGPT通过引入结构“邻居”演示来丰富SMILES提示，以指导预测。在小分子之外，ESMFold利用在蛋白质序列上训练的LLM（ESM-2）来预测具有原子级分辨率的3D蛋白质结构。类似地，GP-GPT采用基于Llama的模型将基因组序列映射到表型，将基因组知识转化为文本提示。对于跨模态检索场景，Text2Mol将文本查询和化学表示（如fingerprints）嵌入到共享的嵌入空间中。总的来说，这些基于序列的Transformer和LLM展示了self-attention机制在捕捉化学和生物模式方面的多功能性，即使没有显式的图message passing。

**GNNs as Auxiliary Models**

一些研究将GNN派生的embeddings $\mathbf{Z} = \mathrm{GNN}(\mathbf{X},\mathbf{A})$ 传递给Q-Former或类似的投影模块，生成离散的“分子token” $\mathbf{z}_{\mathrm{token}}$ ，与文本数据 $\mathbf{d}_{\mathcal{G}}$ 一起处理。MolCA和UniMoT通过将图编码的结构信息注入到冻结的LLM中，用于分子到文本生成、检索或字幕等任务，阐释了这一原理。GIT-Mol将这一概念扩展到涉及图、图像和文本的三向多模态设置 $(\mathbf{Z},\mathbf{d}_{\mathcal{G}},\mathbf{x}_{\mathrm{img}})$ 。类似地，GIMLET和Molecular Multimodal Foundation Model将GNN派生的特征 $\mathbf{Z}$ 与文本提示一起纳入基于指令或基于注意力的框架中。InstructMol利用分子-文本对比预训练来对齐图编码器 $\mathrm{GNN}(\cdot)$ 与语言模型，而一种多模态结构-文本方法则采用对比目标进行文本驱动的分子检索和编辑。

## 7.2.3 Hybrid Approaches

尽管Graph Neural Networks (GNNs)擅长捕捉局部连接性和结构细节，而语言模型（如Transformer或LLMs）则能捕捉全局或语义细节（尤其是在涉及文本时），但单一模型可能不足以应对复杂的现实世界应用。混合模型整合了来自GNNs的结构归纳偏置，表示为 $\mathrm{GNN}(\mathbf{X},\mathbf{A})$，以及来自Transformers或LLMs的基于语言的推理，表示为 $\mathrm{LLM}(\mathbf{d}_{\mathcal{G}})$，从而为多样化任务提供更全面的分子表示。

在任务专业化方面，一些混合模型明确针对更广泛或更专业的任务。ReLM [348]将反应预测表述为：首先使用GNN输出 $\mathbf{Z}_{\mathrm{candidates}}$ 生成候选产物，然后由LLM根据反应条件 $\mathbf{d}_{\mathrm{reaction}}$ 进行条件化排序。CLAMP [343]将分子编码器 $\mathbf{Z}_{\mathrm{mol}}$ 与基于文本的生物测定描述 $\mathbf{d}_{\mathrm{bioassay}}$ 对齐，以实现zero-shot发现任务。MolGPS [331]将message-passing neural networks (MPNN)与Transformer模块相结合，以提高在大规模监督数据集上的可扩展性。DPA-2 [328]整合了保持对称性的GNN层和基于Transformer的注意力机制，用于多任务分子模拟。MolFM [345]则统一了图嵌入、文本Transformer嵌入和知识图谱特征 $\mathbf{Z}_{\mathrm{KG}}$，以实现跨模态检索。此外，还有专门的混合设计，如GALLON [294]，它将GNN和LLM的表示蒸馏到一个单一的多层感知机 (MLP) $\hat{y} = \mathrm{MLP}(\mathbf{z}_{\mathrm{GNN}}\| \mathbf{z}_{\mathrm{LLM}})$ 中，用于分子性质预测。Hybrid-LLM-GNN [340]则整合了晶体学嵌入 $\mathbf{Z}_{\mathrm{crystal}}$ 和基于语言的特征，用于材料性质推断。总而言之，这些混合方法通过结合图级别的归纳偏置和基于语言的模型，展示了显著的优势，在分子性质预测、反应建模和文本引导的分子操作等任务中取得了稳健的性能。

## 7.2.4 Future Directions

未来在分子图领域的Graph Foundation Models (GFMs) 的发展方向主要集中在几个有前景的研究趋势。首先，开发能够显式编码旋转 $(R)$ 和平移 $(T)$ 等对称性的等变GNN架构，对于准确建模分子性质至关重要。利用大规模无标签分子数据集进行自监督预训练，可以显著增强泛化能力和预测鲁棒性，尤其是在处理新颖分子骨架时。将量子化学原理和物理定律融入的Physics-informed neural networks是另一个关键方向，能够实现更忠实的化学相互作用建模。最后，结合分子图数据与文本和结构上下文的多模态检索增强策略，对于提高药物发现和材料设计等高风险应用中的可解释性和可靠性至关重要。

## 7.3 Algorithmic Graphs

本章探讨了“算法图”（algorithmic graphs），即用于表示算法过程、组合结构和数学关系的图结构输入。这些图编码了需要对离散结构进行推理的过程性任务，例如最短路径查找、可满足性检查、排序和符号数学。与侧重于语义推理的传统图学习任务不同，算法图问题要求模型能够模仿或泛化经典算法的行为。本节回顾了专为算法推理设计的Graph Foundation Models (GFMs)，重点介绍了它们捕捉结构不变性、支持多步推理以及跨不同大小和复杂度的实例进行泛化的能力。此外，还总结了推动这一新兴方向发展的代表性基准、学习范式和模型架构。

## 7.3.1 Structured Graph Reasoning

本章节探讨了结构化图推理（Structured Graph Reasoning）的两种主要方法：面向任务（Task-Oriented）和指令微调（Instruction-Tuned）。

**面向任务的方法**：早期研究侧重于构建能够处理多种算法任务的通用神经求解器。Triplet-GMPNN [354] 提出了一种基于 GNN 的 GFM，用于解决最短路径、排序和动态规划等问题，其形式化为学习一个映射 $\Phi :(\mathcal{G},t)\mapsto y$，其中 $t$ 代表任务类型，$y$ 是目标解决方案。这种多任务方法强调了任务条件下的图消息传递（Message Passing）的重要性。GCoder [366] 将图推理视为结构化程序生成，直接从输入图 $\mathcal{G}$ 生成代码 $c = \Psi (\mathcal{G})$。通过结合强化学习和编译器反馈，GCoder 提高了程序正确性和执行效率，展示了图数学 GFM 如何连接声明式图表示与可执行过程知识。GraphPatternBench [369] 评估了图 $\mathcal{G}$ 上的模式识别任务，模型通过学习一个二元分类函数 $f:\mathcal{V}\mapsto \{0,1\}$ 来预测结构化图模式（如 cliques, cycles）。

**指令微调的方法**：GraphInstruct [365] 引入了指令微调推理，其中图任务通过指令 $I$ 指定，GFM 推断 $y = \Theta (\mathcal{G}, I)$。GraphWiz [32] 进一步要求 GFM 生成可解释的逐步推理轨迹 $[y_1, y_2, \ldots , y_T]$，将中间解决方案与图的演化状态对齐。MAGMA [370] 使用类似的中间推理轨迹在 $\{\mathcal{G}_t\}$ 上评估经典算法（如 BFS, DFS, Dijkstra）。GraphLLM [367] 通过图到文本序列化将学习到的图嵌入 $\mathbf{z}_i$ 集成到预训练语言模型中，从而处理结构化图表示。GraphToken [368] 则直接学习结构嵌入 $\mathbf{z}_i = \phi (v_i, \mathcal{N}(v_i), \mathbf{A})$，使 GFM 在推理过程中能够原生利用拓扑上下文。

## 7.3.2 Benchmarking and Multi-Agent Collaboration

本章节对当前的Graph Foundation Models (GFMs) 进行了全面的基准测试（benchmarking）和多智能体协作（Multi-Agent Collaboration）的探讨。

**基准测试 (Benchmarking)**

*   **GraphArena [371]**: 该基准测试评估了GFMs在多项式时间（polynomial-time）和NP-complete任务上的表现，重点关注正确率（correctness）和幻觉（hallucination）的评估，其评估指标为 $\ell = \mathrm{Eval}(y_{\mathrm{pred}}, y_{\mathrm{true}})$。
*   **NLGraph [372]**: 该基准测试将评估范围扩展到自然语言查询（natural language queries）在图上的应用，要求模型将文本查询解析为形式化的图查询 $q = \xi (d)$，然后进行求解。
*   **GPT4Graph [33]**: 该基准测试侧重于图中的语义和结构化推理，包括中心性估计（centrality estimation）和图分类（graph classification）。它揭示了预训练的LLMs与结构化、图感知（graph-aware）的GFMs之间存在的差距。

**多智能体协作 (Multi-Agent Collaboration)**

多智能体协作被认为是解决复杂图推理问题的另一有前景的方向。

*   **GraphTeam [362]**: 该方法使用多个专门化的LLM智能体，每个智能体负责解析（parsing）、检索（retrieval）、编码（coding）或推理（reasoning）。每个智能体计算 $\mathbf{z}_i^{(k)} = \phi_k(\mathcal{G})$，并通过智能体间共享中间结果进行迭代优化。
*   **GraphTool-Instruction [355]**: 该方法进一步扩展了多智能体协作，明确地集成了外部工具调用（external tool calls），即模型提取子任务查询 $q$，然后通过工具求解 $y = \mathrm{Tool}(q)$。
*   **GraphAgent-Reasoner [361]**: 该方法采用了类似的智能体分解策略，但将图问题进一步细化为以节点为中心（node-centric）的子任务，每个智能体解决 $y_i = \phi (\mathcal{N}(v_i), \mathbf{x}_i)$，最终通过聚合得到全局预测。

## 7.3.3 Encoding Strategies and Algorithmic Refinement

本章节探讨了用于LLM进行图推理的编码策略和算法改进。

**结构感知编码方法**

*   **Structured JSON encoding** [373] 将节点的邻域序列化为层级JSON树，直接在prompt中保留邻接信息 $\mathcal{N}(v_i)$。
*   **Graph Linearization** [359] 将图 $\mathcal{G}$ 编码为按中心性排序的线性token序列：$\pi = \mathrm{Order}(\mathcal{V}, \mathrm{Centrality})$，以在序列处理中保留关系显著性。
*   **PIE** [364] 将图推理分解为分阶段推理：$y = \Theta_{\mathrm{execute}}(\Theta_{\mathrm{design}}(\Theta_{\mathrm{understand}}(\mathcal{G})))$，每个阶段生成结构化伪代码指导下一阶段。
*   **LogDepth Transformer Hierarchy** [374] 理论证明了对数深度Transformer（深度 $\log N$）能有效捕捉长程图依赖，在某些推理问题上优于标准Transformer和GNNs，为未来GFMs提供了架构指导。

**扩展推理方法**

*   **LLM4Hypergraph** [358] 将图推理扩展到超图 $\mathcal{H} = (\mathcal{V}, \mathcal{E})$，其中超边连接任意节点子集。该模型采用专门的prompting策略（Hyper- BAG, Hyper-COT）将高阶关系编码为：$\mathbf{z}_e = \phi (e,\{v_i:v_i\in e\})$。
*   **NLGIFT** [375] 通过引入结构性变化（如度分布、节点属性和边稀疏性变化）来衡量out-of-distribution泛化能力，要求GFMs动态适应。
*   **Traversal** 仍然是图数学推理的核心。**PathCompare** [357] 通过prompt模型比较候选路径 $c = \mathrm{Compare}(p_1, p_2)$ 来增强遍历推理，其中路径是边序列 $(v_i, v_j) \in \mathcal{E}$。
*   **TREETOP** [376] 将这些技术应用于对话树，其中节点代表对话轮次，边编码回复关系。

## 7.3.4 Future Directions

未来的 Graph Foundation Models (GFMs) 将整合混合检索增强推理，在推理过程中动态获取相关的子图，以改善局部与全局上下文的对齐。受 Thought Propagation [360] 的启发，

## 7.4 Document Network

本章节探讨了语义文档图（semantic document graphs）上的Graph Foundation Models (GFMs)，这些图将文本实体（如文档）作为节点，将它们之间的语义联系（如引用或主题相似性）作为边。节点和边可以包含特征，形成属性矩阵，其结构由邻接矩阵定义。语义文档GFMs旨在联合建模文本语义和图结构，但面临内容-结构对齐和跨领域可扩展性等挑战。尽管大型语言模型（LLMs）可以编码丰富的文本特征 $\mathbf{z}_{i}^{\mathrm{text}}$，而Graph Neural Networks (GNNs)可以传播结构信号 $\mathbf{z}_{i}^{\mathrm{graph}}$，但在具有多样化关系和不断演变内容的异构文档图中对齐这些表示是困难的。

**Prompt-based Integration Approaches** 旨在增强多关系表示学习。METAG [377] 提出了一种多路复用嵌入框架，通过动态注入来自 $\mathcal{T}$ 的关系特定先验token，由语言模型编码器生成节点嵌入 $\mathbf{z}_i$，从而获得对不同边类型 $\mathbf{E}$ 具有适应性的关系感知嵌入，同时保持参数效率并丰富结构语义。G-Prompt [379] 通过引入一种用于TAGs的图适配器增强的prompting策略，扩展了任务特定适应性。它将局部邻域特征 $\mathcal{N}_v$ 融合到prompt中，注入到LLM中，这种混合设计保留了全局语义和局部结构，提高了few-shot和zero-shot节点表示学习。

**Multi-Objective Optimization Approaches** 提供了预训练之外的优化策略。PATTON [380] 联合优化了两个目标：网络上下文掩码语言建模（MLM）和掩码节点预测。前者利用邻域上下文 $\mathcal{N}_v$ 重建 $\mathbf{x}_i$ 中的掩码token，后者基于文本嵌入预测节点身份。这种双任务设置将局部语义恢复与全局图推理对齐，生成同时捕获token级和拓扑信息的节点嵌入 $\mathbf{z}_i$。ConGraT [105] 采用双编码器设计，分别使用GNN和预训练语言模型生成 $\mathbf{z}_{i}^{\mathrm{graph}}$ 和 $\mathbf{z}_{i}^{\mathrm{text}}$。通过最大化互信息，一个跨模态对比损失对齐这些视图，增强了语义文档GFMs的跨领域泛化能力。

**Hybrid Training Approaches** 结合了不同的训练方法。LLM4GraphTopology [378] 通过prompting LLMs评估节点对 $(v_{i},v_{j})$ 之间的语义相似性来优化图拓扑，并根据相似性阈值调整邻接矩阵 $\mathbf{A}$。此过程通过伪标签传播得到加强，LLM生成的标签在更新后的图中扩散以增强分类和聚类。为了支持可扩展学习，GLEM [106] 引入了一个变分EM框架，在基于GNN的结构推理（E-step）和基于LLM的语义编码（M-step）之间交替进行。节点嵌入 $\mathbf{z}_i$ 通过在GNN(A, X)中传播并根据聚合的图信号条件化语言表示来迭代更新。TAPE [89] 通过将LLM生成的解释 $d_{v_i}$ 与节点特征 $\mathbf{x}_i$ 相结合，形成增强的输入 $[\mathbf{x}_i||d_{v_i}]$ 输入GNN，提高了可解释性，从而获得更准确和可解释的节点表示。

表12总结了在异构图上的领域特定GFMs。

**Future Directions** 指出语义文档图基础模型的演进趋势是从静态图编码器到动态自适应的图-文本联合建模流水线。未来的方向包括：1. 层次化prompting，将章节级和文档级上下文整合到 $\mathbf{z}_i$ 中；2. 对比增强，联合对齐节点文本、边描述 $d_{e_{ij}}$ 和全局元数据 $d_g$；3. 多语言预训练，使GFMs能够跨多语言科学语料库进行泛化。这些创新将进一步巩固语义文档GFMs在学术发现、法律文档分析和知识图谱上的大规模检索等领域的中心地位。

## 7.5 Heterogeneous Graph

异构图（Heterogeneous Graph, HG）由节点集 $\mathcal{V}$、边集 $\mathcal{E}$、节点类型集 $\mathcal{T}$ 和边类型集 $\mathcal{R}$ 组成，其中 $|\mathcal{T}| + |\mathcal{R}| > 2$。$\tau(\cdot)$ 和 $\phi(\cdot;\cdot)$ 分别是映射函数，用于识别节点和边的类型。异构图表示学习的核心任务是生成能够准确反映结构和语义信息的节点Embedding。

**基于图模型的方法**：早期研究主要依赖自监督学习。SELAR [382] 提出元学习方法来平衡辅助任务，提升节点表示的主任务性能。CrossHG-Meta [385] 解决了小样本学习（few-shot learning）的挑战，缓解数据稀疏性。PT-HGNN [383] 在节点和语义层面应用对比学习（contrastive learning），捕捉细微的结构信息。HetGPT [384] 引入图提示（graph prompting）策略，使预训练的Graph Neural Networks (GNNs) 适应不同下游任务。

**基于语言模型的方法**：受自然语言处理（NLP）的启发，研究者开始将语言编码器集成到异构图建模中。GaLM [388] 结合邻接矩阵和文本信息，改进了掩码语言模型（masked language modeling）。Higpt [390] 和 HierPromptLM [386] 生成类比语言token的图token，分别通过异构图Transformer (HGT) 和大型语言模型（LLMs）进行处理和微调（fine-tuning）。GHGRL [389] 利用LLMs的推理能力，从文本属性中识别节点类型，生成语义丰富的节点Embedding。HTAG数据集等基准的建立促进了这些方法的研究。

**混合方法**：近期，结合GNNs和LLMs的混合模型在捕捉结构依赖和语义细节方面取得了最先进的性能。Heterformer [381] 集成了基于Transformer的邻居聚合与文本上下文，统一了结构和语义表示。THLM [387] 提出了一个双编码器预训练框架，结合GNNs的结构洞察和LLMs的语义编码，生成多模态节点Embedding。

**未来方向**：未来的研究方向包括探索更高级的多模态集成策略以增强结构-语义一致性，通过显式对齐不同模态的Embedding来提高可解释性，以及开发响应图结构变化的动态自适应模型。此外，计算可扩展性和标准化评估框架的研究对于推进健壮且上下文丰富的Graph Foundation Models (GFMs) 至关重要。

Table 13 总结了不同领域（知识图谱、学术网络、时间图、因果图）的领域特定GFMs，展示了它们在骨干模型（Backbone）、预训练（Pretrain）、适应（Adaptation）、特征对齐（Feature Align）、结构对齐（Structure Align）和任务对齐（Task Align）等方面的特点。

## 7.6 Knowledge Graph

为知识图谱（Knowledge Graph, KG）设计Graph Foundation Models（GFMs）面临独特挑战，主要在于有效推断复杂关系和捕捉三元组（实体-关系-实体）间的隐式关联。与通用图不同，知识图谱模型需要处理组合泛化、逻辑一致性和归纳推理，尤其针对未见实体和关系。当前研究主要集中在两个关键任务：逻辑查询回答（Logical Query Answering）和归纳链接预测（Inductive Link Prediction）。

逻辑查询回答旨在准确响应涉及多跳推理和逻辑运算符（如交集、并集、否定）的结构化查询。模型需在查询中进行组合泛化，动态聚合推理信号，包括针对未见实体和关系。UltraQuery通过将投影和逻辑运算符定义为词汇无关函数，实现零样本（zero-shot）泛化。KG-ICL利用prompt-based reasoning，动态构建由不同message-passing networks编码的查询特定prompt graph，展现出强大的泛化能力。KICGPT将LLMs融入知识图谱补全，利用LLMs的文本理解能力增强模型容量。

归纳链接预测任务侧重于在不依赖已学习实体嵌入的情况下预测缺失关系或链接。该任务可被表述为学习可迁移的关系表示，以推断缺失链接，即使实体在训练期间未出现。ULTRA通过引入基于关系（relation-based）的meta-graph结构，在关系间传播信息，增强了对新知识图谱的可迁移性。Higher-order KGFM通过建模多关系motif来捕捉复杂的依赖关系，显著提升了归纳推理的表达能力。

未来研究方向应侧重于三个方面：首先，扩展至处理二元关系以外的复杂高阶关系交互，如时间关系或n-元关系。其次，将文本、视觉和数值信息等多模态数据整合到知识图谱中，实现全面的多模态推理能力。最后，提高模型的可解释性、可控性和计算可扩展性，尤其是在医疗和金融等对透明度和计算效率要求极高的敏感领域。

## 7.7 Temporal Graph

Temporal graphs, represented as sequences of evolving graph snapshots $\{\mathcal{G}^t = (\mathcal{V}^t,\mathcal{E}^t)\}_{t = 1}^T$, capture dynamic node interactions over time. Each node $v_i \in \mathcal{V}^t$ has a time-dependent feature vector $\mathbf{x}_i^t \in \mathbb{R}^D$, and each edge $e_{ij}^t \in \mathcal{E}^t$ has an evolving feature $\mathbf{e}_{ij}^t \in \mathbb{R}^D$. Modeling these structures requires encoding spatial dependencies within each snapshot $\mathcal{G}^t$ and temporal dependencies across snapshots. Traditional temporal GNNs often use handcrafted diffusion mechanisms, which struggle to generalize to new temporal patterns, especially when nodes and edges have rich, evolving text descriptions.

Recent research has explored the use of large language models (LLMs) for temporal graph reasoning. LLM4DyG [395] benchmarks LLMs on spatial-temporal graph tasks by serializing dynamic graphs into sequences of adjacency matrices $\{\mathbf{A}^t\}_{t = 1}^T$ with evolving node descriptions $\{d_{v_i}^t\}$. The study found that LLM performance degrades with increasing graph size $N$ and temporal density $T$, indicating challenges in maintaining spatial-temporal consistency at scale. To address this, Disentangled Spatial-Temporal Thoughts (DST2) was proposed, which separates spatial reasoning within $\mathcal{G}^t$ from temporal reasoning across snapshots $\mathcal{G}^{t - 1}\rightarrow \mathcal{G}^t$, improving interpretability and prediction accuracy. Another line of work focuses on LLMs modeling graph flow dynamics, where node states $y_i^t$ evolve based on local neighborhoods and historical attributes. FlowGPT [396] benchmarks LLMs on their ability to capture diffusion processes like SIR by serializing dynamic graphs into time-ordered sequences of node states and adjacency matrices, evaluating their capacity to trace propagation patterns and identify influential nodes. These works highlight the potential and challenges of LLM-based reasoning in temporal graphs.

To improve the adaptability of foundation models across different temporal graphs, MiNT [392] introduces a multi-network pretraining strategy. MiNT learns from a collection of networks $\{\mathcal{G}^{(k)}\}_{k = 1}^{K}$, each with its own time horizon, using a single encoder to generate temporally-aware node representations $\mathbf{z}_i^{(k,t)} = \mathrm{GNN}(\mathbf{x}_i^{(k,t)},\mathbf{A}^{(k,t)})$ that generalize to unseen graphs. By leveraging structural and temporal diversity, MiNT surpasses traditional temporal GNNs trained on individual datasets, demonstrating the effectiveness of cross-network pretraining for temporal graph foundation models.

Future research directions for temporal graph reasoning include disentangled spatial-temporal modeling, cross-graph generalization, and flow-aware sequence modeling. Hierarchical temporal abstraction could enrich node representations $\mathbf{z}_i^t$ with multi-scale embeddings for reasoning over both short- and long-term patterns. Adaptive serialization, which adjusts input granularity based on graph density or event frequency, could enhance LLM adaptability. Hybrid architectures combining GNN-based spatial encoding with LLM-based temporal reasoning hold promise for developing expressive and interpretable temporal graph foundation models.

## 7.8 Academic Network

学术网络（Academic Network）主要关注学术引用图 $\mathcal{G} = (\mathcal{V},\mathcal{E})$ 的建模，其中节点 $v_i \in \mathcal{V}$ 代表论文（包含元数据和文本 $\mathbf{x}_i \in \mathbb{R}^D$），边 $e_{ij} \in \mathcal{E}$ 表示引用关系。这类图需要同时考虑语义相关性和引用动态，并平衡局部一致性与全局引用流。与静态检索不同，引用图反映了不断演变的科学讨论，需要能够整合节点内容、引用上下文和时间相关性的嵌入 $\mathbf{z}_i$，实现动态上下文检索，其中引用边补充文本相似性。

LitFM [391] 是该领域的开创性工作，提出了首个明确将学术引用图整合到 LLM 工作流程中的 literature foundation model。该框架使用一个 graph retriever，基于邻接矩阵 $\mathbf{A}$ 中的图邻近性和引用感知嵌入 $\mathbf{z}_i$ 来检索结构上相关的论文，从而缓解了 LLM 常见的引用幻觉和知识不完整等问题。除了简单的图增强检索，LitFM 还利用领域特定的引用图进行 instruction tuning，使其能够泛化到引用预测、相关工作生成和文献综述总结等任务。LitFM 的发展表明，学术图 foundation models 有潜力重塑 LLM 生态系统中科学文献的处理、总结和引用方式。

未来的研究方向可以包括：通过整合时间引用模式和多模态信号（如图形、表格和方程图）来丰富论文嵌入 $\mathbf{z}_i$。此外，将 instruction tuning 扩展到任务组合，可以实现更复杂的学术推理任务。随着引用图规模和复杂性的不断增长，将 LLM 的语义能力与引用图的结构洞察相结合，将是构建 robust academic graph foundation models 的核心。

## 7.9 Causal Graph

因果图（Causal Graph），表示为有向无环图（DAGs）$\mathcal{G} = (\mathcal{V},\mathcal{E})$，编码了因果关系，其中节点$v_i$代表变量，有向边$e_{ij}$捕捉因果联系。节点特征$\mathbf{x}_i\in \mathbb{R}^D$可包含文本或元数据等上下文数据，形成混合语义-因果结构。设计因果Graph Foundation Models (GFMs)面临独特挑战：图稀疏且有方向性，需要推断非对称依赖关系，且常源于嘈杂、文本密集型数据。这要求对文本证据和图结构进行联合推理，使语义对齐和结构一致性变得关键但难以实现。

**语言模型与因果推理**：为解决因果图推理问题，Causal-LLM [393]提出了一种zero-shot方法，从非结构化文本构建“$v_i$是否导致$v_j$？”的成对查询，迭代构建全局因果图$\mathcal{G}$。该方法无需显式监督，利用LLMs的因果推理能力实现可扩展发现，但其在处理间接链（如$v_i\rightarrow v_j\rightarrow v_k$）时存在困难，暴露了prompt设计上的局限性。作为补充，CLEAR [397]提出了一个基准，用于评估LLMs在二十项因果任务上的表现，包括D-separation、backdoor adjustment和effect estimation。模型在$\mathcal{G}$的结构和文本视图上进行测试，结果显示在高阶节点或长路径的图上性能有所下降。CLEAR还表明，措辞和上下文顺序显著影响结果，突显了当前prompt方法在因果推理中的脆弱性。

**未来方向**：因果GFMs的出现为跨不同科学领域的、可扩展的、可解释的因果发现提供了一条有前景的道路。未来的研究可以探索结构化因果prompting，将领域特定的因果先验（如偏好的因果顺序，例如时间先后）纳入查询。另一个有前景的方向是，用从多个嘈杂来源派生的置信度感知嵌入（confidence-aware embeddings）来增强节点特征$\mathbf{x}_i$，使模型能够表达不确定性感知的因果图。此外，将因果图学习整合到多模态GFMs中，其中文本、表格和图共同为因果推断做出贡献，可以显著增强数据丰富的科学领域的因果发现能力。这些创新将进一步巩固因果图基础模型作为自动化科学推理和知识发现的必备工具的地位。

## 8 Theoretical Understandings

本章深入探讨了Graph Neural Networks (GNNs) 和 Graph Foundation Models (GFMs) 的理论基础，旨在提供对这些模型如何学习和泛化的深刻理解。

**核心贡献与主要观点：**

本章的核心贡献在于阐明了GNNs和GFMs在处理图结构数据时的理论机制，重点关注了其表达能力、泛化能力以及与Transformer等模型的联系。主要观点包括：

1.  **GNNs的表达能力与局限性：** 讨论了GNNs（如GCN, GraphSAGE, GAT）通过Message Passing机制聚合邻居信息来学习Node Embedding的理论基础。强调了GNNs的表达能力受到其聚合和更新函数的限制，并与Weisfeiler-Lehman (WL) 算法的判别能力进行了比较，指出了标准GNNs在区分某些图结构（如Graph Isomorphism问题）上的局限性。

2.  **Transformer与GNNs的融合：** 探讨了Transformer架构如何被引入图学习领域，催生了Graph Foundation Models (GFMs)。分析了Transformer的Self-attention机制在图上的应用，以及其如何克服传统GNNs在处理长距离依赖和全局信息时的挑战。讨论了GFMs如何通过大规模Pre-training和Fine-tuning范式，实现强大的Cross-domain Transfer和Few-shot Learning能力。

3.  **GFMs的泛化能力与学习范式：** 详细阐述了GFMs的泛化能力，特别是在In-context Learning和Zero-shot Learning场景下的表现。解释了GFMs如何通过在海量图数据上进行Self-supervised Learning或Contrastive Learning等任务的Pre-training，学习到通用的图表示，从而在下游任务（如Node Classification, Link Prediction, Graph Classification）上实现高效的Fine-tuning或直接应用。

4.  **理论联系与未来方向：** 探讨了GNNs和GFMs在理论上与图论、统计学习等领域的联系。展望了未来研究方向，包括如何进一步提升GNNs和GFMs的表达能力，设计更有效的Pre-training任务，以及在多模态数据（Multi-modal Learning）和复杂图结构（Heterogeneous Graph）上的应用。

**方法与结果：**

本章通过理论分析、模型比较和现有研究的梳理，来支持其论点。

*   **理论分析：** 运用图论和机器学习的理论工具，分析了GNNs的Message Passing机制、聚合函数以及Transformer的Self-attention机制在图上的数学原理。
*   **模型比较：** 对比了不同类型的GNNs（GCN, GraphSAGE, GAT）以及Transformer-based GNNs在表达能力和性能上的差异。
*   **学习范式分析：** 梳理了Self-supervised Learning, Contrastive Learning, Pre-training, Fine-tuning, In-context Learning, Few-shot Learning, Zero-shot Learning等在GFMs中的应用及其理论基础。
*   **结果（理论推导与现有研究成果）：** 理论分析揭示了GNNs在处理某些图结构时的局限性，而Transformer的引入则显著提升了模型处理长距离依赖和全局信息的能力。现有研究成果表明，GFMs通过大规模Pre-training，在多种下游图任务上展现出优越的泛化能力和高效的Few-shot Learning性能。

## 8.1 Emergence and Scaling Law

本章探讨了Foundation models在模型规模、数据量和计算量增加时出现的Emergence现象，即性能显著提升。这种现象可通过neural scaling laws量化描述。尽管LLMs的scaling laws研究已相当成熟，但在graph-based models中复现这些观察结果仍是当前挑战。

## 8.1.1 Well-Structured Graphs

本章节主要探讨了在“Well-Structured Graphs”领域中图学习的scaling laws。这类图结构通常具有天然预定义的结构和内在语义，类似于语言的语法规则，这使得图学习中的scaling properties更容易显现。

在分子和原子系统领域，已有实证证据支持scaling laws的存在。例如，JMP [30]通过在大规模数据集上进行pretraining，提升了在不同化学领域的原子属性预测能力。其pretraining语料库包含了约1.2亿个系统，涵盖了OC20、OC22、ANI-1x和Transition-1x等数据源，这些数据包含平衡和非平衡原子结构，并以能量和力作为主要的supervision signals。研究表明，pretraining模型能够获得可迁移的知识，仅需少量labeled data即可进行downstream adaptation。类似地，DPA-2 [328]在超过1000万个原子结构上进行了大规模multi-task pretraining，促进了知识向未见任务的迁移。这些研究[30, 328, 329]强调了在具有自然结构的图上扩展图模型能够提升性能，这与LLMs和vision models的趋势一致。

为了进一步量化分子图中的emergence，研究人员致力于确定实现scaling laws所需的数据和模型规模的临界阈值[398, 399]。Frey et al. [398]研究了大规模图基化学模型中的neural scaling behaviors，识别出关键的scaling exponents，这些exponents能够捕捉到随着模型容量和数据集规模增加而带来的性能提升。他们的研究发现，对于最大的数据集，scaling exponent为0.17；对于equvairant GNN-based interatomic potential models，scaling exponent为0.26，这表明随着资源的增加，pretraining loss有可衡量的提升。Chen et al. [399]对分子图中的scaling laws进行了广泛分析，考察了data modality、dataset partitioning strategies、pretraining paradigms和model capacity constraints的影响。其主要发现包括：

*   **Modality Dependence**: 不同的分子表示方法表现出不同的scaling behaviors。Graph-based和fingerprint-based encodings具有最高的数据效率，而SMILES-based表示在数据集规模增加时，性能提升效果减弱。
*   **Pretraining Efficacy**: Pretraining在low-data regimes下能提供显著的优势，但在high-data scenarios下，其收益递减，甚至可能出现negative transfer effects。
*   **Dataset Partitioning**: 数据利用的效率取决于partitioning strategies。随机划分（Random splits）效率最高，而基于scaffold（scaffold-based）和不平衡划分（imbalanced splits）会引入distribution shifts，降低学习效果。
*   **Model Capacity Trade-offs**: 数据集规模与最优模型容量之间没有直接的线性关系。在某些情况下，较小的数据集需要更大的模型才能达到最佳性能。

除了分子图，scaling laws也被应用于时序图（temporal graphs）的研究。MiNT [392]分析了动态交易网络（dynamic transaction networks）中的scaling behaviors，使用了84个时序图的集合。通过在64个网络上进行pretraining，并在20个未见网络上评估transferability，MiNT实现了优越的zero-shot performance，超越了在单个数据集上训练的模型。关键的是，他们的研究表明，随着训练网络数量的增加，性能持续提升。

## 8.1.2 General Graphs

本章节探讨了Scaling Laws在通用Graph Foundation Models (GFMs) 上的适用性，指出尽管在分子和原子图等结构化领域已有研究，但在通用GFMs上的探索尚不充分。

研究从监督学习和自监督学习两个角度进行了分析。在监督学习方面，Liu et al. [400] 的研究表明，模型深度对GFMs的Scaling Performance至关重要。他们发现，传统的衡量数据量的方法（如图实例数量）在图数据中效果不佳，因为单个图的大小不规则。因此，他们提出使用节点或边的数量作为定义图数据Scaling Laws的更可靠指标。

从自监督学习角度，Ma et al. [401] 考察了现有图Self-supervised Learning (SSL) 技术是否展现出一致的Neural Scaling Behavior。研究发现，尽管SSL loss随着数据和模型规模的增加而持续改进，但下游任务的性能对架构选择和pretext task设计高度敏感。与在其他领域中更大数据集和模型能带来更好性能的趋势不同，图SSL方法并未表现出清晰的Scaling Trends。因此，他们认为现有的图SSL框架可能尚不适合训练可扩展的GFMs。

此外，一些研究提出了先进的模型[64, 76]并评估了它们的Scaling Behavior，但这些分析通常局限于小型图数据集[64]，或仅关注模型Scaling而非数据Scaling效应[76]。

这些观察引出了一个核心问题：Scaling Laws是否天然存在于图学习中？如果不存在，要实现GFMs的真正Scaling Law需要满足哪些条件？章节最后指出，这些开放性问题将在后续章节（Section 10.1）中进一步探讨并提出未来研究方向。

## 8.2 Transferability

Transferability 指模型从源任务中提取模式并将其知识应用于相关目标任务以提升性能的能力。其核心原理在于预训练模型捕获跨领域的通用、可迁移模式。例如，在文本数据中，可迁移模式表现为 tokens、词语和短语；在图像数据中，则表现为轮廓、颜色、纹理和边缘。理解可迁移模式对于开发 Graph Foundation Models (GFMs) 至关重要。本文将从单任务和跨任务两个角度探讨 GFMs 的 transferability。

## 8.2.1 Single-Task Transferability

本章节探讨了单任务迁移能力（Single-Task Transferability），重点关注Graph Neural Networks (GNNs) 在不同图任务上的泛化表现。

**节点级任务 (Node-Level Tasks)**：
节点级任务旨在理解图中单个节点的属性，这些属性通常受邻近节点属性的影响。节点间的连接遵循两种基本原则：“物以类聚”（homophily）或“异性相吸”（heterophily）。Homophily 指连接节点具有相似特征，而 heterophily 指连接节点具有不同属性。实现节点级任务迁移能力的主要挑战在于设计一个能够同时捕捉 homophily 和 heterophily 模式的统一模型。标准的 GNN 架构在同时处理这两种类型的图时泛化能力较差，性能不佳。为解决此问题，近期方法通过引入额外的文本描述提供上下文信息，或采用可学习的预测聚合机制，以自适应地建模不同的节点交互模式。

**链接级任务 (Link-Level Tasks)**：
链接级任务要求模型捕捉节点对之间的关系结构，通常依赖于基于邻近度的度量来确定连接的可能性。具体而言，如果两个节点共享共同的邻域，它们更有可能被连接。根据邻域重叠程度，邻近度可分为两个级别：局部邻近度（local proximity），节点共享直接邻居；全局邻近度（global proximity），节点展现高阶邻域关系。有效建模这些邻近模式具有挑战性，因为传统的 message-passing GNNs 缺乏捕捉 link isomorphism 的必要表达能力。为增强关系建模能力，诸如 labeling tricks 等高级技术引入了额外的结构知识或 positional embeddings 来丰富链接表示，从而提高表达能力。

**图级任务 (Graph-Level Tasks)**：
图级任务涉及学习捕捉称为 graph motifs 的独特子结构的表示。Graph motifs 是定义图中结构属性的小型、重复模式。图级迁移能力的复杂性源于 motif 分布在不同图中的差异，这要求模型在不同的 motif 集合中识别共享的 motifs，这可能通过 disentangled representation learning 或 invariance learning 来实现。然而，另一个根本性挑战在于 message-passing GNNs 的表达能力限制，它们本质上受限于 1- WL test。即使可以识别共享的 motifs，标准的 GNN 架构也可能无法有效地编码它们。为解决此限制，已提出 expressive GNNs 来增强 motif 编码能力。关于网络分析、模型表达能力和稳定性等更详细的讨论，可参考相关研究。

## 8.2.2 Cross-Task Transferability

本章节探讨了 Graph Foundation Models (GFMs) 在跨任务迁移能力 (Cross-Task Transferability) 方面的理论基础和方法。

**主要论点：** 提升 GFM 的跨任务迁移能力，即模型在不同任务和数据域之间有效复用的能力，是设计更通用和强大的 GFM 的关键。本章从三个主要角度探讨了可迁移模式的定义和实现：Graphon 理论、子结构 (substructures) 和树结构 (tree structures)。

**方法与结果：**

1.  **Graphon 理论：**
*   **理论基础：** Graphon 理论 [409, 410, 288] 被视为识别图中可迁移模式的理论基础。如果两个图由相同的 graphon 生成，它们预计会共享相似的拓扑属性，从而实现高迁移能力。
*   **研究进展：** Ruiz et al. [409] 建立了从同一 graphon 采样的两个图的 embedding 的理论界限。Cao et al. [410] 利用 graphon 理论分析了 pre-training 和 fine-tuning 设置下的迁移能力，通过将预训练图映射到 graphon 空间来确保迁移能力。Sun et al. [288] 基于 graphon 理论提出了一种 fine-tuning 策略。
*   **局限性：** Graphon 理论在现实图上的应用受限于其强烈的潜在假设 [411]。即使假设成立，从大量跨域图中识别共享 graphon 仍然是一个挑战，限制了其在 GFM 设计中的实际应用。

2.  **子结构 (Substructures)：**
*   **定义：** 另一种定义可迁移模式的方法是利用重复出现的子结构，如三角形、星形和 $k$-cliques [293, 36]。这些 motifs 经常出现在不同的图域中，但可能具有不同的语义含义。
*   **研究进展：** 近期研究 [173, 22] 提出了基于子图的学习框架，使用 GNNs 对包含这些结构的采样子图进行编码以进行预测。从理论上讲，这些方法利用图谱分析来量化迁移能力。Levie et al. [412] 通过稳定性分析了迁移能力，认为有效的迁移应最小化对小扰动的敏感性。Levie et al. [411] 证明了当不同图离散化相同的底层空间时，迁移能力是可行的。Zhu et al. [195] 的研究进一步表明，ego-graph 分布的更高相似性与更好的迁移能力相关。

3.  **树结构 (Tree Structures)：**
*   **问题：** 传统的 message-passing GNNs 受限于 1-WL test [413, 408]，难以区分某些 motifs，如星形、共轭环和 $k$-cliques [207, 208, 210]。
*   **解决方案：** 为解决此限制，近期研究探索了基于子树 (subtree) 的表示来定义可迁移模式。Wang et al. [23] 首次提出将子树结构作为基本可迁移模式。Wang et al. [76] 进一步为基于树的模式的稳定性、迁移能力和泛化性提供了理论保证。
*   **优势：** 基于子树的方法的主要优势在于 message-passing GNNs 可以完全捕获子树结构 [413]。
*   **局限性：** 然而，基于树的表示会丢弃某些结构依赖性，可能导致信息丢失。

## 9 Dataset Resources

本章节概述了用于评估Graph learning methods的各种数据集资源。Graph-structured data广泛存在于各个领域，包括电子商务、学术引用网络、知识库、分子科学、时序图、社交网络、脑图和图像等。这些数据集涵盖了不同的规模、特征以及基于graph的任务，为研究提供了多样化的基准。

## 9.1 Tasks and Domains Overview

本章概述了用于评估图学习方法的数据集，这些数据集涵盖了多个领域，并具有独特的结构和任务相关属性。这种多样性允许对各种应用场景下的图学习方法进行全面评估，从而深入了解其通用性和领域特定性能。

## 9.1.1 Tasks

本节概述了图神经网络（GNNs）在三个关键任务中的应用：节点分类（Node Classification）、链接预测（Link Prediction）和图分类（Graph Classification）。

**节点分类（Node Classification）** 旨在预测图中节点的标签，例如根据研究领域对学术论文进行分类。此任务的关键在于有效编码节点自身的特征及其邻域的结构信息。

**链接预测（Link Prediction）** 旨在预测节点对之间是否存在边，或预测演化网络中的未来边。在推荐系统和知识库补全中至关重要。其核心挑战在于有效建模节点相似性，这需要结合结构邻近性和特征兼容性，并利用捕捉高阶连通性模式的嵌入技术。

**图分类（Graph Classification）** 任务为整个图预测标签，广泛应用于分子性质预测和社交网络分析。该任务需要开发有效的图级别表示，以保留局部子结构信息和全局拓扑特征。图分类框架通常采用分层池化（Graph Pooling）机制，逐步粗化图表示，类似于卷积神经网络（CNNs）在计算机视觉中的池化操作。此类方法的有效性取决于其识别图结构中具有区分性子图的能力。

## 9.1.2 Domains

本节概述了图学习研究中常用的数据集领域，包括电子商务、学术界、知识库、分子科学、时间图、社交网络、脑图和图像。

*   **电子商务**数据集通常包含大规模产品图，节点代表产品，边代表用户交互或产品相似性。这些图通常具有复杂的异构结构，具有多种边类型，代表不同的交互模式，如共同购买、共同浏览和语义相似性。
*   **学术界**数据集模拟了引文网络，节点代表论文，边代表引文关系，支持研究领域分类和引文预测任务。这些网络通常表现出时间演化特征，因为引文随时间累积，研究轨迹不断演变，为动态图建模方法提供了机会。
*   **知识库**数据集包含结构化实体及其相互关系，主要用于链接预测任务，以推断缺失的关系或验证实体链接。这些数据集通常包含本体约束和层次结构，为推理任务引入了有利的归纳偏置。
*   **分子科学**数据集由许多代表分子结构的图组成，主要用于属性预测、药物发现和生物化学分析任务。这些图在节点度分布和边形成方面表现出很强的规律性，反映了化学键合原理的物理约束。
*   **时间图**数据集具有随时间演化的动态图，适用于时间链接预测和演化网络中的异常检测等任务。这些数据集捕获了纵向结构转换，能够对图结构的演化模式和时间依赖性进行建模。
*   **社交网络**数据集代表用户之间的交互，有助于社区检测、影响力预测和内容推荐等任务。这些网络通常表现出独特的属性，如高聚类系数、小世界现象和无标度度分布，这些属性会影响算法设计。
*   **脑图**数据集模拟神经连接或血管结构，支持神经系统疾病诊断和解剖学研究等任务。这些图由于其固有的多尺度组织，从微观神经元电路到通过白质束连接的宏观大脑区域，带来了独特的挑战。
*   **图像**数据集代表指纹等视觉结构，支持与视觉模式识别和图像分类相关的任务。这些图通常编码视觉元素之间的空间关系，将网格结构图像数据转换为不规则图结构，以捕获有意义的对象-部分关系。

表14提供了这些基准数据集的概述，按领域、任务类型和结构属性（包括节点数、边数和类别数）进行分类，并指明数据集是否包含文本属性。

## 9.2 Benchmark Descriptions

本章节介绍了近期图学习研究中涌现的多个领域的基准（benchmarks）。Text-space Graph Foundation Models [414] 提供了13个包含文本属性的基准，覆盖了从大规模电商网络（Products: 316K nodes）到小型学术图（Cora）的范围，主要关注 Node Prediction 和 Link Prediction 任务。Knowledge Base Benchmarks [28] 提供了标准知识图谱（WN18RR, FB15K237）的文本增强版本，用于语义 Link Prediction 任务。Temporal Graph Benchmarks [415] 包含如 ICEWS1819 等演化数据集，用于动态结构中的 Temporal Link Prediction。TAGLAS [416] 引入了包含文本属性的分子数据集（Chemblpre, PCBA），拥有数十万个图，用于药物发现中的 Property Prediction。Graph Pattern Recognition [369] 则提供了纯结构性基准（ENZYMES, MUTAG），用于评估在无文本属性情况下的拓扑理解能力。此外，还有专门用于特定任务的基准，涵盖了脑连接（ogbl-vessel [419]）、推荐系统（MovieLens [99]）以及社交网络（Reddit, Flickr [418]）等领域。

## 10 Open Questions

本章节聚焦于 Graph Neural Networks (GNNs) 和 Graph Foundation Models (GFMs) 领域尚未解决的关键问题和未来研究方向。

**主要论点与贡献：**

本章系统性地梳理了当前 GNNs 和 GFMs 研究中存在的挑战，并提出了十个开放性问题，旨在引导未来的研究工作。这些问题涵盖了模型的理论基础、实际应用、效率和可解释性等多个方面。

**方法与结果（未提及具体方法和结果，但指出了研究方向）：**

1.  **理论基础的深化：** 尽管 GNNs 在实践中取得了巨大成功，但其理论边界和表达能力仍需深入研究。例如，理解 GNNs 的表达能力上限，以及它们与传统图算法（如 Graph Isomorphism）的关系。
2.  **模型设计与架构创新：** 如何设计更强大的 GNNs 架构，以处理更复杂的图结构（如 Heterogeneous Graph）和任务（如 Graph Generation）是关键。这包括探索新的 Message Passing 机制、Attention 机制（如 Transformer 在图上的应用）以及 Graph Pooling 方法。
3.  **预训练与迁移学习：** 发展有效的 Pre-training 策略和 Self-supervised Learning 方法，以构建通用的 GFMs，并实现高效的 Fine-tuning、In-context Learning、Few-shot Learning 和 Zero-shot Learning，是实现跨领域迁移（Cross-domain Transfer）和 Domain Adaptation 的重要途径。
4.  **效率与可扩展性：** 随着图规模的不断增大，如何提高 GNNs 的训练和推理效率，以及处理大规模图（如 Knowledge Graph）的能力，是亟待解决的问题。
5.  **可解释性与鲁棒性：** 提升 GNNs 的可解释性，理解其决策过程，以及增强模型在噪声或对抗性攻击下的鲁棒性，是其在关键领域应用的前提。
6.  **多模态与跨模态学习：** 如何将 GNNs 与其他模态的数据（如文本、图像）相结合，实现 Multi-modal Learning，并进行跨模态的图表示学习，是拓展 GNNs 应用边界的重要方向。
7.  **特定任务的优化：** 针对 Graph Classification、Node Classification、Link Prediction、Graph Anomaly Detection 等具体任务，如何设计更优化的 GNNs 模型和训练方法。
8.  **数据质量与偏差：** 如何处理不完整、有噪声或存在偏差的图数据，并确保 GNNs 的公平性和无偏性。
9.  **评估指标与基准：** 建立更全面、更具区分度的评估指标和标准化的基准数据集，以更准确地衡量 GNNs 和 GFMs 的性能。
10. **新兴应用领域探索：** 探索 GNNs 和 GFMs 在更多新兴领域的应用潜力，如科学发现、药物研发、社交网络分析等。

总而言之，本章为 GNNs 和 GFMs 的未来研究指明了方向，强调了在理论、模型、效率、可解释性以及应用落地等方面仍有大量工作需要探索。

## 10.1 How to Enhance Scalability?

本章节探讨了如何提升Graph Foundation Models (GFMs) 的可扩展性，指出当前GFMs尚未展现出类似LLMs的scaling law。为实现真正的图scaling law，文章强调了三个关键方面：

1.  **更好的Graph Backbones**: 现有的Graph Neural Networks (GNNs) 存在过平滑（over-smoothing）、过压缩（oversquashing）、长距离依赖建模不足以及捕捉图子结构能力有限等内在局限性。这些问题不仅阻碍了模型的可扩展性，也影响了多GPU训练效率。Transformer架构在NLP和CV领域的成功为图学习提供了灵感。虽然基础的graph transformer将图序列化，但其二次复杂度限制了其在大型图上的应用。近期研究提出将子结构作为graph tokens，通过子结构模式序列来表示节点、边和整个图，这显著降低了编码复杂度并提高了可扩展性，是GFMs未来发展的一个有前景的方向。

2.  **更好的Pretraining Objectives**: 成功的预训练目标对于从大规模数据中提取可迁移知识至关重要。在NLP和视觉领域，生成式预训练（如next-token prediction）是主流，能有效捕捉有意义的语义。相比之下，大多数图的self-supervised learning方法依赖于对比式预训练（contrastive pretraining），其效果不如生成式预训练。尽管有研究探索了图的重构目标，但主要集中在节点和边等低级语义，未能像NLP和CV那样重构词语或图像块以保留高级语义。因此，现有的生成式图方法未能超越对比学习。为了实现GFMs的有意义预训练，关键在于转向重构高级语义结构。

3.  **更好的Learning Instances**: 在LLMs中，由词语组成的句子是基本学习实例；在VLMs中，由视觉块组成的图像是主要学习实例。从这些实例进行训练使模型能够获得可迁移和可扩展的知识。然而，在GFMs中，尚不清楚应该扩展节点、边还是整个图作为学习实例。此外，不同的图任务依赖于不同的学习实例：节点级任务关注节点，而图级任务侧重于图。为了在任务间实现统一，已提出了子图和树等统一学习实例。然而，一个关键问题是：扩展这些统一学习实例是否能促进跨任务知识的获取？

## 10.2 How to Mitigating Data Scarcity?

为应对图学习中的数据稀疏性问题，本文提出了三个关键方向。

首先，**Automated Graph Collection Pipelines** 借鉴了LLMs和LVMs的成功经验，即通过自动化数据收集技术来获取大规模数据集。与文本和图像数据不同，图数据的构建通常需要人工的语义和领域特定关系的梳理。然而，近期LLMs的进展表明，自动化数据集构建技术可以有效地从学术库、生物医学数据库和在线知识图谱等多样化来源系统地提取结构化关系，从而解决图数据的获取难题。

其次，**Synthetic Data Generation** 强调了数据增强和合成技术在缓解数据稀疏性方面的作用。在LLMs领域，知识蒸馏和数据合成是提升模型泛化能力的重要策略。类似地，在图学习中，图扩散模型等生成模型的发展使得通过合成数据来增强图结构成为可能。例如，扩散模型已被用于提升图数据集的结构多样性，而LLMs则可用于生成文本属性图的合成文本属性。这些技术为扩充现有数据集提供了新途径，但开发能够保持真实世界图结构和语义完整性的鲁棒图生成技术仍是未来的重要研究方向。

最后，**Acquiring High-Quality Graph Data** 指出，高质量数据的重要性可能超越数据量本身。正如LLM预训练和指令微调研究所示，在少量高质量数据上训练的模型，其性能可能与在海量低质量数据上训练的模型相当甚至更优。将此原则应用于图学习，精心策划的高质量图数据集可能比简单地扩大数据集规模带来更大的效益。然而，图数据集常存在不完整性，且评估其质量具有挑战性。尽管已有多种数据评估技术用于评估机器学习中的数据贡献，但为图数据定义质量指标仍是一个开放性问题。图数据的质量与所选的backbone architecture和pre-training strategy密切相关，因此需要进一步研究有效的图数据评估方法。

## 10.3 How to Better Evaluate GFMs?

评估 Graph Foundation Models (GFMs) 的有效性至关重要。然而，由于 GFMs 在不同领域的广泛应用，使用小型基准进行的传统评估方法往往不足。本节讨论了推进评估框架所需的两个方面。

**开发高级基准 (Developing Advanced Benchmarks)**：评估 foundation models 的能力需要精心设计的基准。然而，现有的图基准存在几个局限性：(1) 它们常常缺乏变革性的真实世界应用；(2) 它们的构建方式未能有意义地反映实际用例；(3) 图社区的基准测试文化因其不一致性和可复现性问题而受到批评。鉴于这些挑战，构建高质量、大规模且与现实场景一致的基准对于有效评估 GFMs 至关重要。此类基准应包含多样化的图结构、多种学习任务和不同级别的监督，以全面评估模型能力。

**超越准确性：评估泛化性、鲁棒性和可信度 (Beyond Accuracy: Evaluating Generalization, Robustness, and Trustworthiness)**：准确性等传统评估指标不足以捕捉 GFMs 的全部潜力。除了在基准数据集上的原始性能外，评估其跨不同领域的泛化能力、对抗性和噪声数据的鲁棒性以及在高风险应用中的可信度至关重要。开发明确测试这些维度的新型评估指标和基准，对于更全面地理解 GFM 能力是必要的。未来的工作应探索衡量领域适应性 (domain adaptation)、分布偏移下的可靠性、可解释性以及图决策中的伦理考量的方法。

## 10.4 How to Better Utilize GFMs?

本章节探讨了如何更好地利用Graph Foundation Models (GFMs)，重点关注提升其适应性、应用性和多模态集成能力。

**先进的适应方法**：尽管图提示学习（graph prompt learning）等技术已引入GFMs的适应性方法，但仍需对提示（prompt）进行微调（fine-tuning）。借鉴Large Visual Models (LVMs) 的范式，将GFMs处理图数据的方式扩展至自回归（autoregressive）模式，有望实现真正的zero-shot和in-context learning，无需显式的任务特定适应。

**杀手级应用**：当前许多GFMs的应用，如社交网络分析、药物属性预测和推荐系统，仍可被传统图学习模型有效解决。因此，关键在于发掘GFMs的独特价值，即在传统方法力有未逮的复杂场景中应用。潜在方向包括：芯片设计中的电路布局优化、组合优化（combinatorial optimization）中NP-hard图问题的可扩展解决方案，以及关系数据库（relational databases）的查询优化和知识提取。

**多模态知识集成**：图数据天然包含多模态结构化知识，例如分子数据可表示为图、序列、文本或图像；社交网络则涉及用户名、职位、图像、活动日志和历史交互等多种数据类型。如何设计模型有效集成和处理这些多模态图信息仍是挑战。一个关键问题是应设计统一模型处理所有模态，还是采用模态特定模型以发挥各自优势。

**人机协同（Human-in-the-Loop）**：在药物发现、推荐和科学工作流等领域，GFMs的泛化能力需要结合人类反馈和领域特定监督。集成人机协同机制能够实现模型纠错、提示优化和交互式适应，从而更好地与专家知识和实际需求对齐。随着GFMs的广泛部署，人类的参与对于提升可解释性、控制性和实际可靠性至关重要。

## 10.5 Advanced Theoretical Understandings

本章节深入探讨了Graph Foundation Models (GFMs) 的高级理论理解，旨在提升其有效性、可靠性和泛化能力。主要研究了三个开放性理论挑战：

**1. Transferability (可迁移性)**

图数据编码的复杂且常为手动定义的关联性，使得其可迁移知识不如文本或图像直观。尽管有实证研究表明，GFMs 可以在看似不相关的领域之间实现知识迁移，但缺乏理论和直观解释。例如，社交网络和分子图在结构分布上存在显著差异，难以概念化其共享的可迁移模式。近期研究通过分析子树分布来刻画不同领域图之间的可迁移性，但将图仅视为树的组合会丢失结构信息。因此，需要一个全面的理论框架来定义和量化图领域内外的可迁移知识，以实现更有效的 GFMs 迁移学习策略。

**2. Pattern Conflict Issue (模式冲突问题)**

在 GFMs 中识别跨任务可迁移模式更具挑战性，因为存在模式冲突。当相同的结构模式在不同领域具有不同的语义含义时，就会出现此问题，导致学习到的表示可能不一致。例如，在预训练阶段，模型可能在社交网络和分子网络等跨领域数据集上进行训练。如果模型学会识别和利用三角形结构，在社交网络中，三角形通常代表稳定性（“朋友的朋友是我的朋友”）；而在分子图中，三角形模式可能因特定的化学约束而指示不稳定性。这种根本性的解释差异会严重降低模型性能。现有方法要么未能解决，要么仅部分缓解了模式冲突问题。开发有效解决此挑战的策略对于构建真正可泛化的 GFMs 至关重要。

**3. Robustness and Trustworthiness (鲁棒性和可信度)**

真实世界的图数据表现出各种不良特性，包括长尾分布、不完整性、类别不平衡、有限的标记数据和结构变化。为了开发鲁棒且可信的 GFMs，理解模型如何应对这些挑战至关重要。一个有前景的方向是分析 GFMs 在结构分布变化下的稳定性，包括研究其对对抗性扰动的韧性、处理缺失或噪声数据以及确保决策的公平性。为鲁棒性建立理论保证对于在医疗保健、金融和网络安全等高风险应用中部署 GFMs 至关重要。

**4. Generalization (泛化能力)**

在机器学习中，平衡模型拟合能力和泛化能力是基础。过度强调拟合能力可能导致在特定数据集上过拟合，从而损害在未见图上的性能；而过度关注泛化能力可能会损害在同分布任务上的预测准确性。理解 GFMs 的泛化能力对于优化这种权衡至关重要。一项开创性工作利用基于子树的学习 token 建立了 GFMs 的泛化界限。然而，需要更广泛的泛化分析，超越树结构，以获得更具应用性的见解。

## 11 Conclusion

本章对Graph Foundation Models (GFMs)这一新兴的图机器学习范式进行了全面系统的回顾。GFMs旨在将Foundation Models在自然语言处理和计算机视觉领域的成功经验迁移至图结构数据。文章首先阐述了GFMs的发展背景，并指出了图数据固有的挑战，包括异构性、非欧几里得结构以及跨域迁移能力。为统一现有研究，作者提出了一个通用的GFMs框架，将其分解为骨干网络（backbone architectures）、预训练策略（pretraining strategies）和适配机制（adaptation mechanisms）等模块化组件。

GFMs被划分为三大类：通用GFMs（universal GFMs），旨在实现跨任务和跨领域的广泛泛化；任务特定GFMs（task-specific GFMs），侧重于在特定目标（如link prediction或node classification）上取得高性能；以及领域特定GFMs（domain-specific GFMs），专注于特定应用领域（如分子图、Knowledge Graph和计算图）。文章对每类GFMs的核心设计原则、代表性方法进行了分析和比较，突出了它们的优势和局限性。此外，研究还深入探讨了GFMs的理论基础，包括其表达能力（expressiveness）、迁移能力（transferability）和泛化保证（generalization guarantees）。

尽管取得了显著进展，GFMs领域仍面临诸多挑战，包括：GFMs向大规模图的可扩展性（scalability）；多模态信号（multimodal signals）的整合；原则性的评估协议（principled evaluation protocols）的开发；以及解释其迁移能力和泛化的理论基础的构建。

展望未来，GFMs有望成为通用图智能（general-purpose graph intelligence）的基础设施。未来的研究应致力于构建更具可扩展性、可解释性和适应性的架构，扩展跨真实世界领域的图预训练语料库（graph pretraining corpora），并推进解释其行为的理论框架。通过融合结构归纳偏置（structural inductive biases），GFMs在科学发现、工业系统和结构化数据决策方面展现出巨大的潜力。

---

## 统计信息

- **总处理块数**: 120
- **原始总token数**: 39,605
- **总结总token数**: 8,061
- **整体压缩比**: 20.35%
- **平均压缩比**: 360.21%
- **处理章节数**: 120


*此文档由MinerU内容总结器V2自动生成，基于Langchain Markdown分割技术。*