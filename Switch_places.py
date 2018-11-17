def switch(l):
    print "orginal list"
    print l
    print "---------"
    
    
    tmp = l[1]
    l[1] = l[0]
    l[0] = tmp
    print "first swap"
    print l
    print "---------"
#======separation========#
    tmp = l[2]
    l[2] = l[3]
    l[3] = tmp
    print "2nd swap"
    print l
    print "---------"
#======separation========#
    tmp = l[4]
    l[4] = l[5]
    l[5] = tmp
    
    print "3rd swap"
    print l
    print "---------"
#======separation========#
    tmp = l[6]
    l[6] = l[7]
    l[7] = tmp
    
    print "4th swap"
    print l
    print "---------"
#======separation========#
    tmp = l[1]
    l[1] = l[2]
    l[2] = tmp
    
    print "5th swap"
    print l
    print "---------"
#======separation========#
    tmp = l[6]
    l[6] = l[7]
    l[7] = tmp
    
    print "6th swap"
    print l
    print "---------"
#======separation========#
    tmp = l[3]
    l[3] = l[4]
    l[4] = tmp
    print "7th swap"
    print l
    print "---------"
#======separation========#
    tmp = l[2]
    l[2] = l[3]
    l[3] = tmp
    print "8th swap"
    print l
    print "---------"
#======separation========#
    tmp = l[6]
    l[6] = l[7]
    l[7] = tmp
    print "9th swap"
    print l
    print "---------"
#======separation========#
    tmp = l[5]
    l[5] = l[6]
    l[6] = tmp
    print "10th swap"
    print l
    print "---------"
#======separation========#
    tmp = l[4]
    l[4] = l[5]
    l[5] = tmp
    print "11th swap"
    print l
    print "---------"
#======separation========#
    tmp = l[3]
    l[3] = l[4]
    l[4] = tmp
    print "12th swap"
    print l
    print "---------"
#======separation========#
    

    print "Current Swap"
    return l
    
    
    l = ["r","b","r","b","r","b","r","b"]
