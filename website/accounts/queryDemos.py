# Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


# RELATED SET EXAMPLE
# class ParentModel(models.Model):
# name = models.CharField(max_length=200, null=True)

# class ChildModel(models.Model):
# 	parent = models.ForeignKey(ParentModel)
# 	name = models.CharField(max_length=200, null=True)
#
# parent = ParentModel.objects.first()
# Returns all child models related to parent
# parent.childmodel_set.all()
