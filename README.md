workshop-qgisplateform
======================


Télécharger les données
-----------------------

Un shapefile des chantiers du Grand Lyon est disponible [ici](http://smartdata.grandlyon.com/smartdata/wp-content/plugins/wp-smartdata/proxy.php?format=Shape-zip&name=pvo_patrimoine_voirie.pvochantierperturbant&commune=&href=https%3A%2F%2Fdownload.data.grandlyon.com%2Fwfs%2Fgrandlyon%3FSERVICE%3DWFS%26REQUEST%3DGetFeature%26typename%3Dpvo_patrimoine_voirie.pvochantierperturbant%26outputformat%3DSHAPEZIP%26VERSION%3D2.0.0%26SRSNAME%3DEPSG%3A3946). Vous pouvez obtenir des détails en visitant http://smartdata.grandlyon.com/search/?Q=chantier.

Une fois le fichier sauvé, inutile de le décompresser, QGIS s'en chargera.


Charger les données dan QGIS
----------------------------

### Fond de plan

Ouvrir le menu 'Layers' et choisir 'Add WMS/WMTS Layer'. Dans la boite de dialogue cliquer sur 'new' et informer les champs suivants:
* Name: Grand Lyon
* URL: https://download.data.grandlyon.com/wms/grandlyon

Cliquer sur 'connect' et sellectioner la couche 'Plan guide du Grand Lyon'. Clicker sur 'Add'puis 'Close'.

### Couche vectorielle

Ouvrir le menu 'Layers' et choisir 'Add Vector Layer', cliquer sur 'Browse' et selectionner le fichier téléchargé contenant les chantiers du Grand Lyon.

Dans le paneau 'Layers' (à gauche par defaut) selectionner la couche vectorielle, cliquer avec le bouton de droite pour obtenir le menu contextuel et sélectionner les propriétés de la couche.

Dans la fenêtre des propriétés, sélectioner l'onglet 'Style'. Sélectionner le rectangle montrant le style courant (paneau gauche).

![Fenêtre des propriétés de la couche](images/layers_properties.png)

Changez le style pour avoir des polygone blancs avec un contour rouge de 1.5 mm. Fermer la fenêtre en cliquant sur 'OK'.


Modifier le format des dates
----------------------------

Le fonctions de QGIS sont accessibles en python, ce qui permet de créer des extensions ou d'effectuer des traitements sur les données. Nous souhaitons changer le format des dates et transformer jj/mm/aaaa en aaaa/mm/jj afin de pouvoir utiliser l'extension TimeManager qui ne supporte pas le format.

Sélectioner la couche des chantiers, ouvrir le menu contextuel (click droit) et selectionner la table des attributs. Observer les champs 'debutchant' et 'finchantie'. Fermer la tables des attributs.



Dans le menu 'Plugins' sélectioner la console python. Dans la console pythin, entrer la commande:

```python
iface.activeLayer()
```
    
Qu'observez-vous? Sélectioner le fond de plan et relancer la commande (vous pouvez rapeller la dernière comande avec la touche flèche vers le haut).

Selectionner à nouveau la couche de chantiers et lancer la commande:

```python
for feature in iface.activeLayer().getFeatures():
   print feature['debutchant']
```
Nous utilisons la commande split() qui permet de découper une chaîne de charactère pour récupérer jour mois et années dans trois variables différentes, nous utilisons ensuite la fonction de formatage t=pour obtenir la date au format souhaité:

```python
for feature in iface.activeLayer().getFeatures():
   [jour, mois, annee] = feature['debutchant'].split('/')
   print "%s/%s/%s"%(annee, mois, jour)
```







