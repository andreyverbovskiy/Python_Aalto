def main():
    
    print("This program calculates and summarizes the estimated profits from an investment.")

    initial_investment    = float(input("Initial investment sum (eur):\n"))
    annual_profit_percent = float(input("Expected annual growth / return rate (including expenses) (%):\n"))
    per_month_investment  = float(input("Monthly investment (+) or withdrawal (-) (eur):\n"))
    years                 = float(input("For how many years are you planning to hold the investment?\n"))

    e = "eur"
    print('{:>5s} | {:>5s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('Year','Month','Start','Monthly', 'End', 'Cumulative'))
    print('{:>5s} | {:>5s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('','','balance','Profit', 'balance','Profit'))
    print('{:>5s} | {:>5s} | {:>10s} | {:>10s} | {:>10s} | {:>10s}'.format('','',e,e,e,e))
    print('-' * 65)

    annual_profit_multiplier = 0.01 * annual_profit_percent
    # There are 12 months in a year; let's divide the exponential growth to them expecting it to be constant:
    monthly_profit_multiplier = ((1 + annual_profit_multiplier) ** (1 / 12) - 1) 


    
    start = initial_investment #copy the first value

    for a in range(1,int(years)+1):
      for b in range(1,13):
        if(start<0):
          break
        else:
          month_profit = float(start*monthly_profit_multiplier) # month profit calc
          end_balance = (start + per_month_investment) + month_profit # end balance
          x = end_balance - (initial_investment + per_month_investment*b) # cimilative profit
      
          print('{:>5d} | {:>5d} '.format(a, b, ))
          print('{:>5s} | {:>5s} '.format('', '', ))

          print('{:>5s} | {:>5s} | {:>10f} | {:>10f} | {:>10f} | {:>10f}'.format('', '', round(start,2), round(month_profit, 2), round(end_balance,2), round(x,2)))
          start = end_balance # overwrite the starting value
        

    print("End balance:",round(end_balance,2))


main()
