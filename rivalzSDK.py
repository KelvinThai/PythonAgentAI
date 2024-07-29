from rivalz_client.client import RivalzClient
import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader
# Initialize the client
client = RivalzClient('eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IjY2MGE4OTY1ZGQzYmJhZDUyNzIyYjM2NyIsImF1dGhUeXBlIjoiaXBmcy1zZWNyZXQtYXBpLWtleSIsImlhdCI6MTcyMTExMzM3MywiZXhwIjoxNzUyNjcwOTczfQ.T5UQdvTrdsgRgg5ppPlTnCPRBIoeus2I43FWQ2CkpZo')

def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index

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
        file_path= hash+filename

        content_bytes = bytearray(file)
        imute_byte=bytes(content_bytes)
        f = open(file_path, "wb")
        f.write(imute_byte)
        f.close()

        data_pdf = PDFReader().load_data(file=file_path)
        print(data_pdf)
        pdf_index = get_index(data_pdf, hash)
        
        return pdf_index
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

pdf_index = readFromHash('d79cf77ddf567af85bc99b8be28a22dcf0eda64a9560d528e39dfafdff492765')
pdf_engine = pdf_index.as_query_engine()