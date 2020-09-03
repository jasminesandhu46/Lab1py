# Author: Jasmine Sandhu jps6818@psu.edu
# Collaborator: Gabriel Charpentier gbc5202@psu.edu
# Collaborator: Brian Truong bqt5199@psu.edu

temp = input ("Enter temperature: ")
temp = float(temp)
letter = input ("Enter unit in F/f or C/c: ")
if letter == "f" or letter == "F":
  tempnew = (temp-32)/1.8
  print(f"{temp}° in Fahrenheit is equivalent to {tempnew}° Celsius.")
elif letter == "c" or letter == "C":
  tempnew = (9*temp/5)+32
  print(f"{temp}° in Celsius is equivalent to {tempnew}° Fahrenheit.")
else:
  print(f"Invalid unit({letter}).")

    