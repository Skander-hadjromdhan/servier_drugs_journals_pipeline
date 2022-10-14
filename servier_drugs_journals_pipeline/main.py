import sys
import logging

from servier_drugs_journals_pipeline.src.pipeline.pipeline import pipeline
from servier_drugs_journals_pipeline.src.helpers.adhoc_check import adhoc_check

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    drugs_file_path = sys.argv[1]
    clinical_trials_file_path = sys.argv[2]
    pubmed_file_path_1 = sys.argv[3]
    pubmed_file_path_2 = sys.argv[4]
    result_path = sys.argv[5]

    pipeline(drugs_file_path, clinical_trials_file_path, pubmed_file_path_1, pubmed_file_path_2, result_path)
    adhoc_check(result_path)
