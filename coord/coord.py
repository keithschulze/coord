""" Provides core functions for converting between coordinate systems

Coord module provides simple module for converting between different coordinate
systems using numpy.
"""

import numpy as np

__author__ = "Keith Schulze"
__copyright__ = "Copyright 2015, Monash Micro Imaging"
__license__ = "MIT"
__version__ = "0.1.0"
__email__ = "keith.schulze@monash.edu"
__status__ = "development"


def cartesian2spherical(coords):
    """Convert Cartesian to Spherical coordinates.

    Converts an array of 3D Cartesian coordinates [x, y, z] to
    the equivalent array of Spherical coordinates [r, theta, phi].

    Parameters
    ----------
    coords: numpy.ndarray
            An m by 3 array of m Cartesian coordinates (x, y, z) in an
            3-dimensional space.

    Returns
    -------
    out_coords: numpy.ndarray
                Returns an m by 3 array of m Spherical coordinates in the
                order r (radial distance), theta (azimuth angle, radians)
                and phi (zenith angle, radians).
    """
    sphere = np.zeros(coords.shape)
    xy_sq = coords[:, 0]**2 + coords[:, 1]**2
    sphere[:, 0] = np.sqrt(xy_sq + coords[:, 2]**2)
    sphere[:, 1] = np.arctan2(coords[:, 1], coords[:, 0])
    sphere[:, 2] = np.arctan2(np.sqrt(xy_sq), coords[:, 2])
    return sphere


def spherical2cartesian(sphere):
    """Convert Spherical to Cartesian coordinates.

    Converts an array of Spherical coordinates [r, theta, phi] to
    the equivalent array of Cartesian coordinates [x, y, z].

    Parameters
    ----------
    coords: numpy.ndarray
            An m by 3 array of m Spherical coordinates in the
            order r (radial distance), theta (azimuth angle, radians)
            and theta (zenith angle, radians).

    Returns
    -------
    out_coords: numpy.ndarray
                Returns an m by 3 array of m Cartesian coordinates (x, y, z) in an
                3-dimensional space.
    """
    cart = np.zeros(sphere.shape, dtype=np.float64)
    sine_phi = np.sin(sphere[:, 2])

    cart[:, 0] = sphere[:, 0] * np.cos(sphere[:, 1]) * sine_phi
    cart[:, 1] = sphere[:, 0] * np.sin(sphere[:, 1]) * sine_phi
    cart[:, 2] = sphere[:, 0] * np.cos(sphere[:, 2])
    return cart


def spherical2cylindrical(sph):
    """Convert Spherical to Cylindrical coordinates.

    Converts an array of Spherical coordinates [r, theta, phi] to
    the equivalent array of Cylindrical coordinates [r, theta, z].

    Parameters
    ----------
    coords: numpy.ndarray
            An m by 3 array of m Spherical coordinates in the
            order r (radial distance), theta (azimuth angle, radians)
            and phi (zenith angle, radians).

    Returns
    -------
    out_coords: numpy.ndarray
                Returns an m by 3 array of m Cylindrical coordinates in the
                order r (radial distance), theta (azimuth angle, radians)
                and z (height).
    """
    cyl = np.zeros(sph.shape)
    cyl[:, 0] = sph[:, 0] * np.sin(sph[:, 2])
    cyl[:, 1] = sph[:, 1]
    cyl[:, 2] = sph[:, 0] * np.cos(sph[:, 2])
    return cyl


def cylindrical2spherical(cyl):
    """Convert Cylindrical to Spherical coordinates.

    Converts an array of Cylindrical coordinates [r, theta, z] to
    the equivalent array of Spherical coordinates [r, theta, phi].

    Parameters
    ----------
    coords: numpy.ndarray
            An m by 3 array of m Cylindrical coordinates in the
            order r (radial distance), theta (azimuth angle, radians)
            and z (height).

    Returns
    -------
    out_coords: numpy.ndarray
                Returns an m by 3 array of m Spherical coordinates in the
                order r (radial distance), theta (azimuth angle, radians)
                and phi (zenith angle, radians).
    """
    sph = np.zeros(cyl.shape)
    sph[:, 0] = np.sqrt(cyl[:, 0]**2 + cyl[:, 2]**2)
    sph[:, 1] = cyl[:, 1]
    sph[:, 2] = np.arctan2(cyl[:, 0], cyl[:, 2])
    return sph


def cartesian2cylindrical(coords):
    """Convert Cartesian to Cylindrical coordinates.

    Converts an array of 3D Cartesian coordinates [x, y, z] to
    the equivalent array of Cylindrical coordinates [r, theta, z].

    Parameters
    ----------
    coords: numpy.ndarray
            An m by 3 array of m Cartesian coordinates (x, y, z) in an
            3-dimensional space.

    Returns
    -------
    out_coords: numpy.ndarray
                Returns an m by 3 array of m Cylindrical coordinates in the
                order r (radial distance), theta (azimuth angle, radians)
                and z (height).
    """
    cyl = np.zeros(coords.shape)
    cyl[:, 0] = np.sqrt(coords[:, 0] ** 2 + coords[:, 1] ** 2)
    cyl[:, 1] = np.arctan2(coords[:, 1], coords[:, 0])
    cyl[:, 2] = coords[:, 2]
    return cyl


def cylindrical2cartesian(cylinder):
    """Convert Cylindrical to Cartesian coordinates.

    Converts an array of Cylindrical coordinates [r, theta, z] to
    the equivalent array of Cartesian coordinates [x, y, z].

    Parameters
    ----------
    coords: numpy.ndarray
            An m by 3 array of m Cylindrical coordinates in the
            order r (radial distance), theta (azimuth angle, radians)
            and z (height).

    Returns
    -------
    out_coords: numpy.ndarray
                Returns an m by 3 array of m Cartesian coordinates (x, y, z) in an
                3-dimensional space.
    """
    cart = np.zeros(cylinder.shape)
    cart[:, 0] = cylinder[:, 0] * np.cos(cylinder[:, 1])
    cart[:, 1] = cylinder[:, 0] * np.sin(cylinder[:, 1])
    cart[:, 2] = cylinder[:, 2]
    return cart
