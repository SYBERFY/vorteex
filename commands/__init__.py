from .configure import arguments as ConfigureArguments
from .query import arguments as QueryArguments


def build_commands(sub_parser_creator):
    ConfigureArguments(sub_parser_creator)
    QueryArguments(sub_parser_creator)
