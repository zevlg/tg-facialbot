#!/usr/bin/env python3
import argparse
import logging

from fcs import FaceStyleBot


__version__ = '0.1.0'


def logging_lvl(verbosity: int):
    LOG_LVL_MAP = {
        0: logging.CRITICAL,
        1: logging.ERROR,
        2: logging.WARN,
        3: logging.INFO,
        4: logging.DEBUG
    }
    # clamp verbosity into [0,4] range
    if verbosity < 0:
        verbosity = 0
    elif verbosity > 4:
        verbosity = 4
    return LOG_LVL_MAP[verbosity]


def main():
    parser = argparse.ArgumentParser(description='Version: %s' % __version__)
    parser.add_argument('token',
                        help='Telegram token to use')
    parser.add_argument('--debug-user', type=int,
                        help='Send debug info to user id')
    parser.add_argument('-v', '--verbosity', type=int, default=3,
                        help='Verbosity level [0-4] (default: 3=INFO)')

    args = parser.parse_args()
    logging.basicConfig(level=logging_lvl(args.verbosity),
                        format="%(asctime)-15s [%(name)s/%(levelname)s] %(message)s")

    bot = FaceStyleBot(args)
    bot.run()


if __name__ == '__main__':
    main()
