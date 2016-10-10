import sys, socket

#try:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1',8888))
s.send('HELLO padmanabhan.ka \n')
done = 'DONE'
math = 'MATH'
#data = s.recv(1024)
#print data
#print data.split(" ")
#method(data)
#def method(data):
#fin = done in data
while s.recv(1024).find('MATH')!=-1:

    # loop = math in data
     #data = s.recv(1024)
     #fin = done in data
	  #while fin != True:
     #data = s.recv(1024)
    # fin = done in data
     #if fin==True:
      #  print data[5:]
       # s.close()

     #if loop==True:
	    data = s.recv(1024)
        print data
        a = data[13:]
        #if a=='\0':   
        b = a.rstrip()
        c = b.split(" ")
        #print data
        #print a
        #print b
        #print c
        #print c[0]
        #print c[1]
        #print c[2]
        #print c[3]
        x = int(c[1])
        y = int(c[3])
        z = c[2]
        if z=="+":
           p = str(x+y)
           q = "NAME padmanabhan.ka ANSWER "+p+"\n"
           s.send(q)
           #method (s.recv(1024))
        elif z=="-":
           p = str(x-y)
           q = "NAME padmanabhan.ka ANSWER "+p+"\n"
           s.send(q)
           #method (s.recv(1024))
        elif z=="*":
           p = str(x*y)
           q = "NAME padmanabhan.ka ANSWER "+p+"\n"
           s.send(q)
           #method (s.recv(1024))
        elif z=="/":
		   if y != 0:
             p = str(x/y)
             q = "NAME padmanabhan.ka ANSWER "+p+"\n"
             s.send(q)
             #method (s.recv(1024))
			 
print s.recv(1024)[5:]
s.close()
