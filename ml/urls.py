from django.urls import path
from . import views

app_name = "ml"

urlpatterns = [
    path('classification/', views.classification, name='classification'),
    path('regression/', views.regression, name='regression'),
    path('clustering/', views.clustering, name='clustering'),
    path('deeplearning/', views.deeplearning, name='deeplearning'),
    path('neuralnetwork/', views.neuralnetwork, name='neuralnetwork'),
    
    path('classificationfa/', views.classificationfa, name='classificationfa'),
    path('regressionfa/', views.regressionfa, name='regressionfa'),
    path('clusteringfa/', views.clusteringfa, name='clusteringfa'),
    path('deeplearningfa/', views.deeplearningfa, name='deeplearningfa'),
    path('neuralnetworkfa/', views.neuralnetworkfa, name='neuralnetworkfa'),
    
    
    
    path('classificationsvm/', views.classificationsvm, name='classificationsvm'),
    path('classificationlogistic/', views.classificationlogistic, name='classificationlogistic'),
    path('classificationnaivebayes/', views.classificationnaivebayes, name='classificationnaivebayes'),
    path('classificationknearest/', views.classificationknearest, name='classificationknearest'),
    path('classificationdecisiontree/', views.classificationdecisiontree, name='classificationdecisiontree'),
    path('classificationrandomforest/', views.classificationrandomforest, name='classificationrandomforest'),
    
    path('classificationsvmfa/', views.classificationsvmfa, name='classificationsvmfa'),
    path('classificationlogisticfa/', views.classificationlogisticfa, name='classificationlogisticfa'),
    path('classificationnaivebayesfa/', views.classificationnaivebayesfa, name='classificationnaivebayesfa'),
    path('classificationknearestfa/', views.classificationknearestfa, name='classificationknearestfa'),
    path('classificationdecisiontreefa/', views.classificationdecisiontreefa, name='classificationdecisiontreefa'),
    path('classificationrandomforestfa/', views.classificationrandomforestfa, name='classificationrandomforestfa'),
    
    
    
    path('regressionlinear/', views.regressionlinear, name='regressionlinear'),
    path('regressionpolynomial/', views.regressionpolynomial, name='regressionpolynomial'),
    path('regressionlasso/', views.regressionlasso, name='regressionlasso'),
    path('regressionridge/', views.regressionridge, name='regressionridge'),
    path('regressionelasticnet/', views.regressionelasticnet, name='regressionelasticnet'),
    
    path('regressionlinearfa/', views.regressionlinearfa, name='regressionlinearfa'),
    path('regressionpolynomialfa/', views.regressionpolynomialfa, name='regressionpolynomialfa'),
    path('regressionlassofa/', views.regressionlassofa, name='regressionlassofa'),
    path('regressionridgefa/', views.regressionridgefa, name='regressionridgefa'),
    path('regressionelasticnetfa/', views.regressionelasticnetfa, name='regressionelasticnetfa'),
    
    
    
    
    path('clusteringkmeans/', views.clusteringkmeans, name='clusteringkmeans'),
    path('clusteringdbscan/', views.clusteringdbscan, name='clusteringdbscan'),
    path('clusteringagglomerative/', views.clusteringagglomerative, name='clusteringagglomerative'),
    path('clusteringdivisive/', views.clusteringdivisive, name='clusteringdivisive'),
    
    path('clusteringkmeansfa/', views.clusteringkmeansfa, name='clusteringkmeansfa'),
    path('clusteringdbscanfa/', views.clusteringdbscanfa, name='clusteringdbscanfa'),
    path('clusteringagglomerativefa/', views.clusteringagglomerativefa, name='clusteringagglomerativefa'),
    path('clusteringdivisivefa/', views.clusteringdivisivefa, name='clusteringdivisivefa'),
    
    
    
    
    path('neuralnetworkperceptron/', views.neuralnetworkperceptron, name='neuralnetworkperceptron'),
    path('neuralnetworkrecurrent/', views.neuralnetworkrecurrent, name='neuralnetworkrecurrent'),
    path('neuralnetworkconvolutional/', views.neuralnetworkconvolutional, name='neuralnetworkconvolutional'),
    path('neuralnetworkautoencoder/', views.neuralnetworkautoencoder, name='neuralnetworkautoencoder'),
    path('neuralnetworkdeepbelief/', views.neuralnetworkdeepbelief, name='neuralnetworkdeepbelief'),
    path('neuralnetworklstm/', views.neuralnetworklstm, name='neuralnetworklstm'),
    path('neuralnetworkboltzman/', views.neuralnetworkboltzman, name='neuralnetworkboltzman'),
    path('neuralnetworklightgbm/', views.neuralnetworklightgbm, name='neuralnetworklightgbm'),
    path('neuralnetworkadaboost/', views.neuralnetworkadaboost, name='neuralnetworkadaboost'),
    path('neuralnetworkxgboost/', views.neuralnetworkxgboost, name='neuralnetworkxgboost'),
    path('neuralnetworkgans/', views.neuralnetworkgans, name='neuralnetworkgans'),
    
    path('neuralnetworkperceptronfa/', views.neuralnetworkperceptronfa, name='neuralnetworkperceptronfa'),
    path('neuralnetworkrecurrentfa/', views.neuralnetworkrecurrentfa, name='neuralnetworkrecurrentfa'),
    path('neuralnetworkconvolutionalfa/', views.neuralnetworkconvolutionalfa, name='neuralnetworkconvolutionalfa'),
    path('neuralnetworkautoencoderfa/', views.neuralnetworkautoencoderfa, name='neuralnetworkautoencoderfa'),
    path('neuralnetworkdeepbelieffa/', views.neuralnetworkdeepbelieffa, name='neuralnetworkdeepbelieffa'),
    path('neuralnetworklstmfa/', views.neuralnetworklstmfa, name='neuralnetworklstmfa'),
    path('neuralnetworkboltzmanfa/', views.neuralnetworkboltzmanfa, name='neuralnetworkboltzmanfa'),
    path('neuralnetworklightgbmfa/', views.neuralnetworklightgbmfa, name='neuralnetworklightgbmfa'),
    path('neuralnetworkadaboostfa/', views.neuralnetworkadaboostfa, name='neuralnetworkadaboostfa'),
    path('neuralnetworkxgboostfa/', views.neuralnetworkxgboostfa, name='neuralnetworkxgboostfa'),
    path('neuralnetworkgansfa/', views.neuralnetworkgansfa, name='neuralnetworkgansfa'),
    
    
    
    
    path('submitclassificationsvm/', views.classification_svm_chances, name='submit_classification_svm'),
    path('classificationresultsvm/', views.classification_results_svm, name='classificationresultsvm'),
    path('classificationresultsvmfa/', views.classification_results_svmfa, name='classificationresultsvmfa'),
    
    path('submitclassificationlogistic/', views.classification_logistic_chances, name='submit_classification_logistic'),
    path('classificationresultlogistic/', views.classification_results_logistic, name='classificationresultlogistic'),
    path('classificationresultlogisticfa/', views.classification_results_logisticfa, name='classificationresultlogisticfa'),
    
    path('submitclassificationnb/', views.classification_nb_chances, name='submit_classification_nb'),
    path('classificationresultnb/', views.classification_results_nb, name='classificationresultnb'),
    path('classificationresultnbfa/', views.classification_results_nbfa, name='classificationresultnbfa'),
    
    path('submitclassificationknn/', views.classification_knn_chances, name='submit_classification_knn'),
    path('classificationresultknn/', views.classification_results_knn, name='classificationresultknn'),
    path('classificationresultknnfa/', views.classification_results_knnfa, name='classificationresultknnfa'),
    
    path('submitclassificationrf/', views.classification_rf_chances, name='submit_classification_rf'),
    path('classificationresultrf/', views.classification_results_rf, name='classificationresultrf'),
    path('classificationresultrffa/', views.classification_results_rffa, name='classificationresultrffa'),
    
    path('submitclassificationdt/', views.classification_dt_chances, name='submit_classification_dt'),
    path('classificationresultdt/', views.classification_results_dt, name='classificationresultdt'),
    path('classificationresultdtfa/', views.classification_results_dtfa, name='classificationresultdtfa'),
    
    path('submitregressionlinear/', views.regression_linear_chances, name='submit_regression_linear'),
    path('regressionresultlinear/', views.regression_results_linear, name='regressionresultlinear'),
    path('regressionresultlinearfa/', views.regression_results_linearfa, name='regressionresultlinearfa'),
    
    path('submitregressionpolynomial/', views.regression_polynomial_chances, name='submit_regression_polynomial'),
    path('regressionresultpolynomial/', views.regression_results_polynomial, name='regressionresultpolynomial'),
    path('regressionresultpolynomialfa/', views.regression_results_polynomialfa, name='regressionresultpolynomialfa'),
    
    path('submitregressionlasso/', views.regression_lasso_chances, name='submit_regression_lasso'),
    path('regressionresultlasso/', views.regression_results_lasso, name='regressionresultlasso'),
    path('regressionresultlassofa/', views.regression_results_lassofa, name='regressionresultlassofa'),
    
    path('submitregressionridge/', views.regression_ridge_chances, name='submit_regression_ridge'),
    path('regressionresultridge/', views.regression_results_ridge, name='regressionresultridge'),
    path('regressionresultridgefa/', views.regression_results_ridgefa, name='regressionresultridgefa'),
    
    path('submitregressionelasticnet/', views.regression_elasticnet_chances, name='submit_regression_elasticnet'),
    path('regressionresultelasticnet/', views.regression_results_elasticnet, name='regressionresultelasticnet'),
    path('regressionresultelasticnetfa/', views.regression_results_elasticnetfa, name='regressionresultelasticnetfa'),
    
    
    path('test/', views.test, name='test'),
    
]



















