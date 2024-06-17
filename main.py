import s3_operations
import file_operations

s3_operations.download_file_from_bucket('arek-s3-new-bucket', 'excel_test.xlsx')

file_operations.read_from_xlsx('excel_test.xlsx')

#file_operations.add_to_file('script_test.txt', 'First message to add')

file_operations.add_line_to_xlsx('excel_test.xlsx', ['Robert', 'Lewandolski'])

s3_operations.upload_file_to_bucket('arek-s3-new-bucket', 'excel_test.xlsx')

file_operations.remove_file('excel_test.xlsx')

#s3_operations.download_file_from_bucket('arek-s3-new-bucket', 'script_test.txt')



