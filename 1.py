class MyClass(object):
	author = 'wangyongcun'
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def func(self):
		print(self.name, self.age)
		
	def func2(self, args):
		print(args)
		
	@classmethod
	def class_func(cls):
	    print('class_func')
		
	@staticmethod
	def static_func():
	    print('static_func')
		
	@property
	def property_func(self):
	    print('property')
		
		
		
class TestClass(object):
	def __init__(self):
		pass
		
	def func(self):
		print(123)


class HomeClass(object):
    def __init__(self, name):
        self.name = name

    def func(self):
        print(self.name)
