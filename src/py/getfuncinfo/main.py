import linenotest


@linenotest.linenumber
def testspam(index, msg='empty'):
    print('Here is a testspam function. %d %s' % (index, msg))


if __name__ == '__main__':
    testspam(100, msg='1st')
    for i in range(1, 3):
        testspam(i, msg='2nd')
    testspam(index=99)
