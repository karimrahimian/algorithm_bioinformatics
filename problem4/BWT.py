class BWT():
    def __init__(self):
        self.first = []
        self.last = []
        self.keep =[]
        pass

    def buildBWT(self,text,k):
        text += '$'
        rotations = []
        for i in range(len(text)):
            temp = text[i:] + text[:i]
            rotations.append(temp)
            if i%k ==0 :
                self.keep.append(temp)


        rotations = [text[i:] + text[:i] for i in range(len(text))]
        rotations.sort()
        for item in rotations:
            self.first.append(item[0])
            self.last.append(item[len(item)-1])

        bwt = ''.join(r[-1] for r in rotations)
        print(self.keep)
        return bwt

    def decode_bwt(self,bwt):
        rank = [0] * len(bwt)
        sa = [0] * len(bwt)
        for i, c in enumerate(sorted(bwt)):
            rank[i] = bwt.count(c, 0, i)
        for i, c in enumerate(bwt):
            sa[rank[i]] = i
            rank[i] += 1
        text = ''
        i = sa[0]
        for j in range(len(bwt)):
            text += bwt[i]
            i = sa[i]
        text = text[:-1]

        return text
    def buildBWT1(self,text):
        text += '$'
        rotations = [text[i:] + text[:i] for i in range(len(text))]
        rotations.sort()
        bwt = ''.join(r[-1] for r in rotations)
        return bwt