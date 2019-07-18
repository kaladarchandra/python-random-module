import matplotlib.pyplot as plt
import random

name = ['50','20', '20', '9', '1']
l = [1,2,3,4,5]
w = [50,20,20,9,1]

def pie(w,label):
    plt.pie(w,labels = l,startangle = 90)
    plt.title(label)
    plt.legend()
    plt.show()

def returnfrequency(onelist):

    o  = [x.count(1) for x in onelist]
    Tw = [x.count(2) for x in onelist]
    Th = [x.count(3) for x in onelist]
    Fo = [x.count(4) for x in onelist]
    Fi = [x.count(5) for x in onelist]
    
    print(onelist[:2], o[:2])
    print(sum(o),sum(Tw),sum(Th),sum(Fo),sum(Fi))
# YOU COULD GIVE RATIO TO IT
    
    return [sum(o),sum(Tw),sum(Th),sum(Fo),sum(Fi)]


onelist = [random.choices(l,w,k = 10) for x in range(1000)]
label = 'Lists of lenght 10'
w = returnfrequency(onelist)
pie(w,label)
print(onelist)

