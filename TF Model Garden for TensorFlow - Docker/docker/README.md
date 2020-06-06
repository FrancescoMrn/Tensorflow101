# Using the Tensorflow Object Detection API with Docker

This folder contains Docker images for both the CPU and GPU installations for the Tensorflow Object Detection API.
In this version some changes have been performed to allow fast integration with the host machine

## GPU

To run Tensorflow Object Detection API with a GPU you need a NVIDIA graphics card. To be able to access a graphics card with Docker you also need to install [Nvidia-Docker](https://github.com/NVIDIA/nvidia-docker).

## CPU

If you don't have a GPU or you don't have a NVIDIA GPU you'll have to run the CPU version, which uses [Ubuntu](https://hub.docker.com/_/ubuntu) as the base image instead of [Nvidia-Cuda](https://hub.docker.com/r/nvidia/cuda). For this container you don't need [Nvidia-Docker](https://github.com/NVIDIA/nvidia-docker).

## Run an container

To run a container you need to move into the right  directory and then execute ```docker-compose up```.

## Credits

Here the original repo containing the origial docker files: https://github.com/TannerGilbert/Tensorflow-Object-Detection-API-Train-Model
