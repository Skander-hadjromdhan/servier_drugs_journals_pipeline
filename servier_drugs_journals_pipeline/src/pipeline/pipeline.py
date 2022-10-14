import logging

from servier_drugs_journals_pipeline.src.readers.drug_reader import DrugReader
from servier_drugs_journals_pipeline.src.readers.journal_article_reader import JournalArticleReader
from servier_drugs_journals_pipeline.src.helpers.utils import write_graph


logging.basicConfig(level=logging.INFO)


def update_drug_graph(graph_element, journal_article_list, type_article):
    """
    insert the observation depending on the type of article in the graph element
    :param graph_element: graph element that represents one drug
    :param journal_article_list: list of all pubmed or clinical trials objects
    :param type_article: type of the article in journal_article_list
    :return: updated graph element
    """
    journals = []
    for article in journal_article_list:
        article_dict = article.__dict__

        if graph_element["drug_name"] in article_dict["title"]:
            graph_element[type_article].append(
                {"referenced_in": article_dict["title"],
                 "reference_date": article_dict["date"].strftime("%d/%m/%Y")
                 }
            )
            if (article_dict["journal"]+article_dict["date"].strftime("%d/%m/%Y")) not in journals:
                graph_element["journals"].append(
                    {"referenced_in": article_dict["journal"],
                     "reference_date": article_dict["date"].strftime("%d/%m/%Y")
                     }
                )
                journals.append(article_dict["journal"]+article_dict["date"].strftime("%d/%m/%Y"))
    return graph_element


def generate_graph(drug_file_path, clinical_trials_path, pubmed_1_path, pubmed_2_path):
    """
    graph generation function
    :param drug_file_path: drug file path
    :param clinical_trials_path: clinical trials' path
    :param pubmed_1_path: pubmed_1 file path
    :param pubmed_2_path: pubmed_2 file path
    :return: graph of drugs connected with their appearances in journals, pubmed and clinical trials
    """
    logging.info("reading data files & cleaning data")
    drugs = DrugReader(drug_file_path).clean_data()
    clinical_trials = JournalArticleReader(clinical_trials_path).clean_data()
    pubmed_1 = JournalArticleReader(pubmed_1_path).clean_data()
    pubmed_2 = JournalArticleReader(pubmed_2_path).clean_data()
    pubmed = pubmed_1 + pubmed_2
    logging.info("Generating graph")
    output_graph = []
    for drug in drugs:
        drug_name = drug.get_name()
        drug_atc_code = drug.get_atc_code()
        drug_graph_element = {
            "drug_name": drug_name,
            "drug_atc_code": drug_atc_code,
            "journals": [],
            "clinical_trials": [],
            "pubmed": []
        }
        drug_graph_element = update_drug_graph(drug_graph_element, pubmed, "pubmed")
        drug_graph_element = update_drug_graph(drug_graph_element, clinical_trials, "clinical_trials")
        output_graph.append(drug_graph_element)
    return output_graph


def pipeline(drug_file_path, clinical_trials_path, pubmed_1_path, pubmed_2_path, out_file_path):
    """
    full pipeline
    :param drug_file_path: drug file path
    :param clinical_trials_path: clinical trials' path
    :param pubmed_1_path: pubmed_1 file path
    :param pubmed_2_path: pubmed_2 file path
    :param out_file_path: output file path
    :return: void
    """
    graph = generate_graph(drug_file_path, clinical_trials_path, pubmed_1_path, pubmed_2_path)
    write_graph(graph, out_file_path)
    logging.info(f"graph generated and available at the following location : {out_file_path}")
