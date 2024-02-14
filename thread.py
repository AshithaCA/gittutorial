# #threading without class

# import threading
# import time
# a=[1,2,3,4]
# def cube(a):
#     for i in a:
#         print("cube : ",i**3)
#         print(threading.current_thread())
#         time.sleep(1)
# def square(a):
#     for i in a:
#         print("square : ",i**2)
#         print(threading.current_thread())
        
#         time.sleep(1)
# # cube(a)
# # square(a)
# t1=threading.Thread(target=cube,args=(a,))            #creating thread
# t2=threading.Thread(target=square,args=(a,))
# t1.start()                                            #starting thread
# t2.start()
# t1.setName("cube thread")                             #giving name to thread
# t2.setName("square thread")
# # print(threading.enumerate())



#with class
# from threading import Thread
# import time
# class Mythread(Thread):
#     def cube(self,b):
#         for i in b:
#             print("cube of",i,i**3)
#             time.sleep(1)
#     def run(self):
#         for i in range(1,6):
#             print(i)
#             time.sleep(3)
#         print("//////////////")
#         a=(1,2,3,4)
#         self.cube(a)
# t1= Mythread()
# t1.start()



# import threading
# x=0
# def increment(lock):
#     global x
#     for i in range(10):
#         # lock.acquire()
#         x+=1
#         print(x)
#     # print(x,threading.current_thread())
# #     # lock.release()
# def maintask():
#     global x
#     x=0
#     # lock=threading.Lock()
#     t1=threading.Thread(target=increment,args=(lock,))
#     t2=threading.Thread(target=increment,args=(lock))
#     t1.start()
#     t2.start()
#     # t1.join()
#     # t2.join()
# # for i in range(10):
# #     maintask()
# #     print("iteration {0}::x={1}".format(i,x))

# # increment()
# maintask()
# # print("_________")
# # increment()

