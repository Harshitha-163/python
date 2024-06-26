d={}
i=0
ent_inp=int(input('Enter #1 to add student\nEnter #2 to search student\nEnter #3 to del student\nEnter 4# to exit\n\nEnter your choice= '))
if ent_inp==1:
    howmany=int(input('How many student detail you want to enter: '))
    
    while i<=howmany:

        d['RollNum']=input('Enter the Roll Num: ')
        d['RollNum']={}
        d['RollNum']['Name']=input('Enter the Name: ')
        d['RollNum']['Marks']={}
        d['RollNum']['Marks']['English']=input('Enter the Marks of English: ')
        d['RollNum']['Marks']['Maths']=input('Enter the Marks of Maths: ')
    
        i=i+1
        continue
    print(d)