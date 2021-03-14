# The role of this class is that to implement common
# methods to load information
class DomainBase:
    def __init__(self, path: str):
        # 1. Load the file determined by "path".
        # 2. Store the lines/sections, as decided, in
        self._items = []  # or {}, as needed

    # Maybe a default value could indicate random selection?
    # Will there be specific sentences to be selected in specific cases?
    # Or maybe ranges of sentences falling in certain ranges?
    # Maybe (all kinds of) sentences are ordered by "intensity"
    # (e.g. positiveness to contrast negativity, or matching reinforcement)
    # so the index becomes significant
    def get_item(self, idx=-1) -> str:
        pass

    def get_number(self) -> int:
        return len(self._items)
