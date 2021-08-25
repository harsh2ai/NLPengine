from TextualAnalysis.EntityRecognition.common.get_entities import entity_details


class GetEntity():

    def get_ner(self, text):

        # Store entity recognition results
        entity_results = []

        # Iterating through data
        for line in text.split('\n')[:10]:
            columns = line.split('\t')
            columns = [col.strip() for col in columns]
            entity_results.append(entity_details(columns[1]))

        # Flatten list of multiple lists into one
        entity_results = [item for sublist in entity_results for item in sublist]

        ner_detected = []

        # Capture details of ner detected
        for ner_data in entity_results:

            # If score of ner is less than 90%, discard
            if ner_data['score'] >= 0.90:
                # Pass details as output
                ner_detected.append({'entity': ner_data['entity'],
                                     'word': ner_data['word'],
                                     'recognition_score': ner_data['score'],
                                     'word_index': {'index': ner_data['index'],
                                                    'start_loc': ner_data['start'],
                                                    'end_loc': ner_data['end']}})
        return {'ner_detected': ner_detected}
