import collections


class StupidSolution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        x0, x1, y0, y1 = 1, 1, 1, 1
        d = set()
        count = 0
        for rect in rectangles:
            [cx0, cy0, cx1, cy1] = rect
            if x0 > cx0: x0 = cx0
            if x1 < cx1: x1 = cx1
            if y0 > cy0: y0 = cy0
            if y1 < cy1: y1 = cy1
            for i in range(cx0, cx1):
                for j in range(cy0, cy1):
                    if (i, j) in d:
                        return False
                    d.add((i, j))
                    count += 1
        return count == (x1 - x0) * (y1 - y0)


class StupidSolution2(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        x0, x1, y0, y1 = 1, 1, 1, 1
        count = 0
        for idx, rect in enumerate(rectangles):
            [cx0, cy0, cx1, cy1] = rect
            if x0 > cx0: x0 = cx0
            if x1 < cx1: x1 = cx1
            if y0 > cy0: y0 = cy0
            if y1 < cy1: y1 = cy1
            for j in range(idx + 1, len(rectangles)):
                [rx0, ry0, rx1, ry1] = rectangles[j]
                if not (rx0 >= cx1 or cx0 >= rx1 or ry0 >= cy1 or cy0 >= ry1):
                    return False
            count += (cx1 - cx0) * (cy1 - cy0)
        return count == (x1 - x0) * (y1 - y0)


class GoodSolution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        left = min(x[0] for x in rectangles)
        bottom = min(x[1] for x in rectangles)
        right = max(x[2] for x in rectangles)
        top = max(x[3] for x in rectangles)

        points = collections.defaultdict(int)
        for l, b, r, t in rectangles:
            A, B, C, D = (l, b), (r, b), (r, t), (l, t)
            for p, q in zip((A, B, C, D), (1, 2, 4, 8)):
                if points[p] & q: return False
                points[p] |= q

        for px, py in points:
            if left < px < right or bottom < py < top:
                if points[(px, py)] not in (3, 6, 9, 12, 15):
                    return False
        return True