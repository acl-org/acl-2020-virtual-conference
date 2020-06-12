import argparse
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import openreview

OLD_HEADERS = [
    'Submission ID', 'Title', 'Authors', 'Abstract', 'Submission Type'
]

NEW_HEADER = ['UID', 'title', 'authors', 'abstract', 'keywords', 'session']


class CsvConverter(object):
    def __init__(self, n_keywords=5):
        self.n_keywords = n_keywords

    def get_uid(self, entry):
        return entry['Submission ID']

    def get_title(self, entry):
        return entry['Title']

    def get_authors(self, entry):
        return entry['Authors']

    def get_abstract(self, entry):
        return entry['Abstract']

    def get_keywords(self, entry, tfidf_model):
        scores = tfidf_model.transform([entry['Abstract']])[0]
        words = np.array(tfidf_model.get_feature_names())
        sorted_scores = np.argsort(scores.data)
        top_scores = sorted_scores[:-(self.n_keywords + 1): -1]
        keywords = words[scores.indices[top_scores]].tolist()
        return '|'.join(keywords)

    def keyword_model(self, abstracts):
        # Replace this if we get a list of keywords
        # For now return top TF-IDF terms of words in abstracts
        tfidf = TfidfVectorizer(stop_words='english').fit(abstracts)
        return tfidf

    def get_session(self, entry):
        # FIXME: Use this as a placeholder until we get some session info
        return entry['Submission Type']

    def parse_accepted_papers(self, tsv_file):
        with open(tsv_file, 'r') as fd:
            lines = [l.strip().split('\t') for l in fd]
            header, paper_info = lines[0], lines[1:]
        papers = []
        for paper in paper_info:
            entry = {}
            for i, h in enumerate(header):
                entry[h] = paper[i]
            papers.append(entry)
        return papers

    def convert_entries(self, entries):
        tfidf = self.keyword_model([e['Abstract'] for e in entries])

        def get_new_entry(e):
            return (
                e['Submission ID'],
                e['Title'],
                '|'.join(e['Authors'].split(',')),
                '"{}"'.format(e['Abstract']),
                self.get_keywords(e, tfidf),
                # FIXME: Use this as a placeholder until session info
                # is available
                e['Submission Type']
            )
        new_entries = [get_new_entry(e) for e in entries]
        return new_entries

    def convert(self, old_tsv, papers_csv, out_pickle=None):
        old_entries = self.parse_accepted_papers(old_tsv)
        new_entries = self.convert_entries(old_entries)
        with open(papers_csv, 'w') as fd:
            header = ','.join(NEW_HEADER)
            fd.write('{}\n'.format(header))
            for entry in new_entries:
                e = ','.join(entry)
                fd.write('{}\n'.format(e))
        if out_pickle is not None:
            cached_or = {}
            for entry in new_entries:
                cached_or[
                    entry[0] # id
                ] = openreview.Note(
                    '', [], [], [],
                    {'abstract': entry[3], 'title': entry[1]}
                )  # Hack. ICLR Recommender script accepts Openreview notes

            with open(out_pickle, 'wb') as fd:
                pickle.dump(cached_or, fd)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert CSV from original ACL format to Miniconf compatible format"
    )
    parser.add_argument('--inp', type=str, help='Original ACL CSV')
    parser.add_argument('--out', type=str, help='papers.csv')
    parser.add_argument(
        '--out-pickle', type=str,
        help='Dump entries into a pickle compatible with ICLR Recommendation engine'
    )
    parser.add_argument(
        '--n-keywords', type=int, default=3, help='Number of keywords to keep')
    return parser.parse_args()


def main():
    args = parse_args()
    csv_converter = CsvConverter(n_keywords=args.n_keywords)
    csv_converter.convert(args.inp, args.out, out_pickle=args.out_pickle)


if __name__ == '__main__':
    main()
