"""NumPy companion for the adapted Chinese Understanding Linear Algebra.
Original exercises/data: David Austin, https://understandinglinearalgebra.org/ (CC BY 4.0).
Independent Python/NumPy implementations; data are fetched only when requested.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fractions import Fraction
from scipy.linalg import lu as _lu, null_space
import sympy as sp
BASE = 'https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/'

def rref(A, tol=1e-12, dtype=np.float64):
    """Numerical Gauss-Jordan elimination with partial pivoting; returns a copy."""
    R = np.array(A, dtype=dtype, copy=True)
    m,n = R.shape
    i = 0
    for j in range(n):
        if i == m: break
        k = i + np.argmax(np.abs(R[i:,j]))
        if abs(R[k,j]) <= tol: continue
        R[[i,k]] = R[[k,i]]
        R[i] /= R[i,j]
        for k in range(m):
            if k != i: R[k] -= R[k,j] * R[i]
        i += 1
    R[np.abs(R) <= tol] = 0
    return R

def exact_rref(A):
    """Exact RREF; pass integer/Fraction/string entries, not pre-rounded floats."""
    return sp.Matrix(A).rref()[0]

def LU(A):
    P,L,U = _lu(np.asarray(A, dtype=float))
    return P.T,L,U  # textbook convention P @ A = L @ U

def SVD(A):
    A = np.asarray(A, dtype=float)
    U,s,Vt = np.linalg.svd(A, full_matrices=True)
    Sigma = np.zeros(A.shape)
    np.fill_diagonal(Sigma,s)
    return U,Sigma,Vt.T

def eigenmatrix(A):
    vals,P = np.linalg.eig(A)
    return np.diag(vals), P

def projection(b,basis):
    b = np.asarray(b,dtype=float)
    if len(basis)==0: return np.zeros_like(b)
    B=np.column_stack(basis)
    return B @ np.linalg.lstsq(B,b,rcond=None)[0]

def unit(v):
    v=np.asarray(v,dtype=float); n=np.linalg.norm(v)
    if n == 0: raise ValueError('zero vector')
    return v/n

def gs(basis):
    q=[]
    for v in basis:
        w=np.asarray(v,dtype=float).copy()
        for u in q: w -= (u @ w)*u
        if np.linalg.norm(w)<1e-12: raise ValueError('dependent columns')
        q.append(unit(w))
    return q

def QR(A):
    A=np.asarray(A,dtype=float)
    Q=np.column_stack(gs(A.T)); return Q,Q.T@A

def onesvec(n): return np.ones(n)
def demean(v):
    v=np.asarray(v,dtype=float); return v-v.mean()
def vandermonde(x,k): return np.vander(x,N=k+1,increasing=True)
def plot_model(xhat,data,domain=None):
    data=np.asarray(data); x=data[:,0]; y=data[:,1]
    t=np.linspace(*(domain or (x.min(),x.max())),200)
    plt.scatter(x,y); plt.plot(t,vandermonde(t,len(xhat)-1)@xhat); plt.show()
def list_plot(data, color='blue', size=20, aspect_ratio=None, xmin=None,xmax=None,ymin=None,ymax=None):
    D=np.asarray(data); plt.scatter(D[:,0],D[:,1],c=color,s=size)
    if aspect_ratio is not None: plt.gca().set_aspect(aspect_ratio)
    if xmin is not None or xmax is not None: plt.xlim(xmin,xmax)
    if ymin is not None or ymax is not None: plt.ylim(ymin,ymax)
    plt.show()
def series_plot(v,color):
    plt.plot(np.asarray(v),color=color,marker='o',markersize=2)
def series_pair(a,b):
    series_plot(a,'blue'); series_plot(b,'orange'); plt.show()
def kmeans(data,k):
    data=np.asarray(data,dtype=float)
    rng=np.random.default_rng(); C=data[rng.choice(len(data),k,replace=False)].copy()
    for _ in range(15):
        idx=np.argmin(np.sum((data[:,None,:]-C[None,:,:])**2,axis=2),axis=1)
        for j in range(k):
            if np.any(idx==j): C[j]=data[idx==j].mean(axis=0)
    idx=np.argmin(np.sum((data[:,None,:]-C[None,:,:])**2,axis=2),axis=1)
    return [data[idx==j] for j in range(k)], C, np.mean(np.sum((data-C[idx])**2,axis=1))
def minimalobjective(data,k): return min((kmeans(data,k) for _ in range(10)),key=lambda v:v[2])
def plotclusters(clusters,centroids):
    for c in clusters:
        if len(c): plt.scatter(c[:,0],c[:,1],s=20)
    C=np.asarray(centroids); plt.scatter(C[:,0],C[:,1],c='black',s=50); plt.axis('equal'); plt.show()
def quad_plot(A):
    t=np.linspace(-2,2,100); x,y=np.meshgrid(t,t); A=np.asarray(A)
    z=A[0,0]*x*x+(A[0,1]+A[1,0])*x*y+A[1,1]*y*y
    z=np.where(x*x+y*y<=4,z,np.nan)
    ax=plt.figure().add_subplot(projection='3d'); ax.plot_surface(x,y,z,alpha=.8)
    th=np.linspace(0,2*np.pi,200); v=np.stack([np.cos(th),np.sin(th)])
    ax.plot(*v,np.sum(v*(A@v),axis=0)); plt.show()
def approximate(A,k):
    U,s,Vt=np.linalg.svd(A,full_matrices=False); k=int(k)
    return (U[:,:k]*s[:k])@Vt[:k,:]
def display_matrix(A):
    A=np.asarray(A,dtype=float); scale=max(np.max(np.abs(A)),1e-15); C=A/scale
    rgb=np.stack([np.abs(C),np.maximum(C,0),np.maximum(C,0)],axis=-1)
    plt.imshow(rgb,interpolation='nearest',aspect='equal'); plt.show()
def display_column(A,k): display_matrix(np.asarray(A)[:,[k]])
def display_image(A): plt.imshow(np.clip(A,0,255),cmap='gray',vmin=0,vmax=255); plt.axis('off'); plt.show()
def plot_sv(A): plt.plot(np.linalg.svd(A,compute_uv=False),marker='o'); plt.show()
def outer(u,v): return np.outer(u,v)

def load_data(name):
    """Load the original author's datasets, on demand; requires internet."""
    if name=='dot_similarity':
        events=pd.read_csv(BASE+'events.csv',index_col=0); series=pd.read_csv(BASE+'time-series.csv',header=None)
        d=dict(events=events,series=series)
        for key,col in zip(['veterans','memorial','labor','golden','super'],['Veterans Day','Memorial Day','Labor Day','Golden Globe Awards','Super Bowl']): d[key]=events[col].to_numpy()
        d.update({f's{i+1}':series[j].to_numpy() for i,j in enumerate([0,3,1,2])}); return d
    if name=='k_means': return {'data':pd.read_csv(BASE+'clusters_data.csv',header=None).to_numpy()}
    if name=='pca_ex':
        import random
        rng=random.Random(1); x=demean([2*rng.random() for _ in range(100)]); return {'A':np.stack([x,2*x])}
    if name=='pca_demo':
        df=pd.read_csv(BASE+'pca-demo.csv',index_col=0); A=df.to_numpy().T
        ax=plt.figure().add_subplot(projection='3d'); ax.scatter(*A); plt.show()
        return {'A':A,'df':df,'pca_plot':lambda M:list_plot(np.asarray(M).T,aspect_ratio=1)}
    if name in ('pca_iris','pca_penguins'):
        if name=='pca_iris':
            df=pd.read_csv(BASE+'iris.data'); raw=df.iloc[:,:4]; A=(raw-raw.mean()).to_numpy().T; group='species'
        else:
            df=pd.read_csv(BASE+'penguins.csv').drop(columns=['Unnamed: 0']); raw=pd.read_csv(BASE+'penguins_data.csv').drop(columns=['Unnamed: 0']); A=raw.to_numpy().T; group='Species'
        def pca_plot(M,sex='all'):
            M=np.asarray(M); mask=np.ones(len(df),dtype=bool)
            if sex!='all' and 'Sex' in df: mask=df['Sex'].str.lower().eq(sex.lower()).to_numpy()
            for g in df[group].unique():
                ind=(df[group].eq(g).to_numpy())&mask; plt.scatter(M[0,ind],M[1,ind],label=g)
            plt.axis('equal'); plt.legend(); plt.show()
        def sepal_plot(): pca_plot(df.iloc[:,:2].to_numpy().T)
        return dict(df=df,A=A,data=raw,data_mean=raw.mean().to_numpy(),pca_plot=pca_plot,sepal_plot=sepal_plot)
    if name=='svd_supreme':
        return {k:pd.read_csv(BASE+f,index_col=0) for k,f in [('cases','Rehnquist-cases.csv'),('fivefour','Rehnquist-five-four.csv'),('agreement','rehnquist-agreement.csv')]}
    if name=='svd_compress':
        from PIL import Image
        from urllib.request import urlopen
        from io import BytesIO
        def img(f):
            with urlopen(BASE+f,timeout=30) as r: return np.asarray(Image.open(BytesIO(r.read())).convert('L'))
        letter=pd.read_csv(BASE+'letter.csv',header=None,sep=' '); noise=pd.read_csv(BASE+'noise.csv',header=None)
        return dict(A=letter.to_numpy(dtype=float),letter=letter,noise=noise,image=img('utah-gray.png'),noiseimage=img('new-utah-noise.png'))
    raise ValueError(name)
