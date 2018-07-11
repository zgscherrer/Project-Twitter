import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def get_labels():
    file = open('labels.txt','r').read()
    list_names = file.split('\n')
    names = []

    for name in list_names:
        name = name.strip('@')
        names.append(name)  

    return names

def animate(i):

    names= get_labels()

    pullData = open("position_1.txt","r").read()
    dataArray = pullData.split('\n')
    x_position_1 = []
    y_position_1 = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            x_position_1.append(int(x))
            y_position_1.append(int(y))
    
    
    pullData = open("position_2.txt","r").read()
    dataArray = pullData.split('\n')
    x_position_2 = []
    y_position_2 = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            x_position_2.append(int(x))
            y_position_2.append(int(y))

    pullData = open("position_3.txt","r").read()
    dataArray = pullData.split('\n')
    x_position_3 = []
    y_position_3 = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            x_position_3.append(int(x))
            y_position_3.append(int(y))

    pullData = open("position_4.txt","r").read()
    dataArray = pullData.split('\n')
    x_position_4 = []
    y_position_4 = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            x_position_4.append(int(x))
            y_position_4.append(int(y))
            
    pullData = open("position_5.txt","r").read()
    dataArray = pullData.split('\n')
    x_position_5 = []
    y_position_5 = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            x_position_5.append(int(x))
            y_position_5.append(int(y))

    ax1.clear()
    
    ax1.plot(x_position_1,y_position_1,label=names[0])
    ax1.plot(x_position_2,y_position_2,label=names[1])
    ax1.plot(x_position_3,y_position_3,label=names[2])
    ax1.plot(x_position_4,y_position_4,label=names[3])
    ax1.plot(x_position_5,y_position_5,label=names[4])
    plt.legend(bbox_to_anchor=(0.2, 1), loc=2, borderaxespad=1)
    plt.xlabel('Time in Seconds',fontsize=16)
    plt.ylabel('# of Tweet Mentions / 20k ',fontsize=16)
    plt.title('A Tale of Twitter Mentions',fontsize=20,fontweight='bold')

names=[]
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ani = animation.FuncAnimation(fig, animate,interval=1000)


plt.show()
