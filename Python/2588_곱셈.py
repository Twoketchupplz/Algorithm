mult1 = int(input())
mult2 = list(input())

output_3 = mult1 * int(mult2[2])
output_4 = mult1 * int(mult2[1])
output_5 = mult1 * int(mult2[0])
output_6 = output_3 + (output_4 * 10) + (output_5 * 100)

print(output_3)
print(output_4)
print(output_5)
print(output_6)
