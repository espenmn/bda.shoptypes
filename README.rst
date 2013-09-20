
=========================
bda.shoptypes
=========================

(Demo) Conttent types for bda.plone.shop

Checking it out
===============

This product also installs bda.plone.shopviews. You should read the "bda.plone.shopviews readme" file 

The content types
=================

There are 3 Content types

Product(bda.shoptypes.product)
------------------------------
Contains two images and two rich text fields. The rich text fields will have their own tabs at the bottom

Productgroup (bda.shoptypes.productgroup)

Variation (bda.shoptypes.variation) that can be added inside a Productgroup folder. You should set the view of Productgroup to one of the Variation (in other words: the view of "Productgroup folder" should be one content item (the default Variation)





Installation
============

Add ``bda.shoptypes`` to the eggs (in buildout.cfg) and install it as addon
in plone control panel.


Author
============

Espen Moe-Nilssen [espenmn]