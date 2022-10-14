import logging

from servier_drugs_journals_pipeline.src.helpers.utils import read_csv
from servier_drugs_journals_pipeline.src.models.durg import Drug


class DrugReader:
    """
    class to read and clean clinical trials and pubmed files
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.raw_data = read_csv(file_path)

    def clean_data(self):
        """
        check if each drug have non-null values in it's two columns
        :return: cleaned data in list of dict format
        """
        idx = 0
        drugs = []
        for observation in self.raw_data:
            idx += 1
            if observation["atccode"] and observation["drug"]:
                drugs.append(Drug(observation["atccode"], observation["drug"]))
            else:
                logging.warning(f"corrupted line {idx} in file : {self.file_path}")
        return drugs
