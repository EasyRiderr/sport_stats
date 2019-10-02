#!/usr/bin/env python
# coding: utf-8
"""
Perform the sanity testing over the database.
"""

import unittest
import sqlite3
import db_handler


class TestDbSanity(unittest.TestCase):
    """
    This class will be used to test the database sanity.
    """

    def setUp(self):
        self.database = sqlite3.connect(db_handler.DB_PATH)
        self.cur = self.database.cursor()


    def tearDown(self):
        self.database.close()


    res_oly_age = {
        '2017': [300, 115, 0],
        '2018': [341, 123, 0]
    }


    def test_oly_by_age(self):
        """
        This unit test ensure that olympics sports data ordered by age are well stored in the
        database.
        """
        for year in self.res_oly_age:
            with self.subTest(year=year):
                req = "SELECT nb FROM by_age WHERE code_fede = 101 AND age = '0 à 4 ans' \
                    AND sex = 'male' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_oly_age[year][0])

                req = "SELECT nb FROM by_age WHERE code_fede = 118 AND age = '55 à 59 ans' \
                    AND sex = 'female' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_oly_age[year][1])

                req = "SELECT nb FROM by_age WHERE code_fede = 133 AND age = '80 ans et plus' \
                    AND sex = 'unknown' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_oly_age[year][2])


    res_noly_age = {
        '2017': [5, 2704, 0],
        '2018': [7, 2497, 0]
    }


    def test_noly_by_age(self):
        """
        This unit test ensure that the non olympics sports data ordered by age are well stored in
        the database.
        """
        for year in self.res_noly_age:
            with self.subTest(year=year):
                req = "SELECT nb FROM by_age WHERE code_fede = 201 AND age = '0 à 4 ans' \
                    AND sex = 'male' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_noly_age[year][0])

                req = "SELECT nb FROM by_age WHERE code_fede = 218 AND age = '55 à 59 ans' \
                    AND sex = 'female' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_noly_age[year][1])

                req = "SELECT nb FROM by_age WHERE code_fede = 267 AND age = '80 ans et plus' \
                    AND sex = 'unknown' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_noly_age[year][2])


    res_multi_age = {
        '2017': [73, 231, 0],
        '2018': [63, 251, 0]
    }


    def test_multi_by_age(self):
        """
        This unit test ensure that the multi sports data ordered by age are well stored in the
        database.
        """
        for year in self.res_noly_age:
            with self.subTest(year=year):
                req = "SELECT nb FROM by_age WHERE code_fede = 401 AND age = '0 à 4 ans' \
                    AND sex = 'male' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_multi_age[year][0])

                req = "SELECT nb FROM by_age WHERE code_fede = 418 AND age = '55 à 59 ans' \
                    AND sex = 'female' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_multi_age[year][1])

                req = "SELECT nb FROM by_age WHERE code_fede = 605 AND age = '80 ans et plus' \
                    AND sex = 'unknown' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_multi_age[year][2])


    res_clubs = {
        '2017': [20, 10, 0],
        '2018': [21, 10, 0]
    }


    def test_clubs(self):
        """
        This unit test ensure that clubs are well stored in the database.
        """
        for year in self.res_clubs:
            with self.subTest(year=year):
                req = "SELECT nb_clubs FROM clubs WHERE code_fede = 101 AND dpt = 'Ain' \
                    AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_clubs[year][0])

                req = "SELECT nb_clubs FROM clubs WHERE code_fede = 233 \
                    AND dpt = 'Maine-et-Loire' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_clubs[year][1])

                req = "SELECT nb_clubs FROM clubs WHERE code_fede = 605 AND dpt = 'Monaco' \
                    AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_clubs[year][2])


    res_oly_dep = {
        '2017': [1165, 250, 0],
        '2018': [1169, 216, 0]
    }


    def test_oly_by_dep(self):
        """
        This unit test ensure that olympics data sorted by departments are well stored in the
        database.
        """
        for year in self.res_oly_dep:
            with self.subTest(year=year):
                req = "SELECT nb FROM by_dpt WHERE code_fede = 101 AND dpt = 'Ain' \
                    AND sex = 'male' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_oly_dep[year][0])

                req = "SELECT nb FROM by_dpt WHERE code_fede = 118 AND dpt = 'Nord' \
                    AND sex = 'female' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_oly_dep[year][1])

                req = "SELECT nb FROM by_dpt WHERE code_fede = 133 AND dpt = 'Monaco' \
                    AND sex = 'unknown' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_oly_dep[year][2])


    res_noly_dep = {
        '2017': [271, 336, 0],
        '2018': [257, 327, 0]
    }


    def test_noly_by_dep(self):
        """
        This unit test ensure that non olympics data sorted by departments are well stored in the
        database.
        """
        for year in self.res_noly_dep:
            with self.subTest(year=year):
                req = "SELECT nb FROM by_dpt WHERE code_fede = 201 AND dpt = 'Ain' \
                    AND sex = 'male' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_noly_dep[year][0])

                req = "SELECT nb FROM by_dpt WHERE code_fede = 218 AND dpt = 'Nord' \
                    AND sex = 'female' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_noly_dep[year][1])

                req = "SELECT nb FROM by_dpt WHERE code_fede = 267 AND dpt = 'Monaco' \
                    AND sex = 'unknown' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_noly_dep[year][2])


    res_multi_dep = {
        '2017': [1436, 51, 0],
        '2018': [1442, 46, 0]
    }


    def test_multi_by_dep(self):
        """
        This unit test ensure that multi sports data sorted by departments are well stored in the
        database.
        """
        for year in self.res_multi_dep:
            with self.subTest(year=year):
                req = "SELECT nb FROM by_dpt WHERE code_fede = 401 AND dpt = 'Ain' \
                    AND sex = 'male' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_multi_dep[year][0])

                req = "SELECT nb FROM by_dpt WHERE code_fede = 418 AND dpt = 'Nord' \
                    AND sex = 'female' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_multi_dep[year][1])

                req = "SELECT nb FROM by_dpt WHERE code_fede = 605 AND dpt = 'Monaco' \
                    AND sex = 'unknown' AND year = " + year
                self.cur.execute(req)
                rows = self.cur.fetchall()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], self.res_multi_dep[year][2])


if __name__ == '__main__':
    unittest.main()
