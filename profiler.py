#   Anthony Miller  12/9/2019
##  CSE431
### Compare the performance of two functions A and B in Python3.7.5 (64 bit)

import sys
import random
import statistics
from time import perf_counter




####
#   Spit out time values for two functions A, B tested on set of inputs size N
####
def GetResults(A, B, N, lowerBound, upperBound):        

    ##   Generate stats in ms for function A
    meanA = statistics.mean(A)
    medianA = statistics.median(A)
    modeA = statistics.mode(A)

    ##   Generate stats in ms for function B
    meanB = statistics.mean(B)
    medianB = statistics.median(B)
    modeB = statistics.mode(B)

    #   Version
    version = ".".join( map(str, sys.version_info[:3]) )
    
    ##  Header
    print()
    print(" For",format(N, ',d'),"calls on random numbers ranging from",
            format(lowerBound, ',d'),"to",format(upperBound, ',d'),":")
    print(" in Python:",version,":")
    print()

    ##  Stats
    #   Stats for function A
    print(" Function A():")
    print(" -> Mean Time Value for A(): {:>30}".format(meanA),"ms" )
    print(" -> Median Time Value for A(): {:>28}".format(medianA),"ms" )
    print(" -> Mode Time Value for A(): {:>30}".format(modeA),"ms" )
    print()

    #   Stats for function B
    print(" Function B(): ")
    print(" -> Mean Time Value for B(): {:>30}".format(meanB),"ms" )
    print(" -> Median Time Value for B(): {:>28}".format(medianB),"ms" )
    print(" -> Mode Time Value for B(): {:>30}".format(modeB),"ms" )
    print()

    ##  Comparisons
    #   Compare mean values
    if meanA < meanB:
        print("The mean time value for function A is lower: ", meanA,"ms")
        print(" -> Difference: ", meanB - meanA,"ms")

    elif meanA > meanB:
        print("The mean time value for function B is lower: ", meanB,"ms")
        print(" -> Difference: ", meanA - meanB,"ms")
    elif meanA == meanB: print("The mean time values were found to be equivalent.")
    print()

    #   Compare median values
    if medianA < medianB:
        print("The median time value for function A is lower: ", medianA,"ms")
        print(" -> Difference: ", medianB - medianA,"ms")

    elif medianA > medianB:
        print("The median time value for function B is lower: ", medianB,"ms")
        print(" -> Difference: ", medianA - medianB,"ms")

    elif medianA == medianB: print("The median time values were found to be equivalent.")
    print()

    #   Compare mode values (if it is relevant to case)
    if modeA < modeB:
        print("The mode time value for function A is lower: ", modeA,"ms")
        print(" -> Difference: ", modeB - modeA,"ms")

    elif modeA > modeB:
        print("The mode time value for function B is lower: ", modeB,"ms")
        print(" -> Difference: ", modeA - modeB,"ms")

    elif modeA == modeB: print("The mode time values were found to be equivalent.")
    print()




####
#   Testing binary AND
####
def A(n):
    return n & 1




####
#   Testing modulo
####
def B(n):
    return n % 2 == 1




####
#   Testbed
####
def main():

    #   Start  clock (this is for fun)
    initialClockProgram = perf_counter()

    #   This is a lot (change at will)
    N = 500000
    lowerBound = 0
    upperBound = 1000000000
    #   Make a length N list of random numbers anywhere between 0 to 1 billion
    randomNumbers = [random.randint(lowerBound, upperBound) for _ in range(N)]
    
    valuesA = []
    valuesB = []

    #   Get each of the two functions performance times for runs in list
    for i in randomNumbers:
        
        ####    binaryAND    ####
        #   Start clock
        initialClockA = perf_counter()

        A(i)

        #   Stop clock
        finalClockA = perf_counter()
        
        #   Append time value to list (in milliseconds)
        valuesA.append( (finalClockA - initialClockA) * 1000 )


        ####    modulo    ####
        #   Start clock
        initialClockB = perf_counter()

        B(i)

        #   Stop clock
        finalClockB = perf_counter()

        #   Append time value to list (in milliseconds)
        valuesB.append( (finalClockB - initialClockB) * 1000 )

    GetResults(valuesA,valuesB,N,lowerBound,upperBound)

    #   Stop clock (for total runtime)
    finalClockProgram = perf_counter()

    print()
    print(" Program run complete.")
    print(" -> Running this entire program took your system: ", ( (finalClockProgram - initialClockProgram) ), " seconds." )
    print()



if __name__=="__main__":
    main()