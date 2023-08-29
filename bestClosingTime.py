def bestClosingTime(customers):
        """
        :type customers: str
        :rtype: int
        """
        customers = customers + 'Q'
        n = len(customers)
        pen = {}
        

        # We'll say customers[i] is the closing time
        for i in range(n):
            x = 0
            for j in range(n):
                if j < i:
                    if customers[j] == 'N':
                        x += 1
                if j >= i:
                    if customers[j] == 'Y':
                        x += 1
            pen[i] = x

        temp = min(pen.values())
        res = [key for key in pen if pen[key] == temp]
        
        return res[0]

customers = "YYYY"
y = bestClosingTime(customers)
print(y)

