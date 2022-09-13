#Created on Mon Mar 29 11:54:19 2021 by Richard Wall

import pysam, argparse

parser = argparse.ArgumentParser(description='Counts barcodes from Leishmania barseq library')
parser.add_argument('-i',nargs='?',dest='infile',help='Input BAM file')

args = parser.parse_args()

args.total5prime = 'TCACCACCCTCAACCACCCCTCA' #total 5 prime reads
count5prime = 0

bamfilea = pysam.Samfile(args.infile,"rb")

for line in bamfilea:
	if args.total5prime in line.seq:
		count5prime += 1

print '5-prime-total', args.total5prime, count5prime 

args.total3prime = 'GCAGAGGAAGAGGAAGGCGAT' #total 3 prime reads
count3prime = 0

bamfileb = pysam.Samfile(args.infile,"rb")

for line in bamfileb:
	if args.total3prime in line.seq:
		count3prime += 1

print '3-prime-total', args.total3prime, count3prime

#to add more barcodes to the analysis - copy from here - see below
		
args.pIR1barcode0001 = 'TAGCATCAGATAGTGCTGAGTAG' #sequence pIR1-barcode-0001 (Wild type)
countpIR1barcode0001 = 0

bamfile1 = pysam.Samfile(args.infile,"rb")

for line in bamfile1:
	if args.pIR1barcode0001 in line.seq:
		countpIR1barcode0001 += 1

print 'pIR1-barcode-0001', args.pIR1barcode0001, countpIR1barcode0001

#to add more barcodes to analysis - copy to here - and paste at bottom - change ALL the '1's to the next number eg. '31' including the 'bamfile1'

args.pIR1barcode0002 = 'TAGTATGGCGTAGCGCAATATAG' #sequence pIR1-barcode-0002
countpIR1barcode0002 = 0

bamfile2 = pysam.Samfile(args.infile,"rb")

for line in bamfile2:
	if args.pIR1barcode0002 in line.seq:
		countpIR1barcode0002 += 1

print 'pIR1-barcode-0002', args.pIR1barcode0002, countpIR1barcode0002

args.pIR1barcode0003 = 'TAGGCTTCCATAGATCCTTGTAG' #sequence pIR1-barcode-0003
countpIR1barcode0003 = 0

bamfile3 = pysam.Samfile(args.infile,"rb")

for line in bamfile3:
	if args.pIR1barcode0003 in line.seq:
		countpIR1barcode0003 += 1

print 'pIR1-barcode-0003', args.pIR1barcode0003, countpIR1barcode0003

args.pIR1barcode0004 = 'TAGAGTGGCTTAGGACAATCTAG' #sequence pIR1-barcode-0004
countpIR1barcode0004 = 0

bamfile4 = pysam.Samfile(args.infile,"rb")

for line in bamfile4:
	if args.pIR1barcode0004 in line.seq:
		countpIR1barcode0004 += 1

print 'pIR1-barcode-0004', args.pIR1barcode0004, countpIR1barcode0004

args.pIR1barcode0005 = 'TAGTTCGCGTTAGCCTATACTAG' #sequence pIR1-barcode-0005
countpIR1barcode0005 = 0

bamfile5 = pysam.Samfile(args.infile,"rb")

for line in bamfile5:
	if args.pIR1barcode0005 in line.seq:
		countpIR1barcode0005 += 1

print 'pIR1-barcode-0005', args.pIR1barcode0005, countpIR1barcode0005

args.pIR1barcode0006 = 'TAGGTTCTGGTAGACCTCAATAG' #sequence pIR1-barcode-0006
countpIR1barcode0006 = 0

bamfile6 = pysam.Samfile(args.infile,"rb")

for line in bamfile6:
	if args.pIR1barcode0006 in line.seq:
		countpIR1barcode0006 += 1

print 'pIR1-barcode-0006', args.pIR1barcode0006, countpIR1barcode0006

