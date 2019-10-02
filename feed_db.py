#!/usr/bin/env python
# coding: utf-8
"""
Feed the database
"""


import csv
import os
import db_handler


def populate_fede(file_path, dbh, category, year):
    """
    Parse the input file sorted by age and feed the federation table.
    :param file_path:
    :param dbh:
    :param category:
    :param year:
    """
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Codes Fédé'] != "":
                dbh.create_federation((row['Codes Fédé'],
                                       row['Fédérations françaises agréées en ' + year],
                                       category))



def populate_by_age(file_path, dbh, year):
    """
    Parse the input file sorted by age and feed the by_age table.
    :param file_path:
    :param dbh:
    :param year:
    """
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        code_fede = 0
        for row in reader:
            if row['Codes Fédé'] != "":
                code_fede = row['Codes Fédé']
            if row['Fédérations françaises agréées en ' + year] == "Licences masculines":
                for age in db_handler.AGE_CATEGORY:
                    dbh.create_age((code_fede, age, 'male', row[age], year))
            if row['Fédérations françaises agréées en ' + year] == "Licences féminines":
                for age in db_handler.AGE_CATEGORY:
                    dbh.create_age((code_fede, age, 'female', row[age], year))
            if row['Fédérations françaises agréées en ' + year] == "Licences non réparties":
                for age in db_handler.AGE_CATEGORY:
                    dbh.create_age((code_fede, age, 'unknown', row[age], year))


def get_departments(file_path):
    """
    Return the departments name list.
    :param file_path:
    :return:
    """
    with open(file_path) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        spamreader.__next__()
        line2 = spamreader.__next__()

    return line2[3:-2]


DPT_LIST = get_departments('data/csv/2017/licencesdepsexe2017_oly.csv')


def fill_clubs(file_path, dbh, year):
    """
    Parse the given file to feed the clubs table.
    :param file_path:
    """
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                code_fede = int(row['Codes Fédé'])
            except ValueError:
                continue
            for dpt in DPT_LIST:
                try:
                    dbh.create_club((code_fede, dpt, row[dpt], year))
                except KeyError:
                    continue


def fill_departments(file_path, dbh, year):
    """
    Feed the by_dep table by parsing the input file ordered by departments.
    :param file_path:
    :param dbh:
    """
    with open(file_path, 'r') as csvfile:
        csvfile.readline()
        content = csvfile.read()
        with open("__tmp_csv.csv", 'w') as tmp_file:
            tmp_file.write(content)
        with open("__tmp_csv.csv", 'r') as tmp_file:
            data = csv.DictReader(tmp_file)
            for row in data:
                if row['Codes Fédé'] != "":
                    code_fede = row['Codes Fédé']
                if row['Fédérations françaises agréées en ' + year] == "Licences masculines":
                    for dep in DPT_LIST:
                        dbh.create_by_dep((code_fede, dep, row[dep], 'male', year))
                if row['Fédérations françaises agréées en ' + year] == "Licences féminines":
                    for dep in DPT_LIST:
                        dbh.create_by_dep((code_fede, dep, row[dep], 'female', year))
                if row['Fédérations françaises agréées en ' + year] == "Licences non réparties":
                    for dep in DPT_LIST:
                        dbh.create_by_dep((code_fede, dep, row[dep], 'unknown', year))
    os.remove("__tmp_csv.csv")


def main():
    """
    Create the sports database and feed it.
    """
    dbh = db_handler.DbHandler()

    years = ["2017", "2018"]

    for year in years:
        print("Process data for ", year)
        path = "data/csv/" + year + "/"

        populate_fede(path + 'licencesagesexe' + year + '_oly.csv', dbh, 'Olympic', year)
        populate_fede(path + 'licencesagesexe' + year + '_noly.csv', dbh, 'Non Olympic', year)
        populate_fede(path + 'licencesagesexe' + year + '_multi.csv', dbh, 'Multisports', year)

        populate_by_age(path + 'licencesagesexe' + year + '_oly.csv', dbh, year)
        populate_by_age(path + 'licencesagesexe' + year + '_noly.csv', dbh, year)
        populate_by_age(path + 'licencesagesexe' + year + '_multi.csv', dbh, year)

        fill_clubs(path + 'clubs' + year + '_dep.csv', dbh, year)

        fill_departments(path + 'licencesdepsexe' + year + '_oly.csv', dbh, year)
        fill_departments(path + 'licencesdepsexe' + year + '_noly.csv', dbh, year)
        fill_departments(path + 'licencesdepsexe' + year + '_multi.csv', dbh, year)

    dbh.save()
    # Close the database connection
    del dbh


if __name__ == "__main__":
    main()
