import re


lines = open("../data/ex10.txt").readlines()
positions = []
velocities = []
for line in lines:
    nums = re.findall(r'\d+', line)
    positions.append((int(nums[0]), int(nums[1])))
    velocities.append((int(nums[2]), int(nums[3])))


