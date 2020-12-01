from .auth import arguments as AuthArguments
from .query import arguments as QueryArguments
from .configure import arguments as ConfigureArguments


def build_commands(sub_parser_creator):
    AuthArguments(sub_parser_creator)
    QueryArguments(sub_parser_creator)
    ConfigureArguments(sub_parser_creator)
