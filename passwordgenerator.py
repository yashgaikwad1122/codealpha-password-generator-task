import random
import string

if __name__ == '__main__':
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.punctuation
    s4=string.digits
    plen = int(input("enter password range "))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    print("your password is:")
    print(" ".join(random.sample(s,plen)))
   # print( " ".join(s[0 : plen])) other method
