class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_hash = {}
            t_hash = {}
            for l1,l2 in zip(s,t):
                if l1 in s_hash:
                    s_hash[l1] += 1
                else:
                    s_hash[l1] = 1
                if l2 in t_hash:
                    t_hash[l2] += 1
                else:
                    t_hash[l2] = 1
        else:
            return False
        if s_hash == t_hash:
            return True
        else:
            return False