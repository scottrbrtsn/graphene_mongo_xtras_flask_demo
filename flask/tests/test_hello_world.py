import pytest
import snapshottest

from graphene_mongo_xtras_flask_demo.hello_world import add, div, hello, mult, sub


def test_add(snapshot):
    t1 = dict(a=1, b=1, c=add(1, 1))
    snapshot.assert_match(t1)

    t2 = dict(a=8, b=34, c=add(8, 34))
    snapshot.assert_match(t2)

    assert add(1, 1) != 3

    assert add(40, 2) == 42


def test_mult(snapshot):

    t1 = dict(a=1, b=1, c=mult(1, 1))
    snapshot.assert_match(t1)

    t2 = dict(a=8, b=34, c=mult(8, 34))
    snapshot.assert_match(t2)

    assert mult(12, 1) != 13

    assert mult(5, 5) == 25
