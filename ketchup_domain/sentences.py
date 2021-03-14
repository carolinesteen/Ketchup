from _domain_base import DomainBase


class Sentences(DomainBase):
    def __init__(self):
        path = ""  # Where are the sentences?
        super(Sentences, self).__init__(path)
