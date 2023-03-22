from pyroaring import BitMap

from collections import defaultdict


class PassportNumberBitMap(BitMap):
    def contains(self, other: int) -> bool:
        return other in self

    def contains_collection(self, collection: list[int]) -> dict[int:bool]:
        return {value: self.contains(value) for value in collection}


passport_memory_db = defaultdict(PassportNumberBitMap)