args.pIR1barcode0007 = 'TAGAGAAGAATAGGAGGAGGTAG' #sequence pIR1-barcode-0007
countpIR1barcode0007 = 0

bamfile7 = pysam.Samfile(args.infile,"rb")

for line in bamfile7:
	if args.pIR1barcode0007 in line.seq:
		countpIR1barcode0007 += 1

print 'pIR1-barcode-0007', args.pIR1barcode0007, countpIR1barcode0007

args.pIR1barcode0008 = 'TAGGATCGACTAGAGCTAGTTAG' #sequence pIR1-barcode-0008
countpIR1barcode0008 = 0

bamfile8 = pysam.Samfile(args.infile,"rb")

for line in bamfile8:
	if args.pIR1barcode0008 in line.seq:
		countpIR1barcode0008 += 1

print 'pIR1-barcode-0008', args.pIR1barcode0008, countpIR1barcode0008

args.pIR1barcode0009 = 'TAGCGCAATCTAGTATGGCTTAG' #sequence pIR1-barcode-0009
countpIR1barcode0009 = 0

bamfile9 = pysam.Samfile(args.infile,"rb")

for line in bamfile9:
	if args.pIR1barcode0009 in line.seq:
		countpIR1barcode0009 += 1

print 'pIR1-barcode-0009', args.pIR1barcode0009, countpIR1barcode0009

args.pIR1barcode0010 = 'TAGCAACCATTAGTGGTTGCTAG' #sequence pIR1-barcode-0010
countpIR1barcode0010 = 0

bamfile10 = pysam.Samfile(args.infile,"rb")

for line in bamfile10:
	if args.pIR1barcode0010 in line.seq:
		countpIR1barcode0010 += 1

print 'pIR1-barcode-0010', args.pIR1barcode0010, countpIR1barcode0010

args.pIR1barcode0011 = 'TAGTCGCTCGTAGCTATCTATAG' #sequence pIR1-barcode-0011
countpIR1barcode0011 = 0

bamfile11 = pysam.Samfile(args.infile,"rb")

for line in bamfile11:
	if args.pIR1barcode0011 in line.seq:
		countpIR1barcode0011 += 1

print 'pIR1-barcode-0011', args.pIR1barcode0011, countpIR1barcode0011

args.pIR1barcode0012 = 'TAGCCTACACTAGTTCGTGTTAG' #sequence pIR1-barcode-0012
countpIR1barcode0012 = 0

bamfile12 = pysam.Samfile(args.infile,"rb")

for line in bamfile12:
	if args.pIR1barcode0012 in line.seq:
		countpIR1barcode0012 += 1

print 'pIR1-barcode-0012', args.pIR1barcode0012, countpIR1barcode0012

args.pIR1barcode0013 = 'TAGGCAAGAGTAGATGGAGATAG' #sequence pIR1-barcode-0013
countpIR1barcode0013 = 0

bamfile13 = pysam.Samfile(args.infile,"rb")

for line in bamfile13:
	if args.pIR1barcode0013 in line.seq:
		countpIR1barcode0013 += 1

print 'pIR1-barcode-0013', args.pIR1barcode0013, countpIR1barcode0013

args.pIR1barcode0014 = 'TAGAGACAACTAGGAGTGGTTAG' #sequence pIR1-barcode-0014
countpIR1barcode0014 = 0

bamfile14 = pysam.Samfile(args.infile,"rb")

for line in bamfile14:
	if args.pIR1barcode0014 in line.seq:
		countpIR1barcode0014 += 1

print 'pIR1-barcode-0014', args.pIR1barcode0014, countpIR1barcode0014

args.pIR1barcode0015 = 'TAGTGCACTCTAGCATGTCTTAG' #sequence pIR1-barcode-0015
countpIR1barcode0015 = 0

bamfile15 = pysam.Samfile(args.infile,"rb")

for line in bamfile15:
	if args.pIR1barcode0015 in line.seq:
		countpIR1barcode0015 += 1

