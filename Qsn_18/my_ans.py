def minPlatforms(arrival, departure):
    platforms = count = i = j = 0
    while i < len(arrival):
        if arrival[i] < departure[j]:
            count = count + 1
            platforms = max(platforms, count)
            i = i + 1
        else:
            count = count - 1
            j = j + 1
    return platforms
print("Minimum platforms required:",minPlatforms([2.00,2.10,3.00,3.20,3.50,5.00],[2.30,3.40,3.20,4.30,4.00,5.20]))
