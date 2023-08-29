
def reorganizeString(s):
    n = len(s)
    Keys = []
    Values = []
    for i in range(n):
        if s[i] not in Keys:
            Keys.append(s[i])
            count = 1
            j = i + 1
            while j <= n - 1:
                if s[i] == s[j]:
                    count += 1
                j += 1
            Values.append(count)

    ans = ""
    my_dict = dict(zip(Keys,Values))

    last_let = {}

    while my_dict:
        next_let = max(my_dict, key=my_dict.get)
        ans = ans + next_let
        if last_let:
            my_dict.update(last_let)
        my_dict[next_let] = my_dict[next_let] - 1
        if my_dict[next_let] == 0:
            del my_dict[next_let]
        else:
            last_let = {next_let: my_dict.pop(next_let)}

    if len(ans) != n:
        return ""
    else:
        return ans

s = "bfrbs"
x = reorganizeString(s)
print(x)