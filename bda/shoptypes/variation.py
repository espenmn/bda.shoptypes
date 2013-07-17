
from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.supermodel import model

from plone.app.textfield import RichText

from Products.Five import BrowserView

from bda.shoptypes import MessageFactory as _


# Interface class; used to define content-type schema.

class IVariation(model.Schema, IImageScaleTraversable):
    """
    Variation to use within a Productgroup
    """

    # If you want a schema-defined interface, delete the model.load
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/variation.xml to define the content type.

    model.load("models/variation.xml")


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Variation(Container):
    pass
    # Add your class methods and properties here


# View class
# The view is configured in configure.zcml. Edit there to change
# its public name. Unless changed, the view will be available
# TTW at content/@@sampleview
#
#class SampleView(BrowserView):
#    """ sample view class """
#
#    The views are put in bda.plone.shopviews product