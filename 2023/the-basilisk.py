'''
One-line Python solution for Advent of Code 2023 (https://adventofcode.com/2023/)
Written by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code, affectionately nicknamed the Basilisk.
           Current progress:
            Day | Pt1 | Pt2
           -----------------
             01 |  ✔  |  ✔
             02 |  ✔  |  ✔
             03 |  ✔  |  ✔
             04 |  ✔  |  ✔
             05 |  ✔  |  ✔
             06 |  ✔  |  ✔
             07 |  ✔  |  ✔
             08 |  ✔  |  ✔
             09 |  ✔  |  ✔
             10 |  ✖  |  ✖
             11 |  ✔  |  ✔
             12 |  ✔  |  ✔
             13 |  ✖  |  ✖
             14 |  ✔  |  ✔
             15 |  ✔  |  ✔
See README and explanation of solutions at https://github.com/savbell/advent-of-code-one-liners
'''

# Input files not included in repo per Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# To run the Basilisk, replace with the paths to your own input files
f = {
    1 : '2023/day-01.txt',
    2 : '2023/day-02.txt',
    3 : '2023/day-03.txt',
    4 : '2023/day-04.txt',
    5 : '2023/day-05.txt',
    6 : '2023/day-06.txt',
    7 : '2023/day-07.txt',
    8 : '2023/day-08.txt',
    9 : '2023/day-09.txt',
    # 10: '2023/day-10.txt', # Still working on both parts...
    11: '2023/day-11.txt',
    12: '2023/day-12.txt',
    # 13: '2023/day-13.txt', # Still working on both parts...
    14: '2023/day-14.txt',
    15: '2023/day-15.txt',
}

