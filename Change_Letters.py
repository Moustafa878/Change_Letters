def change_Letters(str):
    alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    vowels=['a','e','i','o','u']
    temp=""
    for i in str:
        for j in range(0,len(alph)):
            if (i==alph[j]):
                temp+=(alph[j+1])
    print("First Edit  : ",temp)
    for i in temp:
        for j in range(0,len(vowels)):
            if (i==vowels[j]):
                temp=temp.replace(i,i.capitalize())
    temp2='Second Edit : '+temp

    return temp2


print(change_Letters("hello world"))