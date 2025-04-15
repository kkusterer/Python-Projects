
#y2-y1
#Over
#x2-x1

y2_cord = input("what is the 2 y cord :")
y1_cord = input("what is the 1 y cord :")
x2_cord = input("what is the 2 x cord :")
x1_cord = input("what is the 1 x cord :")

arter_calc1_y2_y1 =int(y2_cord) - int(y1_cord)
arter_calc1_x2_x1 =int(x2_cord) - int(x1_cord)

Final_calc = int(arter_calc1_y2_y1) / int(arter_calc1_x2_x1)
print(f'{Final_calc}')