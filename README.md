# Serverless Google Cloud PyTorch/Fastai Models

Deploy a Google Cloud function that serves predictions from PyTorch and Fastai models.

## The trained model

Save your trained learner object and its related transforms, metrics, etc. with the method `learn.export()`. Put your exported learner object in the `data` folder. The default name is `export.pkl`.

If your model is larger than 50MB, you will have to adjust the amount of memory available to the cloud function by adding the flag `--memory` to the `deploy.sh` script. Possible values are 128MB, 256MB, 512MB, 1024MB, and 2048MB. The dependencies take approximately 200MB of space, so please adjust for that.

Deploy a Google Cloud function that serves predictions.
