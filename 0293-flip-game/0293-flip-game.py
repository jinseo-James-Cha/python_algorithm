class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        # + or -
        # change ++ into --
        # cannot do -> the other friend is winner
        # any order of return..

        possible_states = []
        for i in range(len(currentState) - 1):
            if currentState[i] == "+" and currentState[i+1] == "+":
                temp = currentState[:i] + "--" + currentState[i+2:]
                possible_states.append(temp)
        return possible_states