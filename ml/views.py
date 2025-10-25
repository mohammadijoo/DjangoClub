from django.shortcuts import render, redirect
from django.http import JsonResponse
import pandas as pd
from .models import ClassificationResultsSVM, ClassificationResultsNB, ClassificationResultsKNearest, ClassificationResultsLog, ClassificationResultsRF, ClassificationResultsDT
from .models import RegressionResultsLinear, RegressionResultsPolynomial, RegressionResultsLasso, RegressionResultsRidge, RegressionResultsElasticNet
from django.conf import settings
import os
from .forms import LogisticForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
import time
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures


################################################################################



def classification(request):
    return render(request, 'classification.html')
    
def regression(request):
    return render(request, 'regression.html')
    
def clustering(request):
    return render(request, 'clustering.html')
    
def deeplearning(request):
    return render(request, 'deeplearning.html')
    
def neuralnetwork(request):
    return render(request, 'neuralnetwork.html')
    
    
def classificationfa(request):
    return render(request, 'classificationfa.html')
    
def regressionfa(request):
    return render(request, 'regressionfa.html')
    
def clusteringfa(request):
    return render(request, 'clusteringfa.html')
    
def deeplearningfa(request):
    return render(request, 'deeplearningfa.html')
    
def neuralnetworkfa(request):
    return render(request, 'neuralnetworkfa.html')



################################################################################



def regressionlinear(request):
    return render(request, 'regressionlinear.html')

def regressionpolynomial(request):
    return render(request, 'regressionpolynomial.html')

def regressionlasso(request):
    return render(request, 'regressionlasso.html')
    
def regressionridge(request):
    return render(request, 'regressionridge.html')

def regressionelasticnet(request):
    return render(request, 'regressionelasticnet.html')
    
    
    
def regressionlinearfa(request):
    return render(request, 'regressionlinearfa.html')

def regressionpolynomialfa(request):
    return render(request, 'regressionpolynomialfa.html')

def regressionlassofa(request):
    return render(request, 'regressionlassofa.html')
    
def regressionridgefa(request):
    return render(request, 'regressionridgefa.html')

def regressionelasticnetfa(request):
    return render(request, 'regressionelasticnetfa.html')

    


################################################################################



def classificationsvm(request):
    return render(request, 'classificationsvm.html')

def classificationlogistic(request):
    return render(request, 'classificationlogistic.html')

def classificationnaivebayes(request):
    return render(request, 'classificationnaivebayes.html')
    
def classificationknearest(request):
    return render(request, 'classificationknearest.html')

def classificationdecisiontree(request):
    return render(request, 'classificationdecisiontree.html')

def classificationrandomforest(request):
    return render(request, 'classificationrandomforest.html')
    
    
    
def classificationsvmfa(request):
    return render(request, 'classificationsvmfa.html')

def classificationlogisticfa(request):
    return render(request, 'classificationlogisticfa.html')

def classificationnaivebayesfa(request):
    return render(request, 'classificationnaivebayesfa.html')
    
def classificationknearestfa(request):
    return render(request, 'classificationknearestfa.html')

def classificationdecisiontreefa(request):
    return render(request, 'classificationdecisiontreefa.html')

def classificationrandomforestfa(request):
    return render(request, 'classificationrandomforestfa.html')
    


################################################################################



def clusteringkmeans(request):
    return render(request, 'clusteringkmeans.html')

def clusteringdbscan(request):
    return render(request, 'clusteringdbscan.html')

def clusteringagglomerative(request):
    return render(request, 'clusteringagglomerative.html')
    
def clusteringdivisive(request):
    return render(request, 'clusteringdivisive.html')
    
    
    
def clusteringkmeansfa(request):
    return render(request, 'clusteringkmeansfa.html')

def clusteringdbscanfa(request):
    return render(request, 'clusteringdbscanfa.html')

def clusteringagglomerativefa(request):
    return render(request, 'clusteringagglomerativefa.html')
    
def clusteringdivisivefa(request):
    return render(request, 'clusteringdivisivefa.html')

    


################################################################################



