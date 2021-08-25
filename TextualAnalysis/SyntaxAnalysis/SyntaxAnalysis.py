from TextualAnalysis.SyntaxAnalysis.common.get_syntax_analysis import NLPStanzaAnalysis


class GetSyntax():

    def syntax_analysis(self, text):
        # Store language detection results
        syntax_analysis_result = []

        # Iterating through data
        for line in text.split('\n')[:10]:
            columns = line.split('\t')
            columns = [col.strip() for col in columns]
            nlp_s = NLPStanzaAnalysis()
            syntax_analysis_result.append({'text': columns[1], 'per_analysis': nlp_s.percentage_analysis(columns[1])})

        return {'syntax_analysis': syntax_analysis_result}
