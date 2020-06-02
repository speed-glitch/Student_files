### Student_files

This code is the solution to the following problem:

1.      Multiple entries exists in student.txt file for different subject fields as Rollno, StudName, Subject, Marks for each student. e.g
<Rollno>,<StudName>,<Marks>,<Subject>
101,Santosh , maths, 35
102, Hina, English, 41
101,Santosh , Hindi, 30

2.      Merge the student.txt data as per the template file (tempstud.txt) below for each student. The total for each student should be displayed below at end of record.
Template:
{Id:<Rollno>, Name:<StudName>,subject:<Subject>,marks:<Marks>}
e.g
Santosh.101.txt
{Id: 101,name:Santosh , Subject: maths, Marks:35}
{Id: 101,name:Santosh , Subject: Hindi, Marks:30}
                                                            Total : 65

3.      Create different files for each student , filename of this output file should be <Name>.<rollno>.txt

Note:
Supposing I am changing the template file as below 
{ marks:<Marks>-Id#<Rollno>-Name:<StudName>-subject#<Subject>}

I can also make changes to data files as below(changing column fields )
               <Subject>,<RollNo>,<StudName>,<Marks>
maths,101,Santosh , 35
English,102, Hina, , 41
Hindi, 101,Santosh , 30
 
###Any suggestions to improve the code are always welcomed!
