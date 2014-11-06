# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WorkshopClass
                                 A QGIS plugin
 a simple plugin for the workshop
                             -------------------
        begin                : 2014-11-06
        copyright            : (C) 2014 by me
        email                : me@wherever.org
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

def classFactory(iface):
    # load WorkshopClass class from file WorkshopClass
    from workshopclass import WorkshopClass
    return WorkshopClass(iface)
