from sklearn import tree


#features = [avg temp ,snow, rain, max wind, high, low]
features = [[-4, 15, 0, 39, 0, -8], [-1, 14, 0, 52, 0, -7], [-16, 0, 0, 43, 0, -8], [-15, 0, 0, 37, 0, -7], [-9, 0, 0, 9, 0, -8],
[14, 0, 2, 31, -1, -7], [10, 0, 3, 33, -1, -10], [0, 0, 13, 33, -1, -9], [7, 0, 10, 6, 0, -7], [8, 1, 0, 54, 0, -8], 
[-2, 1, 0, 46, 0, -9], [1, 12, 8, 56, 0, -9], [1, 4, 0, 54, -1, -8], [1, 0, 0, 13, 0, -7], [5, 0, 1, 52, 0, -7], 
[-3, 4, 0, 28, 1, -6], [-3, 0, 0, 15, 3, -5,], [0, 0, 5, 33, 3, -4], [5, 0, 0, 44, 3, -4], [4, 0, 0, 9, 2, -5], 
[-3, 1, 0, 67, 1, -6], [-4, 0, 0, 28, 1, -7], [-6, 13, 0, 22, 1, -7], [-6, 0.3, 0, 9, 1, -6]]

#snowday 1 = yes, 0 = no
labels = [0, 1, 0, 0, 0, 
0, 0, 1, 1, 0, 
0, 1, 1, 0, 0, 
0, 0, 0, 0, 0,
0, 0, 1, 0]

#setup model
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

#inputs
print("Snow Day Predictor")
avgtemp = input("What's the average temperature?")
snow = input("How much snow?")
rain = input("How much rain?")
maxwind = input("What's the max wind?")
high = input("What's the average high?")
low = input("What's the average low?")

#predict
prediction = clf.predict([[avgtemp, snow, rain, maxwind, high, low]])

#result
if (prediction == 1):
    print("The AI model predicted a snow day")
    print('YYYYYYY       YYYYYYY           AAA           YYYYYYY       YYYYYYY      !!! ')
    print('Y:::::Y       Y:::::Y          A:::A          Y:::::Y       Y:::::Y     !!:!!')
    print('Y:::::Y       Y:::::Y         A:::::A         Y:::::Y       Y:::::Y     !:::!')
    print('Y::::::Y     Y::::::Y        A:::::::A        Y::::::Y     Y::::::Y     !:::!')
    print('YYY:::::Y   Y:::::YYY       A:::::::::A       YYY:::::Y   Y:::::YYY     !:::!')
    print('   Y:::::Y Y:::::Y         A:::::A:::::A         Y:::::Y Y:::::Y        !:::!')
    print('    Y:::::Y:::::Y         A:::::A A:::::A         Y:::::Y:::::Y         !:::!')
    print('     Y:::::::::Y         A:::::A   A:::::A         Y:::::::::Y          !:::!')
    print('      Y:::::::Y         A:::::A     A:::::A         Y:::::::Y           !:::!')
    print('       Y:::::Y         A:::::AAAAAAAAA:::::A         Y:::::Y            !:::!')
    print('       Y:::::Y        A:::::::::::::::::::::A        Y:::::Y            !!:!!')
    print('       Y:::::Y       A:::::AAAAAAAAAAAAA:::::A       Y:::::Y             !!! ')
    print('       Y:::::Y      A:::::A             A:::::A      Y:::::Y                 ')
    print('    YYYY:::::YYYY  A:::::A               A:::::A  YYYY:::::YYYY          !!! ')
    print('    Y:::::::::::Y A:::::A                 A:::::A Y:::::::::::Y         !!:!!')
    print('    YYYYYYYYYYYYYAAAAAAA                   AAAAAAAYYYYYYYYYYYYY          !!! ')
else :
    print("The AI model predicted no snow day")
    print('FFFFFFFFFFFFFFFFFFFFFFUUUUUUUU     UUUUUUUU       CCCCCCCCCCCCCKKKKKKKKK    KKKKKKK')
    print('F::::::::::::::::::::FU::::::U     U::::::U    CCC::::::::::::CK:::::::K    K:::::K')
    print('F::::::::::::::::::::FU::::::U     U::::::U  CC:::::::::::::::CK:::::::K    K:::::K')
    print('FF::::::FFFFFFFFF::::FUU:::::U     U:::::UU C:::::CCCCCCCC::::CK:::::::K   K::::::K')
    print('  F:::::F       FFFFFF U:::::U     U:::::U C:::::C       CCCCCCKK::::::K  K:::::KKK')
    print('  F:::::F              U:::::D     D:::::UC:::::C                K:::::K K:::::K  ')
    print('  F::::::FFFFFFFFFF    U:::::D     D:::::UC:::::C                K::::::K:::::K  ')
    print('  F:::::::::::::::F    U:::::D     D:::::UC:::::C                K:::::::::::K     ')
    print('  F:::::::::::::::F    U:::::D     D:::::UC:::::C                K:::::::::::K')
    print('  F::::::FFFFFFFFFF    U:::::D     D:::::UC:::::C                K::::::K:::::K   ')
    print('  F:::::F              U:::::D     D:::::UC:::::C                K:::::K K:::::K   ')
    print('  F:::::F              U::::::U   U::::::U C:::::C       CCCCCCKK::::::K  K:::::KKK')
    print('FF:::::::FF            U:::::::UUU:::::::U  C:::::CCCCCCCC::::CK:::::::K   K::::::K')
    print('F::::::::FF             UU:::::::::::::UU    CC:::::::::::::::CK:::::::K    K:::::K')
    print('F::::::::FF               UU:::::::::UU        CCC::::::::::::CK:::::::K    K:::::K')
    print('FFFFFFFFFFF                 UUUUUUUUU             CCCCCCCCCCCCCKKKKKKKKK    KKKKKKK')
