import statistics

def find_median(number1,number2,number3):

  outcome = statistics.median([number1,number2,number3])

  return outcome



def median_filter(signal):
  
  arr = []

  

  for x in range(len(signal)):

    if(x == 0):
      arr.append(signal[0])

    elif (x == len(signal)):
      arr.append(signal[-1])

    else:
      outcome = find_median(signal[x], signal[x-1], signal[x+1])
      arr.append(outcome)
    


  

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

  signal = median_filter(signal)

  print("The median filtered signal is:",signal)
  
   


main()
