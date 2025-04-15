while True:
        main_optition= input("slope calculator (1) or Point slope calculatatior (2)")
        if main_optition =="1":
                y2_cord = input("what is the 2 y cord :")
                y1_cord = input("what is the 1 y cord :")
                x2_cord = input("what is the 2 x cord :")
                x1_cord = input("what is the 1 x cord :")

                arter_calc1_y2_y1 =int(y2_cord) - int(y1_cord)
                arter_calc1_x2_x1 =int(x2_cord) - int(x1_cord)

                Final_calc = int(arter_calc1_y2_y1) / int(arter_calc1_x2_x1)
                print(f'{Final_calc}')

        if main_optition =="2":

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
                        arter_calc1_y2_y1 =int(y2_cord) - int(y1_cord)
                        arter_calc1_x2_x1 =int(x2_cord) - int(x1_cord)
                        slope = int(arter_calc1_y2_y1) / int(arter_calc1_x2_x1)

                        print(f"y-{y1_cord}={slope}(x-{x1_cord})")
                if points_or_slope =="e":
                        break
        
        if main_optition =='e':
                break