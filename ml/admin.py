from django.contrib import admin
from .models import ClassificationResultsSVM, ClassificationResultsNB, ClassificationResultsKNearest, ClassificationResultsLog, ClassificationResultsRF, ClassificationResultsDT
from .models import RegressionResultsLinear, RegressionResultsPolynomial, RegressionResultsLasso, RegressionResultsRidge, RegressionResultsElasticNet


# Register your models here.
admin.site.register(ClassificationResultsSVM)
admin.site.register(ClassificationResultsLog)
admin.site.register(ClassificationResultsNB)
admin.site.register(ClassificationResultsKNearest)
admin.site.register(ClassificationResultsRF)
admin.site.register(ClassificationResultsDT)
admin.site.register(RegressionResultsLinear)
admin.site.register(RegressionResultsPolynomial)
admin.site.register(RegressionResultsLasso)
admin.site.register(RegressionResultsRidge)
admin.site.register(RegressionResultsElasticNet)





