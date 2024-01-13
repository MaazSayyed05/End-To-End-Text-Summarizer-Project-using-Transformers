from Text_Summarizer.config import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfiguraitonManager().get_model_evaluation_config()

    
    def predict(self,text):
        
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 130}  ## max_length: no. of chars in summary

        pipe = pipeline("summarization", model=self.config.model_path,tokenizer=tokenizer)

        
        ##
        print("Dialogue:")
        print(text)

        output = pipe(sample_text, **gen_kwargs)[0]["summary_text"]

        # print("\nReference Summary:")
        # print(reference)


        print("\nModel Summary:")
        print(output)

        return output
