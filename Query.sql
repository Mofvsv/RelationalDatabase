# The query below finds the names and birthdates of all the gorillas.
# 
# Modify it to make it find the names of all the animals that are not
# gorillas and not named 'Max'.
QUERY = '''
select name from animals where (not species = 'gorilla') and (not name = 'Max');
select name from animals where not(species ='gorilla' or name='Max');
'''
# Find all the llamas born between January 1, 1995 and December 31, 1998.
# Fill in the 'where' clause in this query.
QUERY = '''
select name from animals where = 'llamas' and and birthday >='1995-1-1' and birthday<='1998-12-31';
'''