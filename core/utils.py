# Copyright (c) 2012 Jiaxing Song
# released under the MIT License, see LICENSE for details
# utils

'''Core utility functions'''

#-----------------------------------------------------------------------------

def len_comm_prefix(w1, w2):
    '''Find the length of longest common prefix of w1 and w2'''
    r = 0
    while r < min(len(w1), len(w2)):
        if w1[r] != w2[r]:
            break
        r += 1

    return r
