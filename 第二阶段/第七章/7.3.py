import time

def timer(func):
    def wrapper(path):
        start_time = time.time()
        func()
        stop_time = time.time()
        with open(path, 'r+') as file:
            file.seek(0, 2)
            file.write(str(stop_time - start_time)+ '\n')

    return wrapper

# index = timer(index)
@timer
def index():
    time.sleep(3)
    print("welcome")

index("log.txt")