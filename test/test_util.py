from google_ngram_downloader.util import (
    get_indices,
    ngram_to_cooc,
    count_coccurrence,
)

import pytest


def test_get_indices_1grams(unigram_indices):
    indices = list(get_indices(1))
    assert len(set(indices)) == len(indices)

    assert set(indices) == unigram_indices


def test_get_indices_manygrams(bigrams_indices):
    indices = list(get_indices(2))
    assert len(set(indices)) == len(indices)

    assert set(indices) == bigrams_indices


def test_get_indices_5grams(bigrams_indices):
    """Check that there is no "qk" index for 5grams."""
    indices = list(get_indices(5))
    assert len(indices) == len(set(bigrams_indices)) - 1

    assert set(indices) == (bigrams_indices - set(['qk']))

def test_get_indices_1grams_coverage_1m(unigram_indices_1m):
    indices = list(get_indices(1, coverage="1M"))
    assert len(set(indices)) == len(indices)

    assert set(indices) == unigram_indices_1m

def test_get_indices_2grams_coverage_1m(bigram_indices_1m):
    indices = list(get_indices(2, coverage="1M"))
    assert len(set(indices)) == len(indices)

    assert set(indices) == bigram_indices_1m

def test_get_indices_3grams_coverage_1m(trigram_indices_1m):
    indices = list(get_indices(3, coverage="1M"))
    assert len(set(indices)) == len(indices)

    assert set(indices) == trigram_indices_1m

def test_get_indices_4grams_coverage_1m(quadgram_indices_1m):
    indices = list(get_indices(4, coverage="1M"))
    assert len(set(indices)) == len(indices)

    assert set(indices) == quadgram_indices_1m

def test_get_indices_5grams_coverage_1m(fivegram_indices_1m):
    indices = list(get_indices(5, coverage="1M"))
    assert len(set(indices)) == len(indices)

    assert set(indices) == fivegram_indices_1m

@pytest.mark.parametrize(
    ('ngram', 'expected_result', 'index'),
    (
        (
            'aa_DET ab BB zz yz',
            (
                ((0, 5), 3),
                ((0, 2), 3),
                ((0, 3), 3),
                ((0, 4), 3),
            ),
            {'BB': 0, 'aa': 1, 'ab': 2, 'zz': 3, 'yz': 4, 'aa_DET': 5},
        ),
        (
            'aa yz BB yz yz',
            (
                ((0, 1), 3),
                ((0, 2), 3),
                ((0, 2), 3),
                ((0, 2), 3),
            ),
            {'BB': 0, 'aa': 1},
        ),
    ),
)
def test_ngrams_to_cooc(ngram, expected_result, index):
    result = ngram_to_cooc(ngram, 3, index)
    assert result == expected_result


def test_count_coccurrence(records):
    index = {}
    assert count_coccurrence(records, index) == {
        (index['BB'], index['a']): 1110,
        (index['BB'], index['z']): 1110,
        (index['ABCDEFG'], index['a']): 222,
        (index['ABCDEFG'], index['z']): 222,
    }
