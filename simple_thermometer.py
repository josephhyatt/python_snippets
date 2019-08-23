select_temp_scale = input(
    "Input any integer along with 'C or 'F' to get the conversion: ")

unit = select_temp_scale[-1]
select_temp_scale = int(select_temp_scale[0: -1])

if unit == 'C' or unit == 'c':
    select_temp_scale = round(select_temp_scale * (9 / 5) + 32)
    print(str(select_temp_scale) + 'F')
elif unit == 'F' or unit == 'f':
    select_temp_scale = round((select_temp_scale - 32) * (5 / 9))
    print(str(select_temp_scale) + 'C')
