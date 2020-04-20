# Tensorflow 101
Explore and keep track of various scripts to best use Tensorflow

This repo collects scripts create to experiment with Tensorflow (2.10) in various use-case. Many of the script are created as personal exercise notepad of the following courses:

- Machine Learning with TensorFlow on Google Cloud Platform Specialization
- Advanced Machine Learning with TensorFlow on Google Cloud Platform Specialization

The main goal is to explore the best practices to usage of Tensorflow as model development and production framework

---

## TensorFlow Installation Issue

In case of the following error:

>ImportError: DLL load failed: The specified module could not be found.
>Failed to load the native TensorFlow runtime.
>See https://www.tensorflow.org/install/errors
>for some common reasons and solutions. Include the entire stack trace
>above this error message when asking for help.

Possible solutions are:
- You need to install the MSVC 2019 redistributable
- Your CPU does not support AVX2 instructions
- Your CPU/Python is on 32 bits
- There is a library that is in a different location/not installed on your system that cannot be loaded.
