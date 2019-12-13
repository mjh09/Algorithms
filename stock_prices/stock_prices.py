#!/usr/bin/python

import argparse

#function to fin the max difference in an arrar of numbers

def find_max_profit(prices):
  cur_min = prices[0]
  max_prof = 0

  for i in range(len(prices)):
    
    if i == 0:
      pass
    
    
    if i == 1:      #base case to handle the requirement of making one sale - even if unprofitable
      max_prof = prices[i] - cur_min

    
    if prices[i] - cur_min > max_prof:
      max_prof = prices[i] - cur_min
    
    
    if prices[i] < cur_min:
      cur_min = prices[i]
    
    
  return max_prof


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))