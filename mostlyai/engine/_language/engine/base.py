# Copyright 2025 MOSTLY AI
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass
from abc import abstractmethod, ABC
from collections.abc import Callable

from formatron.formatter import FormatterBuilder


@dataclass
class EngineMetrics:
    tokenize_time: float
    generate_time: float


class LanguageEngine(ABC):
    @abstractmethod
    def initialize_logits_processors(
        self, formatter_builders: list[FormatterBuilder], vocab_processors: list[Callable] | None = None
    ):
        pass

    @abstractmethod
    def generate(
        self, text: list[str], sampling_temperature: float, sampling_top_p: float
    ) -> tuple[list[int], EngineMetrics]:
        pass

    @abstractmethod
    def get_default_batch_size(self) -> int:
        pass

    @abstractmethod
    def supports_json_enforcing(self) -> bool:
        pass

    @abstractmethod
    def cleanup(self):
        pass
