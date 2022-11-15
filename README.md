# Logistic-Regression-from-Scratch-with-PyRorch
Demonstration of binomial classification with logistic regression as the primary building block for neural networks. This project also demonstrates the utility of cloud-based resources for simiplicity and enhanced computing power via GPU usage.

This Google Colab notebook contains code for an image classifier using logistic regression. The SEN12FLOOD dataset (https://ieee-dataport.org/open-access/sen12-flood-sar-and-multispectral-dataset-flood-detection) is utilized for training and validating the model. Specifically, the logistic regression classifies images of the dataset as "flooding" or "not flooding". Accuracy in the range of 70% is achieved. Higher accuracy values are likely hindered because of the small size of the extracted dataset which contains 304 training and 77 testing instances. Accuracy could very well be improved through hyperparameter tuning, increasing the amount of training and testing instances, and by trying a different data transformation method.

Such models are useful when reliable binomial classification of large numbers of images is required. 