def neuralnetworkperceptron(request):
    return render(request, 'neuralnetworkperceptron.html')

def neuralnetworkrecurrent(request):
    return render(request, 'neuralnetworkrecurrent.html')

def neuralnetworkconvolutional(request):
    return render(request, 'neuralnetworkconvolutional.html')
    
def neuralnetworkautoencoder(request):
    return render(request, 'neuralnetworkautoencoder.html')

def neuralnetworkdeepbelief(request):
    return render(request, 'neuralnetworkdeepbelief.html')

def neuralnetworklstm(request):
    return render(request, 'neuralnetworklstm.html')

def neuralnetworkboltzman(request):
    return render(request, 'neuralnetworkboltzman.html')
    
def neuralnetworklightgbm(request):
    return render(request, 'neuralnetworklightgbm.html')
    
def neuralnetworkadaboost(request):
    return render(request, 'neuralnetworkadaboost.html')

def neuralnetworkxgboost(request):
    return render(request, 'neuralnetworkxgboost.html')

def neuralnetworkgans(request):
    return render(request, 'neuralnetworkgans.html')
    
    
    
    
    
def neuralnetworkperceptronfa(request):
    return render(request, 'neuralnetworkperceptronfa.html')

def neuralnetworkrecurrentfa(request):
    return render(request, 'neuralnetworkrecurrentfa.html')

def neuralnetworkconvolutionalfa(request):
    return render(request, 'neuralnetworkconvolutionalfa.html')
    
def neuralnetworkautoencoderfa(request):
    return render(request, 'neuralnetworkautoencoderfa.html')

def neuralnetworkdeepbelieffa(request):
    return render(request, 'neuralnetworkdeepbelieffa.html')

def neuralnetworklstmfa(request):
    return render(request, 'neuralnetworklstmfa.html')

def neuralnetworkboltzmanfa(request):
    return render(request, 'neuralnetworkboltzmanfa.html')
    
def neuralnetworklightgbmfa(request):
    return render(request, 'neuralnetworklightgbmfa.html')
    
def neuralnetworkadaboostfa(request):
    return render(request, 'neuralnetworkadaboostfa.html')

def neuralnetworkxgboostfa(request):
    return render(request, 'neuralnetworkxgboostfa.html')

def neuralnetworkgansfa(request):
    return render(request, 'neuralnetworkgansfa.html')
    
    


################################################################################




