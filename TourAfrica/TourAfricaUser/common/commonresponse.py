class BaseResponse():
    def __init__(self, status_code=400, data=None, message=None, success=False, Error=[]):
        self.status_code = status_code
        self.data = data
        self.message = message
        self.success = success
        self.error = Error
        
    def to_dict(self):
        return {
            'success': self.success,
            'message': self.message,
            'data': self.data,
            'error': self.error,
            'statuscode': self.status_code,
        }