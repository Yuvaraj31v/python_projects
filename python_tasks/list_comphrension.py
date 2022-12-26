# Normal list comphrension

squares = [i * i for i in range(10)]
print(squares)

# list comphrension with coditional statements
names = ["yosuva", "Rama", "sanjai", "gautham", "bala", "pradeep", "ramachandran", "rithi"]


def capitialize_names(name):
    return name.upper()


def de_capitialize_names(name):
    return name.lower()


capitialized_name = [capitialize_names(i) if (i[0] == "r") else (de_capitialize_names(i)) for i in names]
print(capitialized_name)


# Nested Comphrension
cites =['hyderabad','chennai','banglore','cochin','jaipur','vagamon','ooty','munnar','wayanad','shimla','manali','north-east ']
weather_report = {cities: [i for i in range(0,3)] for cities in cites}
print(weather_report)