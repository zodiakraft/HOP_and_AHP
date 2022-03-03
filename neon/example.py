def listmerge3(lstlst):
    all=[]
    for lst in lstlst:
      all.extend(lst)
    return all

print(listmerge3([[[1, 3], [2, 5]], [[2, 3], [3, 2]]]))