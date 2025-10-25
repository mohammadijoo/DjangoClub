from django.db import models


class ClassificationResultsSVM(models.Model):

    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification



class ClassificationResultsNB(models.Model):

    Age = models.FloatField()
    Sex = models.FloatField()
    BP = models.FloatField()
    Cholesterol = models.FloatField()
    Na_to_K = models.FloatField()
    Drug = models.CharField(max_length=30)

    def __str__(self):
        return self.Drug
        
        
        
class ClassificationResultsKNearest(models.Model):

    Temperature = models.FloatField()
    L = models.FloatField()
    R = models.FloatField()
    A_M = models.FloatField()
    Color = models.FloatField()
    Spectral_Class = models.FloatField()
    Type = models.CharField(max_length=30)

    def __str__(self):
        return self.Type
        
        
   
class ClassificationResultsLog(models.Model):

    Pregnancies = models.FloatField()
    Glucose = models.FloatField()
    BloodPressure = models.FloatField()
    SkinThickness = models.FloatField()
    Insulin = models.FloatField()
    BMI = models.FloatField()
    DiabetesPedigreeFunction = models.FloatField()
    Age = models.FloatField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification     
        


class ClassificationResultsRF(models.Model):

    RI = models.FloatField()
    Na = models.FloatField()
    Mg = models.FloatField()
    Al = models.FloatField()
    Si = models.FloatField()
    K = models.FloatField()
    Ca = models.FloatField()
    Ba = models.FloatField()
    Fe = models.FloatField()
    Type = models.CharField(max_length=60)

    def __str__(self):
        return self.Type    





class ClassificationResultsDT(models.Model):

    Weight = models.FloatField()
    Length1 = models.FloatField()
    Length2 = models.FloatField()
    Length3 = models.FloatField()
    Height = models.FloatField()
    Width = models.FloatField()
    Species = models.CharField(max_length=30)

    def __str__(self):
        return self.Species




class RegressionResultsLinear(models.Model):

    SqFt = models.FloatField()
    Bedrooms = models.FloatField()
    Bathrooms = models.FloatField()
    Offers = models.FloatField()
    Brick = models.FloatField()
    Neighborhood = models.FloatField()
    Price = models.FloatField()

    def __str__(self):
        return str(self.Price)




class RegressionResultsPolynomial(models.Model):

    fixed_acidity = models.FloatField()
    volatile_acidity = models.FloatField()
    citric_acid = models.FloatField()
    residual_sugar = models.FloatField()
    chlorides = models.FloatField()
    free_sulfur_dioxide = models.FloatField()
    total_sulfur_dioxide = models.FloatField()
    density = models.FloatField()
    pH = models.FloatField()
    sulphates = models.FloatField()
    alcohol = models.FloatField()
    quality = models.FloatField()

    def __str__(self):
        return str(self.quality)
        
        
        
        
        
class RegressionResultsLasso(models.Model):

    carat = models.FloatField()
    cut = models.FloatField()
    color = models.FloatField()
    clarity = models.FloatField()
    depth = models.FloatField()
    table = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return str(self.price)
        
        
        
        
class RegressionResultsRidge(models.Model):

    latitude = models.FloatField()
    longitude = models.FloatField()
    depth = models.FloatField()
    magnitude = models.FloatField()

    def __str__(self):
        return str(self.magnitude)
        
        
        
        
        
class RegressionResultsElasticNet(models.Model):

    Age = models.FloatField()
    Job = models.FloatField()
    Salary = models.FloatField()

    def __str__(self):
        return str(self.Salary)





































       
        