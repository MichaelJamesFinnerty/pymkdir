# pymkdir <h3> (say it like "piemaker") </h3>
###### A lightweight tool for directly generating complex folder and file structures in python


#### Provide strings and get populated folder structures
```
pymkdir.main("[spam/{eggs.py}]")

Folder name:	/path/to/active/dir
	Subfolders:
		Folder name:	spam
			Files:
			eggs.py
```


#### Use injectors (% with +example)
```
pymkdir.main("[spam/{%.py, %_and_spam.js}+eggs]")

Folder name:	/path/to/active/dir
	Subfolders:
		Folder name:	spam
			Files:
			eggs.py
      			eggs_and_spam.js
```


#### Use iterators ($ with *n)
```
pymkdir.main("[spam/{eggs_$.py}*3]")

Folder name:	/path/to/active/dir
	Subfolders:
		Folder name:	spam
			Files:
			eggs_1.py
			eggs_2.py
			eggs_3.py
```


#### Apply file extensions (.example)
```
pymkdir.main("[spam/{eggs, spam_and_eggs}.py]")

Folder name:	/path/to/active/dir
	Subfolders:
		Folder name:	spam
			Files:
			eggs.py
			spam_and_eggs.py
```


#### Create groupings for uniform handling with parenthesis
```
pymkdir.main("[spam/{(eggs, spam).js, index.html}]")

Folder name:	/path/to/active/dir
	Subfolders:
		Folder name:	spam
			Files:
			eggs.js
			spam.js
			index.html
```


#### Nest groupings
```
pymkdir.main("[ spam/{ ( %.html, ( %, %_and_eggs ).js )+spam } ]")
```

#### Nest folders
```
```


#### Nest folders in groups


#### Nest groups in folders


#### Combine to create complex folder structures
```
[folder/{
    index.html, 
    js/{(main, log).js}, 
    styles/{style$}.css*4, 
    data/{
        201$/{
            Q$/{}
        }*4
    }*7}
]



Folder name:	/path/to/active/dir
	Subfolders:
		Folder name:	folder
			Files:
			index.html

			Subfolders:
				Folder name:	js
					Files:
					main.js
					log.js

				Folder name:	styles
					Files:
					style1.css
					style2.css
					style3.css
					style4.css

				Folder name:	data
					Subfolders:
						Folder name:	2011
							Subfolders:
								Folder name:	Q1
								Folder name:	Q2
								Folder name:	Q3
								Folder name:	Q4

						Folder name:	2012
							Subfolders:
								Folder name:	Q1
								Folder name:	Q2
								Folder name:	Q3
								Folder name:	Q4

						Folder name:	2013
							Subfolders:
								Folder name:	Q1
								Folder name:	Q2
								Folder name:	Q3
								Folder name:	Q4

						Folder name:	2014
							Subfolders:
								Folder name:	Q1
								Folder name:	Q2
								Folder name:	Q3
								Folder name:	Q4

						Folder name:	2015
							Subfolders:
								Folder name:	Q1
								Folder name:	Q2
								Folder name:	Q3
								Folder name:	Q4

						Folder name:	2016
							Subfolders:
								Folder name:	Q1
								Folder name:	Q2
								Folder name:	Q3
								Folder name:	Q4

						Folder name:	2017
							Subfolders:
								Folder name:	Q1
								Folder name:	Q2
								Folder name:	Q3
								Folder name:	Q4
```
