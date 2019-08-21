__all__ = ['money', 'read1', 'change']





money = 0
def read1():
    print('spam模块.read1：', money)

def read2():
    print('spam模块.read2')
    read1()

def change():
    global money
    money = 1
    print(money)


if __name__ == '__main__':
    print("脚本执行")
    read1()
