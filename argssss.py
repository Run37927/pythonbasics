def person(**kwargs):
    print(kwargs)
    if 'age' in kwargs:
        print('you age is ', kwargs.get("age"))


person(name="jacob", age=27, brain="big")

