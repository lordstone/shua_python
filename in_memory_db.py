from abc import ABC, abstractmethod
from typing import Any, Optional


def assert_or_print(actual_res: Any, exp_res: Any):
    if actual_res != exp_res:
        print(f"actual result: {actual_res}, expected result: {exp_res}")


class DatabaseInterface(ABC):

    @abstractmethod
    def get(self, timestamp: int, key: str, field: str) -> str:
        pass

    @abstractmethod
    def set(self, timestamp: int, key: str, field: str, value: str):
        pass
    
    @abstractmethod
    def compare_and_set(self, timestamp: int, key: str, field: str, expected_value: str, new_value: str) -> bool:
        pass
    
    @abstractmethod
    def compare_and_delete(self, timestamp: int, key: str, field: str,expected_value: str) -> bool:
        pass

    @abstractmethod
    def delete(self, timestamp: int, key: str, field: str):
        pass


class DatabaseImpl(DatabaseInterface):

    def __init__(self):
        self.records: dict[dict] = {}

    def get(self, timestamp: int, key: str, field: str) -> Optional[str]:
        if key not in self.records:
            return None
        record = self.records[key]
        if field not in record:
            return None
        return record[field]

    def set(self, timestamp: int, key: str, field: str, value: str):
        if key not in self.records:
            self.records[key] = {}
        record = self.records[key]
        record[field] = value
    
    def compare_and_set(self, timestamp: int, key: str, field: str, expected_value: str, new_value: str) -> bool:
        if key not in self.records:
            return False
        record = self.records[key]
        if field not in record or record[field] != expected_value:
            return False
        record[field] = new_value
        return True
    
    def compare_and_delete(self, timestamp: int, key: str, field: str, expected_value: str) -> bool:
        if key not in self.records:
            return False
        record = self.records[key]
        if field not in record or record[field] != expected_value:
            return False
        del record[field]
        return True

    def delete(self, timestamp: int, key: str, field: str):
        if key not in self.records:
            return
        record = self.records[key]
        if field not in record:
            return
        del record[field]


def test_level_1():
    db: DatabaseInterface = DatabaseImpl()
    assert_or_print(db.get(0, "a", "f"), None)
    db.set(1, "a", "f", "v")
    assert_or_print(db.get(2, "a", "f"), "v")
    assert_or_print(db.compare_and_set(3, "a", "f", "q", "u"), False)
    assert_or_print(db.compare_and_set(4, "a", "f", "v", "u"), True)
    assert_or_print(db.get(5, "a", "f"), "u")
    assert_or_print(db.compare_and_delete(6, "a", "f", "v"), False)
    assert_or_print(db.compare_and_delete(7, "a", "f", "u"), True)
    assert_or_print(db.get(8, "a", "f"), None)
    db.set(9, "a", "f", "v")
    assert_or_print(db.get(10, "a", "f"), "v")
    db.delete(9, "a", "f")
    assert_or_print(db.get(8, "a", "f"), None)


def main():
    test_level_1()


if __name__ == "__main__":
    main()
