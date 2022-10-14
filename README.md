# Servier drug analysis test : 

## how to run the solution :

In order to run the solution we need to install at first the requirements 
```
pip install -r requirements.txt
```

The main script will require 5 inputs :
- drug file path
- first pubmed file path
- second pubmed file path
- clinical trial file path
- file path of the output json

The following command line will run the program
```
python ./servier_drugs_journals_pipeline/main.py servier_drugs_journals_pipeline/data/drugs.csv servier_drugs_journals_pipeline/data/pubmed.csv servier_drugs_journals_pipeline/data/pubmed.json servier_drugs_journals_pipeline/data/clinical_trials.csv servier_drugs_journals_pipeline/data/output_graph.json

```

## Solution enhancements :

- write the tests for each module
- create docker image in order deploy it or wrap it with an api to expose it as a serverless service

## Questions : 

- What are the considerations for scaling your code so that it can handle large
data volumes (files of several TB or millions of files for example)? 
Could you describe what changes, if any, should be made to take into account
such volumes?

This solution uses basic python libraries, and it will lead to resources mismanagement if this
solution will deal with high data volumes. In order to avoid the memory errors and to make the program
run faster. We will need to adapt the code to that by using big data solution such as pyspark
or we can create an API that uses some cloud providers resources in order to extract load and transform
the data this second method will lead to a full transformation of our code, so we will explore the in the second part
of the question the steps needed in order to update the solution with pyspark.

If we use pyspark we will not need the models anymore that will be replaced by spark structures (dataframes)
and specify their structures. Second update to do is to use spark csv reader instead of the regular readers
in order to efficiently load the data. Last thing to update is the re-write the logic by using 
spark dataframes instead of dicts in order to have better efficiency.


