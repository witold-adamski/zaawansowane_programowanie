def even(number: int) -> bool:
    return True if number % 2 == 0 else False


test = even(5)
if test:
    print(f'Liczba parzysta')
else:
    print(f'Liczba nieparzysta')
