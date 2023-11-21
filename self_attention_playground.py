import torch
import torch.nn.functional as F


# The mathematical trick of self-attention:

# Setup
torch.manual_seed(42)
B,T,C = 4,8,2 # batch, time, channels
x = torch.randn(B,T,C)
print(x.shape)

# Version 1:

# We want x[b,t] = mean_{i<=t} x[b,i]
xbow = torch.zeros((B,T,C))
for b in range(B):
    for t in range(T):
        xprev = x[b,:t+1] # (t,C)
        xbow[b,t] = torch.mean(xprev, 0)


print(x[0])
print(xbow[0])

# End of version 1.


# Side note:
torch.manual_seed(42)
a = torch.tril(torch.ones(3,3))
a = a / torch.sum(a, 1, keepdim=True)
b = torch.randint(0,10,(3,2)).float()
c = a @ b
print('a=')
print(a)
print('b=')
print(b)
print('c=')
print(c)

# End of side note.


# Version 2:
wei = torch.tril(torch.ones(T, T))
wei = wei / wei.sum(1, keepdim=True)
xbow2 = wei @ x # (B, T, T) @ (B, T, C) ---> (B, T, C)
print("Are xbow and xbow2 the same? -> ", torch.allclose(xbow, xbow2))

# End of version 2.


# Version 3: using Softmax
tril = torch.tril(torch.ones(T,T))
wei = torch.zeros((T,T))
wei = wei.masked_fill(tril == 0, float('-inf'))
wei = F.softmax(wei, dim=-1)
xbow3 = wei @ x
print("Are xbow/xbow2 equal to xbow3? -> ", torch.allclose(xbow, xbow3))

# End of Version 3.