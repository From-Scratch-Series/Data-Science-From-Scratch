assert 1+1 == 2, '1+1 should be 2' #with AssertionError msg

def smallest_item(list):
    assert list, "empty list, please add atleast 1 element in the list" #since, [] is a falsy value hence empty list will raise AssertError
    return min(list)

assert smallest_item([2,3,5,1,0,-1]) == -1
assert smallest_item([])