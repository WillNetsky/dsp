import sys
import csv


def read_data(filename):
    f = open(filename, 'rt')
    reader = csv.reader(f)
    return reader


def print_first_three_keys(d):
    for i in range(3):
        value = d[d.keys()[i-1]]
        print('{0}:{1}'.format(str(d.keys()[i-1]), str(value)))


def question_six(reader):
    faculty = dict()
    for row in reader:
        full_name = row[0].split()
        last_name = full_name[-1]
        for item in row[1:]:
            item.strip()
        faculty[last_name] = row[1:]

    print('Question Six:')
    print_first_three_keys(faculty)


def question_seven(reader):
    faculty = dict()
    for row in reader:
        full_name = row[0].split()
        full_name = tuple(full_name)
        for item in row[1:]:
            item.strip()
        faculty[full_name] = row[1:]

    print('Question Seven:')
    print_first_three_keys(faculty)


def question_eight(reader):
    faculty = dict()
    for row in reader:
        full_name = row[0].split()
        full_name = tuple(full_name)
        for item in row[1:]:
            item.strip()
        faculty[full_name] = row[1:]

    print('Question Eight:')
    for key in sorted(faculty.keys(), key = lambda x: x[-1])[:3]:
        print(str(key) + ' : ' + str(faculty[key]))



def main(argv):
    question_six(read_data('faculty.csv'))
    question_seven(read_data('faculty.csv'))
    question_eight(read_data('faculty.csv'))


if __name__ == '__main__':
    main(sys.argv)