from datasets import load_dataset, load_from_disk

from transformers import AutoModelForSeq2SeqLM,   AutoTokenizer
from transformers import DataCollatorForSeq2Seq
from transformers import TrainingArguments, Trainer

import torch

# pip install --upgrade accelerate
# pip uninstall -y transformers accelerate
# pip install transformers accelerate

from Text_Summarizer.entity import ModelTrainerConfig



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu' ## To check GPU is connected or not
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer,model=model_pegasus)

        # Load Dataset
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=1e6,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        )

        # trainer_args = TrainingArguments(
        #     output_dir = 'pegasus-samsum',
        #     num_train_epochs = 1,
        #     warmup_steps = 500,
        #     per_device_train_batch_size = 1,
        #     per_device_eval_batch_size = 1,
        #     weight_decay = 0.01,
        #     logging_steps = 10,
        #     evaluation_strategy = 'steps',
        #     eval_steps = 500,
        #     save_steps = 1e6,
        #     gradient_accumulation_steps = 16
        # )


        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            data_collator=seq2seq_data_collator,
            tokenizer=tokenizer,
            train_dataset = dataset_samsum_pt['test'], ## Change to train 
            eval_dataset = dataset_samsum_pt['validation'] 
        )
        
         
        trainer.train()

