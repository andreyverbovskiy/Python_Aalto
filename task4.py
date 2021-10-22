import statistics 

#function for median calculation (required by assignment)
def find_median(number1,number2,number3):

  outcome = statistics.median([number1,number2,number3])

  return outcome


#median based filter function
def median_filter(signal):
  
  arr = []

  

  for x in range(len(signal)-1):

    if(x == 0):
      arr.append(signal[0])

    elif (x == len(signal)-2):
      arr.append(signal[x+1])

    else:
      outcome = find_median(signal[x], signal[x-1], signal[x+1])
      arr.append(outcome)

  return arr
    


  

def main():

  signal = []

  inp = 1

  while(inp != ""):
    inp = input("Enter the data points of the signal. Stop with empty line: \n")
    if(inp != ''):
      signal.append(float(inp))
    else:
      pass


  print("The original signal is:", signal)

  arr1 = median_filter(signal)

  print("The median filtered signal is:",arr1)
  
   


main()
