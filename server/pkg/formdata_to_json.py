# Converting form-data from a request into json
# for the continious json validation
def convert_formdata_to_json(formdata):
    json = {}

    for key, value in formdata.items():
        if value.lower() == 'true':
            json[key] = True
        elif value.lower() == 'false':
            json[key] = False
        elif value.isdigit():
            json[key] = int(value)
        elif key == 'image':
            pass
        else:
            json[key] = value

    return json