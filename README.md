# Tensorflow 101


This repo is a collection of notebooks created with the idea of explore the usage of TensorFlow 2.2. Many of the scripts are created as personal exercise notepad of the following two Coursera courses:

- [TensorFlow in Practice Specialization](https://www.coursera.org/specializations/tensorflow-in-practice)
- [Machine Learning with TensorFlow on Google Cloud Platform Specialization](https://www.coursera.org/specializations/machine-learning-tensorflow-gcp)

The code reported in this repository is manipulated both maintain the initial goals of the starting notebook and include new (small) challenge in the application of the code to different datasets.

The ultimate goal is to explore the best practices to use best Tensorflow as both development and production framework.

### Local Environment Instructions

1. Clone the repository, and navigate to the downloaded folder. This may take a minute due to the data inside the repo.
```
git clone https://github.com/FrankMrn/Tensorflow101.git
cd TensorFlow101
```

2. Create a conda environment, with Python 3.6. If prompted to proceed with the install `(Proceed [y]/n)` type y.

	- __Linux__ or __Mac__:
	```
	conda create -n <your-new-environment-name> python=3.6
	source activate <your-new-environment-name>
	```
	- __Windows__:
	```
	conda create --name <your-new-environment-name> python=3.6
	activate <your-new-environment-name>
	```

3. Install Tensorflow and all the other packages

	- __Linux__ or __Mac__:
	```
	conda install pandas, scikit-learn, numpy
  pip install --upgrade tensorflow
	```
	- __Windows__:
	```
  conda install pandas, scikit-learn, numpy
  pip install --upgrade tensorflow
	```

4. Install a few required pip packages.
```
pip install -r requirements.txt
```


### Data

All of the data you'll need to train a neural network are reported inside the relevant courses folder. Specifically inside the subdirectory `data`. In this folder are training and tests set (if split already). The data are publically available on kaggle:

- [Avocado prices](https://www.kaggle.com/neuromusic/avocado-prices)

### TensorFlow import errors

In case of the following error:

>ImportError: DLL load failed: The specified module could not be found.
>Failed to load the native TensorFlow runtime.
>See https://www.tensorflow.org/install/errors
>for some common reasons and solutions. Include the entire stack trace
>above this error message when asking for help.

Possible solutions are:
- You need to install the [MSVC 2019 redistributable](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)
- Your CPU does not support AVX2 instructions
- Your CPU/Python is on 32 bits
- There is a library that is in a different location/not installed on your system that cannot be loaded.
