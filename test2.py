
try:
    var = int(input("Input: "))
except ValueError as e:
    print(f"Only accept integer input. Msg: {e}")

i = [i for i in range(1, var + 1) if (not i % 5 and not i % 3) or (i % 5 and i % 3)]
print("Output: ", len(i))
