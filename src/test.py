from tkinter import Entry   #graphic
from math import pi 
from tkinter import messagebox
import matplotlib.pyplot as plt #graph
import numpy as np
import math
import sys  #max_in
from tkinter import *


def graph_editor(grid=True, grid_N=24):
    plt.ion()  # interactive mode -> figure1 hast ke mitonim bahash taamol konim
    fig, ax = plt.subplots(1)
    ticks = np.linspace(0, 1, grid_N)

    def init_ax(): # har seri miad kol safe ro pak mikone ke betonim chizaye jadid bezarim tosh
        ax.clear()
        ax.set_xlim(0, 1)
        ax.set_xticks(ticks)
        ax.set_xticklabels([])
        ax.set_ylim(0, 1)
        ax.set_yticks(ticks)
        ax.set_yticklabels([])
        if grid:
            ax.grid()

    # node ha ro vorodi migiram
    messagebox.showinfo("HI " , "Place the nodes and press enter")
    print("Place the nodes and press enter")
    init_ax()
    fig.canvas.draw # shoro mikone be keshidan
    nodes_pos = plt.ginput(-1, timeout=-1)  # get all input -> position ha ro migire, arg 1 -> tedad vorodi / arg 2 -> zaman ro limit mikone

    nodes_posx, nodes_posy = zip(*nodes_pos)    # x,y haye node ha ro to 2 ta list joda mirizam 
    nodes = range(len(nodes_pos))   #tedad node ha baraye estefade dar algorithm
    
    root = Tk() #ye window jadid baz mikone baraye vorodi gereftan k
    versiontitle = Label(root, text="input form")  
    versiontitle.pack() 

    k1text = Label(root, text="please insert k (5 <= k =< 15 )Val:")
    k1text.pack()
    k1 = IntVar()  
    k1.set(5)
    k1entry = Entry(root )  #entry yani textfield mizanim ro hamon window root va inke vorodi textfild ro mirize to in
    k1entry.pack()

    j = 5


    def inbalg():
        j = k1entry.get()
        print(k1entry.get())
        root.destroy()  #window ro mibande
        root.quit() #az main loop darmiad
        
    magicbutton = Button(root , text='OK!', command=inbalg)
    magicbutton.pack()

    root.mainloop()
    

    edges = []

    for i in nodes:# ye node asli
        for ang_obj in range(0, j): # har gheta
            reference_angle = 360 / j 
            s_angle = ang_obj * reference_angle#zavie shoro har gheta ro darmiaram az 0 ham shoro mishe , 0 , 60 , 120 ,...(j=6)
            e_angle = s_angle + reference_angle #payan gheta ro mide 60 , 120 , 180 (j=6)
            distance = sys.maxsize
            for k in nodes: #tak tak node ha ro check mikonam nesbat be asli
                dx, dy = nodes_posx[i] - nodes_posx[k], nodes_posy[i]-nodes_posy[k]
                angle_in_radians = math.atan2(dx, dy)#ye zavie mide bar asas 2 noghte
                if angle_in_radians<= 0:
                    angle_in_radians = angle_in_radians + 2*pi  #ye moghe zavie manfi nade miaim + mikonamesh
                angle_in_degrees = angle_in_radians * 180 / pi
                if angle_in_degrees >= s_angle and angle_in_degrees <= e_angle and math.hypot(nodes_posx[i]-nodes_posx[k], nodes_posy[i]-nodes_posy[k]) > 0 and math.hypot(nodes_posx[i]-nodes_posx[k], nodes_posy[i]-nodes_posy[k]) < distance:
                    if(distance!=sys.maxsize):
                        del edges[-1]#har seri ghabli ro pak mikonam age ghablan vorodi gereftam, akharin chizo mire pak mikone
                    distance = math.hypot(nodes_posx[i]-nodes_posx[k], nodes_posy[i]-nodes_posy[k])
                    edges.append((i,k))

    #print(edges)
    fig.canvas.draw()


    init_ax()#harchi ta alan hast ro refresh kon
    for i, j in edges:
        x1, y1 = nodes_pos[i]
        x2, y2 = nodes_pos[j]
        ax.plot([x1, x2], (y1, y2), lw=2, c='k')
    ax.scatter(nodes_posx, nodes_posy, s=30)
    fig.canvas.draw()



    plt.ioff()#dige vorodi jadid nagire

    return nodes, edges,  nodes_pos



if __name__ == '__main__':

    import networkx as nx
    import matplotlib.pyplot as plt

    nodes, edges, nodes_pos = graph_editor()

    G = nx.Graph()  # create graphe mamoli
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    fig, ax = plt.subplots(1)
    nx.draw(G, pos=dict(zip(nodes, nodes_pos)), ax=ax)
    plt.show() #figure 2 ro mide
