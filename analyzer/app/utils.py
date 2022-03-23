def ner_report(outputs):
    tag_dict = {
        "B-date": "date",
        "B-event": "event",
        "B-facility": "facility",
        "B-location": "location",
        "B-money": "money",
        "B-organization": "organization",
        "B-percent": "percent",
        "B-person": "person",
        "B-product": "product",
        "B-time": "time",
        "I-date": "date",
        "I-event": "event",
        "I-facility": "facility",
        "I-location": "location",
        "I-money": "money",
        "I-organization": "organization",
        "I-percent": "percent",
        "I-person": "person",
        "I-product": "product",
        "I-time": "time",
        "O": "O",
    }
    report_entity = {
        "date": [],
        "event": [],
        "facility": [],
        "location": [],
        "money": [],
        "organization": [],
        "percent": [],
        "person": [],
        "product": [],
        "time": [],
    }
    output = outputs[0]
    output_entity = output["entity"]
    phrase_tag = tag_dict[output["entity"]]
    I_B = output_entity.split("-")
    recognized_phrase = str(output["word"] + " ")
    GO = True
    curser = 0
    while GO:
        curser += 1
        if curser != len(outputs):
            output_entity = outputs[curser]["entity"]
            I_B = output_entity.split("-")
            if I_B[0] == "I" and I_B[1] == phrase_tag:
                recognized_phrase += str(outputs[curser]["word"] + " ")
            if I_B[0] == "B":
                report_entity[phrase_tag].append(recognized_phrase)
                phrase_tag = tag_dict[outputs[curser]["entity"]]
                recognized_phrase = str(outputs[curser]["word"] + " ")
        else:
            report_entity[phrase_tag].append(recognized_phrase)
            GO = False
    return report_entity