def classification_svm_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        # Unpickle model
        model = pd.read_pickle(r"https://django3.ir/static/ml/models/classification_svm_model.pickle")
        # Make prediction
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        classification = result[0]

        ClassificationResultsSVM.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length, petal_width=petal_width, classification=classification)
        time.sleep(4)

        return JsonResponse({'result': classification, 'sepal_length': sepal_length, 'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width}, safe=False)


def classification_results_svm(request):
    # Submit prediction and show all
    data = {"dataset": ClassificationResultsSVM.objects.all()}
    return render(request, "classificationresultsvm.html", data)
    
def classification_results_svmfa(request):
    # Submit prediction and show all
    data = {"dataset": ClassificationResultsSVM.objects.all()}
    return render(request, "classificationresultsvmfa.html", data)
    
    
    

    
################################################################################






def classification_logistic_chances(request):    

    if request.POST.get('action') == 'post':

        # Receive data from client
        Pregnancies = float(request.POST.get('Pregnancies'))
        Glucose = float(request.POST.get('Glucose'))
        BloodPressure = float(request.POST.get('BloodPressure'))
        SkinThickness = float(request.POST.get('SkinThickness'))
        Insulin = float(request.POST.get('Insulin'))
        BMI = float(request.POST.get('BMI'))
        DiabetesPedigreeFunction = float(request.POST.get('DiabetesPedigreeFunction'))
        Age = float(request.POST.get('Age'))

        # Unpickle model
        model = pd.read_pickle(r"https://django3.ir/static/ml/models/classification_logistic_model.pickle")
        # Make prediction
        result = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        classification = result[0]

        ClassificationResultsLog.objects.create(Pregnancies=Pregnancies, Glucose=Glucose, BloodPressure=BloodPressure, SkinThickness=SkinThickness, Insulin=Insulin, BMI=BMI, DiabetesPedigreeFunction=DiabetesPedigreeFunction, Age=Age, classification=classification)
        time.sleep(4)

        return JsonResponse({'result': classification, 'Pregnancies': Pregnancies, 'Glucose': Glucose, 'BloodPressure': BloodPressure, 'SkinThickness': SkinThickness, 'Insulin': Insulin, 'BMI': BMI, 'DiabetesPedigreeFunction': DiabetesPedigreeFunction, 'Age': Age}, safe=False)


def classification_results_logistic(request):
    # Submit prediction and show all
    data = {"dataset": ClassificationResultsLog.objects.all()}
    return render(request, "classificationresultlogistic.html", data)
    
def classification_results_logisticfa(request):
    # Submit prediction and show all
    data = {"dataset": ClassificationResultsLog.objects.all()}
    return render(request, "classificationresultlogisticfa.html", data)




################################################################################




def classification_nb_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        Age = float(request.POST.get('Age'))
        Sex = float(request.POST.get('Sex'))
        BP = float(request.POST.get('BP'))
        Cholesterol = float(request.POST.get('Cholesterol'))
        Na_to_K = float(request.POST.get('Na_to_K'))

        # Unpickle model
        model = pd.read_pickle(r"https://django3.ir/static/ml/models/classification_NB_model.pickle")
        # Make prediction
        result = model.predict([[Age, Sex, BP, Cholesterol, Na_to_K]])

        Drug = result[0]

        ClassificationResultsNB.objects.create(Age=Age, Sex=Sex, BP=BP, Cholesterol=Cholesterol, Na_to_K=Na_to_K, Drug=Drug)
        time.sleep(4)

        return JsonResponse({'result': Drug, 'Age': Age, 'Sex': Sex, 'BP': BP, 'Cholesterol': Cholesterol, 'Na_to_K': Na_to_K}, safe=False)


def classification_results_nb(request):
    # Submit prediction and show all
    data = {"dataset": ClassificationResultsNB.objects.all()}
    return render(request, "classificationresultnb.html", data)
    
def classification_results_nbfa(request):
    # Submit prediction and show all
    data = {"dataset": ClassificationResultsNB.objects.all()}
    return render(request, "classificationresultnbfa.html", data)
    
    
    

    
################################################################################




def classification_knn_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        Temperature = float(request.POST.get('Temperature'))
        L = float(request.POST.get('L'))
        R = float(request.POST.get('R'))
        A_M = float(request.POST.get('A_M'))
        Color = float(request.POST.get('Color'))
        Spectral_Class = float(request.POST.get('Spectral_Class'))

        # Unpickle model
        model = pd.read_pickle(r"https://django3.ir/static/ml/models/classification_knn_model.pickle")
        # Make prediction
        result = model.predict([[Temperature, L, R, A_M, Color, Spectral_Class]])

        Type = result[0]

        ClassificationResultsKNearest.objects.create(Temperature=Temperature, L=L, R=R, A_M=A_M, Color=Color, Spectral_Class=Spectral_Class, Type=Type)
        time.sleep(4)

        return JsonResponse({'result': Type, 'Temperature': Temperature, 'L': L, 'R': R, 'A_M': A_M, 'Color': Color, 'Spectral_Class': Spectral_Class}, safe=False)


def classification_results_knn(request):
    # Submit prediction and show all
    data = {"dataset": ClassificationResultsKNearest.objects.all()}
    return render(request, "classificationresultknn.html", data)
    
def classification_results_knnfa(request):
    # Submit prediction and show all
    data = {"dataset": ClassificationResultsKNearest.objects.all()}
    return render(request, "classificationresultknnfa.html", data)
    
    
    

    
################################################################################




def classification_rf_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        RI = float(request.POST.get('RI'))
        Na = float(request.POST.get('Na'))
        Mg = float(request.POST.get('Mg'))
        Al = float(request.POST.get('Al'))
        Si = float(request.POST.get('Si'))
        K = float(request.POST.get('K'))
        Ca = float(request.POST.get('Ca'))
        Ba = float(request.POST.get('Ba'))
        Fe = float(request.POST.get('Fe'))

        # Unpickle model
        model = pd.read_pickle(r"https://django3.ir/static/ml/models/classification_RandomForest_model.pickle")
        # Make prediction
        result = model.predict([[RI, Na, Mg, Al, Si, K, Ca, Ba, Fe]])

        Type = result[0]

        ClassificationResultsRF.objects.create(RI=RI, Na=Na, Mg=Mg, Al=Al, Si=Si, K=K, Ca=Ca, Ba=Ba, Fe=Fe, Type=Type)
        time.sleep(10)

        return JsonResponse({'result': Type, 'RI':RI, 'Na':Na, 'Mg':Mg, 'Al':Al, 'Si':Si, 'K':K, 'Ca':Ca, 'Ba':Ba, 'Fe':Fe}, safe=False)



def classification_results_rf(request):
    # Submit prediction and show all
    data = {"dataset": ClassificationResultsRF.objects.all()}
    return render(request, "classificationresultRF.html", data)
    
def classification_results_rffa(request):
    # Submit prediction and show all
    data = {"dataset": ClassificationResultsRF.objects.all()}
    return render(request, "classificationresultRFfa.html", data)



# def classification_results_rf(request):
    
#     RI = float(request.POST.get('RI', False))    
#     Na = float(request.POST.get('Na', False))    
#     Mg = float(request.POST.get('Mg', False))    
#     Al = float(request.POST.get('Al', False))    
#     Si = float(request.POST.get('Si', False))    
#     K = float(request.POST.get('K', False))    
#     Ca = float(request.POST.get('Ca', False))    
#     Ba = float(request.POST.get('Ba', False))    
#     Fe = float(request.POST.get('Fe', False))    

#     # Unpickle model
#     model = pd.read_pickle(r"https://django3.ir/static/ml/models/classification_RandomForest_model.pickle")
#     # Make prediction
#     result = model.predict([[RI, Na, Mg, Al, Si, K, Ca, Ba, Fe]])

#     Type = result[0]

#     #ClassificationResultsRF.objects.create(RI=RI, Na=Na, Mg=Mg, Al=Al, Si=Si, K=K, Ca=Ca, Ba=Ba, Fe=Fe, Type=Type)
#     time.sleep(4)
        
#     # Submit prediction and show all
    
#     return render(request, "classificationresultRF.html", {'RI':RI, 'Na':Na, 'Mg':Mg, 'Al':Al, 'Si':Si, 'K':K, 'Ca':Ca, 'Ba':Ba, 'Fe':Fe, 'Type':Type})
    
    
    

    
################################################################################




def classification_dt_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        Weight = float(request.POST.get('Weight'))
        Length1 = float(request.POST.get('Length1'))
        Length2 = float(request.POST.get('Length2'))
        Length3 = float(request.POST.get('Length3'))
        Height = float(request.POST.get('Height'))
        Width = float(request.POST.get('Width'))

        # Unpickle model
        model = pd.read_pickle(r"https://django3.ir/static/ml/models/classification_DT_model.pickle")
        # Make prediction
        result = model.predict([[Weight, Length1, Length2, Length3, Height, Width]])

        Species = result[0]

        ClassificationResultsDT.objects.create(Weight=Weight, Length1=Length1, Length2=Length2, Length3=Length3, Height=Height, Width=Width, Species=Species)
        time.sleep(4)

        return JsonResponse({'result': Species, 'Weight': Weight, 'Length1': Length1, 'Length2': Length2, 'Length3': Length3, 'Height': Height, 'Width': Width}, safe=False)


def classification_results_dt(request):
    # Submit prediction and show all
    data = {"dataset": ClassificationResultsDT.objects.all()}
    return render(request, "classificationresultdt.html", data)
    
def classification_results_dtfa(request):
    # Submit prediction and show all
    data = {"dataset": ClassificationResultsDT.objects.all()}
    return render(request, "classificationresultdtfa.html", data)
    
    
    

    
################################################################################




def regression_linear_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        SqFt = float(request.POST.get('SqFt'))
        Bedrooms = float(request.POST.get('Bedrooms'))
        Bathrooms = float(request.POST.get('Bathrooms'))
        Offers = float(request.POST.get('Offers'))
        Brick = float(request.POST.get('Brick'))
        Neighborhood = float(request.POST.get('Neighborhood'))

        # Unpickle model
        model = pd.read_pickle(r"https://django3.ir/static/ml/models/regression_linear_model.pickle")
        # Make prediction

        result = model.predict([[SqFt, Bedrooms, Bathrooms, Offers, Brick, Neighborhood]])

        Price = round(result[0], 2)

        RegressionResultsLinear.objects.create(SqFt=SqFt, Bedrooms=Bedrooms, Bathrooms=Bathrooms, Offers=Offers, Brick=Brick, Neighborhood=Neighborhood, Price=Price)
        time.sleep(4)

        return JsonResponse({'result': Price, 'SqFt': SqFt, 'Bedrooms': Bedrooms, 'Bathrooms': Bathrooms, 'Offers': Offers, 'Brick': Brick, 'Neighborhood': Neighborhood}, safe=False)


def regression_results_linear(request):
    # Submit prediction and show all
    data = {"dataset": RegressionResultsLinear.objects.all()}
    return render(request, "regressionresultlinear.html", data)
    
def regression_results_linearfa(request):
    # Submit prediction and show all
    data = {"dataset": RegressionResultsLinear.objects.all()}
    return render(request, "regressionresultlinearfa.html", data)
    
    
    

    
################################################################################




def regression_polynomial_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        fixed_acidity = float(request.POST.get('fixed_acidity'))
        volatile_acidity = float(request.POST.get('volatile_acidity'))
        citric_acid = float(request.POST.get('citric_acid'))
        residual_sugar = float(request.POST.get('residual_sugar'))
        chlorides = float(request.POST.get('chlorides'))
        free_sulfur_dioxide = float(request.POST.get('free_sulfur_dioxide'))
        total_sulfur_dioxide = float(request.POST.get('total_sulfur_dioxide'))
        density = float(request.POST.get('density'))
        pH = float(request.POST.get('pH'))
        sulphates = float(request.POST.get('sulphates'))
        alcohol = float(request.POST.get('alcohol'))

        # Unpickle model
        model = pd.read_pickle(r"https://django3.ir/static/ml/models/regression_polynomial_model.pickle")
        # Make prediction
        
        poly = PolynomialFeatures(degree=3)

        result = model.predict(poly.fit_transform([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]]))

        quality = round(result[0], 2)

        RegressionResultsPolynomial.objects.create(fixed_acidity=fixed_acidity, volatile_acidity=volatile_acidity, citric_acid=citric_acid, residual_sugar=residual_sugar, chlorides=chlorides, free_sulfur_dioxide=free_sulfur_dioxide, total_sulfur_dioxide=total_sulfur_dioxide, density=density, pH=pH, sulphates=sulphates, alcohol=alcohol, quality=quality)
        time.sleep(5)

        return JsonResponse({'result': quality, 'fixed_acidity': fixed_acidity, 'volatile_acidity': volatile_acidity, 'citric_acid': citric_acid, 'residual_sugar': residual_sugar, 'chlorides': chlorides, 'free_sulfur_dioxide': free_sulfur_dioxide, 'total_sulfur_dioxide': total_sulfur_dioxide, 'density': density, 'pH': pH, 'sulphates': sulphates, 'alcohol': alcohol}, safe=False)


def regression_results_polynomial(request):
    # Submit prediction and show all
    data = {"dataset": RegressionResultsPolynomial.objects.all()}
    return render(request, "regressionresultpolynomial.html", data)
    
def regression_results_polynomialfa(request):
    # Submit prediction and show all
    data = {"dataset": RegressionResultsPolynomial.objects.all()}
    return render(request, "regressionresultpolynomialfa.html", data)
    
    
    

    
################################################################################




def regression_lasso_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        carat = float(request.POST.get('carat'))
        cut = float(request.POST.get('cut'))
        color = float(request.POST.get('color'))
        clarity = float(request.POST.get('clarity'))
        depth = float(request.POST.get('depth'))
        table = float(request.POST.get('table'))
        x = float(request.POST.get('x'))
        y = float(request.POST.get('y'))
        z = float(request.POST.get('z'))

        # Unpickle model
        model = pd.read_pickle(r"https://django3.ir/static/ml/models/regression_lasso_model.pickle")
        # Make prediction

        result = model.predict([[carat, cut, color, clarity, depth, table, x, y, z]])

        price = round(result[0], 2)
        
        if price < 0:
            price = 0

        RegressionResultsLasso.objects.create(carat=carat, cut=cut, color=color, clarity=clarity, depth=depth, table=table, x=x, y=y, z=z, price=price)
        time.sleep(5)

        return JsonResponse({'result': price, 'carat': carat, 'cut': cut, 'color': color, 'clarity': clarity, 'depth': depth, 'table': table, 'x': x, 'y': y, 'z': z}, safe=False)


def regression_results_lasso(request):
    # Submit prediction and show all
    data = {"dataset": RegressionResultsLasso.objects.all()}
    return render(request, "regressionresultlasso.html", data)
    
def regression_results_lassofa(request):
    # Submit prediction and show all
    data = {"dataset": RegressionResultsLasso.objects.all()}
    return render(request, "regressionresultlassofa.html", data)
    
    
    

    
################################################################################




def regression_ridge_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))
        depth = float(request.POST.get('depth'))

        # Unpickle model
        model = pd.read_pickle(r"https://django3.ir/static/ml/models/regression_ridge_model.pickle")
        
        # Make prediction
        result = model.predict([[latitude, longitude, depth]])

        magnitude = round(result[0], 2)

        RegressionResultsRidge.objects.create(latitude=latitude, longitude=longitude, depth=depth, magnitude=magnitude)
        time.sleep(5)

        return JsonResponse({'result': magnitude, 'latitude': latitude, 'longitude': longitude, 'depth': depth}, safe=False)


