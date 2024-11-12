def main():
    kitten(Buffy = 'meow', Zilla = 'grr', angel = 'rawr')

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print(f'Kitten {k} says {kwargs[k]}')
    else: 
        print('meow')

if __name__ == '__main__':
    main()