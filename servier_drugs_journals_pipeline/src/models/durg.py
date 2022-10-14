class Drug:
    """
    class to store data of the journal articles (pubmed / clinical_trials)
    """

    def __init__(self, atc_code, name):
        self.atc_code = atc_code
        self.name = name

    def get_atc_code(self):
        return self.atc_code

    def get_name(self):
        return self.name
