from _domain_base import DomainBase


class Interaction(DomainBase):
    def __init__(self):
        path = ""  # Where are the interaction?
        super(Interaction, self).__init__(path)

    # Is there a need to overload the getter?
    # Are there specific interactions for specific cases?
    # Where is this decided?

