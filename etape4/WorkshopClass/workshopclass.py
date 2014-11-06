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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from workshopclassdialog import WorkshopClassDialog
import os.path

class WorkshopClass:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'workshopclass_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = WorkshopClassDialog()
        
        self.canvas = self.iface.mapCanvas()
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        self.clickTool.canvasClicked.connect(self.handleMouseDown)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/workshopclass/icon.png"),
            u"run", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&workshop_plugin", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&workshop_plugin", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        self.canvas.setMapTool(self.clickTool)

    def handleMouseDown(self, point, button):
        # we assume one vector layer and optionnally a second layer that is not a vector layer
        layers = [layer for layerId, layer in QgsMapLayerRegistry.instance().mapLayers().iteritems()]
        layer = layers[0] if isinstance(layers[0], QgsVectorLayer) else layers[1]
       
        # we create a rectangle of 2 pixels around the point 
        # and select the first feature in this rectangle
        nbPixels = 2
        pointGeometry = QgsGeometry.fromPoint(point)
        pointBuffer = pointGeometry.buffer( (self.canvas.mapUnitsPerPixel() * nbPixels),0)
        rectangle = pointBuffer.boundingBox()
        features = layer.getFeatures( QgsFeatureRequest(rectangle))

        for feature in features:
            self.dlg.lineEditDebut.setText(feature['debutchant'])
            self.dlg.lineEditFin.setText(feature['finchantie'])
              
            # show the dialog
            self.dlg.show()
            # Run the dialog event loop
            result = self.dlg.exec_()
            # See if OK was pressed
            if result == 1:
                fid = feature.id()
                field = feature.fieldNameIndex('debutchant')
                layer.changeAttributeValue(fid, field, self.dlg.ui.lineEditDebut.text())
                field = feature.fieldNameIndex('finchantie')
                layer.changeAttributeValue(fid, field, self.dlg.ui.lineEditFin.text())

        self.iface.actionPan().trigger()

