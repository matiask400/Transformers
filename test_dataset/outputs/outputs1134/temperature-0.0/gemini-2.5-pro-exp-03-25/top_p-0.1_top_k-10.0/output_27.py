import sys

# Set higher recursion depth for potentially deep Tries, although unlikely with L=10
# sys.setrecursionlimit(20000)

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self):
        # Stores children nodes: {char: TrieNode}
        self.children = {}
        # Stores the index of the word. We need the largest index,
        # so we update it whenever we insert a word with a larger index.
        self.index = -1

class WordFilter:
    """
    Implements a word filter that allows searching by prefix and suffix,
    returning the largest index of a matching word. Uses a Trie for efficiency.
    """
    def __init__(self, words: list[str]):
        """
        Initializes the WordFilter with a list of words.
        Builds a Trie storing combinations of suffix + '#' + word
        to enable efficient prefix searching on this combined string.

        Args:
            words: A list of strings.
        """
        self.trie = TrieNode()
        # Use a character not present in the words as a separator
        separator = '#'

        # Iterate through words with their indices
        for index, word in enumerate(words):
            n = len(word)
            # Generate all suffixes of the word (including the full word itself)
            # The length of the suffix ranges from 0 to n
            for i in range(n + 1):
                suffix = word[n-i:] # Suffix of length i
                # Construct the string: suffix + separator + word
                # Max length = 10 + 1 + 10 = 21
                combined_key = suffix + separator + word

                # Insert the combined key into the Trie
                node = self.trie
                # Update the index at the root for the empty prefix case if needed
                # (though our query always has non-empty prefix/suffix)
                # node.index = max(node.index, index) # Optional, depends on exact interpretation

                for char in combined_key:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                    # IMPORTANT: Update the index at *every* node along the path.
                    # This ensures that any prefix search ending at this node
                    # will retrieve the largest index seen so far for words
                    # contributing to paths passing through this node.
                    # Since we process words in increasing index order, simply assigning
                    # would work too, but max is safer conceptually.
                    node.index = max(node.index, index)
                    # node.index = index # This also works because we iterate index 0..N-1


    def f(self, prefix: str, suffix: str) -> int:
        """
        Searches for a word in the dictionary that has the given prefix
        and suffix. Returns the largest index of such a word, or -1 if none exists.

        Args:
            prefix: The desired prefix.
            suffix: The desired suffix.

        Returns:
            The largest index of a word matching the prefix and suffix, or -1.
        """
        separator = '#'
        # Construct the search query string: suffix + separator + prefix
        search_key = suffix + separator + prefix

        node = self.trie
        # Traverse the Trie based on the search key
        for char in search_key:
            if char not in node.children:
                # If any character is not found, no word matches
                return -1
            node = node.children[char]

        # The index stored at the final node represents the largest index
        # of a word whose (suffix + '#' + word) string starts with
        # (search_suffix + '#' + search_prefix). This corresponds to a word
        # matching the original prefix and suffix criteria.
        return node.index

# --- Testing Framework ---

def run_tests():
    """
    Runs predefined test cases against the WordFilter implementation.
    """
    test_cases = [
        # Example 1
        {
            "commands": ["WordFilter", "f"],
            "inputs": [[["apple"]], ["a", "e"]],
            "expected_outputs": [None, 0]
        },
        # Custom Test 1: Multiple words, multiple matches
        {
            "commands": ["WordFilter", "f", "f", "f", "f"],
            "inputs": [[["apple", "ape", "apply", "apricot"]], ["ap", "e"], ["a", "y"], ["apr", "t"], ["b", "e"]],
            "expected_outputs": [None, 1, 2, 3, -1] # ape(1), apply(2), apricot(3), no match
        },
        # Custom Test 2: Overlapping matches, largest index needed
        {
            "commands": ["WordFilter", "f"],
            "inputs": [[["banana", "bandana"]], ["ba", "na"]],
            "expected_outputs": [None, 1] # bandana(1) has larger index than banana(0)
        },
        # Custom Test 3: Empty prefix/suffix (not allowed by constraints, but good check)
        # Constraints: 1 <= prefix.length, suffix.length <= 10
        # {
        #     "commands": ["WordFilter", "f", "f", "f"],
        #     "inputs": [[["test"]], ["", "t"], ["t", ""], ["", ""]],
        #     "expected_outputs": [None, 0, 0, 0] # Assuming empty matches everything
        # },
        # Custom Test 4: No match
        {
            "commands": ["WordFilter", "f"],
            "inputs": [[["word"]], ["w", "d"], ["x", "y"]],
            "expected_outputs": [None, 0, -1]
        },
         # Custom Test 5: Longer words and prefixes/suffixes
        {
            "commands": ["WordFilter", "f", "f"],
            "inputs": [[["abcdefghij", "klmnopqrst"]], ["abc", "hij"], ["klm", "rst"]],
            "expected_outputs": [None, 0, 1]
        },
        # Custom Test 6: Repeated words (should use largest index)
        {
            "commands": ["WordFilter", "f"],
            "inputs": [[["repeat", "word", "repeat"]], ["re", "at"]],
            "expected_outputs": [None, 2] # Index 2 is the largest for "repeat"
        },
        # Custom Test 7: Suffix is the whole word
         {
            "commands": ["WordFilter", "f"],
            "inputs": [[["apple", "apply"]], ["a", "apply"]],
            "expected_outputs": [None, 1]
        },
        # Custom Test 8: Prefix is the whole word
         {
            "commands": ["WordFilter", "f"],
            "inputs": [[["apple", "apply"]], ["apply", "y"]],
            "expected_outputs": [None, 1]
        },
         # Custom Test 9: Prefix and Suffix are the whole word
         {
            "commands": ["WordFilter", "f"],
            "inputs": [[["apple", "apply"]], ["apply", "apply"]],
            "expected_outputs": [None, 1]
        },
    ]

    correct_count = 0
    total_tests = 0
    word_filter_instance = None

    for i, case in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        commands = case["commands"]
        inputs = case["inputs"]
        expected_outputs = case["expected_outputs"]
        instance_created = False

        for j, command in enumerate(commands):
            total_tests += 1
            current_input = inputs[j]
            expected_output = expected_outputs[j]
            actual_output = None

            try:
                if command == "WordFilter":
                    # Handle potential multiple WordFilter calls within a "case" if designed that way
                    # (though current structure implies one per case)
                    if instance_created:
                         print("Warning: Re-initializing WordFilter within the same test case.")
                    word_filter_instance = WordFilter(*current_input)
                    actual_output = None # Constructor returns None
                    instance_created = True
                    print(f"Command: {command}({current_input})")
                elif command == "f":
                    if word_filter_instance is None:
                         raise ValueError("WordFilter instance not initialized before calling 'f'")
                    actual_output = word_filter_instance.f(*current_input)
                    print(f"Command: {command}({current_input}) -> Expected: {expected_output}, Got: {actual_output}")
                else:
                    print(f"Unknown command: {command}")
                    continue # Skip unknown commands

                # Compare actual output with expected output
                result = (actual_output == expected_output)
                print(result)
                if result:
                    correct_count += 1
                else:
                    # Optionally print more details on failure
                    # print(f"Failed: Expected {expected_output}, Got {actual_output}")
                    pass

            except Exception as e:
                print(f"Error executing command {command}({current_input}): {e}")
                print(False) # Mark test as failed due to error

        print("-" * 20)


    print(f"\nTotal tests passed: {correct_count} / {total_tests}")

if __name__ == "__main__":
    run_tests()