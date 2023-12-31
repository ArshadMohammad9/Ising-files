import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def lattice(args):
    rows, columns = args
    lattice=np.zeros((rows,columns))
    for i in range (rows):
        for j in range (columns):
            lattice[i][j]=(2*np.random.randint(0,2)-1)
    lattice[rows-1, :]=lattice[0, :]
    lattice[:,columns-1]=lattice[:,0]
    return lattice

def view(args):
    lattice = args
    im = plt.imshow(lattice, cmap='magma')
    plt.colorbar(im)
    plt.show()
     
def m(args):
    lattice = args
    m = 0
    for i in range (len(lattice)):
        for j in range (len(lattice)):
            m +=lattice[i][j]
    return m

def E(args):
    lattice, J = args
    dub = np.zeros((len(lattice)+2, len(lattice)+2))
    for i in range (len(lattice)):
        for j in range (len(lattice)):
            dub[i+1][j+1]=lattice[i][j]
            
    dub[:,0]=dub[:,1]
    dub[:,len(lattice)+1]=dub[:,len(lattice)]
    dub[0,:]=dub[1,:]
    dub[len(lattice)+1,:]=dub[len(lattice),:]
    dub[0][0]=0
    dub[0][len(lattice)+1]=0
    dub[len(lattice)+1][0]=0
    dub[len(lattice)+1][len(lattice)+1]=0
    
    E=np.zeros((len(lattice)+2, len(lattice)+2))
    for i in range (1,len(lattice)+1):
        for j in range(1,len(lattice)+1):
            S_i = dub[i][j]
            S_j = dub[i][j-1]+dub[i][j+1]+dub[i-1][j]+dub[i+1][j]
            E[i][j]= -J* S_i*S_j               
    energy = np.sum(E)       
    return energy

def MCC1(args):
    lattice, T, J = args
    E_0 = E((lattice,J))
    b = 1/T
    dub = lattice
    for i in range (len(lattice)):
        for j in range (len(lattice)):
            dub[i][j]=-1*lattice[i][j]
            E_dub = E((dub,J))
            
            if (E_0 > E_dub):
                lattice = dub
                E_0 = E_dub
            else:
                exp = np.exp(-b*(E_dub-E_0))
                x = np.random.uniform(0,1)
                if (x<exp):
                    lattice = dub
                    E_0 = E_dub
                else:
                    lattice = lattice
                    E_0 = E_0
    return lattice

def MCC(args):
    lattice, T, J = args
    E_0 = E((lattice,J))
    b = 1/T
    dub = lattice
    for i in range (len(lattice)):
        for j in range (len(lattice)):
            a = np.random.randint(0,len(lattice))
            b = np.random.randint(0,len(lattice))
            dub[a][b]=-1*lattice[a][b]
            E_dub = E((dub,J))
            
            if (E_0 > E_dub):
                lattice = dub
                E_0 = E_dub
            else:
                exp = np.exp(-b*(E_dub-E_0))
                x = np.random.uniform(0,1)
                if (x<exp):
                    lattice = dub
                    E_0 = E_dub
                else:
                    lattice = lattice
                    E_0 = E_0
    return lattice

def equi(args):
    lattice, T, J, N = args
    for i in range (N):
        lattice = MCC((lattice, T, J))
    print("equi done")
    return lattice

