from _domain_base import DomainBase


class Examples(DomainBase):
    def __init__(self):
        path = ""  # Where are the examples?
        super(Examples, self).__init__(path)
