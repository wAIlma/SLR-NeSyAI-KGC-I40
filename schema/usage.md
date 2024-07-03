# Usage

To use this ontology, follow these steps:

1. Download or clone this repository.
2. Import `ontology.ttl` or `ontology.rdf` into your ontology editor or application.
3. Start using the defined classes and properties in your ontology modeling or data.

## Example Data

The main directory contains a sample data file (`example.ttl`) that demonstrating  how to represent a person with a name.

``` Turtle
@prefix bibo: <http://purl.org/ontology/bibo/> .
@prefix cito: <http://purl.org/spar/cito/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix swrc: <http://swrc.ontoware.org/ontology#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://github.com/wAIlma/SLR-NeSyAI-KGC/main/schema/paper/Chen2023> a bibo:Document ;
    rdfs:label "{Reinforcement learning-based distant supervision relation extraction for fault diagnosis knowledge graph construction under industry 4.0}" ;
    orkg:hasResearchField <https://github.com/wAIlma/SLR-NeSyAI-KGC/main/schema/keyword/Distant_supervision_relation_extraction>,
        <https://github.com/wAIlma/SLR-NeSyAI-KGC/main/schema/keyword/Fault_diagnosis>,
        <https://github.com/wAIlma/SLR-NeSyAI-KGC/main/schema/keyword/Knowledge_graph>,
        <https://github.com/wAIlma/SLR-NeSyAI-KGC/main/schema/keyword/Reinforcement_Learning> ;
    dcterms:issued "2023" ;
    dcterms:title "{Reinforcement learning-based distant supervision relation extraction for fault diagnosis knowledge graph construction under industry 4.0}" ;
    bibo:abstract "Fault diagnosis is the key concern in the operation and maintenance of industrial assets. A fault diagnosis knowledge graph (KG) can provide decision support to the engineers to efficiently conduct maintenance tasks. However, as a type of domain KG, it would be time-consuming to manually label the corpus collected from the multi-source including the maintenance log, handbook and article. Meanwhile, the existence of the noisy sentence in the multi-source corpus jeopardises the performance of relation extraction modelling. In order to address this issue, this paper proposes a distant supervision relation extraction (DSRE)-based approach to construct a fault diagnosis KG. In this approach, the ontology of the fault diagnosis KG is firstly designed. Subsequently, a DSRE algorithm named relation-aware-based sentence-level attention enhanced piecewise convolutional neural network with reinforcement learning strategy (PCNN-ATTRA-RL) is proposed. The algorithm can effectively lower the impact of noisy sentences and accurately label the relation of different entities when the labelled data is insufficient. In this algorithm, PCNN-ATTRA is designed as the DSRE classifier to effectively extract the relation between entity pairs. RL is conducted to remove the noisy sentence so as to further improve the performance. An experimental study based on the multi-source corpus collected from the real world reveals that the proposed approach shows merits in comparison with the state-of-the-art algorithms. Meanwhile, a fault diagnosis KG, which can greatly support the decision-making of the engineers in the fault diagnosis, is established via the proposed approach." ;
    bibo:doi "10.1016/j.aei.2023.101900" ;
    bibo:url "https://linkinghub.elsevier.com/retrieve/pii/S1474034623000289" ;
    swrc:author <https://github.com/wAIlma/SLR-NeSyAI-KGC/main/schema/author/Chen_Chong>,
        <https://github.com/wAIlma/SLR-NeSyAI-KGC/main/schema/author/Cheng_Lianglun>,
        <https://github.com/wAIlma/SLR-NeSyAI-KGC/main/schema/author/Deng_Jianfeng>,
        <https://github.com/wAIlma/SLR-NeSyAI-KGC/main/schema/author/Liu_Ying>,
        <https://github.com/wAIlma/SLR-NeSyAI-KGC/main/schema/author/Wang_Tao>,
        <https://github.com/wAIlma/SLR-NeSyAI-KGC/main/schema/author/Xie_Haojia>,
        <https://github.com/wAIlma/SLR-NeSyAI-KGC/main/schema/author/Zheng_Yu> ;
    swrc:publishedIn <https://github.com/wAIlma/SLR-NeSyAI-KGC/main/schema/journal/Advanced_Engineering_Informatics> .

```