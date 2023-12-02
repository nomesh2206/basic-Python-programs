class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        pow_of_2 = set([2**i for i in range(0, 22)])
        MOD = 10**9 + 7
        
        cnt = {}
        for d in deliciousness:
            if d in cnt:
                cnt[d] += 1
            else:
                cnt[d] = 1
                
        res = 0
        visit = set()
        for key, val in cnt.items():
            for n in pow_of_2:
                if n - key in cnt:
                    if n - key == key:
                        res += val * (val - 1) // 2
                    else:
                        if n - key not in visit:
                            res += val * cnt[n - key]
            visit.add(key)
        return res % MOD
