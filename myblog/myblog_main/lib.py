# -*- coding:utf8 -*-
__author__ = 'xxc'
from flask import request, Response
from flask import Blueprint as FlaskBlueprint
from inspect import isclass
from werkzeug.wrappers import BaseResponse
from warnings import warn
from pprint import pprint



class View(object):
    '''
    pretend self is function, when return string or Response,
    covert another that illegal return to Response thought method res2response

    can announce staticmethod get, post, options, head, put, delete and
    getorpost
    '''
    res = None

    def __new__(cls, *args, **kwargs):
        res = cls.dispatch(request.method.lower(), request, args, kwargs)
        if isinstance(res, (basestring, BaseResponse)):
            return res
        elif isinstance(res, tuple) and len(res) == 2\
                and isinstance(res[0], basestring)\
                and isinstance(res[1], int):
            return res
        else:
            ins = super(View, cls).__new__(cls)
            ins.res = res
            return ins

    @classmethod
    def dispatch(cls, method, request, args, kwargs):
        if hasattr(cls, method):
            cb = getattr(cls, method)
            if callable(cb):
                return cb(*args, **kwargs)
        raise ValueError('invalid method %r' % method)

    def res2response(self, res):
        warn("%r:should override method" % self)
        return Response(unicode(res))

    def __call__(self, environ, start_response):
        '''
        代理到response
        '''
        res = self.res2response(self.res)
        return res.__call__(environ, start_response)


class Blueprint(FlaskBlueprint):
    def route(self, rule, **options):
        """Like :meth:`Flask.route` but for a blueprint.  The endpoint for the
        :func:`url_for` function is prefixed with the name of the blueprint.
        """
        def decorator(f):
            endpoint = options.pop("endpoint", f.__name__)
            if 'methods' not in options\
                    and isclass(f)\
                    and issubclass(f, View):
                methods = []
                if hasattr(f, 'getorpost'):
                    setattr(f, 'get', staticmethod(f.getorpost))
                    setattr(f, 'post', staticmethod(f.getorpost))
                elif hasattr(f, 'postorget'):
                    setattr(f, 'get', staticmethod(f.getorpost))
                    setattr(f, 'post', staticmethod(f.getorpost))
                for m in ('get', "post", "put", "head", "delete", "options"):
                    if hasattr(f, m) and callable(getattr(f, m)):
                        methods.append(m.upper())
                options['methods'] = methods
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator


