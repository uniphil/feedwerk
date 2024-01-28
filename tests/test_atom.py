# -*- coding: utf-8 -*-
"""
    tests.atom
    ~~~~~~~~~~

    Tests the cache system

    :copyright: 2007 Pallets
    :license: BSD-3-Clause
"""
import datetime
import pytest

from feedwerk.atom import format_iso8601, AtomFeed, FeedEntry


class TestAtomFeed(object):
    """
    Testcase for the `AtomFeed` class
    """

    def test_atom_no_args(self):
        with pytest.raises(ValueError):
            AtomFeed()

    def test_atom_title_no_id(self):
        with pytest.raises(ValueError):
            AtomFeed(title='test_title')

    def test_atom_add_one(self):
        a = AtomFeed(title='test_title', id=1)
        f = FeedEntry(
            title='test_title', id=1, updated=datetime.datetime.now())
        assert len(a.entries) == 0
        a.add(f)
        assert len(a.entries) == 1

    def test_atom_add_one_kwargs(self):
        a = AtomFeed(title='test_title', id=1)
        assert len(a.entries) == 0
        a.add(title='test_title', id=1, updated=datetime.datetime.now())
        assert len(a.entries) == 1
        assert isinstance(a.entries[0], FeedEntry)

    def test_atom_to_str(self):
        updated_time = datetime.datetime.now()
        expected_repr = '''
        <?xml version="1.0" encoding="utf-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
            <title type="text">test_title</title>
            <id>1</id>
            <updated>%s</updated>
            <generator>Werkzeug</generator>
        </feed>
        ''' % format_iso8601(updated_time)
        a = AtomFeed(title='test_title', id=1, updated=updated_time)
        assert str(a).strip().replace(' ', '') == \
            expected_repr.strip().replace(' ', '')

    def test_atom_to_str_no_updated(self):
        expected_before_updated = '''
        <?xml version="1.0" encoding="utf-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
            <title type="text">test_title</title>
            <id>1</id>
            <
        '''
        expected_after_updated = '''
            <generator>Werkzeug</generator>
        </feed>
        '''
        a = AtomFeed(title='test_title', id=1)
        before_updated, _, after_updated = str(a).replace(' ', '').split('updated>')
        assert before_updated.strip() == expected_before_updated.strip().replace(' ', '')
        assert after_updated.strip() == expected_after_updated.strip().replace(' ', '')


class TestFeedEntry(object):
    """
    Test case for the `FeedEntry` object
    """

    def test_feed_entry_no_args(self):
        with pytest.raises(ValueError):
            FeedEntry()

    def test_feed_entry_no_id(self):
        with pytest.raises(ValueError):
            FeedEntry(title='test_title')

    def test_feed_entry_no_updated(self):
        with pytest.raises(ValueError):
            FeedEntry(title='test_title', id=1)

    def test_feed_entry_to_str(self):
        updated_time = datetime.datetime.now()
        expected_feed_entry_str = '''
        <entry>
            <title type="text">test_title</title>
            <id>1</id>
            <updated>%s</updated>
        </entry>
        ''' % format_iso8601(updated_time)

        f = FeedEntry(title='test_title', id=1, updated=updated_time)
        assert str(f).strip().replace(' ', '') == \
            expected_feed_entry_str.strip().replace(' ', '')


def test_format_iso8601():
    # naive datetime should be treated as utc
    dt = datetime.datetime(2014, 8, 31, 2, 5, 6)
    assert format_iso8601(dt) == '2014-08-31T02:05:06Z'

    # tz-aware datetime
    dt = datetime.datetime(2014, 8, 31, 11, 5, 6, tzinfo=KST())
    assert format_iso8601(dt) == '2014-08-31T11:05:06+09:00'


class KST(datetime.tzinfo):

    """KST implementation for test_format_iso8601()."""

    def utcoffset(self, dt):
        return datetime.timedelta(hours=9)

    def tzname(self, dt):
        return 'KST'

    def dst(self, dt):
        return datetime.timedelta(0)
