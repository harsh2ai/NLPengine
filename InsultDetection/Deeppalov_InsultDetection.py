from deeppavlov import configs, build_model

model = build_model(configs.classifiers.insults_kaggle_bert, download=True)


class InsultDetection():

    def detect_insult(self, text):
        return model(text)

    def get_insult_detection(self, text):
        insult_detection_analysis = []

        # Iterating through data
        for line in text.split('\n')[:10]:
            columns = line.split('\t')
            columns = [col.strip() for col in columns]
            insult_detection_analysis.append({columns[1]: set(InsultDetection.detect_insult(columns[1]))})

        return {'insult_detection': insult_detection_analysis}
