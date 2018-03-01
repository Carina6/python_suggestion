#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '{}:{}'.format(self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):   # attrs 为类的 属性 或者 方法
        if name == 'Model':
            return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)
        print('Found model: {}'.format(name))

        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping:{}==>{}'.format(k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)             # 从类的属性中删除Field属性， 以便后续获取实例的属性值

        attrs['__mapping__'] = mappings
        attrs['__table__'] = name

        return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('"Model" object has no attribute {}'.format(key))

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []

        for k, v in self.__mapping__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k))      # getattr会先找类的属性或者父类的属性，如果存在该key,则返回
        sql = 'insert into {}({}) values ({})'.format(self.__table__, ','.join(fields), ','.join(params))
        print('sql:{}'.format(sql))
        print('args:{}'.format(args))


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='michael', email='test@orm.org', password='pwd')    # id, name, email, password为实例的属性
u.save()