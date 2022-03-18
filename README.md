# Persian text analyzer
NER, Sentiment, Classification in Persian text by using prepared Pytorch model


## Usage

1. First of all you need to download the prepared models. Each task has it's own model. After downloading them, you should put them into related folders.

 - [NER Model](https://foveo-video.s3.ca-central-1.amazonaws.com/stream/models/ner/pytorch_model.bin)

 - [Sentiment Model](https://foveo-video.s3.ca-central-1.amazonaws.com/stream/models/sentiment/pytorch_model.bin)

 - [Classification Model](https://foveo-video.s3.ca-central-1.amazonaws.com/stream/models/classification/pytorch_model.bin)

2. Use docker-compose to setup Django container by bellow command:
```
docker-compose up
```
4. Now, Django app is ready to use. Three APIs are available:
- `http://localhost:8040/v1/app/ner/`
- `http://localhost:8040/v1/app/sentiment/`
- `http://localhost:8040/v1/app/classification/`

You should send POST request with text field in the body.