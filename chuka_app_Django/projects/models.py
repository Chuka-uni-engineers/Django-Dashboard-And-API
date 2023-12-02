from django.db import models

from users.models import UserAccount


class Project(models.model):
    project_name = models.CharField(max_length=50, null=False)
    # Project admin to be determined through the member ranks
    # project_admin = models.ForeignKey(UserAccount, on_delete=models.SET_NULL)
    project_members = models.ManyToManyField(UserAccount, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.project_name)
