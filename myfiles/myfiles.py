#remove new line '\n' syntax while reading lines of any file
def rmnl(l):
    n_l=[]
    for i in l:
        if i[len(i)-1:len(i)]=='\n':
            n_l.append(i[0:len(i)-1])
    return n_l        