print 'pIR1-barcode-0015', args.pIR1barcode0015, countpIR1barcode0015

args.pIR1barcode0016 = 'TAGCTCCTACTAGTCTTCGTTAG' #sequence pIR1-barcode-0016
countpIR1barcode0016 = 0

bamfile16 = pysam.Samfile(args.infile,"rb")

for line in bamfile16:
	if args.pIR1barcode0016 in line.seq:
		countpIR1barcode0016 += 1

print 'pIR1-barcode-0016', args.pIR1barcode0016, countpIR1barcode0016

args.pIR1barcode0017 = 'TAGATGGAATTAGGCAAGGCTAG' #sequence pIR1-barcode-0017
countpIR1barcode0017 = 0

bamfile17 = pysam.Samfile(args.infile,"rb")

for line in bamfile17:
	if args.pIR1barcode0017 in line.seq:
		countpIR1barcode0017 += 1

print 'pIR1-barcode-0017', args.pIR1barcode0017, countpIR1barcode0017

args.pIR1barcode0018 = 'TAGGCGTGGATAGATACAAGTAG' #sequence pIR1-barcode-0018
countpIR1barcode0018 = 0

bamfile18 = pysam.Samfile(args.infile,"rb")

for line in bamfile18:
	if args.pIR1barcode0018 in line.seq:
		countpIR1barcode0018 += 1

print 'pIR1-barcode-0018', args.pIR1barcode0018, countpIR1barcode0018

args.pIR1barcode0019 = 'TAGCACAGCTTAGTGTGATCTAG' #sequence pIR1-barcode-0019
countpIR1barcode0019 = 0

bamfile19 = pysam.Samfile(args.infile,"rb")

for line in bamfile19:
	if args.pIR1barcode0019 in line.seq:
		countpIR1barcode0019 += 1

print 'pIR1-barcode-0019', args.pIR1barcode0019, countpIR1barcode0019

args.pIR1barcode0020 = 'TAGATAACTGTAGGCGGTCATAG' #sequence pIR1-barcode-0020
countpIR1barcode0020 = 0

bamfile20 = pysam.Samfile(args.infile,"rb")

for line in bamfile20:
	if args.pIR1barcode0020 in line.seq:
		countpIR1barcode0020 += 1

print 'pIR1-barcode-0020', args.pIR1barcode0020, countpIR1barcode0020

args.pIR1barcode0021 = 'TAGTGGTCGATAGCAACTAGTAG' #sequence pIR1-barcode-0021
countpIR1barcode0021 = 0

bamfile21 = pysam.Samfile(args.infile,"rb")

for line in bamfile21:
	if args.pIR1barcode0021 in line.seq:
		countpIR1barcode0021 += 1

print 'pIR1-barcode-0021', args.pIR1barcode0021, countpIR1barcode0021

args.pIR1barcode0022 = 'TAGAGAATAGTAGGAGGCGATAG' #sequence pIR1-barcode-0022
countpIR1barcode0022 = 0

bamfile22 = pysam.Samfile(args.infile,"rb")

for line in bamfile22:
	if args.pIR1barcode0022 in line.seq:
		countpIR1barcode0022 += 1

print 'pIR1-barcode-0022', args.pIR1barcode0022, countpIR1barcode0022

args.pIR1barcode0023 = 'TAGCTCAGTATAGTCTGACGTAG' #sequence pIR1-barcode-0023
countpIR1barcode0023 = 0

bamfile23 = pysam.Samfile(args.infile,"rb")

for line in bamfile23:
	if args.pIR1barcode0023 in line.seq:
		countpIR1barcode0023 += 1

print 'pIR1-barcode-0023', args.pIR1barcode0023, countpIR1barcode0023

args.pIR1barcode0024 = 'TAGTATCAGTTAGCGCTGACTAG' #sequence pIR1-barcode-0024
countpIR1barcode0024 = 0

bamfile24 = pysam.Samfile(args.infile,"rb")

