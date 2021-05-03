# number of files to create
numFiles = 3

# run the file creator
python Par_file_creator.py -numFiles 3 


# replace the model geometry in the original par file with content from geometry txt files
# inserts contents of Model_Geometry* in the desired location in Par_file*
sed -i -e '/#geometry:/r Model_Geometry0.txt' Par_file0.txt
