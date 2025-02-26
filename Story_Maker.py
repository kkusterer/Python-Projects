while True:
    def all():
        print('Story picker')
        print('Pick cowboy story(1) or alein story(2)')
        choice = input("Enter choice (1/2): ")
        name = input('Name:')
        age = input('age:')
        place = input('place:')
        place2 = input('place 2:')


        if choice == '1':

            print(f'\nOnce apon a time there was a cowboy named {name} he was {age} years old he lived in the small city of {place} he did not like that city so he moved avay to {place2} he was the best cowboy in the west. THE END.')

        if choice == '2':

            print(f'\nOnce apon a time in the future an alein named {name} he was a very shy alein and all of the other ailens were always mean to {name} {name} was only {age} years old he moved from {place} to {place2} and he lived a peaceful life all alone. THE END.')


    if __name__ == "__main__":
                all()
