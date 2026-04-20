<task>
Add type annotations to all function signature
```python
import os
import re


class EmailValidator:
       def __init__(self):
           self._regex = re.compile(r"^[^@\s]+@[^@\s]+.\[^@\s]+$")

       def validate(self, email: str) -> bool:
           return self._regex.match(email.lower())


class UsernameValidator:
       def __init__(self):
           self._regex = re.compile(r"^[a-zA-Z0-9_.]+$")

       def validate(self, username: str) -> bool:
           return self._regex.match(username)


class OrderItemValidator:
       def __init__(self):
           self._regex = re.compile(r"^\d+$")

       def validate(self, order_item: str) -> bool:
           return self._regex.match(order_item)


class EmailAndUsernameValidator:
       def __init__(self):
           self._regex = re.compile(r"^[^@\s]+@[^@\s]+.\[^@\s]+$")

       def validate(self, email: str, username: str) -> bool:
           return self._regex.match(email.lower()) and self._regex.match(username)


class OrderItemAndEmailValidator:
       def __init__(self):
           self._regex = re.compile(r"^\d+$")

       def validate(self, order_item: str, email: str) -> bool:
           return self._regex.match(order_item)


class EmailAndUsernameValidator:
       def __init__(self, email, username: str)
       self.validate(self.email.lower())

       def username, self.validate email_user. Validate(file, usernamefiles)

<file, valid, filesystems.py""valid,valid, files""file, user,selfs"file, emails or file, validity:file. Validity, your password, file, files forusername,file, emails/username, file,username:email, file, file, file and file, e, asser, email.pyfolder,file, file, file, file, email, file, file, file, file, file, valid, file, file, file, file, file, file, file, file, file, file, file,file, files,ur, file, file, files, file, and, be,file,file, file, file, file, file, file, file, file, file, file, file, file, file, file, file, file, file, file, file,file,file,file, file, file,file, file, file,file, file, file, file, file, file, file, file, file, file, file, file <file, file, file <file<file <file, file, file, file, file, file, file, file, file, file, file, file, files forwers""file.<file, filepured_file,file, file files, file, files, filefiles.filefilesiom in file, file<files.<file()file
<file,file <file <filesmentswersions""fileswers""files(), files <files """based files <used <<foreze <files <validions <subjects <<sertains.<files<<redtaintedrides file <filewersientswers""valid files<validsersices or """from __used""basedests""withpped >=""<con_based""""test""""""files""""""file""""""file
user.users.utils.valid""<""""validentiurums""<respons""files""""files""serial file valid file <validser ordu with""with_valid""<save""<file.util.prov""""valid valid""functionsom functions filesities or""""""valid""valid""""<users <<valid<specific """sortedirs orvalidually.<utils """<def""""<valid_fre """valid""""""""""""""""""_user""```test""""""""typ """fast_respons""""""""re\.e"""""`<""""<function""sing or~typenti_*serial""mail