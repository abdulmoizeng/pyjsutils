
from pyjsutils import Timer

timer = Timer()
def fn():
    print('Python is not JS')
timer.setTimeout(fn, 3.0)

timer2 = Timer()
timer2.setClearTimer()