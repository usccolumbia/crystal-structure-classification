# Identification of Crystal Symmetry from Noisy Diffraction Patterns by A Shape Analysis and Deep Learning

### Introduction
This work contributes a novel descriptor Shaped Diffraction Pattern (Shaped DP) and Multi-stream DenseNet (MSDN) for crystal structure classification.

We also provide the codes as follows:
  1) Shaped DP (see [Descriptor](https://github.com/tiongleslie/crystal-structure-classification/tree/master/Descriptor))
  2) Pre-trained model of MSDN (see [MSDN](https://github.com/tiongleslie/crystal-structure-classification/tree/master/MSDN))

### Compatibility
We tested the codes with:
  1) Tensorflow-GPU 1.13.1 under Ubuntu 18.04 and Anaconda3 (Python 3.7)
  1) Tensorflow-GPU 1.13.1/Tensorflow 1.13.1 under Windows 10 and Anaconda3 (Python 3.7)

### Requirements
  1) [Anaconda3](https://www.anaconda.com/distribution/#download-section)
  2) [TensorFlow-GPU 1.13.1 or Tensorflow 1.13.1](https://www.tensorflow.org/install/pip)
  3) [PIL](https://anaconda.org/anaconda/pillow)
  4) [NatSort](https://pypi.org/project/natsort/)
  5) [SciPy](https://anaconda.org/anaconda/scipy)
  6) [Matplotlib](https://anaconda.org/conda-forge/matplotlib)
  7) [Numpy 1.16.4](https://pypi.org/project/numpy/1.16.4/)
 
### Sample code
#### Shaped DP
- Run the code `test_descriptor.py` in [Descriptor](https://github.com/tiongleslie/crystal-structure-classification/tree/master/Descriptor)
```shell
$ python test_descriptor.py
```

#### Pre-trained model: MSDN
- Run the code `test_MSDN.py` in [MSDN](https://github.com/tiongleslie/crystal-structure-classification/tree/master/MSDN)
```shell
$ python test_MSDN.py --batch_size 16 --plot_sample 0
```

### Dataset
The dataset is shared on [Google Drive](https://drive.google.com/drive/folders/1l7n6khjbbUB6cRS-xwlYw5xbyOphXBn6).

### Citation
Please cite us if you are using our model in your research works: <br />

[1] Leslie Ching Ow Tiong, Jeongrae Kim, Sang Soo Han and Donghun Kim, "Identification of crystal symmetry from noisy diffraction patterns by a shape analysis and deep learning," *arXiv*:2005.12476, 2020. (See [link](https://arxiv.org/abs/2005.12476)).
