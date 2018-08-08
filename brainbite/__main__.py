import argparse
from logging import getLogger
from pathlib import Path
import sys

from brainbite.transpiler import transpiler


assert __name__ == '__main__'

_logger = getLogger(__name__)
_dir = Path(__file__).parent


def init_parser():
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers()

    # sample parser
    sample_parser = sub_parser.add_parser(
        'sample',
        help='you can get some prepared samples. to list up sample, specify -.'
    )
    sample_parser.add_argument(
        'name', help='sample you want to get.'
    )
    sample_parser.set_defaults(handler=command_sample)

    # trans parser
    trans_parser = sub_parser.add_parser(
        'trans', help='transpile brainfuck code to python one.'
    )
    trans_parser.add_argument(
        'path', help='brainfuck code path what you want to translate.'
    )
    trans_parser.set_defaults(handler=command_trans)

    return parser


def command_sample(args):
    if args.name == '-':
        for sample_py in (_dir / 'sample').glob('*.py'):
            print(
                sample_py.stem
            )
        return

    #
    sample_py = _dir / f'sample/{args.name}.py'

    if not sample_py.is_file():
        _logger.warning(
            f'Sample {args.name} is not prepared.'
        )
        return

    sys.stdout.write(
        sample_py.open().read()
    )


def command_trans(args):
    if args.path == '-':
        src = sys.stdin.read()
    else:
        path = Path(args.path)

        if not path.is_file():
            _logger.warning(
                f'File {args.path} is not found.'
            )
            return

        src = path.open().read()

    sys.stdout.write(
        transpiler.substitute(src)
    )


def main():
    parser = init_parser()

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


main()
