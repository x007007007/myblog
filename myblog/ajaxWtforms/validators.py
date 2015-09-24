# -*- coding: utf8 -*-
__author__ = 'xxc'


class ValidatorSchema(object):
    _form_validator = True

    def __init__(self, fields, validator):
        self.fields = fields
        self.validator = validator

