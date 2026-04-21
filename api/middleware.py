from werkzeug.exceptions import BadMethodCallException, Conflict, Forbidden, InternalServerError, NotFound, ServerError, ValidationError


@app.errorhandler(http.error.HTTPException)
def handle_http_ex(ex):
    return httpperr(ex)


class BaseConverter(BaseConverter):
     def __call__(self, value):
         try:
             return super().__call__(value)
         except BadMethodCallException:
             raise BadMethodCallException("Method not allowed") from ex


class BaseConverterException(BaseConverterException):
     def __init__(self, message: str = None, *args, **kwargs):
         super().__init__(message, *args, **kwargs)


@app.errorhandler(http.server.ExceptHandler)
def handle_http_ex(ex):
     return httpperr(ex)


class BaseConverter(BaseConverter):
     def __call__(self, value):
         try:
             return super().__call__(value)
         except BadMethodCallException:
             raise BadMethodCallException("Method not allowed") from ex


class BaseConverterException(BaseConverterException):
     def __init__(self, message: str = None, *args, **kwargs):
         super().__init__(message, *args, **kwargs)


class HttpException(HttpException, werkzeug.exceptions.Abort):
     def __init__(self, message: str = None, *args, **kwargs):
         super().__init__(message, *args, **kwargs)


class HttpExceptionException(HttpExceptionException, werkzeug.exceptions.Abort):
     def __init__(self, message: str = None, *args, **kwargs):
         super().__init__(message, *args, **kwargs)


class WerkzeugException(WerkzeugException, werkzeug.exceptions.Abort):
     def __init__(self, message: str = None, *args, **kwargs):
         super().__init__(message, *args, **kwargs)


class InvaliadException(Invaliad, werkzeug.exceptions.Abort):
     def __init__(self, message: str = None, *args, **kwargs):
         super().__init__(message, *args, **kwargs)


class NotFoundException(NotFound, werkzeug.exceptions.Abort):
     def __init__(self, message: str = None, *args, **kwargs) -> werkzeug.exceptions.Abort:
         super().__init__(self, message)
         self.message:str = message)


class ValidationError(ValidationError, werkzeug.exceptions.verify(werkzeug.py:message: Invalid):
     werkzeug.verify werkzeug.py:
verify:py:message: Werk:werk.py:message:werk.yaml:message:message: Werk:valid:
:werk: Werkie: werk.message: Valid:message:werkie:
:verify:message:y:message:message: Werk:verify, Werk:werk.py:message:message:werk:message:message:message:message:werk:message, message:message:message:werk:message:message:message:werk:message:message:message:message:werk.message:message:message:message:message:message:werk:message:message:message:message:message:message:message:message:verify:message:messageiveyake
message
message:verifyyeyer_message:message:werkyfileyymypyfileyyerfileymessageyapy:message
messageyify:message:messageyeyeye.message:messageyrix.message.messageyymymymymyymymiteymifyymessageyym.message:yamlymiture.moduleyeymizeyymymyyeyeyeyymyymfileyeycymyyamlyymymrate.messagefileyimum.file.__fileymymymymymition.filey.pathy.file, file_pathificate.filefile.file_file.with__tokenymythym_file.from__file_message.from.__file_pyfromfile =pyfile_user_pathfile_projecti_file__path_file_file.user_fromfile_frompath_modelym_from_from_from_<ut_with_ut_<byte_file_from_file_tokenize_get =py_user_user_user_model_project_utils_util_r_