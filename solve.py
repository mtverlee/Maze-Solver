"""

Maze-Solver
By: Matt VerLee
mtverlee@mavs.coloradomesa.edu
https://github.com/mtverlee

"""

import numpy as np;
from PIL import Image;
import time
from mazes import Maze;
from factory import SolverFactory;
import argparse

sf = SolverFactory();
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--method", nargs='?', const=sf.Default, default=sf.Default,
						choices=sf.Choices)
parser.add_argument("input_file")
parser.add_argument("output_file")
args = parser.parse_args()

method = args.method;

print ("Loading Image...");
im = Image.open(args.input_file);

print ("Reading Image...");
t0 = time.time()
maze = Maze(im);
t1 = time.time()
print ("Node Count:", maze.count);
total = t1-t0
print ("Time elapsed:", total, "\n");

[title, solver] = sf.createsolver(args.method);
print ("Starting Solve:", title);

t0 = time.time()
[result, stats] = solver(maze);
t1 = time.time()

total = t1-t0

print ("Nodes explored: ", stats[0]);
if (stats[2]):
	print ("Path found - length was:", stats[1]);
else:
	print ("No Path Found!");
print ("Time elapsed: ", total, "\n");

print ("Saving Image...");
mazeimage = np.array(im)
imout = np.array(mazeimage);
imout[imout==1] = 255;
out = imout[:,:,np.newaxis];

out = np.repeat(out, 3, axis=2);

resultpath = [n.Position for n in result];

length = len(resultpath);

px = [0, 0, 0];
for i in range(0, length - 1):
	a = resultpath[i];
	b = resultpath[i+1];

	px[0] = int((i / length) * 255);
	px[2] = 255 - px[0];

	if a[0] == b[0]:
		for x in range(min(a[1],b[1]), max(a[1],b[1])):
			out[a[0],x,:] = px
	elif a[1] == b[1]:
		for y in range(min(a[0],b[0]), max(a[0],b[0]) + 1):
			out[y,a[1],:] = px

img = Image.fromarray(out);
img.save(args.output_file)
print("Done!")
