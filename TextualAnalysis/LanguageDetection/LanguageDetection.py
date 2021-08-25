from TextualAnalysis.LanguageDetection.common.detect_lang import detect_lang, map_lang_name

class GetLanguage():

    def language_detection(self, text):
        # Store language detection results
        lang_results = []

        # Iterating through data
        for line in text.split('\n')[:10]:
            columns = line.split('\t')
            columns = [col.strip() for col in columns]
            language = detect_lang(columns[1])
            lang_details = map_lang_name(language)
            lang_results.append(lang_details)

        # Flatten list of multiple lists into one
        lang_results = [i for n, i in enumerate(lang_results) if i not in lang_results[n + 1:]]

        return {'lang_detected': lang_results}
