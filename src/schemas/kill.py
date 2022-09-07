from typing import Union, Optional
from pydantic import Field

from .base import BaseArgs


class KillArgs(BaseArgs):
    owner: Union[str, None] = Field(default=None, alias="--owner")
    run: Union[str, None] = Field(default=None, alias="--run")
    preserve_queue: Union[bool, None] = Field(default=None, alias="--preserve-queue")
    job: Union[int, None] = Field(default=None, alias="--job")
    jobspec: Union[str, None] = Field(default=None, alias="--jobspec")
    machine_type: Union[str, None] = Field(default='default', alias="--machine-type")
    archive: Union[str, None] = Field(default=None, alias="--archive")
