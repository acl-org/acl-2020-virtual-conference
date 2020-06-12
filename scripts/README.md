This directory contains extensions to help support the mini-conf library.

Follow the procedure described in [this gist](https://gist.github.com/georgepar/3d5cda48c50c6ee57f56aaea9b99603d) to obtain
the embeddings and the paper projections.


These include:

* `embeddings.py` : For turning abstracts into embeddings. Creates an `embeddings.torch` file. 

```bash
python embeddings.py ../sitedata/papers.csv
```

* `reduce.py` : For creating two-dimensional representations of the embeddings.

```bash
python reduce.py ../sitedata/papers.csv embeddings.torch > ../sitedata/papers_projection.json --projection-method umap
```

* `parse_calendar.py` : to convert a local or remote ICS file to JSON. -- more on importing calendars see [README_Schedule.md](README_Schedule.md)

```bash
python parse_calendar.py --in sample_cal.ics
```

* Image-Extraction: https://github.com/Mini-Conf/image-extraction for pulling images from PDF files. 

