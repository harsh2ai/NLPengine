from TextualAnalysis.TopicModeling.common.get_topic import *


class GetTopic():

    def topicmodeling(self, text):
        topic_model_result = []

        # Iterating through data
        for line in text.split('\n')[:10]:
            columns = line.split('\t')
            columns = [col.strip() for col in columns]

            tm = TopicModel.topic_modelling(columns[1])
            topic_model_result.append({'text': columns[1],
                                       'topics': tm[0],
                                       'topic_dist': tm[1]})

        return {'topic_analysis': topic_model_result}
