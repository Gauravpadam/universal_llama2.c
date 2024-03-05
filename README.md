# Universal LLAMA2.c
This is a fork of [Andrej Karpathy's llama2.c](https://github.com/karpathy/llama2.c) with the refactorization of training the model on your own dataset

## How to use this repository
1. Clone or fork & clone
1. Setup the environment variable (.env) by referring to the .env.sample file provided
1. Run the following commands
```
python universal_stager.py download
python universal_stager.py pretokenize
 ```

Now, your dataset is ready

Run the command:
```
python train.py
```
To train the model on your local machine with low computational power

You can also switch from `CPU` to `CUDA`, See `train.py` to understand



 
