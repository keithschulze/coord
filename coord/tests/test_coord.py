"""Tests for Coords module
"""

import numpy as np
import unittest
from coord import coord


class CoordTests(unittest.TestCase):

    """ Test case for coord module.
    """

    def setUp(self):
        self.cartcoords = np.array([[1.32, 5.21, 6.26],
                                    [5.23, 9.48, 1.22],
                                    [4.61, 2.67, 8.45]])

        self.sphercoords = np.array([[8.25070300035094, 1.32265882940926, 0.709445461424002],
                                     [10.8954898926115, 1.06665825153994, 1.45858807503646],
                                     [9.98916913461775, 0.524966770280452, 0.562515560918575]])

        self.cylcoords = np.array([[5.374616265, 1.32265882940926, 6.26],
                                   [10.82697095, 1.06665825153994, 1.22],
                                   [5.327382096, 0.524966770280452, 8.45]])

    def test_conv_cart_to_sphere(self):
        out = coord.cartesian2spherical(self.cartcoords)
        np.testing.assert_array_almost_equal(out, self.sphercoords)

    def test_conv_sphere_to_cart(self):
        out = coord.spherical2cartesian(self.sphercoords)
        np.testing.assert_array_almost_equal(out, self.cartcoords)

    def test_conv_cart_to_cyl(self):
        out = coord.cartesian2cylindrical(self.cartcoords)
        np.testing.assert_array_almost_equal(out, self.cylcoords)

    def test_conv_cyl_to_cart(self):
        out = coord.cylindrical2cartesian(self.cylcoords)
        np.testing.assert_array_almost_equal(out, self.cartcoords)

    def test_conv_sphere_to_cyl(self):
        out = coord.spherical2cylindrical(self.sphercoords)
        np.testing.assert_array_almost_equal(out, self.cylcoords)

    def test_conv_cyl_to_sphere(self):
        out = coord.cylindrical2spherical(self.cylcoords)
        np.testing.assert_array_almost_equal(out, self.sphercoords)
