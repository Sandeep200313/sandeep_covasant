D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }

#UNION OF DICTIONARIES
D_UNION={}
for key in D1:
    D_UNION[key]=D1[key]
for key in D2:
    D_UNION[key]=D2[key]
print(D_UNION)


#INTERSECTION OF DICTINARIES
D_INTERSECT={}
for key in D1:
    if key in D2:
        D_INTERSECT[key]=D1[key]
print(D_INTERSECT)


#values are added for same keys
D_MERGE={}
for key in D1:
    D_MERGE[key]=D1[key]
for key in D2:
    if key in D_MERGE:
        D_MERGE[key]=D_MERGE[key]+D2[key]
    else:
        D_MERGE[key]=D2[key]
print(D_MERGE)