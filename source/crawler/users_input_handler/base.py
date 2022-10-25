from pydantic_cli import HAS_AUTOCOMPLETE_SUPPORT
from pydantic_cli.examples import ExampleConfigDefaults

from pydantic import BaseModel, Field, validator


class CommandLineInterface(BaseModel):
    """ CLI interface, which stands for featching and validating input argument. """

    class Config(ExampleConfigDefaults):
        CLI_SHELL_COMPLETION_ENABLE = HAS_AUTOCOMPLETE_SUPPORT

    url: str = Field(
        ...,
        title=" url address ",
        description=" url address to crawle ",
        required=True,
        cli=("-u", "--url")
    )

    depth: int = Field(
        1,
        title=" depth ",
        description=" recursion depth to crawle statically linked pages (by default, only the root URL will be processed) ",
        required=True,
        ge=1,
        le=100,
        cli=("-d", "--depth")
    )
