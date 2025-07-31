import bisect
import sys
from typing import Any, Dict, List, Optional, Protocol, Tuple


def assert_or_print(actual_res: Any, exp_res: Any, lino: Optional[int] = None):
    if actual_res != exp_res:
        print(f"actual result: {actual_res}, expected result: {exp_res} in line number {lino if lino else 'unknown'}")


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


class DatabaseInterfaceL3(Protocol):

    def set_with_ttl(self, timestamp: int, key: str, field: str, value: str, ttl: int):
        ...

class DatabaseInterfaceL4(Protocol):

    def get_at_timestamp(self, timestamp: int, key: str, field: str, at_timestamp: int):
        ...


class DatabaseImpl(DatabaseInterfaceL1, DatabaseInterfaceL2, DatabaseInterfaceL3, DatabaseInterfaceL4):

    # FIXME: the field or value cannot include `sep`.
    sep = ":"

    max_timestamp = sys.maxsize

    # L1
    def __init__(self):
        # value, expiry: `max_timestamp` to be never expiring
        self.records: Dict[str, Dict[str, Tuple[str, int]]] = {}

        # timestamp, optional of value
        self.record_logs: Dict[str, Dict[str, List[Tuple[int, Optional[str]]]]] = {}

    def _snapshot(self, timestamp: int, key: str, field: str, value: Optional[str], expiry: Optional[int] = None):
        if key not in self.record_logs:
            self.record_logs[key] = {}
        rlog = self.record_logs[key]
        if field not in rlog:
            rlog[field] = []
        flog = rlog[field]
        bisect.insort_left(flog, (timestamp, value), key=lambda x: x[0])
        if expiry:
            bisect.insort_left(flog, (expiry, None), key=lambda x: x[0])

    def get(self, timestamp: int, key: str, field: str) -> Optional[str]:
        if key not in self.records:
            return None
        record = self.records[key]
        if field not in record:
            return None
        val, expiry = record[field]
        if expiry == self.max_timestamp or expiry >= timestamp:
            return val
        return None

    def set(self, timestamp: int, key: str, field: str, value: str):
        if key not in self.records:
            self.records[key] = {}
        record = self.records[key]
        record[field] = (value, self.max_timestamp)
        self._snapshot(timestamp, key, field, value)
    
    def compare_and_set(self, timestamp: int, key: str, field: str, expected_value: str, new_value: str) -> bool:
        if key not in self.records:
            return False
        record = self.records[key]
        if field not in record or record[field][1] <= timestamp or record[field][0] != expected_value:
            return False
        record[field] = (new_value, record[field][1])
        self._snapshot(timestamp, key, field, new_value)
        return True
    
    def compare_and_delete(self, timestamp: int, key: str, field: str, expected_value: str) -> bool:
        if key not in self.records:
            return False
        record = self.records[key]
        if field not in record or record[field][1] <= timestamp or record[field][0] != expected_value:
            return False
        del record[field]
        self._snapshot(timestamp, key, field, None)
        return True

    def delete(self, timestamp: int, key: str, field: str):
        if key not in self.records:
            return
        record = self.records[key]
        if field not in record:
            return
        del record[field]
        self._snapshot(timestamp, key, field, None)
    
    # L2
    def scan(self, timestamp: int, key: str) -> List[str]:
        if key not in self.records:
            return []
        record: Dict[str, str] = self.records[key]
        ret: List[str] = []
        for fld, (val, expiry) in record.items():
            if timestamp >= expiry:
                continue
            ret.append(f"{fld}{self.sep}{val}")
        ret.sort(key=lambda rec: rec.rsplit(":", maxsplit=1)[0])
        return ret
        

    def scan_with_prefix(self, timestamp: int, key: str, prefix: str) -> List[str]:
        if key not in self.records:
            return []
        record: Dict[str, str] = self.records[key]
        ret: List[str] = []
        for fld, (val, expiry) in record.items():
            if timestamp >= expiry:
                continue
            if fld.startswith(prefix):
                ret.append(f"{fld}{self.sep}{val}")
        ret.sort(key=lambda rec: rec.rsplit(":", maxsplit=1)[0])
        return ret
    
    # L3
    def set_with_ttl(self, timestamp, key, field, value, ttl):
        if ttl <= 0:
            return
        expiry = timestamp + ttl
        if key not in self.records:
            self.records[key] = {}
        record = self.records[key]
        record[field] = (value, expiry)
        self._snapshot(timestamp, key, field, value, expiry)
    
    # L4
    def get_at_timestamp(self, timestamp: int, key: str, field: str, at_timestamp: int) -> Optional[str]:
        if key not in self.record_logs:
            return
        rlog = self.record_logs[key]
        if field not in rlog:
            return
        flog = rlog[field]
        if not flog:
            return None
        idx = bisect.bisect_right(flog, at_timestamp, key=lambda x: x[0]) - 1
        if idx < 0:
            return None
        return flog[idx][1]


