import os
import openai
import pandas as pd
import httplib2 
from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
import time
import pandas as pd
import numpy as np


# Авторизация в OPENAI
openai.organization = "org-bTI6lp1QnSelVMz4isrFbgDx"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()


# Авторизация в Google
CREDENTIALS_FILE = 'banded-cable-385612-0ca06f32ab93.json'  # Имя файла с закрытым ключом, вы должны подставить свое
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе


# Читаем запросы из файлов и делаем из них список
def read_texts () -> list:
  reqs = []
  paths = ['./GPTtoGoogle/text_shorts_male.txt', './GPTtoGoogle/text_shorts_female.txt', './GPTtoGoogle/text_medium_male.txt',
           './GPTtoGoogle/text_medium_female.txt', './GPTtoGoogle/text_longlead_male.txt', './GPTtoGoogle/text_longlead_female.txt',
           './GPTtoGoogle/text_poems_male.txt', './GPTtoGoogle/text_poems_female.txt', './GPTtoGoogle/text_army_male.txt', './GPTtoGoogle/text_army_female.txt']
  for path in paths:
      file = open(path, 'r', encoding='utf-8')
      req = file.read()
      reqs.append(req)
      file.close()
  return reqs


def create_answers(reqs:list) -> list:
  def split_answer(answers:list) -> list:
    splited_answers = []
    lst = []
    for elem in answers:
        lst = elem.split('\n')
        splited_answers.append(lst)
    return splited_answers

  def clear_digits(answers: list) -> list:
    cleared_answers = []
    for answer in answers:
        clear_answer = []
        for string in answer:
            clear_answer.append(string[3:])
        clear_answer = [x.strip() for x in clear_answer]
        cleared_answers.append(clear_answer)
    return cleared_answers

  answers = []
  for req in reqs:
        print(req)
        result = []
        while len(result) == 0:
             try:
                 completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": req}])
                 result = completion.choices[0].message['content']
             except:
                  print('Error')
                  time.sleep(60)
                  continue
        answers.append(result)
  map_func = lambda x: x.replace('\n\n', '\n')
  answers = list(map(map_func, answers))
  splited_answers = split_answer(answers)
  cleared_answers = clear_digits(splited_answers)
  return cleared_answers

def create_table (answers:list) -> pd.DataFrame:
    dictionary = dict(shorts_male = np.array(answers[0]), shorts_female = np.array(answers[1]), medium_male = np.array(answers[2]),
                  medium_female = np.array(answers[3]), longlead_male = np.array(answers[4]), longlead_female = np.array(answers[5]),
                  poems_male = np.array(answers[6]), poems_female = np.array(answers[7]), army_male = np.array(answers[8]),
                  army_female = np.array(answers[9]))
    table = pd.DataFrame(dict([(k, pd.Series(v)) for k,v in dictionary.items()]))
    return table


reqs = read_texts()
answers = create_answers(reqs)
table = create_table(answers)
table.to_csv('./GPTtoGoogle/reviews.csv')          