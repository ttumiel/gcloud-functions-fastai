# Serverless Google Cloud Fastai/PyTorch Models

Deploy a Google Cloud function that serves predictions from Fastai models.

## The trained model

Save your trained learner object and its related transforms, metrics, etc. with the method `learn.export()`. Put your exported learner object in the `data` folder. The default name is `export.pkl`.

If your model is larger than 50MB, you will have to adjust the amount of memory available to the cloud function by adding the flag `--memory` to the `deploy.sh` script. Possible values are 128MB, 256MB, 512MB, 1024MB, and 2048MB. The dependencies take approximately 200MB of space, so please adjust for that.

## Tutorial

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tom2718/gcloud-functions-fastai/blob/master/tutorial.ipynb)

### Requirements

#### Local Computer

- [gcloud SDK](https://cloud.google.com/sdk/)
- A Google cloud account with billing enabled

#### Cloud
Google Cloud functions runs Python 3.7.1 on Ubuntu 18.04.

### Set up

After installing the `gcloud` CLI tool, run `gcloud init` to create and create a new project by simply following the prompts. This project will be where your cloud function will be kept so name it appropriately. Alternatively, you can select an existing project from the list. 

### Model data

Save your fastai model using `learn.export()` and place it in the data folder. You should create a function that calls the predict method appropriately from the loaded model. See the `utils.py` file for example of text generation and classification.

### Deploying

Once you have a function that can generate predictions, create a function in `main.py` which will call your prediction method and decorate the function with the `endpoint` decorator. This will provide parsed data to your method for prediction. To deploy your function to the same cloud project, simply run the following, replacing YOUR_FUNCTION with the name of your function.

```sh
gcloud functions deploy YOUR_FUNCTION --runtime python37 --trigger-http
```

### Function Status

Deploying your function will fail if your saved model is >50MB. This can be corrected by logging in to Google cloud, opening functions from the menu and editing your function's memory to a suitable amount. The dependencies take approximately 200MB of space, so adjust accordingly.

### Pricing

Functions provides a decent free tier, with the first 2 million invocations being free.

See the [full pricing docs here](https://cloud.google.com/functions/pricing)

### Test the function

To test the function, find the endpoint link that is specified on the function page. You can use a query string to send data in the function call or post data to the function using a REST API tool.
