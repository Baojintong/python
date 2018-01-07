import threading

#学生类
class Student:
    def __init__(self,name):
        self.name=name
    def setName(self,name):
        self.__name=name
    def sayHello(self):
        print('你好%s同学'%self.name)

# 创建全局ThreadLocal对象:
local_school=threading.local()

def process_student():
    # 获取当前线程关联的student:
    std=local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
