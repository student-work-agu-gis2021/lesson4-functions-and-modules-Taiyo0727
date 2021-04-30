def fahr_to_celsius(temp_fahrenheit):
  #We can change from fahrenheit to fahr_to_celsius.
  #temp_fahrenheit : the temparture you want to change.
  converted_temp = (temp_fahrenheit -32) /1.8
  return converted_temp
def temp_classifier(temp_celsius):
#purpose of the function : separate to temperature
#parameter : temperature of Celsius
#returned values : x < -2 is 0, -2<=x <2 is 1, 2<= x <15 is 2, and x>=15 is 3
  if temp_celsius < -2:
    return 0
  elif temp_celsius <2:
    return 1
  elif temp_celsius < 15:
    return 2
  elif temp_celsius >=15:
    return 3
