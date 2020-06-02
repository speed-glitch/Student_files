### Student_files

This code is the solution to the following problem:

1)Multiple entries exists in student.txt file for different subject fields as Rollno, StudName, Subject, Marks for each student.
e.g.,  \newline
\<Rollno\>,\<StudName\>,\<Marks\>,\<Subject\>  \newline
101,Santosh , maths, 35  \newline
102, Hina, English, 41  \newline
101,Santosh , Hindi, 30  \newline

2)Merge the student.txt data as per the template file (tempstud.txt) below for each student. The total for each student should be displayed below at end of record.  \newline
Template:  \newline
{Id:\<Rollno\>, Name:\<StudName\>,subject:\<Subject\>,marks:\<Marks\>}  \newline
e.g  \newline
Santosh.101.txt  \newline
{Id: 101,name:Santosh , Subject: maths, Marks:35}  \newline
{Id: 101,name:Santosh , Subject: Hindi, Marks:30}  \newline
                                                            Total : 65

3)Create different files for each student , filename of this output file should be \<Name\>.\<rollno\>.txt

Note:  \newline
Supposing I am changing the template file as below  \newline
{ marks:\<Marks\>-Id#\<Rollno\>-Name:\<StudName\>-subject#\<Subject\>}  \newline

I can also make changes to data files as below(changing column fields )  \newline
               \<Subject\>,\<RollNo\>,\<StudName\>,\<Marks\>  \newline
maths,101,Santosh , 35  \newline
English,102, Hina, , 41  \newline
Hindi, 101,Santosh , 30  \newline
 
### Any suggestions to improve the code are always welcomed!
