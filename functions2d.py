import torch
import numpy as np

def real5(x):
    x1 = x[:, 0]
    x2 = x[:, 1]
    return torch.exp(-x1)*(x1+x2**3)

def trial5(f, x1, x2):
    #x1 = x[:, 0]
    #x2 = x[:, 1]
    x = torch.cat((x1.view(-1, 1), x2.view(-1, 1)), 1)
    x2_3 = x2**3
    e1 = np.exp(-1.)
    ex1 = torch.exp(-x1)
    
    A = (1-x1)*x2_3+x1*(1+x2_3)*e1+(1-x2)*x1*(ex1-e1)+x2*((1+x1)*ex1-(1-x1+2*x1*e1))
    return A + x1*(1-x1)*x2*(1-x2)*f(x).t()

def diff5(t, x, gx):
    t0 = t[:, 0]
    t1 = t[:, 1]
    delta2x = gx[1][0] + gx[1][1]
    return delta2x - torch.exp(-t0)*(t0 - 2 + t1**3 + 6 * t1)

int5=(0, 1, 0, 1)

degree5 = 2

def real6(x, a=3):
    x1 = x[:, 0]
    x2 = x[:, 1]
    return torch.exp(-(a*x1+x2)/5)*torch.sin((a*x1)**2+x2)

def trial6(f, x1, x2, a=3):
    x = torch.cat((x1.view(-1, 1), x2.view(-1, 1)), 1)
    a2 = a**2
    x1_2 = x1**2
    eax5 = torch.exp(-a*x1/5)
    ey5 = torch.exp(-x2/5)
    ea5 = np.exp(-a/5)
    e15 = np.exp(-1./5)
    c1 = ey5*torch.sin(x2)
    c2 = ey5*torch.sin(a2+x2)*ea5
    c3 = eax5*torch.sin(a2*x1_2)-x1*np.sin(a2)*ea5
    c4 = (eax5*torch.sin(a2*x1_2+1)-(1-x1)*np.sin(1)-x1*ea5*np.sin(a2+1))*e15
    
    A = (1-x1)*c1+x1*c2+(1-x2)*c3+x2*c4
    return A + x1*(1-x1)*x2*(1-x2)*f(x).t()

def diff6(t, x, gx, a=3):
    t0 = t[:, 0]
    t1 = t[:, 1]
    a2 = a**2
    delta2x = gx[1][0] + gx[1][1]
    angle = (a*t0)**2+t1
    return delta2x - torch.exp(-(a*t0 + t1)/5)*((-4*a**3*t0/5-2/5+2*a2)*torch.cos(angle)+(1/25-1-4*(a2*t0)**2+a2/25)*torch.sin(angle))

int6=(0, 1, 0, 1)

degree6 = 2

# not complete

def real7(x):
    x1 = x[:, 0]
    x2 = x[:, 1]
    return x2**2*torch.sin(x1*np.pi)

def trial7(f, x1, x2):
    x = torch.cat((x1.view(-1, 1), x2.view(-1, 1)), 1)
    x_1 = Variable(torch.cat((torch.Tensor(x1), torch.Tensor(np.ones(len(x1)))), 1))
    print(x_1)
    B = 1
    return B + x1*(1-x1)*x2*(f(x) - f(x_1) - 1)

def diff7(t, x, gx):
    t0 = t[:, 0]
    t1 = t[:, 1]
    delta2x = gx[1][0] + gx[1][1]
    return delta2x - (2 - (np.pi * t1)**2) * torch.sin(np.pi * t0)

int7=(0, 1, 0, 1)

degree7 = 2

def real8(x):
    return torch.exp(-x/5)*torch.sin(x)

def trial8(f, x1, x2):
    x = torch.cat((x1.view(-1, 1), x2.view(-1, 1)), 1)
    return x*np.sin(1.)*np.exp(-1./5)+x*(1-x)*f(x)

def diff8(t, x, gx):
    t0 = t[:, 0]
    t1 = t[:, 1]
    delta2x = gx[1][0] + gx[1][1]
    return delta2x + x * gx[0][1] - torch.sin(np.pi * t0) * (2 - (np.pi * t1)**2 + 2 * t1**3 * torch.sin(np.pi * t0))

int8=(0, 1, 0, 1)

degree8 = 2

function={
'p5':real5,
'p6':real6,
'p7':real7,
'p8':real8
}

trial={
'p5':trial5,
'p6':trial6,
'p7':trial7,
'p8':trial8
}

interval={
'p5':int5,
'p6':int6,
'p7':int7,
'p8':int8
}

diff_eq={
'p5':diff5,
'p6':diff6,
'p7':diff7,
'p8':diff8
}

degree={
'p5':degree5,
'p6':degree6,
'p7':degree7,
'p8':degree8
}
