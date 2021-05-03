class Solution79:
    # �������������ĸ����߷���
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board, word):
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        mark = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # ����Ԫ�ر��Ϊ��ʹ��
                    mark[i][j] = 1
                    if self.backtrack(i, j, mark, board, word[1:]) == True:
                        return True
                    else:
                        # ����
                        mark[i][j] = 0
        return False

    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0:
            return True

        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]

            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == \
                    word[0]:
                # ������Ѿ�ʹ�ù���Ԫ�أ�����
                if mark[cur_i][cur_j] == 1:
                    continue
                # ����Ԫ�ر��Ϊ��ʹ��
                mark[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                    return True
                else:
                    # ����
                    mark[cur_i][cur_j] = 0
        return False



board = [["a","b"],["c","d"]]
word ="abcd"
s = Solution79
print(s.exist(s,board,word))




