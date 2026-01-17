def sum_positive_numbers(n):
  result = 0
  for number in range (1,n):
    result = result + n
  return result

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


def count_users(group):
    count = 0
    for member in get_members(group):
        if is_group(member):
            count += count_users(member)
        else:
            count += 1
    return count
