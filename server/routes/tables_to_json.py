from app import ma
from models import GoodTypes, Goods
from flask import jsonify
from api_calls.error import ApiError


def split_select(field_list, meta_class, no_class_context, unnecessary_class_context):
    if field_list is not None:
        field_list = field_list.split(',')
        variables = dir(meta_class)

        for field in field_list:
            if (field not in variables and field not in no_class_context) or field in unnecessary_class_context or field == '':
                raise ApiError('INVALID_SELECT_FIELD')

    return field_list


class GoodsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Goods
        include_fk = True


def goods_json(good_table, is_many, field_list):
    
    no_class_context = ()
    unnecessary_class_context = ()
    field_list = split_select(field_list, Goods, no_class_context, unnecessary_class_context)

    schema = GoodsSchema(many=is_many, only = field_list)
 
    return schema.dump(good_table)


def good_types_json(good_type_table, is_many, field_list, expand):
    
    no_class_context = ('goodsCount')
    unnecessary_class_context = ('goods')
    field_list = split_select(field_list, GoodTypes, no_class_context, unnecessary_class_context)


    class GoodTypesSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = GoodTypes

        if expand is not None:
            if '.' in expand:
                expandValue, good_field_list = expand.split('.')

                if expandValue != 'goods':
                    raise ApiError('INVALID_EXPAND_VALUE')

                if '=' in good_field_list:
                    expand_value_parameter, good_field_list = good_field_list.split('=')

                    if expand_value_parameter != 'select':
                        raise ApiError('INVALID_EXPAND_VALUE_PARAMETER')

                    no_class_context = ()
                    unnecessary_class_context = ()
                    good_field_list = split_select(good_field_list, Goods, no_class_context, unnecessary_class_context)

                else:
                    raise ApiError('INVALID_EXPAND_VALUE_PARAMETER')

                goods = ma.Nested(GoodsSchema, many=True, only=good_field_list)

            elif expand != 'goods':
                raise ApiError('INVALID_EXPAND_VALUE')

            else:
                goods = ma.Nested(GoodsSchema, many=True)

            if field_list is not None:
                field_list.append('goods')

    
    select_count = True

    if field_list is not None and 'goodsCount' in field_list:
        field_list.remove('goodsCount')
    elif field_list is not None:
        select_count = False

    schema = GoodTypesSchema(many=is_many, only=field_list)
    dumped_schema = schema.dump(good_type_table)

    if select_count:
        if is_many:
            for i in range(len(dumped_schema)):
                dumped_schema[i]['goodsCount'] = good_type_table[i].goods.count()
        else:
            dumped_schema['goodsCount'] = good_type_table.goods.count()
    
    return dumped_schema