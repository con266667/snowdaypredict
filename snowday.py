from sklearn import tree

#features = [avg temp ,snow, rain, max wind, high, low]
features = [[-4, 15, 0, 39, 0, -8], [-1, 14, 0, 52, 0, -7], [-16, 0, 0, 43, 0, -8], [-15, 0, 0, 37, 0, -7], [-9, 0, 0, 9, 0, -8],
[14, 0, 2, 31, -1, -7], [10, 0, 3, 33, -1, -10], [0, 0, 13, 33, -1, -9], [7, 0, 10, 6, 0, -7], [8, 1, 0, 54, 0, -8], 
[-2, 1, 0, 46, 0, -9], [1, 12, 8, 56, 0, -9], [1, 4, 0, 54, -1, -8], [1, 0, 0, 13, 0, -7], [5, 0, 1, 52, 0, -7], 
[-3, 4, 0, 28, 1, -6], [-3, 0, 0, 15, 3, -5,], [0, 0, 5, 33, 3, -4], [5, 0, 0, 44, 3, -4], [4, 0, 0, 9, 2, -5], 
[-3, 1, 0, 67, 1, -6], [-4, 0, 0, 28, 1, -7], [-6, 13, 0, 22, 1, -7]]

#snowday 1 = yes, 0 = no
labels = [0, 1, 0, 0, 0, 
0, 0, 1, 1, 0, 
0, 1, 1, 0, 0, 
0, 0, 0, 0, 0,
0, 0, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

avgtemp = input("What's the average temperature?")
snow = input("How much snow?")
rain = input("How much rain?")
maxwind = input("What's the max wind?")
high = input("What's the average high?")
low = input("What's the average low?")

prediction = clf.predict([[avgtemp, snow, rain, maxwind, high, low]])

if (prediction == 1):
    print("It's gonna be a snow day!!!!! ... well i think")
    print('  _________ _______   ________  __      __  ________      _____ _____.___.  _.')
    print(' /   _____/ \      \  \_____  \/  \    /  \ \______ \    /  _  \\__  |   |   |')
    print(' \_____  \  /   |   \  /   |   \   \/\/   /  |    |  \  /  /_\  \/   |   |   |')
    print(' /        \/    |    \/    |    \        /   |    `   \/    |    \____   |  \|')
    print('/_______  /\____|__  /\_______  /\__/\  /   /_______  /\____|__  / ______|  __')
    print('        \/         \/         \/      \/            \/         \/\/         \/')
else :
    print("fuka shiste, it not be snow day :(")
