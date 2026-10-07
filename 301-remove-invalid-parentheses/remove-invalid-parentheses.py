class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = {s}
        visited = {s}

        while queue:
            result = []

            # Check current level
            for string in queue:
                if is_valid(string):
                    result.append(string)

            # If valid strings found, this is the minimum removal level
            if result:
                return result

            # Generate next level
            next_queue = set()

            for string in queue:
                for i in range(len(string)):
                    # Only remove parentheses
                    if string[i] not in "()":
                        continue

                    new_string = string[:i] + string[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_queue.add(new_string)

            queue = next_queue

        return [""]