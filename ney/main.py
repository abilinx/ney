import argparse
import sys

from ney.io import TerminalInputStream, TerminalOutputStream, FileInputStream, FileOutputStream
from ney.pipe import Pipe
from ney.filter import RegexFilter


def parse_arguments():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-c', '--config', help='configuration file path', default='./config.xml')
    arg_parser.add_argument('-i', '--input', help='input source', default='terminal')
    arg_parser.add_argument('-o', '--output', help='output destination', default='terminal')
    return arg_parser.parse_args()


def initialize_input(input_arg):
    if input_arg == 'terminal':
        return TerminalInputStream()
    else:
        return FileInputStream(input_arg)


def initialize_output(output_arg):
    if output_arg == 'terminal':
        return TerminalOutputStream()
    else:
        return FileOutputStream(output_arg)


def pass_log(input_stream, output_stream):
    try:
        log_line = input_stream.get_next()
        while log_line.text:
            output_stream.pass_through(log_line)
            log_line = input_stream.get_next()
    except KeyboardInterrupt:
        pass
    return


if __name__ == '__main__':
    args = parse_arguments()
    input_stream = initialize_input(args.input)
    output_stream = initialize_output(args.output)

    pipe = Pipe(output_stream)
    pipe.add_filter(RegexFilter(r'.*bad.*'))
    pipe.destination = output_stream

    pass_log(input_stream, pipe)
    sys.exit(0)
