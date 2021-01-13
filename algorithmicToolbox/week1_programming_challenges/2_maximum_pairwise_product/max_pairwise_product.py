# python3


def max_pairwise_product(numbers):
    if numbers[0] > numbers[1]:
        max1 = numbers[0]
        max2 = numbers[1]
    else:
        max1 = numbers[1] 
        max2 = numbers[0]
    for number in numbers[2:]:
        if number > max1:
            max2 = max1
            max1 = number
        elif number > max2:
            max2 = number
    return max1 * max2

def max_pairwise_product_starter(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def test(testList):
    import time
    for tst in testList:
        print('Test:', tst.get('title'))
        start = time.time()
        try:
            output = max_pairwise_product(tst.get('numbers'))
        except IndexError:
            end = time.time()
            print('IndexError exception occured!')
            print('Time elapsed: ',end - start, 'seconds.')
        except:
            end = time.time()
            print('Exception occured!')
            print('Time elapsed: ',end - start, 'seconds.')
            end = time.time()
        else:
            end = time.time()
            if output == tst.get('expected'):
                print('Test passed!')
                print('Time elapsed: ',end - start, 'seconds.')
            else:
                print('Test failed!\nExpected:', tst.get('expected'), '\n  Result:', output)
                print('Time elapsed: ',end - start, 'seconds.')

def testSuite():
    test([
        {
            'title':'Simple input, size 2, sorted',
            'numbers':[1, 2],
            'expected': 2
        },
        {
            'title':'Simple input, size 3, unsorted',
            'numbers':[2, 1, 3],
            'expected':6
        },
        {
            'title':'Input size 10, unsorted',
            'numbers':[2, 5, 1, 9, 4, 7, 3, 6, 8, 10],
            'expected':90
        }, 
        {
            'title':'Repeated max number',
            'numbers':[9, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            'expected':81
        },
        {
            'title':'Size 2, large numbers',
            'numbers':[100000, 200000],
            'expected': 100000 * 200000
        }, 
        {
            'title':'Max size', 
            'numbers':[i for i in range(200001)],
            'expected':199999*200000
        },
        {
            'title':'Size 0 - should throw exception',
            'numbers':[],
            'expected':0
        }
    ])

def stressTest(max_size, max_number):
    import random
    random.seed(1)
    for i in range(100000):
        print('Running test no.', i)
        n = random.randint(2, max_size)
        numbers = [random.randint(2, max_number) for _ in range(n)]
        try:
            result1 = max_pairwise_product_starter(numbers)
        except:
            print('Exception thrown with starter algorithm')
            return
        else:
            try:
                result2 = max_pairwise_product(numbers)
            except:
                print('Exception thrown with new algorithm')
                return
            else:
                if result1 == result2:
                    print('OK')
                else:
                    print('Not OK:\nTest:', numbers, '\n\nalg1:', result1, '\n\nalg2:', result2)
                    return




if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

    # testSuite()
    # stressTest(200, 200000)
