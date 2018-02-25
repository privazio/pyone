import dicttoxml
import xmltodict

#
# This function will cast parameters to make them nebula friendly
# flat dictionaries will be turned into attribute=value vectors
# dictionaries with root dictionary will be serialized as XML
#
# Structures will be turned into strings before being submitted.


def dict2one(param):
    # if this is a structured type
    if isinstance(param, dict):
        if bool(param):
            root = param.values()[0]
            if isinstance(root, dict):
                # We return this dictionary as XML
                return dicttoxml.dicttoxml(param, root=False, attr_type=False)
            else:
                # We return this dictionary as attribute=value vector
                ret = str()
                for k, v in param.iteritems():
                    ret = ret + k + " = " + str('"') + str(v) + str('"') + str('\n')
                return ret
        else:
            raise Exception("Cannot cast empty dictionary")
    else:
        return param

#
# This function returns a dictionary from a binding
# The dictionary can then be used
#


def one2dict(param):
    dom = param.toDOM()
    ret = xmltodict.parse(dom.toxml())
    del ret[dom.documentElement.tagName]['@xmlns']
    return ret
