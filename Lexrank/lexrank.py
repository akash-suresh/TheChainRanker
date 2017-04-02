

from summa.summarizer import summarize


fileName = "amazon.txt"
File = open(fileName) #open file
lines = File.read()


summary = summarize(lines)

print summary


