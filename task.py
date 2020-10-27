float1 = float(input("float please: "))
float2 = float(input("another: "))
int1 = int(input("integer please: "))
int2 = int(input("another: "))
int3 = int(input("ANOTHER: "))
nums = [float1, float2, int1, int2, int3]
ans = nums[0] + nums[2] + nums[1]
if ans > 24:
    print("wow special numbers")
