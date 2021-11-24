from abc import ABC, abstractmethod


class FilenameGenerator(ABC):

    @abstractmethod
    def generate_filename(obj: object) -> str:
        pass
