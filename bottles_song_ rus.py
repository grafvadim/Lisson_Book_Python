world = "бутылок"
for beer_num in range(99, 0, -1):
    print(beer_num, world, "пива на стене.")
    print(beer_num, world, "пива.")
    print("Возьми одну.")
    print("Пусти по кругу.")
    if beer_num == 1:
        print("Нет бутылок пива на стене!")
        print("Не поплахело Вам от 99 бутылок пива))")
        print("Хорош бухать, иди работай!!!")
    else:
        new_num = beer_num - 1
        if new_num >= 11 and new_num <= 19:
            world = "бутылок"
        else:
            if new_num % 10 == 1:
                world = "бутылка"
            elif new_num % 10 in (2, 3, 4):
                world = "бутылки"
            else:
                world = "бутылок"
        print(new_num, world, "пива на стене.")
    print()