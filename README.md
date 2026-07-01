# Robust_Agentic_Query_Corrector

A lightweight multi-agent framework for automatically correcting search queries using Large Language Models (LLMs).

The system first detects whether a query needs correction and then applies the appropriate specialized correction agent. The process repeats until no further corrections are required.

## Features

- Multi-agent query correction pipeline
- Automatic error detection
- Supports:
  - Misspelling correction
  - Word ordering correction
  - Query naturality improvement
  - Synonym replacement
  - Query paraphrasing
- Iterative correction until convergence

## Repository Structure

```
agentic_query_corrector/
│── agents/
│   ├── detector.py
│   ├── misspelling.py
│   ├── naturality.py
│   ├── ordering.py
│   ├── paraphrase.py
│   ├── synonym.py
│   └── prompts.py
│
├── data/
├── output/
├── llm.py
├── orchestrator.py
└── main.py
```

## Input Format

The input must be a TSV file containing two columns:

| qid | query |
|-----|-------|
| 1 | weather in london |
| 2 | best resturant near me |

Place the file inside:

```
agentic_query_corrector/data/
```

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd Robust_Agentic_Query_Corrector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running

Execute:

```bash
python -m agentic_query_corrector.main \
    --input queries.tsv \
    --output corrected_queries.tsv
```

where:

- `queries.tsv` is located in `agentic_query_corrector/data/`
- The output will be written to `agentic_query_corrector/output/`

## Output Format

The generated TSV contains:

| qid | query | corrected_query |
|-----|-------|-----------------|
| 1 | weather in london | weather in london |
| 2 | best resturant near me | best restaurant near me |

## Pipeline

```
Input Query
      │
      ▼
Detector Agent
      │
      ▼
Select Correction Agent
      │
      ▼
Apply Correction
      │
      ▼
Needs More Correction?
      │
 ┌────┴────┐
 │   Yes   │
 └────┬────┘
      │
      ▼
Detector Agent
      │
      ▼
 Final Corrected Query
```

## License

This project is released under the MIT License.
