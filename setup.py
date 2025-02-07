from setuptools import setup, Extension
import pybind11
import torch
import os

# Encuentra la ruta de los headers de PyTorch manualmente
torch_include = os.path.join(torch.__path__[0], 'include')

torch_include_paths = [torch_include, os.path.join(torch_include, 'torch/csrc/api/include')]

ext_modules = [
    Extension(
        name="chinese_whispers",
        sources=["chinese_whispers.cpp"],
        include_dirs=[pybind11.get_include()] + torch_include_paths,
        language="c++",
        extra_compile_args=["-std=c++17", "-O3"],
    )
]

setup(
    name="chinese_whispers",
    ext_modules=ext_modules,
)
