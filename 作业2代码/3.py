class mysqlist():
    '''顺序表/线性表'''

    def __init__(self, size):
        self.size = size
        self.sqlist = [0]

    def add(self, data):
        '''在尾部添加元素'''
        self.sqlist.append(data)

    def insert(self, index, data):
        '''在索引index处插入x'''
        if index < 1 or index > self.size:
            raise IndexError("插入位置错误")
        else:
            self.sqlist.insert(index, data)

    def delete(self, index):
        '''删除索引index处的值'''
        if index < 1 or index > self.size:
            raise IndexError("删除位置错误")
        else:
            return self.sqlist.pop(index)

    def findelem(self, index):
        '''返回索引index处的值'''
        if index < 1 or index > self.size:
            raise IndexError("查询位置错误")
        else:
            return self.sqlist[index]

    def length(self):
        '''返回线性表长度'''
        return len(self.sqlist) - 1

    def showlist(self):
        '''输出线性表'''
        return self.sqlist[1:]


if __name__ == "__main__":
    # m是数到第几个人死亡，n是总人数，index是从第几个开始数
    n, m = map(int, input().split())
    result = []
    index = 1
    # y = mysqlist(n)
    peopleList = []
    # for i in range(1, n + 1):
    #     y.add
    for i in range(1, n + 1):
        peopleList.append(i)
    # while y.length() > 1:
    #     length = y.length()
    #     index = (index + m - 1) % length
    #     if index == 0:
    #         index = length
    #     temp = y.delete(index)
    #     result.append(temp)
    while len(peopleList) - 1 > 1:
        length = len(peopleList) - 1
        index = (index + m - 1) % length
        if index == 0:
            index = length
        temp = peopleList.pop(index)
        result.append(temp)

    # result.append(y.findelem(1))
    #
    # print(f"\n死亡顺序为：{result}")