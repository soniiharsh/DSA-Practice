class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next

        index = 1
        first = -1
        last = -1
        minDistance = float('inf')

        while curr and curr.next:
            nextNode = curr.next

            if (curr.val > prev.val and curr.val > nextNode.val) or \
               (curr.val < prev.val and curr.val < nextNode.val):

                if first == -1:
                    first = index
                else:
                    minDistance = min(minDistance, index - last)

                last = index

            prev = curr
            curr = curr.next
            index += 1

        if first == -1 or first == last:
            return [-1, -1]

        return [minDistance, last - first]