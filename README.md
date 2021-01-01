# Key-Value-DB
A Small JSON Formatted Key Value DB

Basically has 4 options!
*ADD key-value pair to DB

*RETRIVE value for the key

*DELETE key-value

*SHOW DB and Exit


Sample Outputs:
To add:
	Welcome to KeyValue Miniature DB
	Enter your Options!
	1 Add a new KeyValue 
	2 Get the Value for the Key 
	3 Del a value for the Key 
	4 Show DB and exit 
	Enter Your Option : 1


	enter the key : Key1
	enter the value : Value1

	Key value Successfully added!


	Welcome to KeyValue Miniature DB
	Enter your Options!
	1 Add a new KeyValue 
	2 Get the Value for the Key 
	3 Del a value for the Key 
	4 Show DB and exit 
	Enter Your Option : 1


	enter the key : Key2
	enter the value : Value2

	Key value Successfully added!
	

	Welcome to KeyValue Miniature DB
	Enter your Options!
	1 Add a new KeyValue 
	2 Get the Value for the Key 
	3 Del a value for the Key 
	4 Show DB and exit 
	Enter Your Option : 1


	enter the key : Hello
	enter the value : World

	Key value Successfully added!


	Welcome to KeyValue Miniature DB
	Enter your Options!
	1 Add a new KeyValue 
	2 Get the Value for the Key 
	3 Del a value for the Key 
	4 Show DB and exit 
	Enter Your Option : 1


	enter the key : Daenerys
	enter the value : Queen Daenerys I Targaryen, also known as Daenerys Stormborn, and colloquially known as Dany, was the younger sister of Rhaegar Targaryen and Viserys Targaryen and only daughter of King Aerys II Targaryen and Queen Rhaella Targaryen, who were both ousted from the Iron Throne during Robert's Rebellion. She also served a brief tenure as the de facto Queen of the Andals and the First Men and the twenty-first ruler of the Seven Kingdoms, after claiming the throne from her predecessor Cersei I Lannister, who was killed in the Battle of King's Landing. However, she was never formally crowned, nor did she sit upon the Iron Throne.

	Key value Successfully added!

To Retrieve:
	Welcome to KeyValue Miniature DB
	Enter your Options!
	1 Add a new KeyValue 
	2 Get the Value for the Key 
	3 Del a value for the Key 
	4 Show DB and exit 
	Enter Your Option : 2


	enter the key : key1
	Key not present 

	Welcome to KeyValue Miniature DB
	Enter your Options!
	1 Add a new KeyValue 
	2 Get the Value for the Key 
	3 Del a value for the Key 
	4 Show DB and exit 
	Enter Your Option : 2


	enter the key : Key1
	Value1

To Delete:

	Welcome to KeyValue Miniature DB
	Enter your Options!
	1 Add a new KeyValue 
	2 Get the Value for the Key 
	3 Del a value for the Key 
	4 Show DB and exit 
	Enter Your Option : 3


	enter the key : Key2
	Key Deleted successfully

	The Updated DB is

	{
	  "Key1": "Value1",
	  "Hello": "World",
	  "Daenerys": "Queen Daenerys I Targaryen, also known as Daenerys Stormborn, and colloquially known as Dany, was the younger sister of 			       Rhaegar Targaryen and Viserys Targaryen and only daughter of King Aerys II Targaryen and Queen Rhaella Targaryen, who were 			       both ousted from the Iron Throne during Robert's Rebellion. She also served a brief tenure as the de facto Queen of the 			       Andals and the First Men and the twenty-first ruler of the Seven Kingdoms, after claiming the throne from her predecessor 			       Cersei I Lannister, who was killed in the Battle of King's Landing. However, she was never formally crowned, nor did she 	               sit upon the Iron Throne."
	}

Error Handled:

	Welcome to KeyValue Miniature DB
	Enter your Options!
	1 Add a new KeyValue 
	2 Get the Value for the Key 
	3 Del a value for the Key 
	4 Show DB and exit 
	Enter Your Option : 1


	enter the key : Daenerys Stormborn of House Targaryen, the First of Her Name, Queen of the Andals and the First Men, Protector of the 				Seven Kingdoms
	Enter a Valid key which is a string with 32 chars


	And So On!!

