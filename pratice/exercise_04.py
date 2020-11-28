print("\t\t\tMultiplication Table\n")

for i in range(1,13):
    print(i, end="\t")
print()
print("__________\n")

for j in range(1,13):
  for k in range(1,13):
    print(k * j, end="\t")
  print("\n")