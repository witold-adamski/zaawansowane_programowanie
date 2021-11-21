def hello(name: str, surname: str) -> str:
    s = f'Cześć {name} {surname}';
    return s


test = hello('Adam', 'Malysz')
print(test)
