import csv
from validate_email import validate_email

# create new file for validated email address

output_header = ['client_id','email','phone','first_name','last_name','name','country_code','city','is_valid']

def write_output(row_data):
    with open('edited_email_list.csv', mode='a') as output_csv:
        output_csv_writer = csv.writer(output_csv, delimiter=',')
        output_csv_writer.writerow(row_data)

write_output(output_header)

with open('test_email.csv') as email_list_csv:
    email_list = csv.reader(email_list_csv, delimiter=',')

    next(email_list) #skip csv header

    for row in email_list:
        is_valid = validate_email(email_address=row[1])
        
        if is_valid == True:
            validated_email = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],str(is_valid)]
            write_output(validated_email)
            # print(validated_email)
