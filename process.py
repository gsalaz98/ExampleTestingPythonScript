import os

def asdf():
    print(os.environ['QC_DATAFLEET_DEPLOYMENT_DATE'])
    data = [
        '20200101,1',
        '20200102,2',
        '20200103,3'
    ]

    os.mkdir('/temp-output-directory')
    with open('/temp-output-directory/vendor_example.csv', 'w') as vendor_file:
        vendor_file.write('\n'.join(data))

if __name__ == '__main__':
    asdf()
