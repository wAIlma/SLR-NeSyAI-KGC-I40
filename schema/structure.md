# Ontology Documentation

This document provides an overview and detailed description of the ontology used in this knowledge graph. 

The ontology integrates several well-known vocabularies and custom properties to represent research papers, their metadata, and related entities.

## Namespaces

- `bibo`: <http://purl.org/ontology/bibo/>
- `cito`: <http://purl.org/spar/cito/>
- `dcterms`: <http://purl.org/dc/terms/>
- `foaf`: <http://xmlns.com/foaf/0.1/>
- `orkg`: <http://orkg.org/core>
- `owl`: <http://www.w3.org/2002/07/owl#>
- `rdfs`: <http://www.w3.org/2000/01/rdf-schema#>
- `swrc`: <http://swrc.ontoware.org/ontology#>
- `xsd`: <http://www.w3.org/2001/XMLSchema#>

## Classes

### orkg:ResearchField
- **Label**: Research Field
- **Comment**: A field of study related to research.
- **Description**: This class represents various research fields to which research papers may belong.

### swrc:Conference
- **Label**: Conference
- **Comment**: A conference event.
- **Description**: This class represents conferences where research papers are presented.

### swrc:Journal
- **Label**: Journal
- **Comment**: A periodical containing scholarly articles.
- **Description**: This class represents journals in which research papers are published.

### foaf:Organization
- **Label**: Organization
- **Comment**: An organization such as a company or institution.
- **Description**: This class represents organizations, which may include universities, companies, research institutes, etc.

### orkg:Paper
- **Label**: Research Paper
- **Comment**: A research paper.
- **Description**: This class represents individual research papers.

### swrc:Publication
- **Label**: Publication
- **Comment**: A scientific publication.
- **Equivalent Class**: `orkg:Paper`, `bibo:Document`
- **Description**: This class represents publications, which are equivalent to research papers and documents.

### foaf:Person
- **Label**: Person
- **Comment**: A person.
- **Description**: This class represents individuals, typically researchers, authors, or members of organizations.

### bibo:Document
- **Label**: Document
- **Comment**: Any written or printed work.
- **Description**: This class represents any type of document, including research papers.

## Properties

### Object Properties

#### orkg:hasResearchField
- **Label**: hasResearchField
- **Comment**: The research field of the paper.
- **Domain**: `orkg:Paper`
- **Range**: `orkg:ResearchField`
- **Description**: This property links a research paper to its corresponding research field.

#### cito:cites
- **Label**: cites
- **Comment**: Indicates that one document cites another document.
- **Domain**: `bibo:Document`
- **Range**: `bibo:Document`
- **Description**: This property denotes that one document cites another document, establishing a citation relationship between documents.

#### swrc:author
- **Label**: author
- **Comment**: Author of the publication.
- **Domain**: `swrc:Publication`
- **Range**: `foaf:Person`
- **Description**: This property links a publication to its author(s).

#### swrc:presentedAt
- **Label**: presented at
- **Comment**: The conference at which the publication was presented.
- **Domain**: `swrc:Publication`
- **Range**: `swrc:Conference`
- **Description**: This property links a publication to the conference where it was presented.

#### swrc:publishedIn
- **Label**: published in
- **Comment**: The journal in which the publication is published.
- **Domain**: `swrc:Publication`
- **Range**: `swrc:Journal`
- **Description**: This property links a publication to the journal in which it was published.

#### foaf:member
- **Label**: member
- **Comment**: A member of an organization.
- **Domain**: `foaf:Organization`
- **Range**: `foaf:Person`
- **Description**: This property links an organization to its members.

### Datatype Properties

#### dcterms:issued
- **Label**: issued
- **Comment**: Date of formal issuance (e.g., publication) of the resource.
- **Domain**: `bibo:Document`
- **Range**: `xsd:date`
- **Description**: This property specifies the publication date of a document.

#### dcterms:title
- **Label**: title
- **Comment**: A name given to the resource.
- **Domain**: `bibo:Document`
- **Range**: `rdfs:Literal`
- **Description**: This property specifies the title of a document.

#### bibo:abstract
- **Label**: abstract
- **Comment**: Abstract of a document.
- **Domain**: `bibo:Document`
- **Range**: `rdfs:Literal`
- **Description**: This property provides the abstract or summary of a document.

#### bibo:doi
- **Label**: DOI
- **Comment**: Digital Object Identifier for a document.
- **Domain**: `bibo:Document`
- **Range**: `rdfs:Literal`
- **Description**: This property specifies the Digital Object Identifier (DOI) of a document.

#### bibo:url
- **Label**: URL
- **Comment**: URL for a document.
- **Domain**: `bibo:Document`
- **Range**: `xsd:anyURI`
- **Description**: This property specifies the URL where the document can be accessed.

#### foaf:name
- **Label**: name
- **Comment**: A name for some thing.
- **Domain**: `foaf:Person`
- **Range**: `rdfs:Literal`
- **Description**: This property specifies the name of a person.

