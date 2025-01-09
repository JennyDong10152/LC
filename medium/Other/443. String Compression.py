class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        n = len(chars)
        idx = 0
        while i < n:
            length = 1
            while (i + length < n and chars[i + length] == chars[i]):
                length += 1

            chars[idx] = chars[i]
            idx += 1
            if length > 1:
                length_str = str(length)
                chars[idx:idx+len(length_str)] = list(length_str)
                idx += len(length_str)
            i += length
        return idx