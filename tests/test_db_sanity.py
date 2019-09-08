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


    def test_oly_by_age_2017(self):
        """
        This unit test ensure that for the year 2017, the olympics sports data ordered by age are
        well stored in the database.
        """
        req = "SELECT nb FROM by_age WHERE code_fede = 101 AND age = '0 à 4 ans' \
            AND sex = 'male' AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 300)

        req = "SELECT nb FROM by_age WHERE code_fede = 118 AND age = '55 à 59 ans' \
            AND sex = 'female' AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 115)

        req = "SELECT nb FROM by_age WHERE code_fede = 133 AND age = '80 ans et plus' \
            AND sex = 'unknown' AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 0)


    def test_noly_by_age_2017(self):
        """
        This unit test ensure that for the year 2017, the non olympics sports data ordered by age
        are well stored in the database.
        """
        req = "SELECT nb FROM by_age WHERE code_fede = 201 AND age = '0 à 4 ans' \
            AND sex = 'male' AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 5)

        req = "SELECT nb FROM by_age WHERE code_fede = 218 AND age = '55 à 59 ans' \
            AND sex = 'female' AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 2704)

        req = "SELECT nb FROM by_age WHERE code_fede = 267 AND age = '80 ans et plus' \
            AND sex = 'unknown' AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 0)


    def test_multi_by_age_2017(self):
        """
        This unit test ensure that for the year 2017, the multi sports data ordered by age are
        well stored in the database.
        """
        req = "SELECT nb FROM by_age WHERE code_fede = 401 AND age = '0 à 4 ans' \
            AND sex = 'male' AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 73)

        req = "SELECT nb FROM by_age WHERE code_fede = 418 AND age = '55 à 59 ans' \
            AND sex = 'female' AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 231)

        req = "SELECT nb FROM by_age WHERE code_fede = 605 AND age = '80 ans et plus' \
            AND sex = 'unknown' AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 0)


    def test_clubs_2017(self):
        """
        This unit test ensure that for the year 2017, clubs are well stored in the database.
        """
        req = "SELECT nb_clubs FROM clubs WHERE code_fede = 101 AND dpt = 'Ain' AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 20)

        req = "SELECT nb_clubs FROM clubs WHERE code_fede = 233 AND dpt = 'Maine-et-Loire' \
            AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 10)

        req = "SELECT nb_clubs FROM clubs WHERE code_fede = 605 AND dpt = 'Monaco' \
            AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 0)


    def test_oly_by_dep_2017(self):
        """
        This unit test ensure that for the year 2017, olympics data sorted by departments are well
        stored in the database.
        """
        req = "SELECT nb FROM by_dpt WHERE code_fede = 101 AND dpt = 'Ain' AND sex = 'male' \
            AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 1165)

        req = "SELECT nb FROM by_dpt WHERE code_fede = 118 AND dpt = 'Nord' AND sex = 'female' \
            AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 250)

        req = "SELECT nb FROM by_dpt WHERE code_fede = 133 AND dpt = 'Monaco' \
            AND sex = 'unknown' AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 0)


    def test_noly_by_dep_2017(self):
        """
        This unit test ensure that for the year 2017, non olympics data sorted by departments are
        well stored in the database.
        """
        req = "SELECT nb FROM by_dpt WHERE code_fede = 201 AND dpt = 'Ain' AND sex = 'male' \
            AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 271)

        req = "SELECT nb FROM by_dpt WHERE code_fede = 218 AND dpt = 'Nord' AND sex = 'female' \
            AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 336)

        req = "SELECT nb FROM by_dpt WHERE code_fede = 267 AND dpt = 'Monaco' \
            AND sex = 'unknown' AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 0)


    def test_multi_by_dep_2017(self):
        """
        This unit test ensure that for the year 2017, multi sports data sorted by departments are
        well stored in the database.
        """
        req = "SELECT nb FROM by_dpt WHERE code_fede = 401 AND dpt = 'Ain' AND sex = 'male' \
            AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 1436)

        req = "SELECT nb FROM by_dpt WHERE code_fede = 418 AND dpt = 'Nord' AND sex = 'female' \
            AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 51)

        req = "SELECT nb FROM by_dpt WHERE code_fede = 605 AND dpt = 'Monaco' \
            AND sex = 'unknown' AND year = 2017"
        self.cur.execute(req)
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 0)


if __name__ == '__main__':
    unittest.main()
