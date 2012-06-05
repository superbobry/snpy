       _____ _   _ _____
      / ____| \ | |  __ \
     | (___ |  \| | |__) |   _
      \___ \| . ` |  ___/ | | |
      ____) | |\  | |   | |_| |
     |_____/|_| \_|_|    \__, |
                          __/ |
                         |___/

An easy to use wrapper-library for working with [openSNP](http://opensnp.org)
data. The current implementation only supports local or downloaded files,
but [JSON API](http://opensnp.org/faq#api) interaction is planned.

All you need to remember at this point is a single function:

```python
>>> import sn
>>> snps = sn.parse("72.ftdna-illumina.36")
>>> sns
>>> snps[:1]
[_SNP(name='rs3094315', variation=None, chromosome='1', position=742429, strand=None, genotype='AA')]
```
