# Indexing from scratch for fun
Having benefitted from `CREATE INDEX` over many years' worth of webapp buildling, I realized I was kind of conceptualizing it as free performance pixie dust and hadn't implemented an index from scratch before. So when I randomly saw this [comment](https://news.ycombinator.com/item?id=30604221)° on the Orange Site I made a note to actually try it on a weekend as a miniproject. That weekend finally arrived! 🎉

So basically [index-fun.py](./index-fun.py) is the result of me attempting to build baby's first index in Python, plus a binary search slightly modified to accomodate my ugly "index" 🤡 file.
The point was to take direct inspiration from how dead tree book indexes work - the text file is literally just a text file with sorted lines of
`$word,$index` e.g. `foo, 38`

Results:
```
tablescan found wiz @ 9971
tablescan runtime 0.0005388259887695312
binarySearch found wiz @ 9971
index runtime 0.0000209808
```

### TODO:
- [ ] Try something like this again but with btrees

<details>
<summary>° copy of the comment for convenience:</summary>

```
Take a large unordered text file and then create an ordered index in a separate file of word ==> line
write a brief binary search algo to search the index.
Compare searching the words with a "table scan" on the first file using grep, vs the binary search on the index.
You will find the table scan is O(n) and your binary search is roughly O(log n)
In 60 minutes you'll understand more about indexing than reading stack overflow.
```

</details>