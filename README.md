# AI Lab (CS4944) - Lab Work

Solutions for AI Lab weeks 1 to 6. Each week has its own folder with code and a report.

## How to run

Python 3.10 or newer. No extra setup for weeks 1 to 5. Week 6 needs extra packages, see week6/README.md.

```bash
python week1/lab1_compare.py
python week1/lab1_rules.py
python week2/lab2_percepts.py
python week2/lab2_check.py
python week3/lab3_bfs_dfs.py
python week3/lab3_depth_search.py
python week3/lab3_ucs.py
python week4/lab4_astar.py
python week4/lab4_astar_audit.py
python week5/lab5_minimax.py
```

## Weeks

### Week 1 - Introduction to AI and Paradigms
- lab1_compare.py: symbolic rule vs probability threshold on four scholarship cases
- lab1_rules.py: rule checker with two extra conditions and four test cases
- Lab1_Report.docx: timeline, rule tests, disagreement table, conversational test comparison

### Week 2 - Intelligent Agents and PEAS
- lab2_percepts.py: reflex classroom agent on six percepts
- lab2_model.py: stateful agent that remembers its last mode
- lab2_check.py: full mode transition trace
- Lab2_Report.docx: PEAS specs, environment classification, reflex vs stateful comparison

### Week 3 - Uninformed Search
- lab3_bfs_dfs.py: BFS and DFS on the A to G graph
- lab3_depth_search.py: DLS and IDDFS at limits 1 to 4
- lab3_ucs.py: weighted graph, UCS lowest cost path, BFS route comparison
- Lab3_Report.docx: hand traces, DLS/IDDFS results, weighted graph and costs

### Week 4 - Informed Search, Heuristics and A*
- lab4_astar.py: A* and UCS on the campus graph with expansion counts
- lab4_astar_audit.py: heuristic audit and the h(C) = 10 overestimate experiment
- Lab4_Report.docx: hand g/h/f values, A* vs UCS table, overestimate experiment

### Week 5 - Adversarial Search, Minimax and Alpha-Beta
- lab5_minimax.py: minimax and alpha-beta with leaf counters, original and reordered trees
- Lab5_Report.docx: hand trace, leaf counts, pruning comparison

### Week 6 - NLP: Tokenization, Embeddings and Text Chunking
- task1_tokens.py: whitespace vs word-like tokens on six inputs
- faq_chatbot.py and task1_chatbot_check.py: FAQ chatbot and behaviour checks
- task2_chunks.py: 40-word windows (overlap 0 and 10) and sentence-aware chunks
- task3_retrieval.py: retrieval evaluation, Hit@3 and MRR@3, retrieval_log.csv
- document_chatbot.py: evidence chatbot using the picked setup
- corpus.json and queries.json: synthetic documents and labelled queries
- Lab6_Report.docx: token tables, chunk comparison, retrieval results
