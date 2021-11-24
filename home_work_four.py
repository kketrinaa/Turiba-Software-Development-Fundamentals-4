def tower(height,fromPole, toPole, withPole):

    if height >= 1:
        tower(height-1,fromPole,withPole,toPole)
        disk(fromPole,toPole)
        tower(height-1,withPole,toPole,fromPole)

def disk(fromp,top):
    print("moving from",fromp,"to",top)

tower(12,"a","b","c")
