#!/usr/bin/env python
# -*- coding: utf-8 -*-


def create_args_string(num):
    l = []
    for n in range(num):
        l.append('?')
    return ', '.join(l)


class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '{}, {}:{}'.format(self.__class__.__name__, self.name, self.column_type)


class StringField(Field):
    def __init__(self, name=None, column_type='varchar(100)', primary_key=False, default=None):
        super(StringField, self).__init__(name, column_type, primary_key, default)


class IntegerField(Field):
    def __init__(self, name, column_type='bigint', primary_key=False, default=None):
        super(IntegerField, self).__init__(name, column_type, primary_key, default)


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):  # attrs 为类的 属性 或者 方法
        if name == 'Model':
            return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)
        table_name = attrs.get('__table__', None) or name
        print('Found model: {}({})'.format(name, table_name))

        mappings = dict()  # 表（User）的类属性键值对
        table_fields = []  # 表的列名
        model_fields = []  # model的属性名
        primary_key = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping:{}==>{}'.format(k, v))
                mappings[k] = v
                field_name = v.name if v.name else k
                if v.primary_key:
                    if primary_key:
                        raise RuntimeError('Duplicate primary key for field:{}'.format(v.name))
                    primary_key = field_name
                else:
                    table_fields.append(field_name)  # Field 类缺省name参数时，列名默认属性名
                    model_fields.append(k)  # 表（User）的类属性名称
        if not primary_key:
            raise RuntimeError('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)  # 从类的属性中删除Field属性， 以便后续获取实例的属性值

        attrs['__mapping__'] = mappings
        attrs['__table__'] = table_name
        attrs['__primary_key__'] = primary_key
        attrs['__fields__'] = table_fields  # 表的属性名
        attrs['__name_fields__'] = model_fields
        attrs['__select__'] = 'select {},{} from {} where {}=?'.format(primary_key, ','.join(table_fields), table_name,
                                                                       primary_key)
        attrs['__insert__'] = 'insert into {}({}) values ({})'.format(table_name, ','.join(table_fields),
                                                                      create_args_string(len(table_fields)))
        attrs['__update__'] = 'update {} set {} where {}=?'.format(table_name, ','.join(
            list(map(lambda f: '{}=?'.format(f), table_fields))), primary_key)
        attrs['__delete__'] = 'delete from {} where {}=?'.format(table_name, primary_key)

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

    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)  # getattr会先找类的属性或者父类的属性，如果存在该key,则返回
        if value is None:
            field = self.__mapping__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                setattr(self, key, value)
        return value

    @classmethod
    def save(cls, self):
        args = list(map(lambda k: self.getValueOrDefault(k), self.__name_fields__))
        print('sql:{}'.format(self.__insert__))
        print('args:{}'.format(args))

    @classmethod
    def findByPrimaryKey(cls, id):
        print('sql:{}'.format(cls.__select__))
        print('args:{}'.format(id))

    @classmethod
    def updateByPrimaryKey(cls, id):
        print('sql:{}'.format(cls.__update__))
        print('args:{}'.format(id))

    @classmethod
    def deleteByPrimaryKey(cls, id):
        print('sql:{}'.format(cls.__delete__))
        print('args:{}'.format(id))


class User(Model):
    id = IntegerField('id', primary_key=True)
    name = StringField('username')
    email = StringField('email')
    password = StringField('password', default='1234')


u = User(id=12345, name='michael', email='test@orm.org')  # id, name, email, password为实例的属性
User.save(u)
User.findByPrimaryKey(1)
User.updateByPrimaryKey(2)
User.deleteByPrimaryKey(3)
