import random

# assuming that waiting is a list of say... ids (i will use names in example)
# we might want to pair up 1 group of 3 if it is odd but
# maybe not say if people are speed dating, they probably 
# don't want 3 ppl groups, or maybe they do! if not one person
# will remain in the waiting room

waitingRoom = ["lei","keer","priscilla","kiana","arvie","Tutu","Laolao"]
pairs = []

def pairUp (waitingRoom, group3,pairs):
    random.shuffle(waitingRoom)
    odd = isOdd(len(waitingRoom))
    if len(waitingRoom) > 1:
        pairs,waitingRoom = formGroups(waitingRoom,odd,group3,pairs)
    return (pairs,waitingRoom)


def formGroups(room, odd, group3, pairs):  #O(n)
    if (odd and group3):
        group = [room[0],room[1],room[2]]
        pairs.append(group)
        room = room[3:]
    while len(room) > 1:
        pair = [room[0],room[1]]
        pairs.append(pair)
        room = room[2:]
    return pairs,room



# people can return to the waiting room if they are done or have paired previously
def returnToWait(pairs,pair,waitingRoom):    
    for person in pair:
        waitingRoom.append(person)
    pairs.pop(pairs.index(pair))
    return pairs,waitingRoom


def isOdd (num):
    if (num%2 == 0):
        return False
    else: return True


# initial pairing
print("initial pairing: ")
pairs,waitingRoom = pairUp(waitingRoom, True, pairs)
print("     pairs:" + str(pairs))
print("     waitingRoom:" + str(waitingRoom))
# 2 groups return to waitingroom, in practice we won't have the index
# we will just have the pair themselves
print("Return 2 groups to waitingRoom:")
returnToWait(pairs,pairs[2],waitingRoom)
returnToWait(pairs,pairs[0],waitingRoom)
print("     pairs:" + str(pairs))
print("     waitingRoom:" + str(waitingRoom))
# pair again! I acknologe that it is possibel that people might have the same pairs
print("pair again: ")
pairs,waitingRoom = pairUp(waitingRoom, False , pairs)
print("     pairs:" + str(pairs))
print("     waitingRoom:" + str(waitingRoom))


# If I were to attempt this again I mgiht take another route, say finding all possible
# combinations, or keeping a set of seen pairs and when the possible pairs have exhausted
# people can either choose to talk to someone they have talked to before or remain in the 
# waiting room. but alas! I'm outta time :) formGroup function is the most costly with O(n)
# append could potentially take O(n) if there was not enough space allocated but since
# we have a fixed size of people it shouldn't be a concern