for line in bamfile24:
	if args.pIR1barcode0024 in line.seq:
		countpIR1barcode0024 += 1

print 'pIR1-barcode-0024', args.pIR1barcode0024, countpIR1barcode0024

args.pIR1barcode0025 = 'TAGAGCAACATAGGATGGTGTAG' #sequence pIR1-barcode-0025
countpIR1barcode0025 = 0

bamfile25 = pysam.Samfile(args.infile,"rb")

for line in bamfile25:
	if args.pIR1barcode0025 in line.seq:
		countpIR1barcode0025 += 1

print 'pIR1-barcode-0025', args.pIR1barcode0025, countpIR1barcode0025

args.pIR1barcode0026 = 'TAGTGTAGCGTAGCACGATATAG' #sequence pIR1-barcode-0026
countpIR1barcode0026 = 0

bamfile26 = pysam.Samfile(args.infile,"rb")

for line in bamfile26:
	if args.pIR1barcode0026 in line.seq:
		countpIR1barcode0026 += 1

print 'pIR1-barcode-0026', args.pIR1barcode0026, countpIR1barcode0026

args.pIR1barcode0027 = 'TAGCAGAACATAGTGAGGTGTAG' #sequence pIR1-barcode-0027
countpIR1barcode0027 = 0

bamfile27 = pysam.Samfile(args.infile,"rb")

for line in bamfile27:
	if args.pIR1barcode0027 in line.seq:
		countpIR1barcode0027 += 1

print 'pIR1-barcode-0027', args.pIR1barcode0027, countpIR1barcode0027

args.pIR1barcode0028 = 'TAGACCAAGATAGGTTGGAGTAG' #sequence pIR1-barcode-0028
countpIR1barcode0028 = 0

bamfile28 = pysam.Samfile(args.infile,"rb")

for line in bamfile28:
	if args.pIR1barcode0028 in line.seq:
		countpIR1barcode0028 += 1

print 'pIR1-barcode-0028', args.pIR1barcode0028, countpIR1barcode0028

args.pIR1barcode0029 = 'TAGGCAATCGTAGATGGCTATAG' #sequence pIR1-barcode-0029
countpIR1barcode0029 = 0

bamfile29 = pysam.Samfile(args.infile,"rb")

for line in bamfile29:
	if args.pIR1barcode0029 in line.seq:
		countpIR1barcode0029 += 1

print 'pIR1-barcode-0029', args.pIR1barcode0029, countpIR1barcode0029

args.pIR1barcode0030 = 'TAGCAACAGCTAGTGGTGATTAG' #sequence pIR1-barcode-0030
countpIR1barcode0030 = 0

bamfile30 = pysam.Samfile(args.infile,"rb")

for line in bamfile30:
	if args.pIR1barcode0030 in line.seq:
		countpIR1barcode0030 += 1

print 'pIR1-barcode-0030', args.pIR1barcode0030, countpIR1barcode0030

#paste new barcodes here

print 'total-barcodes', 'All-barcodes-combined', (countpIR1barcode0001 + countpIR1barcode0002 + countpIR1barcode0003 + countpIR1barcode0004 + countpIR1barcode0005 + countpIR1barcode0006 + countpIR1barcode0007 + countpIR1barcode0008 + countpIR1barcode0009 + countpIR1barcode0010 + countpIR1barcode0011 + countpIR1barcode0012 + countpIR1barcode0013 + countpIR1barcode0014 + countpIR1barcode0015 + countpIR1barcode0016 + countpIR1barcode0017 + countpIR1barcode0018 + countpIR1barcode0019 + countpIR1barcode0020 + countpIR1barcode0021 + countpIR1barcode0022 + countpIR1barcode0023 + countpIR1barcode0024 + countpIR1barcode0025 + countpIR1barcode0026 + countpIR1barcode0027 + countpIR1barcode0028 + countpIR1barcode0029 + countpIR1barcode0030)




