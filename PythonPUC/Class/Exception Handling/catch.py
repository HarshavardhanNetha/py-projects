try:
    import randm
except SyntaxError:
    print('Syntac Error')
except IndexError:
    print('Index Error')
except ImportError:
    print('Import Error')
