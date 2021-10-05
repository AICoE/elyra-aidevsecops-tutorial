# Neural Magic

[Neural Magic][1]’s novel algorithms enable convolutional neural networks to run on commodity CPUs – at GPU speeds and better. Data scientists no longer have to compromise on model design and input size, or deal with scarce and costly GPU resources. [Neural Magic][1] is making the power of deep learning simple, accessible, and affordable for anyone.

[Neural Magic][1]’s Deep Sparse architecture is designed to mimic, on commodity hardware, the way brains compute. It uses neural network sparsity combined with locality of communication by utilizing the CPU’s large fast caches and its very large memory.

Sparsification through pruning is a broadly studied ML technique, allowing reductions of 10x or more in the size and the theoretical compute needed to execute a neural network, without losing much accuracy. So, while a GPU runs networks faster using more FLOPs, [Neural Magic][1] runs them faster via a reduction in the necessary FLOPs.

## Sparsification
Sparsification is the process of taking a trained deep learning model and removing redundant information from the overprecise and over-parameterized network resulting in a faster and smaller model. Techniques for sparsification are all encompassing including everything from inducing sparsity using pruning and quantization to enabling naturally occurring sparsity using activation sparsity or winograd/FFT . When implemented correctly, these techniques result in significantly more performant and smaller models with limited to no effect on the baseline metrics.

## Software Components
The Deep Sparse product suite builds on top of sparsification enabling you to easily apply the techniques to your datasets and models using recipe-driven approaches. Recipes encode the directions for how to sparsify a model into a simple, easily editable format.

- Download a sparsification recipe and sparsified model from the [SparseZoo][2].

- Alternatively, create a recipe for your model using [Sparsify][3].

- Apply your recipe with only a few lines of code using [SparseML][4].

- Finally, for GPU-level performance on CPUs, deploy your sparse-quantized model with the [DeepSparse Engine][5].

Sparsify and SparseML tools allow us to easily reach industry leading levels of sparsity while preserving baseline accuracy, and the DeepSparse Engine’s breakthrough sparse kernels execute this computation effectively.


## Steps implemented to deploy custom Neural Magic model in this tutorial

1. Train your model.
2. Convert the model to [ONNX][6] model.
3. Create a recipe for your model deploying locally [Sparsify][3]. (manual step already performed you can find the recipe [here](../../models/pytorch-nm-mnist-recipe.yaml)). If you are interested in repeating that step, you can follow the documentation [here](https://github.com/neuralmagic/sparsify)
4. Train the model with [Neural Magic][1] optimizer ([SparseML][4]).
5. Convert the model to [ONNX][6] model.
6. Deploy with [Neural Magic][1] [DeepSparse Engine][5].

## Next Step

- [Explore notebooks for Neural Magic](./mnist-classification-application-pytorch-neuralmagic.md)

## References

* [Neural Magic][1]
* [SparseZoo][2]
* [Sparsify][3]
* [SparseML][4]
* [DeepSparse Engine][5]
* [ONNX][6]


[1]: https://neuralmagic.com/
[2]: https://github.com/neuralmagic/sparsezoo
[3]: https://github.com/neuralmagic/sparsify
[4]: https://github.com/neuralmagic/sparseml
[5]: https://github.com/neuralmagic/deepsparse
[6]: https://onnx.ai/
