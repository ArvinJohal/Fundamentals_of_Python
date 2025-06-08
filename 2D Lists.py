Teams = [['Arsenal','Chelsea','Liverpool'],['Man City','Man U','Newcastle']]
#print(Teams[1][2])
#Teams[1][1]='Manchester United'
# x = Teams [1]
# y = x [1:3]
# print (y)
present = False
for team in Teams:
    for name in team:
        print(name)
        if name == "Liverpool":
            print("name found")