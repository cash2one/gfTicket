#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Liantian'
__email__ = "liantian@188.com"
# Stdlib imports
# Core Django imports
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# Third-party app imports

# Imports from your apps


from .models import DocumentUser


def has_document_user(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            try:
                document_user = (request.user.document_user is not None)
            except DocumentUser.DoesNotExist:
                return HttpResponseRedirect(reverse(viewname="Document:initialize_user") + "?next=" + request.path)
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)

# def verified_document_user_generic_permission(function=None):
#     def _dec(view_func):
#         def _view(request, *args, **kwargs):
#             if request.user.document_user.generic_permission is False:
#                 return HttpResponseRedirect(reverse(viewname="Document:error") + "?error=" + _("当前用户权限不足（文档系统普通权限）"))
#             return view_func(request, *args, **kwargs)
#
#         _view.__name__ = view_func.__name__
#         _view.__dict__ = view_func.__dict__
#         _view.__doc__ = view_func.__doc__
#
#         return _view
#
#     if function is None:
#         return _dec
#     else:
#         return _dec(function)
#
#
# def verified_document_user_advanced_permission(function=None):
#     def _dec(view_func):
#         def _view(request, *args, **kwargs):
#             if request.user.document_user.advanced_permission is False:
#                 return HttpResponseRedirect(reverse(viewname="Document:error") + "?error=" + _("当前用户权限不足（文档系统高级权限）"))
#             return view_func(request, *args, **kwargs)
#
#         _view.__name__ = view_func.__name__
#         _view.__dict__ = view_func.__dict__
#         _view.__doc__ = view_func.__doc__
#
#         return _view
#
#     if function is None:
#         return _dec
#     else:
#         return _dec(function)