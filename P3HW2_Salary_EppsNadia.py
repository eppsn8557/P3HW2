 # CTI-110

   # P3HW2 - Salary

   # Nadia Epps

   # 30 October 2023

   #

print('Enter employees name:', end=' ')
name = input()
hoursw = float(input('Enter number of hours worked: '))
prate = float(input('Enter employees pay rate: '))
print('-----------------------------------')
print('Employee name:', name)
print()
print('Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
print('-------------------------------------------------------------------------------')
ovtime = 0
if hoursw >= 40:
    ovtime = hoursw - 40
    hoursw = hoursw - ovtime
else:
    ovtime == 0
otimepay = (ovtime * (prate*1.5))
reghour = prate * hoursw
grosspay = reghour + otimepay
print(f'{hoursw}            {prate}      {ovtime}          {otimepay:.2f}            {reghour:.2f}        {grosspay:.2f}')


