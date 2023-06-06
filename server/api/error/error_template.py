class ApiError(Exception): # editable class template for all kinds of errors
    status_code = 400 # default status code 'BAD_REQUEST', if it's not provided


    def __init__(self, error, status_code=None):
        super().__init__

        self.error = error

        if status_code is not None:
            self.status_code = status_code


    def to_dict(self): # returning json response with a name of an error
        for_json = dict()
        for_json['message'] = self.error
        
        return for_json
