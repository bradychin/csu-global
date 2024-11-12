password = 'pass'
pw = ''
authorized = False
count = 0
max_attempt = 5

while pw != password:
    count += 1
    if count > max_attempt:
        break
    if count == 3: 
        continue
    pw = input(f'{count}: what is the password? ')
else:
    authorized = True

print('logged in' if authorized else 'na man')


companies = ('apple', 'amazon', 'tesla')

for company in companies:
    if company == 'apple':
        continue
    if company == 'amazon':
        break
    print(company)
else:
    print('thats all the companies')

