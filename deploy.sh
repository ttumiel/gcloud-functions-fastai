echo "Ensure you have run `gcloud init` before running this"
echo "-----------------------------------------------------"
echo "Deploying text endpoint function"
gcloud functions deploy text_endpoint --runtime python37 --trigger-http