def merge_sort(A, a = 0, b = None):
    '''Sort A(a:b)'''
    if b is Nonoe: b = len(A)
    if 1 < b -a:
        c = (a+b+1)//2
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R=A[a:c], A[c:b]
        merge(L, R, A, len(L), len(R), a, b)