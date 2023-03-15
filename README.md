gcloud builds submit --tag gcr.io/summarizer-380412/summary-test-00003-qes  --project=summarizer-380412

gcloud run deploy --image gcr.io/summarizer-380412/summary-test-00003-qes --platform managed  --project=summarizer-380412 --allow-unauthenticated