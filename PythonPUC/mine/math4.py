a=int(input("Root1:"))
b=int(input("Root2:"))
c=int(input("Root3:"))
d=int(input("Root4:"))
s1=-(a+b+c+d)
s2=(a*b)+(b*c)+(c*d)+(d*a)
s3=-((a*b*c)+(b*c*d)+(c*d*a)+(d*a*b))
s4=(a*b*c*d)
print(s1,"\n",s2,"\n",s3,"\n",s4)
print("The eqn is x^4+{}x^3+{}x^2+{}x+{}".format(s1,s2,s3,s4))
