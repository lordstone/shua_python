from typing import Any, List, Optional, Protocol


def assert_or_print(actual_res: Any, exp_res: Any):
    if actual_res != exp_res:
        print(f"actual result: {actual_res}, expected result: {exp_res}")


class DatabaseInterfaceL1(Protocol):

    def get(self, timestamp: int, key: str, field: str) -> str:
        ...

    def set(self, timestamp: int, key: str, field: str, value: str):
        ...
    
    def compare_and_set(self, timestamp: int, key: str, field: str, expected_value: str, new_value: str) -> bool:
        ...
    
    def compare_and_delete(self, timestamp: int, key: str, field: str,expected_value: str) -> bool:
        ...

    def delete(self, timestamp: int, key: str, field: str):
        ...


class DatabaseInterfaceL2(Protocol):

    def scan(self, timestamp: int, key: str) -> List[str]:
        ...

    def scan_with_prefix(self, timestamp: int, key: str, prefix: str) -> List[str]:
        ...


class DatabaseImpl(DatabaseInterfaceL1, DatabaseInterfaceL2):

    # FIXME: the field or value cannot include `sep`.
    sep = ":"

    # L1
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
    
    # L2
    def scan(self, timestamp: int, key: str) -> List[str]:
        if key not in self.records:
            return []
        record: Dict[str, str] = self.records[key]
        ret: List[str] = []
        for fld, val in record.items():
            ret.append(f"{fld}{self.sep}{val}")
        ret.sort(key=lambda rec: rec.rsplit(":", maxsplit=1)[0])
        return ret
        

    def scan_with_prefix(self, timestamp: int, key: str, prefix: str) -> List[str]:
        if key not in self.records:
            return []
        record: Dict[str, str] = self.records[key]
        ret: List[str] = []
        for fld, val in record.items():
            if fld.startswith(prefix):
                ret.append(f"{fld}{self.sep}{val}")
        ret.sort(key=lambda rec: rec.rsplit(":", maxsplit=1)[0])
        return ret


def test_level_1():
    db = DatabaseImpl()
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
    db.delete(11, "a", "f")
    assert_or_print(db.get(12, "a", "f"), None)


def test_level_2():
    db = DatabaseImpl()
    db.set(0, "a", "f1.1", "v.v")
    db.set(1, "a", "f2", "u")
    db.set(2, "a", "f1", "v")
    db.set(3, "a", "f3", "w")
    db.set(4, "a", "f1.1.1", "v.v.v")
    assert_or_print(db.scan(5, "a"), [
        "f1:v", "f1.1:v.v", "f1.1.1:v.v.v", "f2:u", "f3:w",
        ])
    assert_or_print(db.scan_with_prefix(6, "a", "f1"), [
        "f1:v", "f1.1:v.v", "f1.1.1:v.v.v",
        ])


def main():
    test_level_1()
    test_level_2()


if __name__ == "__main__":
    main()
