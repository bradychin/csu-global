def main():
    x = kitten()
    print(type(x), x)

def kitten():
    print('meow')
    return dict(x = 42, y = 43, z = 52)

if __name__ == '__main__':
    main()