# Packaging with Spack

Repository for the [Spack exercise](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/spack_exercise.md). The code is a slightly modified version of the [code used in the CMake exercise](https://github.com/Simulation-Software-Engineering/cmake-exercise).

The directory `docker/` contains the recipe of the Docker image that has been prepared for the exercise. Build a Docker image from the recipe and start a container from this image.

The manatory exercise solution can be found in the folder `mandatory` and the solution for the optional exercise can be found in the folder `optional`.

The flags to enable or disable `boost` and `yaml-cpp` are:

Enable boost: `+boost`, disable boost: `~boost`.
Enable yaml-cpp: `+yamlcpp`, disable boost: `~yamlcpp`.

Notice that the optional solution uses a release on my fork so you need to execute:

```bash
spack create https://github.com/FelixKimmerle/spack-exercise/archive/refs/tags/v0.3.4.tar.gz
```
