# Persian text analyzer
NER, Sentiment, Classification in Persian text by prepared Pytorch model


## Usage

1. First [download](https://foveo-video.s3.ca-central-1.amazonaws.com/stream/ner_pytorch_model.bin) the model and put it into model folder.
2. Use docker-compose to setup container by bellow command:
```
docker-compose up
```
3. Get into container by bellow command:
```
docker exec -it persian_ner bash
```
4. Run main code by:
```
python ner.py
```


