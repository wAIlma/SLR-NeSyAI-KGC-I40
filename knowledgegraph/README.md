# Populated Knowledge Graph for Systematic Literature Review

## Overview
This directory contains the populated knowledge graph (KG) derived from the systematic literature review (SLR) on Knowledge Graph Construction using Neuro-Symbolic AI approaches. The knowledge graph is constructed using the combined BIBO, CITO, SWRC, and ORKG ontologies to represent detailed bibliographic, citation, research community, and structured research information.

## Loading the Knowledge Graph 

To load the knowledge graph into a Python environment, you can use the rdflib library, which supports the TTL format.

```python
from rdflib import Graph

 # Path to the knowledge graph file
kg_file = 'knowledge_graph.ttl' 

# Path to the Query file
with open('queries/query1.sparql') as query_file:
        sparql_query = query_file.read()

graph = Graph()
graph.parse(kg_file, format="ttl")

#Query the knowledge graph using SPARQL.
results = graph.query(sparql_query)

# Print the results
for row in results:
    print(row)
```

## Predefined Queries

Some specific and prepared queries are in the [Query folder](queries/), they cam be executed using the prepared [script](query_sparql.py)

* **[Query 1](queries/query1.sparql):** List All Research Papers and Their Titles
* **[Query 2](queries/query2.sparql):** Get Papers Published in a Specific Journal
* **[Query 3](queries/query3.sparql):** Get Citation Counts for Each Paper
* **[Query 4](queries/query4.sparql):** List All Research Fields and Associated Papers
* **[Query 5](queries/query5.sparql):**  Get the DOI and URL of Each Paper

