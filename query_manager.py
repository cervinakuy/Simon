from typing import Optional, List

def split_to_only_words_and_numbers(query: str) -> List:
    filtered_words: List = []
    word: str
    for word in query.split(" "):
        character: str
        filtered_word: str = ""
        for character in word.lower():
            if character.isalpha() or character.isnumeric():
                filtered_word += character
        filtered_words.append(filtered_word)
    return filtered_words


class QueryManager:
    def __init__(self):
        self.queries: List[QueryResponse] = []

    def add_query(self, hot_words: List, minimum_number_of_hits: int, response: str) -> None:
        self.queries.append(QueryResponse(hot_words, minimum_number_of_hits, response))

    def get_best_response(self, query: str) -> Optional[str]:
        print("\n\n\n")
        query_words: List = split_to_only_words_and_numbers(query)
        best_response_index: int = 0
        best_response_hits = 0
        for index, query_response in enumerate(self.queries):
            current_query_hits = query_response.calculate_total_hits(query_words)
            # print("Hits for [%s]: %d", query_response.hot_words, current_query_hits)
            if current_query_hits > best_response_hits:
                best_response_index = index
                best_response_hits = current_query_hits
        if best_response_hits == 0:
            return None
        return self.queries[best_response_index].response


class QueryResponse:
    def __init__(self, hot_words: List, minimum_number_of_hits: int, response: str) -> None:
        self.hot_words: List = hot_words  # key words to look for
        self.minimum_number_of_hits = minimum_number_of_hits  # minimum number of word hits to deem a good response
        self.response = response  # automated response to send if deemed a good response

    def calculate_total_hits(self, query_words: List) -> int:
        hits = 0
        for hot_word in self.hot_words:
            if hot_word in query_words:
                hits += 1
        if hits < self.minimum_number_of_hits:  # if does not have the minimum number of hits, ignore
            return 0
        return hits / len(self.hot_words)
