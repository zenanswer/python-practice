File list
====

-   calculateattribute.py - usage of \@property, getter only
-   propertytest.py - usage of \@property, with setter and deleter
-   propertytest2.py - usage of class.\_\_setattr\_\_
-   simpledescriptor.py - a simple descriptor for type checking
-   propertydescriptor.py - usage of data descriptor for type checking on a class
-   cachedproperty.py - usage of non-data descriptor on a class method



Data Descriptor (资料描述)
====

[Descriptor-HOW-TO-Guide @ PyZh](http://pyzh.readthedocs.io/en/latest/Descriptor-HOW-TO-Guide.html)

[Python 黑魔法 --- 描述器（descriptor） 人世间@简书](http://www.jianshu.com/p/250f0d305c35)

常用装饰器： @staticmethod, @classmethod, @property

>对于对象来说，关键在于object.\_\_getattribute\_\_()，它将b.x转为type(b).\_\_dict\_\_\['x'\].\_\_get\_\_(b, type(b))。这种实现依据这样的一个优先链：资料描述符优先于实例变量，实例变量优先于非资料描述符，如果对象包含\_\_getattr\_\_()方法，那么这个方法 (\_\_getattr\_\_())的访问优先级最低。完整的C实现在Objects/object.c中PyObject_GenericGetAttr()。
>
>而对于类来讲，关键之处在于type.\_\_getattribute\_\_()方法，它将B.x转换为B.\_\_dict\_\_\['x'\].\_\_get\_\_(None, B)。
>
>[【译】Python描述符指南](https://harveyqing.gitbooks.io/python-read-and-write/content/python_advance/python_descriptor.html)
