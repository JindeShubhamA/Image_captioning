import os, sys
sys.path.append(os.path.dirname(os.getcwd()))
import csv
from utils.utils import *
from preprocessing.preprocessing import *
import tensorflow as tf
from variables import *
from training import *
from evaluation import *

def main():
   img_list, caption_list = get_image_n_caption(csv_file_path,image_path,debug)
   encode_train = sorted(set(img_list))
   store_img_extracted_features(encode_train)
   caption_vector, tokenizer, train_seqs = tokenize_words(max_words,caption_list)
   max_length = max_len_tensor(train_seqs)
   img_name_train, img_name_val, cap_train, cap_val = split(img_list,caption_vector)
   decoder, encoder=training(img_name_train, img_name_val, cap_train, cap_val, tokenizer)


   rid = np.random.randint(0, len(img_name_val))
   image = img_name_val[rid]
   real_caption = ' '.join([tokenizer.index_word[i] for i in cap_val[rid] if i not in [0]])


   result, attention_plot = evaluate(image, tokenizer, max_length, decoder, encoder)

   print ('Real Caption:', real_caption)
   print ('Prediction Caption:', ' '.join(result))




if __name__ == '__main__':
    main()