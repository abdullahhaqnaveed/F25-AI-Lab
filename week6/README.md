# Week 6 - NLP: Tokenization, Embeddings and Text Chunking

## Setup

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

The first run with the embedding backend downloads the sentence model. If the model cannot
be downloaded, the scripts still run with TF-IDF and say so in their output.

## Files

corpus.json and queries.json are already made by create_dataset.py. Do not run it again
unless you delete them first, because it refuses to overwrite them.

Run in this order:

```bash
python task1_tokens.py
python task1_chatbot_check.py
python task2_chunks.py
python task2_semantic_check.py
python task3_retrieval.py
python document_chatbot.py
```

task3_retrieval.py writes retrieval_log.csv with the top 3 results for every query and
prints Hit@3 and MRR@3 for development and test queries. document_chatbot.py uses the
setup picked on development results (overlap 10 windows with sentence embeddings when the
model is available, TF-IDF otherwise, see Lab6_Report.docx)
and asks you to pick a result before it shows the passage.

The five scenario scripts and the guided scripts can be run on their own:

```bash
python scenario1_handbook.py
python scenario2_support.py
python scenario3_docs.py
python scenario4_workplace.py
python scenario5_equipment.py
python guided_tokens.py
python guided_chunks.py
python guided_metrics.py
python guided_embeddings.py
python guided_limits.py
```
