import tabula

pdf_path = "sample.pdf"

#list of dataframes dfs AND to extact single table frm pdf

#dfs = tabula.read_pdf(pdf_path, pages='1')
#to get the length
#print(len(dfs))
#to get table
#print(dfs[0])
#csv file
#dfs[0].to_csv("first_table.csv")
#or we can do this
#tabula.convert_into(pdf_path, "first_table2.csv", output_format="csv", pages='1')

#extract multiple tables from 1 page 
#dfs = tabula.read_pdf(pdf_path, pages='2')
#to get the length
#print(len(dfs))
#for i in range (len(dfs)):
    #dfs[i].to_csv(f"page_2_table{i}.csv")

#extract all tables fr pdf file

dfs = tabula.read_pdf(pdf_path, pages='all')
#to get the length
print(len(dfs))
for i in range (len(dfs)):
    dfs[i].to_csv(f"all_pages_table{i}.csv")



