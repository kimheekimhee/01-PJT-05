heights = [10, 10, 20, 30]

max_height = max(heights)
min_height = min(heights)

for i in range(len(heights)):
    if heights[i] == max_height:
        heights[i] += 1
        break
for i in range(len(heights)):
    if heights[i] == min_height:
        heights[i] -= 1
        break

print(heights)

max_height = max(heights)
min_height = min(heights)

print(max_height-min_height)