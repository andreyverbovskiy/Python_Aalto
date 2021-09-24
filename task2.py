
#heat calculation emission following a formula
def calculate_warming(power,time,device_type,room_size):

  if(device_type == "computer"):
    return (0.92 * power * time*60) /(1012 * 1.225 * room_size)
  elif(device_type == "lights"):
    return (0.9 * power * time*60) /(1012 * 1.225 * room_size)
  elif(device_type == "oven"):
    return (0.95 * power * time*60) /(1012 * 1.225 * room_size)
  elif(device_type == "washing mashine"):
    return (0.8 * power * time*60) /(1012 * 1.225 * room_size)
  else:
    return -99

#cost calculation of power consumption 
def calculate_cost(power,time):
  return round((power * time/60 * 9.89)/1000, 2)



def main():
  
  #arrays to store data
  devices = []
  power = []
  time = []
  fin_ans_w = [] # array to store warming calculation results for final heat outcome
  fin_ans_c = [] # array to store cost calculations results for final cost outcome

  #inputs
  room_size = float(input("Could you please tell me what your room size is?(m3):\n"))
  device_type = input("Could you please tell me what your device type is?:\n")
  average_power = float(input("Could you please tell me what your average power is?(watts):\n"))
  usage_time = int(input("Could you please tell me what your usage time is?(mins):\n"))
  check = input("Would you like to input a new device?:\n")

  #store inputs into arrays for future operations 
  devices.append(device_type)
  power.append(average_power)
  time.append(usage_time)
  
  #loop for adding more devices
  while(check == "yes"):
    d =  input("Could you please tell me what your device type is?:\n")
    a = float(input("Could you please tell me what your average power is?(watts):\n"))
    t = int(input("Could you please tell me what your usage time is?(mins):\n"))
    
    devices.append(d)
    power.append(a)
    time.append(t)
    check = input("Would you like to input a new device?:\n")

  
  #loop for overall heat calculation
  for x in range(len(devices)):
    ans = round(calculate_warming(power[x],time[x],devices[x],room_size),2)
    fin_ans_w.append(ans)
  
  #loop for overall cost calculation
  for y in range(len(devices)):
    fin_ans_c.append(calculate_cost(power[x],time[x]))
  
  #print out the final outcomes
  print("The electric devices heat the room by",sum(fin_ans_w),"degrees and it costs",sum(fin_ans_c),"cents")

main()
