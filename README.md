# Bleu

Calculate the Bleu Score for Machine Translated Text.
-----------------------------------------------------

HOW TO RUN

首先设置working directory为根目录

python calculatebleu.py "candidate-file.txt" "reference-file/directory"

eg1 :

python calculatebleu.py "dataset/candidate.txt" "dataset/referenceSets"

eg2 :

python calculatebleu.py "dataset/candidate.txt" "dataset/referenceSets/reference.txt"

OUTPUT

bleu_out.txt : contains the Bleu score for the candidate-file

---

Reference

BLEU: a Method for Automatic Evaluation of Machine Translation
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu

## 以下是 我的贡献：

#### UI方式运行

`python main.py`

#### 编译成exe

- 打开cmder
- sh build.sh
- 编译完成后，会有个dist/ 文件夹，exe 文件在里面，直接双击打开
