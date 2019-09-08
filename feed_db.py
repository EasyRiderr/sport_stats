#!/usr/bin/env python
# coding: utf-8
"""
Feed the database
"""


import csv
import os
import db_handler


def populate_fede(file_path, dbh, category):
    """
    Parse the input file sorted by age and feed the federation table.
    :param file_path:
    :param dbh:
    :param category:
    """
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Codes Fédé'] != "":
                dbh.create_federation((row['Codes Fédé'],
                                       row['Fédérations françaises agréées en 2017'],
                                       category))



def populate_by_age(file_path, dbh):
    """
    Parse the input file sorted by age and feed the by_age table.
    :param file_path:
    :param dbh:
    """
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        code_fede = 0
        for row in reader:
            if row['Codes Fédé'] != "":
                code_fede = row['Codes Fédé']
            if row['Fédérations françaises agréées en 2017'] == "Licences masculines":
                for age in db_handler.AGE_CATEGORY:
                    dbh.create_age((code_fede, age, 'male', row[age], 2017))
            if row['Fédérations françaises agréées en 2017'] == "Licences féminines":
                for age in db_handler.AGE_CATEGORY:
                    dbh.create_age((code_fede, age, 'female', row[age], 2017))
            if row['Fédérations françaises agréées en 2017'] == "Licences non réparties":
                for age in db_handler.AGE_CATEGORY:
                    dbh.create_age((code_fede, age, 'unknown', row[age], 2017))


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


DPT_LIST = get_departments('data/csv/2017/licencesdepsexe17_oly.csv')


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
                if row['Fédérations françaises agréées en 2017'] == "Licences masculines":
                    for dep in DPT_LIST:
                        dbh.create_by_dep((code_fede, dep, row[dep], 'male', year))
                if row['Fédérations françaises agréées en 2017'] == "Licences féminines":
                    for dep in DPT_LIST:
                        dbh.create_by_dep((code_fede, dep, row[dep], 'female', year))
                if row['Fédérations françaises agréées en 2017'] == "Licences non réparties":
                    for dep in DPT_LIST:
                        dbh.create_by_dep((code_fede, dep, row[dep], 'unknown', year))
    os.remove("__tmp_csv.csv")


def main():
    """
    Create the sports database and feed it.
    """
    dbh = db_handler.DbHandler()

    path = "data/csv/2017/"

    populate_fede(path + 'licencesagesexe17_oly.csv', dbh, 'Olympic')
    populate_fede(path + 'licencesagesexe17_noly.csv', dbh, 'Non Olympic')
    populate_fede(path + 'licencesagesexe17_multi.csv', dbh, 'Multisports')

    populate_by_age(path + 'licencesagesexe17_oly.csv', dbh)
    populate_by_age(path + 'licencesagesexe17_noly.csv', dbh)
    populate_by_age(path + 'licencesagesexe17_multi.csv', dbh)

    fill_clubs(path + 'clubs17_dep.csv', dbh, 2017)

    fill_departments(path + 'licencesdepsexe17_oly.csv', dbh, 2017)
    fill_departments(path + 'licencesdepsexe17_noly.csv', dbh, 2017)
    fill_departments(path + 'licencesdepsexe17_multi.csv', dbh, 2017)

    dbh.save()
    # Close the database connection
    del dbh


if __name__ == "__main__":
    main()