def regression_results_ridge(request):
    # Submit prediction and show all
    data = {"dataset": RegressionResultsRidge.objects.all()}
    return render(request, "regressionresultridge.html", data)
    
def regression_results_ridgefa(request):
    # Submit prediction and show all
    data = {"dataset": RegressionResultsRidge.objects.all()}
    return render(request, "regressionresultridgefa.html", data)
    
    
    

    
################################################################################




def regression_elasticnet_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        Age = float(request.POST.get('Age'))
        Job = float(request.POST.get('Job'))

        # Unpickle model
        model = pd.read_pickle(r"https://django3.ir/static/ml/models/regression_ElasticNet_model.pickle")
        
        # Make prediction
        result = model.predict([[Age, Job]])

        Salary = round(result[0], 2)

        RegressionResultsElasticNet.objects.create(Age=Age, Job=Job, Salary=Salary)
        time.sleep(5)

        return JsonResponse({'result': Salary, 'Age': Age, 'Job': Job}, safe=False)


def regression_results_elasticnet(request):
    # Submit prediction and show all
    data = {"dataset": RegressionResultsElasticNet.objects.all()}
    return render(request, "regressionresultelasticnet.html", data)
    
def regression_results_elasticnetfa(request):
    # Submit prediction and show all
    data = {"dataset": RegressionResultsElasticNet.objects.all()}
    return render(request, "regressionresultelasticnetfa.html", data)
    
    
    

    
################################################################################




def test(request):
    Temperature = 3500
    L = 500
    R = 800
    A_M = 11
    Color = 8
    Spectral_Class = 5

    # Unpickle model
    model = pd.read_pickle(r"https://django3.ir/static/ml/models/classification_knn_model.pickle")
    # Make prediction
    x = model.predict([[Temperature, L, R, A_M, Color, Spectral_Class]])
    result = x[0]
    return render(request, 'test.html', {'result': result})














    
    
    
    
    
    
    
    
    
    
    
