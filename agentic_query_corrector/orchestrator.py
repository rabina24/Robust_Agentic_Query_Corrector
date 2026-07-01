from agentic_query_corrector.agents.detector import DetectorAgent

from agentic_query_corrector.agents.misspelling import MisspellingAgent
from agentic_query_corrector.agents.naturality import NaturalityAgent
from agentic_query_corrector.agents.ordering import OrderingAgent
from agentic_query_corrector.agents.paraphrase import ParaphraseAgent
from agentic_query_corrector.agents.synonym import SynonymAgent


class QueryCorrectionOrchestrator:

    def __init__(self):

        self.detector = DetectorAgent()

        self.tools = {
            "Misspelled": MisspellingAgent(),
            "Naturality": NaturalityAgent(),
            "Ordering": OrderingAgent(),
            "Paraphrase": ParaphraseAgent(),
            "Synonyms": SynonymAgent()
        }

        self.max_iterations = 10

    def correct(self, query):

        current_query = query

        for _ in range(self.max_iterations):

            decision = self.detector.detect(current_query)

            if decision["needs_correction"] is False:
                break

            error_type = decision["type"]

            if error_type not in self.tools:
                break

            current_query = self.tools[error_type].correct(
                current_query
            )

        return current_query