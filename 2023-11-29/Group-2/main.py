def input_determination():
  og_values_in_sum=str(input('Input the sum of fractions and/or decimals you want to add in form +Y+Z+...')).split('+').strip()
  precision=int(input('what precision do you want the result to use for your fractions?'))
  values_in_sum=[]
  for i in range(len(og_values_in_sum)):
    if '/' in og_values_in_sum[i]:
      fraction_numerator = og_values_in_sum[i].partition('/')[0]
      fraction_denomenator = og_values_in_sum[i].partition('/')[2]
      
      values_in_sum[i] = Tuple[fraction_numerator, fraction_denomenator]
    else if '.' in og_values_in_sum[i]:
      values_in_sum[i]=turn_to_int(og_values_in_sum[i])
    
    
  
            

def turn_to_int(num: float) -> Tuple[int, int]:
    str_num = f"{num}"
    decimal_point = int(str_num.index("."))
    int_num = int(str_num.replace(".", ""))
    return int_num, decimal_point