################################ THE BASILISK ################################
print((re:=__import__('re') or 1) and (ft:=__import__('functools') or 1) and (it:=__import__('itertools') or 1) and (math:=__import__('math') or 1) and (q:={d:open(p).read().strip() for d,p in f.items()}) and 'Day 01 Part 1:',sum([(d:=re.findall(r'\d',l)) and int(d[0]+d[-1]) for l in q[1].split('\n')]),'\nDay 01 Part 2:',sum([int(''.join([{'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}[d] if d.isalpha() else d for d in [n[0],n[-1]]])) for l in q[1].split('\n') for n in [re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))',l)]]),'\nDay 02 Part 1:',sum([int(g[0]) for g in re.findall(r'(\d+):((?: *\d+\s+\w+,?;?)+)',q[2])])-sum([int(g[0]) for g in re.findall(r'Game (\d+):((?:\s*\d+\s+\w+,?;?)+)',q[2]) if any([int(d[0])>12 and d[1]=='red' or int(d[0])>13 and d[1]=='green' or int(d[0])>14 and d[1]=='blue' for d in re.findall(r'(\d+)\s+(\w+)',g[1])])]),'\nDay 02 Part 2:',sum([(m:=re.findall(r'(\d+)\s+(\w+)',g[1])) and max([int(d[0]) for d in m if d[1]=='red'])*max([int(d[0]) for d in m if d[1]=='green'])*max([int(d[0]) for d in m if d[1]=='blue']) for g in re.findall(r'(\d+):((?: *\d+\s+\w+,?;?)+)',q[2])]),'\nDay 03 Part 1:',sum([int(n[0]) for n in [[n.group(),[(x,n.start()+i) for i in range(len(n.group()))]] for x,l in enumerate(q[3].split('\n')) for n in re.finditer(r'\d+',l)] if any([abs(c[0]-s[1][0])<=1 and abs(c[1]-s[1][1])<=1 for c in n[1] for s in [[s.group(),(x,s.start())] for x,l in enumerate(q[3].split('\n')) for s in re.finditer(r'[^.\d]',l)]])]),'\nDay 03 Part 2:',(r:=[[s.group(),(x,s.start()),[]] for x,l in enumerate(q[3].split('\n')) for s in re.finditer(r'[*]',l)]) and [s[2].append(n) if n not in s[2] else 0 for n in [[int(n.group()),[(x,n.start()+i) for i in range(len(n.group()))]] for x,l in enumerate(q[3].split('\n')) for n in re.finditer(r'\d+',l)] for c in n[1] for s in r if abs(c[0]-s[1][0])<=1 and abs(c[1]-s[1][1])<=1] and sum([s[2][0][0]*s[2][1][0] for s in r if len(s[2])==2]),'\nDay 04 Part 1:',sum([2**(len(n)-1) if len(n)>0 else 0 for n in [n[0].intersection(n[1]) for n in [(set(map(int,n[0].split())),set(map(int,n[1].split()))) for n in re.findall(r': +((?:\d+\s+)+)\| +((?:\d+\s*)+)',q[4])]]]),'\nDay 04 Part 2:',((c:=[[1,len(n[0].intersection(n[1]))] for n in [(set(map(int,n[0].split())), set(map(int,n[1].split()))) for n in re.findall(r'\d+: +((?:\d+\s+)+)\| +((?:\d+\s*)+)',q[4])]]) and not (t:=0) and [(t:=t+n[0]) and [c.__setitem__(i+j,[c[i+j][0]+1,c[i+j][1]]) for _ in range(n[0]) for j in range(1,n[1]+1)] for i, n in enumerate(c)] and t),'\nDay 05 Part 1:',(v:=[[list(map(int,l.split())) for l in d.split('\n')] for d in [d for _,d in [re.split(r':\n',s) for s in re.split(r'\n\n',q[5])[1:]]]]) and (c:=lambda i,m:(lambda c:c[0]+(i-c[1]) if c[1]+c[2]>i else i)(min([y for y in m if y[1]<=i],default=[0,0,0],key=lambda x:i-x[1]))) and min([c(s,v[6])for s in [c(s,v[5]) for s in [c(s,v[4]) for s in [c(s,v[3]) for s in [c(s,v[2]) for s in [c(s,v[1]) for s in [c(s,v[0]) for s in list(map(int,re.split(r'\n\n',q[5])[0].split()[1:]))]]]]]]]),'\nDay 05 Part 2:',[(v:=re.split(r'\n\n',q[5])) and (s:=list(map(int,v[0].split()[1:]))) and (m:=v[1:]) and (c:=[(a,a+b) for a,b in zip(s[::2],s[1::2])]) and [[(w:=[tuple(map(int,x.split())) for x in g.split('\n')[1:]]) and (u:=[-99]) and (o:=[0]) and (l:=-99) and [(l:=max(l,(p:=r[0] - r[1])+r[1]+r[2])) and [(not u.__setitem__(-1,r[1]) and not o.__setitem__(-1,p)) if u and u[-1]==r[1] else (u.__iadd__([r[1]])) and o.__iadd__([p])] and (u.__iadd__([r[1]+r[2]]) and o.__iadd__([0])) for r in sorted(w,key=lambda x: x[1])] and not (t:=[]) and [(j:=[i[0]]) and not (h:=None) and [(((h:=d-1) if h is None else 0) and (j.__iadd__([p]) if p < i[1] and p != i[1] else 0) if not p <= j[-1] else 0) for d,p in enumerate(u)] and (j.__iadd__([i[1]]) and (h:=h or len(o))) and [(d:=o[min(h or float('inf'),len(o)-1)]) and (h:=h+1) and t.__iadd__([(a+d,b+d)]) for a,b in zip(j,j[1:])] for i in c]] and (c:=t) for g in m]] and min(x[0] for x in c),'\nDay 06 Part 1:',(so:=lambda b,c:[(b+((b**2)-(4*c))**0.5)/2,(b-((b**2)-(4*c))**0.5)/2]) and (h:=lambda i:int(i[1])-int(i[0]) if i[0]<i[1] else int(i[0])-int(i[1]) if i[0]%1!=0 else int(i[0])-int(i[1])-1) and (u:=[int(n) for n in re.findall(r'\d+',q[6])]) and ft.reduce(lambda a,b:a*b,[h(so(r[0], r[1])) for r in [[u[i],u[i+int(len(u)/2)]] for i in range(int(len(u)/2))]]),'\nDay 06 Part 2:',(so:=lambda b,c:[(b+((b**2)-(4*c))**0.5)/2,(b-((b**2)-(4*c))**0.5)/2]) and (h:=lambda i:int(i[1])-int(i[0]) if i[0]<i[1] else int(i[0])-int(i[1]) if i[0]%1!=0 else int(i[0])-int(i[1])-1) and (u:=[n for n in re.findall(r'\d+',q[6])]) and (r:=[int(''.join([u[i] for i in range(int(len(u)/2))])), int(''.join([u[i] for i in range(int(len(u)/2),len(u))]))]) and h(so(r[0], r[1])),'\nDay 07 Part 1:',(y:=[[['AKQJT98765432'.index(c)+1 for c in g.split()[0]],g.split()[1]] for g in q[7].split('\n')]) and [g.__iadd__([(s:=sorted(g[0])) and (7 if len(set(s))==1 else 6 if s[0]==s[1]==s[2]==s[3] or s[1]==s[2]==s[3]==s[4] else 5 if s[0]==s[1]==s[2] and s[3]==s[4] or s[0]==s[1] and s[2]==s[3]==s[4] else 4 if s[0]==s[1]==s[2] or s[1]==s[2]==s[3] or s[2]==s[3]==s[4] else 3 if s[0]==s[1] and s[2]==s[3] or s[0]==s[1] and s[3]==s[4] or s[1]==s[2] and s[3]==s[4] else 2 if len(set(s))==4 else 1)]) for g in y] and sum([int(g[1])*(i+1) for i, g in enumerate([g for g in [list(g) for _,g in it.groupby(sorted(y,key=lambda x:x[2]), lambda x:x[2])] for g in sorted(g,key=lambda x:x[0],reverse=True)])]),'\nDay 07 Part 2:',(y:=[[['AKQT98765432J'.index(c)+1 for c in g.split()[0]],g.split()[1]] for g in q[7].split('\n')]) and (score:=lambda h:(7 if len(set(h)) == 1 or len(set(h)) == 2 and 13 in h else 0) or (s:=sorted([min([c for c in h if h.count(c) == max([h.count(c) for c in h if c != 13])]) if c == 13 else c for c in h])) and (6 if s[0]==s[1]==s[2]==s[3] or s[1]==s[2]==s[3]==s[4] else 5 if s[0]==s[1]==s[2] and s[3]==s[4] or s[0]==s[1] and s[2]==s[3]==s[4] else 4 if s[0]==s[1]==s[2] or s[1]==s[2]==s[3] or s[2]==s[3]==s[4] else 3 if s[0]==s[1] and s[2]==s[3] or s[0]==s[1] and s[3]==s[4] or s[1]==s[2] and s[3]==s[4] else 2 if len(set(s))==4 else 1)) and [g.__iadd__([score(g[0])]) for g in y] and sum([int(g[1])*(i+1) for i, g in enumerate([g for g in [list(g) for _,g in it.groupby(sorted(y,key=lambda x:x[2]),lambda x:x[2])] for g in sorted(g,key=lambda x:x[0],reverse=True)])]),'\nDay 08 Part 1:',(i:=q[8].split('\n')[0]) and (g:=[re.findall(r'(\w+) = \((\w+), (\w+)\)',l) for l in q[8].split('\n')[2:]]) and (g:=(u:=g[0][0][0]) and {o[0][0]:o[0][1:] for o in g}) and not (k:=0) and [((k:=k+1) and (u:=g[u][1] if d=='R' else g[u][0])) for d in it.takewhile(lambda _:(not u.endswith('Z')),it.cycle(i))] and k,'\nDay 08 Part 2:',(i:=q[8].split('\n')[0]) and (g:=[re.findall(r'(\w+) = \((\w+), (\w+)\)', l) for l in q[8].split('\n')[2:]]) and (f:=[n[0][0] for n in g if n[0][0].endswith('A')]) and (g:={n[0][0]: n[0][1:] for n in g}) and not (a:=[]) and [(u:=o) and not (k:=0) and [((k:=k+1) and (u:=g[u][1] if d == 'R' else g[u][0])) for d in it.takewhile(lambda _:(not u.endswith('Z')),it.cycle(i))] and (a.__iadd__([k])) for o in f] and math.lcm(*a),'\nDay 09 Part 1:',sum((h:=[list(map(int,x.split())) for x in q[9].split('\n')]) and not (p:=[]) and [not (b:=[]) and (c:=a.copy()) and [b.__iadd__([c[-1]]) and (c:=[c[i+1]-c[i] for i in range(len(c)-1)]) for _ in it.takewhile(lambda _:not all([x==0 for x in c]),it.repeat(None))] and p.__iadd__([ft.reduce(lambda x,y:x+y,b[::-1])]) for a in h] and p),'\nDay 09 Part 2:',sum((h:=[list(map(int,x.split())) for x in q[9].split('\n')]) and not (p:=[]) and [not (b:=[]) and (c:=a.copy()) and [b.__iadd__([c[0]]) and (c:=[c[i+1]-c[i] for i in range(len(c)-1)]) for _ in it.takewhile(lambda _:not all([x==0 for x in c]),it.repeat(None))] and b.__iadd__([0]) and p.__iadd__(not (e:=0) and [e:=n-e for n in b[::-1]] and [e]) for a in h] and p),'\nDay 11 Part 1:',sum((s:=[(x,y) for y,r in enumerate(q[11].strip().split()) for x,c in enumerate(r) if c=='#']) and not (e:=[y for y in range(max(s,key=lambda x:x[1])[1]+1) if not any([y==g[1] for g in s])]) and (o:=[x for x in range(max(s,key=lambda x:x[0])[0]+1) if not any([x==g[0] for g in s])]) and (s:=[(g[0]+len([x for x in o if x<g[0]]),g[1]+len([y for y in e if y<g[1]])) for g in s]) and not (p:={}) and [p.__setitem__((i,j),abs(i[0]-j[0])+abs(i[1]-j[1])) for i in s for j in s if i!=j and (j,i) not in p] and p.values()),'\nDay 11 Part 2:',sum((s:=[(x,y) for y,r in enumerate(q[11].strip().split()) for x,c in enumerate(r) if c=='#']) and not (e:=[y for y in range(max(s,key=lambda x:x[1])[1]+1) if not any([y==g[1] for g in s])]) and (o:=[x for x in range(max(s,key=lambda x:x[0])[0]+1) if not any([x==g[0] for g in s])]) and (s:=[(g[0]+(len([x for x in o if x<g[0]])*999999),g[1]+(len([y for y in e if y<g[1]])*999999)) for g in s]) and not (p:={}) and [p.__setitem__((i,j),abs(i[0]-j[0])+abs(i[1]-j[1])) for i in s for j in s if i!=j and (j,i) not in p] and p.values()),'\nDay 12 Part 1:',sum([not (r:=set()) and [r.update([''.join(c) for c in it.product(*([['#','.'] if s=='?' else [s] for s in y])) if [len(x) for x in re.findall(r'#+',''.join(c))]==u]) for y,u in [s]] and len(r) for s in [[x[0],[int(y) for y in x[1].split(',')]] for x in [x.split() for x in q[12].strip().split('\n')]]]),'\nDay 12 Part 2:',sum((c:=ft.cache(lambda b,n,g=0: (not (r:=0) and [(r:=r+c(b[1:],n,g+1)) if p=='#' else 1 and (g > 0 and (n and n[0]==g and (r:=r+c(b[1:],n[1:])))) or (g==0 and (r:=r+c(b[1:],n))) if p!='#' else 1 for p in (['.','#'] if b[0]=='?' else b[0])] and r) if b else not n and not g)) and [c(s[0],s[1]) for s in [('?'.join([x[0]]*5)+'.',x[1]*5) for x in [(x[0],tuple(map(int,x[1].split(',')))) for x in [x.split() for x in q[12].strip().split('\n')]]]]),'\nDay 14 Part 1:',sum((p:=[list(x) for x in q[14].strip().split('\n')]) and not p.insert(0,['#']*len(p[0])) and [[(p[i][j]=='O') and [(p[k][j]=='.') and [(p[k][j]=='.' and not p[k].__setitem__(j,'O') and p[k+1].__setitem__(j,'.'))] for k in it.takewhile(lambda x:p[x][j]!='#',range(i-1,-1,-1))] for j in range(len(p[0]))] for i in range(len(p))] and [sum([1 for x in p if x=='O'])*(i+1) for i,p in enumerate(p[::-1])]),'\nDay 14 Part 2:',sum((t:=lambda p,d:(((d==1) and [[(p[i][j]=='O') and [(p[k][j]=='.') and [(p[k][j]=='.' and not p[k].__setitem__(j,'O') and p[k+1].__setitem__(j,'.'))] for k in it.takewhile(lambda x:p[x][j]!='#',range(i-1,-1,-1))] for j in range(len(p[0]))] for i in range(len(p))]) or ((d==2) and [[(p[i][j]=='O') and [(p[i][k]=='.') and [(p[i][k]=='.' and not p[i].__setitem__(k,'O') and p[i].__setitem__(k+1,'.'))] for k in it.takewhile(lambda x:p[i][x]!='#',range(j-1,-1,-1))]] for i in range(len(p)) for j in range(len(p[0]))]) or (d==3) and [(p[i][j]=='O') and [(p[k][j]=='.') and [(p[k][j]=='.' and not p[k].__setitem__(j,'O') and p[k-1].__setitem__(j,'.'))] for k in it.takewhile(lambda x:p[x][j]!='#',range(i+1,len(p)))] for j in range(len(p[0])) for i in range(len(p)-1,-1,-1)] or (d==4) and [(p[i][j]=='O') and [(p[i][k]=='.') and [(p[i][k]=='.' and not p[i].__setitem__(k,'O') and p[i].__setitem__(k-1,'.'))] for k in it.takewhile(lambda x:p[i][x]!='#',range(j+1,len(p[0])))] for i in range(len(p)) for j in range(len(p[0])-1,-1,-1)]) and p) and (o:=lambda p:'y'.join(['x'.join(x) for x in p])) and (g:=lambda x:[x.split('x') for x in x.split('y')]) and (p:=[['#']+list(x)+['#'] for x in q[14].strip().split('\n')]) and not p.insert(0,['#']*len(p[0])) and not p.append(['#']*len(p[0])) and (s:=[o(p)]) and [(p:=t(t(t(t(p,1),2),3),4)) and (o(p) not in s) and s.append(o(p)) for _ in it.takewhile(lambda x:o(p) not in s[:-1],it.repeat(None))] and (p:=g(s[(1000000000-(b:=s.index(o(p)))) % (len(s)-b)+b])) and [sum([1 for x in p if x=='O'])*(i) for i,p in enumerate(p[::-1])]),'\nDay 15 Part 1:',sum([(v:=0) or [v:=(v+ord(c))*17%256 for c in s] and v for s in q[15].split(',')]),'\nDay 15 Part 2:',sum((b:=[[] for _ in range(256)]) and [((l:=''.join([c for c in s if c.isalpha()])) and (o:=''.join([c for c in s if not c.isalnum()])) and (f:=''.join([c for c in s if c.isdigit()])) and (d:=(l,f)) and (a:=0) or 1) and not (a:=0) and [a:=(a+ord(c))*17%256 for c in l] and ((b[a].append(d) if l not in [x[0] for x in b[a]] else ((e:=[x[0] for x in b[a]].index(l)) or 1) and b[a].pop(e) and b[a].insert(e,d)) if o=='=' else b[a].pop([x[0] for x in b[a]].index(l)) if l in [x[0] for x in b[a]] else 0) for s in q[15].split(',')] and [(i+1)*(j+1)*int(n[1]) for i,p in enumerate(b) for j,n in enumerate(p)]))