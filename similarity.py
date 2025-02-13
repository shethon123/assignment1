# -------------------------------------------------------------------------
# AUTHOR: Sheldin Lau
# FILENAME: similarity.py
# SPECIFICATION: Building Document-Term Matrix and using Cosine Similarity for Document Similarity
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: 5 Hours
# -----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy,
#pandas, or other sklearn modules.
#You have to work here only with standard dictionaries, lists, and arrays

# Importing some Python libraries
import csv
from sklearn.metrics.pairwise import cosine_similarity
documents = []

#reading the documents in a csv file
with open('cleaned_documents.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         documents.append (row)
         print(row)

#Building the document-term matrix by using binary encoding.
#You must identify each distinct word in the collection without applying any transformations, using
# the spaces as your character delimiter.
#--> add your Python code here
docTermMatrix = []
for i in range(len(documents)):
  docTermMatrix.append([])

# gets all the words for the matrix
all_words = {}
for i in range(len(documents)):
  document = documents[i][1]
  splitspaced = document.split(" ")
  for word in splitspaced:
    if(all_words.get(word) == None):
      all_words[word] = 1

# uses all the words to fill a dictionary with the binary encoding
document_matrix = []
for i in range(len(documents)):
  splitspaced = documents[i][1].split(" ")
  all_words = dict.fromkeys(all_words,0)
  for word in splitspaced:
    if (all_words.get(word) != None):
      all_words[word] = 1
  document_matrix.append(all_words)

# convert to a list containing only binary encoding
for i in range(len(documents)):
  docTermMatrix[i] = list(document_matrix[i].values())


# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# --> Add your Python code here
highestcosine = 0
doc1 = 0
doc2 = 1
cosinesimilarity = cosine_similarity(docTermMatrix)

for i in range(len(documents)):
  for j in range(len(documents)):
    if i == j:
      continue
    else:
      if cosinesimilarity[i][j] > highestcosine:
        doc1 = i+1
        doc2 = j+1
        highestcosine = cosinesimilarity[i][j]

# Print the highest cosine similarity following the information below
# The most similar documents are document 10 and document 100 with cosine similarity = x
# --> Add your Python code here

print("The most similar documents are document " + str(doc1) + " and document " + str(doc2) + " with cosine similarity = " + str(highestcosine))
