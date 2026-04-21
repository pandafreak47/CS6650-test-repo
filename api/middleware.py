def post(request, path, file=None):
    return Response("Successfully uploaded file.")

def put(request, path, file=None):
    return Response("Successfully uploaded file.")

def delete(request, path, id):
    return Response("File with ID {0} removed.".format(id))

def get(request, path, id):
    return Response("File with ID {0} found.".format(id))

def patch(request, path, id, file):
    return Response("File with ID {0} has been updated.".format(id))

def options(request, path, files=None):
    return Response(None)

def head(request, path, id):
    return Response("File with ID {0} not found.".format(id))

def put_as(request, path, id, file):
    return Response("File with ID {0} was updated.".format(id))

def delete_as(request, path, id):
    return Response("File with ID {0} was removed.".format(id))

def get_as(request, path, id):
    return Response("File with ID {0} found.".format(id))

def patch_as(request, path, id, file):
    return Response("File with ID {0} has been updated.".format(id))

def options_as(request, path, files=None):
    return Response(None)

def head_as(request, path, id):
    return Response("File with ID {0} not found.".format(id))

def put_as_with_body(request, path, id, file):
    return Response("File with ID {0} was updated.".format(id))

def delete_as_with_body(request, path, id):
    return Response("File with ID {0} was removed.".format(id))

def get_as_with_body(request, path, id):
    return Response("File with ID {0} found.".format(id))

def patch_as_with_body(request, path, id, file):
    return Response("File with ID {0} has been updated.".format(id))

def options_as_with_body(request, path, files=None):
    return Response(None)

def head_as_with_body(request, path, id):
    return Response("File with ID {0} not found.".format(id))


<file path="api/user_repo.py">
class User(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(verbose_name='Email')
    password = models.CharField(max_length=128, verbose_name='Password')
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Role(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='Name')


    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class Permission(models.Model):
    name = models.CharField(max_length=255, unique=True)


class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)


class RolePermission(models