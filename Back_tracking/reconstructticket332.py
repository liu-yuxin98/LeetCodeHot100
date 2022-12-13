class Solution:

    ticketDict = dict()
    usedTicket = dict()
    path = []
    res = []

    def backtrack(self, airport, totalTickets):
        if len(self.path) == totalTickets+1:
            self.res = self.path[::]
            return
        if airport not in self.ticketDict:
            print([])
            return
        next_terminals = sorted(self.ticketDict[airport])
        # print(next_terminals)
        # print('------------------------------')
        for next_terminal in next_terminals:
            if self.usedTicket[(airport, next_terminal)][0] == self.usedTicket[(airport, next_terminal)][1]:
                # all this ticket is used up
                continue
            self.path.append(next_terminal)
            self.usedTicket[(airport, next_terminal)][0] += 1
            self.backtrack(next_terminal, totalTickets)
            if self.res != []:
                break
            self.path.pop()
            self.usedTicket[(airport, next_terminal)][0] -= 1

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        self.ticketDict = dict()
        self.usedTicket = dict()
        self.path = []
        self.res = []
        for ticket in tickets:
            self.usedTicket[(ticket[0], ticket[1])] = self.usedTicket.get(
                (ticket[0], ticket[1]), [0, 0])
            self.usedTicket[(ticket[0], ticket[1])][1] += 1
            # [0,1] 0-> how many this ticket is used   1-> how many (ticket[0], ticket[1]) total
            self.ticketDict[ticket[0]] = self.ticketDict.get(
                ticket[0], []) + [ticket[1]]
        # must start from jfk
        self.path.append("JFK")
        self.backtrack("JFK", len(tickets))
        return self.res


s = Solution()

ticketsList = [[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
               [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"],
                   ["ATL", "JFK"], ["ATL", "SFO"]],
               [["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], ["ANU", "EZE"], [
                   "TIA", "ANU"], ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"]],
               ]

for tickets in ticketsList[2:]:
    print(s.findItinerary(tickets))
