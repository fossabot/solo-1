# -*- coding: utf-8 -*-
#
# Copyright (c) 2017-2019, 2023 Víctor Molina García
#
# This file is part of solo.
#
# solo is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# solo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with solo; if not, see <https://www.gnu.org/licenses/>.
#
"""Basic tests for the :class:`Geometry` class."""

import os.path
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import numpy as np
from solo.api import Geometry
from . import TestSolo


UNITTEST_FOLDER = os.path.dirname(__file__)
GEOMETRY_FOLDER = os.path.join(UNITTEST_FOLDER, "obj", "geo")


class TestGeometry(TestSolo):
    """Basic tests for the :class:`Geometry` class."""

    def check_geo_equal(self, geo1, geo2):
        """Generic equal check for :class:`Geometry` classes."""

        self.assertTrue(np.allclose(geo1.day, geo2.day))
        if geo1.sec is None:
            self.assertTrue(geo1.sec is geo2.sec)
        else:
            self.assertTrue(np.allclose(geo1.sec, geo2.sec))
        if geo1.lat is None:
            self.assertTrue(geo1.lat is geo2.lat)
        else:
            self.assertTrue(np.allclose(geo1.lat, geo2.lat))
        if geo1.lon is None:
            self.assertTrue(geo1.lon is geo2.lon)
        else:
            self.assertTrue(np.allclose(geo1.lon, geo2.lon))
        self.assertTrue(np.allclose(geo1.sza, geo2.sza))
        self.assertTrue(np.allclose(geo1.mu0, geo2.mu0))

    def test_geo11(self):
        """Test loading of `geo11.dat` from file."""

        path = os.path.join(GEOMETRY_FOLDER, "geo11.dat")
        geo1 = Geometry.from_file(path)
        geo2 = Geometry(
            day=152, sec=None, lat=None, lon=None, sza=60, mode="deg")
        self.check_geo_equal(geo1, geo2)

    def test_geo12(self):
        """Test loading of `geo12.dat` from file."""

        path = os.path.join(GEOMETRY_FOLDER, "geo12.dat")
        geo1 = Geometry.from_file(path)
        geo2 = Geometry(
            day=152, sec=25311, lat=0.49410271, lon=-0.28797933,
            sza=1.39777933, mode="rad")
        self.check_geo_equal(geo1, geo2)

    def test_geo13(self):
        """Test loading of `geo13.dat` from file."""

        path = os.path.join(GEOMETRY_FOLDER, "geo13.dat")
        geo1 = Geometry.from_file(path)
        geo2 = Geometry(
            day=152, sec=43510, lat=0.49410271, lon=-0.28797933,
            sza=0.2546518, mode="rad")
        self.check_geo_equal(geo1, geo2)

    def test_geo21(self):
        """Test loading of `geo21.dat` from file."""

        path = os.path.join(GEOMETRY_FOLDER, "geo21.dat")
        geo1 = Geometry.from_file(path)
        geo2 = Geometry(
            day=np.array([152, 152, 152, 152, 153]), sec=None, lat=None,
            lon=None, sza=np.array([60, 50.4, 15.1, 21, 75.]), mode="deg")
        self.check_geo_equal(geo1, geo2)

    def test_geo22(self):
        """Test loading of `geo22.dat` from file."""

        path = os.path.join(GEOMETRY_FOLDER, "geo22.dat")
        geo1 = Geometry.from_file(path)
        geo2 = Geometry(
            day=np.array([152, 180, 235]),
            sec=np.array([25311, 5678, 47162]),
            lat=np.array([0.49410271, 0.83950337, 0.00872665]),
            lon=np.array([-0.28797933, 1.31772359, 0.6981317]),
            sza=np.array([1.39777933, 1.17809272, 0.98533964]),
            mode="rad")
        self.check_geo_equal(geo1, geo2)

    def test_geo23(self):
        """Test loading of `geo23.dat` from file."""

        path = os.path.join(GEOMETRY_FOLDER, "geo23.dat")
        geo1 = Geometry.from_file(path)
        geo2 = Geometry(
            day=np.array([152, 180, 235]),
            sec=np.array([43510, 47175, 50820]),
            lat=np.array([0.49410271, 0.83950337, 0.00872665]),
            lon=np.array([-0.28797933, 1.31772359, 0.6981317]),
            sza=np.array([0.2546518, 1.28671359, 1.24504354]),
            mode="rad")
        self.check_geo_equal(geo1, geo2)


if __name__ == "__main__":
    unittest.main()
