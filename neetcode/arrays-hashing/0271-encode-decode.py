from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return 'nil'
        return chr(257).join(strs)

    def decode(self, s: str) -> List[str]:
        if s == 'nil':
            return []
        return s.split(chr(257))