def test_level_1():
    db = DatabaseImpl()
    assert_or_print(db.get(0, "a", "f"), None, 138)
    db.set(1, "a", "f", "v")
    assert_or_print(db.get(2, "a", "f"), "v", 140)
    assert_or_print(db.compare_and_set(3, "a", "f", "q", "u"), False, 141)
    assert_or_print(db.compare_and_set(4, "a", "f", "v", "u"), True, 142)
    assert_or_print(db.get(5, "a", "f"), "u", 143)
    assert_or_print(db.compare_and_delete(6, "a", "f", "v"), False, 144)
    assert_or_print(db.compare_and_delete(7, "a", "f", "u"), True, 145)
    assert_or_print(db.get(8, "a", "f"), None, 146)
    db.set(9, "a", "f", "v")
    assert_or_print(db.get(10, "a", "f"), "v", 147)
    db.delete(11, "a", "f")
    assert_or_print(db.get(12, "a", "f"), None, 148)


def test_level_2():
    db = DatabaseImpl()
    db.set(0, "a", "f1.1", "v.v")
    db.set(1, "a", "f2", "u")
    db.set(2, "a", "f1", "v")
    db.set(3, "a", "f3", "w")
    db.set(4, "a", "f1.1.1", "v.v.v")
    assert_or_print(db.scan(5, "a"), [
        "f1:v", "f1.1:v.v", "f1.1.1:v.v.v", "f2:u", "f3:w",
        ], 162)
    assert_or_print(db.scan_with_prefix(6, "a", "f1"), [
        "f1:v", "f1.1:v.v", "f1.1.1:v.v.v",
        ], 165)


def test_level_3():
    db = DatabaseImpl()
    assert_or_print(db.get(0, "a", "f"), None)
    db.set_with_ttl(1, "a", "f", "v", 3)
    assert_or_print(db.get(2, "a", "f"), "v")
    assert_or_print(db.compare_and_set(3, "a", "f", "v", "u"), True)
    assert_or_print(db.compare_and_set(4, "a", "f", "u", "v"), False)
    assert_or_print(db.get(5, "a", "f"), None)
    assert_or_print(db.compare_and_delete(6, "a", "f", "v"), False)
    assert_or_print(db.compare_and_delete(7, "a", "f", "u"), False)
    assert_or_print(db.get(8, "a", "f"), None)
    db.set_with_ttl(9, "a", "f.1.1", "v", 4)
    db.set_with_ttl(10, "a", "f.2.3", "u", 4)
    assert_or_print(db.scan(11, "a"), [
        "f.1.1:v", "f.2.3:u"
        ])
    assert_or_print(db.scan_with_prefix(12, "a", "f.1"), [
        "f.1.1:v"
        ])
    assert_or_print(db.scan(13, "a"), [
        "f.2.3:u"
        ])
    assert_or_print(db.scan_with_prefix(14, "a", "f.2"), [])


def test_level_4():
    db = DatabaseImpl()
    db.set(1, 'a', 'f', 'v')
    assert_or_print(db.get_at_timestamp(2, 'a', 'f', 0), None, 234)
    assert_or_print(db.get_at_timestamp(3, 'a', 'f', 1), "v", 235)
    assert_or_print(db.get_at_timestamp(4, 'a', 'f', 2), "v", 236)
    db.set_with_ttl(5, 'a', 'g', 'u', 1)
    assert_or_print(db.get_at_timestamp(6, 'a', 'g', 4), None, 237)
    assert_or_print(db.get_at_timestamp(7, 'a', 'g', 5), "u", 238)
    assert_or_print(db.get_at_timestamp(8, 'a', 'g', 6), None, 239)


def main():
    test_level_1()
    test_level_2()
    test_level_3()
    test_level_4()


if __name__ == "__main__":
    main()
