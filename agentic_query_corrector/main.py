import pandas as pd
from agentic_query_corrector.orchestrator import QueryCorrectionOrchestrator
import argparse
from pathlib import Path

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", default="data/query.tsv")
    parser.add_argument("--output", default="output/corrected_query.tsv")

    args = parser.parse_args()


    query_file_loc=Path(f'agentic_query_corrector/data/{args.input}')

    df = pd.read_csv(query_file_loc, sep="\t")

    orchestrator = QueryCorrectionOrchestrator()

    corrected = []

    for _, row in df.iterrows():

        final_query = orchestrator.correct(row["query"])

        corrected.append({
            "qid": row["qid"],
            "query": row["query"],
            "corrected_query": final_query
        })

    out = pd.DataFrame(corrected)
    
    out_query_file_loc=Path(f'agentic_query_corrector/output/{args.output}')
    out.to_csv(out_query_file_loc, sep="\t", index=False)

if __name__ == "__main__":
    main()


'''
python -m agentic_query_corrector.main --input "queries.tsv" --output "corrected_queries.tsv"

'''