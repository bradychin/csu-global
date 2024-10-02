def main():
    infile = open('/Users/bradychin/Library/Mobile Documents/com~apple~CloudDocs/University/CSU Global/Principles of Programming/Lectures/Module 2/11 File IO/lines.txt', 'rt')
    outfile = open('/Users/bradychin/Library/Mobile Documents/com~apple~CloudDocs/University/CSU Global/Principles of Programming/Lectures/Module 2/11 File IO/line-copy.txt', 'wt')
    for line in infile: 
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone')

if __name__ == '__main__': main()