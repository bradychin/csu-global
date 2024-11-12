def main():
    kitten('meow', 'grr', 'purr')

def kitten(*args):
    if len(args):
        for s in args: 
            print(s)
    else:
        print('meow')

if __name__ == '__main__':
    main()