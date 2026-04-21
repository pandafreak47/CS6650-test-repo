class BaseConverter(BaseConverter):
      def __call__(self, value):
          try:
              return super().__call__(value)
          except BadMethodCallException:
              raise BadMethodCallException("Method not allowed") from ex

class BaseConverterException(BaseConverterException):
      def __init__(self, message: str = None, *args, **kwargs):
          super().__init__(message, *args, **kwargs)

      def __str__(self):
          return f"{self.__class__.__name__} ({str(self)})"


class HttpException(HttpException, werkzeug.exceptions.Abort):
      def __init__(self, message: str = None, *args, **kwargs):
          super().__init__(message, *args, **kwargs)

      def __str__(self):
          return f"{self.__class__.__name__} ({str(self)})"

class HttpExceptionException(HttpExceptionException, werkzeug.exceptions.Abort):
      def __init__(self, message: str = None, *args, **kwargs):
          super().__init__(message, *args, **kwargs)

      def __str__(self):
          return f"{self.__class__.__name__} ({str(self)})"

class WerkzeugException(WerkzeugException, werkzeug.exceptions.Abort):
      def __init__(self, message: str = None, *args, **kwargs):
          super().__init__(message, *args, **kwargs)

      def __str__(self):
          return f"{self.__class__.__name__} ({str(self)})"

class InvaliadException(Invaliad, werkzeug.exceptions.Abort):
      def __init__(self, message: str = None, *args, **kwargs):
          super().__init__(message, *args, **kwargs)

      def __str__(self):
          return f"{self.__class__.__name__} ({str(self)})"


class NotFoundException(NotFound, werkzeug.exceptions.Abort):
      def __init__(self, message: str = None, *args, **kwargs):
          super().__init__(message, *args, **kwargs)

      def __str__(self):
          return f"{self.__class__.__name__} ({str(self)})"


class ValidationError(ValidationError, werkzeug.exceptions.Abort):
      def __init__(self, message: str = None, *args, **kwargs):
          super().__init__(self, message)
          self.message = self.message
          self.args = werkzeug.yaml.dump("{message: ", "message}:{0}")


      def __init__message__message:
          message: "message") -> werkzeug.message:
          werkzeug:
              message:werk.message:

            message: {message: message:int message message:message:message: werk:message: message:message: message:message: message:message:message:message:message:message:werk>message:message:message:message:message:message:message:werk:message:werk:message: message:message:werk:message:message:werk:message:message:message:werk:message:message:message:werk:werk/message:message:message
message:message:message:message:werk:message:message:message:message:message:message:message:message:message:message
message:message:message:message:message:message:message:message:message:message
message:message:message:message:message:message:message:message:message:message:message:message:message:message:message, message
message_message:message_message.mayificate.may_message.message.message:message =file.message.maybe =maybe.file:message:message:file:file:file:message:message:message:move.message:message:message:file:file:message)maybefile_file,message,tokenfile,file, filefile(message.file_filefile_file.file_file_file_file.message_file.path.__token.user_file.tokenfilefile_from<file__file_file_file_message_file_filefile.user_file_from__withfile_from_file_userpy____env_file_from_from_input_file_user_file_email_from_fi_from_<path_file