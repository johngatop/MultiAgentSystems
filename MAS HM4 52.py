from math import *
from random import *

range1=100000
range2=100000


sample1=list(range(range1))
sample2=list(range(range2))
supportlist = list(range(range1))

rdm1 = randint(1, 50)
rdm2 = randint(1, 50)


for i in range(range1):
    sample1[i] = randint(1, rdm1)
for i in range(range2):
    sample2[i] = randint(1, rdm2)


def get_mean(inputlist):
    sum = 0
    for i in range(len(inputlist)):
        sum = sum + inputlist[i]
    return sum/len(inputlist)

def get_var(inputlist):
    for i in range(len(inputlist)):
        supportlist[i]=pow(inputlist[i],2)
    return get_mean(supportlist) - pow(get_mean(inputlist),2)

def get_normal_dis(mean, sd, inputlist):
    for i in range(range1):
        inputlist[i]=1/(sqrt(2*pi*sd)) * exp(-((inputlist[i]-mean)**2)/sd)
    return inputlist

def get_kl():
    p1 = log(sd2 ** 2 / sd1 ** 2, e)
    p2 = (sd1 ** 2 + ((mean1 - mean2) ** 2)) / (sd2 ** 2)
    kl = (p1 + p2 - 1) / 2
    return kl

def get_monte_carlo(inputlist1,inputlist2,range1):
    sum=0
    for i in range(range1):
        sum = log(inputlist1[i]/inputlist2[i], e) + sum
    return sum/range1

def get_error(range1):
    sample3=list(range(range1))
    for i in range(range1):
        sample3[i]= log(sample1[i]/sample2[i], e)
    var= get_var(sample3)
    return var/range1


mean1=get_mean(sample1)
sd1=get_var(sample1)

mean2=get_mean(sample2)
sd2=get_var(sample2)


sample1=get_normal_dis(mean1, sd1, sample1)
sample2=get_normal_dis(mean2, sd2, sample2)

kl=get_kl()
mc=get_monte_carlo(sample1,sample2,range1)
diff=kl-mc
error = get_error(range1)


print("Mean 1: ",mean1 ,"  SD1:", sd1)
print("Mean 2: ",mean2 ,"  SD2:", sd2)
print("KL: ",'{0:.10f}'.format(kl) ,"  Monte Carlo: ", '{0:.10f}'.format(mc) , "    error: ", '{0:.10f}'.format(error), "    diff:", '{0:.10f}'.format(diff))