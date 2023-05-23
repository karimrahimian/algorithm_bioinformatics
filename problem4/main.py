from BWT import BWT
if __name__ == "__main__":
    bwt = BWT()
    s = "banana"
    bwtString = bwt.buildBWT(s,3)
    bwtDecode = bwt.decode_bwt("annb$aa")

    print(bwtDecode)
