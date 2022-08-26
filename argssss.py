def person(**kwargs):
    print(kwargs)
    print(type(kwargs))

person(name="jacob", age=27, brain="big")

# {'name': 'jacob', 'age': 27, 'brain': 'big'}
# <class 'dict'>