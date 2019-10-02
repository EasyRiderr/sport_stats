#!/usr/bin/env python
# coding: utf-8

"""Provides all the functions needed to access the sports database."""

import sqlite3


DB_PATH = 'sports.db'


AGE_CATEGORY = [
    "0 à 4 ans",
    "5 à 9 ans",
    "10 à 14 ans",
    "15 à 19 ans",
    "20 à 24 ans",
    "25 à 29 ans",
    "30 à 34 ans",
    "35 à 39 ans",
    "40 à 44 ans",
    "45 à 49 ans",
    "50 à 54 ans",
    "55 à 59 ans",
    "60 à 64 ans",
    "65 à 69 ans",
    "70 à 74 ans",
    "75 à 79 ans",
    "80 ans et plus",
    "Non renseigné"
]


class DbHandler:
    """
    This class will be used to take care of all operations needed on the database.
    """


    def __init__(self):
        """
        Constructor by default, connect to the local database.
        """
        self.__db = sqlite3.connect(DB_PATH)
        self.__cur = self.__db.cursor()
        self.__create_tables()


    def __create_tables(self):
        """
        Creates the database structure.
        """
        self.__cur.execute("""
            CREATE TABLE IF NOT EXISTS federations(
                id INTEGER PRIMARY KEY UNIQUE,
                name TEXT,
                category TEXT
        )
        """)
        self.__cur.execute("""
            CREATE TABLE IF NOT EXISTS clubs(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                code_fede INT,
                dpt TEXT,
                nb_clubs INT,
                year INT,
                FOREIGN KEY(code_fede) REFERENCES federations(i)
        )
        """)
        self.__cur.execute("""
            CREATE TABLE IF NOT EXISTS by_age(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                code_fede INT,
                age TEXT,
                sex TEXT,
                nb INT,
                year INT,
                FOREIGN KEY(code_fede) REFERENCES federations(id)
        )
        """)
        self.__cur.execute("""
            CREATE TABLE IF NOT EXISTS by_dpt(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                code_fede INT,
                dpt TEXT,
                nb INT,
                sex TEXT,
                year INT,
                FOREIGN KEY(code_fede) REFERENCES federations(id)
        )
        """)

        # Save all the changes
        self.save()


    def create_federation(self, fede):
        """
        Insert the given federation into the federations table.
        :param fede:
        :return:
        """
        sql = ''' INSERT or IGNORE INTO federations(id, name, category) VALUES(?, ?, ?) '''
        self.__cur.execute(sql, fede)
        # Save all the changes
        return self.__cur.lastrowid


    def create_age(self, age):
        """
        Insert the given data into the by_age table.
        :param age:
        :return: age id
        """
        sql = ''' INSERT INTO by_age(code_fede, age, sex, nb, year) VALUES(?, ?, ?, ?, ?) '''
        self.__cur.execute(sql, age)
        # Save all the changes
        return self.__cur.lastrowid


    def create_club(self, club):
        """
        Insert the given club in the clubs table.
        :param club:
        :return:
        """
        sql = ''' INSERT INTO clubs(code_fede, dpt, nb_clubs, year) VALUES(?, ?, ?, ?) '''
        self.__cur.execute(sql, club)
        return self.__cur.lastrowid


    def create_by_dep(self, by_dep):
        """
        Insert the given department data into the by_dpt table.
        :param by_dep:
        :return: by_dpt id
        """
        sql = ''' INSERT INTO by_dpt(code_fede, dpt, nb, sex, year) VALUES(?, ?, ?, ?, ?) '''
        self.__cur.execute(sql, by_dep)
        # Save all the changes
        return self.__cur.lastrowid


    def save(self):
        """
        This method is used to commit all changes done on the database.
        """
        self.__db.commit()


    def __del__(self):
        """
        Destructor of the Object, it will be called same if the Constructor has met an exception.
        """
        if self.__cur:
            self.__cur.close()
        if self.__db:
            self.save()
            self.__db.close()
