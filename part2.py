"""
******
PART 2
******
Define a function celsius that takes a single float parameter, the temperature in fahrenheit. The function RETURNS (not print) the celsius reading of the temperature

The formula for converting from fahrenheit to celsius:
C = (F - 32) * 5/9
"""
returnnum = 0

def celsius(f): 
  returnnum = f - 32
  returnnum2 = returnnum * 5/9
  return returnnum2
    