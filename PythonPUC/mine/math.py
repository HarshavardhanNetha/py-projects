a=int(input("Root1:"))
b=int(input("Root2:"))
c=int(input("Root3:"))
d=int(input("Root4:"))
e=int(input("Root5:"))
s1=-(a+b+c+d+e)
s2=(a*b)+(b*c)+(c*d)+(d*e)+(e*a)
s3=-((a*b*c)+(b*c*d)+(c*d*e)+(d*e*a)+(e*a*b))
s4=(a*b*c*d)+(b*c*d*e)+(c*d*e*a)+(d*e*a*b)+(e*a*b*c)
s5=-(a*b*c*d*e)
print(s1,"\n",s2,"\n",s3,"\n",s4,"\n",s5)
print("The eqn is x^5+{}x^4+{}x^3+{}x^2+{}x+{}".format(s1,s2,s3,s4,s5))