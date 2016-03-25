import pandas as pd
import sys


def main(argv):
    faculty = pd.read_csv('faculty.csv')
    faculty[' email'].to_csv('emails.csv', index=False)

if __name__ == '__main__':
    main(sys.argv)

