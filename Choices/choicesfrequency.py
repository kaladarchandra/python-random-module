import random


def rfreq(given_list,w,length):
    
    AllChoices = [random.choices(given_list, w, k = length) for x in range(1000)] # Contains 1000 lists ( of random.choices(given_list, w, k = length) )
 
    Flist = []  
                                                                                    
    for i in range(len(given_list)):
        Flist.append(sum( [choice.count(given_list[i] ) for choice in AllChoices] ))   # Observe Carefully,Forget the loop, understand sentence structure.
                                                                                        # From AllChoices we take every list,
                                                                                        # And we count the frequency for specific item (given_list[i]) in everylist in AllChoices,
                                                                                        # And the sum function essentially sums all the frequencies of that specific item in all lists of AllChoices,
                                                                                        # And we are appending it to a new list. Observe Frequency of given_list[i] is  Flist[i].
                                                                                        # Essentially, After this Flist contains Frequecies of all elements of given_list.

    total = length * 1000
    RFlist = [round((x/total)*100 , 4) for x in Flist]

    print('LIST =',given_list)
    print('CumulativeWeights =',w)
    print('RelativeFrequencies =',RFlist)



weights = [50, 15, 6, 9, 20]
numbers = [0, 1, 2, 3, 4]
length = 2

rfreq(numbers,weights,length)



