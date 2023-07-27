classA = ["MARYA", "MARYAM", "SAFA"]
classA.append("SAHAR")
print(classA)


classA = ["MARYA", "MARYAM", "SAFA"]
classB = ["SARA", "HUSNA", "LINA"]
classA.extend(classB)
print(classA)

classA = ["MARYA", "MARYAM", "SAFA"]
thistuple = ("SARA", "SAHAR")
classA.extend(thistuple)
print(classA)