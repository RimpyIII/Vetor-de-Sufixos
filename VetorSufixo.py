class VS:
    def __init__(self, T):
        T = T.lower()
        T += "$"
        vs = list(range(0,len(T)))
        self.vs = self.mergeSort(T, vs)
        self.lcp = self.LCP(T,self.vs)

    def mergeSort(self, T, V):
        if len(V) > 1:
            meio = len(V)//2
            v1 = self.mergeSort(T, V[0: meio])
            v2 = self.mergeSort(T, V[meio: len(V)])
            return self.merge(T, v1, v2)
        return V

    def merge(self, T, v1, v2):
        p1 = 0
        p2 = 0
        merged = []
        while p1 < len(v1) and p2 < len(v2):
            if self.compara(T, v1[p1], v2[p2]) == -1:
                merged.append(v1[p1])
                p1 += 1
            elif self.compara(T, v1[p1], v2[p2]) == 1:
                merged.append(v2[p2])
                p2 += 1
            else:
                merged.append(v1[p1])
                p1 += 1
        while p1 < len(v1):
            merged.append(v1[p1])
            p1 += 1
        while p2 < len(v2):
            merged.append(v2[p2])
            p2 += 1
        return merged
    
    def compara(self, T, pos1, pos2):
        n = 0
        while True:
            if T[pos1 + n] > T[pos2 + n]:
                return 1
            elif T[pos1 + n] < T[pos2 + n]:
                return -1
            else:
                n += 1

    def LCP(self, T, V):
        lcp = []
        for i in range(0, len(V) - 1):
            n = 0
            while T[V[i] + n] == T[V[i + 1] + n]:
                n += 1
            lcp.append(n)
        return lcp

    def Print(self):
        print(self.vs)
        print(self.lcp)

vs = VS("AAACCTTTGCGACC")
vs.Print()
