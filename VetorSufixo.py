class VS:
    def __init__(self, T):
        T = T.lower()
        T += "$"
        vs = list(range(0,len(T)))
        self.T = T
        self.vs = self.mergeSort(T, vs)
        self.lcp = self.LCP(T,self.vs)
        self.lcp = [None] + self.lcp
        self.llcp = [None] * len(T)
        self.rlcp = [None] * len(T)
        self.LRLCP(0, len(T) - 1,None)

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
        print(self.llcp)
        print(self.rlcp)
    
    def LRLCP(self, i, j, side):
        if i == j - 1:
            value = self.lcp[j]
        else:
            M = (i + j)//2
            self.LRLCP(i, M, 0)
            self.LRLCP(M, j, 1)
            value = self.min(self.llcp[M], self.rlcp[M])
        if side == 0:
            self.llcp[j] = value
        if side == 1:
            self.rlcp[i] = value
    
    def min(self, v1, v2):
        if v1 > v2:
            return v2
        else:
            return v1

    def searchP(self, P):
        r = 0
        s = self.vs[-1]
        while r < len(P) and P[r] == self.T[s + r]:
            r += 1
        if r < len(P) and P[r] > self.T[s + r]:
            return len(self.T)
        L = 0
        R = len(self.vs) - 1
        l = 0
        while L < R - 1:
            M = (L + R)// 2
            if l == r:
                p = l
                while p < len(P) and P[p] == self.T[self.vs[M] + p]:
                    p += 1
                if p == len(P) or P[p] < self.T[self.vs[M] + p]:
                    R = M
                    r = p
                else:
                    L = M
                    l = p
            elif l > r:
                if l < self.llcp[M]:
                    L = M
                elif l > self.llcp[M]:
                    R = M
                    r = self.llcp[M]
                else:
                    p = l
                    while p < len(P) and P[p] == self.T[self.vs[M] + p]:
                        p += 1
                    if p == len(P) or P[p] < self.T[self.vs[M] + p]:
                        R = M
                        r = p
                    else:
                        L = M
                        l = p
            else:
                if r < self.rlcp[M]:
                    R = M
                elif r > self.rlcp[M]:
                    L = M
                    l = self.rlcp[M]
                else:
                    p = r
                    while p < len(P) and P[p] == self.T[self.vs[M] + p]:
                        p += 1
                    if p == len(P) or P[p] < self.T[self.vs[M] + p]:
                        R = M
                        r = p
                    else:
                        L = M
                        l = p
        return L
    
    def searchS(self, P):
        r = 0
        s = self.vs[-1]
        while r < len(P) and P[r] == self.T[s + r]:
            r += 1
        if r < len(P) and P[r] > self.T[s + r]:
            return len(self.T)
        L = 0
        R = len(self.vs) - 1
        l = 0
        while L < R - 1:
            M = (L + R)// 2
            if l == r:
                p = l
                while p < len(P) and P[p] == self.T[self.vs[M] + p]:
                    p += 1
                if p == len(P) or P[p] > self.T[self.vs[M] + p]:
                    L = M
                    l = p
                else:
                    R = M
                    r = p
            elif l > r:
                if l < self.llcp[M]:
                    L = M
                elif l > self.llcp[M]:
                    R = M
                    r = self.llcp[M]
                else:
                    p = l
                    while p < len(P) and P[p] == self.T[self.vs[M] + p]:
                        p += 1
                    if p == len(P) or P[p] > self.T[self.vs[M] + p]:
                        L = M
                        l = p
                    else:
                        R = M
                        r = p
            else:
                if r < self.rlcp[M]:
                    R = M
                elif r > self.rlcp[M]:
                    L = M
                    l = self.rlcp[M]
                else:
                    p = r
                    while p < len(P) and P[p] == self.T[self.vs[M] + p]:
                        p += 1
                    if p == len(P) or P[p] > self.T[self.vs[M] + p]:
                        L = M
                        l = p
                    else:
                        R = M
                        r = p
        return R
    
    def Search(self, P):
        p = self.searchP(P)
        if p == len(self.T):
            return False
        else:
            r = 0
            p += 1
            while r < len(P) and self.T[self.vs[p] + r] == P[r]:
                r += 1
            if r == len(P):
                return True
            else:
                return False
    
    def NOccurences(self, P):
        p = self.searchP(P)
        s = self.searchS(P)
        if p == len(self.T):
            return 0
        else:
            r = 0
            if s == len(self.T) - 1:
                while r < len(P) and self.T[self.vs[s] + r] == P[r]:
                    r += 1
                if r == len(P):
                    s += 1
            return s - p - 1
                
    def Occurences(self, P):
        p = self.searchP(P)
        s = self.searchS(P)
        occ = []
        if p == len(self.T):
            return occ
        else:
            r = 0
            if s == len(self.T) - 1:
                while r < len(P) and self.T[self.vs[s] + r] == P[r]:
                    r += 1
                if r == len(P):
                    s += 1
            for i in range(p + 1, s):
                occ.append(self.vs[i])
            return occ



vs = VS("abracadabra")
vs.Print()
print(vs.Occurences("bra"))