import argparse
import requests
import csv
import math

parser = argparse.ArgumentParser()
parser.add_argument("server", type=str)
parser.add_argument("port", type=int)
parser.add_argument("key", type=str)
parser.add_argument("--smaller", type=int, default=10)
parser.add_argument("--accuracy", type=int, default=1)
args = parser.parse_args()

resp = requests.get(f"http://{args.server}:{args.port}")
resp = resp.json()
resp = resp[args.key]
l_0 = []
l1 = []

with open("orbit_deviation.csv", mode="wt", encoding="utf-8") as csvfile:
    for keys, value in resp.items():
        l_0.append(value)
    wr = csv.writer(csvfile, delimiter=",")
    for i in range(len(l_0[3])):
        if l_0[0][i] >= args.smaller and l_0[1][i] and args.smaller and l_0[2][i] >= args.smaller:
            if l_0[0][i] >= l_0[1][i] and l_0[0][i] >= l_0[2][i]:
                l2 = "x"
            elif l_0[1][i] >= l_0[0][i] and l_0[1][i] >= l_0[2][i]:
                l2 = "y"
            else:
                l2 = "z"
            if l_0[0][i] <= l_0[1][i] and l_0[0][i] <= l_0[2][i]:
                l3 = "x"
            elif l_0[1][i] <= l_0[0][i] and l_0[1][i] <= l_0[2][i]:
                l3 = "y"
            else:
                l3 = "z"
            l1.append([i + 1, l_0[0][i], l_0[1][i], l_0[2][i], l2, l3])
    for i in l1:
        wr.writerow([i[0],
                     i[4],
                     max(i[1], i[2], i[3]),
                     i[5],
                     min(i[1], i[2], i[3]),
                     round(math.sqrt(i[1] ** 2 + i[2] ** 2 + i[3] ** 2), args.accuracy)
                     ])
