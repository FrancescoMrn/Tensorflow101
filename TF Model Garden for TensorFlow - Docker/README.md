# TF Model Garden for TensorFlow


This repo implements Model Garden for TensorFlow inside a docker container in this readme is reported a short guide to run quickly APIs like:

- Tensorflow Object Detection API

### Local Environment Instructions

1. Clone the repository, and navigate to the downloaded folder. This may take a minute due to the data inside the repo.
```
git clone https://github.com/FrankMrn/Tensorflow101.git
cd TensorFlow101/TF Model Garden for TensorFlow - Docker/docker/cpu
```
or in case your environment has Nvidia drivers
```
cd TensorFlow101/TF Model Garden for TensorFlow - Docker/docker/gpu
```

2. Compile docker file
```
docker-compose up
```
This command will create the docker image starting from the DOCKERFILE

3. Git clone Model Garden for TensorFlow
Download Model Garden for TensorFlow repo in your local host
```
git clone https://github.com/tensorflow/models.git
```

4. Run docker.
Run docker container with the connection to the repository cloned in the local host to allow data/code transfer.
```
docker run -p 8888:8888 --mount type=bind,source=<path-to-Model Garden for TensorFlow-repo>,target=/models/ cpu_tensorflow_object_detection_api
```

### Credits

Here the original repo containing the original docker file: https://github.com/TannerGilbert/Tensorflow-Object-Detection-API-Train-Model
