str="google.com"
d=dict()
for c in str:
    if c in d:
        d[c]=d[c]+1
    else:
        d[c]=1
print(d)