

def int_to_roman(num : int) -> str:  
  values = [  
      1000, 900, 500, 400, 100,  
      90, 50, 40, 10, 9, 5, 4, 1  
  ]  
  roman = [  
      "M", "CM", "D", "CD", "C",  
      "XC", "L", "XL", "X", "IX", "V", "IV", "I"  
  ]  
  roman_num = ""  
  i = 0  
  while num > 0:  
      for _ in range(num // values[i]):  
          roman_num += roman[i]  
          num -= values[i]  
      i += 1  
  return roman_num  


print(int_to_roman(1993))  
print(int_to_roman(3))  
print(int_to_roman(4))  
print(int_to_roman(9))  
print(int_to_roman(58))  
print(int_to_roman(1994))  