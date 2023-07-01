# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Webnucleo
else:
    import _Webnucleo

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Webnucleo.delete_SwigPyIterator

    def value(self):
        return _Webnucleo.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _Webnucleo.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _Webnucleo.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _Webnucleo.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _Webnucleo.SwigPyIterator_equal(self, x)

    def copy(self):
        return _Webnucleo.SwigPyIterator_copy(self)

    def next(self):
        return _Webnucleo.SwigPyIterator_next(self)

    def __next__(self):
        return _Webnucleo.SwigPyIterator___next__(self)

    def previous(self):
        return _Webnucleo.SwigPyIterator_previous(self)

    def advance(self, n):
        return _Webnucleo.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _Webnucleo.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _Webnucleo.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _Webnucleo.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _Webnucleo.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _Webnucleo.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _Webnucleo.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _Webnucleo:
_Webnucleo.SwigPyIterator_swigregister(SwigPyIterator)

SHARED_PTR_DISOWN = _Webnucleo.SHARED_PTR_DISOWN
class WebnucleoXml(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _Webnucleo.WebnucleoXml_swiginit(self, _Webnucleo.new_WebnucleoXml(*args))

    def SetInputFile(self, inp):
        return _Webnucleo.WebnucleoXml_SetInputFile(self, inp)

    def Init(self):
        return _Webnucleo.WebnucleoXml_Init(self)

    def UpdateData(self, inputCSV, outputXML):
        return _Webnucleo.WebnucleoXml_UpdateData(self, inputCSV, outputXML)

    def Z(self):
        return _Webnucleo.WebnucleoXml_Z(self)

    def A(self):
        return _Webnucleo.WebnucleoXml_A(self)

    def Spin(self):
        return _Webnucleo.WebnucleoXml_Spin(self)

    def Mass_excess(self):
        return _Webnucleo.WebnucleoXml_Mass_excess(self)

    def Source(self):
        return _Webnucleo.WebnucleoXml_Source(self)

    def PartFuncT9(self):
        return _Webnucleo.WebnucleoXml_PartFuncT9(self)

    def PartFuncLog10(self):
        return _Webnucleo.WebnucleoXml_PartFuncLog10(self)
    __swig_destroy__ = _Webnucleo.delete_WebnucleoXml

# Register WebnucleoXml in _Webnucleo:
_Webnucleo.WebnucleoXml_swigregister(WebnucleoXml)

class std_vector_int(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _Webnucleo.std_vector_int_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _Webnucleo.std_vector_int___nonzero__(self)

    def __bool__(self):
        return _Webnucleo.std_vector_int___bool__(self)

    def __len__(self):
        return _Webnucleo.std_vector_int___len__(self)

    def __getslice__(self, i, j):
        return _Webnucleo.std_vector_int___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _Webnucleo.std_vector_int___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _Webnucleo.std_vector_int___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _Webnucleo.std_vector_int___delitem__(self, *args)

    def __getitem__(self, *args):
        return _Webnucleo.std_vector_int___getitem__(self, *args)

    def __setitem__(self, *args):
        return _Webnucleo.std_vector_int___setitem__(self, *args)

    def pop(self):
        return _Webnucleo.std_vector_int_pop(self)

    def append(self, x):
        return _Webnucleo.std_vector_int_append(self, x)

    def empty(self):
        return _Webnucleo.std_vector_int_empty(self)

    def size(self):
        return _Webnucleo.std_vector_int_size(self)

    def swap(self, v):
        return _Webnucleo.std_vector_int_swap(self, v)

    def begin(self):
        return _Webnucleo.std_vector_int_begin(self)

    def end(self):
        return _Webnucleo.std_vector_int_end(self)

    def rbegin(self):
        return _Webnucleo.std_vector_int_rbegin(self)

    def rend(self):
        return _Webnucleo.std_vector_int_rend(self)

    def clear(self):
        return _Webnucleo.std_vector_int_clear(self)

    def get_allocator(self):
        return _Webnucleo.std_vector_int_get_allocator(self)

    def pop_back(self):
        return _Webnucleo.std_vector_int_pop_back(self)

    def erase(self, *args):
        return _Webnucleo.std_vector_int_erase(self, *args)

    def __init__(self, *args):
        _Webnucleo.std_vector_int_swiginit(self, _Webnucleo.new_std_vector_int(*args))

    def push_back(self, x):
        return _Webnucleo.std_vector_int_push_back(self, x)

    def front(self):
        return _Webnucleo.std_vector_int_front(self)

    def back(self):
        return _Webnucleo.std_vector_int_back(self)

    def assign(self, n, x):
        return _Webnucleo.std_vector_int_assign(self, n, x)

    def resize(self, *args):
        return _Webnucleo.std_vector_int_resize(self, *args)

    def insert(self, *args):
        return _Webnucleo.std_vector_int_insert(self, *args)

    def reserve(self, n):
        return _Webnucleo.std_vector_int_reserve(self, n)

    def capacity(self):
        return _Webnucleo.std_vector_int_capacity(self)
    __swig_destroy__ = _Webnucleo.delete_std_vector_int

# Register std_vector_int in _Webnucleo:
_Webnucleo.std_vector_int_swigregister(std_vector_int)

class std_vector_double(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _Webnucleo.std_vector_double_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _Webnucleo.std_vector_double___nonzero__(self)

    def __bool__(self):
        return _Webnucleo.std_vector_double___bool__(self)

    def __len__(self):
        return _Webnucleo.std_vector_double___len__(self)

    def __getslice__(self, i, j):
        return _Webnucleo.std_vector_double___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _Webnucleo.std_vector_double___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _Webnucleo.std_vector_double___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _Webnucleo.std_vector_double___delitem__(self, *args)

    def __getitem__(self, *args):
        return _Webnucleo.std_vector_double___getitem__(self, *args)

    def __setitem__(self, *args):
        return _Webnucleo.std_vector_double___setitem__(self, *args)

    def pop(self):
        return _Webnucleo.std_vector_double_pop(self)

    def append(self, x):
        return _Webnucleo.std_vector_double_append(self, x)

    def empty(self):
        return _Webnucleo.std_vector_double_empty(self)

    def size(self):
        return _Webnucleo.std_vector_double_size(self)

    def swap(self, v):
        return _Webnucleo.std_vector_double_swap(self, v)

    def begin(self):
        return _Webnucleo.std_vector_double_begin(self)

    def end(self):
        return _Webnucleo.std_vector_double_end(self)

    def rbegin(self):
        return _Webnucleo.std_vector_double_rbegin(self)

    def rend(self):
        return _Webnucleo.std_vector_double_rend(self)

    def clear(self):
        return _Webnucleo.std_vector_double_clear(self)

    def get_allocator(self):
        return _Webnucleo.std_vector_double_get_allocator(self)

    def pop_back(self):
        return _Webnucleo.std_vector_double_pop_back(self)

    def erase(self, *args):
        return _Webnucleo.std_vector_double_erase(self, *args)

    def __init__(self, *args):
        _Webnucleo.std_vector_double_swiginit(self, _Webnucleo.new_std_vector_double(*args))

    def push_back(self, x):
        return _Webnucleo.std_vector_double_push_back(self, x)

    def front(self):
        return _Webnucleo.std_vector_double_front(self)

    def back(self):
        return _Webnucleo.std_vector_double_back(self)

    def assign(self, n, x):
        return _Webnucleo.std_vector_double_assign(self, n, x)

    def resize(self, *args):
        return _Webnucleo.std_vector_double_resize(self, *args)

    def insert(self, *args):
        return _Webnucleo.std_vector_double_insert(self, *args)

    def reserve(self, n):
        return _Webnucleo.std_vector_double_reserve(self, n)

    def capacity(self):
        return _Webnucleo.std_vector_double_capacity(self)
    __swig_destroy__ = _Webnucleo.delete_std_vector_double

# Register std_vector_double in _Webnucleo:
_Webnucleo.std_vector_double_swigregister(std_vector_double)

class std_vector_std_vector_double(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _Webnucleo.std_vector_std_vector_double_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _Webnucleo.std_vector_std_vector_double___nonzero__(self)

    def __bool__(self):
        return _Webnucleo.std_vector_std_vector_double___bool__(self)

    def __len__(self):
        return _Webnucleo.std_vector_std_vector_double___len__(self)

    def __getslice__(self, i, j):
        return _Webnucleo.std_vector_std_vector_double___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _Webnucleo.std_vector_std_vector_double___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _Webnucleo.std_vector_std_vector_double___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _Webnucleo.std_vector_std_vector_double___delitem__(self, *args)

    def __getitem__(self, *args):
        return _Webnucleo.std_vector_std_vector_double___getitem__(self, *args)

    def __setitem__(self, *args):
        return _Webnucleo.std_vector_std_vector_double___setitem__(self, *args)

    def pop(self):
        return _Webnucleo.std_vector_std_vector_double_pop(self)

    def append(self, x):
        return _Webnucleo.std_vector_std_vector_double_append(self, x)

    def empty(self):
        return _Webnucleo.std_vector_std_vector_double_empty(self)

    def size(self):
        return _Webnucleo.std_vector_std_vector_double_size(self)

    def swap(self, v):
        return _Webnucleo.std_vector_std_vector_double_swap(self, v)

    def begin(self):
        return _Webnucleo.std_vector_std_vector_double_begin(self)

    def end(self):
        return _Webnucleo.std_vector_std_vector_double_end(self)

    def rbegin(self):
        return _Webnucleo.std_vector_std_vector_double_rbegin(self)

    def rend(self):
        return _Webnucleo.std_vector_std_vector_double_rend(self)

    def clear(self):
        return _Webnucleo.std_vector_std_vector_double_clear(self)

    def get_allocator(self):
        return _Webnucleo.std_vector_std_vector_double_get_allocator(self)

    def pop_back(self):
        return _Webnucleo.std_vector_std_vector_double_pop_back(self)

    def erase(self, *args):
        return _Webnucleo.std_vector_std_vector_double_erase(self, *args)

    def __init__(self, *args):
        _Webnucleo.std_vector_std_vector_double_swiginit(self, _Webnucleo.new_std_vector_std_vector_double(*args))

    def push_back(self, x):
        return _Webnucleo.std_vector_std_vector_double_push_back(self, x)

    def front(self):
        return _Webnucleo.std_vector_std_vector_double_front(self)

    def back(self):
        return _Webnucleo.std_vector_std_vector_double_back(self)

    def assign(self, n, x):
        return _Webnucleo.std_vector_std_vector_double_assign(self, n, x)

    def resize(self, *args):
        return _Webnucleo.std_vector_std_vector_double_resize(self, *args)

    def insert(self, *args):
        return _Webnucleo.std_vector_std_vector_double_insert(self, *args)

    def reserve(self, n):
        return _Webnucleo.std_vector_std_vector_double_reserve(self, n)

    def capacity(self):
        return _Webnucleo.std_vector_std_vector_double_capacity(self)
    __swig_destroy__ = _Webnucleo.delete_std_vector_std_vector_double

# Register std_vector_std_vector_double in _Webnucleo:
_Webnucleo.std_vector_std_vector_double_swigregister(std_vector_std_vector_double)

class std_vector_std_string(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _Webnucleo.std_vector_std_string_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _Webnucleo.std_vector_std_string___nonzero__(self)

    def __bool__(self):
        return _Webnucleo.std_vector_std_string___bool__(self)

    def __len__(self):
        return _Webnucleo.std_vector_std_string___len__(self)

    def __getslice__(self, i, j):
        return _Webnucleo.std_vector_std_string___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _Webnucleo.std_vector_std_string___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _Webnucleo.std_vector_std_string___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _Webnucleo.std_vector_std_string___delitem__(self, *args)

    def __getitem__(self, *args):
        return _Webnucleo.std_vector_std_string___getitem__(self, *args)

    def __setitem__(self, *args):
        return _Webnucleo.std_vector_std_string___setitem__(self, *args)

    def pop(self):
        return _Webnucleo.std_vector_std_string_pop(self)

    def append(self, x):
        return _Webnucleo.std_vector_std_string_append(self, x)

    def empty(self):
        return _Webnucleo.std_vector_std_string_empty(self)

    def size(self):
        return _Webnucleo.std_vector_std_string_size(self)

    def swap(self, v):
        return _Webnucleo.std_vector_std_string_swap(self, v)

    def begin(self):
        return _Webnucleo.std_vector_std_string_begin(self)

    def end(self):
        return _Webnucleo.std_vector_std_string_end(self)

    def rbegin(self):
        return _Webnucleo.std_vector_std_string_rbegin(self)

    def rend(self):
        return _Webnucleo.std_vector_std_string_rend(self)

    def clear(self):
        return _Webnucleo.std_vector_std_string_clear(self)

    def get_allocator(self):
        return _Webnucleo.std_vector_std_string_get_allocator(self)

    def pop_back(self):
        return _Webnucleo.std_vector_std_string_pop_back(self)

    def erase(self, *args):
        return _Webnucleo.std_vector_std_string_erase(self, *args)

    def __init__(self, *args):
        _Webnucleo.std_vector_std_string_swiginit(self, _Webnucleo.new_std_vector_std_string(*args))

    def push_back(self, x):
        return _Webnucleo.std_vector_std_string_push_back(self, x)

    def front(self):
        return _Webnucleo.std_vector_std_string_front(self)

    def back(self):
        return _Webnucleo.std_vector_std_string_back(self)

    def assign(self, n, x):
        return _Webnucleo.std_vector_std_string_assign(self, n, x)

    def resize(self, *args):
        return _Webnucleo.std_vector_std_string_resize(self, *args)

    def insert(self, *args):
        return _Webnucleo.std_vector_std_string_insert(self, *args)

    def reserve(self, n):
        return _Webnucleo.std_vector_std_string_reserve(self, n)

    def capacity(self):
        return _Webnucleo.std_vector_std_string_capacity(self)
    __swig_destroy__ = _Webnucleo.delete_std_vector_std_string

# Register std_vector_std_string in _Webnucleo:
_Webnucleo.std_vector_std_string_swigregister(std_vector_std_string)


