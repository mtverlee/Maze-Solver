class Maze:
	class Node:
		def __init__(self, position):
			self.Position = position;
			self.Neighbours = [None, None, None, None];

	def __init__(self, im):

		width = im.width;
		height = im.height;
		data = list(im.getdata(0));

		self.start = None;
		self.end = None;

		topnodes = [None] * width;
		count = 0;
		
		for x in range (1, width - 1):
			if data[x] > 0:
				self.start = Maze.Node((0,x));
				topnodes[x] = self.start;
				count += 1;

		for y in range (1, height - 1):
			print ("row", str(y));
			
			rowoffset = y * width;
			rowaboveoffset = rowoffset - width;
			rowbelowoffset = rowoffset + width;

			prv = False;
			cur = False;
			nxt = data[rowoffset + 1] > 0;

			leftnode = None;

			for x in range (1, width - 1):
				prv = cur;
				cur = nxt;
				nxt = data[rowoffset + x + 1] > 0;

				n = None;

				if cur == False:
					continue;
				
				if prv == True:
					if nxt == True:
						if data[rowaboveoffset + x] > 0 or data[rowbelowoffset + x] > 0:
							n = Maze.Node((y,x));
							leftnode.Neighbours[1] = n;
							n.Neighbours[3] = leftnode;
							leftnode = n;
					else:
						n = Maze.Node((y,x));
						leftnode.Neighbours[1] = n;
						n.Neighbours[3] = leftnode;
						leftnode = None;
				else:
					if nxt == True:
						n = Maze.Node((y,x));
						leftnode = n;
					else:
						if (data[rowaboveoffset + x] == 0) or (data[rowbelowoffset + x] == 0):
							n = Maze.Node((y,x));

				if n != None:
					if (data[rowaboveoffset + x] > 0):
						t = topnodes[x];
						t.Neighbours[2] = n;
						n.Neighbours[0] = t;

					if (data[rowbelowoffset + x] > 0):
						topnodes[x] = n;
					else:
						topnodes[x] = None;

					count += 1;

		rowoffset = (height - 1) * width;
		for x in range (1, width - 1):
			if data[rowoffset + x] > 0:
				self.end = Maze.Node((height - 1,x));
				t = topnodes[x];
				t.Neighbours[2] = self.end;
				self.end.Neighbours[0] = t;
				count += 1;

		self.count = count;
		self.width = width;
		self.height = height;

