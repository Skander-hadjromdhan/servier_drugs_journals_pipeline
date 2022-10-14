class JournalItem:
    """
    class to store data of the journal articles (pubmed / clinical_trials)
    """

    def __init__(self, obj_id, date, title, journal):
        self.id = obj_id
        self.date = date
        self.title = title
        self.journal = journal

    def get_id(self):
        return self.id

    def get_date(self):
        return self.date

    def get_title(self):
        return self.title

    def get_journal(self):
        return self.journal
