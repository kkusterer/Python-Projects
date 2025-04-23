#point slope is y-y=m(x-x)
    


points_or_slope = input("do you have the slope already and 1 point? (1). Or need slope and have 2 orderd pairs. (2)")

if points_or_slope == "1":
        slope_1 =input("what is the slope")
        x_point_1 = input("what is the x number in the pair")
        y_point_1 = input("what is the y number in the pair")
        print(f"y-{y_point_1}={slope_1}(x-{x_point_1})")

if points_or_slope =="2":
        y2_cord = input("what is the 2 y cord :")
        y1_cord = input("what is the 1 y cord :")
        x2_cord = input("what is the 2 x cord :")
        x1_cord = input("what is the 1 x cord :")
        arter_calc1_y2_y1 =float(y2_cord) - float(y1_cord)
        arter_calc1_x2_x1 =float(x2_cord) - float(x1_cord)
        slope = float(arter_calc1_y2_y1) / float(arter_calc1_x2_x1)

        print(f"y-{y1_cord}={slope}(x-{x1_cord})")