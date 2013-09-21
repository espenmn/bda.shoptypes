
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

Product (bda.shoptypes.product)
------------------------------
Contains two image-fields and two rich text fields. 
One of the images is intended for showing in the cart, while the other is intended as "productimage".
The first rich text field is intended for "description", while the other is intended for "technical information".
"Product" has "Buyable" and "Stock" behaviour which is required for beeing addable to the cart.

Productgroup (bda.shoptypes.productgroup)
-----------------------------------------
Is a folderish content type that can only contain "Variations". The content type has two rich text fields, 
the same ones as "Product". The idea is to use these for all the information that is the same
for all the contained "Variations".
There is also a Image. 

Variation (bda.shoptypes.variation) 
-----------------------------------
Can (only) be added inside a Productgroup folder. A "Variation" contains two Image fields and one "Colors" fields.
"Variation" has "Buyable" and "Stock" behaviour which is required for beeing addable to the cart.



Installation
============

Add ``bda.shoptypes`` to the eggs (in buildout.cfg) and install it as addon
in plone control panel.


Author
============

Espen Moe-Nilssen [espenmn]
