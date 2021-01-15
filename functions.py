# Your code goes here
def challenge_1(_input):
    _min = float('inf')
    for n in _input:
        if n < _min and n >= 0:
            _min = n
    return _min

def challenge_2(_input):
    import re
    nums = {'one': 1, 'two': 2, 'three': 3}
    ns = []

    c = re.sub(r'[!?\.,]+', ' ', _input)
    c = re.sub(r'\s+', ' ', c)
    c = c.lower()

    for token in c.split():
        if token in nums:
            ns.append(nums[token])

    return ns

def challenge_3(_input):
    return list(filter(lambda n: n % 2 == 1, _input))