def filtering(array, name_array):
    start_ind = 0#array.index('Past Auctions') + 2
    end_ind = array.index('Get the Artsy app')
    array = array[start_ind:end_ind]
    array2 = array.copy()
    # print(new_array)
    # remove non title elements from name_array
    last = None
    while last is None:
        try:
            name_array.remove('Bought In')
        except:
            last = not None
    print(name_array)
    start_ind_piece = []
    for piece in name_array:
        # loop through array to find matching elements to each name_array
        for v in array2:
            if v.startswith(piece):
                piecee = v
                #print(v)
                start_ind_piece.append(array2.index(piecee))
                break
        for kk in range(0, start_ind_piece[len(start_ind_piece) - 1]+1):
            array2[kk] = ""

    print(start_ind_piece)
    for i in range(0, len(start_ind_piece) -1):
        if i + 1 == len(start_ind_piece):
            end_ind = len(array) - 1
        else:
            end_ind = start_ind_piece[i + 1] - 1
            print(array[start_ind_piece[i]:end_ind])
    #print(array)
