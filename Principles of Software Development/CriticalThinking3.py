import os
os.system('cls' if os.name == 'nt' else 'clear')

class Prototype:
    # Prompt number of pages
    while True:
        try: 
            number_of_pages = int(input('Enter the number of pages in the prototype: '))
            if number_of_pages <=0:
                print(f'Enter at least 1 page.\n')
            else: 
                break
        except ValueError:
            print(f'Please enter a number.\n')

    # Prompt name of page
    pages = []
    print(f'\n')
    for page in range(number_of_pages):
        page_name = input(f'Enter the name of page {page+1}: ')
        pages.append(page_name)
    else:
        print(f'\n')

    # Display in sequence
    print(f'Sequence of pages:')
    for item in range(len(pages)):
        print(f'    Page {item+1}: {pages[item]}')
    else:
        print(f'\n')

if __name__ == "__main__":
    Prototype()