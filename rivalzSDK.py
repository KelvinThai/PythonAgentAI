from rivalz_client.client import RivalzClient
# Initialize the client
client = RivalzClient('eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IjY2MGE4OTY1ZGQzYmJhZDUyNzIyYjM2NyIsImF1dGhUeXBlIjoiaXBmcy1zZWNyZXQtYXBpLWtleSIsImlhdCI6MTcyMTExMzM3MywiZXhwIjoxNzUyNjcwOTczfQ.T5UQdvTrdsgRgg5ppPlTnCPRBIoeus2I43FWQ2CkpZo')

def initAndupload():
    # Upload a file
    upload_response = client.upload_file('./data/test.pdf')
    return upload_response['uploadHash']

# # Upload a passport image
# passport_response = client.upload_passport('path/to/your/passport_image.jpg')
# print(f"Uploaded Passport Response: {passport_response}")

# Download a file
def readFromHash(hash):
        # Download the file
    try:
        file,filename = client.download(hash)
        content_bytes = bytearray(file)
        imute_byte=bytes(content_bytes)
        f = open(hash+filename, "wb")
        f.write(imute_byte)
        f.close()
        return file,filename
    except Exception as e:
        print(f"An error occurred during file download: {e}")
    
# Delete a file
# delete_response = client.delete_file('QmSampleHash')
# print(f"Delete File Response: {delete_response}")

# initAndupload()
# readFromHash('bcc157cfb58c75a39ca7a125a4f20ecd690cc9309e44adab6173973f3e5309e4')
hash=''
while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    if prompt=='upload':
        hash = initAndupload()
        print(hash)
    if prompt=='download':
        result = readFromHash(hash)
        
        print(result)

# readFromHash('bcc157cfb58c75a39ca7a125a4f20ecd690cc9309e44adab6173973f3e5309e4')