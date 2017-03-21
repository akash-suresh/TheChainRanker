from summa import summarizer


fileName = "amazon.txt"
File = open(fileName) #open file
lines = File.read()


summary = summarizer.summarize(lines)

print summary
