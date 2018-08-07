import argparse
from logging import getLogger
from pathlib import Path


assert __name__ == '__main__'

_logger = getLogger(__name__)
_dir = Path(__file__).parent


def init_parser():
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers()

    # sample parser
    sample_parser = sub_parser.add_parser('sample')
    sample_parser.add_argument('name')
    sample_parser.set_defaults(handler=command_sample)

    return parser


def command_sample(args):
    sample_py = _dir / f'sample/{args.name}.py'

    if not sample_py.is_file():
        _logger.warning(
            f'Sample {args.name} is not prepared.'
        )
        return

    print(
        sample_py.open().read()
    )


def main():
    parser = init_parser()

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


main()
