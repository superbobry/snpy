# -*- coding: utf-8 -*-

import csv
import os.path
from collections import namedtuple

try:
    import vcf
except ImportError:
    vcf = None


_SNP = namedtuple("_SNP", ["name",
                           "variation",
                           "chromosome",
                           "position",
                           "strand",
                           "genotype"])


class SNP(_SNP):
    def __new__(cls, name, chromosome, position, genotype,
                variation=None, strand=None):
        return super(SNP, cls).__new__(cls, name, variation, chromosome,
                                       int(position), strand, genotype)


def _23andme(path):
    handle = csv.DictReader(open(path, "rb"),
        fieldnames=["name", "chromosome", "position", "genotype"],
        delimiter="\t")

    for row in handle:
        if not row["name"].startswith("#"):
            yield SNP(**row)


def _23andme_exome(path):
    if vcf is None:
        raise RuntimeError("PyVCF not available, please 'easy_install' it.")

    for r in vcf.VCFReader(open(path, "rb")):
        for sample in r.samples:
            yield SNP(name=r.ID, chromosome=r.CHROM, position=r.POS,
                      genotype=sample.gt_bases.replace("/", ""))


def decodeme(path):
    handle = csv.DictReader(open(path, "rb"),
        fieldnames=["name", "variation", "chromosome", "position",
                    "strand", "genotype"])

    for row in handle:
        # A flanky header criterion -- the last column should be
        # 'XX', where X is one of "ACGT-".
        if len(row["genotype"]) == 2:
            yield SNP(**row)


def ftdna(path):
    handle = csv.DictReader(open(path, "rb"),
        fieldnames=["name", "chromosome", "position", "genotype"])

    for row in handle:
        if row["position"].isdigit():
            yield SNP(**row)


def parse(path, source=None):
    if source is None:
        _, source, _ = path.rsplit(os.path.extsep)

    try:
        handler = {"23andme": _23andme,
                   "23andme-exome-vcf": _23andme_exome,
                   "decodeme": decodeme,
                   "ftdna-illumina": ftdna}[source]
    except KeyError:
        raise RuntimeError("Unsupported source: {0!r}".format(source))
    else:
        return list(handler(path))
