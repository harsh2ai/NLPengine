from transformers import AutoTokenizer,AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-emotion")

model = AutoModelForSeq2SeqLM.from_pretrained("mrm8488/t5-base-finetuned-emotion")


class EmotionDetections:


    
  def detect_emotion(self,text):
     
      input_ids=tokenizer.encode(text+'</s>',return_tensors='pt')
      output=model.generate(input_ids=input_ids,max_length=2)

      dec = [tokenizer.decode(ids) for ids in output]
      label=dec[0]
      label=label.replace("<pad>","")
      return label

