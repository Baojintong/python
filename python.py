# 除了使用type()创建类以外，要控制类的创建行为还可以使用 metaclass
# 正常使用顺序 1.定义类 2.创建对象
# 元类的使用顺序 1.定义元类 2.创建类 3.创建对象
# 可以进行类的动态创建


# 我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：

# 规范的命名方法
class ListMetaclass(type):  # metaclass是类的模板，所以必须从`type`类型派生：
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，
# 传入关键字参数metaclass：
class MyList(list, metaclass=ListMetaclass):
    pass


# 指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
# 在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

# __new__()方法接收到的参数依次是：
#
# 1.当前准备创建的类的对象；
#
# 2.类的名字；
#
# 3.类继承的父类集合；
#
# 4.类的方法集合。

# 这样我们就在自己的List里面添加了add方法
L = MyList()
L.add(1)
print(L)  # [1]

# 普通list是没有add方法的--s是使用append和insert进行插入的
