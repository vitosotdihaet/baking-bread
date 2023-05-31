from api_calls.error import ApiError


def split_select(field_list, meta_class, no_class_context, unnecessary_class_context):
    if field_list is not None:
        field_list = field_list.split(',')
        variables = dir(meta_class)

        for field in field_list:
            if (field not in variables and field not in no_class_context) or field in unnecessary_class_context or field == '':
                raise ApiError('INVALID_SELECT_FIELD')

    return field_list