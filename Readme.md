## Picnic Hackathon

This project is inspired by Tensorflow's [tutorial](https://www.tensorflow.org/hub/tutorials/image_retraining) on Transfer learning and applied to [Picnic's dataset](https://picnic.devpost.com/)

## How to Run?

1. Download and unzip the data from devpost
2. Run following script to re-arrange training data

```
python main.py
```

3. Training Model

```
python retrain.py --image_dir data
```

To train with different parameters

```
python retrain.py -h
```

To augment data, please check augment.py which uses [Augmenter](https://augmentor.readthedocs.io/en/master/userguide/usage.html)

4. Label Test data

```
python label_image.py
```
