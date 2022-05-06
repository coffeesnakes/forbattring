
def lonelyinteger(a):
    # Write your code here
    map = dict()
    for i in a:
        map[i] = map.get(i, 0) + 1
    
    for freq in map.items(): 
        if freq[1] == 1:
            return freq[0]
        