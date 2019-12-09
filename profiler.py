#   Anthony Miller  12/9/2019
##  CSE431
### Compare the performance of two functions A and B in Python3.7.5 (64 bit)

import random
import statistics
from time import perf_counter

##
#   Spit out time values for two functions A, B tested on same set of inputs size N
##
def GetResults(A, B, N):

    #   Generate stats in ms for function A
    meanA = statistics.mean(A)
    medianA = statistics.median(A)
    modeA = statistics.mode(A)

    #   Generate stats in ms for function B
    meanB = statistics.mean(B)
    medianB = statistics.median(B)
    modeB = statistics.mode(B)

    #   Header
    print()
    print(" For ",format(N, ',d')," function calls on random numbers ranging from 0 to 1,000,000,000:")
    print()

    #   Stats for function A
    print(" Function IsOddA():")
    print(" -> Mean Time Value for IsOddA(): {:>30}".format(meanA),"ms" )
    print(" -> Median Time Value for IsOddA(): {:>28}".format(medianA),"ms" )
    print(" -> Mode Time Value for IsOddA(): {:>30}".format(modeA),"ms" )
    print()

    #   Stats for function B
    print(" Function IsOddB(): ")
    print(" -> Mean Time Value for IsOddB(): {:>30}".format(meanB),"ms" )
    print(" -> Median Time Value for IsOddB(): {:>28}".format(medianB),"ms" )
    print(" -> Mode Time Value for IsOddB(): {:>30}".format(modeB),"ms" )
    print()


    #   Compare mean values
    if meanA < meanB: print("The mean time value for function A is lower: ", meanA,"ms")
    elif meanA > meanB: print("The mean time value for function B is lower: ", meanB,"ms")
    elif meanA == meanB: print("The mean time values were found to be equivalent.")
    print()

    #   Compare median values
    if medianA < medianB: print("The median time value for function A is lower: ", medianA,"ms")
    elif medianA > medianB: print("The median time value for function B is lower: ", medianB,"ms")
    elif medianA == medianB: print("The median time values were found to be equivalent.")
    print()

    #   Compare mode values (if it is relevant to case)
    if modeA < modeB: print("The mode time value for function A is lower: ", modeA,"ms")
    elif modeA > modeB: print("The mode time value for function B is lower: ", modeB,"ms")
    elif modeA == modeB: print("The mode time values were found to be equivalent.")
    print()




##
#   Testing binary AND
##
def isOddA(n):
    return n & 1


##
#   Testing modulo
##
def isOddB(n):
    return n % 2 == 1


##
#   Testbed
##
def main():

    #   This is for fun
    programInitial = perf_counter()

    #   This is a lot (change at will)
    N = 10000000

    #   Make a length N list of random numbers anywhere between 0 to 1 billion
    randomNumbers = [random.randint(0, 1000000000) for _ in range(N)]
    
    A = []
    B = []

    #   Get each of the two functions performance times for 10,000 runs in a list
    for i in randomNumbers:
        
        ####    binaryAND    ####
        #   Start
        aInitial = perf_counter()

        isOddA(i)

        #   Stop
        aFinal = perf_counter()
        
        #   Append time value to list (in milliseconds)
        A.append( (aFinal - aInitial) * 1000 )


        ####    modulo    ####
        #   Start
        bInitial = perf_counter()

        isOddB(i)

        #   Stop
        bFinal = perf_counter()

        #   Append time value to list (in milliseconds)
        B.append( (bFinal - bInitial) * 1000 )

    GetResults(A,B,N)

    programFinal = perf_counter()

    print()
    print(" Program run complete.")
    print(" -> Running this entire program took your system: ", ( (programFinal - programInitial) ), " seconds." )
    print()



if __name__=="__main__":
    main()