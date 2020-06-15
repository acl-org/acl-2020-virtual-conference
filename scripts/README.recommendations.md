# How to get similar paper recommendations

In this guide we can see how to get paper recommendations using the pretrained model provided
from [ICLR webpage](https://github.com/ICLR/iclr.github.io/tree/master/recommendations) and abstract embeddings.



## Create a visualization based on BERT embeddings

1. Grab ACL2020
   [papers.csv](https://github.com/acl-org/acl-2020-virtual-conference-sitedata/blob/add_acl2020_accepted_papers_tsv/papers.csv)
   from this branch or a more recent version and copy it to `sitedata_acl2020`.
2. Run `python scripts/embeddings.py sitedata_acl2020/papers.csv` to produce the BERT embeddings
   for the paper abstracts.
3. Run `python scripts/reduce.py --projection-method [tsne|umap] acl-2020-virtual-conference-sitedata/papers.csv embeddings.torch > sitedata_acl2020/papers_projection.json`
   to produce a 2D projection of the BERT embeddings for visualization. `--projection-method`
   selects which dimensionality reduction technique to use.
4. Rerun `make run` and go to the paper visualization page


## Produce similar paper recommendations

1. Grab the
   [acl2020\_accepted\_papers.tsv](https://github.com/acl-org/acl-2020-virtual-conference-sitedata/blob/add_acl2020_accepted_papers_tsv/acl2020_accepted_papers.tsv)
   file.
2. Run `python scripts/create_papers_csv.py --inp acl2020_accepted_papers.tsv --out dummy.csv --out-pickle cached_or.pkl --n-keywords 5` to produce `cached_or.pkl`.
   This file is compatible with the inference scripts provided in [https://github.com/ICLR/iclr.github.io/tree/master/recommendations](https://github.com/ICLR/iclr.github.io/tree/master/recommendations)
3. Clone [https://github.com/ICLR/iclr.github.io](https://github.com/ICLR/iclr.github.io). You will
   need `git-lfs` installed.
4. `cp cached_or.pkl iclr.github.io && cd iclr.github.io/recommendations`
5. Install missing requirements
6. `python recs.py`. This will run inference using a pretrained similarity model and produce the
   `rec.pkl` file that contains the paper similarities.
7. You can use the `iclr.github.io/data/pkl_to_json.py` script to produce the `paper_recs.json`
   file that contains the similar paper recommendations that can be displayed to the website. Make
   sure to modify the filepaths to point to the correct `cached_or.pkl`, `rec.pkl`.
8. Grab the produced `paper_recs.json` file and copy it to `sitedata_acl2020`. A version of this file
   produced using this method is
   [here](https://github.com/acl-org/acl-2020-virtual-conference-sitedata/blob/add_acl2020_accepted_papers_tsv/paper_recs.json)
9. I have already modified the `poster.html` template and `main.py` to display the paper
   recommendations in `54_add_similar_papers_graph` branch.
