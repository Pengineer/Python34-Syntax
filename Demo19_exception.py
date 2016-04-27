# 异常
'''
Python标准异常总结:
AssertionError  断言语句（assert）失败
AttributeError  尝试访问未知的对象属性
EOFError    用户输入文件末尾标志EOF（Ctrl+d）
FloatingPointError  浮点计算错误
GeneratorExit   generator.close()方法被调用的时候
ImportError 导入模块失败的时候
IndexError  索引超出序列的范围
KeyError    字典中查找一个不存在的关键字
KeyboardInterrupt   用户输入中断键（Ctrl+c）
MemoryError 内存溢出（可通过删除对象释放内存）
NameError   尝试访问一个不存在的变量
NotImplementedError 尚未实现的方法
OSError 操作系统产生的异常（例如打开一个不存在的文件）
OverflowError   数值运算超出最大限制
ReferenceError  弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象
RuntimeError    一般的运行时错误
StopIteration   迭代器没有更多的值
SyntaxError Python的语法错误
IndentationError    缩进错误
TabError    Tab和空格混合使用
SystemError Python编译器系统错误
SystemExit  Python编译器进程被关闭
TypeError   不同类型间的无效操作
UnboundLocalError   访问一个未初始化的本地变量（NameError的子类）
UnicodeError    Unicode相关的错误（ValueError的子类）
UnicodeEncodeError  Unicode编码时的错误（UnicodeError的子类）
UnicodeDecodeError  Unicode解码时的错误（UnicodeError的子类）
UnicodeTranslateError   Unicode转换时的错误（UnicodeError的子类）
ValueError  传入无效的参数
ZeroDivisionError   除数为零

以下是 Python 内置异常类的层次结构：
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
      +-- StopIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
'''

# 异常处理模块：try-except
try:
  f = open('不存在的文件.txt')
  f.close()
  sum = 1 + '1'
except OSError as reason:
  print('文件打开失败，错误原因：' + str(reason))
except TypeError as reason:
  print('类型错误，错误原因：' + str(reason))

# 如果并不知道异常的类型，或则想和Java中的Exception一样，接受所有异常，可以这样:
# except 后面什么都不接
# 但是，强烈不建议这么干
try:
  f = open('不存在的文件.txt')
  f.close()
  sum = 1 + '1'
except:
  print('文件操作失败，错误原因：' + str(reason))

# try-finally语句
'''
try:
  检测范围
except Exception[as reason]:
  出现异常（Exception）后的处理代码
finally:
  无论如何都会被执行的代码
'''

# 异常的抛出：类似Java中的Throw new RuntimeException()
raise my_exception
raise my_exception('抛出异常')


