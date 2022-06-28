from importlib import resources
from import_export import resources
from ...models.manage_models import branch



class branch_record(resources.ModelResource):
    class Meta:
        model = branch