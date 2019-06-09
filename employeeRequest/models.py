from django.db import models
from auditlog.registry import auditlog

# Create your models here.

class EmployeeRequest(models.Model):
    request_name = models.CharField(max_length=50)
    request_details = models.TextField()
    status = models.IntegerField(default=0)
    user = models.ForeignKey('users.User', default=1, on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.CASCADE, related_name='created_by+')
    modified_by = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.CASCADE, related_name='modified_by+')

    def as_json(self):
        return dict(
            request_name=str(self.request_name),
            request_details=str(self.request_details),
            user=self.user_id,
            status = int(self.status),
            created_at = self.created_at,
            modified_at = self.modified_at
        )


auditlog.register(EmployeeRequest)
