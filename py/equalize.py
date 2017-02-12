# repeat last item in short list to equalize to lists

short = [x for x in range(8)]
llong = [y for y in range(12)]

"""
for i in range(len(short), len(llong)):
	short.append(short[-1])

print short
print llong

"""
def equalize(one_list, two_list):
    if len(one_list) > len(two_list):
        short = two_list
        llong = one_list
    else:
        short = one_list
        llong = two_list

    for i in range(len(short), len(llong)):
        short.append(short[-1])


equalize(short, llong)

print short
print llong
