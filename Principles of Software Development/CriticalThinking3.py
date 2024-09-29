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

    # Display pages
    print(f'Pages:')
    for item in range(len(pages)):
        print(f'    Page {item+1}: {pages[item]}')
    else:
        print(f'\n')
    
    # Enter sequence
    print('Enter the sequence of the pages by entering the page number. Enter "f" to finsh the sequence.')
    sequence = []
    step = 1
    while True:
        try:
            sequence_step = input(f'Enter page name of step {step}: ')
            if sequence_step == 'f':
                break 
            elif not sequence_step in pages:
                print('That is not an option.')
            else:
                sequence.append(sequence_step)
                step += 1
        except ValueError:
            print('An error occured.')

    print(f'\n########################################')
    print(f'Sequence of the pages:')
    for step in range(len(sequence)):
        print(f'    Step {step+1}: {sequence[step]}')
    else:
        print(f'########################################\n')

if __name__ == "__main__":
    Prototype()