
# Multi-Document CAG with Agentic Workflows

## Overview
This project implements a **Multi-Document Context-Augmented Generation (CAG)**
system using **agentic AI workflows**. Documents are stored in **Google Cloud
Storage**, and a dedicated AI agent is dynamically instantiated for each
document. A final synthesis agent aggregates responses from all document agents
to generate an accurate, traceable answer with **page-level citations and page
image references**.

## Problem Statement
Traditional RAG systems face challenges when:
- Multiple documents are uploaded simultaneously
- Cross-document reasoning is required
- Responses need traceability (page numbers, sources)
- Users need visual verification of extracted content

## Solution
An **agent-based CAG architecture** where:
- Each uploaded document is handled by an independent **Document Agent**
- Documents are fetched dynamically from **Cloud Storage**
- Agents process documents in parallel
- A **Final Synthesis Agent** consolidates all agent responses
- The final answer includes **page number citations and page images** for
  transparency and trust

## Architecture
### Agent Roles
- **Controller Agent**
  - Orchestrates the workflow
  - Routes Cloud Storage documents to individual agents

- **Document Agents (One per document)**
  - Load documents from Cloud Storage
  - Perform context extraction and embedding
  - Return structured insights with page references

- **Final Synthesis Agent**
  - Aggregates responses from all document agents
  - Applies CAG to enrich the final response
  - Generates answers with page-level citations

## Context-Augmented Generation (CAG)
Unlike traditional RAG, this system augments generation with:
- Structured contextual summaries from each agent
- Page-level metadata
- Multi-agent consensus before final response generation

## Tech Stack
- Python
- Vertex AI (Gemini)
- Agentic AI Framework (Agno / Custom Agents)
- Google Cloud Storage (Document Storage)
- FastAPI
- Docker
- Google Cloud Run

## Key Features
- Multi-document upload support
- One agent per document (parallel execution)
- Cloud Storage–based document management
- CAG & RAG hybrid pipeline
- Page number citations in responses
- Page image preview for reference transparency
- Scalable, production-ready deployment

## Response Transparency
Each response includes:
- Referenced document names
- Page numbers
- Corresponding page images
This ensures users can verify exactly where the information originated.

## Use Cases
- Enterprise knowledge assistants
- Policy and compliance analysis
- Legal and technical document review
- Research and multi-report analysis

## Status
Architecture finalized  
Backend agent orchestration in progress  
Deployment-ready design
