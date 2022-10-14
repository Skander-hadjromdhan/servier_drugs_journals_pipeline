import logging
import re
import uuid

from servier_drugs_journals_pipeline.src.helpers.utils import read_csv, read_json, date_parser
from servier_drugs_journals_pipeline.src.models.journal_item import JournalItem


class JournalArticleReader:
    """
    class to read and clean clinical trials and pubmed files
    """

    def __init__(self, file_path):
        self.file_path = file_path
        if file_path.endswith(".csv"):
            self.raw_data = read_csv(file_path)
        else:
            self.raw_data = read_json(file_path)

    def clean_data(self):
        """
        clean the data after reading it. in order to do so the following actions will be made :
        1- check number of columns should be 4 for each observation
        2- parse the date
        3- remove non ascii characters from title and journal, strip them and transform them to uppercase
        4- generate a new id in order to store the data
        :raises KeyError if the schema is not respected
        :raises ValueError if date format is not known
        :raises NotImplementedError if file contains more than 4 columns
        :return: list of objects of type JournalArticles
        """
        clean_data = []
        idx = 0
        for observation in self.raw_data:
            idx += 1
            rows = list(observation.keys())
            if len(rows) > 4:
                raise NotImplementedError(f"Journal article file {self.file_path} contains more than 4 columns")
            col_title = "scientific_title" if "scientific_title" in rows else "title"
            if observation["date"] and observation[col_title]:
                date = date_parser(observation["date"])
                title = re.sub(r"\\[a-z0-9]{3}", "", observation[col_title]).upper().strip()
                journal = re.sub(r"\\[a-z0-9]{3}", "", observation["journal"]).upper().strip()
                obj_id = uuid.uuid4()
                clean_data.append(JournalItem(obj_id, date, title, journal))
            else:
                logging.warning(f"corrupted line {idx} in file : {self.file_path}")
        return clean_data
