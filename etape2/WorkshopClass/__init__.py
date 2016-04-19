# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WorkshopClass
                                 A QGIS plugin
 A workshop for QGIS plugin
                             -------------------
        begin                : 2016-04-19
        copyright            : (C) 2016 by Oslandia
        email                : infos+qgis@oslandia.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load WorkshopClass class from file WorkshopClass.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .WorkshopClass import WorkshopClass
    return WorkshopClass(iface)
