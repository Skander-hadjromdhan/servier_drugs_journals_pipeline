import logging

from servier_drugs_journals_pipeline.src.helpers.utils import read_json


logging.basicConfig(level=logging.INFO)


def adhoc_check(json_path):
    """
    check which journal has most appearances
    :param json_path: path of the graph json file
    :return: void
    """
    graph = read_json(json_path)
    my_counter = {}
    best_journal = None
    best_score = 0
    for drug in graph:
        journals = drug["journals"]
        for journal in journals:
            if journal["referenced_in"] not in my_counter.keys():
                my_counter[journal["referenced_in"]] = 1
                if best_score < 1:
                    best_journal = journal["referenced_in"]
                    best_score = 1
            else:
                my_counter[journal["referenced_in"]] += 1
                if best_score < my_counter[journal["referenced_in"]]:
                    best_journal = journal["referenced_in"]
                    best_score = my_counter[journal["referenced_in"]]
    logging.info(f"adhoc check results = best_journal {best_journal} with a score of {best_score}")
