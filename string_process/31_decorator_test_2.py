# 装饰器本身就是一个函数，不会修改被修饰函数里面的代码，不能修改函数的调用方式。这是原则
# 可以理解为在一个函数外面加另外一个函数，为其他函数添加附加功能
# 应用场景，例如, 不能修改函数体
# 装饰器 = 高阶函数 + 函数嵌套 + 闭包
# 带固定参数的装饰器
import time

def deco(f):                # 高阶函数，以函数名作为参数, 参数就是要装饰的函数
    def wrapper(a, b):       # 函数嵌套,这个函数要和需要装饰的函数参数一致
        start_time = time.time()
        res = f(a, b)              # 这里执行要装饰的函数
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" % execution_time)
        return res
    return wrapper          # 返回值是嵌套函数的函数名

@deco
def f(a, b):
    print("be on")
    time.sleep(1)
    print("result is %d" % (a+b))   # 执行完这一步，跳转到def wrapper(a,b)里面的f(a,b)
    return "f函数返回值"

if __name__ == '__main__':
    res = f(3, 4)            # 此处设置断点，查看函数如何执行,顺序是先执行deco()函数，在执行f(a,b)之前跳转到def f(a,b)函数里面
    print(res)
