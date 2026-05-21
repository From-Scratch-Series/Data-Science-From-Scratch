from typing import Union, List, Optional, Dict, Iterable, Tuple, Callable

def add(a,b): return a+b

try:
    add(3,'a')
except TypeError:
    print("cannot add an int to a str")


def add_with_type(a: int, b: int) -> int: return a+b


def ugly_func(value: List[int], operation: Union[str, int,bool, float]) -> int: 
    return 0

#default list type, but allows any type of element inside
def total(a:list) -> float:
    return sum(a)

#if we wanted the list of specific type
def total_float(a:List[float]) -> float:
    return sum(a)

a: List[int] = [] #default is [], takes list of ints
b: Optional[float] = None #either None or float, default is None

Department: Dict['str', 'int'] = {'ECE': 1, 'CSE':2, 'PHY': 2}


#both list and generators are iterables
lazy = True
if lazy:
    evens: Iterable[int] = (x for x in range(10) if x%2==0) #generator
else:
    # evens = ['a','b'] #not allowed since types were declared
    evens = [0,2,4,6,8]

triple_engine: Tuple[str, int, str] = ('a',3,'e')

def hof(repeater: Callable[[str, int],str],s: str) -> str:
    return repeater(s,2)

