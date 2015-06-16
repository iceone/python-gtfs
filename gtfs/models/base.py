# -*- coding: utf-8 -*-
"""
    gtfs.models.base
    ~~~~~~~~~~~~~~~~~~~~

    Base model like namedtuple.
"""
import os
import sys
from operator import itemgetter


def BaseModel(typename, fields):

    typeclass = """class {typename}(tuple):

        __slots__ = ()
        __required__ = ()

        def __new__(cls, {args}):
            iterable = map(str, ({args}))
            result = tuple.__new__(cls, iterable)
            if len(result) != {numfields}:
                raise TypeError('Expected {numfields} arguments, got {{gotfields}}'
                    .format(gotfields=len(result))
                )
            for field in cls.__required__:
                if not len(getattr(result, field)):
                    raise ValueError('Missing required Field {{field}}'
                        .format(field=field)
                    )
            return result

        def __repr__(self):
            return '<{typename} {repr_fields}>' % self

        @property
        def __fields__(self):
            return ({fields})

    {properties}
    """
    
    property_fmt = """
        {name} = property(itemgetter({index}))
    """

    repr_fields = ', '.join(['{0}=%r'.format(field) for field in fields])
    properties = ''.join(
        [property_fmt.format(name=name, index=idx) for idx, name in enumerate(fields)]
    )

    typedef = typeclass.format(
        typename=typename,
        numfields=len(fields),
        args=repr(fields).replace("'", "")[1:-1],
        fields=repr(fields)[1:-1],
        repr_fields=repr_fields,
        properties=properties
    )
   
    namespace = dict(
        itemgetter=itemgetter,
        property=property,
        tuple=tuple,
        properties=properties,
        __name__=sys._getframe().f_code.co_name
    )

    exec typedef in namespace
    return namespace[typename]
