

def testit(func, *nkwargs, **kwargs):
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception as diag:
        result = (False, str(diag))
    return result
    
def test():
    funcs = (int, float, str)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print('-'*20)
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)

            if retval[0]:
                print('%s(%s) = ' % (eachFunc.__name__, 'eachVal'), retval[1])
            else:
                print('%s(%s) = Failed:' % (eachFunc.__name__, 'eachVal'), retval[1])

if __name__ == '__main__':
    test()