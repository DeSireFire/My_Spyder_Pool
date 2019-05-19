test1 = {
    'a':66,
    'v':67,
    'c':68,
    'd':69,
}
nya = 2
test2 = {}
for i in test1.keys():
    test2[i] = test1[i]/nya

print(test2)

for i in test1.keys():
    test1[i] = test1[i]/nya

print(test1)