#!/usr/bin/python
# coding: utf8
import logging
import geocoder

location = 'index.home.raft'
ottawa = (45.4215296, -75.6971930)


def test_w3w():
    g = geocoder.w3w(location)
    assert g.ok


def test_w3w_reverse():
    g = geocoder.w3w(ottawa, method='reverse')
    assert g.ok


def main():
    logging.basicConfig(level=logging.INFO)
    test_w3w()


if __name__ == '__main__':
    main()
