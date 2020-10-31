def maxweight(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    ans = 0
    while i <= j:
        ans += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return ans
print(maxweight([32,3,45,5,5,74,34,56],73))
